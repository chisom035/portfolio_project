from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    """Render the home page with portfolio content."""
    
    
    skill_categories = [
        {
            'name': 'Frontend',
            'skills': ['HTML/CSS', 'JavaScript', 'React', 'Vue.js', 'Bootstrap']
        },
        {
            'name': 'Backend', 
            'skills': ['Node.js', 'Python/Django', 'MySQL', 'MongoDB', 'PostgreSQL', 'Express.js']
        },
        {
            'name': 'Tools & DevOps',
            'skills': ['Git', 'Docker', 'AWS', 'GitHub', 'VS Code', 'Postman', 'Jira']
        }
    ]
    
    course_info = {
        'name': 'CSE310 - Web Application Development',
        'description': 'This portfolio is developed as part of CSE310 course requirements, showcasing full-stack development with Django.',
        'technologies': ['Django', 'Python', 'HTML5', 'CSS3', 'JavaScript', 'SQLite'],
        'features': [
            'Dynamic content rendering',
            'Database integration',
            'User input validation',
            'Responsive design',
            'Static file management',
            'Form handling with CSRF'
        ]
    }
    
    context = {
        'skill_categories': skill_categories,
        'course_info': course_info,
        'project_count': 6,
        'experience_years': 3,
        'skill_count': 18,
        'page_title': 'Chisom Wonodi - Portfolio',
    }
    
    return render(request, 'portfolio/index.html', context)

def projects(request):
    """Render the projects page."""
    return render(request, 'portfolio/projects.html')

def contact(request):
    """Handle contact form submissions."""
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()
        
        
        errors = []
        
        if not name:
            errors.append('Name is required')
        elif len(name) < 2:
            errors.append('Name must be at least 2 characters')
            
        if not email:
            errors.append('Email is required')
        elif '@' not in email or '.' not in email:
            errors.append('Please enter a valid email address')
            
        if not message:
            errors.append('Message is required')
        elif len(message) < 10:
            errors.append('Message must be at least 10 characters')
        
        if errors:
            for error in errors:
                messages.error(request, error)
        else:
         
            messages.success(request, 'Thank you for your message! I will get back to you soon.')
            
            
            print(f"=== CSE310 PORTFOLIO CONTACT FORM ===")
            print(f"Name: {name}")
            print(f"Email: {email}")
            print(f"Message: {message}")
            print(f"Timestamp: {request.POST.get('timestamp', 'N/A')}")
            print("=" * 40)
            
        
        return redirect('home')
    
    return redirect('home')