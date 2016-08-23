# from django import forms

# from tvoy_style.fields import ReCaptchaField
from django import forms
# from captcha.fields import ReCaptchaField

# class FormWithCaptcha(forms.Form):
#     captcha = ReCaptchaField()



# our new form
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )


# class ContactForm(forms.Form):
#     contact_name = forms.CharField(
#             label='Your subject',
#             widget=forms.TextInput(
#                     attrs={'class': 'validate[required] text-input'}))
#     contact_email = forms.EmailField(
#             label='Your e-mail address',
#             required=False,
#             widget=forms.TextInput(attrs={'class': 'validate[required,custom[email]] text-input'}))
#     content = forms.CharField(
#             label='Your message',
#             widget=forms.Textarea(attrs={'class': 'validate[required,custom[onlyLetterNumber]] text-input'}))

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_email'].label = "Your email:"
        self.fields['content'].label = "What do you want to say?"
    