
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('hello/', views.hello),
    path('', views.index, name='index'),
    #path('index2/<int:id>', views.index2, name='index-2'),
    path('index2/', views.index2, name='index-2'),
    path('datatable/', views.dataTable, name='data-table'),
    path('projects/', views.projectlist, name='project-list'),
    #path('typeDocuments/', views.docummentypelist, name='documment-type-list'),
    path('typeDocuments/', views.docummentypelist, name='documment-type-list'),
    # path('Subject/', views.Subjectlist, name='subject-list'),
    # path('action/', views.Actionlist, name='action-list'),
    # path('status/', views.Statuslist, name='status-list'),
    # path('employee/', views.Employeelist, name='employee-list'),
    #path('cotation/<int:id>', views.Cotationlist, name='cotation-list'),
    path('cotation/', views.Cotationlist, name='cotation-list'),
    path('cotationFilter/', views.Cotationlist_filter, name='cotation-list-filter'),
    path('visualiza_df/', views.VisualizaDF, name='visualiza-df'),
    path('edite_cotation/', views.EditeCotation, name='edite-cota'),
    #path('edite_cotation_all/', views.EditeCotationAll, name='edite-cota-all'),
    path('edite_LD/<int:id>', views.EditeLD, name='edite-ld'),
    path('LD_Proj/', views.LD_Proj, name='ld-projeto'),
    path('CreatePL/', views.Create_PL, name='Create-PL'),
    path('CreateCota/', views.Create_Cotation, name='Create-cota'),
    #path('PageT/', views.Pagetypelist, name='page-t'),
    #path('DocT/', views.Doctypelist, name='doc-t'),
    path('createLD/', views.Create_LD, name='create-LD'),
    path('CalcCota/', views.Calc_Cota, name='calc-cota'),
    path('upload/', views.Uploadlists, name='upload-list'),
    path('upload_Table/', views.UploadTable, name='upload-table'),
    path('download_df/', views.download_df, name='download-df'),
    path('ajustes_table/', views.ajustestable, name='ajustes-table'),
    
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#pip3 install django-crispy-forms

