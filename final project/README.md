InternTrack - Internship & Job Application Tracker

## Project Overview

InternTrack is a Python-based application designed to centralize and analyze internship and job applications. It solves the problem of tracking applications across multiple platforms by providing a single, organized system with built-in analytics.

## MVP Features (Complete)

✅ **Application Management**
- Add new applications with company, role, location, and date
- Update application status through defined workflow
- View all applications in a formatted table
- View detailed information for specific applications
- Delete applications

✅ **Data Persistence**
- Applications automatically saved to JSON file
- Data persists between program runs
- Clean data structure for future extensions

✅ **Analytics & Statistics**
- Total applications count
- Response rate calculation
- Rejection rate tracking
- Status breakdown
- Applications by location
- Performance metrics at a glance

✅ **User Interface**
- Simple command-line menu interface
- Input validation for dates and selections
- Clear formatted output
- User-friendly prompts

✅ **Web Interface** (Built with Flask & CSS)
- Modern, responsive design
- Beautiful dashboard with metrics
- Easy-to-use forms for adding/editing applications
- Color-coded status badges
- Mobile-friendly layout

## How to Run

### Option 1: Command-Line Interface

```bash
python interntrack.py
```

Then follow the on-screen menu to manage your applications.

### Option 2: Web Interface (Recommended)

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the Flask application:
```bash
python web_app.py
```

3. Open your browser and navigate to:
```
http://localhost:5000
```

Then use the web interface to manage your applications.

## Data Structure

Each application is stored as a dictionary with the following fields:
```python
{
    "id": <unique_id>,
    "company": <string>,
    "role": <string>,
    "date_applied": <YYYY-MM-DD>,
    "location": <string>,
    "status": <string>,
    "date_updated": <YYYY-MM-DD>
}
```

**Valid Statuses:**
- Applied
- Under Review
- Interview Scheduled
- Rejected
- Offer Extended
- Offer Accepted

## Web Interface Features

### Dashboard
- View key metrics at a glance
- See recent applications
- Monitor status breakdown
- Track response and rejection rates

### Applications Page
- View all applications in a sortable table
- Edit application details
- Delete applications
- Status indicators with color coding

### Add/Edit Applications
- Clean form interface
- Easy status updates
- Date picker for application dates

### Statistics Page
- Comprehensive analytics dashboard
- Visual charts and breakdowns
- Location-based analysis
- Key insights and metrics
- Success rate tracking

## Project Structure

```
interntrack/
├── interntrack.py          # CLI version of the application
├── web_app.py              # Flask web application
├── requirements.txt        # Python dependencies
├── README.md               # This file
├── finalproposal.md        # Project proposal
├── AI_USAGE.md            # AI tool documentation
├── .gitignore             # Git ignore file
├── templates/             # HTML templates
│   ├── base.html          # Base template with navigation
│   ├── index.html         # Dashboard
│   ├── applications.html  # All applications view
│   ├── add_application.html
│   ├── edit_application.html
│   └── statistics.html    # Statistics page
├── static/                # Static assets
│   └── style.css          # Stylesheet
└── applications.json      # Data storage (auto-generated)
```

## Stretch Goals for Future Development

📊 **Visualization**
- Timeline of applications over time
- Success rate by role category
- Interactive charts using matplotlib

💾 **Data Export**
- Export to CSV format
- Generate reports

🎯 **Enhanced Analysis**
- Predict which roles lead to more interviews
- Response time analysis
- Priority scoring system
- Deadline tracking

🔧 **Features**
- Edit existing application details
- Search/filter applications
- Import existing applications from CSV

## Learning Outcomes

This project demonstrates:

**Core Python Concepts:**
- **File I/O**: JSON file handling for data persistence
- **Data Structures**: Dictionaries and lists for organizing data
- **Functions**: Modular design with clear separation of concerns
- **Control Flow**: Menu-based user interaction with input validation
- **Error Handling**: Graceful handling of invalid inputs
- **String Formatting**: Clear, organized output presentation
- **Data Analysis**: Statistical calculations and metrics

**Web Development:**
- **Flask Framework**: Building web applications with Python
- **Routing**: URL routing and HTTP methods (GET/POST)
- **Templates**: Using Jinja2 templates for dynamic HTML
- **Forms**: Processing form data and validation
- **CSS**: Creating responsive, modern user interfaces
- **MVC Architecture**: Separation of concerns in web apps
- **RESTful API**: Creating API endpoints for data

**Software Engineering:**
- **Code Organization**: Separating CLI and web interfaces
- **Modularity**: Reusable code across interfaces
- **Responsive Design**: Mobile-friendly web layouts
- **User Experience**: Building intuitive interfaces

# InternTrack — UI Design Drop-in

A simplistic, cream-and-neutral redesign for the InternTrack Flask app, with subtle animation transitions throughout. Templates are wired to match `web_app.py` exactly.

## What's inside

```
interntrack-ui/
├── preview.html              ← open this directly in a browser to see the design
├── static/
│   └── style.css             ← drop into your project's static/ folder
└── templates/
    ├── base.html             ← layout + nav + scripts
    ├── index.html            ← Dashboard
    ├── applications.html     ← All applications table
    ├── add_application.html  ← New application form
    ├── edit_application.html ← Edit application form
    └── statistics.html       ← Statistics page
```

## Preview

Open `preview.html` in your browser — no Flask required. The sidebar links switch between all five views and demo the animations.

## Drop-in to your Flask app

1. Copy `static/style.css` → your `static/` folder (replace existing).
2. Copy everything in `templates/` → your `templates/` folder (replace existing).

That's it — no changes needed in `web_app.py`. The templates use the exact endpoint names and context variables your routes pass.

## Endpoints used

| Template | Endpoint | Method |
|---|---|---|
| `base.html` (nav) | `index`, `view_applications`, `add_application`, `statistics` | GET |
| `index.html` | `view_applications`, `add_application` | GET |
| `applications.html` | `add_application`, `edit_application(app_id)`, `delete_application(app_id)` | GET / POST |
| `add_application.html` | `add_application`, `view_applications` | POST / GET |
| `edit_application.html` | `edit_application(app_id)`, `view_applications` | POST / GET |
| `statistics.html` | (read-only) | GET |

## Context variables (matched to web_app.py)

### `index.html` — `index()` route
```python
render_template('index.html',
    stats=stats,                  # dict — see shape below
    applications=applications,    # list[dict] (each w/ status_color)
    suggested=suggested,          # list[{company, role, location, season}]
    reminders=reminders,          # list[{company, role, date, location}]
    status_colors=status_colors,  # dict {status: hex}
)
```

### `applications.html` — `view_applications()` route
```python
render_template('applications.html', applications=apps_with_colors)
```

### `add_application.html` — `add_application()` route
```python
render_template('add_application.html',
    statuses=VALID_STATUSES,      # list[str]
    error=...,                    # optional, str
)
```

### `edit_application.html` — `edit_application()` route
```python
render_template('edit_application.html',
    application=app_to_edit,      # dict
    statuses=VALID_STATUSES,
)
```

### `statistics.html` — `statistics()` route
```python
render_template('statistics.html',
    stats=stats,
    status_colors=status_colors,
    applications=applications,
)
```

### `stats` dict shape (from `calculate_statistics`)
```python
{
    "total":          int,
    "response_rate":  float,   # 0–100
    "rejection_rate": float,
    "responded":      int,
    "rejections":     int,
    "by_status":      {status_name: count},
    "by_location":    {location_name: count},
}
```

The dashboard derives `active_count` (interviews + offers) from `stats.by_status` and the `recent` list from `applications` sorted by `date_applied` — no extra context needed. The statistics page derives a `success_rate` (offers / total) the same way.

## Design system

| Token | Value | Use |
|---|---|---|
| `--bg` | `#f7f2ea` | warm cream page background |
| `--surface` | `#fdfbf6` | cards, table, forms |
| `--accent` | `#a89478` | warm taupe — bars, focus rings |
| `--accent-deep` | `#6b5d4a` | primary buttons, headings emphasis |
| `--ink` | `#2d2922` | primary text |
| Status pills | muted earth-tones | `pill-applied`, `pill-review`, `pill-interview`, `pill-rejected`, `pill-offer`, `pill-accepted` |

Headings use **Fraunces** (serif), body uses **Inter** (sans). Both load from Google Fonts with `display=swap`.

The CSS pill classes use a hand-tuned muted palette that fits the cream theme. If you'd rather use the bright `status_colors` from `get_status_color()`, swap the `<span class="pill ...">` for an inline-styled badge — but the current muted set looks much calmer.

## Animations

- **Page entrance**: each view fades up in 550ms on load.
- **Stat cards**: rise + stagger (50ms steps).
- **Table rows**: fade in with stagger.
- **Stat numbers**: count up from 0 to target with cubic ease-out.
- **Bar charts**: fill widths animate in over 1s.
- **Hover lifts** on cards and primary buttons.
- **Focus rings** with soft taupe glow on inputs.
- **Brand dot**: gentle pulse.
- **Active nav indicator**: slide-in left bar.
- Respects `prefers-reduced-motion`.