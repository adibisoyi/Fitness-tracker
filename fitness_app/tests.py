from django.test import TestCase

# Create your tests here.
from django.urls import path
from . import views
from .models import User, User_matrix
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import User as Usertable
from selenium.webdriver.common.by import By
from .models import Exercise_details, User_matrix
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

#Tests for MODELS
class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertTrue(self.user.check_password('testpassword'))

    def test_user_str_representation(self):
        self.assertEqual(str(self.user), 'testuser')#Update this based on your URL pattern

class ExerciseDetailsModelTest(TestCase):
    def setUp(self):
        self.exercise = Exercise_details.objects.create(
            exercise_name="Test Exercise",
            exercise_reps="10",
            exercise_goal="Build Muscle",
            exercise_relaxation="Yoga",
            exercise_details="Details of the exercise",
            relexercise_details="Details of the relaxation exercise"
        )

    def test_exercise_creation(self):
        self.assertEqual(self.exercise.exercise_name, 'Test Exercise')
        # Add more assertions for other fields

    def test_exercise_str_representation(self):
        self.assertEqual(str(self.exercise), 'Test Exercise')

class UserMatrixModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.exercise = Exercise_details.objects.create(
            exercise_name="Test Exercise",
            exercise_reps="10",
            exercise_goal="Build Muscle",
            exercise_relaxation="Yoga",
            exercise_details="Details of the exercise",
            relexercise_details="Details of the relaxation exercise"
        )
        self.user_matrix = User_matrix.objects.create(
            current_calorie="100",
            heartbeat="80",
            user_grade="Intermediate",
            Cuser=self.user,
            Exercice=self.exercise
        )

    def test_user_matrix_creation(self):
        self.assertEqual(self.user_matrix.current_calorie, '100')
        # Add more assertions for other fields

    def test_user_matrix_str_representation(self):
        self.assertEqual(str(self.user_matrix), 'testuser')

    def test_user_matrix_get_absolute_url(self):
        url = self.user_matrix.get_absolute_url()
        self.assertEqual(url, f'/user/matrix/{self.user_matrix.id}')  # Update this based on your URL pattern


#Test for Views

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        # Create a test user
        self.user = Usertable.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        # Log in the test user
        self.client.login(username='testuser', password='testpassword')

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'fitness_app/index.html')

    def test_register_view(self):
        response = self.client.get(reverse('register_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_user_details_view(self):
        response = self.client.get(reverse('user-detail', args=[str(self.user.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'fitness_app/user_detail.html')

    def test_logout_view(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # 302 for redirect after logout
        self.assertRedirects(response, reverse('index'))

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
        expected_url = "http://127.0.0.1:8000/"  # Replace with the expected URL
        self.assertEqual(expected_url, self.driver.current_url)


class UserLoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_user_login(self):
        self.driver.get("http://127.0.0.1:8000/accounts/profile")  # Replace with the actual URL of your login page

        # Assuming you have login form fields like username, password
        username_input = self.driver.find_element(By.NAME, "username")
        password_input = self.driver.find_element(By.NAME, "password")

        # Fill in the login form
        username_input.send_keys("testuser")
        password_input.send_keys("testpassword")

        # Find the submit button using the XPATH strategy
        submit_button = self.driver.find_element(By.XPATH, '//button[@type="submit"]')

        # Submit the form
        submit_button.click()

        # Wait for the login to complete (you might need a more robust wait strategy)
        time.sleep(2)

        # Assert that the login was successful
        expected_url = "http://127.0.0.1:8000/accounts/profile/user/3"  # Replace with the expected URL
        self.assertEqual(expected_url, self.driver.current_url)

if __name__ == "__main__":
    unittest.main()
