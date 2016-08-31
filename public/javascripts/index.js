var socket = io.connect();

socket.on('connect', function(data) {
  console.log("Conectado");
});

function send_Fr(){
  socket.emit('face_register', "Execute");
}

function send_Fr_(){
  socket.emit('face_register', "Exec");
}