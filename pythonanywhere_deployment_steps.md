# Complete PythonAnywhere Deployment Guide

## Prerequisites
- Your Django project ready
- GitHub repository (optional but recommended)
- Email address for account creation

## Step-by-Step Deployment

### Step 1: Create PythonAnywhere Account
1. Go to [pythonanywhere.com](https://pythonanywhere.com)
2. Click **"Sign up for a Beginner account"**
3. Choose **"Beginner"** (free tier)
4. Enter your details:
   - Username (this becomes your subdomain)
   - Email address
   - Password
5. Verify your email address
6. Log in to your account

### Step 2: Upload Your Django Project

#### Option A: Upload Files Directly
1. Go to **"Files"** tab
2. Navigate to `/home/yourusername/`
3. Create a new folder: `doni-portfolio`
4. Upload all your project files:
   - `manage.py`
   - `requirements.txt`
   - `portfolio/` folder
   - `portfolio_project/` folder
   - `templates/` folder
   - `static/` folder
   - `media/` folder

#### Option B: Clone from GitHub (Recommended)
1. Go to **"Consoles"** tab
2. Click **"Bash"** to open a console
3. Run these commands:
   ```bash
   cd /home/yourusername
   git clone https://github.com/yourusername/doni-portfolio.git
   cd doni-portfolio
   ```

### Step 3: Install Dependencies
1. In the Bash console, run:
   ```bash
   pip3.10 install --user -r requirements.txt
   ```
   (Replace 3.10 with your Python version)

### Step 4: Create Web App
1. Go to **"Web"** tab
2. Click **"Add a new web app"**
3. Choose **"Django"**
4. Select **"Next"**
5. Choose **"Manual configuration"**
6. Select **"Python 3.10"** (or latest available)
7. Click **"Next"**
8. Enter your project directory: `/home/yourusername/doni-portfolio`
9. Enter your project name: `portfolio_project`
10. Click **"Next"**

### Step 5: Configure Web App Settings
1. In the web app configuration page:
2. **WSGI configuration file**: Click the link to edit
3. Replace the content with:
   ```python
   import os
   import sys

   # Add your project directory to the Python path
   path = '/home/yourusername/doni-portfolio'
   if path not in sys.path:
       sys.path.append(path)

   # Set the Django settings module
   os.environ['DJANGO_SETTINGS_MODULE'] = 'portfolio_project.settings'

   # Import Django's WSGI application
   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```
4. **Save** the file

### Step 6: Set Up MySQL Database
1. Go to **"Databases"** tab
2. Click **"Create database"**
3. Choose **"MySQL"**
4. Enter database name: `default`
5. Click **"Create"**
6. **Copy the database details** (you'll need these)

### Step 7: Update Django Settings
1. Go to **"Files"** tab
2. Navigate to `/home/yourusername/doni-portfolio/portfolio_project/`
3. Edit `settings.py`
4. Update the DATABASES section:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'yourusername$default',
           'USER': 'yourusername',
           'PASSWORD': 'your-db-password',
           'HOST': 'yourusername.mysql.pythonanywhere.com',
           'OPTIONS': {
               'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
           },
       }
   }
   ```
5. Update ALLOWED_HOSTS:
   ```python
   ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']
   ```
6. Set DEBUG to False:
   ```python
   DEBUG = False
   ```
7. **Save** the file

### Step 8: Run Database Migrations
1. Go to **"Consoles"** tab
2. Click **"Bash"**
3. Run these commands:
   ```bash
   cd /home/yourusername/doni-portfolio
   python3.10 manage.py migrate
   python3.10 manage.py collectstatic --noinput
   python3.10 manage.py createsuperuser
   ```

### Step 9: Configure Static Files
1. Go to **"Web"** tab
2. In your web app configuration:
3. **Static files**: Add these mappings:
   - URL: `/static/` → Directory: `/home/yourusername/doni-portfolio/staticfiles`
   - URL: `/media/` → Directory: `/home/yourusername/doni-portfolio/media`

### Step 10: Deploy and Test
1. Go to **"Web"** tab
2. Click **"Reload"** button
3. Wait for the reload to complete
4. Visit your site: `https://yourusername.pythonanywhere.com`
5. Test the admin: `https://yourusername.pythonanywhere.com/admin/`

### Step 11: Add Your Content
1. Log into Django admin
2. Add your personal information
3. Add projects, skills, education, etc.
4. Upload your profile image and resume

## Troubleshooting

### Common Issues:
1. **Import Error**: Check Python path in WSGI file
2. **Database Error**: Verify database credentials
3. **Static Files**: Check static files mapping
4. **Permission Error**: Ensure file permissions are correct

### Useful Commands:
```bash
# Check Python version
python3.10 --version

# Check installed packages
pip3.10 list

# Check Django version
python3.10 manage.py version

# Run Django shell
python3.10 manage.py shell
```

## Your Portfolio Will Be Live At:
`https://yourusername.pythonanywhere.com`

## Important Notes:
- **Log in every 3 months** to keep account active
- **Free tier limits**: 512MB disk space, low CPU
- **Custom domain**: Not available on free tier
- **Email**: May need to configure SMTP settings

## Next Steps:
1. Set up custom domain (if needed)
2. Configure email settings
3. Add SSL certificate (automatic)
4. Monitor usage and performance
