from django.db import models

# Create your models here.


class Idea(models.Model):
    idea_title = models.CharField(max_length=255)
    idea_description = models.CharField(max_length=1000)
    idea_instant_investment = models.IntegerField()
    idea_total_investment = models.IntegerField()
    posted_datetime = models.DateTimeField(auto_now=True)
    