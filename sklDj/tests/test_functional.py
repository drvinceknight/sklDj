from selenium import webdriver
import unittest

class VisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get('http://localhost:8000/frontend')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()


class NewVisitorTest(VisitorTest):

    def test_can_read_the_home_page(self):

        # Geraint checks that the title shows that he's in the correct place.
        self.assertIn('sklDj', self.browser.title)

if __name__ == '__main__':
    unittest.main()
