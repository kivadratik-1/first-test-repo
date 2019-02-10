from django.test import TestCase

# Create your tests here.

from .models import SimpleGuest

class GuestModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        #SimpleGuest.objects.create(simple_guest_name='Big')
        SimpleGuest.objects.create(simple_guest_name='Big', simple_guest_id = 1 )

    def test_simple_guest_name_verbose_name(self):
        guest=SimpleGuest.objects.get(simple_guest_id=1)
        field_label = guest._meta.get_field('simple_guest_name').verbose_name
        self.assertEquals(field_label,'Впиши сюда свое имя:')

    def test_simple_guest_name_max_length(self):
        guest=SimpleGuest.objects.get(simple_guest_id=1)
        max_length = guest._meta.get_field('simple_guest_name').max_length
        self.assertEquals(max_length,200)


class TestSimpleGuest(TestCase):
    def tett_missing_date(self):
        pass


