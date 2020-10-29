from . import views
from django.urls import path
from .import views
from .views import *

urlpatterns=[
    path('',Class_view.as_view(),name="testing"),
    path('message1',Message.as_view(template_name='message1.html'),name="message1"),
    path('author', AuthorView.as_view(),name='author'),
    path('authorlist',AuthorList.as_view(),name='author-list'),
    path('studentlist',StudentList.as_view(),name='student-list'),
    path('parentview/<int:id>',ParentView.as_view(),name='parentview'),
    path('student/<int:pk>',StudentDetailView.as_view(),name='studentdetail'),
    path('addstudent',StudentAdd.as_view(),name='addstudent'),
    path('createstudent',StudentCreateView.as_view(),name='studentcreate'),
    path('updatestudent/<int:pk>',UpdateStudent.as_view(),name='updatestudent'),
    path('delatestudent/<int:pk>',DelateStudent.as_view(),name='delatestudent'),
]