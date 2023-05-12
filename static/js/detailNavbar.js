const navBar = document.getElementById('nav');
const navLogo = document.getElementById('nav-logo');
const searchLabel = document.getElementById('search-label');
const searchIcon = document.getElementById('search-icon');

function changeNavbar() {
    if (window.scrollY > 300) {
        navBar.classList.remove('transparent');
        navLogo.classList.remove('white');
        searchLabel.classList.remove('transparent');
        searchIcon.classList.remove('white');
    } else {
        navBar.classList.add('transparent');
        navLogo.classList.add('white');
        searchLabel.classList.add('transparent');
        searchIcon.classList.add('white');
    }
}

window.addEventListener('scroll', changeNavbar);