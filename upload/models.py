import os
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django import forms
from django.contrib.auth.models import User,Group
import datetime
from .validators import validate_file_extension
from django.core.validators import RegexValidator
#from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
GENDER = (('M','M'), ('F','F'), ('other','other'))
class Files(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(max_length=256, null=True) #, widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}))
    file = models.FileField(upload_to= 'images/',validators=[validate_file_extension],blank=True,null=True)
    title = models.CharField(max_length=255, blank=True,null=True) 
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_multiple = models.NullBooleanField(default=True,null = True,blank=True)

    def __str__(self):
        return self.name
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True) #, to=settings.AUTH_USER_MODEL
    Role=models.ForeignKey(Group,on_delete=models.CASCADE,null= True)
    GENDER = (('M','M'), ('F','F'), ('other','other'))
    Gender = models.CharField(max_length=10, choices=GENDER,null=True)
    #Img = models.ImageField(upload_to= 'images/',blank=True)
    def __str__(self):
        return self.user
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Userdetails(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{7,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True) #, to=settings.AUTH_USER_MODEL
    Img = models.ImageField(upload_to= 'images/',blank=True)
    father_name = models.CharField(max_length=255,blank=True, null=True)
    mother_name = models.CharField(max_length=255, null=True)
    grandfather_name = models.CharField(max_length=255,blank=True, null=True)
    spouse_name = models.CharField(max_length=255,blank=True, null=True)
    citizenship_no = models.CharField(max_length=255, null=True)
    issued_district = models.CharField(max_length=255, null=True)
    issue_date = models.CharField(max_length=64, null=True)
    temporary_address = models.CharField(max_length=255, null=True)
    permanent_address = models.CharField(max_length=255, null=True)
    Mobile_no = models.CharField(validators=[phone_regex], max_length=17, blank=True,null=True)
    landline = models.CharField(validators=[phone_regex], max_length=17, blank=True,null=True)
    secondary_school = models.CharField(max_length=255, null=True)
    passed_year1 = models.CharField(max_length=64,null=True)
    division_percentage1 = models.CharField(max_length=64, null=True)
    intermediate_school = models.CharField(max_length=255, null=True)
    passed_year2 = models.CharField(max_length=64, null=True)
    division_percentage2 = models.CharField(max_length=64, null=True)
    Bachelor = models.CharField(max_length=255,blank=True, null=True)
    passed_year3 = models.CharField(max_length=64,blank=True, null=True)
    division_percentage3 = models.CharField(max_length=64,blank=True, null=True)
    Masters = models.CharField(max_length=255,blank=True, null=True)
    passed_year4 = models.CharField(max_length=64,blank=True, null=True)
    division_percentage4 = models.CharField(max_length=64,blank=True, null=True)
    
    
    def __str__(self):
        return self.user
    
class Contacts(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{7,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    Name= models.CharField(max_length=100)
    Description = models.CharField(max_length=200, null=True,blank=True)
    Office_name=models.CharField(max_length=100)
    Address = models.CharField(max_length=100 )
    Mobile_no1=models.CharField(validators=[phone_regex], max_length=17, blank=True,null=True)
    Mobile_no2=models.CharField(validators=[phone_regex], max_length=17, blank=True,null=True)
    landline_no=models.CharField(validators=[phone_regex], max_length=17, blank=True,null=True)
    email=models.EmailField(null=True,blank=True)
    
    #phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    #phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list

# def UploadedFile(self, attname):
#     return 'E:/testsql/testsql/New Folder/%s' %self.id

def UploadedFile(instance, filename):
    return './{0}/{1}'.format(instance.dir,filename)



class Directory(models.Model):
    directory = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.directory

class Create_folder(models.Model):
    dir = models.ForeignKey(Directory,on_delete=models.CASCADE,null=True,blank=True)
    file = models.FileField(upload_to=UploadedFile, null=True,blank=True)

    # def __str__(self):
    #     return self.dir



class Rename(models.Model):
    destination = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.destination

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline


