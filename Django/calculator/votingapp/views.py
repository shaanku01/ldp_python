from django.shortcuts import render
from django.http import HttpResponse,JsonResponse


# Create your views here.
programmingLanguages = ["Python", "JavaScript", "Java", "C++", "Ruby", "Swift", "Kotlin", "Go", "Rust", "PHP", "TypeScript", "Scala", "Perl", "Haskell", "Lua"]
globalCounter = dict()
def index(request):
    mydict = {
        "arr":programmingLanguages
    }
    return render(request,'index.html',context=mydict)

def getQuery(request):
    q  = request.GET['languages']
    if q in globalCounter:
        globalCounter[q] = globalCounter[q] + 1
    else:
        globalCounter[q] = 1
    mydict = {
        "arr" : programmingLanguages,
        "globalcnt": globalCounter
    }
    return render(request,'index.html',context=mydict)

def sortData(request):
    global globalCounter
    globalCounter = dict(sorted(globalCounter.items(),key=lambda x:x[1],reverse=True))
    mydict = {
        "arr" : programmingLanguages,
        "globalcnt": globalCounter
    }
    return render(request,'index.html',context=mydict)
