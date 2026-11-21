from django.urls import path
from . import views

urlpatterns = [
    path('get-notifications/', views.get_notifications, name='get_notifications'),
    path('mark-as-read/', views.mark_as_read, name='mark_as_read'),
] 