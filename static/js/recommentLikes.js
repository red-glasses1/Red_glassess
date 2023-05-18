// 코멘트 댓글 좋아요 비동기 처리
const recommentForms = document.querySelectorAll('.recomment-like-forms')
const recommentCsrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

recommentForms.forEach((form) => {
    form.addEventListener('submit', function (event) {
        event.preventDefault()
        const detailId = event.target.dataset.detailId
        const commentId = event.target.dataset.commentId
        const recommentId = event.target.dataset.recommentId
        axios({
            method: 'post',
            url: `/posts/${detailId}/comments/${commentId}/recomments/${recommentId}/likes/`,
            headers: {'X-CSRFToken': recommentCsrftoken},
        })
            .then((response) => {
                const isLiked = response.data.is_liked
                const likeBtn = document.querySelector(`#like-${detailId}-${commentId}-${recommentId}`)
                const recommentLikeIcon = document.getElementById(`like-icon-${detailId}-${commentId}-${recommentId}`)
                const recommentLikeCount = document.getElementById(`like-count-${detailId}-${commentId}-${recommentId}`)
                const likeCount = response.data.like_count;
                if (isLiked === true) {
                    recommentLikeCount.classList.remove('recomment-like_btn');
                    recommentLikeCount.classList.add('recomment-unlike_btn');
                    recommentLikeIcon.classList.remove('recomment-like_btn');
                    recommentLikeIcon.classList.add('recomment-unlike_btn');
                    recommentLikeCount.innerText = likeCount;
                } else {
                    recommentLikeCount.classList.remove('recomment-unlike_btn');
                    recommentLikeCount.classList.add('recomment-like_btn');
                    recommentLikeIcon.classList.remove('recomment-unlike_btn');
                    recommentLikeIcon.classList.add('recomment-like_btn');
                    recommentLikeCount.innerText = likeCount;
                }
            })
            .catch((error) => {
                console.log(error.response)
            })
    })
})