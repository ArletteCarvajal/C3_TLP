import requests # biblioteca de python que simplifica la realización métodos y funcionalidades para interactuar con servicios web y apis utilizando los protocolos HTTP
from datetime import datetime
from .models import Plantas,  Registro_Produccion 

def enviar_mensaje_slack(registro):
    url = 'https://slack.com/api/chat.postMessage'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer xoxb-7384383188946-7384399429666-1pAe2rvuCqILq7acsgxHmaie'
    }
    mensaje = f"{datetime.now()} {registro.producto.planta.codigo} – Nuevo Registro de Producción – {registro.producto.codigo} {registro.litros_producidos} litros registrados | Total Almacenado: CALCULA_TOTAL_ALMACENADO"
    data = {
        'channel': '#ProductTracker',
        'text': mensaje
    }
    response = requests.post(url, headers=headers, json=data)
    return response