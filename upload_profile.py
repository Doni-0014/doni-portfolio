#!/usr/bin/env python
"""
Simple script to upload your profile image to the portfolio.
This bypasses the admin panel issues.
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from portfolio.models import PersonalInfo
from django.core.files import File

def upload_profile_image():
    """Upload a profile image to the PersonalInfo model."""
    print("🖼️  Profile Image Uploader")
    print("=" * 40)
    
    # Get or create personal info
    personal_info, created = PersonalInfo.objects.get_or_create(
        name="Doni Alston G",
        defaults={
            'title': 'Python Full Stack Developer',
            'bio': 'Passionate about creating innovative web solutions with Python, Django, and modern frontend technologies.',
            'email': 'doni.alston@example.com',
        }
    )
    
    print(f"📋 Current profile: {personal_info.name}")
    print(f"📧 Email: {personal_info.email}")
    
    if personal_info.profile_image:
        print(f"🖼️  Current image: {personal_info.profile_image.name}")
        response = input("Do you want to replace the current image? (y/n): ").lower()
        if response != 'y':
            print("❌ Image upload cancelled.")
            return
    
    # Get image path from user
    print("\n📁 Please enter the path to your image file:")
    print("   Example: C:\\Users\\YourName\\Pictures\\my_photo.jpg")
    print("   Or just the filename if it's in the same folder as this script")
    
    image_path = input("\nImage path: ").strip()
    
    # Remove quotes if user added them
    image_path = image_path.strip('"').strip("'")
    
    try:
        # Check if file exists
        if not os.path.exists(image_path):
            print(f"❌ Error: File '{image_path}' not found.")
            print("Please check the path and try again.")
            return
        
        # Check file size (max 5MB)
        file_size = os.path.getsize(image_path)
        if file_size > 5 * 1024 * 1024:  # 5MB
            print(f"❌ Error: File is too large ({file_size / 1024 / 1024:.1f}MB).")
            print("Please use an image smaller than 5MB.")
            return
        
        # Open and save the image
        with open(image_path, 'rb') as f:
            personal_info.profile_image.save(
                os.path.basename(image_path),
                File(f),
                save=True
            )
        
        print(f"\n✅ Successfully uploaded profile image!")
        print(f"📁 Image saved as: {personal_info.profile_image.name}")
        print(f"🌐 You can now view it at: http://127.0.0.1:8000")
        print(f"🔄 Refresh your browser to see the changes!")
        
    except FileNotFoundError:
        print(f"❌ Error: Image file '{image_path}' not found.")
        print("Please make sure the file path is correct.")
    except Exception as e:
        print(f"❌ Error uploading image: {e}")
        print("Please check the file format (JPG, PNG, GIF) and try again.")

if __name__ == "__main__":
    upload_profile_image()
