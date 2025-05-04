from django import forms
from gallery.models import Category

class EmailForm(forms.Form):
    
    name = forms.CharField(widget=forms.TextInput())
    phone_number = forms.CharField(widget=forms.TextInput())
    email = forms.CharField(widget=forms.EmailInput())
    message = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'textarea'
    }))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['theme_message'] = forms.ChoiceField(
            choices=[(i.id, i.name) for i in Category.objects.all()]
        )