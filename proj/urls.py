
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('index2/', views.index, name='index-2'),
    path('On_Projects/', views.OnProjects, name='on-prjects'),
    path('Document_List/', views.DocumentList, name='document-list'),
    path('Base_Doc/', views.BaseDoc, name='base-doc'),
    path('Cotation_List/', views.CotationList, name='cotation-list'),
    #path('edite_LD/<int:id>', views.EditeLD, name='edite-ld'),
    
    
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
