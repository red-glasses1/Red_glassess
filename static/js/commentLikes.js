// 코멘트 좋아요 비동기 처리
const commentForms = document.querySelectorAll('.comment-like-forms')
const commentCsrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
const commentLikeCount = document.getElementById('comment-like-count')

commentForms.forEach((form) => {
    form.addEventListener('submit', function (event) {
        event.preventDefault()
        const detailId = event.target.dataset.detailId
        const commentId = event.target.dataset.commentId
        axios({
            method: 'post',
            url: `/posts/${detailId}/comments/${commentId}/likes/`,
            headers: {'X-CSRFToken': commentCsrftoken},
        })
            .then((response) => {
                const isLiked = response.data.is_liked
                const likeBtn = document.querySelector(`#like-${detailId}-${commentId}`)
                const likeCount = response.data.like_count;
                if (isLiked === true) {
                    likeBtn.classList.add('color-pink');
                    likeBtn.classList.remove('text-secondary');
                    commentLikeCount.innerText = likeCount;
                } else {
                    likeBtn.classList.add('text-secondary');
                    likeBtn.classList.remove('color-pink');
                    commentLikeCount.innerText = likeCount;
                }
            })
            .catch((error) => {
                console.log(error.response)
            })
    })
})