from django.db.models.fields import return_None
from django.shortcuts import render

from blog.models import AboutMe, Media, Experience, Education
from blog.models import Projects, Post
from django.db.models import F


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

def projects_view(request):
    projects = Projects.objects.all()
    medias = Media.objects.all()
    return render(request, 'projects.html', {'projects': projects, 'medias': medias})


def post_view(request):
    posts = Post.objects.all()
    medias = Media.objects.all()
    return render(request, 'post.html', {'posts': posts, 'medias': medias})


def post_detail(request, pk):
    post = Post.objects.filter(pk=pk).first()
    if not post:
        from django.http import Http404
        raise Http404("Post not found")

    # Increment view count once per visit (simple increment)
    post.views = F('views') + 1
    post.save(update_fields=['views'])
    # Refresh from db to get integer value
    post.refresh_from_db()

    # Track viewer if authenticated
    if request.user.is_authenticated:
        post.viewers.add(request.user)

    medias = Media.objects.all()
    return render(request, 'post_detail.html', {'post': post, 'medias': medias})
