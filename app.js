var express = require('express');
var app = express();
var path = require('path');
var server = require('http').createServer(app).listen(8080 , function(){
    console.log('Express server listening on port 8080!');
});
var io = require('socket.io').listen(server);

//Format 
app.get('/public', function(req, res){
    res.sendFile(__dirname+"/index.html");
});

app.get('/test', function(req, res){
    res.send("ok");
});




io.sockets.on('connection', function (socket) {
    socket.on('WTN', function (data) {
        io.sockets.emit("NTC" , data);
    });

    socket.on('CTN', function (data) {
        buzz = data;
        io.sockets.emit("NTW" , data);
    });

});

