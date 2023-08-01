from django.shortcuts import render
from .forms import RegisterForm
from django.contrib.auth.models import User

# czy hasla sa takie same
# czy username wolny
# czy email wolny
# walidacja hasla

# Create your views here.


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html', {'form': RegisterForm()})
    else:  # POST
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            usernameTaken = User.objects.filter(username=username).exists()
            emailTaken = User.objects.filter(email=email).exists()
            if emailTaken:
                error = 'This email is already taken. Try again.'
            if usernameTaken:
                error = 'This username is already taken. Try again.'

            if not emailTaken and not usernameTaken:
                return render(request, 'register.html', {'message': 'success', 'form': RegisterForm()})
        else:
            error = 'Your passwords did not match. Try again.'

        return render(request, 'register.html', {'error': error, 'form': RegisterForm()})
