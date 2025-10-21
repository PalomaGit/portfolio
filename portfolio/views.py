from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Project, Testimonial, BlogPost, ContactMessage, Skill, Service
from .forms import ContactForm


def single_page(request):
    """Página única con todas las secciones optimizada"""
    # Optimización: usar select_related y prefetch_related cuando sea posible
    featured_projects = Project.objects.filter(featured=True).order_by('-created_date')[:6]
    featured_testimonials = Testimonial.objects.filter(featured=True).order_by('-created_date')[:3]
    recent_posts = BlogPost.objects.filter(published=True).order_by('-created_date')[:3]
    skills = Skill.objects.all().order_by('category', 'order', 'name')
    services = Service.objects.all().order_by('order', 'title')
    
    # Handle contact form
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mensaje enviado correctamente. Te contactaré pronto.')
            return redirect('home')
    else:
        form = ContactForm()

    # Optimización: usar defaultdict para agrupar skills
    from collections import defaultdict
    skills_by_category = defaultdict(list)
    for skill in skills:
        category = skill.get_category_display()
        skills_by_category[category].append(skill)

    context = {
        'featured_projects': featured_projects,
        'featured_testimonials': featured_testimonials,
        'recent_posts': recent_posts,
        'skills': dict(skills_by_category),
        'services': services,
        'form': form,
    }
    return render(request, 'portfolio/single_page_futuristic.html', context)


def blog_detail(request, slug):
    """Detalle de un post del blog"""
    post = get_object_or_404(BlogPost, slug=slug, published=True)
    recent_posts = BlogPost.objects.filter(published=True).exclude(pk=post.pk).order_by('-created_date')[:3]
    
    context = {
        'post': post,
        'recent_posts': recent_posts,
    }
    return render(request, 'portfolio/blog_detail.html', context)