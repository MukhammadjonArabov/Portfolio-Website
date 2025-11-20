from django.urls import path
from blog import views
from blog.views import about_me_view

urlpatterns = [
    path("", about_me_view, name="about"),
]