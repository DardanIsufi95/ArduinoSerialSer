var express = require('express');
var app = express();
var path = require('path');
var server = require('http').createServer(app).listen(3000 , function(){
    console.log('Express server listening on port 3000!');
});
var io = require('socket.io').listen(server);

app.use('/public', express.static(path.join(__dirname, 'public')));


io.sockets.on('connection', function (socket) {
  console.log(socket);
  socket.on('data', function (data) {
    console.log(data);
    socket.emit('data', 'Hello Back');
  });
});