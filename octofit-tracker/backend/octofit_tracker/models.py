from djongo import models

class Team(models.Model):
    team_id = models.CharField(max_length=24, primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class User(models.Model):
    user_id = models.CharField(max_length=24, primary_key=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    team = models.EmbeddedField(model_container=Team, null=True)

    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.EmbeddedField(model_container=User)
    type = models.CharField(max_length=100)
    duration = models.IntegerField()  # in minutes
    date = models.DateField()

    def __str__(self):
        return f"{self.user.name} - {self.type}"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    suggested_for = models.JSONField(default=list)  # List of team_ids

    def __str__(self):
        return self.name

class Leaderboard(models.Model):
    team = models.EmbeddedField(model_container=Team)
    points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.team.name} - {self.points} points"
