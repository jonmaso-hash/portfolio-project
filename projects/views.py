from django.shortcuts import render
from .models import Project


# Create your views here.
def projects_view(request):
    projects_list = Project.objects.all().order_by('-year') #ordering the projects by in descending order 
    context = {'projects': projects_list}
    return render(request, 'projects/project.html', context)