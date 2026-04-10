from django import forms
from .models import CustomUser
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password



class SignUpForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email" , "username", "password"]

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
    


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email", "bio", "photo"] 


class MyPasswordChangeForm(forms.Form):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}), 
        label="Eski parol"
    )
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}), 
        label="Yangi parol"
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}), 
        label="Yangi parolni tasdiqlang"
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(MyPasswordChangeForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        old_password = cleaned_data.get("old_password")
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if old_password:
            # check_password o'rniga authenticate ishlatish xavfsizroq
            if not self.user.check_password(old_password):
                self.add_error('old_password', "Eski parolingiz noto'g'ri kiritildi!")

        # Yangi parollar bir-biriga mosligini tekshirish
        if new_password and confirm_password:
            if new_password != confirm_password:
                self.add_error('confirm_password', "Yangi parollar bir-biriga mos kelmadi!")
            
            # Yangi parol eski parol bilan bir xil bo'lmasligi kerak
            if new_password == old_password:
                self.add_error('new_password', "Yangi parol eski paroldan farq qilishi kerak!")

            # Django'ning built-in password validatorlari (min length, common password, etc.)
            if not self.errors.get("new_password") and not self.errors.get("confirm_password"):
                try:
                    validate_password(new_password, self.user)
                except ValidationError as exc:
                    for msg in exc.messages:
                        self.add_error("new_password", msg)

        return cleaned_data
