from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import Http404, HttpResponseRedirect
from reporting.models import User
from django.contrib.auth import authenticate, login,logout
from django.core.context_processors import csrf




# Main Template file for the login static view
def base(request):
    return render(request, 'reporting/base.html')

def detail(request, full_name):
    name = get_object_or_404(User, pk=full_name)
    return render(request, 'reporting/404.html')


def login(request):
    c={}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def auth_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect('/reporting/loggedin')
        else:
            # Return a 'disabled account' error message
            return HttpResponseRedirect('/reporting/404')
    else:
        # Return an 'invalid login' error message.
        return HttpResponseRedirect('/reporting/404')

def loggedin(request):
    return render_to_response('loggedin.html',
                              {'full_name': request.user.username})
def invalid_login(request):
   logout(request)
   return HttpResponseRedirect('/reporting/base')
