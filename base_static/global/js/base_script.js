// menu animation

const headerMenu = document.querySelector('[data-header="menu"]')

function AnimateMenuScroll() {
    const windowTop = window.pageYOffset;
    if (windowTop > 0) {
        headerMenu.classList.add('sombra-menu')
    }
    else {
        headerMenu.classList.remove('sombra-menu')
    }
}

window.addEventListener('scroll', function() {
    AnimateMenuScroll();
})

// ============================================================================