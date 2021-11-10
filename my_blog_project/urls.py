"""my_blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import django
from django.conf.urls import *
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from blog_app import views

admin.site.site_header="BLOG Admin Panel"
admin.site.site_title="SHAYERI BLOG"
admin.site.index_title="MY SHAYERI BLOG"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.indexpage,name='home'),
    path('login',views.loginuser, name='login'),
    path('signupuser',views.signupuser,name='signupuser'),
    path('changepassword',views.change_password,name='changepassword'),
   
    path('logout',views.logoutuser,name='logout'),
    path('post',views.blogpost,name='post'),
    path('userdashboard',views.userdashboard,name='userdashboard'),
    path('postbyid<int:id>',views.postbyid,name='postbyid'),
    path('delete<int:id>',views.delete,name="delete"),
    path('update<int:id>',views.update,name="update"),
    path('comment',views.comment,name='comment'),
    path('like',views.like,name='like'),
    #forget password
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password_reset_complete.html'
         ),
         name='password_reset_complete'),
    
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
        
