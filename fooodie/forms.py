from django import forms
from fooodie.models import UserProfile, Photo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm): 
    class Meta: 
        model = UserProfile 
        fields = ('picture',)
        
class UserSearchBarForm(forms.Form):
    username=forms.CharField()
    
class UserSettings(forms.Form):
    username=forms.CharField()
    email = forms.EmailField()
    password = forms.PasswordInput()
    class Meta:
        model=UserProfile
        fields=('picture',)

class PhotoForm(forms.ModelForm):
    class Meta:
        model=Photo
        fields=('name', 'photo',)