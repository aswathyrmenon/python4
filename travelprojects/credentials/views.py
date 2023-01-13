from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.shortcuts import redirect
# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,'login.html')
def register (request):
    if request.method == "POST":
        username = request.POST['USERNAME']
        firstname = request.POST['FIRSTNAME']
        lastname = request.POST['LASTNAME']
        email = request.POST['EMAIL']
        password = request.POST['PASSWORD']
        cpassword = request.POST['CONFIRM PASSWORD']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exists")
                return redirect('register')
            else:
                 user =User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
                 user.save();
            return redirect('login')

        else:
            messages.info(request,"incorrect password")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')