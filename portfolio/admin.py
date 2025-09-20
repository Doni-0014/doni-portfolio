from django.contrib import admin
from .models import (
	Skill,
	Education,
	Certification,
	Project,
	BlogPost,
	ContactMessage,
	PersonalInfo,
)


@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
	list_display = (
		'name', 'title', 'email', 'phone', 'location', 'updated_at'
	)
	search_fields = ('name', 'title', 'email', 'location')
	readonly_fields = ('updated_at',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
	list_filter = ('is_read', 'created_at')
	search_fields = ('name', 'email', 'subject', 'message')
	readonly_fields = ('created_at',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
	list_display = ('name', 'category', 'proficiency', 'is_active', 'order')
	list_filter = ('category', 'is_active')
	search_fields = ('name',)
	ordering = ('order', 'name')


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
	list_display = (
		'institution', 'degree', 'start_date', 'end_date', 'is_current'
	)
	list_filter = ('is_current', 'start_date', 'end_date')
	search_fields = ('institution', 'degree', 'field_of_study')


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
	list_display = ('title', 'issuer', 'issue_date', 'expiry_date', 'is_active')
	list_filter = ('is_active', 'issue_date', 'expiry_date')
	search_fields = ('title', 'issuer', 'credential_id')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ('title', 'featured', 'created_at', 'updated_at', 'order')
	list_filter = ('featured', 'created_at')
	search_fields = ('title', 'description')
	filter_horizontal = ('tech_stack',)
	readonly_fields = ('created_at', 'updated_at')


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'published', 'featured', 'created_at')
	list_filter = ('published', 'featured', 'created_at')
	search_fields = ('title', 'content', 'tags')
	prepopulated_fields = {"slug": ("title",)}
	readonly_fields = ('created_at', 'updated_at')