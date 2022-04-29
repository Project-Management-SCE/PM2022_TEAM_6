from django import forms
from voulnteers.models import volnteer,Feedback


class CreateNewVoulnteer(forms.Form):
    username = forms.CharField(label="Name", max_length=200)
    email = forms.EmailField(label="Email", max_length=200)
    password = forms.CharField(label="New password", widget=forms.PasswordInput)

    class Meta:
        model = volnteer
        fields = ['username', 'email', 'password']


class LoginVoulnteer(forms.Form):
    username = forms.CharField(label="Name", max_length=200)
    password = forms.CharField(label="password", widget=forms.PasswordInput)

    class Meta:
        model = volnteer
        fields = ['username', 'password']


class FeedbackForm(forms.Form):
    class Meta:
        model = Feedback
        fields = ['by', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 6, 'cols': 30})
        }
