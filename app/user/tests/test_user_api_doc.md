Test code

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