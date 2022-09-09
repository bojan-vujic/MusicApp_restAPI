
var togglePassword = document.querySelector('#togglePassword'),
    password       = document.querySelector('#current-password')

togglePassword.addEventListener('click', () => {
  var type = password.getAttribute('type')
  if (type === 'password') {
    password.setAttribute('type', 'text')
    togglePassword.src = '/media/password-hide.png'
  } else {
    password.setAttribute('type', 'password')
    togglePassword.src = '/media/password-show.png'
  }
})

