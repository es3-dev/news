const btnLoginHeader = document.getElementById('button-header-login')
    if(btnLoginHeader) {
        btnLoginHeader.addEventListener('click',  () => {
            window.location.href = btnLoginHeader.dataset.url
        })
}

const btnSignupHeader = document.getElementById('button-header-sign-up')
    if(btnSignupHeader)
        btnSignupHeader.addEventListener('click', () => {
            window.location.href= btnSignupHeader.dataset.url
    })

//Logout con JS
// Selecciona el botón de logout (Leave) por su clase
const btnLeave = document.querySelector('.btn-leave');
// Si existe el botón de logout, agrega un listener para hacer logout al hacer click
if (btnLeave) {
    btnLeave.addEventListener('click', () => {
        // Envía una petición POST a /logout/ usando fetch
        fetch('/logout/', {
            method: 'POST',
            headers: {
                // Incluye el CSRF token necesario para peticiones POST en Django
                'X-CSRFToken': getCookie('csrftoken'),
                'Content-Type': 'application/json',
            },
        })
        .then(response => {
            // Si la respuesta es una redirección, redirige el navegador a la nueva URL
            if (response.redirected) {
                window.location.href = response.url;
            } else {
                // Si no, recarga la página actual
                window.location.reload();
            }
        });
    });
}

// Función para obtener el CSRF token de las cookies
function getCookie(name) {
    let cookieValue = null;
    // Verifica si hay cookies en el documento
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        // Recorre todas las cookies buscando la que coincide con el nombre
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Si encuentra la cookie, obtiene su valor
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

