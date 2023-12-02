from app1.models import*
from django import forms
class studentform(forms.ModelForm):
    class Meta:
        model=student
        fields='__all__'
