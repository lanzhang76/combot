function httpGetAsync(theUrl, callback) {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.onreadystatechange = function() {
    if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
      callback(xmlHttp.responseText);
  };
  xmlHttp.open("GET", theUrl, true); // true for asynchronous
  xmlHttp.send(null);
}

// currentURL = "http://127.0.0.1:5000/generate";
// httpGetAsync(currentURL, function(response) {
//   //alert(response["lines"]);
//   console.log(response);
// });
// httpGetAsync("http://127.0.0.1:5000/generate", function(response) {
//   console.log(response);
//   location.reload();
// });
