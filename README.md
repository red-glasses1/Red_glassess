# 왓챠피디아 클론 팀 프로젝트

기간: 2023년 5월 9일 → 2023년 5월 19일
태그: API, 백엔드, 클론

<aside>
📜 프로젝트 개요

</aside>

첫 팀 프로젝트로 왓챠피디아의 사이트 클론 프로젝트를 진행하였습니다.

해당 프로젝트를 통해 사용자가 손쉽게 영화 및 드라마 정보를 검색하고 리뷰를 작성하는 등의 다양한 기능을 구현하는 프로젝트를 진행하였습니다.

<aside>
💪🏻 프로젝트 목표

</aside>

1. 왓챠피디아와 유사한 UI/UX를 구현
2. 영화 및 드라마에 대한 정보를 tmdb의 API를 이용하여 영화 정보 데이터 연동.
3. 사용자가 영화 및 드라마에 대한 리뷰를 작성하고 조회할 수 있는 기능을 구현함
4. 상세페이지(영화정보, 사용자 프로필 정보) 구현
5. 소셜 로그인(카카오,구글) 구현
6. 팔로우, 좋아요 기능 구현

<aside>
👨🏻‍💻 사용 기술

</aside>

- Django
- Python
- Javascript
- Mysql
- Bootstrap
- OAuth2.0(Kakao, Google)

<aside>
🔥 프로젝트 멤버

</aside>

- 김초원: 조장, 프론트엔드
- 조정곤: 프론트엔드, 백엔드
- 임지혜: 프론트엔드
- 오창인(본인): 백엔드

<aside>
💡 나의 역할

</aside>

- 구현한 기능
    - 영화를 담는 Post 앱, 프로필 정보를 담는 accounts 앱의 모델(DB)설계
    - forms.py 내 보안문제를 초래할 수 있는 부분 수정.
    - Django의 쿼리셋을 이용한 영화 검색 필터 구현
    - Create(SignUp),Read(포스팅 리스트),Update(회원 수정),Delete 구현

<aside>
📢 프로젝트 결과물

</aside>

- **배포 페이지**
    
    [Watcha Pedia](https://port-0-red-glassess-13aenn2blhthwfuc.sel4.cloudtype.app/)
    
- **소스코드**
    
    [https://github.com/red-glasses1/Red_glassess.git](https://github.com/red-glasses1/Red_glassess.git)
    
- **발표 자료**
    
    ![Red_glasses 왓챠피디아1024_6.jpg](%E1%84%8B%E1%85%AA%E1%86%BA%E1%84%8E%E1%85%A3%E1%84%91%E1%85%B5%E1%84%83%E1%85%B5%E1%84%8B%E1%85%A1%20%E1%84%8F%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A9%E1%86%AB%20%E1%84%90%E1%85%B5%E1%86%B7%20%E1%84%91%E1%85%B3%E1%84%85%E1%85%A9%E1%84%8C%E1%85%A6%E1%86%A8%E1%84%90%E1%85%B3%2078e91e5fc2514e569b60313c8bc77eda/Red_glasses_%25E1%2584%258B%25E1%2585%25AA%25E1%2586%25BA%25E1%2584%258E%25E1%2585%25A3%25E1%2584%2591%25E1%2585%25B5%25E1%2584%2583%25E1%2585%25B5%25E1%2584%258B%25E1%2585%25A11024_6.jpg)
    
    ![Red_glasses 왓챠피디아1024_8.jpg](%E1%84%8B%E1%85%AA%E1%86%BA%E1%84%8E%E1%85%A3%E1%84%91%E1%85%B5%E1%84%83%E1%85%B5%E1%84%8B%E1%85%A1%20%E1%84%8F%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A9%E1%86%AB%20%E1%84%90%E1%85%B5%E1%86%B7%20%E1%84%91%E1%85%B3%E1%84%85%E1%85%A9%E1%84%8C%E1%85%A6%E1%86%A8%E1%84%90%E1%85%B3%2078e91e5fc2514e569b60313c8bc77eda/Red_glasses_%25E1%2584%258B%25E1%2585%25AA%25E1%2586%25BA%25E1%2584%258E%25E1%2585%25A3%25E1%2584%2591%25E1%2585%25B5%25E1%2584%2583%25E1%2585%25B5%25E1%2584%258B%25E1%2585%25A11024_8.jpg)
    
    ![Red_glasses 왓챠피디아1024_15.jpg](%E1%84%8B%E1%85%AA%E1%86%BA%E1%84%8E%E1%85%A3%E1%84%91%E1%85%B5%E1%84%83%E1%85%B5%E1%84%8B%E1%85%A1%20%E1%84%8F%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A9%E1%86%AB%20%E1%84%90%E1%85%B5%E1%86%B7%20%E1%84%91%E1%85%B3%E1%84%85%E1%85%A9%E1%84%8C%E1%85%A6%E1%86%A8%E1%84%90%E1%85%B3%2078e91e5fc2514e569b60313c8bc77eda/Red_glasses_%25E1%2584%258B%25E1%2585%25AA%25E1%2586%25BA%25E1%2584%258E%25E1%2585%25A3%25E1%2584%2591%25E1%2585%25B5%25E1%2584%2583%25E1%2585%25B5%25E1%2584%258B%25E1%2585%25A11024_15.jpg)
    
    ![Red_glasses 왓챠피디아1024_12.jpg](%E1%84%8B%E1%85%AA%E1%86%BA%E1%84%8E%E1%85%A3%E1%84%91%E1%85%B5%E1%84%83%E1%85%B5%E1%84%8B%E1%85%A1%20%E1%84%8F%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A9%E1%86%AB%20%E1%84%90%E1%85%B5%E1%86%B7%20%E1%84%91%E1%85%B3%E1%84%85%E1%85%A9%E1%84%8C%E1%85%A6%E1%86%A8%E1%84%90%E1%85%B3%2078e91e5fc2514e569b60313c8bc77eda/Red_glasses_%25E1%2584%258B%25E1%2585%25AA%25E1%2586%25BA%25E1%2584%258E%25E1%2585%25A3%25E1%2584%2591%25E1%2585%25B5%25E1%2584%2583%25E1%2585%25B5%25E1%2584%258B%25E1%2585%25A11024_12.jpg)
    
    ![Red_glasses 왓챠피디아1024_13.jpg](%E1%84%8B%E1%85%AA%E1%86%BA%E1%84%8E%E1%85%A3%E1%84%91%E1%85%B5%E1%84%83%E1%85%B5%E1%84%8B%E1%85%A1%20%E1%84%8F%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A9%E1%86%AB%20%E1%84%90%E1%85%B5%E1%86%B7%20%E1%84%91%E1%85%B3%E1%84%85%E1%85%A9%E1%84%8C%E1%85%A6%E1%86%A8%E1%84%90%E1%85%B3%2078e91e5fc2514e569b60313c8bc77eda/Red_glasses_%25E1%2584%258B%25E1%2585%25AA%25E1%2586%25BA%25E1%2584%258E%25E1%2585%25A3%25E1%2584%2591%25E1%2585%25B5%25E1%2584%2583%25E1%2585%25B5%25E1%2584%258B%25E1%2585%25A11024_13.jpg)
    
    ![Red_glasses 왓챠피디아1024_14.jpg](%E1%84%8B%E1%85%AA%E1%86%BA%E1%84%8E%E1%85%A3%E1%84%91%E1%85%B5%E1%84%83%E1%85%B5%E1%84%8B%E1%85%A1%20%E1%84%8F%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A9%E1%86%AB%20%E1%84%90%E1%85%B5%E1%86%B7%20%E1%84%91%E1%85%B3%E1%84%85%E1%85%A9%E1%84%8C%E1%85%A6%E1%86%A8%E1%84%90%E1%85%B3%2078e91e5fc2514e569b60313c8bc77eda/Red_glasses_%25E1%2584%258B%25E1%2585%25AA%25E1%2586%25BA%25E1%2584%258E%25E1%2585%25A3%25E1%2584%2591%25E1%2585%25B5%25E1%2584%2583%25E1%2585%25B5%25E1%2584%258B%25E1%2585%25A11024_14.jpg)
    
    ![Red_glasses 왓챠피디아1024_10.jpg](%E1%84%8B%E1%85%AA%E1%86%BA%E1%84%8E%E1%85%A3%E1%84%91%E1%85%B5%E1%84%83%E1%85%B5%E1%84%8B%E1%85%A1%20%E1%84%8F%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A9%E1%86%AB%20%E1%84%90%E1%85%B5%E1%86%B7%20%E1%84%91%E1%85%B3%E1%84%85%E1%85%A9%E1%84%8C%E1%85%A6%E1%86%A8%E1%84%90%E1%85%B3%2078e91e5fc2514e569b60313c8bc77eda/Red_glasses_%25E1%2584%258B%25E1%2585%25AA%25E1%2586%25BA%25E1%2584%258E%25E1%2585%25A3%25E1%2584%2591%25E1%2585%25B5%25E1%2584%2583%25E1%2585%25B5%25E1%2584%258B%25E1%2585%25A11024_10.jpg)
    
    ![Red_glasses 왓챠피디아1024_11.jpg](%E1%84%8B%E1%85%AA%E1%86%BA%E1%84%8E%E1%85%A3%E1%84%91%E1%85%B5%E1%84%83%E1%85%B5%E1%84%8B%E1%85%A1%20%E1%84%8F%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A9%E1%86%AB%20%E1%84%90%E1%85%B5%E1%86%B7%20%E1%84%91%E1%85%B3%E1%84%85%E1%85%A9%E1%84%8C%E1%85%A6%E1%86%A8%E1%84%90%E1%85%B3%2078e91e5fc2514e569b60313c8bc77eda/Red_glasses_%25E1%2584%258B%25E1%2585%25AA%25E1%2586%25BA%25E1%2584%258E%25E1%2585%25A3%25E1%2584%2591%25E1%2585%25B5%25E1%2584%2583%25E1%2585%25B5%25E1%2584%258B%25E1%2585%25A11024_11.jpg)
