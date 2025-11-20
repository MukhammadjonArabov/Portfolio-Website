from django.db.models.fields import return_None
from django.shortcuts import render

from blog.models import AboutMe, Media


def about_me_view(request):
    about = AboutMe.objects.first()
    medias = Media.objects.all()
    return render(request, 'about_me.html', {'about': about, 'medias': medias})
