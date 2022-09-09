
// TOGGLE SIDEBAR MENU BUTTON
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
var toggleButton = document.getElementsByClassName('toggle-button')[0]
var navbarMenu   = document.getElementsByClassName('nav-bar')[0]
var bar          = document.getElementsByClassName('bar')
var sidebar      = document.getElementsByClassName('sidebar')[0]
var sidebarLinks = document.getElementsByClassName('sidebar-nav-link')

function toggleClass() {
  bar[0].classList.toggle('active-top')
  bar[1].classList.toggle('active-middle')
  bar[2].classList.toggle('active-bottom')
  navbarMenu.classList.toggle('navbar-active')
  sidebar.classList.toggle('sidebar-active')
  for (let link of sidebarLinks) {
    link.classList.toggle('nav-link')
    link.classList.toggle('navlink-left')
  }
}

toggleButton.addEventListener('click', toggleClass)
