from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib import messages
#from .models import MyProject, PageT, DocT, DocumentStandard, Subject, Action, StatusDoc, Employee, Cotation, Upload, ProjectValue, LdProj
#from .forms import MyProjectForm, SubjectForm, PageTForm, DocTForm, PageformatForm, DocumentStandardForm, EmployeeForm, StatusDocForm, ActionForm, CotationForm, LdProjForm
from datetime import datetime


@login_required
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
