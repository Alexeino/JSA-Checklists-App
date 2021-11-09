from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.
def login_view(request):
    form = AuthenticationForm()
    if request.method == "POST":
        data = request.POST
        username = data['username']
        password = data['password']
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect(reverse('home'))
        
        else:
            messages.error(request,'Invalid Username or Password')
            return render(request,'login_form.html',{
                'form':form
            })
        
    context={
        'form':form
    }
    return render(request,'login_form.html',context)

@login_required
def home(request):
    if request.method == "POST":
        selected_checklist = request.POST.get('checklist_select')
        # print(selected_checklist)
        request.session['selected_checklist'] = selected_checklist
        
        return redirect(reverse('jsa_checklist'))
    return render(request,'welcome.html')

def jsa_checklist(request):
    selected_checklist = request.session['selected_checklist']
    if selected_checklist == "mw_checklist":
        pass
    elif selected_checklist == "opgw_checklist":
        pass
    elif selected_checklist == "ofc_checklist":
        pass
    elif selected_checklist == "pole_checklist":
        pass
    else:
        messages.error(request,'Invalid JSA Checklist Choice, Please Select Valid Choice..')
        return redirect(reverse('home'))
    
    
    context={
        'checklist':selected_checklist
    }
    return render(request,'jsa_checklist.html',context)