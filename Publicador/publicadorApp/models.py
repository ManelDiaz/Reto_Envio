from django.db import models

class Mensaje(models.Model):
    texto = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.texto[:50]
