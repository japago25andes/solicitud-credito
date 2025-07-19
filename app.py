from flask import Flask, request, jsonify
from flask_cors import CORS
from google.cloud import tasks_v2
from datetime import datetime

import json
import logging
import os


app = Flask(__name__)
CORS(app, origins="*")

logging.basicConfig(level=logging.INFO)

@app.route('/solicitud-credito', methods=['POST'])
def recibir_solicitud_credito():
    """
    Endpoint para recibir datos de solicitud de crédito
    """
    try:
        # Obtener datos del request
        data = request.get_json()
        
        # Validar que se recibieron datos
        if not data:
            return jsonify({
                'success': False,
                'message': 'No se recibieron datos'
            }), 400
        
        # Estructurar los datos recibidos
        solicitud_credito = {
            'nit': data.get('nit'),
            'valor_solicitado': data.get('valor_solicitado'),
            'plazo': data.get('plazo'),
            'tasa': data.get('tasa'),
            'linea': data.get('linea'),
            'valor_cobros': data.get('valor_cobros'),
            'pagaduria': data.get('pagaduria'),
            'codeudor1': data.get('codeudor1'),
            'codeudor2': data.get('codeudor2'),
            'valor_cuota': data.get('valor_cuota'),
            'completo': data.get('completo'),
            'aprobado': data.get('aprobado'),
            'detalle': data.get('detalle'),
            'devengado': data.get('devengado'),
            'deducido': data.get('deducido'),
            'fecha': data.get('fecha'),
            'impreso': data.get('impreso'),
            'fecha_primer_pago': data.get('fecha_primer_pago'),
            'forma_pago': data.get('forma_pago'),
            'frecuencia': data.get('frecuencia'),
            'usuario': data.get('usuario'),
            'terminal': data.get('terminal'),
            'cod_clase_garantia': data.get('cod_clase_garantia'),
            'valor': data.get('valor'),
            'descripcion_garantia': data.get('descripcion_garantia'),
            'encargado_evaluar_garantia': data.get('encargado_evaluar_garantia'),
            'tipo_sistema_amortizacion': data.get('tipo_sistema_amortizacion'),
            'cod_destino_credito': data.get('cod_destino_credito'),
            'modalidad_cuota': data.get('modalidad_cuota'),
            'numero_poliza': data.get('numero_poliza'),
            'tasa_seguro': data.get('tasa_seguro'),
            'cuota_administracion': data.get('cuota_administracion'),
            'timestamp_recepcion': datetime.now().isoformat()
        }
        
        # Enviar a la cola de procesamiento
        # Nota: Por ahora está mockeado, hay que implementar el servicio real
        enviar_a_cola(solicitud_credito)
        
        # Respuesta exitosa
        return jsonify({
            'success': True,
            'message': 'Solicitud de crédito recibida exitosamente',
            'timestamp': datetime.now().isoformat(),
            'id_referencia': f"SOL-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error al procesar la solicitud: {str(e)}'
        }), 500

def enviar_a_cola(datos):
    """
    Envía el mensaje a una cola de Google Cloud Tasks
    """
    try:
        endpoint = os.environ.get('TASK_ENDPOINT')
        client = tasks_v2.CloudTasksClient()
        project = 'misw4301-g26'
        queue = 'credit-process-queue'
        location = 'us-central1'  # Endpoint that will process the task
        payload = json.dumps(datos)

        parent = client.queue_path(project, location, queue)

        task = {
            'http_request': {
                'http_method': tasks_v2.HttpMethod.POST,
                'url': endpoint,
                'headers': {'Content-Type': 'application/json'},
                'body': payload.encode()
            }
        }
        logging.info(f"=== ENVIANDO A COLA ===")
        logging.info(f"Datos: {json.dumps(datos, indent=2, default=str)}")
        response = client.create_task(parent=parent, task=task)
        logging.info(f"=== ENVIADO EXITOSAMENTE ===")
        return True
    except Exception as e:
        logging.error(f"Error al enviar a la cola: {str(e)}")
        return False

@app.route('/health', methods=['GET'])
def health_check():
    """
    Endpoint de salud del servicio
    """
    return jsonify({
        'status': 'OK',
        'service': 'Solicitud Credito API',
        'timestamp': datetime.now().isoformat()
    }), 200

if __name__ == '__main__':
    # Configuración para Docker y desarrollo
    port = int(os.environ.get('PORT', 5001))
    app.run(debug=False, host='0.0.0.0', port=port)
