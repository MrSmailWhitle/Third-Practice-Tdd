from django.test import TestCase
from django.core.urlresolvers import resolve
# Create your tests here.
class homepage(TestCase):
    def test_resolveHomePage(self):
        resolver=resolve('/')