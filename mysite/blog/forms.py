from pyexpat import model
from django import forms
from django import forms
from blog.models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ['author','title','text']
        widgets = {
            'title':forms.TextInput(attrs={
                'class':'textinputclass'
            }),
            'text':forms.Textarea(attrs={
                'class':'editable medium-editor-textarea postcontent'
            })
        }
        
class CommentForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ['name','text']
    
    widgets = {
        'name':forms.TextInput(attrs={
            'class': 'textinputclass'
        }),
        'text': forms.Textarea(attrs={
            'class': 'editable medium-editor-textarea'
        })
    }