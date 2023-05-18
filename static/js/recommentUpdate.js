const recommentUpdate = document.getElementById('recomment-update');
const recommentContent = document.getElementById('recomment-content');
const recommentInput = document.createElement('input');

recommentUpdate.addEventListener('click', () => {
    recommentInput.value = recommentContent.innerText;
    recommentContent.parentNode.replaceChild(recommentInput, recommentContent);
    recommentInput.classList.add('update-input')
})
