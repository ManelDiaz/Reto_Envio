import paho.mqtt.client as mqtt
from django.shortcuts import render, get_list_or_404
from django.utils.timezone import now
from django.views import View
from .models import MensajeRecibido
import os
import threading


def on_connect(client, userdata, flags, rc):
    print("Conectado al broker con código:", rc)
    client.subscribe(topic="chat/mensaje", qos=1)


def on_message(client, userdata, message):
    mensaje_texto = message.payload.decode("utf-8")
    MensajeRecibido.objects.create(texto=mensaje_texto, fecha_recepcion=now())


def recibir_mensajes():
    client = mqtt.Client(client_id="subscriptorApp", clean_session=False)
    client.tls_set(
        ca_certs="/certs/ca.crt",
        certfile="/certs/server.crt",
        keyfile="/certs/server.key",
        tls_version=mqtt.ssl.PROTOCOL_TLS
        
    )
    client.tls_insecure_set(True)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host="broker", port=8883)
    client.loop_forever()


threading.Thread(target=recibir_mensajes, daemon=True).start()


class ListaMensajesView(View):
    def get(self, request):
        mensajes = MensajeRecibido.objects.order_by("fecha_recepcion")
        return render(request, "index.html", {"lista_mensajes": mensajes})
