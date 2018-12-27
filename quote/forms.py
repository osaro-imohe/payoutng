#from django import forms


#class QuoteForm(forms.Form):
    #item_name = forms.CharField(label='What are you selling?', max_length=100)
    #item_condition = forms.ChoiceField(choices=[('question','Question'),('other','other')])
    #first_name = forms.CharField(label='First Name?', max_length=100)
    #last_name = forms.CharField(label='Last Name?', max_length=100)
    #email = forms.EmailField(label='E-mail')

from django import forms
from quote.models import CustomUser



class ContactForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['brand', 'model', 'your_name','email',]
        widgets = {
            'brand': forms.TextInput(attrs={'placeholder': 'Brand e.g Samsung'}),
            'model': forms.TextInput(attrs={'placeholder': 'Model e.g Galaxy S9'}),
            'your_name': forms.TextInput(attrs={'placeholder': 'Your name'}),
            'email': forms.TextInput(attrs={'placeholder': 'E-mail'}),
        }
