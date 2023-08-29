from django.urls import path
from . import views

urlpatterns = [
    path('',views.myfunctioncall , name="index"),
    path('about',views.myfunctionabout,name='about'),
    path('add/<int:a>/<int:b>',views.addNumbers,name="add"),
    path('intro/<str:name>/<int:age>',views.intro,name="intro"),

    path('myfirstpage',views.renderPage,name='renderPage'),
    path('mysecondpage',views.mySecondPage,name='mysecondpage'),
    path('mythirdpage',views.myThirdPage,name='mythirdpage'),

    path('myimagepage',views.myImagePage,name='myimagepage'),

    path('myimagepage5/<str:imagename>',views.myimagepage5,name = 'myimagepage5'),

    # Forms
    path('myForm',views.myForm,name='myForm'),
    path('submitmyform',views.submitMyForm,name='submitmyform'),

    path('myform2', views.myForm2, name='myform2')
]