"""
Tests for the user API
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('user:create')
TOKEN_USER_URL = reverse('user:token')


def create_user(**params):
    """Create and return new user"""

    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    """Test the public features of the user API"""

    def setUp(self):
        self.client = APIClient()

    def test_create_user_success(self):
        """Test creating a user is successful"""

        # payload -> 탑재 화물
        payload = {
            'email': 'test@example.com',
            'password': 'testPass123',
            'name': 'Test Name',
        }

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        # 생성된 user 객체를 불러온다
        #   1. 패스워드가 동작하는지 확인
        #   2. 불러운 user 객체에 password 정보가 없는지 확인 (없어야함)

        user = get_user_model().objects.get(email=payload['email'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertFalse(user.check_password('wrongPassword'))
        self.assertNotIn('password', res.data)

    def test_user_with_email_exists_error(self):
        """Test error returned if user with email exists"""

        payload = {
            'email': 'test@example.com',
            'password': 'testPass123',
            'name': 'Test name',
        }

        # payload 를 바탕으로 유저를 생성
        create_user(**payload)

        # 같은 정보로 유저를 생성하는 요청을 보내고 결과 객체를 res 에 담는다
        res = self.client.post(CREATE_USER_URL, payload)

        # Test code
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short_error(self):
        """Test an error is returned if password less than 5 chars"""

        # 2 chars password
        payload = {
            'email': 'test@example.com',
            'password': 'pw',
            'name': 'Test name',
        }

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

        # exists() 함수는 filter 된 정보가 존재하는지 bool 타입으로 리턴함
        user_is_exists = get_user_model().objects.filter(
            email=payload['email']
        ).exists()
        self.assertFalse(user_is_exists)

    def test_create_token_for_user(self):
        """TEst generates token for valid credentials"""

        # 유저 생성
        user_details = {
            'name': 'Test Name',
            'email': 'test@example.com',
            'password': 'test-user-password321',
        }
        create_user(**user_details)

        # 토큰 객체 생성
        payload = {
            'email': 'test@example.com',
            'password': 'test-user-password321',
        }
        res = self.client.post(TOKEN_USER_URL, payload)

        # Assert
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn('token', res.data)

    def test_create_token_bad_credentials(self):
        """Test returns error if credentials invalid"""

        # 유저 생성
        user_details = {
            'email': 'test@example.com',
            'password': 'correctPassword',
        }
        create_user(**user_details)

        # 토큰 객체 생성 (wrong password)
        payload = {
            'email': 'test@example.com',
            'password': 'wrongPassword'
        }
        res = self.client.post(TOKEN_USER_URL, payload)

        # Assert
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('token', res.data)

    def test_create_token_blank_password(self):
        """Test posting a blank password returns an error"""

        # Create Token object (blank password)
        payload = {
            'email': 'test@example.com',
            'password': '',
        }
        res = self.client.post(TOKEN_USER_URL, payload)

        # Assert
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('token', res.data)
