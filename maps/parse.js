var fs = require('fs');
fs.readFile("transposegeo.csv", 'utf8', function(err, data) {
  if (err) throw err;
  var splitup = data.split("\n");
  var blah = splitup.map(function(a) {
    return a.split(",");
  });
  var newArr = [];
  var numNtas = blah.length;
  /* var NTAObject = {
    id: "string",
    coords: [
      {lat: double, long, double}, ...
    ]
  }*/
  for (var i = 0; i < numNtas; i++) {
    var newNTA = {coords: []};
    var ntaArr = blah[i];
    newNTA.id = ntaArr[0];
    for (var j = 1; j < ntaArr.length; j+=2) {
      var long = ntaArr[j];
      var lat = ntaArr[j+1];
      if (long && lat) {
        newNTA.coords.push({lat: Number(lat), lng: Number(long)});
      }
    }
    newArr[i] = newNTA;
  }
  console.log(newArr[0].coords[2]);
  fs.writeFile('myjsonfile.json', JSON.stringify(newArr), 'utf8', function(a) {
    return;
  });
});
