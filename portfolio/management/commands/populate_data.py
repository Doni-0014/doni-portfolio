from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from portfolio.models import (
    PersonalInfo, Skill, Education, Certification, 
    Project, BlogPost
)


class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')
        
        # Create superuser if it doesn't exist
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            self.stdout.write('Created superuser: admin/admin123')
        
        # Create Personal Info
        personal_info, created = PersonalInfo.objects.get_or_create(
            name="Doni Alston G",
            defaults={
                'title': 'Python Full Stack Developer',
                'bio': 'Passionate about creating innovative web solutions with Python, Django, and modern frontend technologies. I love building scalable applications that make a difference.',
                'email': 'doni.alston@example.com',
                'phone': '+1 (555) 123-4567',
                'location': 'San Francisco, CA',
                'github_url': 'https://github.com/donialston',
                'linkedin_url': 'https://linkedin.com/in/donialston',
                'twitter_url': 'https://twitter.com/donialston',
            }
        )
        
        if created:
            self.stdout.write('Created personal info')
        
        # Create Skills
        skills_data = [
            # Frontend
            {'name': 'HTML5', 'proficiency': 95, 'category': 'frontend', 'icon': 'fab fa-html5'},
            {'name': 'CSS3', 'proficiency': 90, 'category': 'frontend', 'icon': 'fab fa-css3-alt'},
            {'name': 'JavaScript', 'proficiency': 85, 'category': 'frontend', 'icon': 'fab fa-js-square'},
            {'name': 'React', 'proficiency': 80, 'category': 'frontend', 'icon': 'fab fa-react'},
            {'name': 'Vue.js', 'proficiency': 75, 'category': 'frontend', 'icon': 'fab fa-vue'},
            {'name': 'Tailwind CSS', 'proficiency': 90, 'category': 'frontend', 'icon': 'fas fa-paint-brush'},
            
            # Backend
            {'name': 'Python', 'proficiency': 95, 'category': 'backend', 'icon': 'fab fa-python'},
            {'name': 'Django', 'proficiency': 90, 'category': 'backend', 'icon': 'fas fa-server'},
            {'name': 'Flask', 'proficiency': 85, 'category': 'backend', 'icon': 'fas fa-flask'},
            {'name': 'FastAPI', 'proficiency': 80, 'category': 'backend', 'icon': 'fas fa-rocket'},
            {'name': 'Node.js', 'proficiency': 75, 'category': 'backend', 'icon': 'fab fa-node-js'},
            {'name': 'Express.js', 'proficiency': 70, 'category': 'backend', 'icon': 'fas fa-code'},
            
            # Database
            {'name': 'PostgreSQL', 'proficiency': 85, 'category': 'database', 'icon': 'fas fa-database'},
            {'name': 'MySQL', 'proficiency': 80, 'category': 'database', 'icon': 'fas fa-database'},
            {'name': 'MongoDB', 'proficiency': 75, 'category': 'database', 'icon': 'fas fa-leaf'},
            {'name': 'Redis', 'proficiency': 70, 'category': 'database', 'icon': 'fas fa-memory'},
            
            # Tools
            {'name': 'Git', 'proficiency': 90, 'category': 'tools', 'icon': 'fab fa-git-alt'},
            {'name': 'Docker', 'proficiency': 80, 'category': 'tools', 'icon': 'fab fa-docker'},
            {'name': 'AWS', 'proficiency': 75, 'category': 'tools', 'icon': 'fab fa-aws'},
            {'name': 'Linux', 'proficiency': 85, 'category': 'tools', 'icon': 'fab fa-linux'},
        ]
        
        for skill_data in skills_data:
            skill, created = Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults=skill_data
            )
            if created:
                self.stdout.write(f'Created skill: {skill.name}')
        
        # Create Education
        education_data = [
            {
                'institution': 'University of California, Berkeley',
                'degree': 'Bachelor of Science in Computer Science',
                'field_of_study': 'Computer Science',
                'start_date': '2018-09-01',
                'end_date': '2022-05-15',
                'gpa': 3.8,
                'description': 'Focused on software engineering, algorithms, and data structures.',
            },
            {
                'institution': 'Stanford University',
                'degree': 'Master of Science in Software Engineering',
                'field_of_study': 'Software Engineering',
                'start_date': '2022-09-01',
                'end_date': '2024-05-15',
                'gpa': 3.9,
                'description': 'Advanced studies in software architecture, machine learning, and distributed systems.',
                'is_current': True,
            }
        ]
        
        for edu_data in education_data:
            education, created = Education.objects.get_or_create(
                institution=edu_data['institution'],
                degree=edu_data['degree'],
                defaults=edu_data
            )
            if created:
                self.stdout.write(f'Created education: {education.degree}')
        
        # Create Certifications
        certifications_data = [
            {
                'title': 'AWS Certified Solutions Architect',
                'issuer': 'Amazon Web Services',
                'issue_date': '2023-06-15',
                'expiry_date': '2026-06-15',
                'credential_id': 'AWS-SAA-123456',
                'description': 'Validates expertise in designing distributed systems on AWS.',
            },
            {
                'title': 'Django Professional Certification',
                'issuer': 'Django Software Foundation',
                'issue_date': '2023-03-20',
                'credential_id': 'Django-Pro-789012',
                'description': 'Certified Django developer with expertise in web development.',
            },
            {
                'title': 'Python Institute PCAP',
                'issuer': 'Python Institute',
                'issue_date': '2022-12-10',
                'credential_id': 'PCAP-345678',
                'description': 'Certified Associate in Python Programming.',
            }
        ]
        
        for cert_data in certifications_data:
            certification, created = Certification.objects.get_or_create(
                title=cert_data['title'],
                issuer=cert_data['issuer'],
                defaults=cert_data
            )
            if created:
                self.stdout.write(f'Created certification: {certification.title}')
        
        # Create Projects
        projects_data = [
            {
                'title': 'E-Commerce Platform',
                'description': 'A full-stack e-commerce platform built with Django and React.',
                'long_description': 'This project features a complete e-commerce solution with user authentication, product management, shopping cart, payment processing, and admin dashboard. Built with Django REST Framework for the backend and React for the frontend.',
                'github_url': 'https://github.com/donialston/ecommerce-platform',
                'live_url': 'https://ecommerce-demo.example.com',
                'featured': True,
            },
            {
                'title': 'Task Management API',
                'description': 'RESTful API for task management with real-time updates.',
                'long_description': 'A comprehensive task management API built with Django REST Framework and WebSockets. Features include user authentication, project management, task assignment, real-time notifications, and file uploads.',
                'github_url': 'https://github.com/donialston/task-management-api',
                'live_url': 'https://task-api.example.com',
                'featured': True,
            },
            {
                'title': 'Weather Dashboard',
                'description': 'Real-time weather dashboard with data visualization.',
                'long_description': 'A responsive weather dashboard that displays current weather conditions and forecasts. Built with Django, Chart.js, and external weather APIs. Features include location-based weather, historical data, and interactive charts.',
                'github_url': 'https://github.com/donialston/weather-dashboard',
                'live_url': 'https://weather-demo.example.com',
                'featured': True,
            },
            {
                'title': 'Blog CMS',
                'description': 'Content management system for blogging with Markdown support.',
                'long_description': 'A feature-rich blogging platform with Markdown support, comment system, user management, and SEO optimization. Built with Django and includes features like draft posts, categories, tags, and social sharing.',
                'github_url': 'https://github.com/donialston/blog-cms',
                'live_url': 'https://blog-cms.example.com',
            },
            {
                'title': 'Portfolio Website',
                'description': 'Personal portfolio website with admin panel.',
                'long_description': 'A responsive portfolio website showcasing projects, skills, and experience. Features include dark/light mode, contact form, blog integration, and admin panel for content management.',
                'github_url': 'https://github.com/donialston/portfolio',
                'live_url': 'https://doni-alston.dev',
            },
            {
                'title': 'Chat Application',
                'description': 'Real-time chat application with WebSockets.',
                'long_description': 'A real-time chat application built with Django Channels and WebSockets. Features include private messaging, group chats, file sharing, message history, and user presence indicators.',
                'github_url': 'https://github.com/donialston/chat-app',
                'live_url': 'https://chat-demo.example.com',
            }
        ]
        
        for project_data in projects_data:
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults=project_data
            )
            if created:
                # Add some skills to projects
                if 'Django' in project.title or 'API' in project.title:
                    django_skill = Skill.objects.get(name='Django')
                    project.tech_stack.add(django_skill)
                if 'React' in project.title or 'Dashboard' in project.title:
                    react_skill = Skill.objects.get(name='React')
                    project.tech_stack.add(react_skill)
                if 'Python' in project.title:
                    python_skill = Skill.objects.get(name='Python')
                    project.tech_stack.add(python_skill)
                
                self.stdout.write(f'Created project: {project.title}')
        
        # Create Blog Posts
        blog_posts_data = [
            {
                'title': 'Getting Started with Django REST Framework',
                'slug': 'getting-started-django-rest-framework',
                'content': '''# Getting Started with Django REST Framework

Django REST Framework (DRF) is a powerful and flexible toolkit for building Web APIs. In this article, we'll explore the basics of DRF and how to create your first API.

## What is Django REST Framework?

DRF is a third-party package that extends Django's built-in capabilities to make it easy to build RESTful APIs. It provides:

- Serializers for converting complex data types to native Python datatypes
- ViewSets and APIViews for handling HTTP requests
- Authentication and permissions
- Browsable API interface
- Pagination and filtering

## Installation

```bash
pip install djangorestframework
```

Add it to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    # ...
    'rest_framework',
]
```

## Creating Your First API

Let's create a simple API for a blog:

```python
# models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# serializers.py
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

# views.py
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

## Conclusion

Django REST Framework makes it easy to build powerful APIs. With its built-in features and extensive documentation, you can quickly create robust web services.

Happy coding!''',
                'excerpt': 'Learn how to build powerful APIs with Django REST Framework. This comprehensive guide covers installation, serializers, viewsets, and more.',
                'published': True,
                'featured': True,
                'tags': 'django, python, api, rest, web-development',
            },
            {
                'title': 'Building Responsive UIs with Tailwind CSS',
                'slug': 'building-responsive-uis-tailwind-css',
                'content': '''# Building Responsive UIs with Tailwind CSS

Tailwind CSS is a utility-first CSS framework that makes it easy to build modern, responsive user interfaces. In this article, we'll explore how to use Tailwind effectively.

## Why Tailwind CSS?

- **Utility-first approach**: Build complex designs without writing custom CSS
- **Responsive by default**: Mobile-first responsive design
- **Consistent design system**: Predefined spacing, colors, and typography
- **Small bundle size**: Only includes the CSS you actually use
- **Highly customizable**: Easy to extend and modify

## Getting Started

Install Tailwind CSS:

```bash
npm install -D tailwindcss
npx tailwindcss init
```

Configure your `tailwind.config.js`:

```javascript
module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

## Basic Usage

```html
<div class="max-w-md mx-auto bg-white rounded-xl shadow-md overflow-hidden md:max-w-2xl">
  <div class="md:flex">
    <div class="md:shrink-0">
      <img class="h-48 w-full object-cover md:h-full md:w-48" src="/img/building.jpg" alt="Modern building">
    </div>
    <div class="p-8">
      <div class="uppercase tracking-wide text-sm text-indigo-500 font-semibold">Company retreats</div>
      <a href="#" class="block mt-1 text-lg leading-tight font-medium text-black hover:underline">Incredible accommodation for your team</a>
      <p class="mt-2 text-slate-500">Looking to take your team away on a retreat to enjoy awesome food and take in some sunshine? I have a few places near me.</p>
    </div>
  </div>
</div>
```

## Responsive Design

Tailwind uses a mobile-first approach:

```html
<div class="w-full md:w-1/2 lg:w-1/3 xl:w-1/4">
  <!-- This div is full width on mobile, half on tablet, third on desktop, quarter on large screens -->
</div>
```

## Dark Mode

Enable dark mode in your config:

```javascript
module.exports = {
  darkMode: 'class', // or 'media'
  // ...
}
```

Use dark mode classes:

```html
<div class="bg-white dark:bg-gray-800 text-gray-900 dark:text-white">
  <!-- Content -->
</div>
```

## Conclusion

Tailwind CSS is a powerful tool for building modern, responsive UIs. Its utility-first approach and excellent documentation make it a great choice for any project.

Start building with Tailwind today!''',
                'excerpt': 'Learn how to build beautiful, responsive user interfaces with Tailwind CSS. This guide covers the basics and advanced techniques.',
                'published': True,
                'featured': True,
                'tags': 'tailwind, css, frontend, responsive, web-design',
            },
            {
                'title': 'Python Best Practices for Web Development',
                'slug': 'python-best-practices-web-development',
                'content': '''# Python Best Practices for Web Development

Writing clean, maintainable Python code is essential for successful web development projects. Here are some best practices to follow.

## Code Organization

### 1. Use Virtual Environments

Always use virtual environments to isolate your project dependencies:

```bash
python -m venv myproject_env
source myproject_env/bin/activate  # On Windows: myproject_env\\Scripts\\activate
pip install -r requirements.txt
```

### 2. Follow PEP 8

PEP 8 is the official Python style guide:

```python
# Good
def calculate_total_price(items):
    """Calculate the total price of items."""
    return sum(item.price for item in items)

# Bad
def calculateTotalPrice(items):
    return sum([item.price for item in items])
```

### 3. Use Type Hints

Type hints improve code readability and help catch errors:

```python
from typing import List, Optional

def process_users(users: List[dict]) -> Optional[int]:
    """Process a list of users and return count."""
    if not users:
        return None
    return len(users)
```

## Django-Specific Best Practices

### 1. Use Django Settings

```python
# settings.py
import os
from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
DATABASE_URL = config('DATABASE_URL')
```

### 2. Model Best Practices

```python
from django.db import models
from django.core.validators import MinValueValidator

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    
    def __str__(self):
        return self.name
```

### 3. View Best Practices

```python
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib import messages

class ProductListView(ListView):
    model = Product
    template_name = 'products/list.html'
    context_object_name = 'products'
    paginate_by = 20
    
    def get_queryset(self):
        return Product.objects.filter(is_active=True)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk, is_active=True)
    return render(request, 'products/detail.html', {'product': product})
```

## Security Best Practices

### 1. Use Environment Variables

Never hardcode sensitive information:

```python
# Good
SECRET_KEY = os.environ.get('SECRET_KEY')

# Bad
SECRET_KEY = 'my-secret-key-123'
```

### 2. Validate Input

Always validate user input:

```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    
    def clean_message(self):
        message = self.cleaned_data['message']
        if len(message) < 10:
            raise forms.ValidationError("Message must be at least 10 characters long.")
        return message
```

## Performance Best Practices

### 1. Use Database Optimization

```python
# Use select_related for foreign keys
products = Product.objects.select_related('category').all()

# Use prefetch_related for many-to-many
products = Product.objects.prefetch_related('tags').all()

# Use only() to limit fields
products = Product.objects.only('name', 'price').all()
```

### 2. Use Caching

```python
from django.core.cache import cache

def get_expensive_data():
    data = cache.get('expensive_data')
    if data is None:
        data = perform_expensive_operation()
        cache.set('expensive_data', data, 300)  # Cache for 5 minutes
    return data
```

## Testing Best Practices

### 1. Write Unit Tests

```python
from django.test import TestCase
from django.urls import reverse
from .models import Product

class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name='Test Product',
            price=10.00
        )
    
    def test_product_creation(self):
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.price, 10.00)
    
    def test_product_str(self):
        self.assertEqual(str(self.product), 'Test Product')
```

## Conclusion

Following these best practices will help you write better Python code and build more maintainable web applications. Remember to always prioritize readability, security, and performance.

Happy coding!''',
                'excerpt': 'Learn essential Python best practices for web development. This comprehensive guide covers code organization, security, performance, and testing.',
                'published': True,
                'featured': False,
                'tags': 'python, django, best-practices, web-development, programming',
            }
        ]
        
        for post_data in blog_posts_data:
            blog_post, created = BlogPost.objects.get_or_create(
                slug=post_data['slug'],
                defaults=post_data
            )
            if created:
                self.stdout.write(f'Created blog post: {blog_post.title}')
        
        
        self.stdout.write(
            self.style.SUCCESS('Successfully populated database with sample data!')
        )
