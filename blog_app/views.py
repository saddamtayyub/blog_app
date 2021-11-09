from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.shortcuts import render, redirect
from django.http import request
# decorator login
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import postform

# user login logout
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import authenticate, logout,login,update_session_auth_hash



# Create your views here.

def indexpage(request):
    data =Post.objects.all()
    #return HttpResponse('index page')
    return render(request,'index.html',{'data':data})



# login system
def loginuser(request):
    if request.method=='POST':
        name=request.POST['name']
        psw=request.POST['password']
        user = authenticate(request, username=name, password=psw)
        if user is not None:
            login(request, user)
            #return HttpResponse('login suc')
            return redirect('userdashboard')
        else:
            return HttpResponse('incorect password or name')
    return render(request,'login.html')




# sign up user
def signupuser(request):
    if request.method=="POST":
        fm=UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            print("user created")    
            return redirect("login")
    fm=UserCreationForm()
    return render(request,'signup.html',{'form':fm})




  # change password 
def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                # session update 
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, 'Your password was successfully updated!')
                return redirect('userdashboard')
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = PasswordChangeForm(request.user)
        return render(request, 'change_password.html', {'form': form})
    return redirect('login')

# forget password
def forgot_password(request):
    if request.method == 'POST':
        return password_reset(request, 
            from_email=request.POST.get('email'))
    else:
        return render(request, 'forgot_password.html')


# logout system
def logoutuser(request):
    logout(request)
    return redirect('home')

def userdashboard(request):
    data =Post.objects.all()
    #return HttpResponse('index page')
    return render(request,'userdashboard.html',{'data':data})





def blogpost(request):
    
    if request.method == 'POST':
        fm=postform(request.POST, request.FILES)
        #print('=============',fm)
        if fm.is_valid():
            fm.save()
            return redirect('userdashboard')
        return HttpResponse('not valid data')
    form=postform
    return render(request,'post.html',{'form':form})    


def delete(request,id):
    print(id)
    data=Post.objects.get(id=id)
    data.delete()
    return HttpResponse('data deleted')







# from django.contrib.auth.views import password_reset,password_reset_done,password_reset_confirm,password_reset_complete


# @login_required    
# def lexrequestpassword(request):
#     """
#     Reset Password
#     """
#     path = reverse('lexresetpassworddone')

#     return password_reset(request,post_reset_redirect=path)

# @login_required    
# def lexresetpassworddone(request):
#     """
#     Reset Password Done
#     """
#     path = reverse('lexresetpasswordconfirmed')

#     return password_reset_done(request,template_name=path)


# @login_required    
# def lexresetpasswordconfirmed(request):
#     """
#     Reset Password Confirmed
#     """
#     path = reverse('lexresetpasswordcompleted')

#     return password_reset_confirm(request,post_reset_redirect=path)

# @login_required    
# def lexresetpasswordcompleted(request):
#     """
#     Reset Password Completed
#     """
#     path = reverse('lexmain')

#     return password_reset_complete(request,post_reset_redirect=path) 