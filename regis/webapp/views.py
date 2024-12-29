# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
# from django.contrib import messages
# from .forms import RegisterForm

# def home(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']

#         # Authenticate user
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             auth_login(request, user)
#             messages.success(request, 'You have been logged in successfully')
#             return redirect('home')
#         else:
#             messages.error(request, 'Invalid credentials, please try again')
#             return redirect('home')
#     else:
#         return render(request, 'home.html', {})

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             auth_login(request, user)
#             messages.success(request, 'You have been logged in successfully')
#             return redirect('home')
#         else:
#             messages.error(request, 'Invalid credentials, please try again')
#             return redirect('login')
#     else:
#         return render(request, 'login.html')

# def logout(request):
#     auth_logout(request)
#     messages.success(request, 'You have been logged out')
#     return redirect('home')

# def register_user(request):
# 	if request.method == 'POST':
# 		form = RegisterForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			# Authenticate and login
# 			username = form.cleaned_data['username']
# 			password = form.cleaned_data['password1']
# 			user = authenticate(username=username, password=password)
# 			login(request, user)
# 			messages.success(request, "You Have Successfully Registered! Welcome!")
# 			return redirect('home')
# 	else:
# 		form = RegisterForm()
# 		return render(request, 'register_user.html', {'form':form})

# 	return render(request, 'register_user.html', {'form':form})
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .forms import RegisterForm
from .models import Record

def home(request):
    records = Record.objects.all()


    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'You have been logged in successfully')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials, please try again')
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'You have been logged in successfully')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials, please try again')
            return redirect('login')
    else:
        return render(request, 'home.html',)

def logout_user(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            messages.success(request, "You have successfully registered! Welcome!")
            return redirect('home')
    else:
        form = RegisterForm()
    
    return render(request, 'register_user.html', {'form': form})