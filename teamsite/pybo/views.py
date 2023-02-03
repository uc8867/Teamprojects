from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm

from .models import Question


# Create your views here.

def index(request):
    question = Question.objects.all
    context = {'question': question}
    return render(request, 'pybo/main.html', context)

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

#요청게시판
def question(requst):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)

#회원가입
#def registerPage(request):
#    form = UserCreationForm()
#    if request.method == "POST":
#        form = UserCreationForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('login')
#    context={'form':form}
#    return render(request, 'accounts/register.html', context)