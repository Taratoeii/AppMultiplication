from django.urls import path
from . import views
app_name = 'app'
urlpatterns = [
    path('<int:id>/', views.Show, name='Show'),
    path('', views.InputNum, name='InputNum'),
    path('mul/', views.mul, name='mul'),
    path('keep/', views.keep, name='keep'),
]