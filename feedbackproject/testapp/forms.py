from django import forms
from django.core import validators

class FeedbackForm(forms.Form):
    name = forms.CharField()
    rollno = forms.IntegerField()
    email = forms.EmailField()
    password = forms.CharField(label='Enter password',widget=forms.PasswordInput)
    rpassword = forms.CharField(label='Password(Again)',widget=forms.PasswordInput)
    feedback = forms.CharField(widget=forms.Textarea)
    bot_handler = forms.CharField(required=False,widget=forms.HiddenInput)

    def clean(self):
        print("Total form validation.....")
        total_cleaned_data = super().clean()
        print("Validating Name")
        inputname  = total_cleaned_data["name"]
        if inputname[0].lower() != 's':
            raise forms.ValidationError("Name must start with 's'")
        print("Validating Roll Number")
        inputrollno = total_cleaned_data["rollno"]
        if inputrollno <=0:
            raise forms.ValidationError("Roll number must be greater than zero")
        inputmail = total_cleaned_data["email"]
        print("Validating Email ID")
        if inputmail[-10:] != '@gmail.com':
            raise forms.ValidationError("Email must be '@gmail.com'")
        print("Password and Confirm Password")
        password = total_cleaned_data["password"]
        rpassword = total_cleaned_data["rpassword"]
        if password != rpassword:
            raise forms.ValidationError("Both Passwords must be same......")
        bot_handler_data = total_cleaned_data["bot_handler"]
        if len(bot_handler_data) > 0:
            raise forms.ValidationError("Request from BOT...cant submit this form")



