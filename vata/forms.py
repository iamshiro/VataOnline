from django import forms
from .models import Movie
from .models import AddComments


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'url']


class AddCommentsForm(forms.ModelForm):
    class Meta:
        model = AddComments
        fields = ('name','text_comments')