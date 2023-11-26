from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
    path('', views.index, name='index'),

    path('user/', views.UsermatrixListView.as_view(), name= 'user'),
    # path('user/detail/<int:pk>', views.UserDetailView.as_view(), name='user-detail'),
    path('user/matrix/<int:pk>', views.UsermatrixDetailView.as_view(), name='user-matrix'),
    path('accounts/profile' , views.loginUser, name= 'login'),
    path('accounts/profile/user/<int:pk>' , views.userDetails, name= 'user-detail'),
    path('accounts/register' , views.registerPage, name = 'register_page'),
    path('accounts/profile/logout' , views.logoutUser, name= 'logout'),

]