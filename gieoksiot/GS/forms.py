from django import forms

class loginForm(forms.Form):
    ID = forms.CharField(label="ID", max_length=12)
    Password = forms.IntegerField(label="Password", required=False)
    
    