from typing import Any
from django.db import models
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.models import User as Usertable
from .forms import CreateUserForm, LoginUserForm
from django.contrib import messages
from django.contrib.auth.models import Group
from .models import User, User_matrix
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.


class UserListView(generic.ListView):
    model = User

class UserDetailView(generic.DetailView):
    model = User_matrix

    def get_object(self, queryset=None):
        user = Usertable.objects.get(pk=self.kwargs['pk'])
        user_matrix = User_matrix.objects.filter(Cuser=user)
        return user_matrix[0]

# Project Class Views
class UsermatrixListView(generic.ListView):
    model = User_matrix
class UsermatrixDetailView(generic.DetailView):
    model = User_matrix



def index(request):
# Render index.html
    user_detail = Usertable.objects.all()
    matrix_detail = User_matrix.objects.all()
    print("active user query set", user_detail)
    print("other data queryset",matrix_detail)


    return render(request, 'fitness_app/index.html', {'user_detail': user_detail, 'matrix_detail': matrix_detail, "user": request.user})

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'])
            login(request,new_user)
            #username = form.cleaned_data.get('username')
            #messages.success(request,'Account was created for' + User.name)
            return redirect('index')
    context={'form':form}
    return render(request,'registration/register.html',context)

def loginUser(request):
    if request.method == "POST":
        form = LoginUserForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('user-detail',
                            pk=user.id)
    else:
        form = LoginUserForm()
    return render(request,'registration/login.html',{'form':form})

def userDetails(request, pk):
    user = Usertable.objects.get(pk=pk)
    user_matrix = User_matrix.objects.filter(Cuser=user)
    return render(request, "fitness_app/user_detail.html", {"user_matrix": user_matrix[0]})

def logoutUser(request):
    logout(request)
    return redirect("index")


