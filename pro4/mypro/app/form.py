from django import forms
from app.models import Book
class bookform(forms.ModelForm):
    class Meta:
        model=Book
        field='__all__'