from django.test import TestCase
from books_fbv.models import Book

# Create your tests here.


class BookFBVTestCase(TestCase):
    def setUp(self):
        Book.objects.create(name="lion", pages=1)
        Book.objects.create(name="cat", pages=2)

    def test_create_book_1(self):
        """Animals that can speak are correctly identified"""
        lion = Book.objects.get(name="lion")
        cat = Book.objects.get(name="cat")
        self.assertEqual(lion.pages, 1)
        self.assertEqual(cat.pages, 2)
    
    def test_create_book_2(self):
        """Animals that can speak are correctly identified"""
        lion = Book.objects.get(name="lion")
        cat = Book.objects.get(name="cat")
        self.assertEqual(lion.pages, 1)
        self.assertEqual(cat.pages, 2)
    
    def test_create_book_3(self):
        """Animals that can speak are correctly identified"""
        lion = Book.objects.get(name="lion")
        cat = Book.objects.get(name="cat")
        self.assertEqual(lion.pages, 1)
        self.assertEqual(cat.pages, 2)
    
    def test_create_book_4(self):
        """Animals that can speak are correctly identified"""
        lion = Book.objects.get(name="lion")
        cat = Book.objects.get(name="cat")
        self.assertEqual(lion.pages, 1)
        self.assertEqual(cat.pages, 2)
    
    def test_create_book_5(self):
        """Animals that can speak are correctly identified"""
        lion = Book.objects.get(name="lion")
        cat = Book.objects.get(name="cat")
        self.assertEqual(lion.pages, 1)
        self.assertEqual(cat.pages, 2)
    
    def test_create_book_6(self):
        """Animals that can speak are correctly identified"""
        lion = Book.objects.get(name="lion")
        cat = Book.objects.get(name="cat")
        self.assertEqual(lion.pages, 1)
        self.assertEqual(cat.pages, 2)
