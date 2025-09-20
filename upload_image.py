#!/usr/bin/env python
"""
Simple script to upload a profile image to the portfolio.
Place your image file in the same directory as this script and run it.
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from portfolio.models import PersonalInfo
from django.core.files import File

def upload_profile_image(image_path):
    """Upload a profile image to the PersonalInfo model."""
    try:
        # Get or create personal info
        personal_info, created = PersonalInfo.objects.get_or_create(
            name="Doni Alston G",
            defaults={
                'title': 'Python Full Stack Developer',
                'bio': 'Passionate about creating innovative web solutions with Python, Django, and modern frontend technologies.',
                'email': 'doni.alston@example.com',
            }
        )
        
        # Open and save the image
        with open(image_path, 'rb') as f:
            personal_info.profile_image.save(
                os.path.basename(image_path),
                File(f),
                save=True
            )
        
        print(f"✅ Successfully uploaded profile image: {image_path}")
        print(f"Image saved as: {personal_info.profile_image.name}")
        
    except FileNotFoundError:
        print(f"❌ Error: Image file '{image_path}' not found.")
        print("Please make sure the image file is in the same directory as this script.")
    except Exception as e:
        print(f"❌ Error uploading image: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python upload_image.py <image_file_path>")
        print("Example: python upload_image.py my_photo.jpg")
        sys.exit(1)
    
    image_path = sys.argv[1]
    upload_profile_image(image_path)
