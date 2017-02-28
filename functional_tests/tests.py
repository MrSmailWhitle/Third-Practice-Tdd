from selenium import webdriver
#import unittest
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import time
class VisitorThehome(LiveServerTestCase):
    def setUp(self):
        self.browser=webdriver.Ie()
        self.browser.implicitly_wait(10)
    def tearDown(self):
        self.browser.quit()
    def check_out_todo_list_item(self,item_txt):
        table=self.browser.find_element_by_id("list_of_to_do")
        rows=table.find_elements_by_tag_name('tr')
        self.assertIn(item_txt,[row.text for row in rows])

    def test_newViseter_begin_input(self):
        self.browser.get(self.live_server_url)
        print(self.browser.title)
        #time.sleep(10)
        self.assertIn('To-Do',self.browser.title)
        time.sleep(1)
        headtxt=self.browser.find_element_by_tag_name('h1')
        self.assertIn('To Do',headtxt.text)
        inputbox=self.browser.find_element_by_id('id_new_item')
        self.assertEqual("add a new list",inputbox.get_attribute("placeholder"))

        inputbox.send_keys("Lilei,Phone my girl friend")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(3)
        self.check_out_todo_list_item('1.Lilei,Phone my girl friend')

        time.sleep(2)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys("Lilei,Call to mum hello")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(3)
        self.check_out_todo_list_item('2.Lilei,Call to mum hello')
        self.check_out_todo_list_item('1.Lilei,Phone my girl friend')

        self.fail("finishd the test")

#if __name__=='__main__':
   # unittest.main(warnings='ignore')