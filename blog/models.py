from django.db import models
from django.conf import settings
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
    image = models.ImageField(upload_to="posts/", null=True, blank=True)
    views = models.PositiveIntegerField(default=0)
    viewers = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='viewed_posts')

    def __str__(self):
        return getattr(self, 'title', 'Post')

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

