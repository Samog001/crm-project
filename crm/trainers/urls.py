from django.urls import path 
from .import views

urlpatterns=[
   
    
    path('trainer-list/',views.TrainerListView.as_view(),name='trainer-list'),
    
    path('registration1/',views.TrainerRegistrationView.as_view(),name='registration1'),
    
    path('trainer-detail/<str:uuid>/',views.TrainerDetailView.as_view(),name='trainer-detail'),
    
    # path('error-404/',views.Error404View.as_view(),name='error-404'),
    
    path('trainer-delete/<str:uuid>/',views.TrainerDeleteView.as_view(),name='trainer-delete'),
    
    path('trainer-update/<str:uuid>/',views.TrainerUpdateView.as_view(),name='trainer-update'),
    
]