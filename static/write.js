var userWrote = false;
//POST function
function submitWrite(writeData, writeURL) {
  var xmlhttp = new XMLHttpRequest();
  xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      console.log(this.responseText);
    } else {
      console.log("nothing");
    }
  };
  xmlhttp.open("POST", writeURL, true);
  xmlhttp.setRequestHeader("Content-Type", "application/json");
  xmlhttp.send(JSON.stringify(writeData));
  location.reload();
}

//user input textarea POST request
$("#text-area").keydown(function(e) {
  var key = e.which;
  if (key == 13) {
    var row1 = document.getElementById("text-area").value;
    var lineTotal = row1;
    theURL = "http://127.0.0.1:5000/writeto";
    console.log(`hello. ${lineTotal} is submitted`);
    writeData = {
      turn: "hilarious human",
      line: lineTotal
    };
    submitWrite(writeData, theURL);
  }
});

//user input turns into for generator's perfix POST Reuqest
function switchTurn() {
  console.log("clicked");
  var userInput = "shit";
  dataToSend = { prefix: userInput };
  theURL = "http://127.0.0.1:5000/generate";
  submitWrite(dataToSend, theURL);
}
