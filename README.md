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

## 📦 Instalación y Configuración

### 1. Clonar el Repositorio
```bash
git clone https://github.com/PalomaGit/portfolio.git
cd portfolio
```

### 2. Crear Entorno Virtual
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar Variables de Entorno
Copia el archivo `.env.example` y renómbralo a `.env`:
```bash
cp .env.example .env
```

Edita el archivo `.env` y configura las variables necesarias. Para desarrollo local, el archivo ya viene con valores por defecto que funcionan. **Importante**: Genera una nueva `SECRET_KEY` para producción usando:
```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

### 5. Aplicar Migraciones
```bash
python manage.py migrate
```

### 6. Crear Superusuario (Opcional)
```bash
python manage.py createsuperuser
```

### 7. Ejecutar el Servidor
```bash
python manage.py runserver
```

El sitio estará disponible en `http://localhost:8000`

## 👤 Autor

**Paloma Ocaña Piña**
- LinkedIn: [Paloma Ocaña Piña](https://www.linkedin.com/in/paloma-oca%C3%B1a-pi%C3%B1a/)
- GitHub: [@PalomaGit](https://github.com/PalomaGit/)
- Email: palomaopina4c@gmail.com

## 🙏 Agradecimientos a
- Django Community
- Bootstrap Team
- Font Awesome
- AOS Library
- Docker Community
- Luis, por inspirarme profundamente a cada día.