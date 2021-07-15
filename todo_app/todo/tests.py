from django.test import TestCase
from .models import todoitem

# Create your tests here.

class test_urls(TestCase):
    def test_welcomepage(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)
    
    def test_homepage(self):
        response_home = self.client.get("/home/")
        self.assertEqual(response_home.status_code, 200)
        
    def test_aboutpage(self):
        response_about = self.client.get("/about/")
        self.assertEqual(response_about.status_code, 200)

class test_crud(TestCase):
    # Find how to get TODO model as dict
    def test_createtodo(self):
        new_item = self.client.post("/home/", todoitem(item = "testing item"))
        self.assertEqual(new_item.status_code, 302)