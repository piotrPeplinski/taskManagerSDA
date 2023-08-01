from django.shortcuts import render
from .forms import RegisterForm
from django.contrib.auth.models import User
import re
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
# czy hasla sa takie same
# czy username wolny
# czy email wolny
# walidacja maila
# walidacja hasla

# Create your views here.


def check_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    # pass the regular expression
    # and the string into the fullmatch() method
    if (re.fullmatch(regex, email)):
        return True
    else:
        return False


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
                emailValid = check_email(email)
                if emailValid:
                    try:
                        validate_password(password1)
                    except ValidationError as e:
                        return render(request, 'register.html', {'passwordErrors': e.messages, 'form': RegisterForm()})
                    else:
                        return render(request, 'register.html', {'message': 'success', 'form': RegisterForm()})
                else:
                    error = 'Invalid email. Try again.'
        else:
            error = 'Your passwords did not match. Try again.'

        return render(request, 'register.html', {'error': error, 'form': RegisterForm()})
