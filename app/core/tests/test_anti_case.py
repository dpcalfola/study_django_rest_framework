"""
Anti-test case code

    * 안티 케이스 테스트가 아닐때는 모두 주석처리 해 놓음
        -> 특정 테스트 코드를 필요할 때만 작동하도록 만드는 방법 필요
"""

# from django.test import TestCase
# from django.contrib.auth import get_user_model
#
#
# class AntiTestCase(TestCase):
#     """Test cases that should not be passed"""
#
#     def test_create_user_without_email(self):
#         """
#         If this test code passed, It says user created with blank email
#         """
#         user_without_email = get_user_model().objects.create_user('', 'testPassword643')
#         self.assertEqual(user_without_email.email, '')
