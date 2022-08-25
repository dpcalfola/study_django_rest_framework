"""
Tests for models
"""
from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


class ModelTests(TestCase):
    """Test models"""

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful"""

        # Test message
        print('\nModel Test 1: Create user')

        email = 'test_email@example.com'
        password = 'testPassword423'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users"""

        # Test message
        print('\nModel Test 2: Normalize email')

        sample_email = [
            # Test sample:
            # 1. Domain - Uppercase should be changed to lowercase
            # 2. Local part - Should not be changed
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['test2@Example.com', 'test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com']
        ]

        for email, expected in sample_email:
            user = get_user_model().objects.create_user(email, 'samplePassword123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test that create a user without an email raises a ValueError"""

        # Test message
        print('\nModel Test 3: new user without email raises ValueError')

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email='', password='testPassword123')

    def test_create_superuser(self):
        """Test creating superuser"""

        user = get_user_model().objects.create_superuser(
            email='testSuperUser@expample.com',
            password='testSuperUserPassword',
        )

        # ".is_superuser" field provided by PermissionsMixin
        self.assertTrue(user.is_superuser)

        # ".is_staff" field provided by AbstractBaseUser
        self.assertTrue(user.is_staff)

    def test_create_recipe(self):
        """Test creating a recipe is successful"""
        user = get_user_model().objects.create_user(
            'test@example',
            'testPassword321',
        )
        recipe = models.Recipe.objects.create(
            user=user,
            title='Sample recipe name',
            time_minutes=5,
            price=Decimal('5.50'),
            description='Sample recipe description',
        )

        self.assertEqual(str(recipe), recipe.title)
