from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView

from app.forms import *
# Create your views here.
#FBV for returning string as REsponse

def fbv_string(request):
    return HttpResponse('<h1>This is returned by FBV</h1>')

#CBV for returning string as REsponse

class Cbv_string(View):
    def get(self,request):
        return HttpResponse('CBV string')

#FBV for returning HTML page as response

def fbv_page(request):
    return render(request,'fbv_page.html')

#CBV for returning HTML page as response

class cbv_page(View):
    def get(self,request):
        return render(request,'cbv_page.html')

# FBV for dealing with django forms

def fbv_form(request):
    form=StudentForm()
    d={'form':form}

    if request.method=='POST':
        form_data=StudentForm(request.POST)
        if form_data.is_valid():
            return HttpResponse(str(form_data.cleaned_data))
    return render(request,'fbv_form.html',d)

# CBV for dealing with django forms

class cbv_form(View):
    def get(self,request):
        form=StudentForm()
        d={'form':form}
        return render(request,'cbv_form.html',d)
    
    def post(self,request):
        form_data=StudentForm(request.POST)
        if form_data.is_valid():
            return HttpResponse(str(form_data.cleaned_data))

# returning HTML page By using TemplateView Class

class cbv_template(TemplateView):
    template_name='cbv_template.html'
























