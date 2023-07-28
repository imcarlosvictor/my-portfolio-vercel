from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    company = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)

