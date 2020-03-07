from django import forms
from . import models

class CreateReview(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'body']
