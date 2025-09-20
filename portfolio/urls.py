from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('projects/', views.ProjectsView.as_view(), name='projects'),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('api/projects/filter/', views.project_filter_ajax, name='project_filter'),
    path('loading/', views.loading_screen, name='loading'),
]
