from django.http import response
from django.test import TestCase
from .models import Book
from .views import books

class TestAPI(TestCase):
    def setUp(self):
        """setup"""
        Book.objects.create(title= 't1', genre= 'g1')
        Book.objects.create(title= 't2', genre= 'g1')
        Book.objects.create(title= 't3', genre= 'g2')
        Book.objects.create(title= 't4', genre= 'g2')
        Book.objects.create(title= 't5', genre= 'g3')
        Book.objects.create(title= 't6', genre= 'g3')
    
    # tests
    def test_books(self):
        genre1 = 'g1'
        genre2 = 'g2'
        genre3 = 'g3'
        
        response1 = self.client.get("/books/g1/")
        response2 = self.client.get("/books/g2/")
        response3 = self.client.get("/books/g3/")

        self.assertNotEqual(response1.status_code, 404)
        self.assertNotEqual(response2.status_code, 404)
        self.assertNotEqual(response3.status_code, 404)

        self.assertEqual(Book.objects.count(), 6)
        
        data1 = response1.json()
        data2 = response2.json()
        data3 = response3.json()

        self.assertNotIn(None, data1['books'])
        self.assertNotIn(None, data2['books'])
        self.assertNotIn(None, data3['books'])
        
        json1r = str(response1.content, encoding= 'utf8')
        json2r = str(response2.content, encoding= 'utf8')
        json3r = str(response3.content, encoding= 'utf8')

        json1m = {
            'title': 'List of Books',
            'genre': genre1,
            'books': [1, 2]
        }
        json2m = {
            'title': 'List of Books',
            'genre': genre2,
            'books': [3, 4]
        }
        json3m = {
            'title': 'List of Books',
            'genre': genre3,
            'books': [5, 6]
        }
        
        self.assertJSONEqual(json1r, json1m)
        self.assertJSONEqual(json2r, json2m)
        self.assertJSONEqual(json3r, json3m)
        
        
        # self.assertTrue(data1['title'] == 'List of Books')
        # self.assertTrue(data2['title'] == 'List of Books')
        # self.assertTrue(data3['title'] == 'List of Books')

        # self.assertTrue(data1['genre'] == genre1)
        # self.assertTrue(data2['genre'] == genre2)
        # self.assertTrue(data3['genre'] == genre3)
        
        # self.assertEqual(data1['books'], [1, 2])
        # self.assertEqual(data1['books'], [3, 4])
        # self.assertEqual(data1['books'], [5, 6])

        
        