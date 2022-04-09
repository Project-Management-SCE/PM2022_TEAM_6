from django import forms

class CreateNewVoulnteer(forms.Form):
    name=forms.CharField(label="Name",max_length=200)
    email=forms.EmailField(label="Email",max_length=200)
    psw=forms.CharField(label="New password",widget=forms.PasswordInput)