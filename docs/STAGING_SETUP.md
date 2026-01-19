# 🧪 Staging/Testing Environment Setup

This guide shows you how to set up a **staging environment** for testing changes without affecting your production site.

## 🎯 Concept

- **Production**: `projecthack.onrender.com` - Your live, working site
- **Staging**: `projecthack-staging.onrender.com` - Your testing environment

## 📋 Setup Steps

### Option 1: Separate Render Services (Recommended)

1. **Keep your current production service** (`projecthack`) as-is
   - This is your stable, working version
   - Don't make changes directly to this

2. **Create a new staging service:**
   - Go to Render dashboard
   - Click "New +" → "Web Service"
   - Connect the same GitHub repo: `elokwentnie/ProjectHack`
   - Name it: `projecthack-staging` (or `projecthack-test`)
   - **Important**: Use a different branch or the same branch (your choice)

3. **Configure staging service:**
   - **Name:** `projecthack-staging`
   - **Branch:** `main` (or create a `staging` branch)
   - **Build Command:** Same as production
   - **Start Command:** Same as production

4. **Set different environment variables:**
   - `SECRET_KEY`: Generate a NEW one (different from production)
   - `DEBUG`: `True` (so you can see errors)
   - `ALLOWED_HOSTS`: `projecthack-staging.onrender.com`

### Option 2: Use Different Git Branches

1. **Create a staging branch:**
   ```bash
   git checkout -b staging
   git push -u origin staging
   ```

2. **Production service** → Deploy from `main` branch
3. **Staging service** → Deploy from `staging` branch

4. **Workflow:**
   - Make changes on `staging` branch
   - Test on staging environment
   - If it works, merge to `main` → Production auto-deploys

## 🔄 Recommended Workflow

### Daily Development:

1. **Make changes locally**
2. **Test locally** (`python manage.py runserver`)
3. **Push to `staging` branch** (or create a feature branch)
4. **Staging environment auto-deploys**
5. **Test on staging URL**
6. **If everything works → Merge to `main`**
7. **Production auto-deploys** (only when you're confident)

### Quick Testing:

1. Push to `main` branch
2. Staging deploys first (if using same branch, deploy manually)
3. Test staging
4. If good, production is already updated (or merge to main)

## 🛡️ Protecting Production

### Option A: Manual Deploy (Safest)

1. In Render, set production service to **"Manual Deploy"**
2. Staging auto-deploys on every push
3. Production only deploys when you click "Deploy" manually

**How to enable:**
- Go to production service → Settings
- Under "Auto-Deploy", change to "No"
- Now you control when production updates

### Option B: Branch Protection

1. Production deploys from `main` branch only
2. Staging deploys from `staging` branch
3. Never push directly to `main` - always test on `staging` first

## 📝 Environment Variables Comparison

### Production:
```
SECRET_KEY=<production-secret-key>
DEBUG=False
ALLOWED_HOSTS=projecthack.onrender.com
```

### Staging:
```
SECRET_KEY=<different-staging-secret-key>
DEBUG=True
ALLOWED_HOSTS=projecthack-staging.onrender.com
```

## 🎯 Best Practice Setup

1. **Production Service:**
   - Name: `projecthack`
   - Branch: `main`
   - Auto-Deploy: **OFF** (manual only)
   - Environment: Production settings

2. **Staging Service:**
   - Name: `projecthack-staging`
   - Branch: `main` (or `staging`)
   - Auto-Deploy: **ON** (test every change)
   - Environment: Debug enabled

## 🚀 Quick Start

1. Create staging service on Render (5 minutes)
2. Set different environment variables
3. Test changes on staging first
4. Only deploy to production when confident

## 💡 Pro Tips

- **Use different database**: Staging can use a separate SQLite or PostgreSQL
- **Different domains**: Easy to tell which is which
- **Test destructive changes**: Try migrations, big changes on staging first
- **Share staging URL**: Let others test before production

---

**Result:** You can test freely on staging without breaking production! 🎉

