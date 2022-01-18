from django.db import models
from django.contrib.auth import get_user_model

class MyProject(models.Model): #Títulos de projeto

    project_name = models.CharField(max_length=255, verbose_name='NOME DO PROJETO')
    company = models.CharField(max_length=255, verbose_name='NOME DA EMPRESA')
    pref_proj = models.CharField(max_length=30, verbose_name='PREFÍXO DO PROJETO')
    cod_proj = models.CharField(max_length=30, verbose_name='CÓDIGO DO PROJETO')
    comments = models.TextField(verbose_name='COMENTÁRIOS')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name


class Subject(models.Model): #Disciplinas do Projeto

    subject_name = models.CharField(max_length=255, verbose_name='DISCIPLINA')
    subject_cod = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject_name


class DocT(models.Model): #Tipo de Documento

    name_doc = models.CharField(max_length=5, verbose_name='TIPO DE DOCUMENTO')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return self.name_doc

class DocumentBase(models.Model):

    document_name = models.CharField(max_length=255, verbose_name='NOME DOCUMENTO')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.document_name


class PageSheet(models.Model): #Lista de Acões

    name_sheet = models.CharField(max_length=4, verbose_name='TIPO DE FOLHA')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return self.name_sheet

class Pageformat(models.Model): #Lista de Acões

    name_format = models.CharField(max_length=15, verbose_name='TIPO DE ARQUIVO')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name_format


class StatusDoc(models.Model): #Lista de Status do Projeto

    doc_status = models.CharField(max_length=50, verbose_name='STATUS')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return self.doc_status


class Action(models.Model): #Lista de Acões

    action_type = models.CharField(max_length=12, verbose_name='AÇÃO')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return self.action_type


class Employee(models.Model): #Lista de Funcionários

    emp_name = models.CharField(max_length=255, verbose_name='NOME DO COLABORADOR')
    emp_position = models.CharField(max_length=255, verbose_name='FUNÇÃO')
    emp_contract = models.CharField(max_length=20, verbose_name='CONTRATO')
    photo = models.FileField(upload_to='uploads/photos/', blank=True, null=True, verbose_name='FOTO')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='USUÁRIO')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.emp_name


class DocumentListProject(models.Model): #Lista de Acões DocT
    
    proj_name = models.ForeignKey(MyProject, on_delete=models.CASCADE, verbose_name='PROJETO')
    subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='DISCIPLINA')
    doc_name_pattern = models.ForeignKey(DocumentBase, on_delete=models.CASCADE, verbose_name='DOCUMENTO BASE')
    type_doc = models.ForeignKey(DocT, on_delete=models.CASCADE, verbose_name='TIPO DE DOCUMENTO')
    name_doc = models.CharField(max_length=255, blank=True, null=True, verbose_name='NOME DO DOCUMENTO')
    page_type = models.ForeignKey(PageSheet, on_delete=models.CASCADE, verbose_name='TIPO PÁGINA')
    page_format = models.ForeignKey(Pageformat, on_delete=models.CASCADE, verbose_name='FORMATO PÁGINA')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return str(self.doc_name_pattern)


class Cotation(models.Model): #Lista de Acões DocT
    
    proj_name = models.ForeignKey(MyProject, on_delete=models.CASCADE, verbose_name='PROJETO')
    subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='DISCIPLINA')
    doc_name_pattern = models.ForeignKey(DocumentBase, on_delete=models.CASCADE, verbose_name='DOCUMENTO BASE')
    page_type = models.ForeignKey(PageSheet, on_delete=models.CASCADE, verbose_name='TIPO PÁGINA')
    #page_format = models.ForeignKey(Pageformat, on_delete=models.CASCADE, verbose_name='FORMATO PÁGINA')
    qt_page = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True, verbose_name='QT PÁGINA')
    qt_doc = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True, verbose_name='QT DOC')
    qt_hh = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True, verbose_name='QT HH')
    cost_doc = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True, verbose_name='CUSTO DOCUMENTO')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return str(self.doc_name_pattern)





""" class DocumentStandard(models.Model):

    documment_name = models.CharField(max_length=255, verbose_name='NOME DOCUMENTO')
    doc_type = models.ForeignKey(DocT, on_delete=models.CASCADE, verbose_name='CÓDIGO DOC')
    format_doc = models.ForeignKey(Pageformat, on_delete=models.CASCADE, verbose_name='FORMATO DO DOCUMENTO')
    doc_type_page = models.ForeignKey(PageT, on_delete=models.CASCADE, verbose_name='TIPO PÁGINA')
    #user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.documment_name




class LdProj(models.Model): #Lista de Documentos
    
    proj_name = models.ForeignKey(MyProject, on_delete=models.CASCADE, verbose_name='PROJETO')
    subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='DISCIPLINA')
    doc_name_pattern = models.ForeignKey(DocumentStandard, on_delete=models.CASCADE, verbose_name='DOCUMENTO BASE')
    doc_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='NOME DOCUMENTO')
    cod_doc_type = models.ForeignKey(DocT, on_delete=models.CASCADE, verbose_name='CÓDIGO DOC')
    page_type = models.ForeignKey(PageT, on_delete=models.CASCADE, verbose_name='TIPO PÁGINA')
    format_doc = models.ForeignKey(Pageformat, on_delete=models.CASCADE, verbose_name='FORMATO')
    status = models.ForeignKey(StatusDoc, on_delete=models.CASCADE, blank=True, null=True, verbose_name='STATUS')
    responsible = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True, related_name='resp', verbose_name='RESPONSÁVEL')
    elab = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True, related_name='elab', verbose_name='ELABORADOR')
    verif = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True, related_name='verif', verbose_name='VERIFICADOR')
    aprov = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True, related_name='aprov', verbose_name='APROVADOR')
    emiss = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True, related_name='emiss', verbose_name='EMISSOR')
    date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return str(self.proj_name)
 """
