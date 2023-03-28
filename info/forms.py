from django import forms
from .models import Contact


# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = Contact
#         fields = '__all__'
        

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, label='Ad Soyad')
    email = forms.EmailField()
    phone = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea)
    
    