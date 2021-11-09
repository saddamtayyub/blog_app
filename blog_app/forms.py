from django.forms import ModelForm

from .models import Post

# Create the form class.
class postform(ModelForm):
    class Meta:         
        model= Post
        fields = '__all__'
