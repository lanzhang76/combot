currentURL = "http://127.0.0.1:5000/";

function changeColor(newColor) {
  var elem = document.getElementsByClassName("item");
  console.log("clicked");
}

function myFunction() {
  document.getElementById("demo").innerHTML = "Hello World";
}

function enable() {
  var elem = document.getElementById("startButton");
  console.log("clicked");
  //   httpGetAsync("http://127.0.0.1:5000/generate", function(response) {
  //     alert(response);
  //   });
}

function httpGetAsync(theUrl, callback) {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.onreadystatechange = function() {
    if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
      callback(xmlHttp.responseText);
  };
  xmlHttp.open("GET", theUrl, true); // true for asynchronous
  xmlHttp.send(null);
}

function httpPost(theUrl) {
  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
    // Call a function when the state changes.
    if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
      // Request finished. Do processing here.
    }
  };
  xhr.open("POST", "/server", true);
  xhr.send("foo=bar&lorem=ipsum");
}

httpGetAsync("http://127.0.0.1:5000/generate", function(response) {
  //alert(response["lines"]);
  console.log(response);
});
