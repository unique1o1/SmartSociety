from django import forms

class support(forms.Form):
    your_name = forms.CharField(max_length=50)
    your_message = forms.CharField(widget=forms.Textarea)
    your_email = forms.EmailField()
    your_number= forms.IntegerField()
    