from django.urls import path
from pages.views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('education/', EducationPageView.as_view(), name='education'),
    path('projects/', ProjectsPageView.as_view(), name='projects'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('contact/list/', ContactFormResultView.as_view(), name='view_contact'), 
    path('contact/details/<int:pk>/', ContactDetailView.as_view(), name='detail_contact')
]
