import os
import requests
from django.apps import apps
from django.db import models


def enviar_mensaje_slack(registro):
    url = 'https://slack.com/api/chat.postMessage'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer xoxb-7384383188946-7384399429666-1pAe2rvuCqILq7acsgxHmaie'  # Reemplaza con tu token de Slack válido
    }

    # Obtener el modelo Registro_Produccion desde la app core
    Registro_Produccion = apps.get_model('core', 'Registro_Produccion')

    # Consulta para obtener el total almacenado de litros_producidos para el mismo producto y planta
    total_almacenado = Registro_Produccion.objects.filter(
        producto__codigo=registro.producto.codigo,
        producto__planta=registro.producto.planta
    ).aggregate(total=models.Sum('litros_producidos'))['total'] or 0

    # Construir el mensaje a enviar a Slack
    mensaje = (
        f"{registro.fecha_produccion} {registro.hora_registro} "
        f"{registro.producto.planta.codigo} – Nuevo Registro de Producción – "
        f"{registro.producto.codigo} {registro.litros_producidos} litros registrados | "
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
