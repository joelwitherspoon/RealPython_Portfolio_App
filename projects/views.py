"""Views for the projects app"""
from django.shortcuts import render
from .models import Project


# Create your views here.
def all_projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/all_projects.html', context)

def project_detail(request,)