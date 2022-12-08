import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class BaseTest(unittest.TestCase):
    """Base test class"""

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://www.vlance.vn/dang-cuoc-thi')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.delete_all_cookies()

    def tearDown(self):
        self.driver.quit()
