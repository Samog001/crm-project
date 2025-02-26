from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.Home.as_view(),),
    path('dashboard/', views.DashboardView.as_view(),name='dashboard'),
    path('students/', views.StudentsView.as_view(),name='students'),       
    path('batch/', views.BatchView.as_view(),name='batch'),
    path('registration/',views.RegistrationView.as_view(),name='registration'),
    path('student-detail/<str:uuid>',views.StudentDetailView.as_view(),name='student-detail'),
    path('student-delete/<str:uuid>',views.StudentDeleteView.as_view(),name='student-delete'),
    path('student-update/<str:uuid>',views.StudentUpdateView.as_view(),name='student-update'),
]