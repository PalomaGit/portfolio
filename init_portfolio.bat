@echo off
REM Script de inicialización para Windows

echo 🚀 Iniciando Portfolio de Paloma...

REM Ejecutar migraciones
echo 📊 Ejecutando migraciones de base de datos...
python manage.py migrate

REM Recopilar archivos estáticos
echo 🎨 Recopilando archivos estáticos...
python manage.py collectstatic --noinput

REM Crear superusuario si no existe
echo 👤 Verificando superusuario...
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin123') if not User.objects.filter(username='admin').exists() else print('Superusuario ya existe')"

echo ✅ ¡Portfolio de Paloma listo!
echo 🌐 Accede a http://localhost:8000 para ver el sitio
echo 👤 Panel admin: http://localhost:8000/admin/ (admin/admin123)
