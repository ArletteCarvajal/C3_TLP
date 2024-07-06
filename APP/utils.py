import requests # biblioteca de python que simplifica la realización métodos y funcionalidades para interactuar con servicios web y apis utilizando los protocolos HTTP
from datetime import datetime
from .models import Plantas,  Registro_Produccion 

def mensaje_slack (registro):
    url = 'https://slack.com/api/chat.postMessage'
    headrs = {
        'Content-Type' : 'application/json',
        'Authorization' : 'Bearer YOUR_SLACK_BOT_TOKEN'
    }

mensaje = f"{datetime.now()} {Plantas.codigo} - Nuevo Registro de Produccion - { Registro_Produccion.codigo_combustible} {Registro_Produccion.litros_produccion }"