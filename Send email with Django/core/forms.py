from django import forms

from core.models import ContactUs


class ContactForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'your name ...'}))
    email = forms.EmailField(label='',widget=forms.TextInput(attrs={'placeholder': 'email ...'}))
    message = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'your message ...'}))

    class Meta:
        model = ContactUs
        fields = ('name', 'email', 'message')
