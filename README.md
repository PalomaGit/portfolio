# 🚀 Portfolio Profesional - Paloma Ocaña Piña

Mi portfolio profesional (desarrollado con Django) que funciona como mi escaparate digital y CV.

## 🌐 **Demo en Vivo**

### **🚀 Acceso Directo**
**👉 [Ver Portfolio Estático](https://palomagit.github.io/portfolio/)**

### **📱 Previsualización en README**
[![Portfolio Preview](https://img.shields.io/badge/Portfolio-Live-brightgreen?style=for-the-badge&logo=github)](https://palomagit.github.io/portfolio/)
[![Django](https://img.shields.io/badge/Django-5.2.7-green?style=for-the-badge&logo=django)](https://palomagit.github.io/portfolio/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue?style=for-the-badge&logo=docker)](https://palomagit.github.io/portfolio/)
[![Responsive](https://img.shields.io/badge/Responsive-Design-purple?style=for-the-badge&logo=css3)](https://palomagit.github.io/portfolio/)

### **🎯 URLs Disponibles**
- 🔗 **GitHub Pages**: https://palomagit.github.io/portfolio/
- 🐳 **Docker Local**: http://localhost:8000
- 📦 **Repositorio**: https://github.com/PalomaGit/portfolio

## 🚀 Instalación y Uso

### **🐳 Con Docker (Recomendado)**

El portfolio está completamente configurado para funcionar con Docker. Solo necesitas clonar y ejecutar:

```bash
# 1. Clonar el repositorio
git clone https://github.com/PalomaGit/portfolio.git
cd portfolio

# 2. Construir y ejecutar con Docker Compose
docker-compose up --build

# 3. ¡Listo! El sitio estará disponible en:
# 🌐 http://localhost:8000
# 👤 Panel admin: http://localhost:8000/admin/ (admin/admin123)
```

**✨ Lo que incluye automáticamente:**
- ✅ Migraciones de base de datos
- ✅ Archivos estáticos recopilados
- ✅ Superusuario creado (admin/admin123)
- ✅ Datos de ejemplo (proyectos, artículos, habilidades)
- ✅ Configuración completa lista para usar

### **📦 Instalación Manual (Sin Docker)**

```bash
# 1. Clonar el repositorio
git clone https://github.com/PalomaGit/portfolio.git
cd portfolio

# 2. Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar script de inicialización
chmod +x init_portfolio.sh
./init_portfolio.sh

# 5. Ejecutar servidor
python manage.py runserver

# 6. Acceder a:
# 🌐 http://localhost:8000
# 👤 Panel admin: http://localhost:8000/admin/ (admin/admin123)
```

## ✨ Características Principales

- **Diseño Futurista**: Interfaz moderna con efectos visuales avanzados (Matrix Rain, glitch effects, animaciones AOS)
- **Página Única**: Experiencia de scroll suave con navegación dinámica
- **Responsive**: Adaptable a todos los dispositivos
- **Contenido Dinámico**: Gestión de contenido a través del panel de administración
- **Formulario de Contacto**: Sistema de mensajes integrado
- **Optimizado**: Código limpio y eficiente con mejores prácticas

## 🛠️ Tecnologías Utilizadas

- **Backend**: Django 5.2.7
- **Base de Datos**: SQLite
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Contenedores**: Docker & Docker Compose
- **Iconos**: Font Awesome
- **Fuentes**: Google Fonts (Inter)
- **Animaciones**: AOS (Animate On Scroll)

## 📁 Estructura del Proyecto

```
portfolio/
├── portfolio_site/          # Configuración principal de Django
├── portfolio/               # Aplicación principal
│   ├── models.py           # Modelos de datos optimizados
│   ├── views.py            # Vistas simplificadas
│   ├── urls.py             # Rutas mínimas necesarias
│   ├── admin.py            # Panel de administración
│   └── templates/          # Plantillas HTML
├── static/                  # Archivos estáticos
├── media/                   # Archivos multimedia (CV, imágenes)
├── Dockerfile              # Imagen Docker optimizada con seguridad
├── docker-compose.yml      # Orquestación de servicios
└── requirements.txt        # Dependencias Python mínimas
```

## 📱 Secciones del Portfolio

### 🏠 Inicio
- Presentación personal con efectos visuales
- Información de contacto
- Enlaces a redes sociales (LinkedIn, GitHub)

### 👨‍💻 Sobre Mí
- Biografía profesional
- Educación y experiencia
- Habilidades técnicas organizadas por categorías

### 🛠️ Habilidades
- **Frontend**: HTML, CSS, JavaScript, TypeScript, Angular, Bootstrap, Tailwind
- **Backend**: Java, Node.js, PHP
- **Base de Datos**: MySQL, PostgreSQL, MongoDB, SQL Server
- **Herramientas**: Git/GitHub, Docker, Apache, UML, JUnit, Scrum, Kanban, Cursor

### 🚀 Servicios
- Desarrollo Web Full-Stack
- Aplicaciones Web Personalizadas
- Consultoría Técnica
- Optimización de Rendimiento

### 💼 Proyectos
- Portfolio de trabajos realizados
- Enlaces a GitHub y demos en vivo
- Tecnologías utilizadas en cada proyecto

### 💬 Testimonios
- Reseñas de clientes y colegas
- Casos de éxito

### 📝 Blog
- Artículos sobre desarrollo web
- Mejores prácticas
- Tutoriales técnicos

### 📄 Currículum
- Descarga directa del CV en PDF
- Información profesional completa

### 📞 Contacto
- Formulario de contacto funcional
- Información de contacto
- Enlaces a redes sociales

## 🎨 Características del Diseño

### Efectos Visuales
- **Matrix Rain**: Lluvia de caracteres en el fondo
- **Glitch Effects**: Efectos de distorsión en títulos
- **Animaciones AOS**: Efectos de entrada suaves
- **Gradientes**: Colores futuristas y neón
- **Glassmorphism**: Efectos de cristal en elementos


## 🔧 Optimizaciones Implementadas

### Backend
- **Vistas optimizadas**: Solo funciones necesarias, eliminación de código redundante
- **Consultas eficientes**: Uso de `order_by`, `select_related` y `prefetch_related`
- **Modelos mejorados**: Métodos útiles añadidos (`get_technologies_list`, `get_proficiency_display`)
- **URLs simplificadas**: Solo rutas esenciales (home y blog_detail)
- **Slug automático**: Generación automática de slugs para blog posts

### Frontend
- **CSS optimizado**: Variables CSS para consistencia
- **JavaScript eficiente**: Efectos suaves y responsivos
- **Imágenes optimizadas**: Compresión y formatos adecuados
- **Enlaces reales**: LinkedIn y GitHub conectados

### Docker
- **Imagen optimizada**: Usuario no-root para seguridad
- **Health checks**: Monitoreo de estado del contenedor
- **Dependencias mínimas**: Solo paquetes necesarios
- **Seguridad mejorada**: Permisos de usuario restringidos

## 📊 Funcionalidades Técnicas

### Panel de Administración
- Gestión completa de contenido
- Interfaz intuitiva para administradores
- Validación de datos integrada
- Nombres en español para mejor UX

### Formulario de Contacto
- Validación en frontend y backend
- Mensajes de confirmación
- Almacenamiento en base de datos

### Responsive Design
- Adaptable a móviles, tablets y desktop
- Navegación optimizada para touch
- Imágenes responsivas

### GitHub Pages
- **Hosting gratuito**: Versión estática disponible en GitHub Pages
- **URL personalizada**: https://palomagit.github.io/portfolio/
- **CDN global**: Carga rápida desde cualquier ubicación
- **HTTPS automático**: Certificado SSL incluido


## 📈 Próximas Mejoras

- [ ] Sistema de comentarios en blog
- [ ] Integración con APIs externas
- [ ] Sistema de notificaciones
- [ ] Analytics integrado
- [ ] PWA (Progressive Web App)
- [ ] Internacionalización (i18n)

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👤 Autor

**Paloma Ocaña Piña**
- LinkedIn: [Paloma Ocaña Piña](https://www.linkedin.com/in/paloma-oca%C3%B1a-pi%C3%B1a/)
- GitHub: [@PalomaGit](https://github.com/PalomaGit/)
- Email: palomaopina4c@gmail.com

## 🙏 Agradecimientos
- Django Community
- Bootstrap Team
- Font Awesome
- AOS Library
- Docker Community
