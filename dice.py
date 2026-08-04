<div>Click on the dice...</div>
<div id="dice" onclick="stopStart()"></div>
body {
  text-align: center;
  font-family: Helvetica, sans-serif;
}

#dice {
  font-size: 320px;
}

#dice:hover {
  cursor: pointer;
}
var dices = ['&#9856;', '&#9858;', '&#9859;', '&#9860;', '&#9861;'];
var stopped = true;

function change() {
  var random = Math.floor(Math.random() * 6);
  dice.innerHTML =dices[random];
}

function stopStart() {
  if (stopped) {
    stopped = false
    t = setInterval(change, 100);
  }else{
    clearInterval(t);
    stopped = true;
  }
}

window.onload = function() {
  dice = document.getElementById("dice");
  stopStart();
}