from django.forms import ModelForm
from .models import User,User_matrix
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

#create class for project form
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class LoginUserForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']




