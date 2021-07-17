from django.test import TestCase

from .models import Member, Book, Borrowed

class MemberTest(TestCase):

    def setUp(self):
        p1 = Member.objects.create(first_name= 'f1', last_name= 'l1')
        p2 = Member.objects.create(first_name= 'f2', last_name= 'l2')
        # p3 = Member.objects.create(first_name= 'f3', last_name= 'l3')
        # p4 = Member(first_name= 'f4', last_name= 'l4')
        # p5 = Member(first_name= 'f5', last_name= 'l5')

        b1 = Book.objects.create(title= 'b1', genre= 'g1')
        b2 = Book.objects.create(title= 'b2', genre= 'g1')
        b3 = Book.objects.create(title= 'b3', genre= 'g2')
        b4 = Book.objects.create(title= 'b4', genre= 'g2')
        b5 = Book.objects.create(title= 'b5', genre= 'g3')
        b6 = Book.objects.create(title= 'b6', genre= 'g3')
        b7 = Book.objects.create(title= 'b7', genre= 'g4')
        b8 = Book.objects.create(title= 'b8', genre= 'g4')

        Borrowed.objects.create(member= p1, book= b1)
        Borrowed.objects.create(member= p1, book= b2)
        Borrowed.objects.create(member= p1, book= b3)

        Borrowed.objects.create(member= p2, book= b4)
        Borrowed.objects.create(member= p2, book= b5)
        Borrowed.objects.create(member= p2, book= b6)
        Borrowed.objects.create(member= p2, book= b7)
        Borrowed.objects.create(member= p2, book= b8)

    def test_borrowed_books(self):
        p1 = Member.objects.get(first_name = 'f1')
        p2 = Member.objects.get(first_name = 'f2')
        # p3 = Member.objects.get(first_name = 'f3')
        
        list11 = p1.borrowed_books('g1') #2
        list12 = p1.borrowed_books('g2') #1
        list13 = p1.borrowed_books('g3') #0
         
        list21 = p2.borrowed_books('g1') #0
        list22 = p2.borrowed_books('g2') #1
        list23 = p2.borrowed_books('g3') #2
        list24 = p2.borrowed_books('g4') #2
        
        # check list lengths
        self.assertFalse(None in [list11, list12, list13, list21, list22, list23, list24])
        
        self.assertEqual(len(list11), 2)
        self.assertEqual(len(list12), 1)
        self.assertEqual(len(list13), 0)

        self.assertEqual(len(list21), 0)
        self.assertEqual(len(list22), 1)
        self.assertEqual(len(list23), 2)
        self.assertEqual(len(list24), 2)
            
        
        self.assertEqual(list(list11), [1, 2])
        self.assertEqual(list(list12), [3])
        self.assertEqual(list(list13), [])

        self.assertEqual(list(list21), [])
        self.assertEqual(list(list22), [4])
        self.assertEqual(list(list23), [5, 6])
        self.assertEqual(list(list24), [7, 8])
