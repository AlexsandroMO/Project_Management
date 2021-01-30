from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import MyProjectForm, SubjectForm, PageTForm, DocTForm, PageformatForm, DocumentStandardForm, EmployeeForm, StatusDocForm, ActionForm, CotationForm
from django.contrib import messages
from .models import MyProject, PageT, DocT, DocumentStandard, Subject, Action, StatusDoc, Employee, Cotation, Upload, ProjectValue, LdProj

from django.utils.formats import localize
from django.db.models import Q

import codes as CODE
import trata_cota as LDcreate
#import delete_itens
from datetime import datetime
from decimal import Decimal
import sqlite3
import pandas as pd
import numpy as np

def hello(request):
    return HttpResponse('<h1>Hello!</h1>')


def dataTable(request):

    MyProjects = MyProject.objects.all().order_by('project_name')
    DocumentStandards = DocumentStandard.objects.all().order_by('doc_type') 
    Actions = Action.objects.all().order_by('-action_type')
    StatusDocs = StatusDoc.objects.all().order_by('-doc_status')
    Employees = Employee.objects.all().order_by('-emp_name')
    Cotations = Cotation.objects.all().order_by('-proj_name')

    return render(request, 'documentation/datatable.html', {'MyProjects': MyProjects, 'DocumentStandards': DocumentStandards, 'Actions': Actions, 'StatusDocs':StatusDocs, 'Employees':Employees, 'Cotations':Cotations})


@login_required
def index(request):

    MyProjects = MyProject.objects.all().order_by('project_name')
    DocumentStandards = DocumentStandard.objects.all().order_by('doc_type') 
    Actions = Action.objects.all().order_by('-action_type')
    StatusDocs = StatusDoc.objects.all().order_by('-doc_status')
    Employees = Employee.objects.all().order_by('-emp_name')
    #Cotations = Cotation.objects.all().order_by('-proj_name')
    colab = request.user
    colaborador = ''
    photo_colab = ''

    for a in Employees:
        if colab == a.user:
            colaborador = a.emp_name
            photo_colab = a.photo

    return render(request, 'documentation/index.html', {'MyProjects': MyProjects, 'DocumentStandards': DocumentStandards, 'Actions': Actions, 'StatusDocs':StatusDocs, 'Employees':Employees, 'colaborador':colaborador, 'photo_colab':photo_colab})


@login_required
def index2(request, id):

    print('>>>>>>>>>', id)

    Values = ProjectValue.objects.all()
    Cotations = Cotation.objects.filter(proj_name__id=id)#.order_by('-subject_name')
    MyProjects = MyProject.objects.filter(id=id)
    #MyProjects = MyProject.objects.all().order_by('project_name')
    DocumentStandards = DocumentStandard.objects.all().order_by('doc_type') 
    Actions = Action.objects.all().order_by('-action_type')
    StatusDocs = StatusDoc.objects.all().order_by('-doc_status')
    Employees = Employee.objects.all().order_by('-emp_name')
    Cotations = Cotation.objects.all().order_by('-proj_name')

    colab = request.user
    colaborador = ''
    photo_colab = ''

    for a in Employees:
        if colab == a.user:
            colaborador = a.emp_name
            photo_colab = a.photo

    return render(request, 'documentation/index2.html', {'MyProjects': MyProjects, 'DocumentStandards': DocumentStandards, 'Actions': Actions, 'StatusDocs':StatusDocs, 'Employees':Employees, 'Cotations':Cotations, 'colaborador':colaborador, 'photo_colab':photo_colab})


def projectlist(request):

    MyProjects = MyProject.objects.all().order_by('project_name')

    # paginator = Paginator(MyProj, 10)
    # page = request.GET.get('page')

    # MyProjects = paginator.get_page(page)

    return render(request, 'documentation/projetos.html', {'MyProjects': MyProjects})



def Pagetypelist(request):
    
    pagets = PageT.objects.all()

    return render(request, 'documentation/pages-type.html', {'pagets': pagets})



def Doctypelist(request):
    
    docts = DocT.objects.all()
    #paginator = Paginator(doc, 10)
    #page = request.GET.get('page')

    #docts = paginator.get_page(page)

    return render(request, 'documentation/doc-type.html', {'docts': docts})



@login_required
def docummentypelist(request, id):
    
    #Document = DocumentStandard.objects.all().order_by('doc_type').filter(user=request.user)
    Document = DocumentStandard.objects.all().order_by('doc_type')
    #MyProjects = MyProject.objects.all().order_by('project_name')
    MyProjects = MyProject.objects.filter(id=id)
    Subjects = Subject.objects.all().order_by('subject_name')
    Employees = Employee.objects.all().order_by('-emp_name')

    len_doc = len(Document)

    #paginator = Paginator(Document, 20)
    #page = request.GET.get('page')
    #DocumentStandards = paginator.get_page(page)

    colab = request.user

    colaborador = ''
    photo_colab = ''

    for a in Employees:
        if colab == a.user:
            colaborador = a.emp_name
            photo_colab = a.photo

    return render(request, 'documentation/tipos-documentos.html', {'Document': Document, 'MyProjects': MyProjects, 'Subjects': Subjects, 'Employees':Employees, 'len_doc':len_doc, 'colaborador':colaborador, 'photo_colab':photo_colab})



def Subjectlist(request):
    
    Sub = Subject.objects.all().order_by('-subject_name')
    paginator = Paginator(Sub, 10)
    page = request.GET.get('page')

    Subjects = paginator.get_page(page)

    return render(request, 'documentation/disciplinas.html', {'Subjects': Subjects})



def Actionlist(request):
    
    Actions = Action.objects.all().order_by('-action_type') 

    return render(request, 'documentation/action.html', {'Actions': Actions})



def Statuslist(request):
    
    Status = StatusDoc.objects.all().order_by('-doc_status')

    paginator = Paginator(Status, 10)
    page = request.GET.get('page')

    StatusDocs = paginator.get_page(page)

    return render(request, 'documentation/status-doc.html', {'StatusDocs': StatusDocs})



def Employeelist(request):
    
    Empl = Employee.objects.all().order_by('-emp_name')

    paginator = Paginator(Empl, 10)
    page = request.GET.get('page')

    Employees = paginator.get_page(page)

    cols = ['NOME DO COLABORADOR', 'CARGO', 'REGISTRO']

    return render(request, 'documentation/employee.html', {'Employees': Employees, 'cols':cols})



def Uploadlists(request):
    if request.GET.get('arq'):
        print('entrou')

    Uploads = Upload.objects.all().order_by('-arq')

    return render(request, 'documentation/upload.html', {'Uploads':Uploads})





#---------------------------------------------------------------
def Cotationlist(request, id):

    print('>>>>: ', id)

    Cotations = Cotation.objects.filter(proj_name__id=id)#.order_by('-subject_name')
    MyProjects = MyProject.objects.filter(id=id)

    #MyProjects = MyProject.objects.all().order_by('project_name')
    Subjects = Subject.objects.all().order_by('subject_name')
    DocumentStandards = DocumentStandard.objects.all()
    Employees = Employee.objects.all().order_by('-emp_name')

    #----------------------
    calc = []
    for i in Cotations:
        calc.append(i.cost_doc)

    total = localize(sum(calc))
    total = str(total)
    total = total.split()

    total = CODE.financial(total)

    #----------------------
    colab = request.user

    colaborador = ''
    photo_colab = ''

    for a in Employees:
        if colab == a.user:
            colaborador = a.emp_name
            photo_colab = a.photo
            
    #----------------------

    return render(request, 'documentation/cotation.html', {'Cotations':Cotations, 'DocumentStandards':DocumentStandards, 'MyProjects':MyProjects, 'Subjects':Subjects, 'total':total, 'colaborador':colaborador, 'photo_colab':photo_colab})



#@login_required
def Cotationlist_filter(request):

    MyProjects = MyProject.objects.all().order_by('project_name')
    Subjects = Subject.objects.all().order_by('subject_name')
    Cotations = Cotation.objects.all().order_by('subject_name').order_by('doc_name').order_by('proj_name')
    DocumentStandards = DocumentStandard.objects.all()
    Employees = Employee.objects.all().order_by('-emp_name')

    GET = dict(request.GET)

    print('>>>>>',GET)

    if dict(request.GET)['sub'][0] != '0':
        sub = int(GET['sub'][0])
        Cotations = Cotations.filter(subject_name__id=sub)

        #----------------------
        calc = []
        for i in Cotations:
            calc.append(i.cost_doc)

        total = localize(sum(calc))
        total = str(total)
        total = total.split()

        total = CODE.financial(total)

        #----------------------
        colab = request.user

        colaborador = ''
        photo_colab = ''

        for a in Employees:
            if colab == a.user:
                colaborador = a.emp_name
                photo_colab = a.photo
                
        #----------------------
    else:
        return redirect('edite-cota')

    return render(request, 'documentation/cotation-filter.html', {'Cotations':Cotations, 'DocumentStandards':DocumentStandards, 'MyProjects':MyProjects, 'Subjects':Subjects, 'total':total, 'colaborador':colaborador, 'photo_colab':photo_colab})



def EditeCotation(request, id):

    Values = ProjectValue.objects.all()
    Cotations = get_object_or_404(Cotation, pk=id)
    form = CotationForm(instance=Cotations)

    print(Values[0].cost_by_hh, Values[0].cost_by_doc, Values[0].cost_by_A1)
    print(form)
  

    if (request.method == 'POST'):
        form = CotationForm(request.POST, instance=Cotations)
        
        if (form.is_valid()):
            Cotations.cost_doc = 0
            Cotations.save()
            return redirect('edite-cota')
            
        else:
            return render(request, 'documentation/edite-cotation.html', {'form': form, 'Cotations': Cotations}) 

    else:
        return render(request, 'documentation/edite-cotation.html', {'form': form, 'Cotations': Cotations})


def DeleteCotation(request, id):
    Cotations = get_object_or_404(Cotation, pk=id)
    Cotations.delete()

    #messages.info(request, 'Documento Deletado com Sucesso!')

    return redirect('/')

#---------------------------------------------------------------
def LD_Proj(request):

    Cotations = Cotation.objects.all().order_by('subject_name').order_by('doc_name').order_by('proj_name')
    MyProjects = MyProject.objects.all().order_by('project_name')
    Subjects = Subject.objects.all().order_by('subject_name')
    DocumentStandards = DocumentStandard.objects.all()
    Employees = Employee.objects.all().order_by('-emp_name')
    #LD_Proj = LdProj.objects.all().order_by('-doc_name')

    #----------------------
    calc = []
    for i in Cotations:
        print(i.cost_doc)
        calc.append(i.cost_doc)

    total = localize(sum(calc))
    total = str(total)
    total = total.split()

    total = CODE.financial(total)

    #----------------------
    colab = request.user
    colaborador = ''
    photo_colab = ''

    for a in Employees:
        if colab == a.user:
            colaborador = a.emp_name
            photo_colab = a.photo

    #----------------------

    return render(request, 'documentation/LD-projeto.html', {'Cotations':Cotations, 'DocumentStandards':DocumentStandards, 'MyProjects':MyProjects, 'Subjects':Subjects, 'total':total, 'colaborador':colaborador, 'photo_colab':photo_colab})




def Create_Cotation(request):

    DocumentStandards = DocumentStandard.objects.all()

    if len(dict(request.GET)) == 3 and dict(request.GET)['proj'][0] != '0' and dict(request.GET)['sub'][0] != '0':
        
        GET = dict(request.GET)

        if dict(request.GET)['action'][0] == 'All':
            LDcreate.cria_orc_all(GET,DocumentStandards)

            return redirect('/')

        elif dict(request.GET)['action'][0] != 'All':
            print('>>>>>>>>>>>>>>>>>>>', dict(request.GET))
            LDcreate.cria_orc_ind(GET)

            return redirect('/')


    else:
        return redirect('/')



def Create_LD(request):

    DocumentStandards = DocumentStandard.objects.all()

    GET = dict(request.GET)
    print('>>>>>>>>>>>>>>>>>>>',GET)

    #if len(dict(request.GET)) == 3 and dict(request.GET)['proj'][0] != '0' and dict(request.GET)['sub'][0] != '0':
        
        

    # if dict(request.GET)['action'][0] == 'All':
    #         #LDcreate.cria_orc_all(GET,DocumentStandards)
    #         pass

    #         return redirect('ld-projeto')

    #     elif dict(request.GET)['action'][0] != 'All':
            
    #         #LDcreate.cria_orc_ind(GET)

    #         return redirect('ld-projeto')


    # else:
    
    return redirect('/')




'''def Create_Cotation(request):
    cost = ProjectValue.objects.all()
    cost_proj = []
    if cost:
        for a in cost:
            cost_proj.append([a.cost_by_hh,a.cost_by_doc,a.cost_by_A1])
    if request.GET.get('cota-radio'):
        cost_type = request.GET.get('cota-radio')
        if cost_type == 'option1':
            val = cost_proj[0][0]
        elif cost_type == 'option2':
            val = cost_proj[0][1]
        elif cost_type == 'option3':
            val = cost_proj[0][2]
    LDcreate.trata_cotation(str(val), cost_type)
    return redirect('')'''



def Calc_Cota(request):

    MyProjects = MyProject.objects.all().order_by('project_name')
    DocumentStandards = DocumentStandard.objects.all().order_by('doc_type') 
    Actions = Action.objects.all().order_by('-action_type')
    StatusDocs = StatusDoc.objects.all().order_by('-doc_status')
    Employees = Employee.objects.all().order_by('-emp_name')
    #Cotations = Cotation.objects.all().order_by('-proj_name')
    colab = request.user
    colaborador = ''
    photo_colab = ''

    for a in Employees:
        if colab == a.user:
            colaborador = a.emp_name
            photo_colab = a.photo

    GET = dict(request.GET)

    Values = ProjectValue.objects.all()
    Cotations = Cotation.objects.all()
   
    LDcreate.calc_cota(Cotations, Values, GET)

    return render(request, 'documentation/index.html', {'MyProjects': MyProjects, 'DocumentStandards': DocumentStandards, 'Actions': Actions, 'StatusDocs':StatusDocs, 'Employees':Employees, 'colaborador':colaborador, 'photo_colab':photo_colab})



















def Create_PL(request): #Uso admin /CreatePL

    MyProjects = MyProject.objects.all()
    PageTs = PageT.objects.all()
    DocTs = DocT.objects.all()
    DocumentStandards = DocumentStandard.objects.all()
    Subjects = Subject.objects.all()
    Actions = Action.objects.all().order_by
    StatusDocs = StatusDoc.objects.all().order_by
    Employees = Employee.objects.all().order_by

    form_proj = MyProjectForm()
    form_dis = SubjectForm()
    form_paget = PageTForm()
    form_doct = DocTForm()
    form_format = PageformatForm()
    form_doc = DocumentStandardForm()
    form_func = EmployeeForm()
    form_st = StatusDocForm()
    form_ac = ActionForm()

    execute = CODE.cria_tabelas(MyProjects,PageTs,DocTs,DocumentStandards,Subjects,Actions,StatusDocs,Employees,form_proj,form_dis,form_paget,form_doct,form_format,form_doc,form_func,form_st,form_ac)
    #print(execute)

    return redirect('/')




