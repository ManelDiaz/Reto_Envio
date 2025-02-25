from django.db import models

class MensajeRecibido(models.Model):
    texto = models.TextField()
    fecha_recepcion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.texto[:50]
