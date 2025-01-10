from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    career_goals = models.TextField()

class Goal(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

