from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from pages.models import Contact

# Create your views here.

class HomePageView(CreateView):
    template_name = 'pages/index.html'
    model = Contact
    fields = ['name', 'email', 'message']
    success_url = '/'  
    def form_valid(self, form):
        # Save the contact form data
        response = super().form_valid(form)
        self.request.session['form_success'] = True     
        return response
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.session.get('form_success'):
            context['success'] = True
            del self.request.session['form_success']
        return context
    
class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

class EducationPageView(TemplateView):
    template_name = 'pages/education.html'

class ProjectsPageView(TemplateView):
    template_name = 'pages/projects.html'
class ContactPageView(CreateView):
    template_name = 'pages/contact.html'
    model = Contact
    fields = ['name', 'email', 'message']
    success_url = '/contact/'  # Redirect to the view contact page after successful submission
    def form_valid(self, form):
        # Save the contact form data
        reponse = super().form_valid(form)
        self.request.session['form_success'] = True     
        return reponse
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.session.get('form_success'):
            context['success'] = True
            del self.request.session['form_success']
        return context
    


class ContactFormResultView(ListView):
    template_name = 'pages/view_contact.html'
    model = Contact


class ContactDetailView(DetailView):
    template_name='pages/details.html'
    model=Contact