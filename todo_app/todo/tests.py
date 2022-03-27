from django.test import TestCase
from .models import ToDoItem


class TestUrls(TestCase):
    def test_welcomepage(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 6000)
    
    def test_homepage(self):
        response_home = self.client.get("/home/")
        self.assertEqual(response_home.status_code, 200)
        
    def test_aboutpage(self):
        response_about = self.client.get("/about/")
        self.assertEqual(response_about.status_code, 200)

class TestCrud(TestCase):
    def setUp(self):
        ToDoItem.objects.create(item="shopping")

    def test_createtodo(self):
        new_item = self.client.post("/home/", {"content":"TESTITEM"})
        self.assertEqual(new_item.status_code, 302)
        todoitem = ToDoItem.objects.get(item = "TESTITEM")
        self.assertTrue(todoitem)
    
    def test_deletetodo(self):
        todoitem = ToDoItem.objects.get(item = "shopping")
        todoid = todoitem.id
        deleting = self.client.post(f"/deletetodo/{todoid}/")
        with self.assertRaises(ToDoItem.DoesNotExist):
            ToDoItem.objects.get(item = "shopping")

    def test_updateTodo(self):
        todoitem = ToDoItem.objects.get(item = "shopping")
        todoid = todoitem.id
        updating = self.client.post(f"/updatetodo/{todoid}/", {"UpdatedItem":"WALKING"})
        updated_item = ToDoItem.objects.get(item = "WALKING")
        self.assertTrue(updated_item)
        

