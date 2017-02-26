from django.test import TestCase
from django.core.urlresolvers import resolve
from apptdd.views import home
from django.http import HttpRequest
# Create your tests here.
class homepage(TestCase):
    #test the resolve is ok
    def test_resolveHomePage(self):
        resolver=resolve('/')
        self.assertEqual(resolver.func,home)
    #test the response
    def test_homepage_response(self):
        req=HttpRequest()
        resp=home(req)
        self.assertTrue(resp.content.startswith(b'<html>'))

