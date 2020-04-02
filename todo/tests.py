from django.test import TestCase

# Create your tests here.
class TestDjango(TestCase):

    # It's important to note that if our methods don't begin with test underscore then Django won't find them
    def test_is_this_thing_on(self):
        self.assertEqual(1, 1)