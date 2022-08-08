"""
Tests for the Django admin modifications
"""

from django.test import TestCase
from django.test import Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    """Tests for Django admin"""

    # setUp -> run before every single test
    def setUp(self):
        """Create user and client"""

        # Test message
        print('\nTest setUp: create superuser and user')

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

        # Doubtful point:
        # Where 'admin:core_user_changelist' came from ?
        # I tried to find out in Django modules but failed
        url = reverse('admin:core_user_changelist')
        result_user_changelist = self.client.get(url)

        # Check changelist has user.name and user.email
        self.assertContains(result_user_changelist, self.user.name)
        self.assertContains(result_user_changelist, self.user.email)
