from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.shortcuts import render, redirect
from django.http import request
# decorator login
from django.contrib.auth.decorators import login_required
from .models import Post , blogcomment, bloglike
from .forms import postform



# user login logout
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import authenticate, logout,login,update_session_auth_hash



# Create your views here.

def indexpage(request):
    type=request.GET.get('type')
    print(type)
    if type=='sad_sayeri':  
        data =Post.objects.filter(cotegory=type)
        return render(request,'index.html',{'data':data})
    elif type=='love_sayeri':              
        data =Post.objects.filter(cotegory=type)
        return render(request,'index.html',{'data':data}) 
    elif type=='sad_sayeri':                                      
        data =Post.objects.filter(cotegory=type)
        return render(request,'index.html',{'data':data})
    elif type=='birthday_sayeri':                                      
        data =Post.objects.filter(cotegory=type)
        return render(request,'index.html',{'data':data})
    elif type=='heart_sayeri':                                      
        data =Post.objects.filter(cotegory=type)
        return render(request,'index.html',{'data':data})
    elif type=='attitude_sayeri':                                      
        data =Post.objects.filter(cotegory=type)
        return render(request,'index.html',{'data':data})    
    else:           #all shayeri
       data =Post.objects.all()
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
@login_required
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




#logout system

def logoutuser(request):
    logout(request)
    return redirect('home')


@login_required
def userdashboard(request):
    data =Post.objects.all()
    user=request.user
    return render(request,'userdashboard.html',{'data':data,'user':user})

# data by id
def postbyid(request,id):
    data =Post.objects.get(id=id)
    lk=bloglike.objects.filter(postid=id)
    cm=blogcomment.objects.filter(postid=id)
    user=request.user
    print("===============",user)
    return render(request,'postbyid.html',{'post':data,'cm':cm,'like':lk,'user':user})


@login_required
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


@login_required
def delete(request,id):
    print(id)
    data=Post.objects.get(id=id)
    data.delete()
    return HttpResponse('data deleted')


@login_required
def update(request,id):
    print(id)
    data=Post.objects.get(id=id)
    if request.method=='POST':
        fm=postform(request.POST, request.FILES,instance=data)
        fm.save()
        return redirect('userdashboard') 
    form=postform(instance=data)
    return render(request,'update.html',{'form':form})




def comment(request):
    comment=request.POST['comment']
    userc=request.user
    postid=request.POST['postid']
    d=postid
    post=Post.objects.get(id=postid)
    print("==",comment,"gggg",userc,postid,post)
    d=blogcomment(comment=comment,userc=userc,post=post,postid=d)
    if comment=="":
        return redirect(f'/postbyid{post.id}')
    d.save()
        
    return redirect(f'/postbyid{post.id}')
    #return HttpResponse('comment successfully')


def like(request):
    userc=request.user
    postid=request.POST['postid']
    d=postid
    post=Post.objects.get(id=postid)
    d=bloglike(userc=userc,post=post,postid=d)
    try:
        l=bloglike.objects.get(postid=postid)
        user=l.userc
        if userc==user:
            return redirect(f'/postbyid{post.id}')
    except:
        d.save()   
        return redirect(f'/postbyid{post.id}')