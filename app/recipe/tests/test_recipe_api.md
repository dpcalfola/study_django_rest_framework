## Recipe API Test

### Test Code 1 - Public access

    URL: api/recipe/recipe-list
        
    test_auth_required():
        1. 퍼블릭으로 get 요청시
            -> 401 UNAUTHORIZED 응답

### Test Code 2 - Private access
    
    URL: api/recipe/recipe-list
    유저 로그인 상태

    test_retrieve_recipes():
        2. 로그인된 유저로 2개의 레시피 객체를 생성하고 get 요청하여 결과를 저장
            2-1. get 요청의 응답이 200 OK
            2-2. 결과 객체의 데이터와 RecipeSerializer 로 생성된 객체의 데이터가 같다

    test_recipe_list_limited_to_user():
        3. 서로 다른 유저(self.user, other_user)로 레시피 객체 생성를 각각 생성하고 get 요청하여 결과를 저장
            3-1. get 요청의 응답이 200 OK
            3-2. 결과 객체의 데이터와 user=self.user 로 필터링된
                RecipeSerializer 로 생성된 객체의 데이터가 같다
                ( == other_user 로 생서된 데이터는 serializer에 없다)