from fastapi import FastAPI, WebSocket, WebSocketDisconnect #Recuerda haber hecho pip install de fastapi y uvicorn
import logging #Opcional

# Logging es una forma de imprimir mensajes de debug, info o error más elegante y versátil que print
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Set para guardar las conexiones entrantes (Opcional)
websocket_connections = set()


@app.websocket("/endpoint-del-socket")
async def websocket_endpoint(websocket: WebSocket):
    try:
        # Aceptar la conexión WebSocket
        await websocket.accept()
        logger.info("Conexión WebSocket aceptada.")

        # Agregar la conexión WebSocket a la lista general
        websocket_connections.add(websocket)

        while True:
            try:
                # Esperar un mensaje del cliente
                data = await websocket.receive_text()
                logger.info(f"Mensaje recibido: {data}")

                # Opcional: Enviar una respuesta al cliente
                await websocket.send_text(f"Mensaje recibido: {data}")

            except WebSocketDisconnect:
                logger.info("Cliente desconectado.")
                break
            except Exception as e:
                logger.error(f"Error en la recepción del mensaje: {e}")
                await websocket.close()
                break

    except Exception as e:
        logger.error(f"Error en la conexión WebSocket: {e}")
        await websocket.close()
    finally:
        if websocket in websocket_connections:
            websocket_connections.remove(websocket)
            logger.info("Conexión WebSocket eliminada del conjunto")

# A continuación se sirve el html, esto no tiene que ver con los websocket, simplemente es el endpoint que sirve la página

from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

# Monta el directorio actual (.) para servir archivos estáticos, en este caso para servir scripts.js
app.mount("/", StaticFiles(directory=".", html=True), name="static")

# Ruta para la página principal (index.html)
@app.get("/", response_class=FileResponse)
async def read_root():
    return "index.html"