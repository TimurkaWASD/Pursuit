from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('users/', include('user.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('', include('targets.urls'))
]



"""
    login/ [name='login']
    logout/ [name='logout']
    password_change/ [name='password_change']
    password_change/done/ [name='password_change_done']
    password_reset/ [name='password_reset']
    password_reset/done/ [name='password_reset_done']
    reset/<uidb64>/<token>/ [name='password_reset_confirm']
    reset/done/ [name='password_reset_complete']
"""