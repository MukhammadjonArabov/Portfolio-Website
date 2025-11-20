from django.contrib import admin
from .models import (
    AboutMe,
    Media,
    Post,
    Experience,
    Education,
    Projects
)
from django.utils.html import format_html


# -------------------
# About Me
# -------------------
@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ("text", "image_preview")

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" height="60" />', obj.image.url)
        return "No Image"


# -------------------
# Media
# -------------------
@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ("url", "image_preview")

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" height="60" />', obj.image.url)
        return "No Image"

    image_preview.short_description = "Preview"


# -------------------
# Post
# -------------------
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("short_title",)

    def short_title(self, obj):
        return obj.title[:50]

    short_title.short_description = "Title"


# -------------------
# Experience
# -------------------
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("short_title", "image_preview")

    def short_title(self, obj):
        return obj.title[:50]

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" height="60" />', obj.image.url)
        return "No Image"

    image_preview.short_description = "Preview"


# -------------------
# Education
# -------------------
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("short_title", "image_preview")

    def short_title(self, obj):
        return obj.title[:50]

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" height="60" />', obj.image.url)
        return "No Image"

    image_preview.short_description = "Preview"


# -------------------
# Projects
# -------------------
@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ("yutube_url", "short_title")

    def short_title(self, obj):
        return obj.title[:50]

    short_title.short_description = "Title"
