# Imports
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
import string
import random
import os
from django.views.static import serve

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
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'upload.html', context)


def update(request, id):
    file = File.objects.get(id=id)
    owner = file.owner
    if request.session['user_id'] == owner.id:
        context = {}
        context['file'] = file
        context['user'] = owner
        return render(request, 'update.html', context)
    return redirect('/')


# def delete(request, id):
#     if request.method == 'GET':
#         return redirect('/')
#     context = {}
#     context['file'] = File.objects.get(id=id)
#     return render(request, 'update.html', context)


def file(request, id):
    file = File.objects.get(id=id)
    owner = file.owner
    context = {}
    context['file'] = File.objects.get(id=id)
    context['users'] = User.objects.all
    if 'user_id' in request.session:
        print("user_id in request.session")
        context['user'] = User.objects.get(id=request.session['user_id'])
        if request.session['user_id'] == owner.id:
            context['owner'] = owner

    return render(request, 'file.html', context)


def upload(request):
    if request.method == 'POST' and request.FILES['file']:
        print(request.POST)
        print(request.FILES)
        code = generate_code()
        new_file = File(name=request.POST['name'], location=request.FILES['file'],
                        code=code, owner=User.objects.get(id=request.session['user_id']), price=request.POST['price'], status=False)
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
        if request.POST['status'] == 'y':
            to_update.status = True
        elif request.POST['status'] == 'n':
            to_update.status = False
        to_update.save()
        print(to_update)
        return redirect(f'/file/{id}/update')
    return redirect('/update')


def generate_code(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def download_file(request, id):
    if request.method == 'POST':
        file_obj = File.objects.get(id=id)
        input_code = request.POST['code'].upper()
        if file_obj.code == input_code:
            filepath = f'storage/{file_obj.location}'
            return serve(request, os.path.basename(filepath), os.path.dirname(filepath))
        messages.error(request, 'Incorrect Code')
        return redirect(f'/file/{id}')
    return redirect(f'/file/{id}')
