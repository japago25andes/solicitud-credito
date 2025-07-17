# API de Solicitud de Crédito

API Flask simple para recibir solicitudes de crédito y enviarlas a una cola de procesamiento.

## 🐳 Ejecutar con Docker (Recomendado)

### Prerequisitos
- Docker Desktop instalado y ejecutándose

### Iniciar aplicación
```bash
# Opción 1: Script automático (Windows)
run-docker.bat

# Opción 2: Comando directo
docker-compose up -d
```

### Detener aplicación
```bash
docker-compose down
```

## 🛠️ Instalación manual (Desarrollo)

Si prefieres ejecutar sin Docker:

1. Instalar dependencias:
```bash
pip install -r requirements.txt
```

2. Ejecutar la aplicación:
```bash
python app.py
```

## 📡 Endpoints

### POST /solicitud-credito
Recibe una solicitud de crédito con todos los campos requeridos.

**URL:** `http://localhost:5000/solicitud-credito`

### GET /health
Endpoint de salud del servicio.

**URL:** `http://localhost:5000/health`

## 🧪 Pruebas

### Usando PowerShell (Windows)
```powershell
$json = @'
{
  "nit": 123456789,
  "valor_solicitado": 100000000,
  "plazo": 12,
  "tasa": 1.5,
  "linea": "CONSUMO",
  "valor_cobros": 50000,
  "pagaduria": 1,
  "codeudor1": 987654321,
  "codeudor2": 0,
  "valor_cuota": 8500000,
  "completo": "S",
  "aprobado": "N",
  "detalle": "Solicitud en evaluacion",
  "devengado": 0,
  "deducido": 0,
  "fecha": "2025-07-16T10:30:00",
  "impreso": "N",
  "fecha_primer_pago": "2025-08-16T00:00:00",
  "forma_pago": 1,
  "frecuencia": 30,
  "usuario": "admin",
  "terminal": "TERM001",
  "cod_clase_garantia": 1,
  "valor": 100000000,
  "descripcion_garantia": "Hipoteca vivienda",
  "encargado_evaluar_garantia": "evaluador1",
  "tipo_sistema_amortizacion": 1,
  "cod_destino_credito": 101,
  "modalidad_cuota": "F",
  "numero_poliza": "POL123456",
  "tasa_seguro": 0.5,
  "cuota_administracion": 25000
}
'@

Invoke-RestMethod -Uri "http://localhost:5000/solicitud-credito" -Method POST -Body $json -ContentType "application/json"
```

### Usando cURL (Linux/Mac)
```bash
curl -X POST http://localhost:5000/solicitud-credito \
  -H "Content-Type: application/json" \
  -d @ejemplo_solicitud.json
```

### Usando Postman
1. **Método:** POST
2. **URL:** `http://localhost:5000/solicitud-credito`
3. **Headers:** `Content-Type: application/json`
4. **Body:** Raw JSON (usar el contenido de `ejemplo_solicitud.json`)

## ✅ Respuesta exitosa
```json
{
  "success": true,
  "message": "Solicitud de crédito recibida exitosamente",
  "timestamp": "2025-07-16T19:25:00.225926",
  "id_referencia": "SOL-20250716192500"
}
```

## 🔧 Arquitectura

### Sistema de colas
El sistema está preparado para integrar servicios de cola. Actualmente mockeado en la función `enviar_a_cola()`.

**Opciones futuras de implementación:**
- **RabbitMQ**: Para alta disponibilidad y confiabilidad
- **Redis**: Para simplicidad y velocidad  
- **AWS SQS**: Para arquitectura cloud

### Estructura del proyecto
```
solicitud-credito/
├── app.py                    # API principal
├── requirements.txt          # Dependencias
├── ejemplo_solicitud.json    # Datos de prueba
├── Dockerfile               # Imagen Docker
├── docker-compose.yml       # Orchestración
├── run-docker.bat          # Script de inicio
└── README.md               # Documentación
```

## 🐞 Troubleshooting

### Docker no inicia
```bash
# Verificar que Docker Desktop esté ejecutándose
docker version

# Si hay conflictos de contenedores
docker-compose down
docker system prune -f
```

### Puerto ocupado
```bash
# Cambiar puerto en docker-compose.yml
ports:
  - "5001:5000"  # Puerto host:contenedor
```
