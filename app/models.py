from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.CharField(max_length=30)
    profile_image = models.ImageField(default='user.png', upload_to="users/", null=True, blank=True)

    def __str__(self):
        return self.user

class Detals(models.Model):
    direction = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    mail = models.CharField(max_length=64)
    tel = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.direction} \n{self.location} \n{self.mail}\n{self.tel}"
    
class Skills(models.Model):
    direction_name = models.CharField(max_length=32)
    percent = models.IntegerField(default=0)
    class_name = models.CharField(max_length=32, default='')

    def __str__(self):
        return self.direction_name
    
class Languages(models.Model):
    language_name = models.CharField(max_length=32)
    percent = models.IntegerField(default=0)
    class_name = models.CharField(max_length=32, default='')

    def __str__(self):
        return self.language_name

class WorkExperince(models.Model):
    direction = models.CharField(max_length=32)
    company = models.CharField(max_length=32)
    company_link = models.CharField(max_length=128, default='')
    date_time = models.CharField(max_length=32, default=0)
    about = models.CharField(max_length=512, default='')

    def __str__(self):
        return f"{self.direction}\n{self.company}"
    
class Educations(models.Model):
    education = models.CharField(max_length=52)
    education_link = models.CharField(max_length=128, default='')
    date_time = models.CharField(max_length=52)
    about = models.CharField(max_length=512)

    def __str__(self):
        return self.education

class Icons(models.Model):
    social_icons =  models.CharField(max_length=128)
    social_icons_link = models.CharField(max_length=128)

class Footer(models.Model):
    company = models.CharField(max_length=128)
    company_link = models.CharField(max_length=128, default='')
    hashtags = models.TextField()

    def __str__(self):
        return self.company