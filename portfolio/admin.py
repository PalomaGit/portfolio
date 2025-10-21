from django.contrib import admin
from .models import Project, Testimonial, BlogPost, ContactMessage, Skill, Service


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_date', 'featured']
    list_filter = ['featured', 'created_date']
    search_fields = ['title', 'description']
    list_editable = ['featured']


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'created_date', 'featured']
    list_filter = ['featured', 'created_date']
    search_fields = ['name', 'company', 'content']
    list_editable = ['featured']


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_date', 'published']
    list_filter = ['published', 'created_date']
    search_fields = ['title', 'content']
    list_editable = ['published']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_date', 'read']
    list_filter = ['read', 'created_date']
    search_fields = ['name', 'email', 'subject']
    list_editable = ['read']
    readonly_fields = ['created_date']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'order']
    list_filter = ['category']
    search_fields = ['name']
    list_editable = ['proficiency', 'order']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    search_fields = ['title', 'description']
    list_editable = ['order']