from django.contrib import admin
from . models import MyProject, Subject, DocT, DocumentBase, DocumentListProject, PageSheet, Pageformat, Action, StatusDoc, Employee, Cotation, Pageformat


class MyProjectAdmin(admin.ModelAdmin):
    fields = ('project_name','company','pref_proj','cod_proj','comments')
    list_display = ('id','project_name','pref_proj','cod_proj','company','comments','created_at','update_at')
    
class SubjectAdmin(admin.ModelAdmin):
    fields = ('subject_name','subject_cod',)
    list_display = ('id','subject_name','subject_cod','created_at','update_at')

class DocTAdmin(admin.ModelAdmin):
    fields = ('name_doc',)
    list_display = ('id','name_doc', 'created_at','update_at')

class DocumentBaseAdmin(admin.ModelAdmin):
    fields = ('document_name',)
    list_display = ('document_name','created_at','update_at')

class DocumentListProjectAdmin(admin.ModelAdmin):
    fields = ('proj_name', 'subject_name', 'doc_name_pattern','tipe_doc','name_doc','page_type','page_format')
    list_display = ('id','proj_name', 'subject_name', 'doc_name_pattern','tipe_doc','name_doc','page_type','page_format','created_at','update_at') 

class PageSheetAdmin(admin.ModelAdmin):
    fields = ('name_sheet',)
    list_display = ('id','name_sheet','created_at','update_at')

class PageformatAdmin(admin.ModelAdmin):
    fields = ('name_format',)
    list_display = ('id','name_format','created_at','update_at')
    
class StatusDocAdmin(admin.ModelAdmin):
    fields = ('doc_status',)
    list_display = ('id','doc_status','created_at','update_at')

class ActionAdmin(admin.ModelAdmin):
    fields = ('action_type',)
    list_display = ('id','action_type','created_at','update_at')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('emp_name', 'emp_position', 'emp_contract','photo', 'user')
    list_display = ('id','emp_name', 'emp_position', 'emp_contract','photo', 'user','created_at','update_at') 


class CotationAdmin(admin.ModelAdmin):
    fields = ('proj_name', 'subject_name', 'doc_name_pattern','page_type','qt_page','qt_doc', 'qt_hh','cost_doc')
    list_display = ('id','proj_name', 'subject_name', 'doc_name_pattern','page_type','qt_page','qt_doc', 'qt_hh','cost_doc', 'created_at','update_at') 






""" class UploadAdmin(admin.ModelAdmin):
    fields = ('arq',)
    list_display = ('arq', 'update_arq')
 """


admin.site.register(MyProject, MyProjectAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(DocT, DocTAdmin)
admin.site.register(DocumentBase, DocumentBaseAdmin)
admin.site.register(DocumentListProject, DocumentListProjectAdmin)
admin.site.register(PageSheet, PageSheetAdmin)
admin.site.register(Pageformat, PageformatAdmin)
admin.site.register(Action)
admin.site.register(StatusDoc)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Cotation, CotationAdmin)
#admin.site.register(Upload)