// URL del WebSocket (reemplázala con la URL de tu servidor WebSocket)
const socketUrl = 'ws://localhost:3054/endpoint-del-socket'; //Cambiar localhost por tu ip si esto se corre en otra máquina

// Inicialización del WebSocket
const socket = new WebSocket(socketUrl);

// Manejo del evento `onopen` cuando se abre la conexión
socket.onopen = function(event) {
    console.log('Conexión establecida con el servidor WebSocket.');
};

// Manejo del evento `onmessage` cuando se recibe un mensaje
socket.onmessage = function(event) {
    console.log('Mensaje recibido del servidor:', event.data);
};

// Manejo del evento `onerror` cuando ocurre un error
socket.onerror = function(event) {
    console.error('Error en la conexión WebSocket:', event);
};

// Manejo del evento `onclose` cuando se cierra la conexión
socket.onclose = function(event) {
    console.log('Conexión WebSocket cerrada. Código de cierre:', event.code, 'Razón:', event.reason);
};

// Función para enviar un mensaje al servidor:
// Esto solo es un ejemplo, lo importante es que socket.send envía lo que le pases hacia el servidor 
// al que estamos conectados, además socket.readyState nos sirve para verificar si la conexión está
// abierta o no.

function sendMessage(message) {
    if (socket.readyState === WebSocket.OPEN) { // Acá verificamos si la conexión está abierta, para poder enviar
        socket.send(message); // Podrías usar socket.send en cualquier parte del código que lo desees
        console.log('Mensaje enviado al servidor:', message);
    } else {
        console.warn('No se puede enviar el mensaje. El WebSocket no está abierto.');
    }
}

// Ejemplo de uso: enviar un mensaje después de 2 segundos
setTimeout(() => {
    sendMessage('Hola, servidor!');
}, 2000);
