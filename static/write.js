var userWrote = false;
var currentUserInput = "what up";

//POST function
function submitWrite(writeData, writeURL) {
  var xmlhttp = new XMLHttpRequest();
  xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      console.log(this.responseText);
      location.reload();
    } else {
      console.log("it's not ready yet");
    }
  };
  xmlhttp.open("POST", writeURL, true);
  xmlhttp.setRequestHeader("Content-Type", "application/json");
  xmlhttp.send(JSON.stringify(writeData));
}

function submitInput() {
  console.log("Enter pressed.");
  var row1 = document.getElementById("text-area").value;
  var lineTotal = row1;
  theURL = "http://127.0.0.1:5000/writeto";
  console.log(`hello. ${lineTotal} is submitted`);
  writeData = {
    turn: "hilarious human",
    line: lineTotal
  };
  currentUserInput = lineTotal;
  console.log(currentUserInput);
  submitWrite(writeData, theURL);
}

function submitGenerate(writeData, writeURL) {
  var xmlhttp = new XMLHttpRequest();
  xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("loadZone").style.display = "none";
      console.log(this.responseText);
      location.reload();
    } else {
      console.log("it's not ready yet");
      document.getElementById("loadZone").style.display = "block";
    }
  };
  xmlhttp.open("POST", writeURL, true);
  xmlhttp.setRequestHeader("Content-Type", "application/json");
  xmlhttp.send(JSON.stringify(writeData));
}

//user input turns into for generator's perfix POST Reuqest
function switchTurn() {
  console.log(currentUserInput);
  var userInput = currentUserInput;
  dataToSend = { prefix: userInput };
  theURL = "http://127.0.0.1:5000/generate";
  submitGenerate(dataToSend, theURL);
}

//KEY DOWN:
//user input textarea POST request
// $("text-area").keydown(function(e) {
//   var key = e.which;
//   if (key == 32) {
//     console.log("Enter pressed.");
//     var row1 = document.getElementById("text-area").value;
//     var lineTotal = row1;
//     theURL = "http://127.0.0.1:5000/writeto";
//     console.log(`hello. ${lineTotal} is submitted`);
//     writeData = {
//       turn: "hilarious human",
//       line: lineTotal
//     };
//     currentUserInput = lineTotal;
//     console.log(currentUserInput);
//     submitWrite(writeData, theURL);
//   } else {
//     console.log(typing);
//   }
// });
