from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import *
from .models import *


class StudentCreateView(View):
    def get(self, request):
        form = StudentForm()
        return render(request, "student/create.html", {"form": form})

    def post(self, request):
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("student-list")
        return render(request, "student/create.html", {"form": form})
        


class StudentListView(View):
    def get(self, request):
        students = Student.objects.all()
        return render(request, "student/list.html", {"students":students})
        

class StudentDetailView(View):
    def get(self, request, pk):
        student = get_object_or_404(Student, pk = pk)
        return render(request, "student/detail.html", {"student":student})
    

class StudentUpdateView(View):
    def get(self, request, pk):
        student = get_object_or_404(Student, pk = pk)
        form = StudentForm(instance=student)
        return render(request, "student/update.html", {"form":form, "student":student})
    
    def post(self, request, pk):
        student = get_object_or_404(Student, pk = pk)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("student-detail", pk)
        return render(request, "student/update.html", {"form":form, "student":student})


class StudentDeleteView(View):
    def get(self, request, pk):
        student = get_object_or_404(Student, pk = pk)
        return render(request, "student/delete.html", {"student":student})
    
    def post(self, request, pk):
        student = get_object_or_404(Student, pk = pk)
        student.delete()
        return redirect("student-list")
    

class TeacherCreateView(View):
    def get(self, request):
        form = TeacherForm()
        return render(request, "teacher/create.html", {"form": form})

    def post(self, request):
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("teacher-list")
        return render(request, "teacher/create.html", {"form": form})


class TeacherListView(View):
    def get(self, request):
        teachers = Teacher.objects.all()
        return render(request, "teacher/list.html", {"teachers":teachers})
        

class TeacherDetailView(View):
    def get(self, request, pk):
        teacher = get_object_or_404(Teacher, pk = pk)
        return render(request, "teacher/detail.html", {"teacher":teacher})
    

class TeacherUpdateView(View):
    def get(self, request, pk):
        teacher = get_object_or_404(Teacher, pk = pk)
        form = TeacherForm(instance=teacher)
        return render(request, "teacher/update.html", {"form":form, "teacher":teacher})
    
    def post(self, request, pk):
        teacher = get_object_or_404(Teacher, pk = pk)
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect("teacher-detail", pk)
        return render(request, "teacher/update.html", {"form":form, "teacher":teacher})


class TeacherDeleteView(View):
    def get(self, request, pk):
        teacher = get_object_or_404(Teacher, pk = pk)
        return render(request, "teacher/delete.html", {"teacher":teacher})
    
    def post(self, request, pk):
        teacher = get_object_or_404(Teacher, pk = pk)
        teacher.delete()
        return redirect("teacher-list")
    

class GroupCreateView(View):
    def get(self, request):
        form = GroupForm()
        return render(request, "group/create.html", {"form": form})

    def post(self, request):
        form = GroupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("group-list")
        return render(request, "group/create.html", {"form": form})


class GroupListView(View):
    def get(self, request):
        groups = Group.objects.all().select_related("teacher")
        return render(request, "group/list.html", {"groups":groups})
        

class GroupDetailView(View):
    def get(self, request, pk):
        group = get_object_or_404(Group, pk = pk)
        return render(request, "group/detail.html", {"group":group})
    

class GroupUpdateView(View):
    def get(self, request, pk):
        group = get_object_or_404(Group, pk = pk)
        form = GroupForm(instance=group)
        return render(request, "group/update.html", {"form":form, "group":group})
    
    def post(self, request, pk):
        group = get_object_or_404(Group, pk = pk)
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect("group-detail", pk)
        return render(request, "group/update.html", {"form":form, "group":group})


class GroupDeleteView(View):
    def get(self, request, pk):
        group = get_object_or_404(Group, pk = pk)
        return render(request, "group/delete.html", {"group":group})
    
    def post(self, request, pk):
        group = get_object_or_404(Group, pk = pk)
        group.delete()
        return redirect("group-list")
    
    