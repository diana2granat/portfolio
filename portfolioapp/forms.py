from django import forms

class ContactForm(forms.Form):
    recipient = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)