from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=r"C:\\Users\\Muhd Arif Bin Rawi\\chromedriver_win32\\chromedriver.exe")
    
    def tearDown(self):
        self.browser.quit()

    def test_basicTest(self):
        self.browser.get("http://127.0.0.1:5000/")
        self.assertIn("To-Do", self.browser.title)
        self.fail("finish the test!")

if __name__ == "__main__":
    unittest.main(warnings="ignore")






