from django import forms
from .models import Review

'''class ReviewForm(forms.Form):
    user_name=forms.CharField(label='Your Name',max_length=10,error_messages=
        {'required':'Name cant be empty',
        'max_length':"Length exceded"}
        )
    review_text=forms.CharField(label='Your feedback',widget=forms.Textarea,max_length=200)
    rating=forms.IntegerField(label='Your Rating',min_value=1,max_value=5)
'''
#required=False.

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        #fields=['user_name','review_text','rating']
        fields='__all__'
        #exlude=['']
        labels={
            'user_name':'Your Name',
            'review_text':'Your Feedback',
            'rating':'Your Rating'
        }
        error_messages={
            'user_name':{
                'required':'Your name can not be empty',
                'max_length':'Maximum length exceeded'
            }
        }
        