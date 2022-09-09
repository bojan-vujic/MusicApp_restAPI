
var el  = document.querySelector('#video_iframe')

var videoWidth  = el.offsetWidth
var videoHeight = videoWidth * 9 / 16

var player
var videoId      = el.dataset.video   // videoId of the youtube video
var startSeconds = el.dataset.start   // set the start for the video interval
var endSeconds   = el.dataset.end     // set the end for the video interval
var duration     = el.dataset.duration
var repeats      = 0

var playerConfig = {
  height: videoHeight,
  width: videoWidth,
  videoId: videoId,
  playerVars: {
    autoplay: 1,            // Auto-play the video on load
    controls: 1,            // Show pause/play buttons in player
    showinfo: 0,            // Hide the video title
    modestbranding: 0,      // Hide the Youtube Logo
    fs: 1,                  // Hide the full screen button
    cc_load_policy: 0,      // Hide closed captions
    iv_load_policy: 3,      // Hide the Video Annotations
    start: startSeconds,    // Start of the video loop (seconds)
    end: endSeconds,        // End of video loop (seconds)
    autohide: 1,            // Hide video controls when playing
    enablejsapi: 1,         // Enable javascript api control
    rel: 1,
  },
  events: {
    'onStateChange': onStateChange,   // reference to Iframe API
    //onReady: ''
  }
}

//excute the video in div
function onYouTubePlayerAPIReady() {
  player = new YT.Player('video_iframe', playerConfig)
  // var elem = document.getElementsByTagName('iframe')[0].contentWindow
  // elem.getElementsByClassName('ytp-watch-later-button')[0].style.display = 'none'
}

//reload the video
function onStateChange(state) {
  // player.playerInfo.currentTime
  // YT.PlayerState.ENDED
  if (state.data === YT.PlayerState.ENDED) {
    repeats++
    if (endSeconds == duration) {
      document.getElementById("update-counter").click()
    } else {
      if (repeats % 2 == 0) {
        document.getElementById("update-counter").click()
      }
    }
    player.loadVideoById({
      videoId: videoId,
      startSeconds: startSeconds,
      endSeconds: endSeconds
    })
    console.log(player)
  }
}