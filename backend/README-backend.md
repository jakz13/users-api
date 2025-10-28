# Backend (Django) - Instrucciones rápidas

Requisitos:
- Docker y docker-compose

Pruebas locales con docker-compose:

1. Crear un archivo `.env` en la raíz con las variables SMTP necesarias (ejemplo):

```
SMTP_USERNAME=tu-email@gmail.com
SMTP_PASSWORD=tu-app-password
ADMIN_EMAIL=admin@example.com
```

2. Levantar servicios:

```bash
docker-compose up --build
```

3. Ejecutar migraciones (en otro terminal):

```bash
docker-compose exec users-api python manage.py migrate
```

4. Abrir frontend en desarrollo o usar `curl`/Postman para interactuar con `http://localhost:8000/api/users/`.

Notas:
- Las credenciales y secretos se deben gestionar con variables de entorno o Kubernetes Secrets en producción.
- Para producción configurar `DEBUG=False` y `ALLOWED_HOSTS` correctamente.
