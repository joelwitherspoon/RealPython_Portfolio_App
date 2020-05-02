"""URLs for the projects app"""

from django.urls import path
from . import views

app_name = 'projects'
urlpatterns = [
    # Home page
    path('', views.all_projects),
    path('<int:pk>',views.project_detail),
]
