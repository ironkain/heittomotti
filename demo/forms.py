from django import forms

from .models import Tilaus

class PostForm(forms.ModelForm):

    class Meta:
        model = Tilaus
        fields = ('koivuklapeja', 'nimi', 'osoite', 'puhelin', 'sposti',)
