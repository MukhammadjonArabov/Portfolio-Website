from django.urls import path
from blog import views

urlpatterns = [
    path("", views.about_me_view, name="about"),
    path('experience/', views.experience_view, name='experience'),
    path('education/', views.education_view, name='education'),
]
