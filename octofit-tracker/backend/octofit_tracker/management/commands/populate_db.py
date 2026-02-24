from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()


        # Create teams with explicit team_id
        marvel = Team.objects.create(team_id='marvel', name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(team_id='dc', name='DC', description='DC superheroes')

        # Create users
        users = [
            User.objects.create(user_id='ironman', email='ironman@marvel.com', name='Iron Man', team=marvel),
            User.objects.create(user_id='captainamerica', email='captainamerica@marvel.com', name='Captain America', team=marvel),
            User.objects.create(user_id='spiderman', email='spiderman@marvel.com', name='Spider-Man', team=marvel),
            User.objects.create(user_id='batman', email='batman@dc.com', name='Batman', team=dc),
            User.objects.create(user_id='superman', email='superman@dc.com', name='Superman', team=dc),
            User.objects.create(user_id='wonderwoman', email='wonderwoman@dc.com', name='Wonder Woman', team=dc),
        ]

        # Create activities
        for user in users:
            Activity.objects.create(user=user, type='Running', duration=30, date=timezone.now().date())
            Activity.objects.create(user=user, type='Cycling', duration=45, date=timezone.now().date())

        # Create workouts
        w1 = Workout.objects.create(name='Hero HIIT', description='High intensity workout for heroes', suggested_for=[marvel.team_id, dc.team_id])
        w2 = Workout.objects.create(name='Power Yoga', description='Yoga for strength and flexibility', suggested_for=[dc.team_id])

        # Create leaderboards
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
