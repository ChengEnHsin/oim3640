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

## How to Run

```bash
python interntrack.py
```

Then follow the on-screen menu to manage your applications.

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
- **File I/O**: JSON file handling for data persistence
- **Data Structures**: Dictionaries and lists for organizing data
- **Functions**: Modular design with clear separation of concerns
- **Control Flow**: Menu-based user interaction with input validation
- **Error Handling**: Graceful handling of invalid inputs
- **String Formatting**: Clear, organized output presentation
- **Data Analysis**: Statistical calculations and metrics
