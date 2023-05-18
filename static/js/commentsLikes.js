// 코멘트 모음 페이지 좋아요 비동기 처리
const commentForms = document.querySelectorAll('.comment-like-forms')
const commentCsrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

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
                const commentLikeCount = document.getElementById(`like-count-${detailId}-${commentId}`)
                const likeCount = response.data.like_count;
                if (isLiked === true) {
                    likeBtn.classList.remove('comment-like_btn');
                    likeBtn.classList.add('comment-unlike_btn');
                    commentLikeCount.innerText = likeCount;
                } else {
                    likeBtn.classList.remove('comment-unlike_btn');
                    likeBtn.classList.add('comment-like_btn');
                    commentLikeCount.innerText = likeCount;
                }
            })
            .catch((error) => {
                console.log(error.response)
            })
    })
})