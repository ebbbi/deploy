from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    Choice=(('PUBLIC','public'), ('PRIVATE', 'private'))
    category=forms.ChoiceField(choices=Choice, widget=forms.Select)
    
    class Meta:
        model=Post
        fields=['title', 'eyes', 'lip', 'face', 'category',]
        
        
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['eyes'].widget.attrs.update({'class' : 'eyes'})
        self.fields['lip'].widget.attrs.update({'class' : 'lip'})
        self.fields['face'].widget.attrs.update({'class' : 'face'})

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['content',]
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({'class' : 'content'})