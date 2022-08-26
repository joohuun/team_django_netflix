📌 Netflix
-   
- 추천시스템을 활용한 Netflix 클론 코딩

📌 Introduction
-    
- 프로젝트명: Netflix
- 기간: 2022.06.02 ~ 2022.06.14
- 핵심역할: 데이터 크롤링, dump movie_data, 협업 필터링, 로그인, 회원가입
   
📌 아키텍처
-   
![img_1.png](/static/img_1.png)
   
📌 핵심기능   
-   
### 1. 로그인/회원가입
> - 유효성 검사, 아이디 중복 검사, JWT Token사용, 카카오 소셜 로그인  
### 2. 메인 페이지   
> - 강아지 히스토리 CRUD   
> - 댓글 CRUD   
> - 좋아요, 좋아요 취소   
> - 인기 게시글 상단 노출   
> - 엘라스틱서치 엔진을 사용한 초성, 해시태그 검색 기능   
### 3. 마이페이지   
> - 개인 프로필 CRUD   
> - 펫 프로필 CRUD   
> - 자신의 반려동물 프로필 이미지 등록시 AI로 강아지vs고양이 구분 (fastAPI사용, ec2 분리)   
> - 페이지네이션   
### 4. 산책 매칭 페이지   
> - 카카오 지도 API 사용하여 게시글 등록시 위치 제공   
> - 매칭 게시판 CRUD (CKEditor 사용)   
> - 날짜, 지역, 성별, 시간대등 필터 설정으로 검색   
> - 실시간 채팅 기능 (Websocket & Django Channels)   
### 5. 애견 월드컵   
> - 자신의 반려동물을 자랑하는 이벤트 페이지   
> - 이달의 인기 반려동물  (월별 초기화)   
### 6. Nginx / Gunicorn / Daphne   
> - Nginx : Proxy 역할   
> - Gunicorn : Django 배포용 WSGI서버 http protocol 요청 처리 (worker : 2)   
> - Daphne : Django 배포용 ASGI서버 WebSocket portocol 요청 처리   

📌 핵심 트러블 슈팅   
-   
### 1) 배포 후 실시간 비동기 채팅서버인 asgi 서버가 작동 안하는 오류   
> - 에러: 배포 후 http에서는 wsgi, asgi 정상 작동, https로 바꾸면서 wsgi는 작동하고 asgi는 통신을 안하는 에러 발생   
> - 원인: 외부에서 443으로 접근할때 80번 포트로 리다이렉트 시켜주는 방식으로 구성하였는데 80번 포트에서 도메인을 연결시켜주지 않아서 443 -> 80 으로 넘어가지 못하였다.   
> - 해결: 80번 포트에 도메인 등록 시켜주기.
> - [코드 참조](https://github.com/joohuun/Petrasche_back/blob/dfa374231cd39c9b53954e713b7d809d011a83aa/nginx/default.conf#L11)
### 2) 쿼리 최적화 진행   
> - 문제점: DB가 쌓이다 보니 서버가 느려지는 현상 발생
> - 원인: 불필요한 쿼리를 많이 날림
> - 해결: 쿼리디버거를 작성하여 모든 API에 적용시켜보며 전, 후를 비교해 보았다. prefetch_related, select_related를 사용하여 미리 입력된 캐시를 읽어와 불필요한 쿼리를 줄였다.
> - [블로그 참조](https://1q2w3ee.tistory.com/50)   

📌 피그마
-

- 회원가입/로그인
- ![img_5.png](/static/img_5.png) ![img_6.png](/static/img_6.png)


- 메인페이지 / 디테일 모달
![img_7.png](/static/img_7.png)
![img_8.png](/static/img_8.png)

- 애견월드컵 뽐뽐뽐
![img_9.png](/static/img_9.png)

- 산책매칭 / 디테일 모달
![img_10.png](/static/img_10.png)
![img_11.png](/static/img_11.png)

- 실시간 채팅 
![img_12.png](/static/img_12.png)

- 마이페이지
![img_13.png](/static/img_13.png)

