from BearClubs.bc.models import User

from django.test import LiveServerTestCase, Client

import haystack

from selenium.webdriver.phantomjs.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

from urlparse import urljoin

class SearchResultsTests(LiveServerTestCase):
    fixtures = ['test_data.json']

    @classmethod
    def setUpClass(cls):
        haystack.connections.reload('test');

        cls.client = Client();
        cls.selenium = WebDriver();
        cls.selenium.implicitly_wait(3);
        cls.selenium.set_page_load_timeout(3)

        super(SearchResultsTests, cls).setUpClass();

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
        super(SearchResultsTests, cls).tearDownClass()


    def test_searchRenders(self):
        url = urljoin(self.live_server_url, '/search/')
        self.selenium.get(url)

        body = self.selenium.find_element_by_tag_name('body')
        self.assertIn('Search', body.text)

    def test_searchEvent(self):
        url = urljoin(self.live_server_url, '/search/')
        self.selenium.get(url)

        checkBox = self.selenium.find_element_by_xpath("//form//input[@id='id_models_0']");
        checkBox.click();
        
        searchInput = self.selenium.find_element_by_xpath("//form//input[@id='id_q']");
        searchInput.send_keys('test');

        submitButton = self.selenium.find_element_by_xpath("//form//input[@class='button']");
        submitButton.click();

        body = self.selenium.find_element_by_tag_name('body')
        self.assertIn('Event: Test Event', body.text)

    def test_searchOrganization(self):
        url = urljoin(self.live_server_url, '/search/')
        self.selenium.get(url)

        checkBox = self.selenium.find_element_by_xpath("//form//input[@id='id_models_1']");
        checkBox.click();
        
        searchInput = self.selenium.find_element_by_xpath("//form//input[@id='id_q']");
        searchInput.send_keys('test');

        submitButton = self.selenium.find_element_by_xpath("//form//input[@class='button']");
        submitButton.click();

        body = self.selenium.find_element_by_tag_name('body')
        self.assertIn('Organization: Test', body.text)

    # def test_searchUser(self):
    #     url = urljoin(self.live_server_url, '/search/')
    #     self.selenium.get(url)

    #     checkBox = self.selenium.find_element_by_xpath("//form//input[@id='id_models_2']");
    #     checkBox.click();
        
    #     searchInput = self.selenium.find_element_by_xpath("//form//input[@id='id_q']");
    #     searchInput.send_keys('test');

    #     submitButton = self.selenium.find_element_by_xpath("//form//input[@class='button']");
    #     submitButton.click();

    #     body = self.selenium.find_element_by_tag_name('body')
    #     self.assertIn('User: test', body.text)