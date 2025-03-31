from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User



class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='username',required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='password',required=True,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='password again',required=True,widget=forms.PasswordInput(attrs={'class':'form-control'}))


    class Meta:
        model = User
        fields = ('username','password1','password2')


    def save(self,commit=False):
        user = super(RegistrationForm,self).save(commit=False)
        user.username = self.cleaned_data['username']
        if commit:
            user.save()
        return user