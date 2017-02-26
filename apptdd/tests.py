from django.test import TestCase
from django.core.urlresolvers import resolve
from apptdd.views import home
from django.template.loader import render_to_string
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
        self.assertIn('To-Do',resp.content.decode())
        self.assertTrue(resp.content.endswith(b'</html>'))
    def test_renderTOstring(self):
        req=HttpRequest()
        resp=home(req)
        expected_html=render_to_string('home.html')
        self.assertEqual(expected_html,resp.content.decode())
    def test_home_can_save_post_data(self):
        res=HttpRequest()
        res.method="POST"
        res.POST['new a item']="a new list item"

        resp=home(res)
        print(resp.content.decode())

        self.assertIn('a new list item',resp.content.decode())
        excepted_html=render_to_string('home.html',{'new_item_text':'a new list item'})
        print(excepted_html)
        self.assertEqual(resp.content.decode(),excepted_html)