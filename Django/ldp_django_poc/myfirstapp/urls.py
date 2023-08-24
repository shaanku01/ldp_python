from django.urls import path
from . import views

urlpatterns = [
    path('',views.myfunctioncall , name="index"),
    path('about',views.myfunctionabout,name='about'),
    path('add/<int:a>/<int:b>',views.addNumbers,name="add"),
    path('intro/<str:name>/<int:age>',views.intro,name="intro"),

    path('myfirstpage',views.renderPage,name='renderPage'),
    path('mysecondpage',views.mySecondPage,name='mysecondpage'),
    path('mythirdpage',views.myThirdPage,name='mythirdpage')
]