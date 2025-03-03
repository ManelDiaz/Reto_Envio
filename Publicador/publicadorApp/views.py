import paho.mqtt.client as mqtt
from django.shortcuts import render, redirect
from django.views import View
from .forms import MensajeForm
import os
import ssl


def index(request):
    return render(request, 'index.html')

def enviar_por_mqtt(mensaje):
    print("Enviando mensaje")
    client = mqtt.Client()
    try:
        client.tls_set(
            ca_certs="/certs/publicador/ca.crt",
            certfile="/certs/publicador/cliente.crt",
            keyfile="/certs/publicador/cliente.key", 
            tls_version=mqtt.ssl.PROTOCOL_TLS
        )
        client.tls_insecure_set(True)
        client.connect("broker", 8883, 60)
        client.publish("chat/mensaje", mensaje)
        print("Mensaje enviado")
    except Exception as e:
        print(f"Error asl enviar mensaje: {e}")
    finally:
        client.disconnect()


class MensajeCreateView(View):
    def get(self, request):
        formulario = MensajeForm()
        print("el get")
        return render(request, "envio.html", {"formulario": formulario})

    def post(self, request):
        formulario = MensajeForm(data=request.POST)
        if formulario.is_valid():
            mensaje = formulario.cleaned_data['texto']
            enviar_por_mqtt(mensaje)
            formulario.save()
            return redirect("index")
        return render(request, "envio.html", {"formulario": formulario})
