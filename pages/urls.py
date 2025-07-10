from django.urls import path
from pages.views import HomePageView, AboutPageView, EducationPageView, ProjectsPageView, ContactPageView, ContactFormResultView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('education/', EducationPageView.as_view(), name='education'),
    path('projects/', ProjectsPageView.as_view(), name='projects'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('view_contact/', ContactFormResultView.as_view(), name='view_contact'), 
]
