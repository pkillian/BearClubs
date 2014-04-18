from BearClubs.bc.models import User

from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from urlparse import urljoin

class UserLoginTests(LiveServerTestCase):
  fixtures = ['test_data.json']

  @classmethod
  def setUpClass(cls):
    cls.selenium = WebDriver()
    cls.selenium.implicitly_wait(3)
    super(UserLoginTests, cls).setUpClass()


  @classmethod
  def tearDownClass(cls):
    cls.selenium.quit()
    super(UserLoginTests, cls).tearDownClass()
    

  def test_login(self):
    url = urljoin(self.live_server_url, '/login/')
    self.selenium.get(url)
    username_input = self.selenium.find_element_by_xpath("//form[@class='login']//input[@id='id_username']")
    password_input = self.selenium.find_element_by_xpath("//form[@class='login']//input[@id='id_password']")
    username_input.send_keys('test')
    password_input.send_keys('1234')
    self.selenium.find_element_by_xpath("//form[@class='login']//input[@value='Log In']").click()
    body = self.selenium.find_element_by_tag_name('body')
    self.assertIn('Dashboard', body.text)