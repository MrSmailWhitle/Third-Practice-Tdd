from selenium import webdriver
import unittest
import time
class VisitorThehome(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Ie()
        self.browser.implicitly_wait(10)
    def tearDown(self):
        #self.browser.quit()
        pass

    def test_newVisitor_get_the_homepage(self):
        self.browser.get("http://localhost:8000")
        time.sleep(4)
        self.assertIn('To-Do',self.browser.title)
        self.fail("finishd the test")
if __name__=='__main__':
    unittest.main(warnings='ignore')