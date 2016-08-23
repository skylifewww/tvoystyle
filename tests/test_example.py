from tvoy_style.core.test import TestCase
from tvoy_style.users.factories import UserFactory


class TestExample(TestCase):

    def test_example(self):
        UserFactory()
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
