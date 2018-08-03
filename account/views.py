from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import FormView

from account.forms import *


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
    user = request.POST['username']
    pwd = request.POST['password']
    request.session['user'] = user
    user = authenticate(username=user, password=pwd)
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
