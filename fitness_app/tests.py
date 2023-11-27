from django.test import TestCase

# Create your tests here.

from .models import User, User_matrix
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
'''
#Tests for MODELS
class UserModelTest(TestCase):
    def setUp(self):
        # Assuming you have a Usertable instance, replace 'your_username' with an actual username
        user = Usertable.objects.create(username='abisoyi')
        self.user = User.objects.create(user=user, level='100')

    def test_user_str(self):
        self.assertEqual(str(self.user), 'abisoyi')

    def test_user_absolute_url(self):
        url = reverse('user-detail', args=[str(self.user.id)])
        self.assertEqual(self.user.get_absolute_url(), url)

    def test_user_choices(self):
        # Ensure that the choices for the 'level' field match the defined choices in the model
        choices = dict(User.GOAL)
        self.assertEqual(self.user.get_level_display(), choices['100'])

    def test_user_level_validation(self):
        # Test that the level field only accepts valid choices
        invalid_user = User.objects.create(user=self.user.user, level='Invalid')
        with self.assertRaises(ValueError):
            invalid_user.full_clean()


class ExerciseDetailsModelTest(TestCase):
    def setUp(self):
        self.exercise = Exercise_details.objects.create(
            exercise_name='Bench Press',
            exercise_reps='3 sets of 10 reps',
            exercise_goal='Strength building',
            exercise_relaxation='2 minutes between sets',
            exercise_details='Lie on a flat bench...',
        )

    def test_exercise_details_str(self):
        self.assertEqual(str(self.exercise), 'Bench Press')

class UserMatrixModelTest(TestCase):
    def setUp(self):
        # Assuming you have a Usertable instance, replace 'your_username' with an actual username
        # You should also create an Exercise_details instance before creating a User_matrix instance
        # as it has a ForeignKey to Exercise_details
        user = Usertable.objects.create(username='your_username')

        self.user_matrix = User_matrix.objects.create(
            current_calorie='2000',
            heartbeat='80',
            user_grade='A',
            Cuser=user,
            Exercice=Exercise_details.objects.create(exercise_name='Squats', exercise_details='Stand with your feet shoulder-width apart...'),
        )

    def test_user_matrix_str(self):
        self.assertEqual(str(self.user_matrix), 'your_username')

    def test_user_matrix_absolute_url(self):
        url = reverse('user-matrix', args=[str(self.user_matrix.id)])
        self.assertEqual(self.user_matrix.get_absolute_url(), url)
'''

#Test for Views
'''
class FitnessAppViewsTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        # Create a test user matrix
        self.user_matrix = User_matrix.objects.create(
            Cuser=self.user,
            # Add other required fields here
        )

        # Create a test client
        self.client = Client()

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'fitness_app/index.html')

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

        # Test registration form submission
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password1': 'newpassword',
            'password2': 'newpassword',
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful registration

        # You can add more assertions to check if the user was created, etc.

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

        # Test login form submission
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword',
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful login

        # You can add more assertions to check if the user is logged in, etc.

    def test_logout_view(self):
        # Log in the user first
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Redirect after successful logout

        # You can add more assertions to check if the user is logged out, etc.

    def test_user_details_view(self):
        response = self.client.get(reverse('user-detail', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'fitness_app/user_detail.html')
'''

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
'''
class UserRegistrationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        self.driver.get("http://127.0.0.1:8000/accounts/register")  # Replace with the actual URL of your registration page

        # Assuming you have registration form fields like username, password1, password2
        username_input = self.driver.find_element("name", "username")
        email_input = self.driver.find_element("name", "email")
        password1_input = self.driver.find_element("name", "password1")
        password2_input = self.driver.find_element("name", "password2")
        submit_button = self.driver.find_element("name", "Create User")

        # Fill in the registration form
        username_input.send_keys("testuser12")
        email_input.send_keys("testuser@example.com")
        password1_input.send_keys("testpassword")
        password2_input.send_keys("testpassword")

        # Submit the form
        submit_button.click()

        # Wait for the registration to complete (you might need a more robust wait strategy)
        time.sleep(2)

        # Assert that the registration was successful
        self.assertIn("index", self.driver.current_url)

if __name__ == "__main__":
    unittest.main()
'''

class UserLoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_user_login(self):
        self.driver.get("http://127.0.0.1:8000/accounts/profile")  # Replace with the actual URL of your login page

        # Assuming you have login form fields like username, password
        username_input = self.driver.find_element("name", "username")
        password_input = self.driver.find_element("name", "password")
        submit_button = self.driver.find_element("name", "submit")

        # Fill in the login form
        username_input.send_keys("testuser")
        password_input.send_keys("testpassword")

        # Submit the form
        submit_button.click()

        # Wait for the login to complete (you might need a more robust wait strategy)
        time.sleep(2)

        # Assert that the login was successful
        self.assertIn("index", self.driver.current_url)

if __name__ == "__main__":
    unittest.main()
