from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

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
    

class Content(models.Model):
    module = models.ForeignKey(Module, related_name='contents', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE) # A ForeignKey field to the ContentType model.
    object_id = models.PositiveIntegerField()# A PositiveIntegerField to store the primary key of the related object.
    item = GenericForeignKey('content_type', 'object_id') # A GenericForeignKey field to the related object combining the two previous fields.


class ItemBase(models.Model):
    owner = models.ForeignKey(User, related_name='%(class)s_related', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title
    

class Text(ItemBase):
    content = models.TextField()

class File(ItemBase):
    file = models.FileField(upload_to='files')

class Image(ItemBase):
    file = models.FileField(upload_to='images')

class Video(ItemBase):
    url = models.URLField()