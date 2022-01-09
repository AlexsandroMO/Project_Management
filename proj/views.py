from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib import messages
from .models import MyProject, Subject, DocumentBase, DocumentListProject #, PageT, DocT, DocumentStandard, Subject, Action, StatusDoc, Employee, Cotation, Upload, ProjectValue, LdProj
#from .forms import MyProjectForm, SubjectForm, PageTForm, DocTForm, PageformatForm, DocumentStandardForm, EmployeeForm, StatusDocForm, ActionForm, CotationForm, LdProjForm
from datetime import datetime


def index(request):

  ''' MyProjects = MyProject.objects.all().order_by('-project_name')
  Employees = Employee.objects.all()

  proj = 0

  colab = request.user
  colaborador = ''
  photo_colab = ''

  for a in Employees:
    if colab == a.user:
      colaborador = a.emp_name
      photo_colab = a.photo'''

  return render(request, 'proj/index.html') #, {'MyProjects': MyProjects,'proj':proj, 'Employees':Employees, 'colaborador':colaborador, 'photo_colab':photo_colab})

@login_required
def index2(request):

  return render(request, 'proj/index2.html') #, {'MyProjects': MyProjects,'proj':proj, 'Employees':Employees, 'colaborador':colaborador, 'photo_colab':photo_colab})

@login_required
def OnProjects(request):

  MyProjects = MyProject.objects.all().order_by('-project_name')
  return render(request, 'proj/on-projects.html',{'MyProjects':MyProjects}) #, {'MyProjects': MyProjects,'proj':proj, 'Employees':Employees, 'colaborador':colaborador, 'photo_colab':photo_colab})


@login_required
def BaseDoc(request):

  Subjects = Subject.objects.all().order_by('-subject_name')
  DocumentBases = DocumentBase.objects.all().order_by('-document_name')
  return render(request, 'proj/document-base.html',{'DocumentBases':DocumentBases, 'Subjects':Subjects}) #, {'MyProjects': MyProjects,'proj':proj, 'Employees':Employees, 'colaborador':colaborador, 'photo_colab':photo_colab})


@login_required
def DocumentList(request):
  POST = dict(request.POST)
  POST2 = dict(request.GET)

  print('>>>>', POST)
  print('>>ID >>', POST2)

  ListDoc = DocumentListProject.objects.all().order_by('-doc_name_pattern')

  return render(request, 'proj/document-list.html',{'ListDoc':ListDoc}) #, {'MyProjects': MyProjects,'proj':proj, 'Employees':Employees, 'colaborador':colaborador, 'photo_colab':photo_colab})


@login_required
def CotationList(request):

  ''' MyProjects = MyProject.objects.all().order_by('-project_name')
  Employees = Employee.objects.all()

  proj = 0

  colab = request.user
  colaborador = ''
  photo_colab = ''

  for a in Employees:
    if colab == a.user:
      colaborador = a.emp_name
      photo_colab = a.photo'''

  return render(request, 'proj/index2.html') #, {'MyProjects': MyProjects,'proj':proj, 'Employees':Employees, 'colaborador':colaborador, 'photo_colab':photo_colab})
