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
