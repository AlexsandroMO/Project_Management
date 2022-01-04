
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index-2'),
    #path('edite_LD/<int:id>', views.EditeLD, name='edite-ld'),
    
    
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
