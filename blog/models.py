from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class AboutMe(models.Model):
    text = RichTextUploadingField()
    image = models.ImageField(upload_to="aboutme/", null=True, blank=True)

    def __str__(self):
        return "About Me"

class Media(models.Model):
    image = models.ImageField(upload_to="media/", null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.url


class Post(models.Model):
    title = RichTextUploadingField()
    description = RichTextUploadingField()

class Experience(models.Model):
    title = RichTextUploadingField()
    description = RichTextUploadingField()
    image = models.ImageField(upload_to="experience/", null=True, blank=True)

class Education(models.Model):
    title = RichTextUploadingField()
    description = RichTextUploadingField()
    image = models.ImageField(upload_to="education/", null=True, blank=True)


class Projects(models.Model):
    yutube_url = models.CharField(max_length=100)
    title = RichTextUploadingField()
    description = RichTextUploadingField()

