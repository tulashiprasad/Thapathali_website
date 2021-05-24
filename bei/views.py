from django.shortcuts import redirect, render, HttpResponse
from datetime import datetime
from bei.models import Contact
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
        
    active_info = {
        'home': 'active',
        'date': str(datetime.now())[:10],
    }
    return render(request, 'index.html', active_info)

    
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('login_username')
        password = request.POST.get('login_password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.error(request, f'Welcome To Thapathali Campus, {user.username}')
                return redirect('/')
                
            else:
                return redirect('/login')
        # else:
            # print('Invalid User name')
    return render(request, 'login.html')

    
def sign_up_user(request):
        
    if request.method == 'POST':
        username = request.POST.get('sign_up_username')
        password = request.POST.get('sign_up_password')
        email = request.POST.get('sign_up_email')
        comfirm_password = request.POST.get('confirm_sign_up_password')

        if password == comfirm_password:  
            user =  User.objects.create_user(username = username, password = password, email = email )
            user.save()
            messages.success(request, 'Congratulations! your account has been suceefully created')
            return redirect('/login')  
        else:
            messages.error(request, 'Password did not match please try again')
            return redirect('/login')  
    else:
        messages.error(request, 'Error!!')
        return redirect('/login')   
    

def logout_user(request):
    logout(request)
    messages.error(request, 'You are sucessfully loged out.')
    return redirect('/login')


def about(request):
    if request.user.is_anonymous:
        return redirect('/login')
    active_info = {
        'about': 'active'
    }
    return render(request, 'about.html', active_info)


def admission(request):
    if request.user.is_anonymous:
        return redirect('/login')
    active_info = {
        'notice': 'active'
    }
    return render(request, 'admission.html', active_info)


def contact(request):
    if request.user.is_anonymous:
        return redirect('/login')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        querry = request.POST.get('querry')

        contact_number = Contact(name=name, email=email, querry=querry)
        contact_number.save()
        messages.success(request, 'Your Query has been sucessffully submited to the authority')


    active_info = {
        'contact': 'active'
    }
    return render(request, 'contact.html', active_info)


def department(request):
    if request.user.is_anonymous:
        return redirect('/login')
    active_info = {
        'notice': 'active'
    }
    return render(request, 'department.html', active_info)


def examination(request):
    if request.user.is_anonymous:
        return redirect('/login')
    active_info = {
        'notice': 'active'
    }
    return render(request, 'examination.html', active_info)
