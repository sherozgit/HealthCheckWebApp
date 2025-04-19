from django.db import models
from django.contrib.auth.models import User  # or your custom user model


class HealthCard(models.Model):
    CardID = models.AutoField(primary_key=True)
    CardName = models.CharField(max_length=255, unique=True, null=False)
    Description = models.TextField(null=False)  # Fixed typo from 'Desctiption'

    def __str__(self):
        return self.CardName


class Session(models.Model):
    SessionID = models.AutoField(primary_key=True)
    Date = models.DateField(null=False)
    Time = models.TimeField(null=False)
    LogRecord = models.TextField(null=True, blank=True)
    SessionDescrip = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.Date} @ {self.Time}"


class Vote(models.Model):
    TRAFFIC_CHOICES = [('Red', 'Red'), ('Green', 'Green'), ('Yellow', 'Yellow')]

    VoteID = models.AutoField(primary_key=True)
    voter = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to user who voted
    team = models.ForeignKey('teams.Team', on_delete=models.CASCADE)  # You must import or define Team model
    card = models.ForeignKey(HealthCard, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    TrafficLight = models.CharField(max_length=6, choices=TRAFFIC_CHOICES, null=False)
    Progress = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('voter', 'team', 'card', 'session')  # Prevent duplicate votes

    def __str__(self):
        return f"{self.voter.username} - {self.card.CardName} - {self.TrafficLight}"
