# Render Deployment Guide

## Quick Start

Your InternTrack application is now configured for deployment on Render!

### Service Information
- **Service ID:** `srv-d7gf81pf9bms73atvaj0`
- **Platform:** Render.com
- **Type:** Web Service (Python/Flask)

## Deployment Steps

### 1. Connect Your GitHub Repository

1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click **New +** → **Web Service**
3. Select **Deploy from Git**
4. Connect your GitHub account
5. Select the `oim3640` repository
6. Click **Connect**

### 2. Configure the Web Service

**Basic Settings:**
- **Name:** `interntrack` (or your preferred name)
- **Environment:** Python 3
- **Region:** Oregon (US East, US West, or EU - your choice)
- **Branch:** main (or your branch)
- **Root Directory:** `final project` (set this if needed)

**Build & Deploy:**
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn web_app:app`

### 3. Environment Variables

Set these in the Render dashboard:
- `FLASK_ENV`: `production`
- `PYTHON_VERSION`: `3.11.0`

### 4. Deploy

1. Click **Deploy**
2. Render will automatically:
   - Install dependencies from `requirements.txt`
   - Build the application
   - Start the Flask server with Gunicorn
3. Your app will be live at: `https://interntrack.onrender.com` (or similar)

## Files Created for Render

### `render.yaml`
Configuration file that tells Render how to build and run the application.

### `Procfile`
Alternative configuration file (Render supports both).

### `.render-buildignore`
Tells Render which files to exclude from the deployment.

### Updated `requirements.txt`
Added `gunicorn==20.1.0` for production server.

### Updated `web_app.py`
Modified to:
- Read PORT from environment variables (Render assigns this)
- Run on `0.0.0.0` (required for Render)
- Use production settings

## Production Configuration

The application now runs in production mode with:

✅ **Gunicorn Server** - Production-grade WSGI server  
✅ **Environment-based Settings** - Uses `FLASK_ENV` variable  
✅ **Port Flexibility** - Reads PORT from environment  
✅ **Host Configuration** - Binds to `0.0.0.0` for deployment  

## Data Persistence

The `applications.json` file will be stored in Render's ephemeral filesystem. This means:

**⚠️ Important:** 
- Data will persist during your service's uptime
- Data will be lost if your service restarts or redeploys
- For persistent data, you should upgrade to paid tier with persistent disk, or use a database

### To Keep Data Persistent:

1. **Option 1: Upgrade to Paid Tier with Persistent Disk**
   - In Render dashboard → Web Service → Settings → Add Disk
   - Mount at `/var/data` and update `DATA_FILE` path

2. **Option 2: Use a Database (Recommended for Production)**
   - Set up PostgreSQL on Render
   - Update `web_app.py` to use database instead of JSON file

## Monitoring & Logs

Check your deployment status:
1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click on your service: `interntrack`
3. View **Logs** tab for debugging
4. Check **Metrics** tab for performance

## Local Testing Before Deployment

Test the production configuration locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Test with Gunicorn (like Render uses)
gunicorn web_app:app --bind 0.0.0.0:5000

# Then visit: http://localhost:5000
```

## Troubleshooting

### Build Failed
- Check logs in Render dashboard
- Ensure all imports in `web_app.py` are in `requirements.txt`
- Verify `render.yaml` syntax is correct

### Application Won't Start
- Check "Start Command" is: `gunicorn web_app:app`
- Verify PORT environment variable is being read
- Check logs for Python errors

### Data Not Persisting
- This is expected with free tier (ephemeral filesystem)
- Add persistent disk or upgrade to paid tier
- Or switch to database solution

### Port Issues
- Don't hardcode port like `5000`
- Use: `int(os.environ.get('PORT', 5000))`
- Bind to `0.0.0.0` not `127.0.0.1`

## Deployment Checklist

- [ ] Files committed to GitHub
- [ ] `requirements.txt` updated with exact versions
- [ ] `web_app.py` reads `PORT` environment variable
- [ ] `render.yaml` or `Procfile` present
- [ ] GitHub repository connected to Render
- [ ] Web Service created with build/start commands
- [ ] Environment variables set in Render dashboard
- [ ] Deploy button clicked
- [ ] Logs show successful build
- [ ] Website accessible at Render URL

## Next Steps

1. **Deploy Now:** Go to Render and connect your repo
2. **Set Up Domain:** Add custom domain in Render settings
3. **Monitor:** Check logs regularly for errors
4. **Upgrade:** Consider paid tier for persistent storage
5. **Database:** Switch to PostgreSQL for production data

## Support Links

- [Render Documentation](https://render.com/docs)
- [Python on Render](https://render.com/docs/deploy-python)
- [Flask Deployment](https://render.com/docs/deploy-flask)
- [Render Dashboard](https://dashboard.render.com)

## Command Reference

**Build:** `pip install -r requirements.txt`  
**Start:** `gunicorn web_app:app`  
**Logs:** View in Render dashboard  
**Redeploy:** Push to GitHub (auto-deploys) or use dashboard  

---

Your service ID is: `srv-d7gf81pf9bms73atvaj0`

For help, visit the [Render Community](https://render.com/community) or check the docs!
