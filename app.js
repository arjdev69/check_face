var express       = require('express.io'),
child = require('child_process');
app = express();
socket = require('socket.io').listen(app.listen(8245));

app.sensors = {};

app.use(express.static(__dirname + '/public'));
app.http().io();

socket.on('connect', function (client) {
  client.on('face_register', function(face){
    console.log("Servidor " + face);

  if(face == "Execute"){
    execute();
  }else{
    execute_();
  }
  client.broadcast.emit("face_register", face);
  });
});

function execute_(){
  var exec = child.exec;
  exec('python facy.py', function(err, stdout, stderr){
    if(err){
      console.log(err);
    }
  });
}

function execute(){
  var exec = child.exec;
  exec('python face.py', function(err, stdout, stderr){
    if(err){
      console.log(err);
    }
  });
}


console.log('Smart Home - C.I.A - 8245');