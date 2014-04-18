from BearClubs.bc.models import User

from django.test import LiveServerTestCase, Client

from selenium.webdriver.phantomjs.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from urlparse import urljoin

class UserDashboardTests(LiveServerTestCase):
    fixtures = ['test_data.json']

    @classmethod
    def setUpClass(cls):
        cls.client = Client();
        cls.selenium = WebDriver();
        cls.selenium.implicitly_wait(3);

        super(UserDashboardTests, cls).setUpClass();

    def setUp(self):
        self.selenium.get(urljoin(self.live_server_url, '/login/'));

        username_input = self.selenium.find_element_by_xpath("//form[@class='login']//input[@id='id_username']");
        password_input = self.selenium.find_element_by_xpath("//form[@class='login']//input[@id='id_password']");
        username_input.send_keys('test');
        password_input.send_keys('1234');

        self.selenium.find_element_by_xpath("//form[@class='login']//input[@value='Log In']").click();


    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(UserDashboardTests, cls).tearDownClass()


    def test_dashboardRenders(self):
        url = urljoin(self.live_server_url, '/user/')
        self.selenium.get(url)

        body = self.selenium.find_element_by_tag_name('body')
        self.assertIn('Dashboard', body.text)

    def test_dashboardHasUserName(self):
        url = urljoin(self.live_server_url, '/user/')
        self.selenium.get(url)

        body = self.selenium.find_element_by_tag_name('body')
        self.assertIn('test', body.text)

    def test_dashboardHasEmail(self):
        url = urljoin(self.live_server_url, '/user/')
        self.selenium.get(url)

        body = self.selenium.find_element_by_tag_name('body')
        self.assertIn('test@gmail.com', body.text)

    def test_dashboardHasEvent(self):
        url = urljoin(self.live_server_url, '/user/')
        self.selenium.get(url)

        body = self.selenium.find_element_by_tag_name('body')
        self.assertIn('Test Event', body.text)

