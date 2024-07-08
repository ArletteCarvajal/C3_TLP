#xoxb-7384383188946-7384399429666-1pAe2rvuCqILq7acsgxHmaie
import os
import requests
from django.apps import apps
from django.db import models
from core.models import Registro_Produccion

def enviar_mensaje_slack(registro):
    url = 'https://slack.com/api/chat.postMessage'
    token = 'xoxb-7384383188946-7384399429666-1pAe2rvuCqILq7acsgxHmaie'  # Tu token de Slack
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    # Consulta para obtener el total almacenado de litros_produccion para el mismo producto y planta
    total_almacenado = Registro_Produccion.objects.filter(
        codigo_combustible__codigo_producto=registro.codigo_combustible.codigo_producto,
        codigo_combustible__nombre_planta=registro.codigo_combustible.nombre_planta
    ).exclude(pk=registro.pk).aggregate(total=models.Sum('litros_produccion'))['total'] or 0

    # Construir el mensaje a enviar a Slack
    mensaje = (
        f"{registro.fecha_produccion} {registro.hora_registro} "
        f"{registro.codigo_combustible.nombre_planta.codigo_planta} – Nuevo Registro de Producción – "
        f"{registro.codigo_combustible.codigo_producto} {registro.litros_produccion} litros registrados | "
        f"Total Almacenado: {total_almacenado} litros"
    )

    # Datos a enviar a Slack
    data = {
        'channel': '#ProductTracker',  # Nombre del canal donde se enviará el mensaje
        'text': mensaje  # Contenido del mensaje
    }

    # Enviar la solicitud POST a la API de Slack
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()  # Capturar errores de solicitud HTTP

    return response  # Devolver la respuesta de la solicitud a Slack
