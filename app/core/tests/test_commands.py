"""
Test custom Django management commands
"""

from unittest.mock import patch

from psycopg2 import OperationalError as Psycopg2OpError

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


# @patch -> mocking test decorator
# Command.check 의 check 는 Command 의 슈퍼클래스의 BaseCommand 의 함수
@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """Test commands"""

    # ** Doubtful point : Who throw patched_check parameter?
    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for database if database ready"""

        # Test message
        print('\nDB Test 1: wait_for_db_ready')

        patched_check.return_value = True

        # call_command
        # -> that from SimpleTestCase module that from django.core.management
        call_command('wait_for_db')

        patched_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """Test waiting for database when getting OperationalError"""

        # Test message
        print('\nDB Test 2: wait_for_db_delay')

        # Psycopg2Error 를 2번, OperationalError 를 3번 Raise 한 이후에 True를 반환한다
        # -> True 를 반환하는 시점의 call_count 는 6이어야 한다
        # -> assertEqual(...
        patched_check.side_effect = [Psycopg2OpError] * 2 + \
                                    [OperationalError] * 3 + \
                                    [True]

        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])
