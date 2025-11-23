from django.urls import path
from blog import views

urlpatterns = [
    path("", views.about_me_view, name="about"),
    path('experience/', views.experience_view, name='experience'),
    path('education/', views.education_view, name='education'),
    path('projects/', views.projects_view, name='projects'),
    path('post/', views.post_view, name='post'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
