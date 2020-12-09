from django.shortcuts import redirect, render
from django.contrib import messages
import bcrypt
from .models import User


def login(request):
    if 'user_id' in request.session:
        print("user_id already in request.session")
        return redirect('/')
    return render(request, 'login.html')

# def success(request):
#     return redirect(request, '/')
#     if 'user_id' not in request.session:
#         print("user_id not in request.session")
#         return redirect('/')
#     print('user_id in session')

#     user = User.objects.get(id=request.session['user_id'])
#     print(user)
#     context = {
#         'user': user
#     }
#     return render(request, 'success.html', context)


def login_user(request):
    if request.method == 'GET':
        return redirect('/')
    # Else
    if not User.objects.authenticate(request.POST['email'], request.POST['pw']):  # noqa
        messages.error(request, 'Wrong Email/Password')
        return redirect('/')
    else:
        user = User.objects.get(email=request.POST['email'])
        request.session['user_id'] = user.id
        request.session['fname'] = user.first_name
        messages.success(request, "You have successfully logged in!")
        return redirect('/')


def logout(request):
    request.session.clear()
    messages.success(request, "You have successfully logged out!")
    return redirect('/')


def create_user(request):
    if request.method == 'GET':
        return redirect('/')

    # Validate form
    errors = User.objects.validate(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        new_user = User.objects.register(request.POST)
        request.session['user_id'] = new_user.id
        messages.success(request, "You have successfully registered!")
        return redirect('/')
