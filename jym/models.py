from django.db import models

# Create your models here.
class Team(models.Model):
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField()
    profile_pic = models.ImageField(upload_to='teams/')
    twitter_url = models.CharField(max_length=100, blank=True, null=True)
    facebook_url = models.CharField(max_length=100, blank=True, null=True)
    instagram_url = models.CharField(max_length=100, blank=True, null=True)
    linkedin_url = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.full_name