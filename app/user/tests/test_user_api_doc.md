## Public User API Test

### Test code 1

    test_create_user_success():
        1. 유저를 생성했을때 201 created 응답
        2. 생성된 유저 객체를 불러온 후
            2-1. 올바른 password 값을 입력했을 때 True 값이 리턴
            2-2. 잘못된 password 값을 입력했을 때 False 값이 리턴
            2-3. 유저 객체에 password 정보가 없다

    test_user_with_email_exists_error():
        1. user를 생성한 이후 같은 정보로 유저를 생성 시도
            -> 400 BAD_REQUEST 응답

    test_password_too_shore_error(self):
        1. 2글자 password로 user 생성을 시도
            -> 400 BAD_REQUEST 응답
        2. 위의 정보로 생성된 user 정보가 없다


### Test code 2 - TOKEN
    
    test_create_token_for_user():
        1. 유저를 생성, 생성된 유저 정보로 token url로 post 요청하여 객체 생성
            1-1. 객체가 생성 되었을때 '200 OK' 응답 
            1-2. 생성된 객체에 토큰 데이터가 있다
    
    test_create_token_bad_credentials():
        2. 잘못된 패스워드로 토큰 객체 생성
            2-1. 객체 생성 응답코드가 '400_BAD_REQUEST'
            2-2. 생성된 객체에 토큰 데이터가 없다
    
    test_create_token_blank_credentials():
        3. blank password 로 토큰 객체 생성
            3-1. 객체 생성 응답코드가 '400_BAD_REQUEST'
            3-2. 생성된 객체에 토큰 데이터가 없다


### Test code 3 - Unauthorized

    test_retrtieve_user_unauthorized():
        1. 권한 없이 ME_URL 로 get 요청시 응답코드가 '401_UNAUTHORIZED'

<br>


## Private User API Tests

* setUp
  * force_authenticate() 로 권한 획득 


### Test code 1

    test_retrieve_profile_success():
        1. ME_URL 로 get 요청하여 객체 생성
            1-1. 객체 생성 응답코드가 '200_OK'
            1-2. 생성된 객체 내부의 정보가 setUp() 에서 생상한 유저 정보와 일치

    test_post_me_not_allowed():
        2. ME_URL 로 POST 요청하여 객체 생성시 응답 코드가 '405_METHOD_NOT_ALLOWED'

    test_update_user_profile():
        3. ME_URL 로 patch 요청하여 'name', 'password' 항목을 업데이트하는 객체를 생성하고, DB를 refresh
            3-1. 객체 생성 응답코드가 '200_OK'
            3-2. 생성된 객체의 'name' 값이 업데이트 되었음
            3-2. 생성된 객체에서 업데이트된 'password' 가 통과됨