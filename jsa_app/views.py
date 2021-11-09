from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import csv
from jsa_app.models import Checklist
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
    questions = []
    title = ""
    
    if selected_checklist == "mw_checklist":
        checklist = Checklist.objects.get(title__icontains = "MW")
        questions = checklist.questions.all()
    elif selected_checklist == "opgw_checklist":
        checklist = Checklist.objects.get(title__icontains = "OPGW")
        title = "OPGW JSA Checklist"
        questions = checklist.questions.all()

    elif selected_checklist == "ofc_checklist":
        checklist = Checklist.objects.get(title__icontains = "OFC")
        title = "OFC JSA Checklist"
        questions = checklist.questions.all()

    elif selected_checklist == "pole_checklist":
        checklist = Checklist.objects.get(title__icontains = "POLE")
        title = "POLE JSA Checklist"
        questions = checklist.questions.all()

    else:
        messages.error(request,'Invalid JSA Checklist Choice, Please Select Valid Choice..')
        return redirect(reverse('home'))
    
    # Handling JSA Submission ...
    
    if request.method == "POST":
        answers = []
        questionare = []
        data = request.POST
        print("**************************8")
        for i,value in enumerate(data.values()):
            #It will give string Responese like [Yes, No, NA, Yes]
            if i != 0:
                answers.append(value)
        for qus in questions:
            questionare.append(qus)
        print(questionare)
        print(answers)
        
        # Now I have List of Question and List of Responses ...
        #TODO: I will generate a CSV file with Questions, Answers, Date Time and User Information.
        
        # Generate CSV File of JSA
        
        
        
    context={
        'selected_checklist':selected_checklist,
        'questions':questions,
        'title':title
    }
    return render(request,'jsa_checklist.html',context)