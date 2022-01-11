from django import forms

from .models import DocumentListProject

class DocumentListProjectForm(forms.ModelForm):

    class Meta:
        model = DocumentListProject
        fields = ('proj_name', 'subject_name', 'doc_name_pattern','type_doc','name_doc','page_type','page_format')