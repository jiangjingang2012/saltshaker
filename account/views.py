from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login

def login_view(request):
    msg = []
    if request.POST:
        if len(request.POST.get('next')) >0:
            _next=request.POST.get('next')
        else:
            _next="/"
        
        _remember = request.POST.get('remember')
        #if _remember != "remember":
        #    pass
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect(_next)
            else:
                msg.append("Disabled account")
        else:
            msg.append("Password error")
    return render(request, 'account/login.html', {'errors': msg})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/account/login')

