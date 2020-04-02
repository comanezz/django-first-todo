from django.test import TestCase
from .forms import ItemForm

# Create your tests here.
class TestToDoItemForm(TestCase):
    
    def test_can_create_an_item_with_just_a_name(self):
        # this object using a dictionary so we will open our curly braces for a dictionary and the key is going to be name and then the value is going to be a string
        form = ItemForm({'name': 'Create tests'})
        """we want to test the is_valid function so if I say self.assertTrue 
        and then inside of that function we're just gonna pass through form.is_valid. 
        This assert true will just check to ensure that the result returned from the form that is valid 
        is true is a boolean off true
        """
        self.assertTrue(form.is_valid())

    def test_correct_message_for_missing_name(self):

        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        # It means that there is an error in the name field.
        self.assertEqual(form.errors['name'], [u'This field is required.'])