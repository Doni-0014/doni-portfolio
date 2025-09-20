# Doni Alston G - Portfolio Website

A stunning, responsive Django-based portfolio web application showcasing the work and skills of Doni Alston G, a Python Full Stack Developer.

## 🌟 Features

### Visual & UX Design
- **Premium-quality UI** inspired by top-rated developer portfolios
- **Tailwind CSS** with custom styles and animations
- **Dark/Light mode toggle** with localStorage persistence
- **Responsive design** optimized for all screen sizes
- **Smooth animations** using AOS (Animate On Scroll)
- **Google Fonts** for elegant typography
- **Loading screens** and skeleton loaders

### Pages & Functionality
- **Home Page**: Hero section with profile, social links, featured projects, testimonials
- **About Page**: Timeline, skills with animated progress bars, education, certifications
- **Projects Page**: Dynamic project showcase with filtering by technology
- **Blog Page**: Markdown-supported blog with search functionality
- **Contact Page**: Styled contact form with email notifications

### Django Backend
- **Models**: Project, ContactMessage, Certification, Education, Skill, BlogPost, PersonalInfo
- **Class-based views** for all functionality
- **Django Forms** with crispy-tailwind styling
- **Admin interface** for content management
- **Email notifications** for contact form submissions

### Additional Features
- **Blog functionality** with Markdown support
- **Loading animations** and skeleton loaders
- **SEO optimized** with proper meta tags
- **Social sharing** for blog posts and projects
- **Search functionality** for blog posts
- **Project filtering** by technology stack

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- pip
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/donialston/portfolio.git
   cd portfolio
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Populate with sample data** (optional)
   ```bash
   python manage.py populate_data
   ```

8. **Run development server**
   ```bash
   python manage.py runserver
   ```

9. **Visit the website**
   Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser

## 📁 Project Structure

```
portfolio/
├── portfolio_project/          # Django project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── portfolio/                  # Main app
│   ├── models.py              # Database models
│   ├── views.py               # Class-based views
│   ├── forms.py               # Django forms
│   ├── admin.py               # Admin configuration
│   ├── urls.py                # URL patterns
│   └── management/            # Custom management commands
├── templates/                 # HTML templates
│   ├── base.html             # Base template
│   └── portfolio/            # App-specific templates
├── static/                   # Static files
│   └── css/                  # Custom CSS
├── media/                    # User uploaded files
├── requirements.txt          # Python dependencies
├── Procfile                  # Heroku deployment
├── render.yaml              # Render.com deployment
└── README.md                # This file
```

## 🛠️ Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (for local development)
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3

# Email Configuration
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
EMAIL_USE_TLS=True

# Production Settings (for deployment)
RENDER=False
DATABASE_URL=your-database-url
```

### Admin Panel

Access the admin panel at `/admin/` to manage:
- Personal information
- Skills and technologies
- Projects and portfolios
- Blog posts
- Contact messages
- Education and certifications

## 🚀 Deployment

### Render.com (Recommended)

1. **Connect your GitHub repository** to Render
2. **Create a new Web Service**
3. **Configure environment variables**:
   - `SECRET_KEY`: Generate a secure secret key
   - `DEBUG`: Set to `False`
   - `DATABASE_URL`: Will be provided by Render
   - `ALLOWED_HOSTS`: Your Render domain
   - `CSRF_TRUSTED_ORIGINS`: Your Render domain
   - Email settings for contact form

4. **Deploy** and your portfolio will be live!

### Heroku

1. **Install Heroku CLI**
2. **Login to Heroku**
   ```bash
   heroku login
   ```

3. **Create Heroku app**
   ```bash
   heroku create your-portfolio-app
   ```

4. **Set environment variables**
   ```bash
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set DEBUG=False
   # Add other environment variables
   ```

5. **Deploy**
   ```bash
   git push heroku main
   heroku run python manage.py migrate
   ```

## 🎨 Customization

### Personal Information
Update your personal information in the Django admin or directly in the database:
- Name, title, bio
- Contact information
- Social media links
- Profile image
- Resume/CV

### Styling
- Modify `static/css/custom.css` for custom styles
- Update Tailwind configuration in `templates/base.html`
- Change color scheme by updating CSS variables

### Content
- Add your projects through the admin panel
- Write blog posts with Markdown support
- Add skills and certifications
- Upload testimonials and reviews

## 📱 Responsive Design

The portfolio is fully responsive and optimized for:
- **Mobile devices** (320px and up)
- **Tablets** (768px and up)
- **Desktop** (1024px and up)
- **Large screens** (1280px and up)

## 🔧 Technologies Used

### Backend
- **Django 4.2.7** - Web framework
- **Python 3.11+** - Programming language
- **SQLite/PostgreSQL** - Database
- **Django REST Framework** - API framework

### Frontend
- **Tailwind CSS** - Utility-first CSS framework
- **JavaScript (ES6+)** - Interactive functionality
- **AOS** - Animate On Scroll library
- **Font Awesome** - Icons
- **Google Fonts** - Typography

### Deployment
- **Render.com** - Cloud hosting platform
- **WhiteNoise** - Static file serving
- **Gunicorn** - WSGI server

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📞 Contact

**Doni Alston G**
- Email: doni.alston@example.com
- GitHub: [@donialston](https://github.com/donialston)
- LinkedIn: [Doni Alston](https://linkedin.com/in/donialston)
- Twitter: [@donialston](https://twitter.com/donialston)

## 🙏 Acknowledgments

- [Django](https://djangoproject.com/) - The web framework
- [Tailwind CSS](https://tailwindcss.com/) - CSS framework
- [AOS](https://michalsnik.github.io/aos/) - Animation library
- [Font Awesome](https://fontawesome.com/) - Icons
- [Google Fonts](https://fonts.google.com/) - Typography

---

⭐ **Star this repository** if you found it helpful!
