from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from .models import (
    Project, ContactMessage, Certification, Education, 
    Skill, PersonalInfo
)
from .forms import ContactForm


class HomeView(TemplateView):
    template_name = 'portfolio/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'personal_info': PersonalInfo.objects.first(),
            'featured_projects': Project.objects.filter(featured=True)[:3],
        })
        return context


class AboutView(TemplateView):
    template_name = 'portfolio/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'personal_info': PersonalInfo.objects.first(),
            'skills': Skill.objects.filter(is_active=True),
            'education': Education.objects.all(),
            'certifications': Certification.objects.filter(is_active=True),
        })
        return context


class ProjectsView(ListView):
    model = Project
    template_name = 'portfolio/projects.html'
    context_object_name = 'projects'
    paginate_by = 6
    
    def get_queryset(self):
        queryset = Project.objects.all()
        tech_filter = self.request.GET.get('tech')
        if tech_filter:
            queryset = queryset.filter(tech_stack__name__icontains=tech_filter)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tech_skills'] = Skill.objects.filter(is_active=True)
        context['selected_tech'] = self.request.GET.get('tech', '')
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'portfolio/project_detail.html'
    context_object_name = 'project'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_projects'] = Project.objects.exclude(
            id=self.object.id
        ).filter(
            tech_stack__in=self.object.tech_stack.all()
        ).distinct()[:3]
        return context


"""Blog views removed as requested."""


class ContactView(FormView):
    template_name = 'portfolio/contact.html'
    form_class = ContactForm
    success_url = '/contact/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['personal_info'] = PersonalInfo.objects.first()
        return context
    
    def form_valid(self, form):
        # Save the contact message
        form.save()
        
        # Try to send email notification
        email_sent = form.send_email()
        
        if email_sent:
            messages.success(
                self.request, 
                'Thank you for your message! I\'ll get back to you soon.'
            )
        else:
            messages.warning(
                self.request, 
                'Your message has been saved, but there was an issue sending the notification email.'
            )
        
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(
            self.request, 
            'Please correct the errors below and try again.'
        )
        return super().form_invalid(form)


def project_filter_ajax(request):
    """AJAX endpoint for filtering projects by technology"""
    tech = request.GET.get('tech', '')
    projects = Project.objects.all()
    
    if tech:
        projects = projects.filter(tech_stack__name__icontains=tech)
    
    # Convert to JSON-serializable format
    projects_data = []
    for project in projects:
        projects_data.append({
            'id': project.id,
            'title': project.title,
            'description': project.description,
            'image_url': project.image.url if project.image else '',
            'github_url': project.github_url,
            'live_url': project.live_url,
            'tech_stack': [skill.name for skill in project.tech_stack.all()],
        })
    
    return JsonResponse({'projects': projects_data})


def loading_screen(request):
    """Simple loading screen view"""
    return render(request, 'portfolio/loading.html')
