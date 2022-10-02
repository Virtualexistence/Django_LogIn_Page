from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import templates
from django.contrib.auth import authenticate, login
from django.contrib.auth.models  import User
from django.contrib import messages
from . import models


def home(request):
    return render(request, 'homepage.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        fname = request.POST.get('first name')
        lname = request.POST.get('last name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        con_passwrd = request.POST.get('c_password')

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your acc has been successfully created!")

        return redirect('signin')
    return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            return render(request, 'userspace.html', {'user': username})
        else:
            messages.error(request, 'Invalid credentials')
            return redirect("home")
        head_blog=request.POST.get('headfield')
        content_blog = request.POST.get("textfield")
        userh = models.Heading(title=head_blog, stuff=content_blog)
        userh.save()
    return render(request, 'signin.html')


def logout(request):
    return redirect("home")