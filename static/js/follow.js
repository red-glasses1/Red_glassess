// 팔로우 팔로잉 비동기 처리
const form = document.querySelector('#follow-form')
const followCsrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

form.addEventListener('submit', function (event) {
    event.preventDefault()

    const userId = event.target.dataset.userId
    axios({
        method: 'post',
        url: `/accounts/${userId}/follower/`,
        headers: {'X-CSRFToken': followCsrftoken,}
    })
    .then((response) => {
        const isFollowed = response.data.is_followed
        const followBtn = document.querySelector('#follow-form > input[type=submit]')
        if (isFollowed === true) {
            followBtn.value = '언팔로우'
            followBtn.classList.add('profile-unfollow_btn')
            followBtn.classList.remove('profile-follow_btn')
        } else {
            followBtn.value = '팔로우'
            followBtn.classList.add('profile-follow_btn')
            followBtn.classList.remove('profile-unfollow_btn')
        }
        const followingsCountTag = document.querySelector('#followings-count')
        const followersCountTag = document.querySelector('#followers-count')
        const followingsCountData = response.data.followings_count
        const followersCountData = response.data.followers_count
        followingsCountTag.textContent = followingsCountData
        followersCountTag.textContent = followersCountData
    })
})