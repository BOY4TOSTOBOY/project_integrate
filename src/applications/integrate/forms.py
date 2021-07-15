from .models import UrlRepository, Commit, ModifiedFile
from django.forms import ModelForm, TextInput


class UrlRepositoryForm(ModelForm):
    class Meta:
        model = UrlRepository
        fields = ['url_text']

        widgets = {
            "url_text": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the repository URL'
            })
        }
