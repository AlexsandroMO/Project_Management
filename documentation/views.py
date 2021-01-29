
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
#from apps.funcionarios.models import 



def hello(request):
    return HttpResponse('<h1>Hello!</h1>')


@login_required
def home(request):
    return render(request,'documentation/index.html')