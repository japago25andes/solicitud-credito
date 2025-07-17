from flask import Flask, request, jsonify
from datetime import datetime
import json
# Importar la librería del sistema de colas cuando se defina cuál usar

app = Flask(__name__)

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
    Función temporal para simular envío a cola
    Pendiente implementar la integración real con el sistema de colas
    """
    print("=== ENVIANDO A COLA ===")
    print(f"Datos: {json.dumps(datos, indent=2, default=str)}")
    print("=== ENVIADO EXITOSAMENTE ===")
        
    return True

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
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
