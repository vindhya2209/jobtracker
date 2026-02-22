from django.db import models
from django.contrib.auth.models import User


# ===============================
# MAIN JOB MODEL
# ===============================
class Job(models.Model):

    CATEGORY_CHOICES = [
        ('SSC', 'SSC'),
        ('UPSC', 'UPSC'),
        ('Railway', 'Railway'),
        ('Banking', 'Banking'),
        ('Defence', 'Defence'),
        ('Army', 'Army'),
        ('Civilian','Civilian')
 ]

    STATUS_CHOICES = [
        ('open', 'Open'),
        ('close', 'Closed'),
        ('deadline', 'Deadline Soon'),
    ]

    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    last_date = models.DateField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()   # Better than CharField
    url = models.URLField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='open'
    )

    def __str__(self):
        return self.title


# ===============================
# OTP MODEL
# ===============================
class OTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username