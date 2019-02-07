from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.Cal, name='Cal'),
    path('input/', views.InputNum, name='InputNum'),
]