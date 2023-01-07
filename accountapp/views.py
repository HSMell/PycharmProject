from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.foms import AccountUpdateForm
from accountapp.models import HelloWorld


# Create your views here.

def hello_world(request):

    if request.method == "POST":

        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request,'accountapp/hello_world.html', context={'hello_world_list': hello_world_list}) #context는 데이터 꾸러미


class AccountCreateView(CreateView):
    model = User  # User는 장고에서 기본제공해주는 모델
    form_class = UserCreationForm # 패스워드 검증 폼 내장 클래스
    success_url = reverse_lazy('accountapp:hello_world')  #함수와 클래스의 불러오는 방식의 차이, rever_lazy는 클래스형에서 사용함
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView):
    model = User  # User는 장고에서 기본제공해주는 모델
    context_object_name = 'target_user'
    form_class = AccountUpdateForm # 패스워드 검증 폼 내장 클래스
    success_url = reverse_lazy('accountapp:hello_world')  #함수와 클래스의 불러오는 방식의 차이, rever_lazy는 클래스형에서 사용함
    template_name = 'accountapp/update.html'

class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'