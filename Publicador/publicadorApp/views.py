import paho.mqtt.client as mqtt
from django.shortcuts import render, redirect
from django.views import View
from .forms import MensajeForm
import ssl


def index(request):
    return render(request, 'index.html')


def enviar_por_mqtt(mensaje):
    cliente = mqtt.Client()
    try:
        cliente.tls_set(
            ca_certs="/certs/broker/ca.crt",
            certfile="/certs/publicador/publicador.crt",
            keyfile="/certs/publicador/publicador.key",
            tls_version=ssl.PROTOCOL_TLSv1_2
        )
        cliente.tls_insecure_set(True)
        cliente.connect("broker", 8883, 60)
        cliente.publish("chat/mensaje", mensaje)
        print("Mensaje enviado", flush=True)
    except Exception as e:
        print("Error: ", e, flush=True)
    finally:
        cliente.disconnect()


class MensajeCreateView(View):
    def get(self, request):
        formulario = MensajeForm()
        return render(request, "envio.html", {"formulario": formulario})

    def post(self, request):
        formulario = MensajeForm(data=request.POST)
        if formulario.is_valid():
            mensaje = formulario.cleaned_data['texto']
            enviar_por_mqtt(mensaje)
            formulario.save()
            return redirect("index")
        return render(request, "envio.html", {"formulario": formulario})
