from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import MyProject, PageT, DocT, DocumentStandard, Subject, Action, StatusDoc, Employee, Cotation, Upload, ProjectValue, LdProj
from .forms import MyProjectForm, SubjectForm, PageTForm, DocTForm, PageformatForm, DocumentStandardForm, EmployeeForm, StatusDocForm, ActionForm, CotationForm, LdProjForm
from django.contrib import messages

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
    proj = 0

    return render(request, 'documentation/datatable.html', {'MyProjects': MyProjects, 'proj':proj})



def index(request):

    MyProjects = MyProject.objects.all().order_by('-project_name')
    Employees = Employee.objects.all()

    proj = 0

    colab = request.user
    colaborador = ''
    photo_colab = ''

    for a in Employees:
        if colab == a.user:
            colaborador = a.emp_name
            photo_colab = a.photo

    return render(request, 'documentation/index.html', {'MyProjects': MyProjects,'proj':proj, 'Employees':Employees, 'colaborador':colaborador, 'photo_colab':photo_colab})


@login_required
def index2(request):

    GET = dict(request.GET)

    DocumentStandards = DocumentStandard.objects.all()
    Actions = Action.objects.all()
    StatusDocs = StatusDoc.objects.all()
    Employees = Employee.objects.all()
    #Cotations = Cotation.objects.all()
    Subjects = Subject.objects.all().order_by('subject_name')

    if dict(request.GET)['proj'][0] != '0':

        proj = int(GET['proj'][0])

        MyProjects = MyProject.objects.filter(id=proj)

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
        return redirect('/')

    return render(request, 'documentation/index2.html', {'MyProjects': MyProjects, 'DocumentStandards': DocumentStandards, 'Subjects':Subjects,'Actions': Actions, 'StatusDocs':StatusDocs, 'Employees':Employees, 'colaborador':colaborador, 'photo_colab':photo_colab, 'proj':proj})

@login_required
def projectlist(request):

    MyProjects = MyProject.objects.all().order_by('project_name')

    # paginator = Paginator(MyProj, 10)
    # page = request.GET.get('page')

    # MyProjects = paginator.get_page(page)

    GET = dict(request.GET)
    proj = int(GET['proj'][0])

    Employees = Employee.objects.all().order_by('-emp_name')
    #----------------------
    colab = request.user

    colaborador = ''
    photo_colab = ''

    for a in Employees:
        if colab == a.user:
            colaborador = a.emp_name
            photo_colab = a.photo
    #----------------------

    return render(request, 'documentation/projetos.html', {'MyProjects': MyProjects, 'colaborador':colaborador, 'photo_colab':photo_colab, 'proj':proj})



@login_required
def docummentypelist(request):

    GET = dict(request.GET)
    proj = int(GET['proj'][0])
    
    Document = DocumentStandard.objects.all().order_by('doc_type')
    MyProjects = MyProject.objects.filter(id=proj)
    Subjects = Subject.objects.all().order_by('subject_name')
    Employees = Employee.objects.all().order_by('-emp_name')

    len_doc = len(Document)

    #proj = 0

    colab = request.user

    colaborador = ''
    photo_colab = ''

    for a in Employees:
        if colab == a.user:
            colaborador = a.emp_name
            photo_colab = a.photo

    return render(request, 'documentation/tipos-documentos.html', {'Document': Document, 'MyProjects': MyProjects, 'Subjects': Subjects, 'Employees':Employees, 'len_doc':len_doc, 'colaborador':colaborador, 'photo_colab':photo_colab, 'proj':proj})



def Uploadlists(request):
    # if request.GET.get('arq'):
    #     print('entrou')

    Uploads = Upload.objects.all().order_by('-arq')

    return render(request, 'documentation/upload.html', {'Uploads':Uploads})


@login_required
def Cotationlist(request):

    Cotations = Cotation.objects.all().order_by('subject_name').order_by('doc_name').order_by('proj_name')
    DocumentStandards = DocumentStandard.objects.all()
    Employees = Employee.objects.all().order_by('-emp_name')

    GET = dict(request.GET)

    if dict(request.GET)['proj'] != '0':
        proj = int(GET['proj'])
        print('--------\n\n\n\n')

        Subjects = Subject.objects.all()
        Cotations = Cotations.filter(proj_name__id=proj)

        #-----------------------
        sub_filter = []
        for i in Cotations:
            sub_filter.append(str(i.subject_name))
        
        sub_filted = sorted(set(sub_filter))

        sub = []
        for i in Subjects:
            for j in sub_filted:
                if i.subject_name == j:
                    sub.append([j, i.id])

        #-----------------------
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

    return render(request, 'documentation/cotation.html', {'Cotations':Cotations, 'DocumentStandards':DocumentStandards, 'Subjects':Subjects, 'total':total, 'colaborador':colaborador, 'photo_colab':photo_colab,'proj':proj, 'sub':sub})


#?sub=1&proj=1

@login_required
def Cotationlist_filter(request):

    GET = dict(request.GET)
    print('-----------', GET)
    print('--------\n\n\n\n')

    MyProjects = MyProject.objects.all().order_by('project_name')
    
    Cotations = Cotation.objects.all()
    DocumentStandards = DocumentStandard.objects.all()
    Employees = Employee.objects.all().order_by('-emp_name')

    sub = int(GET['sub'][0])
    proj = int(GET['proj'][0])
    Subjects = Subject.objects.all().order_by('subject_name')
    Cotations = Cotations.filter(proj_name__id=proj)
    Cotations = Cotations.filter(subject_name__id=sub)
    Subjects = Subjects.filter(id=sub)

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

    return render(request, 'documentation/cotation-filter.html', {'Cotations':Cotations, 'DocumentStandards':DocumentStandards,
                                                                'MyProjects':MyProjects,'Subjects':Subjects, 'total':total,
                                                                'colaborador':colaborador, 'photo_colab':photo_colab,'sub':sub, 'proj':proj})

@login_required
def EditeCotation(request, id):

    GET = dict(request.GET)
    print('\n\n')
    print('>>>>>>>>>>',GET)
    print('\n\n') 

    Employees = Employee.objects.all()
    #----------------------
    colab = request.user

    colaborador = ''
    photo_colab = ''

    for a in Employees:
        if colab == a.user:
            colaborador = a.emp_name
            photo_colab = a.photo
                
    #----------------------

    Cotations = get_object_or_404(Cotation, pk=id)
    form = CotationForm(instance=Cotations)

    if (request.method == 'POST'):
        form = CotationForm(request.POST, instance=Cotations)
        
        if (form.is_valid()):
            Cotations.cost_doc = 0
            Cotations.save()
            return redirect('http://127.0.0.1:8000/cotationFilter/?sub=2&proj=1')
            
        else:
            return render(request, 'documentation/edite-cotation.html', {'form': form, 'Cotations': Cotations, 'colaborador':colaborador, 'photo_colab':photo_colab}) 

    else:
        return render(request, 'documentation/edite-cotation.html', {'form': form, 'Cotations': Cotations, 'colaborador':colaborador, 'photo_colab':photo_colab})



@login_required
def EditeCotationAll(request):
    GET = dict(request.GET)

    print('\n\n')
    print('>>>>>>>>>>',GET)
    print('\n\n') 

    #sub = GET['action-1']
    #proj = GET['xx-2']

    #if GET['id-form'][0] == '0':
        #pass
        #trata_edit_cota_all(GET, sub, proj)

    #else:
        #pass
        #return redirect('edite-cota' + '/' + id)
        

    # Cotations = Cotation.objects.all()
    # Employees = Employee.objects.all()
    # #----------------------
    # colab = request.user

    # colaborador = ''
    # photo_colab = ''

    # for a in Employees:
    #     if colab == a.user:
    #         colaborador = a.emp_name
    #         photo_colab = a.photo
                
    # #----------------------

    #Cotations = get_object_or_404(Cotation, pk=id)
    #form = CotationForm(instance=Cotations)

    if (request.method == 'POST'):
        #form = CotationForm(request.POST, instance=Cotations)
        
        #if (form.is_valid()):
            #Cotations.cost_doc = 0
            #Cotations.save()
            #return redirect('http://127.0.0.1:8000/cotationFilter/?sub=2&proj=1') 'form': form, 
            
        #else:
        return render(request, 'documentation/edite-cotation-all.html') 
        #return render(request, 'documentation/edite-cotation-all.html', {'Cotations': Cotations, 'colaborador':colaborador, 'photo_colab':photo_colab}) 

    else:
        return render(request, 'documentation/edite-cotation-all.html')


def trata_edit_cota_all(GET, proj, sub):
    print('------------->        entrou!!!')

    Cotations = Cotation.objects.all()
    Cotations = Cotations.filter(proj_name__id=proj)
    Cotations = Cotations.filter(subject_name__id=sub)

    Cotations = get_object_or_404(Cotation, pk=id)
    form = CotationForm(instance=Cotations)
    
    form = CotationForm()
        
    #return render(request, 'documentation/edite-cotation.html', {'form': form, 'Cotations': Cotations, 'colaborador':colaborador, 'photo_colab':photo_colab}) 







def DeleteCotation(request, id):
    Cotations = get_object_or_404(Cotation, pk=id)
    Cotations.delete()

    #messages.info(request, 'Documento Deletado com Sucesso!')

    return redirect('/')

#---------------------------------------------------------------
@login_required
def LD_Proj(request):

    LdProjs = LdProj.objects.all().order_by('subject_name')

    GET = dict(request.GET)

    if dict(request.GET)['proj'][0] != '0':
        proj = int(GET['proj'][0])
        LdProjs = LdProjs.filter(proj_name__id=2)

    Employees = Employee.objects.all().order_by('-emp_name')
    #----------------------
    colab = request.user

    colaborador = ''
    photo_colab = ''

    for a in Employees:
        if colab == a.user:
            colaborador = a.emp_name
            photo_colab = a.photo
    #----------------------

    return render(request, 'documentation/LD-projeto.html', {'LdProjs':LdProjs, 'colaborador':colaborador, 'photo_colab':photo_colab, 'proj':proj})


@login_required
def EditeLD(request, id):

    Employees = Employee.objects.all().order_by('-emp_name')
    #----------------------
    colab = request.user

    colaborador = ''
    photo_colab = ''

    for a in Employees:
        if colab == a.user:
            colaborador = a.emp_name
            photo_colab = a.photo
    #----------------------

    LdProjs = LdProj.objects.all()
    LD = get_object_or_404(LdProj, pk=id)
    form = LdProjForm(instance=LD)

    if (request.method == 'POST'):
        form = LdProjForm(request.POST, instance=LD)
        
        if (form.is_valid()):
            #LdProjs.cost_doc = 0
            LD.save()
            return redirect('/')
            
        else:
            return render(request, 'documentation/edite-LD.html', {'form': form, 'LdProjs': LdProjs,'LD':LD, 'colaborador':colaborador, 'photo_colab':photo_colab}) 

    else:
        return render(request, 'documentation/edite-LD.html', {'form': form, 'LdProjs': LdProjs, 'colaborador':colaborador, 'photo_colab':photo_colab})



def Create_Cotation(request):

    DocumentStandards = DocumentStandard.objects.all()

    if len(dict(request.GET)) == 3 and dict(request.GET)['proj'][0] != '0' and dict(request.GET)['sub'][0] != '0':
        
        GET = dict(request.GET)

        if dict(request.GET)['action'][0] == 'All':
            LDcreate.cria_orc_all(GET,DocumentStandards)

            return redirect('/')

        elif dict(request.GET)['action'][0] != 'All':
            LDcreate.cria_orc_ind(GET)

            return redirect('/')


    else:
        return redirect('/')



def Create_LD(request):

    Cotations = Cotation.objects.all()

    GET = dict(request.GET)

    if len(dict(request.GET)) != 0:
        ids = dict(request.GET)['action'][0].split('|')

        proj = int(ids[1])
        sub = int(ids[0])

        Cotations = Cotations.filter(proj_name__id=proj)
        Cotations = Cotations.filter(subject_name__id=sub)

        LDcreate.cria_ld_call(Cotations)

    
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
    #------------------     
    colab = request.user
    colaborador = ''
    photo_colab = ''

    for a in Employees:
        if colab == a.user:
            colaborador = a.emp_name
            photo_colab = a.photo
   #------------------

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

    return redirect('/')




