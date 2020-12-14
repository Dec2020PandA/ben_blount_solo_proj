# Imports
from django.shortcuts import render, redirect
from django.contrib import messages
import string
import random
# Import Models
from log_reg.models import *
from .models import *

# Create your views here.


def index(request):
    if 'user_id' not in request.session:
        print("user_id not in request.session")
        return redirect('/login')
    user = User.objects.get(id=request.session['user_id'])
    files = File.objects.filter(owner=user)
    print(user.files)
    context = {
        'user': user,
        'files': files
    }
    return render(request, 'index.html', context)


def upload_page(request):
    return render(request, 'upload.html')


def update(request, id):
    if request.method == 'GET':
        return redirect('/')
    context = {}
    context['file'] = File.objects.get(id=id)
    return render(request, 'update.html', context)


def delete(request, id):
    if request.method == 'GET':
        return redirect('/')
    context = {}
    context['file'] = File.objects.get(id=id)
    return render(request, 'update.html', context)


def file(request, id):
    context = {}
    context['file'] = File.objects.get(id=id)
    return render(request, 'file.html', context)


def edit_file(request, id):
    context = {}
    context['file'] = File.objects.get(id=id)
    return render(request, 'update.html', context)


def upload(request):
    if request.method == 'POST' and request.FILES['file']:
        print(request.POST)
        print(request.FILES)
        code = generate_code()
        new_file = File(name=request.POST['name'], location=request.FILES['file'],
                        code=code, owner=User.objects.get(id=request.session['user_id']), price=request.POST['price'])
        new_file.save()
        print(new_file)
        id = new_file.id
        return redirect(f'/file/{id}')
    return redirect('/upload')


def save(request, id):
    if request.method == 'POST':
        print(request.POST)
        to_update = File.objects.get(id=id)
        print(to_update)
        if request.POST['new_code'] == 'y':
            code = generate_code()
            to_update.code = code
        to_update.name = request.POST['name']
        to_update.price = request.POST['price']
        to_update.paid
        to_update.save()
        print(to_update)
        return redirect(f'/file/{id}/update')
    return redirect('/update')


def generate_code(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
