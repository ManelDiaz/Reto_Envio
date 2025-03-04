import paho.mqtt.client as mqtt
from django.shortcuts import render, redirect
from django.views import View
from .forms import MensajeForm
import os
import ssl


def index(request):
    return render(request, 'index.html')


def enviar_por_mqtt(mensaje):
    print("Enviando mensaje", flush=True)
    client = mqtt.Client()
    try:
        print("Configurando TLS...", flush=True)
        client.tls_set(
            ca_certs="/certs/broker/ca.crt",
            certfile="/certs/publicador/publicador.crt",
            keyfile="/certs/publicador/publicador.key",
            tls_version = ssl.PROTOCOL_TLSv1_2
        )
        print("TLS configurado", flush=True)

        client.tls_insecure_set(True)

        print("Conectando al broker...", flush=True)
        client.connect("broker", 8883, 60)

        print("Publicando mensaje...", flush=True)
        client.publish("chat/mensaje", mensaje)

        print("Mensaje enviado", flush=True)
    except Exception as e:
        print(f"❌ Error al enviar mensaje: {e}", flush=True)
    finally:
        client.disconnect()


class MensajeCreateView(View):
    def get(self, request):
        formulario = MensajeForm()
        print("el get", flush=True)
        return render(request, "envio.html", {"formulario": formulario})

    def post(self, request):
        formulario = MensajeForm(data=request.POST)
        if formulario.is_valid():
            mensaje = formulario.cleaned_data['texto']
            enviar_por_mqtt(mensaje)
            formulario.save()
            return redirect("index")
        return render(request, "envio.html", {"formulario": formulario})
