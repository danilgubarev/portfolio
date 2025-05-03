from django import forms
from gallery.models import Category

class EmailForm(forms.Form):
    
    name = forms.CharField(widget=forms.TextInput())
    phone_number = forms.IntegerField(widget=forms.NumberInput())
    email = forms.CharField(widget=forms.EmailInput())
    
    # @staticmethod
    # def get_category():
    theme_message = forms.ChoiceField(choices=[(i.id, i.name) for i in Category.objects.all()])
    message = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'textarea'
    }))