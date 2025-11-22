from django.db.models.fields import return_None
from django.shortcuts import render

from blog.models import AboutMe, Media, Experience, Education


def about_me_view(request):
    about = AboutMe.objects.first()
    medias = Media.objects.all()
    return render(request, 'about_me.html', {'about': about, 'medias': medias})

def experience_view(request):
    experiences = Experience.objects.all()
    medias = Media.objects.all() 
    return render(request, 'experience.html', {'experiences': experiences, 'medias': medias})

def education_view(request):
    educations = Education.objects.all()
    medias = Media.objects.all()  # footer uchun
    return render(request, 'education.html', {'educations': educations, 'medias': medias})
