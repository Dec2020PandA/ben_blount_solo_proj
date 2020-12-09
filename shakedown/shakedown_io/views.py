from django.shortcuts import render, redirect
from django.contrib import messages
from log_reg.models import *
from .models import *

# Create your views here.


def index(request):
    if 'user_id' not in request.session:
        print("user_id not in request.session")
        return redirect('/login')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user,
    }
    return render(request, 'index.html', context)
