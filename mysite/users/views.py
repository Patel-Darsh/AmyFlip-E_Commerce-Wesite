from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from users.forms import RegisterForm, ProfFormEditing, ProfFormCreating
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from users.models import Profile
from django.http import JsonResponse
import json





# Create your views here.
#-----------------------------------sign up page ---------------------------------------------------------------
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request,
                'welcome {} your account has been successfully created.now you may Create your profile below'.format(username)
            )
            usersobj = User.objects.get(username = username)
            userid = usersobj.id
            return redirect('profformcreate', user_id = userid)
        
    else:
        form = RegisterForm()


    context = {
        'form': form
    }
    
    return render(request,'users/register.html', context)

#-----------------------------------login page ---------------------------------------------------------------
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if (username == '') or (username is None):
            username = User.objects.get(email = email)

        user = authenticate(username=username, password=password)

        if user is None:
            messages.success(
                request,
                'invalid info, Try again'
            )
            return redirect('login')
    
        
        elif user.is_superuser:
            messages.success(
                request,
                'Welcome Superuser {}, your account have been logged in successfully'.format(user)
            )
            login(request, user)
            return redirect('products:index')

        elif user is  not None:
            messages.success(
                request,
                'Welcome {}, your account have been logged in successfully'.format(username)
            )
            login(request, user)
            return redirect('products:index')


    return render(request, 'users/login.html')

#-----------------------------------logout page ---------------------------------------------------------------
def logout_view(request):
    if request.method == 'POST':
        user = request.user.username
        logout(request)
        messages.success(
            request,
            '{}, your account have been logged out successfully'.format(user)
        )
        return redirect('products:index')
    return render(request, 'users/logout.html')

def ProfilePage(request):
    prof = Profile.objects.get(user = request.user.id)
    if not request.user.is_authenticated:

        return redirect('login')
    
    context = {
        'prof' : prof
    }

    return render(request,'users/profile.html', context)

def edit_profile(request, prof_id):
    prof = Profile.objects.get(id = prof_id)
    form = ProfFormEditing(request.POST or None, request.FILES or None, instance=prof)

    if request.method == 'POST':
        form.save()
        return redirect('profile')

    context = {
        'form' : form
    }
    return render(request, 'users/edit_profile.html', context)

def ProfViewCreating(request, user_id):

    prof = Profile.objects.get(user = user_id)
    profform = ProfFormCreating(request.POST or None, instance=prof)

    if request.method == 'POST':
        if profform.is_valid():
            profform.save()
            messages.success(

                request,
                'please login below'
            )
            return redirect('login')
    

    context = {
        'prof' : prof,
        'profform' : profform
    }

    return render(request, 'users/profformcreate.html', context)


