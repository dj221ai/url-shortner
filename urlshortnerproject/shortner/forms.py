from django import forms
from .models import ShortenedURL

class ShortenedURLForm(forms.ModelForm):

    class Meta:
        model=ShortenedURL
        fields = ('original_url', )

        widgets = {
            'original_url': forms.TextInput(attrs={
                                            'class': 'form-control'
                                            })
        }

