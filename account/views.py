from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.edit import FormView

from account.forms import *
from menu.views import *


def register(request):
    fields = {
        'first_name': request.POST["first-name"],
        'last_name': request.POST['last-name'],
        'restaurant': Restaurante.objects.get(code=request.POST['restaurant-code']),
        'email': request.POST['register-email'],
        'password': request.POST['register-pwd'],
        'is_admin': request.POST['user-type'] == 'admin',
        'is_manager': request.POST['user-type'] == 'manager',
        'is_employee': request.POST['user-type'] == 'employee',
    }
    CustomUser.objects.create(**fields)
    return redirect("account:account")


def account(request):
    try:
        user = request.session['user']
    except KeyError:
        return HttpResponseRedirect(reverse("account:login"))
    context = {
        'user': user
    }
    return render(request, 'account/account.html', context)


def login_display(request, failed=''):
    context = {failed: failed}
    return render(request, 'account/login.html', context)


def login_submit(request):
    email = request.POST['input-email']
    pwd = request.POST['password']
    user = authenticate(username=email, password=pwd)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('account:dashboard'))
    else:
        return HttpResponseRedirect(reverse('account:login_fail',
                                            kwargs={'failed': 'failed'}))


def my_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('account:login'))


def dashboard(request):
    return render(request, 'account/dashboard.html')
