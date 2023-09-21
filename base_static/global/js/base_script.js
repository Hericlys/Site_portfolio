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

// filtro de categorias

function submitForm() {
    let form = document.getElementById('form_filtro');
    form.submit();
}

function deletSearch() {
    let search = document.getElementById('search');
    search.value = ''
    submitForm()
}

// ============================================================================

// mascasras de input

// https://igorescobar.github.io/jQuery-Mask-Plugin/docs.html

$("#telefone").mask("(99) 99999-9999");