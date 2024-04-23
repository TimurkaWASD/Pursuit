from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('profile_editor/', views.profile_editor, name='profile_editor'),
    path('profile/', views.profile, name='profile')
]