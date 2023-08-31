from django.shortcuts import render
from django.http import HttpResponse , JsonResponse

from .forms import *
import re

# Create your views here.
def myfunctioncall(request):
    return HttpResponse("Hello World")

def myfunctionabout(request):
    return HttpResponse("About Route!")

def addNumbers(request,a,b):
    return HttpResponse(a+b)

def intro(request , name,age):
    # JsonResponse takes the dict object.
    dictionary = {
        "name" : name,
        "age" : age
    }
    return JsonResponse(dictionary)

def renderPage(request):
    return render(request,'index.html')

def mySecondPage(request):
    return render(request,'second.html')

def myThirdPage(request):
    var = "Hello World from view three"
    greeting = "Hey how are you??"
    fruits = ["apple","mango","banana"]
    num1 , num2 = 3 , 5
    ans = num1 > num2 
    dictobj = {
        "var" : var,
        "msg":greeting,
        "fruits_list":fruits,
        "num1":num1,
        "num2":num2,
        "ans":ans
    }
    return render(request,'third.html', context=dictobj)


def myImagePage(request):
    return render(request,'imagepage.html')

def myimagepage5(request,imagename):
    myimage = str(imagename).lower()
    if myimage == 'python':
        var = True
    else:
        var = False     
    return render(request,'imagepage5.html',context={'var' : var})

def myForm(request):
    return render(request,'myform.html')

def submitMyForm(request):
    mydictionary = {
        "var1" : request.POST['mytext'] ,
        "var2" : request.POST['mytextarea'],
        "method": request.method
    }
    return JsonResponse(mydictionary)

def myForm2(request):
    if request.method == 'POST':
        form =  FeedbackForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            subject = request.POST['subject']
            email = request.POST['email']
            # var = str("Form submitted "+ str(request.method))
            # return HttpResponse(var)
            mydictionary = {
                "form" : FeedbackForm()
            }
            errors = []
            errorFlag = False
            if title != title.upper():
                errorFlag = True
                errors.append('Title Should be in capital')
                # mydictionary['error'] = True
                # mydictionary['errormsg'] = "Title Should be in capital"
            if not re.search('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',email):
                errorFlag = True
                errors.append('Not a valid email address')
            if errorFlag != True:
                mydictionary['success'] = True
                mydictionary['successMessage'] = "Form Submitted"
            
            mydictionary['error'] = errorFlag
            mydictionary['errors'] = errors
            return render(request,'myform2.html',context=mydictionary)
        else:
            return render(request,'myform2.html',context={"form":form})
    elif request.method == 'GET':
        form = FeedbackForm()
        return render(request,'myform2.html',context={"form":form})
    
def error_404_view(request,exception):
    return render(request,'404.html')