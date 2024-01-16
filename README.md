# FastAPI WebSocket Chat Application

## Descripción

Este proyecto es una aplicación de chat simple desarrollada con FastAPI, utilizando WebSockets para la comunicación en tiempo real. Permite a los usuarios unirse a distintos grupos de chat y enviar mensajes dentro de estos grupos. Además, los usuarios pueden ver el grupo al que están actualmente conectados y tienen la opción de cambiar de grupo o salir de la sala de chat.

## Características

- Conexión a diferentes grupos de chat a través de WebSockets.
- Envío y recepción de mensajes en tiempo real.
- Interfaz de usuario para seleccionar el grupo de chat.
- Visualización del grupo de chat actual.
- Funcionalidad para salir del grupo de chat.

## Tecnologías Utilizadas

- **FastAPI**: Para el backend y manejo de WebSockets.
- **HTML y JavaScript**: Para la interfaz de usuario en el frontend.

## Requisitos

- Python 3.6+
- FastAPI
- Uvicorn (para ejecutar el servidor FastAPI)

## Instalación y Ejecución

1. **Clonar el Repositorio**

   ```bash
   git clone [URL del repositorio]
   cd [nombre del directorio del repositorio]
   ```

2. **Instalar Dependencias**

   ```bash
   pip install fastapi uvicorn websockets
   ```

3. **Ejecutar el Servidor FastAPI**

   ```bash
   uvicorn main:app --reload
   ```
