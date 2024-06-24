from django import forms


class userForm(forms.Form):
    name=forms.CharField()
    email = forms.CharField()
    subject = forms.CharField()
    phone = forms.CharField()
    message = forms.CharField()
