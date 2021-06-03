from datetime import date
from django.test import TestCase, Client
import html
from library_management.models import Book


class TestAll(TestCase):
    def setUp(self):
        self.cli = Client()

    def test_sample1(self):
        Book.objects.create(author='PollARD berrier', title="eND OF OUR dAyS", publication_date=date(2020, 5, 4),
                            text="hOLding mE DOWN I CAN\'T Believe I am DroWninG sOMEHOW FaLL to MY KNEES I CAN\'T Believe WHAT I see")
        Book.objects.create(author='darius KEELER', title="collapse collide", publication_date=date(2014, 12, 31),
                            text="tOO LATE TheY HATE TOO LATE ThEy HaTE yOU\'ve JADED THEy've faded from YOUR Heart And You DIDN'T")

        response = self.cli.get('/booklist/')
        result = html.unescape(response.content.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('POLLARD BERRIER' in result)
        self.assertTrue('End Of Our Days' in result)
        self.assertTrue('Mon 04 May 2020' in result)
        self.assertTrue(("Holding me down i can't believe i am drowning somehow fall to my knees i ..." in result) or (
                "Holding me down i can't believe i am drowning somehow fall to my knees i …" in result))

        self.assertTrue('DARIUS KEELER' in result)
        self.assertTrue('Collapse Collide' in result)
        self.assertTrue('Wed 31 Dec 2014' in result)
        self.assertTrue(
            ("Too late they hate too late they hate you've jaded they've faded from your heart ..." in result) or (
                    "Too late they hate too late they hate you've jaded they've faded from your heart …" in result))

    def test_sample2(self):
        Book.objects.create(author='Mohammad', title="first booK", publication_date=date(2021, 1, 1),
                            text='Many birds and animals live in the world, for example, parrots, pandas, lions, leopards and rabbits. In the sea we can find whales, dolphins, sharks and octopuses.')
        Book.objects.create(author='saJJad', title="sEcOnD", publication_date=date(2010, 10, 10),
                            text='bargharari aziz?')

        response = self.cli.get('/booklist/')

        self.assertEqual(response.status_code, 200)

        self.assertTrue('MOHAMMAD' in response.content.decode('utf-8'))
        self.assertTrue('First Book' in response.content.decode('utf-8'))
        self.assertTrue('Fri 01 Jan 2021' in response.content.decode('utf-8'))
        self.assertTrue((
                                'Many birds and animals live in the world, for example, parrots, pandas, lions, leopards and ...' in response.content.decode(
                            'utf-8')) or (
                                'Many birds and animals live in the world, for example, parrots, pandas, lions, leopards and …' in response.content.decode(
                            'utf-8')))
        self.assertTrue('SAJJAD' in response.content.decode('utf-8'))
        self.assertTrue('Second' in response.content.decode('utf-8'))
        self.assertTrue('Sun 10 Oct 2010' in response.content.decode('utf-8'))
        self.assertTrue('Bargharari aziz?' in response.content.decode('utf-8'))
