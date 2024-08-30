from django.urls import path
from . import views
urlpatterns = [
    path('v1/', views.index),
    path('v1/tools/lookup', views.get_ipv4),
    path('v1/tools/validate', views.validate_ipv4), 
    path('v1/history', views.get_history), 

]
