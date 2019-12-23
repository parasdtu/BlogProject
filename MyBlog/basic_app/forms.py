from django import forms
from basic_app.models import UserProfileInfo
from django.contrib.auth.models import User

class UserInfoForm(forms.ModelForm):
    #def check_username(value):
    password=forms.CharField(widget=forms.PasswordInput())
    verify_email=forms.EmailField(required=True)

    class Meta():
        model=User
        fields=('username','password','email')

    def clean(self):
        all_cleaned_data=super().clean()
        _email=all_cleaned_data['email']
        _vmail=all_cleaned_data['verify_email']
        if _email!=_vmail:
            raise forms.ValidationError("Emails Don't Match")



class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=('profile_pic',)
