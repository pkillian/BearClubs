from BearClubs.bc.models import User

from django.test import LiveServerTestCase, Client

from selenium.webdriver.phantomjs.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from urlparse import urljoin

class UserProfileTests(LiveServerTestCase):
    fixtures = ['test_data.json']

    @classmethod
    def setUpClass(cls):
        cls.client = Client();
        cls.selenium = WebDriver();
        cls.selenium.implicitly_wait(3);
        cls.selenium.set_page_load_timeout(3)

        super(UserProfileTests, cls).setUpClass();

    def setUp(self):
        self.selenium.get(urljoin(self.live_server_url, '/login/'));

        username_input = self.selenium.find_element_by_xpath("//form[@class='login']//input[@id='id_username']");
        password_input = self.selenium.find_element_by_xpath("//form[@class='login']//input[@id='id_password']");
        username_input.send_keys('test');
        password_input.send_keys('1234');

        self.selenium.find_element_by_xpath("//form[@class='login']//input[@value='Log In']").click();


    @classmethod
    def tearDownClass(cls):
        cls.selenium.refresh()
        cls.selenium.quit()
        super(UserProfileTests, cls).tearDownClass()


    def test_profileRenders(self):
        url = urljoin(self.live_server_url, '/user/1')
        self.selenium.get(url)

        body = self.selenium.find_element_by_tag_name('body')
        self.assertIn('Profile', body.text)

    def test_profileHasUserName(self):
        url = urljoin(self.live_server_url, '/user/1')
        self.selenium.get(url)

        body = self.selenium.find_element_by_tag_name('body')
        self.assertIn('test', body.text)

    def test_profileHasEmail(self):
        url = urljoin(self.live_server_url, '/user/1')
        self.selenium.get(url)

        body = self.selenium.find_element_by_tag_name('body')
        self.assertIn('(test@gmail.com)', body.text)

    def test_profileHasOrganization(self):
        url = urljoin(self.live_server_url, '/user/1')
        self.selenium.get(url)

        body = self.selenium.find_element_by_tag_name('body')
        self.assertIn('Test Club', body.text)

    def test_profileHasEvent(self):
        url = urljoin(self.live_server_url, '/user/1')
        self.selenium.get(url)

        body = self.selenium.find_element_by_tag_name('body')
        self.assertIn('Test Event', body.text)

