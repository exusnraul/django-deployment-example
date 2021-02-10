from django import forms
from user_app.models import user_info

class Newuser(forms.ModelForm):
    class Meta():
        model = user_info
        fields = '__all__'
