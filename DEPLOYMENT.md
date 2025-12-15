# 🚀 Deployment Guide

This guide covers deploying ProjectHack to various platforms. Choose the one that best fits your needs.

## 📋 Pre-Deployment Checklist

Before deploying, make sure:
- ✅ All migrations are created
- ✅ Static files are collected
- ✅ Environment variables are set
- ✅ Database is set up
- ✅ `DEBUG = False` in production

---

## 🆓 Free Deployment Options

### Option 1: Render (Recommended - Easiest) ⭐

**Best for:** Quick deployment, free tier available, automatic SSL

#### Steps:

1. **Sign up at [render.com](https://render.com)** (free account)

2. **Create a new Web Service:**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository: `elokwentnie/ProjectHack`
   - Select the repository

3. **Configure the service:**
   - **Name:** `projecthack` (or any name)
   - **Region:** Choose closest to you
   - **Branch:** `main`
   - **Root Directory:** (leave empty)
   - **Runtime:** `Python 3`
   - **Build Command:** 
     ```bash
     pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput
     ```
   - **Start Command:** 
     ```bash
     gunicorn projecthack.wsgi
     ```

4. **Set Environment Variables:**
   - Click "Environment" tab
   - Add these variables:
     ```
     SECRET_KEY=your-secret-key-here (generate a new one)
     DEBUG=False
     ALLOWED_HOSTS=your-app-name.onrender.com
     ```

5. **Deploy:**
   - Click "Create Web Service"
   - Wait 5-10 minutes for first deployment
   - Your app will be live at: `https://your-app-name.onrender.com`

**Free Tier Limits:**
- 750 hours/month (enough for always-on)
- Spins down after 15 min inactivity (wakes up on first request)
- 512 MB RAM

---

### Option 2: Railway

**Best for:** Simple deployment, good free tier

#### Steps:

1. **Sign up at [railway.app](https://railway.app)** (GitHub login)

2. **Create New Project:**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose `elokwentnie/ProjectHack`

3. **Configure:**
   - Railway auto-detects Django
   - Add environment variables:
     ```
     SECRET_KEY=your-secret-key
     DEBUG=False
     ALLOWED_HOSTS=*.railway.app
     ```

4. **Deploy:**
   - Railway automatically deploys
   - Get your URL: `https://your-app-name.railway.app`

**Free Tier:**
- $5 credit/month
- Pay-as-you-go after

---

### Option 3: Fly.io

**Best for:** Global edge deployment, good performance

#### Steps:

1. **Install Fly CLI:**
   ```bash
   curl -L https://fly.io/install.sh | sh
   ```

2. **Sign up and login:**
   ```bash
   fly auth signup
   fly auth login
   ```

3. **Initialize Fly app:**
   ```bash
   cd /Users/nataliadiana/Desktop/mvp
   fly launch
   ```

4. **Deploy:**
   ```bash
   fly deploy
   ```

**Free Tier:**
- 3 shared-cpu VMs
- 3GB persistent volume
- 160GB outbound data transfer

---

### Option 4: PythonAnywhere

**Best for:** Beginner-friendly, free tier available

#### Steps:

1. **Sign up at [pythonanywhere.com](https://www.pythonanywhere.com)**

2. **Upload your code:**
   - Use Git or upload files via web interface
   - Clone your repo in the console

3. **Set up virtual environment:**
   ```bash
   mkvirtualenv projecthack --python=python3.10
   pip install -r requirements.txt
   ```

4. **Configure Web App:**
   - Go to "Web" tab
   - Create new web app
   - Point to your WSGI file

**Free Tier:**
- Limited CPU time
- Single web app
- No custom domains

---

## 💰 Paid Options (Better Performance)

### Heroku

**Best for:** Established platform, add-ons ecosystem

#### Steps:

1. **Install Heroku CLI:**
   ```bash
   brew install heroku/brew/heroku  # macOS
   ```

2. **Login:**
   ```bash
   heroku login
   ```

3. **Create app:**
   ```bash
   heroku create your-app-name
   ```

4. **Set environment variables:**
   ```bash
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set DEBUG=False
   heroku config:set ALLOWED_HOSTS=your-app-name.herokuapp.com
   ```

5. **Deploy:**
   ```bash
   git push heroku main
   ```

**Pricing:** Starts at $7/month (Eco Dyno)

---

### DigitalOcean App Platform

**Best for:** Simple pricing, good performance

- Connect GitHub repo
- Auto-detects Django
- Set environment variables
- Deploy

**Pricing:** Starts at $5/month

---

## 🔧 Production Settings Setup

Before deploying, update your `settings.py` to use environment variables:

```python
import os
from decouple import config

SECRET_KEY = config('SECRET_KEY', default='django-insecure-dev-key-change-in-production')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*').split(',')

# Database (for production, use PostgreSQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME', default='projecthack'),
        'USER': config('DB_USER', default='postgres'),
        'PASSWORD': config('DB_PASSWORD', default=''),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
    }
}
```

---

## 📝 Quick Deploy Checklist

### Before First Deploy:

- [ ] Generate new `SECRET_KEY` (use: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`)
- [ ] Set `DEBUG = False`
- [ ] Update `ALLOWED_HOSTS` with your domain
- [ ] Set up database (PostgreSQL recommended for production)
- [ ] Collect static files: `python manage.py collectstatic`
- [ ] Run migrations: `python manage.py migrate`
- [ ] Load sample projects: `python manage.py load_sample_projects`

### After Deploy:

- [ ] Test all pages work
- [ ] Test onboarding flow
- [ ] Test project selection
- [ ] Test timer functionality
- [ ] Check static files load correctly
- [ ] Set up custom domain (optional)

---

## 🎯 Recommended: Render (Easiest)

For your MVP, I recommend **Render** because:
- ✅ Free tier available
- ✅ Automatic SSL certificates
- ✅ Easy GitHub integration
- ✅ Simple configuration
- ✅ Good documentation

**Quick Start on Render:**
1. Sign up → New Web Service
2. Connect GitHub repo
3. Use build command: `pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput`
4. Use start command: `gunicorn projecthack.wsgi`
5. Set environment variables
6. Deploy!

---

## 🆘 Troubleshooting

### Static files not loading?
- Make sure `collectstatic` runs during build
- Check `STATIC_ROOT` and `STATIC_URL` in settings
- Verify static files are served correctly

### Database errors?
- Make sure migrations run during build
- Check database connection settings
- For SQLite: ensure file permissions are correct

### 500 errors?
- Check logs in your hosting platform
- Verify `DEBUG=False` and `ALLOWED_HOSTS` are set
- Check environment variables are set correctly

### App won't start?
- Check `Procfile` is correct
- Verify `gunicorn` is in requirements.txt
- Check logs for specific errors

---

## 📚 Additional Resources

- [Django Deployment Checklist](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/)
- [Render Django Guide](https://render.com/docs/deploy-django)
- [Railway Django Guide](https://docs.railway.app/guides/django)

---

Need help? Check the logs in your hosting platform's dashboard!

