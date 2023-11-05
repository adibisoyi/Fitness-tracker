from typing import Any
from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import User,User_matrix
# Create your views here.


class UserListView(generic.ListView):
    model = User

class UserDetailView(generic.DetailView):
    model = User_matrix

    def get_object(self, queryset=None):
        user_matrix = User_matrix.objects.get(Cuser__lte=self.kwargs['pk'])

        

        return user_matrix

# Project Class Views
class UsermatrixListView(generic.ListView):
    model = User_matrix
class UsermatrixDetailView(generic.DetailView):
    model = User_matrix


def index(request):
# Render index.html
    user_detail = User.objects.all()
    matrix_detail = User_matrix.objects.all()
    print("active user query set", user_detail)
    print("other data queryset",matrix_detail)
    return render(request, 'fitness_app/index.html', {'user_detail': user_detail, 'matrix_detail': matrix_detail})


