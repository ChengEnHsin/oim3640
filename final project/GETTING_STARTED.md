# Getting Started with InternTrack

## Quick Start (Web Version - Recommended)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Application
```bash
python web_app.py
```

### 3. Open in Browser
Visit: **http://localhost:5000**

## Features

### Dashboard
- View key metrics (total applications, response rate, rejection rate)
- See recent applications
- Monitor status distribution

### Applications
- View all applications in a table
- Edit application details
- Update application status
- Delete applications

### Add Application
- Simple form to add new applications
- Automatically uses today's date if not specified
- Default status is "Applied"

### Statistics
- Comprehensive analytics dashboard
- Response rate and rejection rate
- Status breakdown with visual charts
- Applications by location
- Key insights and next steps

## Data

All applications are stored in `applications.json` file. This file is:
- Automatically created on first use
- Shared between CLI and web interfaces
- Human-readable JSON format

## CLI Version (Alternative)

If you prefer command-line interface:
```bash
python interntrack.py
```

## Troubleshooting

### Port Already in Use
If port 5000 is already in use, modify web_app.py:
```python
app.run(debug=True, port=5001)  # Use different port
```

### No Applications Showing
Make sure `applications.json` exists in the same directory as the scripts, or add your first application through the web interface.

### Browser Won't Connect
- Check that Flask is running (terminal should show "Running on http://localhost:5000")
- Try refreshing the page
- Make sure Flask was installed correctly

## Next Steps

- Add your internship applications
- Track status updates
- Check statistics to analyze your recruiting progress
- Export data or set up additional tracking features

For more information, see [README.md](README.md) and [AI_USAGE.md](AI_USAGE.md).
