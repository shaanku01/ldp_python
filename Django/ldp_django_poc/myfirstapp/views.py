from django.shortcuts import render
from django.http import HttpResponse , JsonResponse

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