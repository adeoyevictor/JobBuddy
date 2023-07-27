from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Job(models.Model):
    COLORS = [
        ('#5350E3', '#5350E3'), 
        ('#25ADE7', '#25ADE7'), 
        ('#2AD587', '#2AD587'), 
        ('#FFF500', '#FFF500'), 
        ('#FF7C00', '#FF7C00'), 
        ('#E350D8', '#E350D8'),
        ('#9012FE', '#9012FE')
        ]

    LEVELS = [
        ('INTERNSHIP', 'INTERNSHIP'),
        ('ENTRY_LEVEL', 'ENTRY_LEVEL'),
        ('MID_LEVEL', 'MID_LEVEL'),
        ('SENIOR_LEVEL', 'SENIOR_LEVEL'),
    ]

    MODES = [
        ('FULL_TIME', 'FULL_TIME'),
        ('PART_TIME', 'PART_TIME'),
        ('CONTRACT', 'CONTRACT'),
    ]

    STAGES = [
        ('NOT_APPLIED', 'NOT_APPLIED'),
        ('APPLIED', 'APPLIED'),
        ('FIRST_INTERVIEW', 'FIRST_INTERVIEW'),
        ('FOLLOW_UP_INTERVIEWS', 'FOLLOW_UP_INTERVIEWS'),
        ('OFFER', 'OFFER'),
    ]

    title = models.CharField(max_length=64)
    company = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    url = models.URLField(null=True, blank=True)
    description = models.TextField(blank=True)
    color = models.CharField(max_length=7, choices=COLORS, default=COLORS[0])
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs')
    posting_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    level = models.CharField(max_length=64, choices=LEVELS, default=LEVELS[0])
    mode = models.CharField(max_length=64, choices=MODES, default=MODES[0])
    stage = models.CharField(max_length=64, choices=STAGES, default=STAGES[0])
    archived = models.BooleanField(default=False)


    def __str__(self):
        return self.title

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'company': self.company,
            'location': self.location,
            'url': self.url,
            'description': self.description,
            'color': self.color,
            'timestamp': self.timestamp.strftime("%b %d %Y, %I:%M %p"),
            'user': self.user.username,
            'posting_date': self.posting_date,
            'level': self.level,
            'mode': self.mode,
            'stage': self.stage,
            'archived': self.archived
        }





        