from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.db.models import Q
from django.views.generic import TemplateView
from todos.models import Todo
# Create your views here.

class HomepageView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        # Asosiy (parent) contextni olamiz
        context = super().get_context_data(**kwargs)
        
        # Bazadagi birinchi 6 ta vazifani id bo'yicha tartiblab olamiz
        context['first_six'] = Todo.objects.all().order_by('id')[:6]
        
        return context

class AboutView(TemplateView):
    template_name = "pages/about.html"

    


