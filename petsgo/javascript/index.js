const open = document.getElementById('open');
const modal_container = document.getElementById('modal_container');
const close = document.getElementById('close');

if (open){

open.addEventListener('click', () => {
    modal_container.classList.add('show');
    alert('hola mundo');
});
}