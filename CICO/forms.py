
from django import forms
class ContactUsForm(forms.Form):
   #name = forms.CharField(required=False)
   #email = forms.EmailField()
   message = forms.CharField(max_length=1000)

class ConnectionForm(forms.Form):
   identification = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length=100)
   password = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length=100)
   