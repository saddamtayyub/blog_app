from django.contrib import admin

# Register your models here.
from .models import Post ,blogcomment,bloglike,likeoncomment

admin.site.register(Post)
admin.site.register(blogcomment)
admin.site.register(bloglike)
admin.site.register(likeoncomment)
