# NOTE: Bu fayl eski variant. URL'lar `accounts/views_clean.py` dan import qilinadi.
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, LoginForm
from django.views import View   
from django.contrib.auth import login, logout, authenticate
from .forms import ProfileEditForm
from django.views.generic import TemplateView
from config.mixins import MyLoginRequiredMixin
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import MyPasswordChangeForm


# Create your views here.
class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, "accounts/signup.html", {"form": form})
    
    def post(self, request):
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            raw_password = form.cleaned_data.get("password")
            user.set_password(raw_password)
            user.save()
            login(request, user)
            return redirect("home")
        return render(request, "accounts/signup.html", {"form": form})


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "accounts/login.html", {"form": form})
    
    def post(self, request):
        form = LoginForm(request.POST)   
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect("home") # Muvaffaqiyatli kirsa bosh sahifaga
            else:
                form.add_error(None, "Username yoki parol noto'g'ri!")

        return render(request, "accounts/login.html", {"form": form})
    

class LogoutView(View):
    def post(self, request):
        logout(request)
        return redirect("home")
    

class ProfileView(MyLoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"


class ProfileEditView(MyLoginRequiredMixin, View):
    def get(self, request):
        # Formaga joriy foydalanuvchi ma'lumotlarini (instance) yuklaymiz
        form = ProfileEditForm(instance=request.user)
        return render(request, "accounts/profile_edit.html", {"form": form})

    def post(self, request):
        # Foydalanuvchi yuborgan yangi ma'lumotlarni instance bilan birga qabul qilamiz
        form = ProfileEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile") # Profil sahifasiga qaytaramiz
        return render(request, "accounts/profile_edit.html", {"form": form})


class ChangePasswordView(MyLoginRequiredMixin, View):
    template_name = 'accounts/change_password.html'

    def get(self, request):
        # Sahifa ochilganda bo'sh forma yuboramiz
        form = MyPasswordChangeForm(user=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        # Ma'lumotlar yuborilganda formani to'ldiramiz
        form = MyPasswordChangeForm(user=request.user, data=request.POST)
        
        if form.is_valid():
            new_password = form.cleaned_data.get('new_password')
            
            # Parolni yangilash va saqlash
            request.user.set_password(new_password)
            request.user.save()
            
            # Sessiya o'chib ketmasligi uchun hashni yangilaymiz
            update_session_auth_hash(request, request.user)
            
            messages.success(request, "Parol muvaffaqiyatli o'zgartirildi! ✅")
            return redirect('profile')
        
        # Agar xatolik bo'lsa, xatolari bilan formani qaytaramiz
        messages.error(request, "Xatoliklarni to'g'rilang.")
        return render(request, self.template_name, {'form': form})
