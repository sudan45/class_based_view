from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .forms import *
from django.views.generic.list import ListView
from django.views.generic import TemplateView


# Create your views here.


class Class_view(View):
    def get(self, request):
        return HttpResponse('<h1> Hello </h1>')


############
# same views but have different url
class Message(View):
    template_name = ''

    def get(self, request):
        context = {'msg': 'hellpo world bitgarage'}
        return render(request, self.template_name, context)


class AuthorView(View):
    template_name = 'author.html'
    form_class = AuthorForm

    def get(self, request):
        form = self.form_class()
        print(form)
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()

        context = {'form': form}
        return render(request, self.template_name, context)


class AuthorList(ListView):
    model = Author
    paginate_by = 2


class StudentList(ListView):
    model=Student
    # template_name='' #default template name is model name _list
    template_name_suffix='_list' #it add the suffix at the default template Created by ListView
    # context_object_name=''
    ordering=['name']


    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(**kwargs)
        



class ParentView(TemplateView):
    template_name='example/parentview.html'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['name']='sudan'
        return context