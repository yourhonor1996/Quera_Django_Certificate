from django.test import TestCase


from .models import Author, Book
from datetime import date
# test the models
class AuthorTest(TestCase):
    def setUp(self):
        self.auth1 = Author.objects.create(first_name= 'f1', last_name= 'l1', date_of_birth= date(1900, 1, 1))
        self.auth2 = Author.objects.create(first_name= 'f2', last_name= 'l2', date_of_birth= date(1900, 1, 2), date_of_death= date(1970, 1, 1))

        self.book1 = Book.objects.create(title= 't1', author= self.auth1, summary= 's1', date_of_publish= date(1910,1,1)) #111
        self.book2 = Book.objects.create(title= 't2', author= self.auth1, summary= 's2', date_of_publish= date(1911,1,1)) #110
        self.book3 = Book.objects.create(title= 't3', author= self.auth1, summary= 's3', date_of_publish= date(1913,1,1)) #109
        self.book4 = Book.objects.create(title= 't4', author= self.auth2, summary= 's4', date_of_publish= date(1914,1,1)) #108
        self.book5 = Book.objects.create(title= 't5', author= self.auth2, summary= 's5', date_of_publish= date(1915,1,1)) #107
        self.book6 = Book.objects.create(title= 't6', author= self.auth2, summary= 's6', date_of_publish= date(1916,1,1)) #106
    
    def test_is_alive_author(self):
        self.assertTrue(self.auth1.is_alive())
        self.assertFalse(self.auth2.is_alive())
        
    def test_get_age_author(self):
        self.assertEqual(str(self.auth1.get_age().days), "44393") #121 years
        self.assertEqual(str(self.auth2.get_age().days), "25566") # 70 years
        
    def test_str_author(self):
        self.assertEqual(str(self.auth1), 'f1 l1')
        self.assertEqual(str(self.auth2), 'f2 l2')
        

    def test_get_age_book(self):
        self.assertEqual(str(self.book1.get_age().days), "40741")
        self.assertEqual(str(self.book2.get_age().days), "40376")
        
        
    def test_str_book(self):
        self.assertEqual(str(self.book1), 't1')
        self.assertEqual(str(self.book2), 't2')
        
    def test_booklist_book(self):
        resp1 = self.client.get("/booklist/100/109/")
        resp2 = self.client.get("/booklist/130/111/")
        
        self.assertEqual(resp1.status_code, 200)
        self.assertEqual(resp2.status_code, 200)

        self.assertTemplateUsed(resp1, "booklist.html")
        self.assertTemplateUsed(resp2, "booklist.html")

        self.assertContains(resp1, 't4')
        self.assertContains(resp1, 't5')
        self.assertContains(resp1, 't6')

        self.assertContains(resp2, 't2')
        self.assertContains(resp2, 't3')
        self.assertContains(resp2, 't4')
        self.assertContains(resp2, 't5')
        self.assertContains(resp2, 't6')
    
   