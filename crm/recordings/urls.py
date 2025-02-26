from django.urls import path
from.import views

urlpatterns = [
    path('recording/',views.RecordingsView.as_view(),name='recordings')
]
