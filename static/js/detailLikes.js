// 디테일 페이지의 영화 보고싶어요 비동기 처리
const detailForms = document.querySelectorAll('.detail-like-forms')
const detailCsrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

detailForms.forEach((form) => {
    form.addEventListener('submit', function (event) {
        event.preventDefault()
        const detailId = event.target.dataset.detailId
        axios({
            method: 'post',
            url: `/posts/${detailId}/likes/`,
            headers: {'X-CSRFToken': detailCsrftoken},
        })
            .then((response) => {
                const isLiked = response.data.is_liked
                const likeBtn = document.querySelector(`#like-${detailId}`)
                if (isLiked === true) {
                    likeBtn.classList.remove('detail-like_btn');
                    likeBtn.classList.add('detail-unlike_btn');
                } else {
                    likeBtn.classList.remove('detail-unlike_btn');
                    likeBtn.classList.add('detail-like_btn');
                }
            })
            .catch((error) => {
                console.log(error.response)
            })
    })
})