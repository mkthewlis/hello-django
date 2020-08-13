from django.test import TestCase
from .models import Item


# This new class inherits built in TestCase class
class TestViews(TestCase):
    # every test defined as method that begins with word 'test'
    # Here, 'self' refers to TestViews class above and this tests
    # that we get the home page
    def test_get_todo_list(self):
        # tests http responses of views with built in testing framework
        # from django
        response = self.client.get('/')
        # confirms that the response is equal to 200 (success http response)
        self.assertEqual(response.status_code, 200)
        # checks that the correct template is used
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_get_add_item_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item_page(self):
        # Item is imported in model at top, so we use that to create an item
        # for the test
        item = Item.objects.create(name='Test Todo Item')
        # edit with item id: f takes anything inside the {} and makes it
        # a string; in this case, it becomes the item id
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def test_can_add_item(self):
        # give an example todo item the name 'Test Added Item' as if the form
        # is submitted
        response = self.client.post('/add', {'name': 'Test Added Item'})
        # if it is added successfully, redirect to homepage
        self.assertRedirects(response, '/')

    def test_can_delete_item(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, '/')
        # proves item is deleted by trying to find an item in the db with
        # the same id as the one deleted = not possible
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)

    def test_can_toggle_item(self):
        item = Item.objects.create(name='Test Todo Item', done=True)
        response = self.client.get(f'/toggle/{item.id}')
        self.assertRedirects(response, '/')
        # This calls the item we have just toggled, here named updated_item
        updated_item = Item.objects.get(id=item.id)
        # Asserts that it is in fact done
        self.assertFalse(updated_item.done)
