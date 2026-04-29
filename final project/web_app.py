"""
InternTrack Web Application
Flask-based web interface for the internship tracker
"""

from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os
import re
from datetime import datetime
import openai

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

openai.api_key = os.environ.get('GPT_KEY', '')
app = Flask(__name__)

# Configuration for production
app.config['ENV'] = os.environ.get('FLASK_ENV', 'development')
DEBUG = app.config['ENV'] == 'development'

# File for persistent data storage
DATA_FILE = "applications.json"
VALID_STATUSES = ["Applied", "Under Review", "Interview Scheduled", "Rejected", "Offer Extended", "Offer Accepted"]


def load_applications():
    """Load applications from JSON file."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []
    return []


def save_applications(applications):
    """Save applications to JSON file."""
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(applications, f, indent=2)
        return True
    except IOError:
        return False


def calculate_statistics(applications):
    """Calculate statistics from applications."""
    if not applications:
        return {
            "total": 0,
            "response_rate": 0,
            "rejection_rate": 0,
            "by_status": {},
            "by_location": {}
        }
    
    total = len(applications)
    responded = sum(1 for app in applications if app['status'] in 
                   ["Under Review", "Interview Scheduled", "Offer Extended", "Offer Accepted"])
    rejections = sum(1 for app in applications if app['status'] == "Rejected")
    
    status_counts = {}
    for app in applications:
        status = app['status']
        status_counts[status] = status_counts.get(status, 0) + 1
    
    location_counts = {}
    for app in applications:
        loc = app['location']
        location_counts[loc] = location_counts.get(loc, 0) + 1
    
    return {
        "total": total,
        "response_rate": round((responded / total * 100) if total > 0 else 0, 1),
        "rejection_rate": round((rejections / total * 100) if total > 0 else 0, 1),
        "responded": responded,
        "rejections": rejections,
        "by_status": status_counts,
        "by_location": location_counts
    }


def get_suggested_internships():
    """Get list of suggested internships to apply to."""
    return [
        {
            "company": "Google",
            "role": "Software Engineer Intern",
            "location": "Mountain View, CA",
            "season": "Summer 2026",
            "job_url": "https://careers.google.com/jobs/results/"
        },
        {
            "company": "Microsoft",
            "role": "Internship Program - Tech",
            "location": "Redmond, WA",
            "season": "Summer 2026",
            "job_url": "https://careers.microsoft.com/us/en"
        },
        {
            "company": "Amazon",
            "role": "Software Development Engineer Intern",
            "location": "Seattle, WA",
            "season": "Summer 2026",
            "job_url": "https://www.amazon.jobs/en/"
        },
        {
            "company": "Apple",
            "role": "Software Engineering Internship",
            "location": "Cupertino, CA",
            "season": "Summer 2026",
            "job_url": "https://www.apple.com/careers/"
        },
        {
            "company": "Meta",
            "role": "Engineering Internship",
            "location": "Menlo Park, CA",
            "season": "Summer 2026",
            "job_url": "https://www.metacareers.com/"
        },
        {
            "company": "Goldman Sachs",
            "role": "Summer Internship Program",
            "location": "New York, NY",
            "season": "Summer 2026",
            "job_url": "https://www.goldmansachs.com/careers/"
        },
        {
            "company": "JP Morgan",
            "role": "Summer Analyst Program",
            "location": "New York, NY",
            "season": "Summer 2026",
            "job_url": "https://careers.jpmorgan.com/us/en/home"
        },
        {
            "company": "Tesla",
            "role": "Engineering Internship",
            "location": "Palo Alto, CA",
            "season": "Summer 2026",
            "job_url": "https://www.tesla.com/careers"
        },
        {
            "company": "Stripe",
            "role": "Software Engineering Internship",
            "location": "San Francisco, CA",
            "season": "Summer 2026",
            "job_url": "https://stripe.com/jobs"
        },
    ]


def get_upcoming_interview_reminders(applications):
    """Extract upcoming interview reminders from applications."""
    return [
        {
            "company": app.get("company", "Unknown"),
            "role": app.get("role", "Interview"),
            "date": app.get("date_updated", "TBD"),
            "location": app.get("location", "Remote"),
        }
        for app in applications
        if app.get("status") == "Interview Scheduled"
    ]


def build_recommendation_prompt(applications, focus):
    """Create a prompt for GPT based on current application history."""
    if applications:
        companies = sorted({app.get('company', 'Unknown') for app in applications if app.get('company')})
        roles = sorted({app.get('role', 'Unknown') for app in applications if app.get('role')})
        locations = sorted({app.get('location', 'Not specified') for app in applications if app.get('location')})
        recent_status = [app.get('status') for app in applications if app.get('status')]
    else:
        companies = []
        roles = []
        locations = []
        recent_status = []

    prompt = [
        {
            "role": "system",
            "content": "You are a helpful career advisor for an internship seeker."
        },
        {
            "role": "user",
            "content": (
                "Based on the current internship application history, offer concise recommendations "
                "for future internships, companies to target, fields to explore, and roles to pursue. "
                "Mention opportunities that align with the user's existing experience and application pattern. "
                "Use plain language and a positive, practical tone."
            )
        }
    ]

    details = []
    if companies:
        details.append(f"Current companies applied to: {', '.join(companies)}.")
    if roles:
        details.append(f"Roles applied for include: {', '.join(roles)}.")
    if locations:
        details.append(f"Locations include: {', '.join(locations)}.")
    if recent_status:
        details.append(f"Current statuses include: {', '.join(sorted(set(recent_status)))}.")

    if details:
        prompt.append({"role": "user", "content": ' '.join(details)})

    if focus:
        prompt.append({"role": "user", "content": f"Please tailor the advice to: {focus}."})
    else:
        prompt.append({"role": "user", "content": "Please give general guidance for which internships, companies, fields, and roles to aim for next."})

    return prompt


def ask_gpt_recommendations(applications, focus):
    """Call OpenAI to generate personalized internship recommendations."""
    if not openai.api_key:
        return None, "GPT_KEY is not configured in the environment."

    prompt = build_recommendation_prompt(applications, focus)
    try:
        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=prompt,
            temperature=0.8,
            max_tokens=400,
        )
        return completion.choices[0].message.content.strip(), None
    except Exception as exc:
        return None, f"GPT recommendation failed: {str(exc)}"


def extract_json_array(text):
    """Extract the first JSON array from a GPT response."""
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\n|```$", "", text, flags=re.I).strip()
    start = text.find("[")
    end = text.rfind("]")
    if start == -1 or end == -1:
        return None
    return text[start:end + 1]


def build_internship_generation_prompt(applications):
    """Build a GPT prompt for current internship listings."""
    companies = sorted({app.get("company", "Unknown") for app in applications if app.get("company")})
    prompt = [
        {
            "role": "system",
            "content": "You are a helpful internship search assistant."
        },
        {
            "role": "user",
            "content": (
                "Provide a JSON array of 5 current internship opportunities available "
                "on major job platforms and company career sites. "
                "Each item should include company, role, location, season, and job_url. "
                "Do not include any extra text outside the JSON array."
            )
        }
    ]
    if companies:
        prompt.append({
            "role": "user",
            "content": f"The user has already applied to: {', '.join(companies)}. Please suggest fresh opportunities that are not duplicate applications."
        })
    return prompt


def generate_more_internships(applications):
    """Generate more suggested internships using GPT."""
    if not openai.api_key:
        return None, "GPT_KEY is not configured in the environment."

    prompt = build_internship_generation_prompt(applications)
    try:
        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=prompt,
            temperature=0.8,
            max_tokens=400,
        )
        content = completion.choices[0].message.content.strip()
        json_text = extract_json_array(content)
        if not json_text:
            return None, "GPT response did not contain a JSON array."

        suggestions = json.loads(json_text)
        if not isinstance(suggestions, list):
            return None, "GPT returned invalid internship data."

        return suggestions, None
    except Exception as exc:
        return None, f"GPT internship generation failed: {str(exc)}"


@app.route('/')
def index():
    """Home page - Dashboard with statistics."""
    applications = load_applications()
    stats = calculate_statistics(applications)
    
    # Add color codes to applications for display
    for app in applications:
        app['status_color'] = get_status_color(app['status'])
    
    # Get suggested internships
    suggested = get_suggested_internships()
    reminders = get_upcoming_interview_reminders(applications)

    # Build status color mapping for dashboard progress bars
    status_colors = {status: get_status_color(status) for status in stats.get('by_status', {}).keys()}
    
    return render_template(
        'index.html',
        stats=stats,
        applications=applications,
        suggested=suggested,
        reminders=reminders,
        status_colors=status_colors,
        generated_error=None,
        generated_notice=None,
        gpt_key_available=bool(openai.api_key),
    )


@app.route('/generate_internships', methods=['POST'])
def generate_internships():
    applications = load_applications()
    stats = calculate_statistics(applications)
    for app in applications:
        app['status_color'] = get_status_color(app['status'])

    suggested, error = generate_more_internships(applications)
    if not suggested:
        suggested = get_suggested_internships()

    reminders = get_upcoming_interview_reminders(applications)
    status_colors = {status: get_status_color(status) for status in stats.get('by_status', {}).keys()}

    return render_template(
        'index.html',
        stats=stats,
        applications=applications,
        suggested=suggested,
        reminders=reminders,
        status_colors=status_colors,
        generated_error=error,
        generated_notice=(None if error else 'Generated current internship opportunities.'),
        gpt_key_available=bool(openai.api_key),
    )


@app.route('/applications')
def view_applications():
    """View all applications."""
    applications = load_applications()
    apps_with_colors = []
    for app in applications:
        color = get_status_color(app['status'])
        apps_with_colors.append({**app, 'status_color': color})
    return render_template('applications.html', applications=apps_with_colors)


@app.route('/add', methods=['GET', 'POST'])
def add_application():
    """Add a new application."""
    if request.method == 'POST':
        applications = load_applications()
        
        company = request.form.get('company', '').strip()
        role = request.form.get('role', '').strip()
        location = request.form.get('location', '').strip() or "Not specified"
        date_applied = request.form.get('date_applied', '').strip()
        
        if not date_applied:
            date_applied = datetime.now().strftime("%Y-%m-%d")
        
        if not company or not role:
            return render_template('add_application.html', 
                                 statuses=VALID_STATUSES,
                                 error="Company and role are required!")
        
        new_app = {
            "id": len(applications) + 1,
            "company": company,
            "role": role,
            "date_applied": date_applied,
            "location": location,
            "status": "Applied",
            "date_updated": datetime.now().strftime("%Y-%m-%d")
        }
        
        applications.append(new_app)
        save_applications(applications)
        
        return redirect(url_for('view_applications'))
    
    return render_template('add_application.html', statuses=VALID_STATUSES)


@app.route('/edit/<int:app_id>', methods=['GET', 'POST'])
def edit_application(app_id):
    """Edit an application."""
    applications = load_applications()
    app_to_edit = next((a for a in applications if a['id'] == app_id), None)
    
    if not app_to_edit:
        return redirect(url_for('view_applications'))
    
    if request.method == 'POST':
        app_to_edit['company'] = request.form.get('company', app_to_edit['company']).strip()
        app_to_edit['role'] = request.form.get('role', app_to_edit['role']).strip()
        app_to_edit['location'] = request.form.get('location', app_to_edit['location']).strip()
        app_to_edit['status'] = request.form.get('status', app_to_edit['status'])
        app_to_edit['date_applied'] = request.form.get('date_applied', app_to_edit['date_applied'])
        app_to_edit['date_updated'] = datetime.now().strftime("%Y-%m-%d")
        
        save_applications(applications)
        return redirect(url_for('view_applications'))
    
    return render_template('edit_application.html', 
                         application=app_to_edit, 
                         statuses=VALID_STATUSES)


@app.route('/delete/<int:app_id>', methods=['POST'])
def delete_application(app_id):
    """Delete an application."""
    applications = load_applications()
    applications = [a for a in applications if a['id'] != app_id]
    save_applications(applications)
    return redirect(url_for('view_applications'))


@app.route('/statistics')
def statistics():
    """View statistics page."""
    applications = load_applications()
    stats = calculate_statistics(applications)
    
    # Add colors for each status
    status_colors = {}
    for status in stats.get('by_status', {}).keys():
        status_colors[status] = get_status_color(status)
    
    return render_template('statistics.html', stats=stats,
                         status_colors=status_colors,
                         applications=applications,
                         recommendation=None,
                         recommendation_error=None,
                         prompt_focus='')


@app.route('/recommendations', methods=['POST'])
def recommendations():
    """Generate GPT-driven internship recommendations."""
    focus = request.form.get('focus', '').strip()
    applications = load_applications()
    stats = calculate_statistics(applications)
    status_colors = {status: get_status_color(status) for status in stats.get('by_status', {}).keys()}

    recommendation, error = ask_gpt_recommendations(applications, focus)

    return render_template('statistics.html', stats=stats,
                         status_colors=status_colors,
                         applications=applications,
                         recommendation=recommendation,
                         recommendation_error=error,
                         prompt_focus=focus)


@app.route('/api/status-breakdown')
def api_status_breakdown():
    """API endpoint for status breakdown data."""
    applications = load_applications()
    stats = calculate_statistics(applications)
    return jsonify(stats['by_status'])


def get_status_color(status):
    """Get color for status badge."""
    colors = {
        "Applied": "#3498db",
        "Under Review": "#f39c12",
        "Interview Scheduled": "#9b59b6",
        "Rejected": "#e74c3c",
        "Offer Extended": "#27ae60",
        "Offer Accepted": "#16a085"
    }
    return colors.get(status, "#95a5a6")


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=DEBUG)
