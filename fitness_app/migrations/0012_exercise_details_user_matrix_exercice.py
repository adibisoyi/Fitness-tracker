# Generated by Django 4.2.5 on 2023-11-26 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fitness_app', '0011_alter_user_matrix_cuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_name', models.CharField(max_length=200)),
                ('exercise_reps', models.CharField(max_length=200)),
                ('exercise_goal', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='user_matrix',
            name='Exercice',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='fitness_app.exercise_details'),
        ),
    ]
