from django import forms
from froala_editor.widgets import FroalaEditor

from blogs.models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model  = Blog
        fields = ['content']