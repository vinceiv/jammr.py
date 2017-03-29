var express = require('express');
var app = express();

app.use(express.static('public'));
app.use(express.static('public/images'));

app.get('/', function (req, res) {
  res.sendFile( __dirname + "/" + "index.html" );
})

app.get('/index.html', function (req, res) {
   res.sendFile( __dirname + "/" + "index.html" );
})

app.get('/images/up.gif', function (req, res) {
  res.sendfile( __dirname + "/images/up.gif" );
})
var server = app.listen(2345, function () {
   var host = server.address().address
   var port = server.address().port

   console.log("Example app listening at http://%s:%s", host, port)
})
