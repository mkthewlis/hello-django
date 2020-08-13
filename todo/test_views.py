from django.test import TestCase


# This new class inherits built in TestCase class
class TestDjango(TestCase):
    # every test defined as method that begins with word 'test'
    # Here, 'self' refers to TestDjango class above.
    def test_this_thing_works(self):
        self.assertEqual(1, 1)
