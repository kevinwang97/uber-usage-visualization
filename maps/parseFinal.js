var fs = require('fs');
fs.readFile("final.csv", 'utf8', function(err, data) {
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
  for (var i = 1; i < numNtas; i++) {
    var ntaData = blah[i];
    var newNTA = {borough: ntaData[0], nta_id: ntaData[1], metric: Number(ntaData[2])};
    newArr[i-1] = newNTA;
  }
  fs.writeFile('uber.json', JSON.stringify(newArr), 'utf8', function(a) {
    return;
  });
});
