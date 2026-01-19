# 🚀 ProjectHack

> **Build Real Projects for Your CV** - A time-bound solo hackathon platform that helps inexperienced IT professionals boost their portfolios with step-by-step guidance.

[![Django](https://img.shields.io/badge/Django-4.2.7-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## ✨ Features

### 🎯 Core Features
- **⏱️ Time-Bound Projects** - Choose from 6h, 12h, 24h, or 48h hackathons
- **📚 Step-by-Step Guidance** - Detailed instructions with technologies introduced along the way
- **🎨 Interactive Onboarding** - Personalized project recommendations based on your skills and interests
- **⏰ Built-in Timer** - Track your progress with a real-time countdown timer
- **📊 Progress Tracking** - Visual progress bars and completion statistics
- **💼 CV-Ready Summary** - Get a professional summary of skills learned for your CV
- **🎨 Custom Project Generation** - Generate personalized projects based on your preferences
- **📥 Downloadable Resources** - Access CSV files, sample data, and other project resources

### 🎨 User Experience
- **🌙 Modern Dark Theme** - Beautiful, modern UI with glassmorphism effects
- **📱 Fully Responsive** - Works perfectly on mobile, tablet, and desktop
- **✨ Smooth Animations** - Polished animations and transitions
- **🚀 No Login Required** - Session-based, start building immediately
- **🎯 Personalized Recommendations** - AI-powered project suggestions

### 📦 Project Tracks
- **Frontend Development** - HTML, CSS, JavaScript projects
- **Backend Development** - Python/Flask, Django APIs
- **React** - React-specific projects with hooks and components
- **Node.js** - Express APIs and server-side JavaScript
- **Python** - Data analysis, automation, and scripting
- **Full-Stack** - Complete applications with frontend and backend

## 🎬 Demo

🔗 Live demo: https://projecthack.onrender.com/

This demo is continuously deployed.  
Every commit automatically updates the running version.

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/projecthack.git
   cd projecthack
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Load sample projects**
   ```bash
   python manage.py load_sample_projects
   ```

6. **Create a superuser** (optional, for admin access)
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Visit the application**
   ```
   http://127.0.0.1:8000/
   ```

## 📚 Available Projects

The platform includes **12+ diverse projects** across 6 tracks:

### Frontend Development
- Personal Portfolio Website (Beginner) - 6h, 12h, 24h, 48h
- Todo App with Local Storage (Intermediate) - 6h, 12h, 24h, 48h
- Weather App with API (Advanced) - 6h, 12h, 24h, 48h
- Interactive Calculator (Beginner) - 6h, 12h, 24h

### React Development
- React Todo Application (Intermediate) - 6h, 12h, 24h, 48h
- React Weather Dashboard (Advanced) - 6h, 12h, 24h, 48h

### Backend Development
- REST API with Flask (Intermediate) - 6h, 12h, 24h, 48h
- Django REST API Blog (Advanced) - 6h, 12h, 24h, 48h
- Node.js Express REST API (Intermediate) - 6h, 12h, 24h, 48h

### Python Development
- Data Analysis with Python (Beginner) - 6h, 12h, 24h, 48h
- File Organizer Automation (Intermediate) - 6h, 12h, 24h, 48h

### Full-Stack Development
- Full-Stack Todo Application (Advanced) - 6h, 12h, 24h, 48h

## 🏗️ Project Structure

```
projecthack/
├── projecthack/          # Django project settings
│   ├── settings.py      # Project configuration
│   ├── urls.py          # Main URL routing
│   └── wsgi.py          # WSGI configuration
├── projects/            # Main application
│   ├── models.py        # Database models
│   ├── views.py         # View logic
│   ├── urls.py          # App URL routing
│   ├── admin.py         # Admin configuration
│   ├── generator.py     # Project generation logic
│   ├── management/      # Management commands
│   │   └── commands/
│   │       ├── load_sample_projects.py
│   │       ├── reset_onboarding.py
│   │       └── check_project_steps.py
│   └── migrations/      # Database migrations
├── templates/           # HTML templates
│   ├── base.html
│   └── projects/
│       ├── home.html
│       ├── onboarding/
│       └── ...
├── static/              # Static files
│   └── files/           # Downloadable resources
├── manage.py            # Django management script
└── requirements.txt     # Python dependencies
```

## 🎯 How It Works

1. **Onboarding** - Answer 4 quick questions about your experience and interests
2. **Get Recommendations** - Receive personalized project suggestions
3. **Choose a Project** - Select a project and timeframe (6h, 12h, 24h, or 48h)
4. **Start Building** - Follow step-by-step guidance with technologies explained
5. **Track Progress** - Monitor your progress with the built-in timer
6. **Get CV Summary** - Receive a professional summary of skills learned

## 🛠️ Management Commands

### Load Sample Projects
```bash
python manage.py load_sample_projects
```
Loads all sample projects with their steps and timeframes.

### Reset Onboarding
```bash
python manage.py reset_onboarding
```
Resets onboarding for the most recent user session.

### Check Project Steps
```bash
python manage.py check_project_steps
```
Shows which projects have steps for which timeframes.

### Cleanup Duplicate Sessions
```bash
python manage.py cleanup_duplicate_sessions
```
Removes duplicate user sessions from the database.

## 🧪 Development

### Running Tests
```bash
python manage.py test
```

### Creating Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Accessing Admin Panel
Visit `http://127.0.0.1:8000/admin/` after creating a superuser.

## 🚀 Deployment

ProjectHack is ready to deploy! See [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) for detailed instructions.

### Quick Deploy Options:

**🆓 Free Options:**
- **[Render](https://render.com)** ⭐ Recommended - Easiest setup, free tier
- **[Railway](https://railway.app)** - Simple deployment, good free tier
- **[Fly.io](https://fly.io)** - Global edge deployment
- **[PythonAnywhere](https://www.pythonanywhere.com)** - Beginner-friendly

**💰 Paid Options:**
- **Heroku** - Established platform ($7/month)
- **DigitalOcean** - Simple pricing ($5/month)

### Quick Start (Render - Recommended):

1. Sign up at [render.com](https://render.com)
2. Create new Web Service → Connect GitHub repo
3. Build Command: `pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput`
4. Start Command: `gunicorn projecthack.wsgi`
5. Set Environment Variables:
   - `SECRET_KEY` - Generate with: `python generate_secret_key.py`
   - `DEBUG=False`
   - `ALLOWED_HOSTS=your-app-name.onrender.com`

### Environment Variables Needed:
- `SECRET_KEY` - Django secret key (generate new one for production)
- `DEBUG` - Set to `False` in production
- `ALLOWED_HOSTS` - Your domain(s), comma-separated

**📖 Full deployment guide:** See [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) for step-by-step instructions for all platforms.

## 🛣️ Roadmap

See [docs/ROADMAP.md](docs/ROADMAP.md) for detailed development plans.

### Upcoming Features
- ⏸️ Pause/Resume Timer
- 📄 PDF Export for CV Summary
- 🔍 Search & Filter Projects
- 👁️ View All Steps Option
- 🏆 Completion Certificates
- 📱 Social Sharing

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Django](https://www.djangoproject.com/)
- Styled with [Tailwind CSS](https://tailwindcss.com/)
- Inspired by the need to help beginners build real projects for their CVs

## 📧 Contact & Support

- **Issues**: [GitHub Issues](https://github.com/YOUR_USERNAME/projecthack/issues)
- **Discussions**: [GitHub Discussions](https://github.com/YOUR_USERNAME/projecthack/discussions)

---

## 🌟 Show Your Support

If you find this project helpful, please give it a ⭐ star on GitHub!

---

⭐ If you find this project helpful, please give it a star!
