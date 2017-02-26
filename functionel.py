from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
class VisitorThehome(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Ie()
        self.browser.implicitly_wait(10)
    def tearDown(self):
        self.browser.quit()

    def test_newViseter_begin_input(self):
        self.browser.get("http://localhost:8000")
        print(self.browser.title)
        time.sleep(10)
        self.assertIn('To-Do',self.browser.title)
        time.sleep(1)
        headtxt=self.browser.find_element_by_tag_name('h1')
        self.assertIn('To Do',headtxt.text)
        inputbox=self.browser.find_element_by_id('id_new_item')
        self.assertEqual("add a new list",inputbox.get_attribute("placeholder"))

        inputbox.send_keys("Lilei,Phone my girl friend")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(5)
        table=self.browser.find_element_by_id("list_of_to_do")
        items=table.find_elements_by_tag_name('tr')
        self.assertIn(
             "1.Lilei,Phone my girl friend",[item.text for item in items],"not find your item,maybe error--it text"
         )

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys("Lilei,Call to mum hello")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(5)
        table = self.browser.find_element_by_id("list_of_to_do")
        items = table.find_elements_by_tag_name('tr')
        self.assertIn(
            "Lilei,Phone my girl friend", [item.text for item in items], "not find your item,maybe error--it text"
        )
        self.assertIn(
            "2.Lilei,Call to mum hello", [item.text for item in items], "not find your item,maybe error--it text"
        )
        


        self.fail("finishd the test")

if __name__=='__main__':
    unittest.main(warnings='ignore')