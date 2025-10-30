from django.db import models

# (backend)
class User(models.Model):
    name = models.CharField(max_length=100)      # ← Frontend: "nombre"
    email = models.EmailField(unique=True)       # ← Frontend: "email"
    phone = models.CharField(max_length=20)      # ← Frontend: "telefono"
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
