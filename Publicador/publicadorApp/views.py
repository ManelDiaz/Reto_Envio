import paho.mqtt.client as mqtt
from django.shortcuts import render, redirect
from django.views import View
from .forms import MensajeForm
import os


def enviar_por_mqtt(mensaje):
    client = mqtt.Client()
    client.connect("broker", 1883, 60)
    client.publish("chat/mensaje", mensaje)
    print("Mensaje enviado")
    client.disconnect()


class MensajeCreateView(View):
    def get(self, request):
        formulario = MensajeForm()
        print("el get")
        return render(request, "index.html", {"formulario": formulario})

    def post(self, request):
        formulario = MensajeForm(data=request.POST)
        if formulario.is_valid():
            mensaje = formulario.cleaned_data['texto']
            enviar_por_mqtt(mensaje)
            return redirect("index")
        return render(request, "index.html", {"formulario": formulario})
