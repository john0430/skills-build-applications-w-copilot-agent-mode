from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate octofit_db with test data.'

    def handle(self, *args, **kwargs):
        # 清空現有資料
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # 建立使用者
        user1 = User.objects.create(email='alice@example.com', name='Alice', password='alicepass')
        user2 = User.objects.create(email='bob@example.com', name='Bob', password='bobpass')
        user3 = User.objects.create(email='carol@example.com', name='Carol', password='carolpass')

        # 建立團隊
        team1 = Team.objects.create(name='Team Octopus')
        team1.members.add(user1, user2)
        team2 = Team.objects.create(name='Team Kraken')
        team2.members.add(user3)

        # 建立活動
        Activity.objects.create(activity_id='act1', user=user1, type='run', duration=30, date=timezone.now())
        Activity.objects.create(activity_id='act2', user=user2, type='walk', duration=60, date=timezone.now())
        Activity.objects.create(activity_id='act3', user=user3, type='bike', duration=45, date=timezone.now())

        # 建立排行榜
        Leaderboard.objects.create(leaderboard_id='lb1', team=team1, score=150)
        Leaderboard.objects.create(leaderboard_id='lb2', team=team2, score=100)

        # 建立運動
        Workout.objects.create(workout_id='wo1', user=user1, description='Pushups', date=timezone.now())
        Workout.objects.create(workout_id='wo2', user=user2, description='Situps', date=timezone.now())
        Workout.objects.create(workout_id='wo3', user=user3, description='Squats', date=timezone.now())

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
