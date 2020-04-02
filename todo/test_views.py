from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Item

class TestViews(TestCase):
    
    def test_get_home_page(self):
        """we need to say page is equal to self.client.get and this is a built-in helper 
        that will basically fake a request to the URL that we pass in as an argument here which 
        is just forward slash and then what we can do is store the output of that in page.
        """
        page = self.client.get('/')
        self.assertEqual(page.status_code, 200)
        """The first argument this takes is the 'page' so we want to ensure that
         this page has used this template so the template that we want to test for is todo_list.html
        """
        self.assertTemplateUsed(page, "todo_list.html")

    def test_get_add_item_page(self):
        page = self.client.get('/add')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "item_form.html")

    def test_get_edit_item_page(self):
        item = Item(name = "Create a Test")
        item.save()

        page = self.client.get('/edit/{0}'.format(item.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "item_form.html")

    # I'm going to create a method called test get edit page for item that does not exist
    def test_get_edit_page_for_item_that_does_not_exist(self):
        page = self.client.get("/edit/1")
        self.assertEqual(page.status_code, 404)

    def test_post_create_an_item(self):
        """the URL that we are posting to is going to be /add
        and then we're going to create a dictionary of items that we're gonna pass to that URL
        """
        response = self.client.post("/add", {"name": "Create a Test"})
        item = get_object_or_404(Item, pk=1)
        self.assertEqual(item.done, False)

    def test_post_edit_an_item(self):
        item = Item(name="Create a Test")
        item.save()
        id = item.id

        response = self.client.post("/edit/{0}".format(id), {"name": "A different name"})
        item = get_object_or_404(Item, pk=id)

        self.assertEqual(item.name, "A different name")

    def test_toggle_status(self):
        item = Item(name="Create a Test")
        item.save()
        id = item.id

        response = self.client.post("/toggle/{0}".format(id))

        item = get_object_or_404(Item, pk=id)
        self.assertEqual(item.done, True)