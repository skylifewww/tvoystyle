# from django.forms.models import ModelForm
# from article.models import Comments
from django import forms

from tvoy_style.fields import ReCaptchaField

from django import forms
from captcha.fields import ReCaptchaField

class FormWithCaptcha(forms.Form):
    captcha = ReCaptchaField()

class ReCaptchaForm(forms.Form):
    subject = forms.CharField(
            label='Your subject',
            widget=forms.TextInput(
                    attrs={'class': 'validate[required] text-input'}))
    email = forms.EmailField(
            label='Your e-mail address',
            required=False,
            widget=forms.TextInput(attrs={'class': 'validate[required,custom[email]] text-input'}))
    message = forms.CharField(
            label='Your message',
            widget=forms.Textarea(attrs={'class': 'validate[required,custom[onlyLetterNumber]] text-input'}))
    recaptcha = ReCaptchaField()
