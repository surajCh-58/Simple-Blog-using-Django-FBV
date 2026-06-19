from django import forms
from . models import *

class Post_Form(forms.ModelForm):
    class Meta:
        model=blog_db
        fields=['title','slug','content']
        labels={
            'title':'Post Title',
            'slug':'Slug',
            'content':'content'
        }
        widgets={
            'title':forms.TextInput(attrs={'placeholder':'Enter title..'}),
            'slug':forms.TextInput(attrs={'placeholder':'Enter slug'}),
            'content':forms.Textarea(attrs={'content':'Enter Content'})
        }
        
    def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            common_class="form-control"
            for field in self.fields.values():
                field.widget.attrs.update({'class':common_class})