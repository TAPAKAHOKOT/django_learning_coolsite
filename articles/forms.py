from django import forms
from .models import *


class ArticlesCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Not selected'

    class Meta:
        model = Articles
        fields = ['category', 'title', 'content', 'cover']
        widgets = {
            'category': forms.Select(attrs={'class': 'form__select'}),
            'title': forms.TextInput(attrs={'class': 'form__input'}),
            'content': forms.Textarea(attrs={'class': 'form__area'}),
            'cover': forms.FileInput(attrs={'class': 'form__image'})
        }
