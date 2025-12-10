from django.shortcuts import render
from .models import Project


# Create your views here.
def project_list(request):
    projects= Project.objects.all().order_by("-date_added")
    context= {
        "projects": projects
    }
    
    return render(request, "portfolio/list.html", context)