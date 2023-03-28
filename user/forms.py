from django import forms
from django.contrib.auth.models import User
import re

username_compiler = re.compile(r'^\w{5,}$')


class RegisterForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password_again = forms.CharField(widget=forms.PasswordInput)
    
    def save(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = User.objects.create_user(
            username=username, 
            first_name=first_name, 
            last_name=last_name, 
            email=email, 
            password=password
        )
        return user
        

    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        if not username_compiler.match(username):
            raise forms.ValidationError('Username yazilisi duzgun deyil')
        elif User.objects.filter(username=username).exists():
            raise forms.ValidationError('Bu istifadeci adi artiq islenilib')

        return username
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Bu email artiq islenilib')
        
        return email
    
    def clean(self):
        super().clean()
        password = self.cleaned_data.get('password')
        password_again = self.cleaned_data.get('password_again')

        if password and password_again and password != password_again:
            raise forms.ValidationError('Sifreler eyni deyil!')
        

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

        