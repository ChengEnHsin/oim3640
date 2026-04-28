"""
InternTrack Web Application
Flask-based web interface for the internship tracker
"""

from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os
from datetime import datetime


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


@app.route('/')
def index():
    """Home page - Dashboard with statistics."""
    applications = load_applications()
    stats = calculate_statistics(applications)
    
    # Add color codes to applications for display
    for app in applications:
        app['status_color'] = get_status_color(app['status'])
    
    return render_template('index.html', stats=stats, applications=applications)


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
                         applications=applications)


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
