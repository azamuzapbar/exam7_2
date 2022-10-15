from .models import Article
from django.forms import ModelForm, TextInput, Textarea

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['email', 'text', 'author']
        widgets = {
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'input email'
            }),
            "author": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'input name'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'input description'
            }),
        }