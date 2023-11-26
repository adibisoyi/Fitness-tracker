from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from .models import User, User_matrix

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            name="Test User",
            email="test@example.com",
            level="100"  # Assuming '100' corresponds to 'Beginner'
        )

    def test_user_creation(self):
        user = User.objects.get(name="Test User")
        self.assertEqual(user.name, "Test User")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.level, "100")

    def test_user_string_representation(self):
        user = User.objects.get(name="Test User")
        self.assertEqual(str(user), "Test User")

    def test_user_absolute_url(self):
        user = User.objects.get(name="Test User")
        self.assertEqual(user.get_absolute_url(), f'/user/detail/{user.id}')

class UserMatrixModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            name="Test User",
            email="test@example.com",
            level="100"
        )
        self.user_matrix = User_matrix.objects.create(
            current_calorie="200",
            heartbeat="80",
            exercise_name="Push-ups",
            exercise_reps="10",
            exercise_goal="50",
            user_grade="A",
            exercise_relaxation="5",
            Cuser=self.user
        )

    def test_user_matrix_creation(self):
        user_matrix = User_matrix.objects.get(exercise_name="Push-ups")
        self.assertEqual(user_matrix.current_calorie, "200")
        self.assertEqual(user_matrix.heartbeat, "80")
        self.assertEqual(user_matrix.exercise_name, "Push-ups")
        self.assertEqual(user_matrix.exercise_reps, "10")
        self.assertEqual(user_matrix.exercise_goal, "50")
        self.assertEqual(user_matrix.user_grade, "A")
        self.assertEqual(user_matrix.exercise_relaxation, "5")
        self.assertEqual(user_matrix.Cuser, self.user)

    def test_user_matrix_string_representation(self):
        user_matrix = User_matrix.objects.get(exercise_name="Push-ups")
        self.assertEqual(str(user_matrix), "Test User")

    def test_user_matrix_absolute_url(self):
        user_matrix = User_matrix.objects.get(exercise_name="Push-ups")
        self.assertEqual(user_matrix.get_absolute_url(), f'/user/matrix/{user_matrix.id}')
