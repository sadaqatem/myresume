
# Create your models here.
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator



# Create your models here.

class Person(models.Model):

    name = models.CharField(max_length=200, null=True)
    description= models.TextField()
    phone = models.BigIntegerField(default=0,null=True)
    email = models.EmailField(max_length=200, null=True)
    profile_pic = models.ImageField(default="profile1.jpg", null=True, blank=True)
    date_of_birth = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    address= models.CharField(max_length=300, null=True)
    fb = models.URLField(max_length=500, null=True)
    insta = models.URLField(max_length=500, null=True)
    twitter = models.URLField(max_length=500, null=True)
    linkedin = models.URLField(max_length=500, null=True)
    githuburl = models.URLField(max_length=500, null=True)
    stackoverflow = models.URLField(max_length=500, null=True)

    def __str__(self):
        return self.name
    

class Project(models.Model):
    CATEGORY = (
        ('web', 'web'),
        ('android', 'android'),
        ('desktop', 'desktop'),
        ('blockchain', 'blockchain'),
    )
    
    name = models.CharField(max_length=200, null=True)
    description=models.TextField()
    completedDate=models.DateField(null=True, blank=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)


class Education(models.Model):
    CATEGORY = (
        ('ssc', 'ssc'),
        ('hssc', 'hssc'),
        ('bachelors', 'bachelors'),
        ('masters', 'masters'),
        ('phd', 'phd'),
        ('other', 'other'),
    )
    FIELD = (
        ('pre-medical', 'pre-medical'),
        ('pre-engineering', 'pre-engineering'),
        ('pre-computer science', 'pre-computer science'),
        ('arts', 'arts'),
        ('software engineering', 'software engineering'),
        ('sociology', 'sociology'),
        ('humanity', 'humanity'),
        ('other', 'other'),
    )
    
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)      
    field = models.CharField(max_length=200, null=True, choices=FIELD)
    institute=models.CharField(max_length=200, null=True)
    marks=models.IntegerField(default=0, null=True)
    completedDate=models.DateField(null=True, blank=True)
    

class Skill(models.Model):
    name=  models.CharField(max_length=200, null=True)
    proficiency= models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
     )
    
    

        
        
        

