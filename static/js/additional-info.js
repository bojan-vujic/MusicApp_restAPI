
var x = 0;
var y = 0;
document.addEventListener('mousemove', onMouseMove, false);
function onMouseMove(e){x = e.clientX; y = e.clientY};
function getX() {return x};
function getY() {return y};

var windowX = window.innerWidth;
var windowY = window.innerHeight;

var elems = document.getElementsByClassName('info-icon-btn');
var titles = document.getElementsByClassName('title-span');

for (let el of elems) {
  el.addEventListener('click', () => {
    var info = el.getElementsByClassName("title-span")[0];
    var mouseX = getX();
    var mouseY = getY();
    pulse(mouseX, mouseY);
    for (let elm of titles) {elm.style.transform = 'scale(0)'};
    showElement(info, mouseX, mouseY, windowX);
  });
};


function showElement(info, mouseX, mouseY, windowX) {
  var width  = info.offsetWidth;

  // apply some styling to an element
  info.style.position = 'fixed';
  info.style.top      = mouseY + 15 + 'px';

  if (mouseX < windowX/2){
    mouseX < (width/2 - 5)
    ? info.style.left = '5px'
    : info.style.left = mouseX - width/2 + 'px';
  } else {
    mouseX + width/2 < (windowX + 10)
    ? info.style.left = mouseX - width/2 + 'px'
    : info.style.left = windowX - width - 10 + 'px';
  }

  info.style.transform = 'scale(0.9)';
  setTimeout(() => {info.style.transform = 'scale(0)'}, 3700);
};

function pulse(x, y) {
  let puls = document.createElement('div');
  document.querySelector('#iframe-info').appendChild(puls);
  puls.classList.add('pulse-div');
  puls.style.top  = y - puls.offsetHeight/2 + 'px';
  puls.style.left = x - puls.offsetWidth/2  + 'px';
  setTimeout(() => {puls.remove()}, 800);
};

