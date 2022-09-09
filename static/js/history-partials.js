
// apply for last time played info
var elements = document.getElementsByClassName('ltpl')

for (let el of elements) {
  var value = el.innerHTML.split(',')[0]
  val = value.toString().replace('1&nbsp;hour', 'an&nbsp;hour')
  // .replace('1&nbsp;', 'a&nbsp;')
  el.innerHTML = val + ' ago'
}

// show/hide div
var buttons   = document.getElementsByClassName('show-buttons')
var infoDivs  = document.getElementsByClassName('sm-info')
var closeDivs = document.getElementsByClassName('sm-info-close')

for (let i = 0; i < buttons.length; i++) {
  var el = buttons[i]
  var cl = closeDivs[i]
  
  el.addEventListener('click', () => {
    for (let x of infoDivs) {x.style.display = 'none'}
    var info = infoDivs[i]
    info.style.display = 'flex'
  })

  cl.addEventListener('click', () => {
    var info = infoDivs[i]
    info.style.display = 'none'
  })
}

var heartImgs    = document.getElementsByClassName('img-heart')
var heartedImgs  = document.getElementsByClassName('img-hearted')
var trashCanImgs = document.getElementsByClassName('img-trash-can')

// add some event listeners to change image src on hover
for (let img1 of heartImgs) {
  var c1 = img1.src
  img1.addEventListener('mouseover', () => {
    img1.src = '/media/heart-video-hover.png';
  })
  img1.addEventListener('mouseout', () => {
    img1.src = c1;
  })
}

for (let img2 of heartedImgs) {
  var c2 = img2.src
  img2.addEventListener('mouseover', () => {
    img2.src = '/media/hearted-video-hover.png';
  })
  img2.addEventListener('mouseout', () => {
    img2.src = c2;
  })
}

for (let img of trashCanImgs) {
  var c = img.src
  img.addEventListener('mouseover', () => {
    img.src = '/media/trash-can-hover.png';
  })
  img.addEventListener('mouseout', () => {
    img.src = c;
  })
}