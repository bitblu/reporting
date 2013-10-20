from django.shortcuts import render

# Main Template file for the login static view
def index(request):
    return render(request, 'reporting/index.html')