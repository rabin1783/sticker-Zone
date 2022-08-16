from email.headerregistry import Address
from pickle import TRUE

from django.db import models

# Create your models here.

class AppUser(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20,null=True,blank=True)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=20)
    dob = models.DateField()
    password = models.CharField(max_length=20)
    profile_pic = models.CharField(max_length=300,null=True,blank=True)
    address = models.CharField(max_length=200)
    verification_code = models.CharField(max_length=6)
    is_verified = models.BooleanField(default = False)
    is_removed = models.BooleanField(default = False)
    created_at = models.DateTimeField(default=0)
    update_at = models.DateTimeField(null=True)
    removed_at = models.DateTimeField(null=True)
    
    

    class Meta:
        db_table = "app_users"

    def __str__(self):
        return self.first_name

class AnimeType(models.Model):
    anime_name = models.CharField(max_length=200)

    class Meta:
        db_table = "app_anime_type"
    def __str__(self):
        return self.anime_name

class Anime(models.Model):
    anime_name = models.BigIntegerField()
    Character = models.BigIntegerField()
    description = models.CharField(max_length=200)
    updated_at = models.DateTimeField(default=0)

    class Meta:
        db_table = "app_anime"
    
    def __str__(self):
        return self.description
