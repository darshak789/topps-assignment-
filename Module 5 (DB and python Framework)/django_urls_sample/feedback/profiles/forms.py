from django import forms

class ProfileForm(forms.Form):
    user_image=forms.ImageField(allow_empty_file=None)# can change this by removing this attribute
    