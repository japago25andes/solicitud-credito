@echo off
echo ============================
echo  Solicitud Credito API
echo ============================

REM Verificar Docker
docker version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Docker Desktop no está ejecutándose
    echo Por favor iniciar Docker Desktop primero
    pause
    exit /b 1
)

echo Limpiando contenedores previos...
docker stop solicitud-credito-api >nul 2>&1
docker rm solicitud-credito-api >nul 2>&1
docker-compose down >nul 2>&1

echo Iniciando aplicación...
docker-compose up -d

if %errorlevel% equ 0 (
    echo.
    echo ✅ API ejecutándose en: http://localhost:5000
    echo 🏥 Health check: http://localhost:5000/health
    echo.
    echo Para detener: docker-compose down
) else (
    echo ERROR: Falló el inicio
)

pause
