
const btnLoginHeader = document.getElementById('button-header-login')
    if(btnLoginHeader) {
        btnLoginHeader.addEventListener('click',  () => {
            window.location.href = btnLoginHeader.dataset.url
        })
}

