from django import forms
from django.db.models import fields
from . import models

class UserForm(forms.ModelForm):
    class Meta:
        model = models.myUser
        fields = '__all__'