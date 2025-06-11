from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email='test@example.com', name='Test User', password='testpass')
        self.assertEqual(user.email, 'test@example.com')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Team A')
        self.assertEqual(team.name, 'Team A')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(email='test2@example.com', name='Test2', password='testpass')
        activity = Activity.objects.create(activity_id='act1', user=user, type='run', duration=30, date='2025-06-11T00:00:00Z')
        self.assertEqual(activity.type, 'run')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='Team B')
        leaderboard = Leaderboard.objects.create(leaderboard_id='lb1', team=team, score=100)
        self.assertEqual(leaderboard.score, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        user = User.objects.create(email='test3@example.com', name='Test3', password='testpass')
        workout = Workout.objects.create(workout_id='wo1', user=user, description='Pushups', date='2025-06-11T00:00:00Z')
        self.assertEqual(workout.description, 'Pushups')
