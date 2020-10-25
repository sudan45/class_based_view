from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .forms import *
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView,CreateView
from django import forms


from .forms import StudentForm



# Create your views here.


class Class_view(View):
    def get(self, request):
        return HttpResponse('<h1> Hello </h1>')


############
# same views but have different url
class Message(View):
    template_name = ''

    # def get(self, request):
    #     context = {'msg': 'hellpo world bitgarage'}
    #     return render(request, self.template_name, context)


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
    # template_name_suffix='_list' #it add the suffix at the default template Created by ListView
    # context_object_name=''
    ordering=['name']





class ParentView(TemplateView):
    template_name='example/parentview.html'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['name']='sudan'
        return context


class StudentDetailView(DetailView):
    model=Student
    template_name='example/student.html'
    context_object_name='student'

    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        context['all_studnet']=self.model.objects.all()
        return context


class StudentAdd(FormView):
    form_class=StudentForm
    template_name='example/addstudent.html'
    context_object_name='studentform'
    success_url='/'


    def form_valid(self,form):
        form.save()
        return super().form_valid(form)



class StudentCreateView(CreateView):
    model=Student
    fields=['name','address','phone','parentname']

    def get_form(self):
        form=super().get_form()
        form.fields['name'].widget=forms.TextInput(attrs={'class':'form-control'})
        form.fields['address'].widget=forms.TextInput(attrs={'class':'form-control'})
        form.fields['phone'].widget=forms.NumberInput(attrs={'class':'form-control'})
        form.fields['parentname'].widget=forms.TextInput(attrs={'class':'form-control'})

        return form



