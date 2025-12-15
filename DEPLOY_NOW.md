# 🚀 Quick Deployment Guide - Render.com

## ⚠️ Generate Your Production Secret Key

**IMPORTANT:** Generate a new secret key for production. Run this command locally:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

**⚠️ Save the generated key securely - you'll need it in step 4!**

---

## Step-by-Step Instructions

### Step 1: Sign Up for Render
1. Go to [https://render.com](https://render.com)
2. Click "Get Started for Free"
3. Sign up with your GitHub account (recommended) or email

### Step 2: Create New Web Service
1. Once logged in, click the **"New +"** button (top right)
2. Select **"Web Service"**
3. Connect your GitHub account if not already connected
4. Find and select your repository: **`elokwentnie/ProjectHack`**
5. Click **"Connect"**

### Step 3: Configure Your Service

Fill in these settings:

- **Name:** `projecthack` (or any name you like)
- **Region:** Choose the closest region to you
- **Branch:** `main`
- **Root Directory:** (leave empty)
- **Runtime:** `Python 3`
- **Build Command:** 
  ```
  pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput && python manage.py load_sample_projects
  ```
- **Start Command:**
  ```
  gunicorn projecthack.wsgi
  ```

### Step 4: Set Environment Variables

1. Scroll down to the **"Environment"** section
2. Click **"Add Environment Variable"** for each of these:

   | Key | Value |
   |-----|-------|
   | `SECRET_KEY` | `[Paste the key you generated above]` |
   | `DEBUG` | `False` |
   | `ALLOWED_HOSTS` | `projecthack.onrender.com` (or your-app-name.onrender.com) |

   **Note:** Replace `projecthack.onrender.com` with your actual app name if different!

### Step 5: Deploy!

1. Scroll to the bottom
2. Click **"Create Web Service"**
3. Wait 5-10 minutes for the first deployment
4. You'll see build logs in real-time
5. Once deployed, your app will be live at: `https://your-app-name.onrender.com`

---

## ✅ Post-Deployment Checklist

After deployment, test these:

- [ ] Visit your app URL
- [ ] Test the onboarding flow
- [ ] Test project selection
- [ ] Test timer functionality
- [ ] Check that static files (CSS/images) load correctly
- [ ] Test all pages work

---

## 🆘 Troubleshooting

### If static files don't load:
- Check that `collectstatic` ran during build (check logs)
- Verify `STATIC_ROOT` is set correctly

### If you get 500 errors:
- Check the logs in Render dashboard
- Verify all environment variables are set correctly
- Make sure `DEBUG=False` and `ALLOWED_HOSTS` matches your domain

### If the app won't start:
- Check the logs for specific errors
- Verify `gunicorn` is in requirements.txt (it is ✅)
- Check that the start command is correct

---

## 📝 Important Notes

- **Free Tier:** Your app will spin down after 15 minutes of inactivity (wakes up on first request)
- **First Request:** May take 30-60 seconds if the app was sleeping
- **Database:** Currently using SQLite (fine for MVP, consider PostgreSQL for production later)

---

## 🎉 You're Done!

Once deployed, share your app URL and celebrate! 🚀
