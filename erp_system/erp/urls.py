from django.urls import path
from .views import * 
urlpatterns = [
    path("students/", StudentListView.as_view(), name="student-list"), 
    path("student/student-create", StudentCreateView.as_view(), name="student-create"),
    path("student/student-detail/<int:pk>/", StudentDetailView.as_view(), name="student-detail"),
    path("student/student-update/<int:pk>/", StudentUpdateView.as_view(), name="student-update"),
    path("student/student-delete/<int:pk>/", StudentDeleteView.as_view(), name="student-delete"),

    path("teachers/", TeacherListView.as_view(), name="teacher-list"), 
    path("teacher/teacher-create", TeacherCreateView.as_view(), name="teacher-create"),
    path("teacher/teacher-detail/<int:pk>/", TeacherDetailView.as_view(), name="teacher-detail"),
    path("teacher/teacher-update/<int:pk>/", TeacherUpdateView.as_view(), name="teacher-update"),
    path("teacher/teacher-delete/<int:pk>/", TeacherDeleteView.as_view(), name="teacher-delete"),

    path("groups/", GroupListView.as_view(), name="group-list"), 
    path("group/group-create", GroupCreateView.as_view(), name="group-create"),
    path("group/group-detail/<int:pk>/", GroupDetailView.as_view(), name="group-detail"),
    path("group/group-update/<int:pk>/", GroupUpdateView.as_view(), name="group-update"),
    path("group/group-delete/<int:pk>/", GroupDeleteView.as_view(), name="group-delete"),

    
]
