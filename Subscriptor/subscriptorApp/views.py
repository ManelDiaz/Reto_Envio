import paho.mqtt.client as mqtt
from django.shortcuts import render
from django.utils.timezone import now
from django.views import View
from .models import MensajeRecibido
import os
import threading
import logging

# Configurar logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        logger.info("✅ Conectado exitosamente al broker MQTT")
        client.subscribe(topic="chat/mensaje", qos=1)
    else:
        logger.error(f"❌ Error al conectar con el broker, código: {rc}")


def on_message(client, userdata, message):
    mensaje_texto = message.payload.decode("utf-8")
    logger.info(f"📩 Mensaje recibido: {mensaje_texto}")

    try:
        MensajeRecibido.objects.create(texto=mensaje_texto, fecha_recepcion=now())
        logger.info("✅ Mensaje guardado en la base de datos")
    except Exception as e:
        logger.error(f"❌ Error guardando en la base de datos: {e}")


def recibir_mensajes():
    try:
        logger.info("🚀 Iniciando conexión MQTT...")

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

        logger.info("🔌 Intentando conectar con el broker...")
        client.connect(host="broker", port=8883)

        logger.info("📡 Iniciando loop para recibir mensajes")
        client.loop_forever()

    except Exception as e:
        logger.error(f"🚨 Error en recibir_mensajes(): {e}")


# Iniciar el hilo en segundo plano de forma segura
def iniciar_hilo_mqtt():
    hilo = threading.Thread(target=recibir_mensajes, daemon=True)
    hilo.start()
    logger.info("🟢 Hilo MQTT iniciado")


# Ejecutar solo si es el proceso principal de Django
if os.environ.get("RUN_MAIN") == "true":
    iniciar_hilo_mqtt()


# Vista para mostrar mensajes
class ListaMensajesView(View):
    def get(self, request):
        logger.info("📌 Vista GET solicitada")
        mensajes = MensajeRecibido.objects.order_by("fecha_recepcion")
        return render(request, "index.html", {"lista_mensajes": mensajes})
