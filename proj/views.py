from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib import messages
from .models import MyProject, Subject, DocumentBase, DocumentListProject #, PageT, DocT, DocumentStandard, Subject, Action, StatusDoc, Employee, Cotation, Upload, ProjectValue, LdProj
#from .forms import MyProjectForm, SubjectForm, PageTForm, DocTForm, PageformatForm, DocumentStandardForm, EmployeeForm, StatusDocForm, ActionForm, CotationForm, LdProjForm
from datetime import datetime

import code

def index(request):

  return render(request, 'proj/index.html') #, {'MyProjects': MyProjects,'proj':proj, 'Employees':Employees, 'colaborador':colaborador, 'photo_colab':photo_colab})


@login_required
def OnProjects(request):

  MyProjects = MyProject.objects.all().order_by('-project_name')

  return render(request, 'proj/on-projects.html',{'MyProjects':MyProjects}) #, {'MyProjects': MyProjects,'proj':proj, 'Employees':Employees, 'colaborador':colaborador, 'photo_colab':photo_colab})


@login_required
def DocumentList(request):

  GET = dict(request.GET)
  if str(GET) == '{}':
    return redirect('/')

  else:
    POST = dict(request.POST)
    #print('>>>>>>>>>>>', type(POST['sub_id']))
    #sub = POST['sub_id']
    #print('>>>>>>>>>>>', POST['check_id'])
    #check_id = POST['check_id']
    #print('>>>>>>>>>>>', POST)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   mais um if nesse POST

    new_id = str(GET).replace("{'","").replace("': ['']}","")
    proj_id = int(new_id)
    ListDoc = DocumentListProject.objects.all().order_by('-doc_name_pattern')

    MyProjects = MyProject.objects.all()
    Subjects = Subject.objects.all()
    DocBase = DocumentBase.objects.all()
    

    #code.create_list(sub, Subjects, proj_id, MyProjects, check_id, DocBase)

    return render(request, 'proj/document-list.html',{'ListDoc':ListDoc,'DocBase':DocBase,'MyProjects':MyProjects,'Subjects':Subjects,'proj_id':proj_id}) #, {'MyProjects': MyProjects,'proj':proj, 'Employees':Employees, 'colaborador':colaborador, 'photo_colab':photo_colab})


@login_required
def BaseDoc(request):

  GET = dict(request.GET)
  if str(GET) == '{}':
    return redirect('/')

  else:
    new_id = str(GET).replace("{'","").replace("': ['']}","")
    proj_id = int(new_id)

    Subjects = Subject.objects.all().order_by('-subject_name')
    DocumentBases = DocumentBase.objects.all().order_by('-document_name')

    return render(request, 'proj/document-base.html',{'DocumentBases':DocumentBases, 'Subjects':Subjects, 'proj_id':proj_id}) #, {'MyProjects': MyProjects,'proj':proj, 'Employees':Employees, 'colaborador':colaborador, 'photo_colab':photo_colab})


@login_required
def CotationList(request):

  GET = dict(request.GET)
  if str(GET) == '{}':
    return redirect('/')

  else:
    new_id = str(GET).replace("{'","").replace("': ['']}","")
    proj_id = int(new_id)

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

    return render(request, 'proj/cotation-list.html', {'proj_id':proj_id}) #, {'MyProjects': MyProjects,'proj':proj, 'Employees':Employees, 'colaborador':colaborador, 'photo_colab':photo_colab})
