from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm
from django.views import View   


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
            return redirect("home")
        return render(request, "accounts/signup.html", {"form": form})
