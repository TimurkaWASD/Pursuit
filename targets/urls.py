from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('create_targets/', views.create_target, name='create_target'),
    path('targets_list/', views.targets_list, name='targets_list'),
    path('change_status/<int:target_id>/', views.change_status, name='change_status'),
    path('change_favorite/<int:target_id>/', views.change_favorite, name='change_favorite'),
    path('change_rating/<int:target_id>/', views.change_rating, name='change_rating'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)