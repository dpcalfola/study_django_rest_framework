"""
Tests for the Django admin modifications
"""

from django.test import TestCase
from django.test import Client
from django.contrib.auth import get_user_model
from django.urls import reverse  # noqa


class AdminSiteTests(TestCase):
    """Tests for Django admin"""

    # setUp -> run before every single test
    def setUp(self):
        """Create user and client"""

        # Test message
        print('\nAdmin Test setUp: create superuser and user')

        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='adminUser@example.com',
            password='testPassword4321'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='userPassword123',
            name='Test user'
        )

    def test_users_list(self):
        """Test that users are listed on page"""

        # I CANNOT UNDERSTAND THIS CODE

        # Test message
        print('Admin Test 1: Users list')

        # Doubtful point:
        # Where 'admin:core_user_changelist' came from ?
        # I tried to find out in Django modules but failed
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        # Check changelist has user.name and user.email
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_edit_user_page(self):
        """Test the edit user page"""

        # Test message
        print('Admin Test 2: Edit user page')

        # Doubtful point again:
        # Where 'admin:core_user_change' came from ?
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
