from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
    

class Course(models.Model):
    owner = models.ForeignKey(User,related_name= 'courses_created', on_delete=models.CASCADE) # The creator of the course
    subject = models.ForeignKey(Subject,related_name='courses', on_delete=models.CASCADE) # The subject the course belongs to
    title = models.CharField(max_length=200) # course title
    slug = models.SlugField(max_length=200, unique=True) # title slug
    overview = models.TextField() # Overview of the course
    created = models.DateTimeField(auto_now_add=True) # When it is created

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
    

class Module(models.Model):
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title