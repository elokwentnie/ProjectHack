"""
Project Generator - Creates custom projects based on user preferences
"""
import random
from .models import Project, ProjectStep


class ProjectGenerator:
    """Generates custom projects with steps based on user preferences"""
    
    # Project idea templates by track and difficulty
    PROJECT_TEMPLATES = {
        'frontend': {
            'beginner': [
                {
                    'title_template': '{keyword} Landing Page',
                    'description_template': 'Build a beautiful landing page for {keyword}. Learn HTML structure, CSS styling, and responsive design while creating a professional-looking website.',
                    'technologies': ['HTML', 'CSS', 'Responsive Design'],
                },
                {
                    'title_template': '{keyword} Showcase Website',
                    'description_template': 'Create a showcase website for {keyword}. Practice modern web design, animations, and user experience principles.',
                    'technologies': ['HTML', 'CSS', 'JavaScript', 'Animations'],
                },
                {
                    'title_template': 'Interactive {keyword} App',
                    'description_template': 'Build an interactive web application focused on {keyword}. Learn JavaScript fundamentals and DOM manipulation.',
                    'technologies': ['HTML', 'CSS', 'JavaScript', 'DOM'],
                },
            ],
            'intermediate': [
                {
                    'title_template': '{keyword} Dashboard',
                    'description_template': 'Create a dynamic dashboard for {keyword}. Learn advanced JavaScript, API integration, and data visualization.',
                    'technologies': ['JavaScript', 'APIs', 'Charts', 'Data Visualization'],
                },
                {
                    'title_template': '{keyword} Management System',
                    'description_template': 'Build a management system for {keyword}. Practice state management, local storage, and complex UI interactions.',
                    'technologies': ['JavaScript', 'Local Storage', 'State Management'],
                },
            ],
            'advanced': [
                {
                    'title_template': 'Real-time {keyword} Platform',
                    'description_template': 'Develop a real-time platform for {keyword}. Integrate WebSockets, handle complex state, and create a scalable architecture.',
                    'technologies': ['WebSockets', 'Advanced JavaScript', 'Real-time Updates'],
                },
            ],
        },
        'backend': {
            'beginner': [
                {
                    'title_template': '{keyword} API',
                    'description_template': 'Build a RESTful API for {keyword}. Learn backend fundamentals, HTTP methods, and API design.',
                    'technologies': ['Python', 'Flask', 'REST API'],
                },
            ],
            'intermediate': [
                {
                    'title_template': '{keyword} Management API',
                    'description_template': 'Create a comprehensive API for managing {keyword}. Implement CRUD operations, authentication, and data validation.',
                    'technologies': ['Python', 'Flask/Django', 'REST API', 'Authentication'],
                },
            ],
            'advanced': [
                {
                    'title_template': 'Scalable {keyword} Backend',
                    'description_template': 'Build a production-ready backend for {keyword}. Implement caching, database optimization, and microservices architecture.',
                    'technologies': ['Django', 'PostgreSQL', 'Redis', 'Caching'],
                },
            ],
        },
        'react': {
            'beginner': [
                {
                    'title_template': '{keyword} React App',
                    'description_template': 'Build a React application for {keyword}. Learn component-based architecture, JSX, and React hooks.',
                    'technologies': ['React', 'JSX', 'Hooks', 'Components'],
                },
            ],
            'intermediate': [
                {
                    'title_template': '{keyword} React Dashboard',
                    'description_template': 'Create a React dashboard for {keyword}. Practice state management, API integration, and component composition.',
                    'technologies': ['React', 'State Management', 'APIs', 'Context API'],
                },
            ],
            'advanced': [
                {
                    'title_template': 'Advanced {keyword} React App',
                    'description_template': 'Develop a complex React application for {keyword}. Implement advanced patterns, performance optimization, and testing.',
                    'technologies': ['React', 'Redux', 'Testing', 'Performance'],
                },
            ],
        },
        'python': {
            'beginner': [
                {
                    'title_template': '{keyword} Data Analysis',
                    'description_template': 'Analyze {keyword} data using Python. Learn pandas, data manipulation, and basic visualization.',
                    'technologies': ['Python', 'pandas', 'matplotlib', 'Data Analysis'],
                },
            ],
            'intermediate': [
                {
                    'title_template': '{keyword} Automation Script',
                    'description_template': 'Create an automation script for {keyword}. Learn file operations, APIs, and workflow automation.',
                    'technologies': ['Python', 'Automation', 'APIs', 'File Operations'],
                },
            ],
            'advanced': [
                {
                    'title_template': 'Advanced {keyword} System',
                    'description_template': 'Build an advanced system for {keyword}. Implement machine learning, data pipelines, and complex algorithms.',
                    'technologies': ['Python', 'Machine Learning', 'Data Pipelines'],
                },
            ],
        },
        'nodejs': {
            'beginner': [
                {
                    'title_template': '{keyword} Node.js API',
                    'description_template': 'Build a Node.js API for {keyword}. Learn Express, routing, and server-side JavaScript.',
                    'technologies': ['Node.js', 'Express', 'REST API'],
                },
            ],
            'intermediate': [
                {
                    'title_template': '{keyword} Node.js Service',
                    'description_template': 'Create a Node.js service for {keyword}. Implement middleware, authentication, and database integration.',
                    'technologies': ['Node.js', 'Express', 'MongoDB', 'Authentication'],
                },
            ],
            'advanced': [
                {
                    'title_template': 'Scalable {keyword} Node.js App',
                    'description_template': 'Develop a scalable Node.js application for {keyword}. Implement microservices, real-time features, and optimization.',
                    'technologies': ['Node.js', 'Microservices', 'WebSockets', 'Performance'],
                },
            ],
        },
        'fullstack': {
            'beginner': [
                {
                    'title_template': '{keyword} Full-Stack App',
                    'description_template': 'Build a complete full-stack application for {keyword}. Connect frontend and backend, handle data flow, and deploy.',
                    'technologies': ['React', 'Node.js', 'Full-Stack', 'Deployment'],
                },
            ],
            'intermediate': [
                {
                    'title_template': '{keyword} Full-Stack Platform',
                    'description_template': 'Create a full-stack platform for {keyword}. Implement authentication, real-time features, and complex state management.',
                    'technologies': ['React', 'Node.js', 'Authentication', 'Real-time'],
                },
            ],
            'advanced': [
                {
                    'title_template': 'Enterprise {keyword} Platform',
                    'description_template': 'Develop an enterprise-grade platform for {keyword}. Implement advanced architecture, scalability, and security.',
                    'technologies': ['React', 'Node.js', 'Microservices', 'Security'],
                },
            ],
        },
    }
    
    # Keywords for project generation
    KEYWORDS = [
        'E-commerce', 'Social Media', 'Fitness', 'Education', 'Finance', 'Travel',
        'Food', 'Music', 'Gaming', 'Health', 'Productivity', 'Entertainment',
        'Shopping', 'News', 'Weather', 'Sports', 'Photography', 'Art', 'Books',
        'Movies', 'Events', 'Real Estate', 'Job Board', 'Blog', 'Portfolio'
    ]
    
    def generate_project(self, track, difficulty, timeframe, keywords=None, interests=None):
        """
        Generate a custom project based on user preferences
        
        Args:
            track: Project track (frontend, backend, etc.)
            difficulty: Project difficulty (beginner, intermediate, advanced)
            timeframe: Selected timeframe (6h, 12h, 24h, 48h)
            keywords: Optional list of keywords
            interests: Optional list of interests
            
        Returns:
            Project instance with generated steps
        """
        # Select keyword
        if keywords and len(keywords) > 0:
            keyword = random.choice(keywords)
        elif interests and len(interests) > 0:
            keyword = random.choice(interests)
        else:
            keyword = random.choice(self.KEYWORDS)
        
        # Get template
        templates = self.PROJECT_TEMPLATES.get(track, {}).get(difficulty, [])
        if not templates:
            # Fallback to any difficulty
            for diff in ['beginner', 'intermediate', 'advanced']:
                templates = self.PROJECT_TEMPLATES.get(track, {}).get(diff, [])
                if templates:
                    break
        
        if not templates:
            # Ultimate fallback
            template = {
                'title_template': '{keyword} Project',
                'description_template': 'Build a project focused on {keyword}. Learn and practice {track} development.',
                'technologies': ['General Development'],
            }
        else:
            template = random.choice(templates)
        
        # Generate title and description
        title = template['title_template'].format(keyword=keyword)
        description = template['description_template'].format(keyword=keyword, track=track)
        
        # Create project
        project = Project.objects.create(
            title=title,
            description=description,
            difficulty=difficulty,
            track=track,
            is_generated=True,
            user_preferences={
                'keywords': keywords or [],
                'interests': interests or [],
                'timeframe': timeframe,
            }
        )
        
        # Generate steps based on timeframe
        self._generate_steps(project, track, difficulty, timeframe, template.get('technologies', []))
        
        return project
    
    def _generate_steps(self, project, track, difficulty, timeframe, base_technologies):
        """Generate project steps based on timeframe"""
        timeframe_hours = int(timeframe.replace('h', ''))
        
        # Base steps for all timeframes
        base_steps = self._get_base_steps(track, difficulty)
        
        # Calculate number of steps based on timeframe
        if timeframe_hours == 6:
            steps = base_steps[:6]
        elif timeframe_hours == 12:
            steps = base_steps[:8]
        elif timeframe_hours == 24:
            steps = base_steps[:12]
        else:  # 48h
            steps = base_steps[:16]
        
        # Create ProjectStep instances
        for idx, step_data in enumerate(steps, 1):
            # Merge base technologies with step-specific ones
            technologies = base_technologies + step_data.get('technologies', [])
            
            ProjectStep.objects.create(
                project=project,
                step_number=idx,
                timeframe=timeframe,
                title=step_data['title'],
                description=step_data['description'],
                technologies=list(set(technologies)),  # Remove duplicates
                estimated_time=step_data.get('estimated_time', timeframe_hours * 60 // len(steps)),
                learning_outcomes=step_data.get('learning_outcomes', '')
            )
    
    def _get_base_steps(self, track, difficulty):
        """Get base step templates for a track and difficulty"""
        # Generic step templates that work for most projects
        base_steps = [
            {
                'title': 'Project Setup and Planning',
                'description': 'Set up your development environment, create project structure, and plan your approach.',
                'technologies': ['Project Setup'],
                'estimated_time': 30,
                'learning_outcomes': 'Project structure and planning',
            },
            {
                'title': 'Core Functionality Implementation',
                'description': 'Implement the core features and functionality of your project.',
                'technologies': ['Core Development'],
                'estimated_time': 120,
                'learning_outcomes': 'Core feature development',
            },
            {
                'title': 'User Interface Development',
                'description': 'Design and implement the user interface. Make it intuitive and user-friendly.',
                'technologies': ['UI/UX'],
                'estimated_time': 90,
                'learning_outcomes': 'User interface design',
            },
            {
                'title': 'Data Management',
                'description': 'Implement data storage, retrieval, and management functionality.',
                'technologies': ['Data Management'],
                'estimated_time': 90,
                'learning_outcomes': 'Data handling',
            },
            {
                'title': 'Testing and Debugging',
                'description': 'Test your application, fix bugs, and ensure everything works correctly.',
                'technologies': ['Testing', 'Debugging'],
                'estimated_time': 60,
                'learning_outcomes': 'Testing and quality assurance',
            },
            {
                'title': 'Polish and Deployment',
                'description': 'Add final touches, optimize performance, and deploy your project.',
                'technologies': ['Deployment', 'Optimization'],
                'estimated_time': 60,
                'learning_outcomes': 'Deployment and optimization',
            },
        ]
        
        # Add track-specific steps
        if track == 'frontend':
            base_steps.extend([
                {
                    'title': 'Responsive Design',
                    'description': 'Make your application work perfectly on all device sizes.',
                    'technologies': ['Responsive Design', 'Media Queries'],
                    'estimated_time': 60,
                },
                {
                    'title': 'JavaScript Interactivity',
                    'description': 'Add interactive features and dynamic behavior.',
                    'technologies': ['JavaScript', 'DOM Manipulation'],
                    'estimated_time': 90,
                },
            ])
        elif track == 'backend':
            base_steps.extend([
                {
                    'title': 'API Endpoints',
                    'description': 'Create RESTful API endpoints for your application.',
                    'technologies': ['REST API', 'Endpoints'],
                    'estimated_time': 90,
                },
                {
                    'title': 'Database Integration',
                    'description': 'Set up and integrate a database for data persistence.',
                    'technologies': ['Database', 'ORM'],
                    'estimated_time': 90,
                },
            ])
        elif track == 'react':
            base_steps.extend([
                {
                    'title': 'Component Architecture',
                    'description': 'Design and build reusable React components.',
                    'technologies': ['React', 'Components'],
                    'estimated_time': 90,
                },
                {
                    'title': 'State Management',
                    'description': 'Implement state management using hooks or context.',
                    'technologies': ['React Hooks', 'State Management'],
                    'estimated_time': 90,
                },
            ])
        
        # Add difficulty-specific steps
        if difficulty == 'intermediate':
            base_steps.extend([
                {
                    'title': 'Advanced Features',
                    'description': 'Implement advanced features and functionality.',
                    'technologies': ['Advanced Development'],
                    'estimated_time': 120,
                },
            ])
        elif difficulty == 'advanced':
            base_steps.extend([
                {
                    'title': 'Advanced Features',
                    'description': 'Implement advanced features and functionality.',
                    'technologies': ['Advanced Development'],
                    'estimated_time': 120,
                },
                {
                    'title': 'Performance Optimization',
                    'description': 'Optimize your application for performance and scalability.',
                    'technologies': ['Performance', 'Optimization'],
                    'estimated_time': 90,
                },
                {
                    'title': 'Security Implementation',
                    'description': 'Add security measures and best practices.',
                    'technologies': ['Security', 'Best Practices'],
                    'estimated_time': 90,
                },
            ])
        
        return base_steps

