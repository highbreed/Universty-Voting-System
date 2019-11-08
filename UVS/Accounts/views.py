from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


# Create your views here.


def index(request):
	templates = 'account_index.html'
	return render(request, templates)


def student_login(request):
	template = 'student_login.html'
	return render(request, template)

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
            ...
    else:
        return render(request, 'student_login.html')