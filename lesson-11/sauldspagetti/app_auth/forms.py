from django import forms
from django.contrib.auth.forms import UserCreationForm


class RegForm(UserCreationForm):
    username = forms.CharField(max_length=64,widget=forms.TextInput(attrs={'class':'form-control form-control-lg'}))
    name = forms.CharField(max_length=64,widget=forms.TextInput(attrs={'class':'form-control form-control-lg'}),required=False)
    surname = forms.CharField(max_length=64,widget=forms.TextInput(attrs={'class':'form-control form-control-lg'}),required=False)
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg'}))
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'name','surname','password1','password2']
