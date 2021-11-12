
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.utils.timezone import now


# Create your models here.

class UserProfile(models.Model):  
    user = models.OneToOneField(User, related_name='profile',on_delete=CASCADE)
    full_name=models.CharField(max_length=50)
    location = models.CharField(max_length=140)  
    gender = models.CharField(max_length=140) 
    mobile=models.CharField(max_length=50) 


    def __str__(self):
        return self.full_name









cotegory=[('sad_sayeri','sad_sayeri'),
('love_sayeri','love_sayeri'),
('birthday_sayeri','birthday_sayeri'),
('heart_sayeri','heart_sayeri'),
('attitude_sayeri','attitude_sayeri')
]



STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200)
    image=models.ImageField(upload_to='images/')
   # slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    cotegory=models.CharField(max_length=100,choices=cotegory,default='love_sayeri')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class blogcomment(models.Model):
    sn=models.AutoField(primary_key=True)
    comment=models.TextField()
    userc=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    postid=models.IntegerField(null=True)
    parent=models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp=models.DateTimeField(default=now)

    def __str__(self):
        return self.comment



class bloglike(models.Model):
    sn=models.AutoField(primary_key=True)
    userc=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    postid=models.IntegerField(null=True)
    parent=models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp=models.DateTimeField(default=now)

    # def __str__(self):
    #     return self.postid


class likeoncomment(models.Model):
    userc=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    postid=models.IntegerField(null=True)
    comenttid=models.IntegerField(null=True)
    parent=models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp=models.DateTimeField(default=now)



class notification(models.Model):
    userc=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    postid=models.IntegerField(null=True)
    postauthor=models.CharField(max_length=50)
    comment=models.TextField()
    timestamp=models.DateTimeField(default=now)

