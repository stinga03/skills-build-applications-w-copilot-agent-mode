from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_user_model(self):
        self.assertTrue(hasattr(User, 'email'))
    def test_team_model(self):
        self.assertTrue(hasattr(Team, 'name'))
    def test_activity_model(self):
        self.assertTrue(hasattr(Activity, 'type'))
    def test_workout_model(self):
        self.assertTrue(hasattr(Workout, 'name'))
    def test_leaderboard_model(self):
        self.assertTrue(hasattr(Leaderboard, 'points'))
