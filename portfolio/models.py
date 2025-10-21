from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    technologies = models.CharField(max_length=500, help_text="Comma-separated list of technologies used")
    github_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    featured = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_date']
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
    
    def __str__(self):
        return self.title
    
    def get_technologies_list(self):
        """Retorna las tecnologías como lista"""
        return [tech.strip() for tech in self.technologies.split(',') if tech.strip()]
    
    def has_links(self):
        """Verifica si el proyecto tiene enlaces"""
        return bool(self.github_url or self.live_url)


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    featured = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return f"{self.name} - {self.company}"


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    excerpt = models.TextField(max_length=500)
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_date']
        verbose_name = 'Post del Blog'
        verbose_name_plural = 'Posts del Blog'
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return f"{self.name} - {self.subject}"


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('database', 'Database'),
        ('tools', 'Tools'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    proficiency = models.IntegerField(default=50, help_text="Proficiency level from 0 to 100")
    icon = models.CharField(max_length=100, blank=True, null=True, help_text="CSS class for icon")
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['category', 'order', 'name']
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'
    
    def __str__(self):
        return self.name
    
    def get_proficiency_display(self):
        """Retorna el nivel de competencia como texto"""
        if self.proficiency >= 90:
            return "Experto"
        elif self.proficiency >= 70:
            return "Avanzado"
        elif self.proficiency >= 50:
            return "Intermedio"
        else:
            return "Básico"
    
    def get_proficiency_color(self):
        """Retorna el color CSS basado en el nivel de competencia"""
        if self.proficiency >= 90:
            return "var(--primary-color)"
        elif self.proficiency >= 70:
            return "var(--secondary-color)"
        elif self.proficiency >= 50:
            return "var(--accent-color)"
        else:
            return "#666"


class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=100, help_text="CSS class for icon")
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order', 'title']
    
    def __str__(self):
        return self.title