from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):
    # name test with something descriptive to help when running tests
    # This one tests that the name field is required to submit
    def test_item_name_is_required(self):
        form = ItemForm({'name': ''})
        # testing the form is not valid, as the name is empty as above ''
        self.assertFalse(form.is_valid())
        # this shows the error occured in the 'name' field
        self.assertIn('name', form.errors.keys())
        # this confirms that the error message is one that shows up if the
        # form is submitted empty
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    # tests that the done field is not required
    def test_done_field_is_not_required(self):
        form = ItemForm({'name': 'Test Todo Item'})
        self.assertTrue(form.is_valid())

    # Currently form fields are listed explicitly in forms.py (name & done),
    # so this test is actually just an example for a future scenario
    # where more fields are added to the form but we don't want them showed
    # to the user in the view
    def test_fields_are_explicit_in_form_metaclass(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
