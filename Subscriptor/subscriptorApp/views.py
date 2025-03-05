import paho.mqtt.client as mqtt
from django.shortcuts import render
from django.utils.timezone import now
from django.views import View
from .models import MensajeRecibido
import os
import threading
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe(topic="chat/mensaje", qos=1)
    else:
        logger.error("Error: ", rc)


def on_message(client, userdata, message):
    mensaje_texto = message.payload.decode("utf-8")

    try:
        MensajeRecibido.objects.create(texto=mensaje_texto, fecha_recepcion=now())
    except Exception as e:
        logger.error("Error: ", e)


def recibir_mensajes():
    try:
        client = mqtt.Client(client_id="subscriptorApp", clean_session=True)
        client.tls_set(
            ca_certs="/certs/broker/ca.crt",
            certfile="/certs/suscriptor/suscriptor.crt",
            keyfile="/certs/suscriptor/suscriptor.key",
            tls_version=mqtt.ssl.PROTOCOL_TLS
        )
        client.tls_insecure_set(True)
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect(host="broker", port=8883)
        client.loop_forever()
    except Exception as e:
        logger.error("Error: ", e)


class ListaMensajesView(View):
    def get(self, request):
        mensajes = MensajeRecibido.objects.order_by("fecha_recepcion")
        return render(request, "index.html", {"lista_mensajes": mensajes})


hilo = threading.Thread(target=recibir_mensajes, daemon=True)
hilo.start()
