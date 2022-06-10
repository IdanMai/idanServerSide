const activePage = window.location.pathname;

document.querySelectorAll('header a').forEach(link => {
    if (link.href.includes(activePage))
        link.classList.add('active-nav');
})

// animate a twist for the house image
document.querySelector('.home-page__container img').addEventListener('click', (e) => {
    console.log(e.target)
    if (e.target.className === 'spin')
        e.target.className = ''
    else
        e.target.className = 'spin'
})