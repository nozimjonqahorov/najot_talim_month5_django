from django import forms
from .models import CustomUser
from django.core.exceptions import ValidationError
class SignUpForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email","age" , "username", "password", "photo"]

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name", "")
        if first_name != first_name.title():
            raise ValidationError("Ismda bosh harf katta bolsin va qolgan harflar kichkina bo'lsin! ")
        if len(first_name) < 3:
            raise ValidationError("Ism kamida 3-ta belgidan iborat bo'lsin ")
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name", "")
        if last_name != last_name.title():
            raise ValidationError("Familiya bosh harf bilan boshlanishi kerak!")
        if len(last_name) < 3:
            raise ValidationError("Familiya kamida 3 ta harfdan iborat bo'lsin!")
        return last_name
    
    def clean_age(self):
        age = self.cleaned_data.get("age", "")
        if age and (age < 5 or age > 150):
            raise ValidationError("Yosh 5 va 150 oralig'ida bo'lishi kerak!")
        return age
    
    def clean_email(self):
        email = self.cleaned_data.get("email", "")
        if not email.endswith("@gmail.com"):
            raise ValidationError("Faqat @gmail.com pochta manzillari qabul qilinadi!")
        return email
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Parollar bir-biriga mos kelmadi!")

        if password1 and len(password1) < 8:
            raise ValidationError("Parol juda qisqa, kamida 8 ta belgi kiriting!")

        return cleaned_data