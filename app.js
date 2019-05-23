var express = require('express');
var app = express();
var path = require('path');
var server = require('http').createServer(app).listen(3000 , function(){
    console.log('Express server listening on port 3000!');
});
var io = require('socket.io').listen(server);

//Format 
app.get('/public', function(req, res){
    res.sendFile(__dirname+"/index.html");
});




io.sockets.on('connection', function (socket) {
//   socket.on('sensors', function (data) {
//     socket.emit('data', 'Im Node');
//   });

    socket.on('WTN', function (data) {
        io.sockets.emit("NTC" , data);
    });

    socket.on('CTN', function (data) {
        buzz = data;
        io.sockets.emit("NTW" , data);
    });

});

