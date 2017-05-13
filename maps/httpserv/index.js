var express = require('express');
var cors = require('cors');
var app = express();
var path = require('path');
var foo = require('./public/myjsonfile.json');
app.use(cors);
// app.use(express.static(path.join(__dirname, 'public')));
app.get("/", function(req, res){
    res.json(foo);
});
app.listen(3000);

// function getJson(req, res, next){
//     res.send(foo);
// }
