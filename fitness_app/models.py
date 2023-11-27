from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User as Usertable

# Create your models here.


class User(models.Model):

    #List of choices for major value in database, human readable name
    GOAL = (
    ('100', 'Begineer'),
    ('500', 'Intermediate'),
    ('1000', 'Pro'),
    )
    #name = models.CharField(max_length=200)
    #email = models.CharField("Email", max_length=200)
    user=models.OneToOneField(Usertable, on_delete=models.CASCADE, unique=True)
    level = models.CharField(max_length=200, choices=GOAL)
    #portfolio = models.OneToOneField(Portfolio, on_delete=models.CASCADE, unique=True)


    #Define default String to return the name for representing the Model object."
    def __str__(self):
        return self.user.username


    #Returns the URL to access a particular instance of MyModelName.
    #if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])

class Exercise_details(models.Model):

    exercise_name =  models.CharField(max_length=200)
    exercise_reps =  models.CharField(max_length=200)
    exercise_goal =  models.CharField(max_length=200)
    exercise_relaxation =  models.CharField(max_length=200)
    exercise_details = models.CharField(max_length=900)
    relexercise_details = models.CharField(max_length=900)

     #Define default String to return the name for representing the Model object."
    def __str__(self):
        return self.exercise_name
    
    #Returns the URL to access a particular instance of MyModelName.
    #if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    # def get_absolute_url(self):
    #     return reverse('exercise-details', args=[str(self.id)])  

class User_matrix(models.Model):
    #name = models.CharField(max_length=200)
    current_calorie = models.CharField(max_length=200)
    heartbeat =  models.CharField(max_length=200)
    user_grade =  models.CharField(max_length=200)
    Cuser = models.ForeignKey(Usertable, on_delete=models.CASCADE, default = None)
    Exercice = models.ForeignKey(Exercise_details,on_delete=models.CASCADE, default = None)

     #Define default String to return the name for representing the Model object."
    def __str__(self):
        return self.Cuser.username
    
    #Returns the URL to access a particular instance of MyModelName.
    #if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse('user-matrix', args=[str(self.id)])
    

