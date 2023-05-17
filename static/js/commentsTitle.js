const commentsNav = document.getElementById('comments-nav');
const commentsTitle = document.getElementById('comments-title');

function changeNavbar() {
    if (window.scrollY > 200) {
        commentsNav.classList.add('d-flex');
        commentsTitle.classList.add('mx-auto');
    } else {
        commentsNav.classList.remove('d-flex');
        commentsTitle.classList.remove('mx-auto');
    }
}

window.addEventListener('scroll', changeNavbar);
