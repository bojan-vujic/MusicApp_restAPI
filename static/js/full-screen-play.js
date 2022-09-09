
// full screen functionalities

// div element, button and some info
var fullScreen = document.getElementsByClassName("full-screen")[0]
var fullScreenInfo = document.getElementsByClassName("full-screen-info")[0]
var btn = document.getElementById("full-screen-btn-img")

btn.addEventListener("click", () => {
  if (!document.fullscreenElement) {
    fullScreen?.requestFullscreen()
    fullScreenInfo.innerHTML = 'Click to exit the full screen.'
    
    setTimeout(() => {
      fullScreenInfo.style.transition = 'all 2s ease'
      fullScreenInfo.style.transform = 'scale(0)'
    }, 3000)
    setTimeout(() => {fullScreenInfo.innerHTML = ''}, 5000)
  }
})

fullScreen.addEventListener("click", () => {
  if (document.fullscreenElement) {document.exitFullscreen()}
})


