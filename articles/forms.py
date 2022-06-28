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
            'category': forms.Select(
                attrs={
                    'class': 'input__item form__select',
                    'placeholder': 'Category'
                }
            ),
            'title': forms.TextInput(
                attrs={
                    'class': 'input__item form__input',
                    'placeholder': 'Title'
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'input__item form__area',
                    'placeholder': 'Content'
                }
            ),
            'cover': forms.FileInput(
                attrs={
                    'class': 'input__item form__image',
                    'placeholder': 'Cover'
                }
            )
        }
