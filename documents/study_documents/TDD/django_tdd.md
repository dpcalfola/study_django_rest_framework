# Django TDD

<br>

### Where do I put test code ?

1. django 앱 내부의 ***tests.py*** 파일
2. ***tests/*** directory
   *  directory 안에는 반드시 \_\_init\_\_.py 를 포함해야 함
   *  모듈은 test_ 로 시작해야 함 
      *  ex1 ) test_module_one.py
      *  ex2 ) def test_method_one(self):


### Test classes

1. SimpleTestCase
    * No DB test
    * 테스트 소요시간이 짧음
    * 예시
        ```
        from django.test import SimpleTestCase
    
        class ViewsTests(SimpleTestCase):

            def test_method_two(self):
            """ testcode """
            return
        ```

2. TestCase
    * 매 테스트마다 DB를 새로 생성 삭제함