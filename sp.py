<div class="wrapper">
  <h1>Stopwatch</h1>
  <p><span id="seconds">00</span></p>
  <button id="button-start">Start</button>
  <button id="button-stop">Stop</button>
  <button id="button-reset">Reset</button>
</div>
window.onload = function () {
  var seconds = 00;
  var milliseconds = 00;
  var appendMilliseconds = document.getElementById("milliseconds");
  var appendSeconds = document.getElementById("seconds");
  var buttonStart = document.getElementById("button-start");
  var buttonStop = document.getElementById("button-stop");
  var buttonReset = document.getElementById("button-reset");
  var Interval;
  
  buttonStart.onclick = function() {
    clearInterval(Interval);
    milliseconds
  }
}
