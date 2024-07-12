const hamburger = document.getElementById('nav-toggle');
const navMenu = document.getElementById('nav-menu');
const navBar = document.querySelector('nav');

hamburger.addEventListener('click', function() {
    navMenu.classList.toggle('active');
    navBar.classList.toggle('menu-active')
    if (navMenu.classList.contains('active')) {
        hamburger.setAttribute('name', 'x');
    } else {
        hamburger.setAttribute('name', 'menu');
    }
});