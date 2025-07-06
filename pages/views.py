from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'pages/index.html'
 
class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

class EducationPageView(TemplateView):
    template_name = 'pages/education.html'

class ProjectsPageView(TemplateView):
    template_name = 'pages/projects.html'
class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'