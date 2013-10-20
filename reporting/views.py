from django.shortcuts import render, get_object_or_404
from django.http import Http404
from reporting.models import User

# Main Template file for the login static view
def index(request):
    return render(request, 'reporting/index.html')

def detail(request, full_name):
    name = get_object_or_404(User, pk=full_name)
    return render(request, 'reporting/404.html')