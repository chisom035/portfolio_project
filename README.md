# Portfolio Website

This is a dynamic, full-stack portfolio website built with Django for my CSE310 Applied Programming course. This portfolio showcases some of my projects, skills, and contact information with responsive design and interactive features. It demonstrates proficiency in Django, Python, HTML, CSS, and JavaScript.

## Instructions for Build and Use

Steps to build and/or run the software:

1. Clone or download the repository to your local machine
2. Open a terminal/command prompt and navigate to the project folder: `cd portfolio_project`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
5. Install Django: `pip install django`
6. Apply database migrations: `python manage.py migrate`
7. Start the development server: `python manage.py runserver`
8. Open your browser and visit: `http://127.0.0.1:8000`

Instructions for using the software:

1. Browse the homepage to view my introduction, skills, and featured projects
2. Navigate to the Projects page using the top menu or "View All Projects" button
3. Filter projects by technology using the filter buttons (Django, JavaScript, Web, etc.)
4. Use the contact form at the bottom of the homepage to send a message
5. View project details by clicking on project cards
6. Access social links in the footer to connect on GitHub and LinkedIn

## Development Environment

To recreate the development environment, you need the following software and/or libraries with the specified versions:

* Python 3.13 (3.8 or higher will work)
* Django 6.0+ (installed via `pip install django`)
* Modern web browser (Chrome, Firefox, Safari or Edge)
* Code editor (VS Code)
* Git for version control
* SQLite3 (comes with Python, used for database)
* Operating System: Windows 10/11, macOS, or Linux Ubuntu

## Useful Websites to Learn More

I found these websites useful in developing this software:

* [Django Documentation](https://docs.djangoproject.com/) - Official Django docs with tutorials and reference
* [MDN Web Docs - Django](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django) - Django tutorials for beginners
* [W3Schools - Django Tutorial](https://www.w3schools.com/django/) - Simple, practical Django examples
* [CSS-Tricks](https://css-tricks.com/) - Modern CSS techniques and responsive design
* [JavaScript.info](https://javascript.info/) - Comprehensive JavaScript guide for DOM manipulation
* [Real Python - Django](https://realpython.com/tutorials/django/) - In-depth Django articles and tutorials
* [Stack Overflow - Django Tag](https://stackoverflow.com/questions/tagged/django) - Community Q&A for problem-solving

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

* Add user authentication system for admin login and content management
* Implement blog functionality to share technical articles and project updates
* Add dark/light mode toggle for better user preference customization
* Integrate email notifications for contact form submissions
* Create project detail pages with more information, screenshots, and code snippets
* Add visitor analytics to track page views and user engagement
* Add more interactive elements like animated skill bars or project demos
* Create downloadable resume/CV section with PDF generation
