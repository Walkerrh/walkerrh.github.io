function login(secret) {
            var hash = sha1(secret)
            var url = hash + "/index.html"
            var alert = document.querySelectorAll('[data-id="alert"]')

            var request = new XMLHttpRequest()
            request.open('GET', url, true)

            request.onload = function () {
                if (request.status >= 200 && request.status < 400) {
                    window.location = url
                } else {
                    parent.location.hash = hash
                    alert[0].style.display = 'block'
                    password[0].setAttribute('placeholder', 'Incorrect password')
                    password[0].value = ''
                }
            }
            request.onerror = function () {
                parent.location.hash = hash
                alert[0].style.display = 'block'
                password[0].setAttribute('placeholder', 'Incorrect password')
                password[0].value = ''
            }
            request.send()
        }

button[0].addEventListener("click", function () {
    login(password[0].value)
})
