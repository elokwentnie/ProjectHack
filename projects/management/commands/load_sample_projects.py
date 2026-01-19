from django.core.management.base import BaseCommand
from projects.models import Project, ProjectStep, ProjectResource


class Command(BaseCommand):
    help = 'Load sample projects with steps'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample projects...')
        
        # Clean up old projects with deprecated track names
        old_projects = Project.objects.filter(track='web_dev')
        if old_projects.exists():
            self.stdout.write('Removing old projects with deprecated track...')
            for old_project in old_projects:
                old_project.steps.all().delete()
                old_project.delete()
        
        # ========== FRONTEND PROJECTS ==========
        
        # Project 1: Personal Portfolio Website (Beginner - Frontend)
        project1, created = Project.objects.get_or_create(
            title='Personal Portfolio Website',
            defaults={
                'description': '''Build your own professional portfolio website from scratch! This project will teach you the fundamentals of frontend development while creating something you can actually use to showcase your work.

You'll learn HTML structure, CSS styling, responsive design, and how to deploy your website. Perfect for beginners who want to create their first real website.'''
            }
        )
        project1.difficulty = 'beginner'
        project1.track = 'frontend'
        project1.save()
        
        if created:
            self.stdout.write(f'Created project: {project1.title}')
            self._add_portfolio_steps(project1)
        
        # Project 2: Todo App with Local Storage (Intermediate - Frontend)
        project2, created = Project.objects.get_or_create(
            title='Todo App with Local Storage',
            defaults={
                'description': '''Create a fully functional todo application that persists data using browser local storage. This project introduces you to JavaScript, DOM manipulation, and data persistence.

You'll build a complete CRUD (Create, Read, Update, Delete) application that works entirely in the browser. Great for learning JavaScript fundamentals and understanding how frontend applications work.'''
            }
        )
        project2.difficulty = 'intermediate'
        project2.track = 'frontend'
        project2.save()
        
        if created:
            self.stdout.write(f'Created project: {project2.title}')
            self._add_todo_steps(project2)
        
        # Project 3: Weather App with API (Advanced Beginner - Frontend)
        project3, created = Project.objects.get_or_create(
            title='Weather App with API',
            defaults={
                'description': '''Build a weather application that fetches real-time weather data from an API. This project teaches you how to work with external APIs, handle asynchronous operations, and create dynamic user interfaces.

You'll learn about API calls, JSON data, async/await or promises, error handling, and creating a responsive, user-friendly interface. This is a great project to understand how modern frontend applications interact with external services.'''
            }
        )
        project3.difficulty = 'advanced'
        project3.track = 'frontend'
        project3.save()
        
        if created:
            self.stdout.write(f'Created project: {project3.title}')
            self._add_weather_steps(project3)
        
        # Project 4: Calculator App (Beginner - Frontend)
        project4, created = Project.objects.get_or_create(
            title='Interactive Calculator',
            defaults={
                'description': '''Build a fully functional calculator with a clean, modern interface. This project teaches you JavaScript fundamentals, event handling, and building interactive user interfaces.

You'll learn how to handle user input, perform calculations, manage state, and create a polished UI. Great for understanding JavaScript logic and DOM manipulation.'''
            }
        )
        project4.difficulty = 'beginner'
        project4.track = 'frontend'
        project4.save()
        
        if created:
            self.stdout.write(f'Created project: {project4.title}')
            self._add_calculator_steps(project4)
        
        # Project 5: React Todo App (Intermediate - React)
        project5, created = Project.objects.get_or_create(
            title='React Todo Application',
            defaults={
                'description': '''Build a modern todo application using React! Learn component-based architecture, state management, and React hooks.

You'll understand React fundamentals, JSX syntax, component lifecycle, and how to build reusable UI components. Perfect for transitioning from vanilla JavaScript to React.'''
            }
        )
        project5.difficulty = 'intermediate'
        project5.track = 'react'
        project5.save()
        
        if created:
            self.stdout.write(f'Created project: {project5.title}')
            self._add_react_todo_steps(project5)
        
        # Project 6: React Weather Dashboard (Advanced - React)
        project6, created = Project.objects.get_or_create(
            title='React Weather Dashboard',
            defaults={
                'description': '''Create a beautiful weather dashboard using React and external APIs. Learn about React hooks, API integration, and building complex component hierarchies.

You'll work with useState, useEffect, custom hooks, and learn how to structure a larger React application.'''
            }
        )
        project6.difficulty = 'advanced'
        project6.track = 'react'
        project6.save()
        
        if created:
            self.stdout.write(f'Created project: {project6.title}')
            self._add_react_weather_steps(project6)
        
        # ========== BACKEND PROJECTS ==========
        
        # Project 7: REST API with Python/Flask (Intermediate - Backend)
        project7, created = Project.objects.get_or_create(
            title='REST API with Flask',
            defaults={
                'description': '''Build a RESTful API using Python and Flask. Learn about HTTP methods, endpoints, request/response handling, and API design principles.

You'll create endpoints for CRUD operations, handle JSON data, implement error handling, and test your API. Essential skills for backend development.'''
            }
        )
        project7.difficulty = 'intermediate'
        project7.track = 'backend'
        project7.save()
        
        if created:
            self.stdout.write(f'Created project: {project7.title}')
            self._add_flask_api_steps(project7)
        
        # Project 8: Node.js Express API (Intermediate - Node.js)
        project8, created = Project.objects.get_or_create(
            title='Node.js Express REST API',
            defaults={
                'description': '''Create a RESTful API using Node.js and Express. Learn about server-side JavaScript, routing, middleware, and building scalable backend services.

You'll understand Node.js fundamentals, Express framework, middleware concepts, and how to structure a backend application.'''
            }
        )
        project8.difficulty = 'intermediate'
        project8.track = 'nodejs'
        project8.save()
        
        if created:
            self.stdout.write(f'Created project: {project8.title}')
            self._add_nodejs_api_steps(project8)
        
        # Project 9: Django Blog API (Advanced - Backend)
        project9, created = Project.objects.get_or_create(
            title='Django REST API Blog',
            defaults={
                'description': '''Build a blog API using Django REST Framework. Learn about Django models, serializers, viewsets, authentication, and building production-ready APIs.

You'll understand Django architecture, ORM, REST API design, and how to build scalable backend applications.'''
            }
        )
        project9.difficulty = 'advanced'
        project9.track = 'backend'
        project9.save()
        
        if created:
            self.stdout.write(f'Created project: {project9.title}')
            self._add_django_api_steps(project9)
        
        # Project 10: Python Data Analysis Script (Beginner - Python)
        project10, created = Project.objects.get_or_create(
            title='Data Analysis with Python',
            defaults={
                'description': '''Analyze a dataset using Python, pandas, and matplotlib. Learn data manipulation, cleaning, visualization, and basic statistics.

You'll work with CSV files, perform data analysis, create visualizations, and generate insights. Great introduction to data science and Python libraries.'''
            }
        )
        project10.difficulty = 'beginner'
        project10.track = 'python'
        project10.save()
        
        if created:
            self.stdout.write(f'Created project: {project10.title}')
            self._add_python_data_steps(project10)
            self._add_python_data_resources(project10)
        
        # Project 11: Python Automation Script (Intermediate - Python)
        project11, created = Project.objects.get_or_create(
            title='File Organizer Automation',
            defaults={
                'description': '''Create a Python script that automatically organizes files in a directory. Learn file system operations, path handling, and automation.

You'll understand Python file I/O, pathlib, working with directories, and building practical automation tools.'''
            }
        )
        project11.difficulty = 'intermediate'
        project11.track = 'python'
        project11.save()
        
        if created:
            self.stdout.write(f'Created project: {project11.title}')
            self._add_python_automation_steps(project11)
        
        # ========== FULL-STACK PROJECTS ==========
        
        # Project 12: Full-Stack Todo App (Advanced - Full-Stack)
        project12, created = Project.objects.get_or_create(
            title='Full-Stack Todo Application',
            defaults={
                'description': '''Build a complete full-stack todo application with a frontend and backend. Learn how to connect frontend and backend, handle API calls, and build a complete application.

You'll integrate a React frontend with a Node.js/Express backend, handle CORS, implement authentication, and deploy a full-stack application.'''
            }
        )
        project12.difficulty = 'advanced'
        project12.track = 'fullstack'
        project12.save()
        
        if created:
            self.stdout.write(f'Created project: {project12.title}')
            self._add_fullstack_todo_steps(project12)
        
        # Project 13: Quiz App (Beginner - Frontend)
        project13, created = Project.objects.get_or_create(
            title='Interactive Quiz Application',
            defaults={
                'description': '''Build an interactive quiz app with multiple-choice questions, score tracking, and instant feedback. This project teaches you how to build engaging, interactive web applications.

You'll learn how to manage application state, handle user interactions, calculate scores, and provide real-time feedback. Great for learning JavaScript fundamentals and building user-friendly interfaces.'''
            }
        )
        project13.difficulty = 'beginner'
        project13.track = 'frontend'
        project13.save()
        
        if created:
            self.stdout.write(f'Created project: {project13.title}')
            self._add_quiz_app_steps(project13)
        
        # Project 14: Recipe Finder App (Intermediate - Frontend)
        project14, created = Project.objects.get_or_create(
            title='Recipe Finder App',
            defaults={
                'description': '''Create a recipe finder application that searches recipes by ingredients or cuisine type. Integrate with a recipe API and display results beautifully.

You'll learn API integration, search functionality, responsive design, and how to create an engaging food-related web application. Perfect for learning how to work with external data sources.'''
            }
        )
        project14.difficulty = 'intermediate'
        project14.track = 'frontend'
        project14.save()
        
        if created:
            self.stdout.write(f'Created project: {project14.title}')
            self._add_recipe_finder_steps(project14)
        
        # Project 15: Note-Taking App (Intermediate - React)
        project15, created = Project.objects.get_or_create(
            title='React Note-Taking App',
            defaults={
                'description': '''Build a beautiful note-taking application using React. Create, edit, delete, and organize notes with categories and search functionality.

You'll learn React state management, component composition, local storage integration, and how to build a practical productivity application. Great for understanding React patterns and best practices.'''
            }
        )
        project15.difficulty = 'intermediate'
        project15.track = 'react'
        project15.save()
        
        if created:
            self.stdout.write(f'Created project: {project15.title}')
            self._add_note_taking_steps(project15)
        
        # Project 16: URL Shortener API (Beginner - Backend)
        project16, created = Project.objects.get_or_create(
            title='URL Shortener API',
            defaults={
                'description': '''Build a URL shortener service using Python and Flask. Create short, shareable links from long URLs, track click statistics, and manage link expiration.

You'll learn about URL encoding, database operations, REST API design, and how to build a practical backend service. Essential skills for backend development.'''
            }
        )
        project16.difficulty = 'beginner'
        project16.track = 'backend'
        project16.save()
        
        if created:
            self.stdout.write(f'Created project: {project16.title}')
            self._add_url_shortener_steps(project16)
        
        # Project 17: Chat API (Advanced - Node.js)
        project17, created = Project.objects.get_or_create(
            title='Real-time Chat API',
            defaults={
                'description': '''Build a real-time chat API using Node.js, Express, and WebSockets. Support multiple chat rooms, user authentication, and message persistence.

You'll learn WebSocket programming, real-time communication, event-driven architecture, and how to build scalable chat applications. Advanced backend development skills.'''
            }
        )
        project17.difficulty = 'advanced'
        project17.track = 'nodejs'
        project17.save()
        
        if created:
            self.stdout.write(f'Created project: {project17.title}')
            self._add_chat_api_steps(project17)
        
        # Project 18: Web Scraper (Intermediate - Python)
        project18, created = Project.objects.get_or_create(
            title='Web Scraper with Python',
            defaults={
                'description': '''Create a Python web scraper to extract data from websites. Learn about HTML parsing, handling dynamic content, and respecting robots.txt.

You'll work with BeautifulSoup, requests library, handle pagination, save data to files, and understand web scraping ethics. Great for learning data extraction and automation.'''
            }
        )
        project18.difficulty = 'intermediate'
        project18.track = 'python'
        project18.save()
        
        if created:
            self.stdout.write(f'Created project: {project18.title}')
            self._add_web_scraper_steps(project18)
        
        # Project 19: Blog Platform (Advanced - Full-Stack)
        project19, created = Project.objects.get_or_create(
            title='Full-Stack Blog Platform',
            defaults={
                'description': '''Build a complete blog platform with a React frontend and Node.js backend. Include features like post creation, editing, comments, user authentication, and rich text editing.

You'll learn full-stack architecture, user authentication, file uploads, rich text editors, and how to build a complete content management system. Comprehensive full-stack project.'''
            }
        )
        project19.difficulty = 'advanced'
        project19.track = 'fullstack'
        project19.save()
        
        if created:
            self.stdout.write(f'Created project: {project19.title}')
            self._add_blog_platform_steps(project19)
        
        # Project 20: E-commerce API (Advanced - Backend)
        project20, created = Project.objects.get_or_create(
            title='E-commerce REST API',
            defaults={
                'description': '''Build a complete e-commerce REST API with Django REST Framework. Implement products, categories, shopping cart, orders, and payment processing integration.

You'll learn advanced Django patterns, complex database relationships, API design, payment gateway integration, and how to build production-ready backend systems.'''
            }
        )
        project20.difficulty = 'advanced'
        project20.track = 'backend'
        project20.save()
        
        if created:
            self.stdout.write(f'Created project: {project20.title}')
            self._add_ecommerce_api_steps(project20)
        
        self.stdout.write(self.style.SUCCESS('Successfully loaded sample projects!'))
        self.stdout.write(f'Total projects: {Project.objects.count()}')
        self.stdout.write(f'Total steps: {ProjectStep.objects.count()}')
    
    def _add_portfolio_steps(self, project):
        """Add steps for Portfolio Website"""
        steps_6h = [
            {'step_number': 1, 'title': 'Setup and Planning', 'description': 'Create a new folder for your project. Plan the structure: Home, About, Projects, Contact sections. Set up a basic HTML file with proper document structure.', 'technologies': ['HTML', 'File System'], 'estimated_time': 30, 'learning_outcomes': 'Understanding project structure and HTML document basics'},
            {'step_number': 2, 'title': 'Build HTML Structure', 'description': 'Create the HTML structure for all sections: header with navigation, hero section, about section, projects showcase, and contact form. Use semantic HTML5 elements.', 'technologies': ['HTML5', 'Semantic HTML'], 'estimated_time': 90, 'learning_outcomes': 'Learning semantic HTML and proper document structure'},
            {'step_number': 3, 'title': 'Style with CSS', 'description': 'Create a CSS file and style your website. Add colors, fonts, spacing, and basic layout. Make it visually appealing with a modern design.', 'technologies': ['CSS', 'Typography', 'Color Theory'], 'estimated_time': 120, 'learning_outcomes': 'CSS fundamentals, styling, and design principles'},
            {'step_number': 4, 'title': 'Make it Responsive', 'description': 'Add media queries to make your website work on mobile, tablet, and desktop. Test on different screen sizes.', 'technologies': ['Responsive Design', 'Media Queries', 'Mobile-First'], 'estimated_time': 60, 'learning_outcomes': 'Responsive web design and mobile optimization'},
            {'step_number': 5, 'title': 'Add Interactivity', 'description': 'Add smooth scrolling, hover effects, and basic animations. Polish the user experience.', 'technologies': ['CSS Transitions', 'User Experience'], 'estimated_time': 40, 'learning_outcomes': 'CSS animations and UX improvements'},
            {'step_number': 6, 'title': 'Deploy to GitHub Pages', 'description': 'Initialize a Git repository, commit your code, push to GitHub, and deploy using GitHub Pages. Share your live website!', 'technologies': ['Git', 'GitHub', 'GitHub Pages', 'Deployment'], 'estimated_time': 40, 'learning_outcomes': 'Version control with Git and web deployment'},
        ]
        for step_data in steps_6h:
            ProjectStep.objects.create(project=project, timeframe='6h', **step_data)
        
        steps_12h = steps_6h + [
            {'step_number': 7, 'title': 'Add JavaScript Functionality', 'description': 'Add interactive features: smooth scroll navigation, form validation, and a simple contact form handler.', 'technologies': ['JavaScript', 'DOM Manipulation', 'Form Validation'], 'estimated_time': 90, 'learning_outcomes': 'JavaScript basics and DOM manipulation'},
            {'step_number': 8, 'title': 'Add Project Showcase', 'description': 'Create a dynamic project showcase section with filtering or categories. Use JavaScript to show/hide projects.', 'technologies': ['JavaScript', 'Event Handling', 'DOM Manipulation'], 'estimated_time': 60, 'learning_outcomes': 'Interactive JavaScript features'},
        ]
        for step_data in steps_12h:
            ProjectStep.objects.create(project=project, timeframe='12h', **step_data)
        
        steps_24h = steps_12h + [
            {'step_number': 9, 'title': 'Add Animations and Transitions', 'description': 'Implement smooth page transitions, scroll animations, and interactive hover effects using CSS and JavaScript.', 'technologies': ['CSS Animations', 'JavaScript', 'UX'], 'estimated_time': 90, 'learning_outcomes': 'Advanced animations and transitions'},
            {'step_number': 10, 'title': 'Add Dark Mode', 'description': 'Implement a dark mode toggle. Use CSS variables and JavaScript to switch between light and dark themes.', 'technologies': ['CSS Variables', 'JavaScript', 'Theme Switching'], 'estimated_time': 60, 'learning_outcomes': 'Theme implementation and CSS variables'},
            {'step_number': 11, 'title': 'Optimize Performance', 'description': 'Optimize images, minify CSS/JS, implement lazy loading, and improve page load times.', 'technologies': ['Performance Optimization', 'Lazy Loading', 'Image Optimization'], 'estimated_time': 75, 'learning_outcomes': 'Web performance optimization'},
            {'step_number': 12, 'title': 'Add SEO and Analytics', 'description': 'Add meta tags, structured data, and Google Analytics. Improve SEO and track website visitors.', 'technologies': ['SEO', 'Google Analytics', 'Structured Data'], 'estimated_time': 45, 'learning_outcomes': 'SEO and web analytics'},
        ]
        for step_data in steps_24h:
            ProjectStep.objects.create(project=project, timeframe='24h', **step_data)
        
        steps_48h = steps_24h + [
            {'step_number': 13, 'title': 'Add Blog Section', 'description': 'Create a blog section with dynamic content. Implement a simple CMS for blog posts.', 'technologies': ['JavaScript', 'Content Management'], 'estimated_time': 120, 'learning_outcomes': 'Content management systems'},
            {'step_number': 14, 'title': 'Add Contact Form Backend', 'description': 'Integrate a contact form with a backend service (Formspree, EmailJS, or custom backend).', 'technologies': ['API Integration', 'Forms'], 'estimated_time': 90, 'learning_outcomes': 'Form backend integration'},
        ]
        for step_data in steps_48h:
            ProjectStep.objects.create(project=project, timeframe='48h', **step_data)
    
    def _add_todo_steps(self, project):
        """Add steps for Todo App"""
        steps_6h = [
            {'step_number': 1, 'title': 'Project Setup and HTML Structure', 'description': 'Create the HTML structure for your todo app: input field, add button, todo list container, and filter buttons (All, Active, Completed).', 'technologies': ['HTML', 'Semantic HTML'], 'estimated_time': 45, 'learning_outcomes': 'HTML structure for interactive applications'},
            {'step_number': 2, 'title': 'Style the Application', 'description': 'Design a clean, modern UI with CSS. Style the input, buttons, and todo items. Add hover and active states.', 'technologies': ['CSS', 'UI Design', 'CSS Flexbox/Grid'], 'estimated_time': 90, 'learning_outcomes': 'CSS layout and styling for applications'},
            {'step_number': 3, 'title': 'Add Todo Functionality (Create)', 'description': 'Implement JavaScript to add new todos. Create a function that takes input, creates a todo object, and displays it in the list.', 'technologies': ['JavaScript', 'DOM Manipulation', 'Event Listeners'], 'estimated_time': 60, 'learning_outcomes': 'JavaScript functions and DOM manipulation'},
            {'step_number': 4, 'title': 'Implement Mark as Complete', 'description': 'Add functionality to mark todos as complete/incomplete. Toggle the completed state and update the UI accordingly.', 'technologies': ['JavaScript', 'State Management', 'Event Handling'], 'estimated_time': 45, 'learning_outcomes': 'Managing application state'},
            {'step_number': 5, 'title': 'Add Delete Functionality', 'description': 'Implement delete functionality. Allow users to remove individual todos from the list.', 'technologies': ['JavaScript', 'DOM Manipulation'], 'estimated_time': 30, 'learning_outcomes': 'Removing elements from DOM'},
            {'step_number': 6, 'title': 'Implement Local Storage', 'description': 'Save todos to browser local storage. Load todos from storage when the page loads. Persist all changes (add, complete, delete).', 'technologies': ['Local Storage API', 'JSON', 'Data Persistence'], 'estimated_time': 90, 'learning_outcomes': 'Browser storage APIs and data persistence'},
        ]
        for step_data in steps_6h:
            ProjectStep.objects.create(project=project, timeframe='6h', **step_data)
        
        steps_12h = steps_6h + [
            {'step_number': 7, 'title': 'Add Filter Functionality', 'description': 'Implement filtering: show all todos, only active ones, or only completed ones. Update the UI based on selected filter.', 'technologies': ['JavaScript', 'Array Methods', 'Filter Logic'], 'estimated_time': 60, 'learning_outcomes': 'Array manipulation and filtering'},
            {'step_number': 8, 'title': 'Add Edit Functionality', 'description': 'Allow users to edit existing todos. Add double-click to edit, save on Enter, cancel on Escape.', 'technologies': ['JavaScript', 'Event Handling', 'Input Management'], 'estimated_time': 75, 'learning_outcomes': 'Advanced event handling and user interactions'},
            {'step_number': 9, 'title': 'Add Counter and Polish', 'description': 'Add a counter showing active todos. Add "Clear Completed" button. Polish the UI and add smooth transitions.', 'technologies': ['JavaScript', 'CSS Transitions', 'UX'], 'estimated_time': 45, 'learning_outcomes': 'UX improvements and polish'},
            {'step_number': 10, 'title': 'Deploy to GitHub Pages', 'description': 'Initialize Git repository, commit code, push to GitHub, and deploy. Test the deployed app.', 'technologies': ['Git', 'GitHub', 'Deployment'], 'estimated_time': 30, 'learning_outcomes': 'Version control and deployment'},
        ]
        for step_data in steps_12h:
            ProjectStep.objects.create(project=project, timeframe='12h', **step_data)
        
        steps_24h = steps_12h + [
            {'step_number': 11, 'title': 'Add Categories/Tags', 'description': 'Implement category or tag system for todos. Allow users to organize todos by categories.', 'technologies': ['JavaScript', 'Data Structure', 'UI Design'], 'estimated_time': 90, 'learning_outcomes': 'Data organization and UI patterns'},
            {'step_number': 12, 'title': 'Add Due Dates and Reminders', 'description': 'Add due date functionality and visual indicators for overdue tasks. Implement date picker.', 'technologies': ['JavaScript', 'Date Handling', 'UI Components'], 'estimated_time': 90, 'learning_outcomes': 'Date manipulation and UI components'},
            {'step_number': 13, 'title': 'Add Search Functionality', 'description': 'Implement search to find todos by text. Add real-time filtering as user types.', 'technologies': ['JavaScript', 'Search Algorithm', 'Real-time Updates'], 'estimated_time': 60, 'learning_outcomes': 'Search implementation'},
            {'step_number': 14, 'title': 'Add Export/Import', 'description': 'Allow users to export todos to JSON/CSV and import them back. Implement file download/upload.', 'technologies': ['JavaScript', 'File API', 'Data Export'], 'estimated_time': 75, 'learning_outcomes': 'File handling and data export'},
        ]
        for step_data in steps_24h:
            ProjectStep.objects.create(project=project, timeframe='24h', **step_data)
        
        steps_48h = steps_24h + [
            {'step_number': 15, 'title': 'Add Collaboration Features', 'description': 'Implement sharing functionality. Allow multiple users to collaborate on todo lists.', 'technologies': ['JavaScript', 'Data Sharing'], 'estimated_time': 120, 'learning_outcomes': 'Collaboration features'},
            {'step_number': 16, 'title': 'Add Notifications', 'description': 'Implement browser notifications for due dates and reminders. Use Notification API.', 'technologies': ['Notifications API', 'JavaScript'], 'estimated_time': 90, 'learning_outcomes': 'Browser notifications'},
        ]
        for step_data in steps_48h:
            ProjectStep.objects.create(project=project, timeframe='48h', **step_data)
    
    def _add_weather_steps(self, project):
        """Add steps for Weather App"""
        steps_6h = [
            {'step_number': 1, 'title': 'Project Setup and API Key', 'description': 'Set up your project structure. Sign up for a free weather API (OpenWeatherMap recommended). Get your API key and understand the API documentation.', 'technologies': ['API', 'HTTP', 'API Keys'], 'estimated_time': 45, 'learning_outcomes': 'Understanding APIs and authentication'},
            {'step_number': 2, 'title': 'Create HTML Structure', 'description': 'Build the HTML structure: search input, current weather display area, forecast section, and loading/error states.', 'technologies': ['HTML', 'Semantic HTML'], 'estimated_time': 60, 'learning_outcomes': 'HTML structure for dynamic content'},
            {'step_number': 3, 'title': 'Style the Application', 'description': 'Design a beautiful weather app UI. Use CSS to create cards, icons, and a responsive layout. Add weather-themed colors and styling.', 'technologies': ['CSS', 'Responsive Design', 'UI Design'], 'estimated_time': 90, 'learning_outcomes': 'CSS styling and responsive layouts'},
            {'step_number': 4, 'title': 'Make Your First API Call', 'description': 'Write JavaScript to make your first API call. Use fetch() to get weather data for a hardcoded city. Log the response to console.', 'technologies': ['JavaScript', 'Fetch API', 'Async Operations'], 'estimated_time': 75, 'learning_outcomes': 'Making HTTP requests and handling responses'},
            {'step_number': 5, 'title': 'Parse and Display Data', 'description': 'Parse the JSON response and display current weather: temperature, description, humidity, wind speed. Update the DOM with the data.', 'technologies': ['JavaScript', 'JSON', 'DOM Manipulation'], 'estimated_time': 60, 'learning_outcomes': 'Working with JSON data and DOM updates'},
        ]
        for step_data in steps_6h:
            ProjectStep.objects.create(project=project, timeframe='6h', **step_data)
        
        steps_12h = steps_6h + [
            {'step_number': 6, 'title': 'Add Search Functionality', 'description': 'Implement city search. Allow users to enter a city name, make an API call, and display weather for that city. Handle form submission.', 'technologies': ['JavaScript', 'Event Handling', 'Form Processing'], 'estimated_time': 60, 'learning_outcomes': 'User input handling and dynamic API calls'},
            {'step_number': 7, 'title': 'Add Error Handling', 'description': 'Handle API errors gracefully. Show user-friendly error messages for invalid cities, network errors, and API failures.', 'technologies': ['JavaScript', 'Error Handling', 'Try-Catch'], 'estimated_time': 45, 'learning_outcomes': 'Error handling and user feedback'},
            {'step_number': 8, 'title': 'Add Weather Icons', 'description': 'Display weather icons based on conditions. Use an icon library or create custom icons. Map weather codes to appropriate icons.', 'technologies': ['JavaScript', 'Conditional Logic', 'Icon Libraries'], 'estimated_time': 60, 'learning_outcomes': 'Working with external libraries and conditionals'},
        ]
        for step_data in steps_12h:
            ProjectStep.objects.create(project=project, timeframe='12h', **step_data)
        
        steps_24h = steps_12h + [
            {'step_number': 9, 'title': 'Add Forecast Display', 'description': 'Fetch and display 5-day forecast. Show daily weather predictions in a nice card layout.', 'technologies': ['JavaScript', 'API', 'Data Processing'], 'estimated_time': 90, 'learning_outcomes': 'Working with complex API responses'},
            {'step_number': 10, 'title': 'Add Loading States', 'description': 'Implement loading indicators while fetching data. Show skeleton screens or spinners during API calls.', 'technologies': ['JavaScript', 'UX', 'Loading States'], 'estimated_time': 45, 'learning_outcomes': 'UX improvements and loading states'},
            {'step_number': 11, 'title': 'Add Local Storage for Recent Searches', 'description': 'Save recent city searches to local storage. Display them as quick-access buttons.', 'technologies': ['Local Storage', 'JavaScript', 'Data Persistence'], 'estimated_time': 60, 'learning_outcomes': 'Local storage and data persistence'},
            {'step_number': 12, 'title': 'Polish and Deploy', 'description': 'Add final touches: animations, transitions, responsive improvements. Deploy to GitHub Pages or Netlify.', 'technologies': ['CSS', 'Git', 'Deployment'], 'estimated_time': 60, 'learning_outcomes': 'Final polish and deployment'},
        ]
        for step_data in steps_24h:
            ProjectStep.objects.create(project=project, timeframe='24h', **step_data)
        
        steps_48h = steps_24h + [
            {'step_number': 13, 'title': 'Add Weather Maps', 'description': 'Integrate a weather map showing current conditions. Use a mapping library like Leaflet or Google Maps.', 'technologies': ['Maps API', 'JavaScript', 'API Integration'], 'estimated_time': 120, 'learning_outcomes': 'Map integration and advanced APIs'},
            {'step_number': 14, 'title': 'Add Weather Alerts', 'description': 'Display weather alerts and warnings. Show severe weather notifications from the API.', 'technologies': ['API', 'Notifications', 'UX'], 'estimated_time': 75, 'learning_outcomes': 'Alert systems and notifications'},
            {'step_number': 15, 'title': 'Add Historical Data', 'description': 'Show historical weather data and trends. Create charts showing temperature patterns.', 'technologies': ['Data Visualization', 'Charts', 'Historical Data'], 'estimated_time': 90, 'learning_outcomes': 'Data visualization and charting'},
            {'step_number': 16, 'title': 'Add Multiple Locations', 'description': 'Allow users to save multiple favorite locations. Implement location management and switching.', 'technologies': ['Data Management', 'Local Storage', 'UI'], 'estimated_time': 75, 'learning_outcomes': 'Multi-location management'},
        ]
        for step_data in steps_48h:
            ProjectStep.objects.create(project=project, timeframe='48h', **step_data)
    
    def _add_calculator_steps(self, project):
        """Add steps for Calculator App"""
        steps_6h = [
            {'step_number': 1, 'title': 'Setup and HTML Structure', 'description': 'Create the HTML structure for your calculator: display screen, number buttons (0-9), operation buttons (+, -, *, /), equals, and clear button.', 'technologies': ['HTML', 'Semantic HTML'], 'estimated_time': 30, 'learning_outcomes': 'HTML structure for interactive components'},
            {'step_number': 2, 'title': 'Style the Calculator', 'description': 'Design a modern calculator UI with CSS. Use CSS Grid or Flexbox for button layout. Add hover and active states.', 'technologies': ['CSS', 'CSS Grid', 'UI Design'], 'estimated_time': 90, 'learning_outcomes': 'CSS Grid/Flexbox and UI styling'},
            {'step_number': 3, 'title': 'Implement Button Click Handlers', 'description': 'Add event listeners to all buttons. Log button clicks to console. Understand event delegation.', 'technologies': ['JavaScript', 'Event Listeners', 'Event Delegation'], 'estimated_time': 45, 'learning_outcomes': 'Event handling in JavaScript'},
            {'step_number': 4, 'title': 'Implement Number Input', 'description': 'Handle number button clicks. Display numbers on the calculator screen. Handle multi-digit numbers.', 'technologies': ['JavaScript', 'DOM Manipulation', 'String Manipulation'], 'estimated_time': 60, 'learning_outcomes': 'DOM updates and string operations'},
            {'step_number': 5, 'title': 'Implement Basic Operations', 'description': 'Add functionality for addition, subtraction, multiplication, and division. Store the operator and first number, then calculate on equals.', 'technologies': ['JavaScript', 'Arithmetic Operations', 'State Management'], 'estimated_time': 90, 'learning_outcomes': 'JavaScript logic and state management'},
            {'step_number': 6, 'title': 'Add Clear and Polish', 'description': 'Implement clear functionality. Handle edge cases (division by zero, etc.). Polish the UI and add smooth transitions.', 'technologies': ['JavaScript', 'Error Handling', 'UX'], 'estimated_time': 45, 'learning_outcomes': 'Error handling and UX polish'},
        ]
        for step_data in steps_6h:
            ProjectStep.objects.create(project=project, timeframe='6h', **step_data)
        
        steps_12h = steps_6h + [
            {'step_number': 7, 'title': 'Add Advanced Operations', 'description': 'Implement square root, percentage, and power operations. Add more mathematical functions.', 'technologies': ['JavaScript', 'Math Operations'], 'estimated_time': 60, 'learning_outcomes': 'Advanced mathematical operations'},
            {'step_number': 8, 'title': 'Add Memory Functions', 'description': 'Implement memory functions: M+, M-, MR, MC. Store values in memory and recall them.', 'technologies': ['JavaScript', 'State Management'], 'estimated_time': 75, 'learning_outcomes': 'Memory management in applications'},
        ]
        for step_data in steps_12h:
            ProjectStep.objects.create(project=project, timeframe='12h', **step_data)
        
        steps_24h = steps_12h + [
            {'step_number': 9, 'title': 'Add History Feature', 'description': 'Keep a history of calculations. Display previous calculations and allow users to reuse results.', 'technologies': ['JavaScript', 'Data Storage', 'UI'], 'estimated_time': 90, 'learning_outcomes': 'History tracking and data persistence'},
            {'step_number': 10, 'title': 'Add Keyboard Support', 'description': 'Allow users to use keyboard to input numbers and operations. Handle keyboard events.', 'technologies': ['JavaScript', 'Keyboard Events'], 'estimated_time': 60, 'learning_outcomes': 'Keyboard event handling'},
            {'step_number': 11, 'title': 'Add Scientific Mode', 'description': 'Create a scientific calculator mode with trigonometric functions, logarithms, and constants.', 'technologies': ['JavaScript', 'Advanced Math'], 'estimated_time': 120, 'learning_outcomes': 'Advanced calculator features'},
        ]
        for step_data in steps_24h:
            ProjectStep.objects.create(project=project, timeframe='24h', **step_data)
    
    def _add_react_todo_steps(self, project):
        """Add steps for React Todo App"""
        steps_12h = [
            {'step_number': 1, 'title': 'Setup React Project', 'description': 'Create a new React app using Create React App or Vite. Understand the project structure, JSX, and component basics.', 'technologies': ['React', 'Create React App', 'JSX'], 'estimated_time': 30, 'learning_outcomes': 'React project setup and JSX syntax'},
            {'step_number': 2, 'title': 'Create Todo Component', 'description': 'Build a basic Todo component. Understand functional components, props, and component structure.', 'technologies': ['React', 'Components', 'Props'], 'estimated_time': 60, 'learning_outcomes': 'React component architecture'},
            {'step_number': 3, 'title': 'Implement useState Hook', 'description': 'Use useState to manage todo list state. Add functionality to create new todos.', 'technologies': ['React Hooks', 'useState', 'State Management'], 'estimated_time': 60, 'learning_outcomes': 'React hooks and state management'},
            {'step_number': 4, 'title': 'Add Todo Operations', 'description': 'Implement complete, delete, and edit functionality. Learn about updating state immutably.', 'technologies': ['React', 'State Updates', 'Immutability'], 'estimated_time': 90, 'learning_outcomes': 'State updates and immutability in React'},
            {'step_number': 5, 'title': 'Add Filtering', 'description': 'Implement filter functionality (All, Active, Completed). Use conditional rendering to show filtered todos.', 'technologies': ['React', 'Conditional Rendering', 'Array Methods'], 'estimated_time': 60, 'learning_outcomes': 'Conditional rendering and filtering'},
            {'step_number': 6, 'title': 'Add Local Storage', 'description': 'Use useEffect to save todos to local storage and load them on mount. Learn about React lifecycle.', 'technologies': ['React Hooks', 'useEffect', 'Local Storage'], 'estimated_time': 75, 'learning_outcomes': 'useEffect hook and side effects'},
            {'step_number': 7, 'title': 'Style with CSS Modules', 'description': 'Style your React components using CSS Modules or styled-components. Make it look professional.', 'technologies': ['CSS Modules', 'React Styling'], 'estimated_time': 60, 'learning_outcomes': 'Styling React applications'},
            {'step_number': 8, 'title': 'Deploy to Netlify/Vercel', 'description': 'Build your React app and deploy to Netlify or Vercel. Understand the build process and deployment.', 'technologies': ['Build Process', 'Deployment', 'Netlify/Vercel'], 'estimated_time': 45, 'learning_outcomes': 'React app deployment'},
        ]
        for step_data in steps_12h:
            ProjectStep.objects.create(project=project, timeframe='12h', **step_data)
        
        steps_6h = steps_12h[:5]
        for step_data in steps_6h:
            ProjectStep.objects.create(project=project, timeframe='6h', **step_data)
    
    def _add_react_weather_steps(self, project):
        """Add steps for React Weather Dashboard"""
        steps_24h = [
            {'step_number': 1, 'title': 'Setup React Project', 'description': 'Create a new React app. Set up project structure and install necessary dependencies (axios, etc.).', 'technologies': ['React', 'npm', 'Dependencies'], 'estimated_time': 30, 'learning_outcomes': 'React project setup'},
            {'step_number': 2, 'title': 'Create Weather API Service', 'description': 'Set up API key and create a service module for weather API calls. Understand API integration.', 'technologies': ['API', 'Axios', 'Service Layer'], 'estimated_time': 45, 'learning_outcomes': 'API integration and service architecture'},
            {'step_number': 3, 'title': 'Build Weather Component', 'description': 'Create a Weather component that displays current weather. Use useState to manage weather data.', 'technologies': ['React', 'Components', 'useState'], 'estimated_time': 90, 'learning_outcomes': 'Component design and state management'},
            {'step_number': 4, 'title': 'Implement useEffect for API Calls', 'description': 'Use useEffect to fetch weather data when component mounts or city changes. Handle loading states.', 'technologies': ['React Hooks', 'useEffect', 'Async Operations'], 'estimated_time': 90, 'learning_outcomes': 'useEffect and async operations'},
            {'step_number': 5, 'title': 'Add Search Functionality', 'description': 'Create a search component. Handle user input and trigger API calls. Implement error handling.', 'technologies': ['React', 'Forms', 'Error Handling'], 'estimated_time': 75, 'learning_outcomes': 'Form handling and error states'},
            {'step_number': 6, 'title': 'Add Forecast Component', 'description': 'Create a Forecast component to display 5-day weather forecast. Learn about component composition.', 'technologies': ['React', 'Component Composition', 'Props'], 'estimated_time': 90, 'learning_outcomes': 'Component composition and reusability'},
            {'step_number': 7, 'title': 'Implement Custom Hooks', 'description': 'Create a custom useWeather hook to encapsulate weather logic. Learn about custom hooks pattern.', 'technologies': ['React', 'Custom Hooks', 'Code Organization'], 'estimated_time': 75, 'learning_outcomes': 'Custom hooks and code organization'},
            {'step_number': 8, 'title': 'Add Context for Global State', 'description': 'Use React Context to manage global state (recent searches, favorites). Learn about context API.', 'technologies': ['React Context', 'Global State'], 'estimated_time': 90, 'learning_outcomes': 'Context API and global state management'},
            {'step_number': 9, 'title': 'Style with CSS-in-JS', 'description': 'Style your dashboard using styled-components or CSS modules. Create a beautiful, responsive UI.', 'technologies': ['Styled Components', 'CSS-in-JS'], 'estimated_time': 90, 'learning_outcomes': 'Modern React styling approaches'},
            {'step_number': 10, 'title': 'Add Animations', 'description': 'Add smooth transitions and animations using CSS or animation libraries. Enhance user experience.', 'technologies': ['CSS Animations', 'React Transitions'], 'estimated_time': 60, 'learning_outcomes': 'Animations in React'},
            {'step_number': 11, 'title': 'Optimize Performance', 'description': 'Use React.memo, useMemo, and useCallback to optimize performance. Understand React optimization.', 'technologies': ['React Optimization', 'Performance'], 'estimated_time': 75, 'learning_outcomes': 'React performance optimization'},
            {'step_number': 12, 'title': 'Deploy Application', 'description': 'Build and deploy your React app. Set up environment variables for API keys.', 'technologies': ['Deployment', 'Environment Variables'], 'estimated_time': 45, 'learning_outcomes': 'Production deployment'},
        ]
        for step_data in steps_24h:
            ProjectStep.objects.create(project=project, timeframe='24h', **step_data)
        
        steps_12h = steps_24h[:8]
        for step_data in steps_12h:
            ProjectStep.objects.create(project=project, timeframe='12h', **step_data)
        
        steps_6h = steps_24h[:5]
        for step_data in steps_6h:
            ProjectStep.objects.create(project=project, timeframe='6h', **step_data)
        
        steps_48h = steps_24h + [
            {'step_number': 13, 'title': 'Add Weather Maps Integration', 'description': 'Integrate weather maps using Leaflet or Google Maps. Show weather conditions on a map.', 'technologies': ['Maps API', 'React', 'Integration'], 'estimated_time': 120, 'learning_outcomes': 'Map integration in React'},
            {'step_number': 14, 'title': 'Add Weather Alerts System', 'description': 'Implement weather alerts and notifications. Show severe weather warnings.', 'technologies': ['Notifications', 'React', 'UX'], 'estimated_time': 90, 'learning_outcomes': 'Alert systems'},
        ]
        for step_data in steps_48h:
            ProjectStep.objects.create(project=project, timeframe='48h', **step_data)
    
    def _add_flask_api_steps(self, project):
        """Add steps for Flask REST API"""
        steps_12h = [
            {'step_number': 1, 'title': 'Setup Python Environment', 'description': 'Create a virtual environment, install Flask and Flask-RESTful. Set up project structure.', 'technologies': ['Python', 'Virtual Environment', 'Flask'], 'estimated_time': 30, 'learning_outcomes': 'Python environment setup'},
            {'step_number': 2, 'title': 'Create Flask App', 'description': 'Initialize Flask application. Set up basic routes and understand Flask routing.', 'technologies': ['Flask', 'Routing', 'Python'], 'estimated_time': 45, 'learning_outcomes': 'Flask basics and routing'},
            {'step_number': 3, 'title': 'Create Data Models', 'description': 'Design your data structure. Create Python classes or use a simple in-memory data store.', 'technologies': ['Python', 'Data Modeling'], 'estimated_time': 60, 'learning_outcomes': 'Data modeling and structure'},
            {'step_number': 4, 'title': 'Implement GET Endpoints', 'description': 'Create GET endpoints to retrieve data. Return JSON responses. Understand HTTP methods.', 'technologies': ['REST API', 'HTTP Methods', 'JSON'], 'estimated_time': 75, 'learning_outcomes': 'REST API design and JSON responses'},
            {'step_number': 5, 'title': 'Implement POST Endpoint', 'description': 'Create POST endpoint to add new data. Handle request data, validate input, and return appropriate responses.', 'technologies': ['REST API', 'Request Handling', 'Validation'], 'estimated_time': 90, 'learning_outcomes': 'Request handling and validation'},
            {'step_number': 6, 'title': 'Implement PUT/PATCH Endpoints', 'description': 'Add endpoints to update existing data. Understand the difference between PUT and PATCH.', 'technologies': ['REST API', 'HTTP Methods'], 'estimated_time': 75, 'learning_outcomes': 'Update operations in REST APIs'},
            {'step_number': 7, 'title': 'Implement DELETE Endpoint', 'description': 'Add DELETE endpoint to remove data. Handle errors for non-existent resources.', 'technologies': ['REST API', 'Error Handling'], 'estimated_time': 45, 'learning_outcomes': 'Delete operations and error handling'},
            {'step_number': 8, 'title': 'Add Error Handling', 'description': 'Implement proper error handling. Return appropriate HTTP status codes and error messages.', 'technologies': ['Error Handling', 'HTTP Status Codes'], 'estimated_time': 60, 'learning_outcomes': 'Error handling in APIs'},
            {'step_number': 9, 'title': 'Test API with Postman', 'description': 'Test all endpoints using Postman. Verify request/response formats and error cases.', 'technologies': ['API Testing', 'Postman'], 'estimated_time': 60, 'learning_outcomes': 'API testing and debugging'},
            {'step_number': 10, 'title': 'Add CORS Support', 'description': 'Configure CORS to allow frontend applications to access your API. Understand cross-origin requests.', 'technologies': ['CORS', 'Flask-CORS'], 'estimated_time': 30, 'learning_outcomes': 'CORS and cross-origin requests'},
        ]
        for step_data in steps_12h:
            ProjectStep.objects.create(project=project, timeframe='12h', **step_data)
        
        steps_6h = steps_12h[:6]
        for step_data in steps_6h:
            ProjectStep.objects.create(project=project, timeframe='6h', **step_data)
        
        steps_24h = steps_12h + [
            {'step_number': 11, 'title': 'Add Database Integration', 'description': 'Integrate SQLite or PostgreSQL database. Replace in-memory storage with persistent database.', 'technologies': ['Database', 'SQLAlchemy', 'Flask'], 'estimated_time': 120, 'learning_outcomes': 'Database integration'},
            {'step_number': 12, 'title': 'Add Authentication', 'description': 'Implement user authentication with JWT tokens. Secure API endpoints.', 'technologies': ['Authentication', 'JWT', 'Security'], 'estimated_time': 120, 'learning_outcomes': 'API authentication'},
        ]
        for step_data in steps_24h:
            ProjectStep.objects.create(project=project, timeframe='24h', **step_data)
        
        steps_48h = steps_24h + [
            {'step_number': 13, 'title': 'Add Rate Limiting', 'description': 'Implement rate limiting to prevent abuse. Add request throttling.', 'technologies': ['Rate Limiting', 'Security'], 'estimated_time': 75, 'learning_outcomes': 'API security'},
            {'step_number': 14, 'title': 'Add API Documentation', 'description': 'Create comprehensive API documentation using Swagger/OpenAPI.', 'technologies': ['API Documentation', 'Swagger'], 'estimated_time': 90, 'learning_outcomes': 'API documentation'},
        ]
        for step_data in steps_48h:
            ProjectStep.objects.create(project=project, timeframe='48h', **step_data)
    
    def _add_nodejs_api_steps(self, project):
        """Add steps for Node.js Express API"""
        steps_12h = [
            {'step_number': 1, 'title': 'Setup Node.js Project', 'description': 'Initialize npm project, install Express. Set up project structure and understand package.json.', 'technologies': ['Node.js', 'npm', 'Express'], 'estimated_time': 30, 'learning_outcomes': 'Node.js project setup'},
            {'step_number': 2, 'title': 'Create Express Server', 'description': 'Set up Express server, create basic routes. Understand middleware and request/response cycle.', 'technologies': ['Express', 'Middleware', 'Routing'], 'estimated_time': 60, 'learning_outcomes': 'Express basics and middleware'},
            {'step_number': 3, 'title': 'Setup Data Storage', 'description': 'Set up in-memory data store or use a simple JSON file. Understand data persistence options.', 'technologies': ['Node.js', 'File System', 'Data Storage'], 'estimated_time': 45, 'learning_outcomes': 'Data storage in Node.js'},
            {'step_number': 4, 'title': 'Implement GET Routes', 'description': 'Create GET routes to retrieve data. Return JSON responses. Handle route parameters.', 'technologies': ['Express', 'REST API', 'Route Parameters'], 'estimated_time': 75, 'learning_outcomes': 'REST API routes and parameters'},
            {'step_number': 5, 'title': 'Implement POST Route', 'description': 'Create POST route to add data. Parse request body, validate input, handle errors.', 'technologies': ['Express', 'Body Parser', 'Validation'], 'estimated_time': 90, 'learning_outcomes': 'Request body parsing and validation'},
            {'step_number': 6, 'title': 'Implement PUT/DELETE Routes', 'description': 'Add routes to update and delete data. Handle resource identification and errors.', 'technologies': ['Express', 'REST API'], 'estimated_time': 75, 'learning_outcomes': 'Update and delete operations'},
            {'step_number': 7, 'title': 'Add Middleware', 'description': 'Create custom middleware for logging, error handling, and request validation.', 'technologies': ['Express', 'Middleware'], 'estimated_time': 60, 'learning_outcomes': 'Custom middleware creation'},
            {'step_number': 8, 'title': 'Add Error Handling', 'description': 'Implement error handling middleware. Return appropriate status codes and error messages.', 'technologies': ['Error Handling', 'Express Middleware'], 'estimated_time': 60, 'learning_outcomes': 'Error handling patterns'},
            {'step_number': 9, 'title': 'Test with Postman', 'description': 'Test all API endpoints. Verify responses and error handling.', 'technologies': ['API Testing', 'Postman'], 'estimated_time': 60, 'learning_outcomes': 'API testing'},
            {'step_number': 10, 'title': 'Deploy to Heroku/Railway', 'description': 'Deploy your Node.js API to a cloud platform. Set up environment variables and process management.', 'technologies': ['Deployment', 'Heroku/Railway'], 'estimated_time': 75, 'learning_outcomes': 'Node.js deployment'},
        ]
        for step_data in steps_12h:
            ProjectStep.objects.create(project=project, timeframe='12h', **step_data)
        
        steps_6h = steps_12h[:6]
        for step_data in steps_6h:
            ProjectStep.objects.create(project=project, timeframe='6h', **step_data)
        
        steps_24h = steps_12h + [
            {'step_number': 11, 'title': 'Add Database Integration', 'description': 'Integrate MongoDB or PostgreSQL. Replace in-memory storage with persistent database.', 'technologies': ['Database', 'MongoDB/PostgreSQL', 'Node.js'], 'estimated_time': 120, 'learning_outcomes': 'Database integration'},
            {'step_number': 12, 'title': 'Add Authentication', 'description': 'Implement JWT authentication. Secure API endpoints with middleware.', 'technologies': ['Authentication', 'JWT', 'Middleware'], 'estimated_time': 120, 'learning_outcomes': 'API authentication'},
        ]
        for step_data in steps_24h:
            ProjectStep.objects.create(project=project, timeframe='24h', **step_data)
        
        steps_48h = steps_24h + [
            {'step_number': 13, 'title': 'Add Rate Limiting', 'description': 'Implement rate limiting middleware. Prevent API abuse.', 'technologies': ['Rate Limiting', 'Security'], 'estimated_time': 75, 'learning_outcomes': 'API security'},
            {'step_number': 14, 'title': 'Add API Documentation', 'description': 'Create API documentation using Swagger or Postman collections.', 'technologies': ['API Documentation', 'Swagger'], 'estimated_time': 90, 'learning_outcomes': 'API documentation'},
        ]
        for step_data in steps_48h:
            ProjectStep.objects.create(project=project, timeframe='48h', **step_data)
    
    def _add_django_api_steps(self, project):
        """Add steps for Django REST API"""
        steps_24h = [
            {'step_number': 1, 'title': 'Setup Django Project', 'description': 'Create Django project and app. Install Django REST Framework. Understand Django project structure.', 'technologies': ['Django', 'Django REST Framework'], 'estimated_time': 45, 'learning_outcomes': 'Django project setup'},
            {'step_number': 2, 'title': 'Create Models', 'description': 'Design and create Django models for blog posts, comments, etc. Understand Django ORM.', 'technologies': ['Django ORM', 'Models', 'Database'], 'estimated_time': 90, 'learning_outcomes': 'Django models and database design'},
            {'step_number': 3, 'title': 'Run Migrations', 'description': 'Create and apply database migrations. Understand Django migration system.', 'technologies': ['Django Migrations', 'Database'], 'estimated_time': 30, 'learning_outcomes': 'Database migrations'},
            {'step_number': 4, 'title': 'Create Serializers', 'description': 'Create DRF serializers for your models. Understand serialization and deserialization.', 'technologies': ['Django REST Framework', 'Serializers'], 'estimated_time': 90, 'learning_outcomes': 'DRF serializers'},
            {'step_number': 5, 'title': 'Create ViewSets', 'description': 'Create ViewSets for CRUD operations. Understand ViewSets vs APIViews.', 'technologies': ['Django REST Framework', 'ViewSets'], 'estimated_time': 90, 'learning_outcomes': 'ViewSets and CRUD operations'},
            {'step_number': 6, 'title': 'Configure URL Routing', 'description': 'Set up URL routing using DRF routers. Register ViewSets with routers.', 'technologies': ['Django', 'URL Routing', 'Routers'], 'estimated_time': 45, 'learning_outcomes': 'URL routing in Django'},
            {'step_number': 7, 'title': 'Add Authentication', 'description': 'Implement token authentication or session authentication. Secure your API endpoints.', 'technologies': ['Authentication', 'Django REST Framework'], 'estimated_time': 90, 'learning_outcomes': 'API authentication'},
            {'step_number': 8, 'title': 'Add Permissions', 'description': 'Set up permissions for different user roles. Understand DRF permission classes.', 'technologies': ['Permissions', 'Django REST Framework'], 'estimated_time': 75, 'learning_outcomes': 'API permissions and authorization'},
            {'step_number': 9, 'title': 'Add Filtering and Pagination', 'description': 'Implement filtering and pagination for list endpoints. Use DRF filter backends.', 'technologies': ['Filtering', 'Pagination', 'Django REST Framework'], 'estimated_time': 75, 'learning_outcomes': 'API filtering and pagination'},
            {'step_number': 10, 'title': 'Test API Endpoints', 'description': 'Test all endpoints using DRF browsable API or Postman. Verify CRUD operations.', 'technologies': ['API Testing', 'Django REST Framework'], 'estimated_time': 60, 'learning_outcomes': 'API testing'},
            {'step_number': 11, 'title': 'Add API Documentation', 'description': 'Set up API documentation using Swagger or DRF schema. Document your endpoints.', 'technologies': ['API Documentation', 'Swagger'], 'estimated_time': 60, 'learning_outcomes': 'API documentation'},
            {'step_number': 12, 'title': 'Deploy to Production', 'description': 'Deploy your Django API to a cloud platform. Set up environment variables and database.', 'technologies': ['Deployment', 'Django', 'Production'], 'estimated_time': 90, 'learning_outcomes': 'Production deployment'},
        ]
        for step_data in steps_24h:
            ProjectStep.objects.create(project=project, timeframe='24h', **step_data)
        
        steps_12h = steps_24h[:8]
        for step_data in steps_12h:
            ProjectStep.objects.create(project=project, timeframe='12h', **step_data)
        
        steps_6h = steps_24h[:5]
        for step_data in steps_6h:
            ProjectStep.objects.create(project=project, timeframe='6h', **step_data)
        
        steps_48h = steps_24h + [
            {'step_number': 13, 'title': 'Add Caching', 'description': 'Implement Redis caching for improved performance. Cache frequently accessed data.', 'technologies': ['Caching', 'Redis', 'Performance'], 'estimated_time': 90, 'learning_outcomes': 'Caching strategies'},
            {'step_number': 14, 'title': 'Add Background Tasks', 'description': 'Implement Celery for background tasks. Handle async operations.', 'technologies': ['Celery', 'Background Tasks'], 'estimated_time': 120, 'learning_outcomes': 'Background task processing'},
        ]
        for step_data in steps_48h:
            ProjectStep.objects.create(project=project, timeframe='48h', **step_data)
    
    def _add_python_data_steps(self, project):
        """Add steps for Python Data Analysis"""
        steps_12h = [
            {'step_number': 1, 'title': 'Setup Python Environment', 'description': 'Install pandas, matplotlib, and numpy. Set up Jupyter notebook or Python script environment.', 'technologies': ['Python', 'pandas', 'matplotlib'], 'estimated_time': 30, 'learning_outcomes': 'Python environment and libraries'},
            {'step_number': 2, 'title': 'Load Dataset', 'description': 'Download or use a sample dataset (CSV file). Load data into pandas DataFrame.', 'technologies': ['pandas', 'Data Loading', 'CSV'], 'estimated_time': 45, 'learning_outcomes': 'Loading data with pandas'},
            {'step_number': 3, 'title': 'Explore Data', 'description': 'Use pandas methods to explore data: head(), info(), describe(). Understand your dataset.', 'technologies': ['pandas', 'Data Exploration'], 'estimated_time': 60, 'learning_outcomes': 'Data exploration techniques'},
            {'step_number': 4, 'title': 'Clean Data', 'description': 'Handle missing values, remove duplicates, fix data types. Clean and prepare data for analysis.', 'technologies': ['pandas', 'Data Cleaning'], 'estimated_time': 90, 'learning_outcomes': 'Data cleaning and preprocessing'},
            {'step_number': 5, 'title': 'Perform Basic Analysis', 'description': 'Calculate statistics: mean, median, mode, standard deviation. Understand data distribution.', 'technologies': ['pandas', 'Statistics'], 'estimated_time': 75, 'learning_outcomes': 'Statistical analysis'},
            {'step_number': 6, 'title': 'Create Visualizations', 'description': 'Create charts: bar charts, line plots, histograms using matplotlib. Visualize your findings.', 'technologies': ['matplotlib', 'Data Visualization'], 'estimated_time': 90, 'learning_outcomes': 'Data visualization'},
            {'step_number': 7, 'title': 'Generate Insights', 'description': 'Analyze patterns, correlations, and trends. Write summary of findings.', 'technologies': ['Data Analysis', 'Insights'], 'estimated_time': 90, 'learning_outcomes': 'Data analysis and insights'},
            {'step_number': 8, 'title': 'Export Results', 'description': 'Export cleaned data and visualizations. Create a report with your findings.', 'technologies': ['pandas', 'Export', 'Reporting'], 'estimated_time': 45, 'learning_outcomes': 'Exporting and reporting'},
        ]
        for step_data in steps_12h:
            ProjectStep.objects.create(project=project, timeframe='12h', **step_data)
        
        steps_6h = steps_12h[:5]
        for step_data in steps_6h:
            ProjectStep.objects.create(project=project, timeframe='6h', **step_data)
        
        steps_24h = steps_12h + [
            {'step_number': 9, 'title': 'Advanced Data Analysis', 'description': 'Perform correlation analysis, statistical tests, and hypothesis testing.', 'technologies': ['Statistics', 'pandas', 'scipy'], 'estimated_time': 120, 'learning_outcomes': 'Advanced statistical analysis'},
            {'step_number': 10, 'title': 'Create Interactive Dashboards', 'description': 'Build interactive dashboards using Plotly or Streamlit. Create user-friendly interfaces.', 'technologies': ['Plotly', 'Streamlit', 'Dashboards'], 'estimated_time': 120, 'learning_outcomes': 'Interactive data visualization'},
        ]
        for step_data in steps_24h:
            ProjectStep.objects.create(project=project, timeframe='24h', **step_data)
        
        steps_48h = steps_24h + [
            {'step_number': 11, 'title': 'Machine Learning Basics', 'description': 'Add simple machine learning models. Predict trends using linear regression.', 'technologies': ['Machine Learning', 'scikit-learn'], 'estimated_time': 150, 'learning_outcomes': 'Introduction to ML'},
            {'step_number': 12, 'title': 'Export to Web Application', 'description': 'Create a web application to display your analysis. Use Flask or Streamlit.', 'technologies': ['Web App', 'Flask/Streamlit'], 'estimated_time': 120, 'learning_outcomes': 'Data science web applications'},
        ]
        for step_data in steps_48h:
            ProjectStep.objects.create(project=project, timeframe='48h', **step_data)
    
    def _add_python_data_resources(self, project):
        """Add downloadable CSV resources for Data Analysis project"""
        resources = [
            {
                'name': 'Sales Data Sample',
                'description': 'Sample sales data with dates, products, quantities, and revenue',
                'resource_type': 'csv',
                'file_path': 'sales_data.csv',
                'file_size': '15 KB',
                'order': 1,
            },
            {
                'name': 'Customer Data Sample',
                'description': 'Customer demographics and purchase history data',
                'resource_type': 'csv',
                'file_path': 'customer_data.csv',
                'file_size': '12 KB',
                'order': 2,
            },
            {
                'name': 'Weather Data Sample',
                'description': 'Historical weather data with temperature, humidity, and precipitation',
                'resource_type': 'csv',
                'file_path': 'weather_data.csv',
                'file_size': '18 KB',
                'order': 3,
            },
        ]
        for resource_data in resources:
            ProjectResource.objects.get_or_create(
                project=project,
                name=resource_data['name'],
                defaults=resource_data
            )
    
    def _add_python_automation_steps(self, project):
        """Add steps for Python Automation"""
        steps_12h = [
            {'step_number': 1, 'title': 'Setup Project', 'description': 'Create Python script. Import necessary modules: os, shutil, pathlib. Understand file operations.', 'technologies': ['Python', 'File System'], 'estimated_time': 30, 'learning_outcomes': 'Python file operations'},
            {'step_number': 2, 'title': 'List Files in Directory', 'description': 'Write code to list all files in a directory. Understand directory traversal.', 'technologies': ['Python', 'os module', 'pathlib'], 'estimated_time': 45, 'learning_outcomes': 'Directory operations'},
            {'step_number': 3, 'title': 'Identify File Types', 'description': 'Group files by extension (.jpg, .pdf, .txt, etc.). Use pathlib to get file extensions.', 'technologies': ['Python', 'pathlib', 'File Types'], 'estimated_time': 60, 'learning_outcomes': 'File type identification'},
            {'step_number': 4, 'title': 'Create Organization Logic', 'description': 'Design folder structure (Documents, Images, Videos, etc.). Create organization rules.', 'technologies': ['Python', 'Logic Design'], 'estimated_time': 60, 'learning_outcomes': 'Algorithm design'},
            {'step_number': 5, 'title': 'Move Files to Folders', 'description': 'Implement file moving logic. Create destination folders if they don\'t exist. Move files safely.', 'technologies': ['Python', 'shutil', 'File Operations'], 'estimated_time': 90, 'learning_outcomes': 'File operations and error handling'},
            {'step_number': 6, 'title': 'Add Logging', 'description': 'Add logging to track what files were moved. Create a log file with operations performed.', 'technologies': ['Python', 'Logging'], 'estimated_time': 45, 'learning_outcomes': 'Logging in Python'},
            {'step_number': 7, 'title': 'Add Safety Features', 'description': 'Add confirmation prompts, dry-run mode, and error handling. Make script safe to use.', 'technologies': ['Python', 'Error Handling', 'Safety'], 'estimated_time': 75, 'learning_outcomes': 'Safe scripting practices'},
            {'step_number': 8, 'title': 'Test and Refine', 'description': 'Test script on sample directory. Handle edge cases. Refine and improve the script.', 'technologies': ['Python', 'Testing'], 'estimated_time': 60, 'learning_outcomes': 'Testing and refinement'},
        ]
        for step_data in steps_12h:
            ProjectStep.objects.create(project=project, timeframe='12h', **step_data)
        
        steps_6h = steps_12h[:5]
        for step_data in steps_6h:
            ProjectStep.objects.create(project=project, timeframe='6h', **step_data)
        
        steps_24h = steps_12h + [
            {'step_number': 9, 'title': 'Add Scheduling Features', 'description': 'Add scheduling capabilities. Run script at specific times using cron or task scheduler.', 'technologies': ['Scheduling', 'cron', 'Task Scheduler'], 'estimated_time': 90, 'learning_outcomes': 'Task scheduling'},
            {'step_number': 10, 'title': 'Add GUI Interface', 'description': 'Create a GUI using tkinter or PyQt. Make the script user-friendly with a graphical interface.', 'technologies': ['GUI', 'tkinter', 'PyQt'], 'estimated_time': 120, 'learning_outcomes': 'GUI development'},
        ]
        for step_data in steps_24h:
            ProjectStep.objects.create(project=project, timeframe='24h', **step_data)
        
        steps_48h = steps_24h + [
            {'step_number': 11, 'title': 'Add Cloud Integration', 'description': 'Integrate with cloud storage (Google Drive, Dropbox). Organize files across cloud services.', 'technologies': ['Cloud APIs', 'Integration'], 'estimated_time': 120, 'learning_outcomes': 'Cloud service integration'},
            {'step_number': 12, 'title': 'Add Web Interface', 'description': 'Create a web interface using Flask. Allow users to organize files through a browser.', 'technologies': ['Flask', 'Web Interface'], 'estimated_time': 150, 'learning_outcomes': 'Web application development'},
        ]
        for step_data in steps_48h:
            ProjectStep.objects.create(project=project, timeframe='48h', **step_data)
    
    def _add_fullstack_todo_steps(self, project):
        """Add steps for Full-Stack Todo App"""
        steps_24h = [
            {'step_number': 1, 'title': 'Setup Backend (Node.js/Express)', 'description': 'Create Express server, set up routes, create in-memory or file-based data store.', 'technologies': ['Node.js', 'Express', 'Backend'], 'estimated_time': 90, 'learning_outcomes': 'Backend API setup'},
            {'step_number': 2, 'title': 'Implement Backend CRUD', 'description': 'Create GET, POST, PUT, DELETE endpoints for todos. Test with Postman.', 'technologies': ['REST API', 'CRUD Operations'], 'estimated_time': 120, 'learning_outcomes': 'REST API implementation'},
            {'step_number': 3, 'title': 'Setup Frontend (React)', 'description': 'Create React app. Set up project structure and install axios for API calls.', 'technologies': ['React', 'Frontend Setup'], 'estimated_time': 45, 'learning_outcomes': 'Frontend setup'},
            {'step_number': 4, 'title': 'Create API Service', 'description': 'Create service module to handle API calls. Use axios to communicate with backend.', 'technologies': ['Axios', 'API Integration'], 'estimated_time': 60, 'learning_outcomes': 'Frontend-backend communication'},
            {'step_number': 5, 'title': 'Build Todo Components', 'description': 'Create React components for displaying todos. Use useState to manage local state.', 'technologies': ['React', 'Components', 'State'], 'estimated_time': 90, 'learning_outcomes': 'React component development'},
            {'step_number': 6, 'title': 'Connect Frontend to Backend', 'description': 'Make API calls from React to fetch and display todos. Handle loading and error states.', 'technologies': ['API Integration', 'React', 'Error Handling'], 'estimated_time': 120, 'learning_outcomes': 'Full-stack integration'},
            {'step_number': 7, 'title': 'Implement Create Todo', 'description': 'Add functionality to create new todos. Send POST request to backend and update UI.', 'technologies': ['REST API', 'React', 'State Management'], 'estimated_time': 75, 'learning_outcomes': 'Create operations'},
            {'step_number': 8, 'title': 'Implement Update and Delete', 'description': 'Add update and delete functionality. Handle PUT and DELETE requests.', 'technologies': ['REST API', 'React'], 'estimated_time': 90, 'learning_outcomes': 'Update and delete operations'},
            {'step_number': 9, 'title': 'Add CORS Configuration', 'description': 'Configure CORS on backend to allow frontend requests. Understand cross-origin requests.', 'technologies': ['CORS', 'Backend Configuration'], 'estimated_time': 30, 'learning_outcomes': 'CORS configuration'},
            {'step_number': 10, 'title': 'Handle Errors and Loading', 'description': 'Add proper error handling and loading states. Improve user experience.', 'technologies': ['Error Handling', 'UX'], 'estimated_time': 60, 'learning_outcomes': 'Error handling and UX'},
            {'step_number': 11, 'title': 'Style the Application', 'description': 'Style both frontend and ensure consistent design. Make it look professional.', 'technologies': ['CSS', 'Styling'], 'estimated_time': 90, 'learning_outcomes': 'Full-stack styling'},
            {'step_number': 12, 'title': 'Deploy Full-Stack App', 'description': 'Deploy backend and frontend separately. Set up environment variables and CORS for production.', 'technologies': ['Deployment', 'Full-Stack'], 'estimated_time': 120, 'learning_outcomes': 'Full-stack deployment'},
        ]
        for step_data in steps_24h:
            ProjectStep.objects.create(project=project, timeframe='24h', **step_data)
        
        steps_12h = steps_24h[:8]
        for step_data in steps_12h:
            ProjectStep.objects.create(project=project, timeframe='12h', **step_data)
        
        steps_6h = steps_24h[:5]
        for step_data in steps_6h:
            ProjectStep.objects.create(project=project, timeframe='6h', **step_data)
        
        steps_48h = steps_24h + [
            {'step_number': 13, 'title': 'Add Real-time Updates', 'description': 'Implement WebSockets for real-time collaboration. Multiple users can see updates instantly.', 'technologies': ['WebSockets', 'Socket.io', 'Real-time'], 'estimated_time': 120, 'learning_outcomes': 'Real-time web applications'},
            {'step_number': 14, 'title': 'Add User Authentication', 'description': 'Implement user authentication and authorization. Secure the application.', 'technologies': ['Authentication', 'JWT', 'Security'], 'estimated_time': 120, 'learning_outcomes': 'Full-stack authentication'},
        ]
        for step_data in steps_48h:
            ProjectStep.objects.create(project=project, timeframe='48h', **step_data)
    
    def _add_quiz_app_steps(self, project):
        """Add steps for Quiz App"""
        steps_6h = [
            {'step_number': 1, 'title': 'Setup and HTML Structure', 'description': 'Create HTML structure: question display, answer options, next button, score display, and result screen.', 'technologies': ['HTML', 'Semantic HTML'], 'estimated_time': 45, 'learning_outcomes': 'HTML structure for interactive apps'},
            {'step_number': 2, 'title': 'Style the Quiz App', 'description': 'Design a clean, engaging quiz interface with CSS. Style questions, buttons, and result screen.', 'technologies': ['CSS', 'UI Design'], 'estimated_time': 75, 'learning_outcomes': 'CSS styling and UI design'},
            {'step_number': 3, 'title': 'Create Question Data Structure', 'description': 'Set up JavaScript array with quiz questions, answers, and correct answer index.', 'technologies': ['JavaScript', 'Data Structures'], 'estimated_time': 45, 'learning_outcomes': 'Data structure design'},
            {'step_number': 4, 'title': 'Display Questions and Answers', 'description': 'Write JavaScript to display questions and answer options dynamically. Navigate through questions.', 'technologies': ['JavaScript', 'DOM Manipulation'], 'estimated_time': 90, 'learning_outcomes': 'Dynamic content rendering'},
            {'step_number': 5, 'title': 'Handle Answer Selection', 'description': 'Implement answer selection logic. Highlight selected answer and check if it\'s correct.', 'technologies': ['JavaScript', 'Event Handling'], 'estimated_time': 75, 'learning_outcomes': 'User interaction handling'},
            {'step_number': 6, 'title': 'Calculate and Display Score', 'description': 'Track correct answers, calculate score, and display final results with feedback.', 'technologies': ['JavaScript', 'Score Calculation'], 'estimated_time': 60, 'learning_outcomes': 'Score tracking and results display'},
        ]
        for step_data in steps_6h:
            ProjectStep.objects.create(project=project, timeframe='6h', **step_data)
        
        steps_12h = steps_6h + [
            {'step_number': 7, 'title': 'Add Timer Functionality', 'description': 'Implement countdown timer for each question. Handle timeout and auto-advance.', 'technologies': ['JavaScript', 'Timers', 'setInterval'], 'estimated_time': 60, 'learning_outcomes': 'Timer implementation'},
            {'step_number': 8, 'title': 'Add Multiple Quiz Categories', 'description': 'Create different quiz categories. Allow users to select quiz type.', 'technologies': ['JavaScript', 'Data Organization'], 'estimated_time': 75, 'learning_outcomes': 'Category management'},
        ]
        for step_data in steps_12h:
            ProjectStep.objects.create(project=project, timeframe='12h', **step_data)
        
        steps_24h = steps_12h + [
            {'step_number': 9, 'title': 'Add Progress Tracking', 'description': 'Show progress bar, question number, and percentage completion.', 'technologies': ['JavaScript', 'Progress Tracking'], 'estimated_time': 45, 'learning_outcomes': 'Progress visualization'},
            {'step_number': 10, 'title': 'Add Results History', 'description': 'Save quiz results to local storage. Display previous scores and statistics.', 'technologies': ['Local Storage', 'JavaScript'], 'estimated_time': 60, 'learning_outcomes': 'Data persistence'},
        ]
        for step_data in steps_24h:
            ProjectStep.objects.create(project=project, timeframe='24h', **step_data)
    
    def _add_recipe_finder_steps(self, project):
        """Add steps for Recipe Finder App"""
        steps_12h = [
            {'step_number': 1, 'title': 'Setup and API Key', 'description': 'Set up project and get API key from a recipe API (Spoonacular or Edamam). Understand API documentation.', 'technologies': ['API', 'API Keys'], 'estimated_time': 45, 'learning_outcomes': 'API setup and authentication'},
            {'step_number': 2, 'title': 'Create HTML Structure', 'description': 'Build HTML: search input, filter options, recipe cards container, and modal for recipe details.', 'technologies': ['HTML', 'Modal Design'], 'estimated_time': 60, 'learning_outcomes': 'HTML structure for data display'},
            {'step_number': 3, 'title': 'Style Recipe Cards', 'description': 'Design beautiful recipe cards with images, titles, cooking time, and difficulty. Make it responsive.', 'technologies': ['CSS', 'Card Design', 'Responsive'], 'estimated_time': 90, 'learning_outcomes': 'Card-based UI design'},
            {'step_number': 4, 'title': 'Implement Search Functionality', 'description': 'Create search form. Make API call on submit and handle response.', 'technologies': ['JavaScript', 'Fetch API', 'Forms'], 'estimated_time': 90, 'learning_outcomes': 'Search implementation'},
            {'step_number': 5, 'title': 'Display Recipe Results', 'description': 'Parse API response and display recipes in cards. Show images, titles, and basic info.', 'technologies': ['JavaScript', 'JSON', 'DOM'], 'estimated_time': 90, 'learning_outcomes': 'Data rendering'},
            {'step_number': 6, 'title': 'Add Recipe Details Modal', 'description': 'Create modal to show full recipe: ingredients, instructions, and nutritional info.', 'technologies': ['JavaScript', 'Modal', 'UI'], 'estimated_time': 75, 'learning_outcomes': 'Modal implementation'},
            {'step_number': 7, 'title': 'Add Filtering Options', 'description': 'Add filters: cuisine type, dietary restrictions, cooking time. Filter API results.', 'technologies': ['JavaScript', 'Filtering', 'API'], 'estimated_time': 90, 'learning_outcomes': 'Advanced filtering'},
            {'step_number': 8, 'title': 'Add Favorites Feature', 'description': 'Allow users to save favorite recipes to local storage. Display favorites section.', 'technologies': ['Local Storage', 'JavaScript'], 'estimated_time': 60, 'learning_outcomes': 'Favorites functionality'},
        ]
        for step_data in steps_12h:
            ProjectStep.objects.create(project=project, timeframe='12h', **step_data)
        
        steps_6h = steps_12h[:5]
        for step_data in steps_6h:
            ProjectStep.objects.create(project=project, timeframe='6h', **step_data)
        
        steps_24h = steps_12h + [
            {'step_number': 9, 'title': 'Add Meal Planning', 'description': 'Implement meal planning feature. Plan meals for the week.', 'technologies': ['JavaScript', 'Planning'], 'estimated_time': 90, 'learning_outcomes': 'Planning features'},
            {'step_number': 10, 'title': 'Add Shopping List Generator', 'description': 'Generate shopping list from selected recipes. Export to text file.', 'technologies': ['JavaScript', 'Export'], 'estimated_time': 75, 'learning_outcomes': 'List generation'},
        ]
        for step_data in steps_24h:
            ProjectStep.objects.create(project=project, timeframe='24h', **step_data)
    
    def _add_note_taking_steps(self, project):
        """Add steps for React Note-Taking App"""
        steps_12h = [
            {'step_number': 1, 'title': 'Setup React Project', 'description': 'Create React app, set up project structure. Install necessary dependencies.', 'technologies': ['React', 'Setup'], 'estimated_time': 30, 'learning_outcomes': 'React project initialization'},
            {'step_number': 2, 'title': 'Create Note Component', 'description': 'Build Note component. Understand component structure and props.', 'technologies': ['React', 'Components', 'Props'], 'estimated_time': 60, 'learning_outcomes': 'Component creation'},
            {'step_number': 3, 'title': 'Implement useState for Notes', 'description': 'Use useState to manage notes array. Add functionality to create new notes.', 'technologies': ['React Hooks', 'useState'], 'estimated_time': 75, 'learning_outcomes': 'State management with hooks'},
            {'step_number': 4, 'title': 'Add Edit Functionality', 'description': 'Implement note editing. Allow inline editing and save changes.', 'technologies': ['React', 'State Updates'], 'estimated_time': 90, 'learning_outcomes': 'Update operations'},
            {'step_number': 5, 'title': 'Add Delete Functionality', 'description': 'Implement note deletion with confirmation. Update state immutably.', 'technologies': ['React', 'Delete Operations'], 'estimated_time': 45, 'learning_outcomes': 'Delete operations'},
            {'step_number': 6, 'title': 'Add Categories/Tags', 'description': 'Implement category system. Allow users to organize notes by category.', 'technologies': ['React', 'Data Organization'], 'estimated_time': 75, 'learning_outcomes': 'Categorization'},
            {'step_number': 7, 'title': 'Add Search Functionality', 'description': 'Implement search to find notes by title or content. Real-time filtering.', 'technologies': ['React', 'Search', 'Filtering'], 'estimated_time': 60, 'learning_outcomes': 'Search implementation'},
            {'step_number': 8, 'title': 'Add Local Storage Integration', 'description': 'Use useEffect to save notes to local storage. Load on component mount.', 'technologies': ['useEffect', 'Local Storage'], 'estimated_time': 60, 'learning_outcomes': 'Data persistence'},
        ]
        for step_data in steps_12h:
            ProjectStep.objects.create(project=project, timeframe='12h', **step_data)
        
        steps_6h = steps_12h[:5]
        for step_data in steps_6h:
            ProjectStep.objects.create(project=project, timeframe='6h', **step_data)
        
        steps_24h = steps_12h + [
            {'step_number': 9, 'title': 'Add Rich Text Editing', 'description': 'Integrate rich text editor. Allow formatting and markdown support.', 'technologies': ['Rich Text', 'Libraries'], 'estimated_time': 120, 'learning_outcomes': 'Rich text editing'},
            {'step_number': 10, 'title': 'Add Export/Import', 'description': 'Export notes to JSON/Markdown. Import notes from file.', 'technologies': ['Export', 'Import', 'File Handling'], 'estimated_time': 90, 'learning_outcomes': 'Data export/import'},
        ]
        for step_data in steps_24h:
            ProjectStep.objects.create(project=project, timeframe='24h', **step_data)
    
    def _add_url_shortener_steps(self, project):
        """Add steps for URL Shortener API"""
        steps_6h = [
            {'step_number': 1, 'title': 'Setup Flask Project', 'description': 'Create Flask app, set up project structure. Install Flask and necessary packages.', 'technologies': ['Flask', 'Python'], 'estimated_time': 30, 'learning_outcomes': 'Flask setup'},
            {'step_number': 2, 'title': 'Design URL Data Model', 'description': 'Create data structure to store original URL and short code. Use in-memory storage or simple file.', 'technologies': ['Python', 'Data Modeling'], 'estimated_time': 45, 'learning_outcomes': 'Data modeling'},
            {'step_number': 3, 'title': 'Generate Short Codes', 'description': 'Implement function to generate unique short codes. Use random string or hash-based approach.', 'technologies': ['Python', 'String Generation'], 'estimated_time': 60, 'learning_outcomes': 'Code generation algorithms'},
            {'step_number': 4, 'title': 'Create Shorten Endpoint', 'description': 'Create POST endpoint to accept long URL, generate short code, and return shortened URL.', 'technologies': ['Flask', 'REST API', 'POST'], 'estimated_time': 75, 'learning_outcomes': 'POST endpoint creation'},
            {'step_number': 5, 'title': 'Create Redirect Endpoint', 'description': 'Create GET endpoint that takes short code and redirects to original URL.', 'technologies': ['Flask', 'Redirect', 'GET'], 'estimated_time': 60, 'learning_outcomes': 'Redirect implementation'},
            {'step_number': 6, 'title': 'Add URL Validation', 'description': 'Validate URL format. Handle invalid URLs with appropriate error messages.', 'technologies': ['Python', 'Validation', 'Error Handling'], 'estimated_time': 45, 'learning_outcomes': 'Input validation'},
        ]
        for step_data in steps_6h:
            ProjectStep.objects.create(project=project, timeframe='6h', **step_data)
        
        steps_12h = steps_6h + [
            {'step_number': 7, 'title': 'Add Database Integration', 'description': 'Replace in-memory storage with SQLite database. Store URLs persistently.', 'technologies': ['Database', 'SQLite', 'Flask'], 'estimated_time': 90, 'learning_outcomes': 'Database integration'},
            {'step_number': 8, 'title': 'Add Click Tracking', 'description': 'Track number of clicks for each shortened URL. Create analytics endpoint.', 'technologies': ['Analytics', 'Database'], 'estimated_time': 75, 'learning_outcomes': 'Analytics tracking'},
            {'step_number': 9, 'title': 'Add Expiration Dates', 'description': 'Allow URLs to have expiration dates. Handle expired URLs appropriately.', 'technologies': ['Date Handling', 'Validation'], 'estimated_time': 60, 'learning_outcomes': 'Expiration logic'},
        ]
        for step_data in steps_12h:
            ProjectStep.objects.create(project=project, timeframe='12h', **step_data)
        
        steps_24h = steps_12h + [
            {'step_number': 10, 'title': 'Add Custom Short Codes', 'description': 'Allow users to create custom short codes. Validate uniqueness.', 'technologies': ['Validation', 'Customization'], 'estimated_time': 60, 'learning_outcomes': 'Custom code generation'},
            {'step_number': 11, 'title': 'Add Frontend Interface', 'description': 'Create simple HTML/CSS/JS frontend to interact with API.', 'technologies': ['Frontend', 'API Integration'], 'estimated_time': 120, 'learning_outcomes': 'Frontend-backend integration'},
        ]
        for step_data in steps_24h:
            ProjectStep.objects.create(project=project, timeframe='24h', **step_data)
    
    def _add_chat_api_steps(self, project):
        """Add steps for Real-time Chat API"""
        steps_24h = [
            {'step_number': 1, 'title': 'Setup Node.js Project', 'description': 'Initialize Node.js project, install Express and Socket.io. Set up server structure.', 'technologies': ['Node.js', 'Express', 'Socket.io'], 'estimated_time': 45, 'learning_outcomes': 'Node.js and WebSocket setup'},
            {'step_number': 2, 'title': 'Configure Socket.io Server', 'description': 'Set up Socket.io on Express server. Handle connection events.', 'technologies': ['Socket.io', 'WebSockets'], 'estimated_time': 60, 'learning_outcomes': 'WebSocket server configuration'},
            {'step_number': 3, 'title': 'Implement Message Broadcasting', 'description': 'Broadcast messages to all connected clients. Handle message events.', 'technologies': ['Socket.io', 'Event Handling'], 'estimated_time': 90, 'learning_outcomes': 'Real-time messaging'},
            {'step_number': 4, 'title': 'Add Room Support', 'description': 'Implement chat rooms. Allow users to join/leave rooms.', 'technologies': ['Socket.io', 'Rooms'], 'estimated_time': 90, 'learning_outcomes': 'Room management'},
            {'step_number': 5, 'title': 'Add User Authentication', 'description': 'Implement user authentication. Identify users in messages.', 'technologies': ['Authentication', 'JWT'], 'estimated_time': 120, 'learning_outcomes': 'User authentication'},
            {'step_number': 6, 'title': 'Store Messages in Database', 'description': 'Save messages to MongoDB or PostgreSQL. Implement message persistence.', 'technologies': ['Database', 'Message Storage'], 'estimated_time': 120, 'learning_outcomes': 'Message persistence'},
            {'step_number': 7, 'title': 'Add Typing Indicators', 'description': 'Implement typing indicators. Show when users are typing.', 'technologies': ['Socket.io', 'Real-time Events'], 'estimated_time': 60, 'learning_outcomes': 'Real-time indicators'},
            {'step_number': 8, 'title': 'Add User Presence', 'description': 'Track online/offline status. Show active users in rooms.', 'technologies': ['Presence', 'Socket.io'], 'estimated_time': 75, 'learning_outcomes': 'User presence tracking'},
        ]
        for step_data in steps_24h:
            ProjectStep.objects.create(project=project, timeframe='24h', **step_data)
        
        steps_12h = steps_24h[:5]
        for step_data in steps_12h:
            ProjectStep.objects.create(project=project, timeframe='12h', **step_data)
        
        steps_48h = steps_24h + [
            {'step_number': 9, 'title': 'Add File Uploads', 'description': 'Implement file/image uploads in chat. Handle file sharing.', 'technologies': ['File Upload', 'Multer'], 'estimated_time': 120, 'learning_outcomes': 'File handling'},
            {'step_number': 10, 'title': 'Add Message Reactions', 'description': 'Implement emoji reactions to messages. Real-time reaction updates.', 'technologies': ['Real-time', 'Features'], 'estimated_time': 90, 'learning_outcomes': 'Advanced features'},
        ]
        for step_data in steps_48h:
            ProjectStep.objects.create(project=project, timeframe='48h', **step_data)
    
    def _add_web_scraper_steps(self, project):
        """Add steps for Web Scraper"""
        steps_12h = [
            {'step_number': 1, 'title': 'Setup Python Environment', 'description': 'Install BeautifulSoup, requests, and pandas. Set up project structure.', 'technologies': ['Python', 'BeautifulSoup', 'requests'], 'estimated_time': 30, 'learning_outcomes': 'Environment setup'},
            {'step_number': 2, 'title': 'Make HTTP Requests', 'description': 'Use requests library to fetch web pages. Handle different response codes.', 'technologies': ['requests', 'HTTP'], 'estimated_time': 60, 'learning_outcomes': 'HTTP requests'},
            {'step_number': 3, 'title': 'Parse HTML Content', 'description': 'Use BeautifulSoup to parse HTML. Understand DOM structure.', 'technologies': ['BeautifulSoup', 'HTML Parsing'], 'estimated_time': 90, 'learning_outcomes': 'HTML parsing'},
            {'step_number': 4, 'title': 'Extract Data', 'description': 'Extract specific data (text, links, images) using CSS selectors or XPath.', 'technologies': ['BeautifulSoup', 'Selectors'], 'estimated_time': 90, 'learning_outcomes': 'Data extraction'},
            {'step_number': 5, 'title': 'Handle Pagination', 'description': 'Navigate through multiple pages. Extract data from all pages.', 'technologies': ['Python', 'Pagination'], 'estimated_time': 75, 'learning_outcomes': 'Pagination handling'},
            {'step_number': 6, 'title': 'Save Data to CSV/JSON', 'description': 'Save extracted data to CSV or JSON files. Organize data properly.', 'technologies': ['pandas', 'CSV', 'JSON'], 'estimated_time': 60, 'learning_outcomes': 'Data export'},
            {'step_number': 7, 'title': 'Add Error Handling', 'description': 'Handle network errors, missing elements, and rate limiting. Add retries.', 'technologies': ['Error Handling', 'Retries'], 'estimated_time': 75, 'learning_outcomes': 'Robust error handling'},
            {'step_number': 8, 'title': 'Respect robots.txt', 'description': 'Check and respect robots.txt file. Understand web scraping ethics.', 'technologies': ['robots.txt', 'Ethics'], 'estimated_time': 45, 'learning_outcomes': 'Ethical scraping'},
        ]
        for step_data in steps_12h:
            ProjectStep.objects.create(project=project, timeframe='12h', **step_data)
        
        steps_6h = steps_12h[:5]
        for step_data in steps_6h:
            ProjectStep.objects.create(project=project, timeframe='6h', **step_data)
        
        steps_24h = steps_12h + [
            {'step_number': 9, 'title': 'Handle JavaScript-Rendered Content', 'description': 'Use Selenium to scrape dynamic content. Handle SPAs.', 'technologies': ['Selenium', 'Dynamic Content'], 'estimated_time': 120, 'learning_outcomes': 'Dynamic content scraping'},
            {'step_number': 10, 'title': 'Add Rate Limiting', 'description': 'Implement delays between requests. Be respectful to servers.', 'technologies': ['Rate Limiting', 'Delays'], 'estimated_time': 45, 'learning_outcomes': 'Rate limiting'},
        ]
        for step_data in steps_24h:
            ProjectStep.objects.create(project=project, timeframe='24h', **step_data)
    
    def _add_blog_platform_steps(self, project):
        """Add steps for Full-Stack Blog Platform"""
        steps_24h = [
            {'step_number': 1, 'title': 'Setup Backend (Node.js/Express)', 'description': 'Create Express server, set up project structure. Install necessary packages.', 'technologies': ['Node.js', 'Express'], 'estimated_time': 45, 'learning_outcomes': 'Backend setup'},
            {'step_number': 2, 'title': 'Create Database Models', 'description': 'Design database schema: users, posts, comments. Set up MongoDB or PostgreSQL.', 'technologies': ['Database', 'Models'], 'estimated_time': 90, 'learning_outcomes': 'Database design'},
            {'step_number': 3, 'title': 'Implement User Authentication', 'description': 'Add JWT authentication. Create login and registration endpoints.', 'technologies': ['Authentication', 'JWT'], 'estimated_time': 120, 'learning_outcomes': 'User authentication'},
            {'step_number': 4, 'title': 'Create Post CRUD API', 'description': 'Build API endpoints for creating, reading, updating, and deleting blog posts.', 'technologies': ['REST API', 'CRUD'], 'estimated_time': 120, 'learning_outcomes': 'CRUD operations'},
            {'step_number': 5, 'title': 'Add Comment System', 'description': 'Implement comment endpoints. Allow nested comments and replies.', 'technologies': ['Comments', 'Nested Data'], 'estimated_time': 90, 'learning_outcomes': 'Comment system'},
            {'step_number': 6, 'title': 'Setup React Frontend', 'description': 'Create React app. Set up routing and project structure.', 'technologies': ['React', 'React Router'], 'estimated_time': 60, 'learning_outcomes': 'Frontend setup'},
            {'step_number': 7, 'title': 'Build Post List Component', 'description': 'Create component to display list of blog posts. Fetch from API.', 'technologies': ['React', 'API Integration'], 'estimated_time': 90, 'learning_outcomes': 'Data fetching'},
            {'step_number': 8, 'title': 'Build Post Editor', 'description': 'Create rich text editor for writing posts. Integrate editor library.', 'technologies': ['Rich Text Editor', 'React'], 'estimated_time': 120, 'learning_outcomes': 'Rich text editing'},
            {'step_number': 9, 'title': 'Build Post Detail Page', 'description': 'Create detailed post view with comments. Handle comments display and creation.', 'technologies': ['React', 'Detail Views'], 'estimated_time': 90, 'learning_outcomes': 'Detail page design'},
            {'step_number': 10, 'title': 'Add Image Upload', 'description': 'Implement image upload for posts. Handle file uploads on backend.', 'technologies': ['File Upload', 'Multer'], 'estimated_time': 120, 'learning_outcomes': 'File handling'},
            {'step_number': 11, 'title': 'Connect Frontend to Backend', 'description': 'Integrate React frontend with API. Handle authentication and protected routes.', 'technologies': ['Integration', 'Protected Routes'], 'estimated_time': 90, 'learning_outcomes': 'Full-stack integration'},
            {'step_number': 12, 'title': 'Deploy Full-Stack App', 'description': 'Deploy backend and frontend. Set up environment variables and database.', 'technologies': ['Deployment', 'Full-Stack'], 'estimated_time': 120, 'learning_outcomes': 'Production deployment'},
        ]
        for step_data in steps_24h:
            ProjectStep.objects.create(project=project, timeframe='24h', **step_data)
        
        steps_12h = steps_24h[:8]
        for step_data in steps_12h:
            ProjectStep.objects.create(project=project, timeframe='12h', **step_data)
        
        steps_48h = steps_24h + [
            {'step_number': 13, 'title': 'Add Search and Filtering', 'description': 'Implement search functionality and category filtering.', 'technologies': ['Search', 'Filtering'], 'estimated_time': 90, 'learning_outcomes': 'Search implementation'},
            {'step_number': 14, 'title': 'Add Admin Dashboard', 'description': 'Create admin panel for managing posts, users, and comments.', 'technologies': ['Admin Panel', 'Dashboard'], 'estimated_time': 120, 'learning_outcomes': 'Admin features'},
        ]
        for step_data in steps_48h:
            ProjectStep.objects.create(project=project, timeframe='48h', **step_data)
    
    def _add_ecommerce_api_steps(self, project):
        """Add steps for E-commerce REST API"""
        steps_24h = [
            {'step_number': 1, 'title': 'Setup Django Project', 'description': 'Create Django project, install Django REST Framework. Set up project structure.', 'technologies': ['Django', 'Django REST Framework'], 'estimated_time': 45, 'learning_outcomes': 'Django setup'},
            {'step_number': 2, 'title': 'Design Database Models', 'description': 'Create models: Product, Category, Cart, Order, OrderItem. Understand relationships.', 'technologies': ['Django ORM', 'Models'], 'estimated_time': 120, 'learning_outcomes': 'Complex database design'},
            {'step_number': 3, 'title': 'Create Product API', 'description': 'Build API endpoints for products: list, detail, create, update, delete.', 'technologies': ['DRF', 'ViewSets'], 'estimated_time': 90, 'learning_outcomes': 'Product API'},
            {'step_number': 4, 'title': 'Implement Category System', 'description': 'Create category API. Allow nested categories and filtering by category.', 'technologies': ['Categories', 'Filtering'], 'estimated_time': 75, 'learning_outcomes': 'Category management'},
            {'step_number': 5, 'title': 'Create Shopping Cart API', 'description': 'Implement shopping cart endpoints. Add/remove items, update quantities.', 'technologies': ['Cart', 'Session Management'], 'estimated_time': 120, 'learning_outcomes': 'Cart implementation'},
            {'step_number': 6, 'title': 'Implement Order Processing', 'description': 'Create order API. Convert cart to order, handle order status.', 'technologies': ['Orders', 'State Management'], 'estimated_time': 120, 'learning_outcomes': 'Order processing'},
            {'step_number': 7, 'title': 'Add User Authentication', 'description': 'Implement user registration and authentication. JWT tokens.', 'technologies': ['Authentication', 'JWT'], 'estimated_time': 90, 'learning_outcomes': 'User authentication'},
            {'step_number': 8, 'title': 'Add Payment Integration', 'description': 'Integrate payment gateway (Stripe). Handle payment processing.', 'technologies': ['Payment', 'Stripe'], 'estimated_time': 120, 'learning_outcomes': 'Payment integration'},
            {'step_number': 9, 'title': 'Add Product Images', 'description': 'Implement image upload for products. Handle multiple images per product.', 'technologies': ['File Upload', 'Images'], 'estimated_time': 90, 'learning_outcomes': 'Image handling'},
            {'step_number': 10, 'title': 'Add Inventory Management', 'description': 'Track product stock. Handle out-of-stock scenarios.', 'technologies': ['Inventory', 'Stock Management'], 'estimated_time': 75, 'learning_outcomes': 'Inventory tracking'},
            {'step_number': 11, 'title': 'Add Search and Filtering', 'description': 'Implement product search and advanced filtering (price, category, rating).', 'technologies': ['Search', 'Filtering', 'DRF'], 'estimated_time': 90, 'learning_outcomes': 'Advanced search'},
            {'step_number': 12, 'title': 'Add API Documentation', 'description': 'Document API with Swagger/OpenAPI. Create comprehensive API docs.', 'technologies': ['Documentation', 'Swagger'], 'estimated_time': 60, 'learning_outcomes': 'API documentation'},
        ]
        for step_data in steps_24h:
            ProjectStep.objects.create(project=project, timeframe='24h', **step_data)
        
        steps_12h = steps_24h[:7]
        for step_data in steps_12h:
            ProjectStep.objects.create(project=project, timeframe='12h', **step_data)
        
        steps_48h = steps_24h + [
            {'step_number': 13, 'title': 'Add Recommendation System', 'description': 'Implement product recommendations based on user behavior.', 'technologies': ['Recommendations', 'Algorithms'], 'estimated_time': 120, 'learning_outcomes': 'Recommendation algorithms'},
            {'step_number': 14, 'title': 'Add Admin Dashboard API', 'description': 'Create admin endpoints for managing products, orders, and users.', 'technologies': ['Admin', 'Management'], 'estimated_time': 90, 'learning_outcomes': 'Admin features'},
        ]
        for step_data in steps_48h:
            ProjectStep.objects.create(project=project, timeframe='48h', **step_data)