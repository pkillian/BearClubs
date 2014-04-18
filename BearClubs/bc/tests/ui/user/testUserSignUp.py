from BearClubs.bc.models import User

from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from urlparse import urljoin

class UserSignUpTests(LiveServerTestCase):
  fixtures = ['test_data.json']

  @classmethod
  def setUpClass(cls):
    cls.selenium = WebDriver()
    cls.selenium.implicitly_wait(3)
    super(UserSignUpTests, cls).setUpClass()


  @classmethod
  def tearDownClass(cls):
    cls.selenium.quit()
    super(UserSignUpTests, cls).tearDownClass()
    

  def test_successfulSignUp(self):
    url = urljoin(self.live_server_url, '/login/')
    self.selenium.get(url)
    username_input = self.selenium.find_element_by_xpath("//form[@class='signup']//input[@id='id_username']")
    email_input = self.selenium.find_element_by_xpath("//form[@class='signup']//input[@id='id_email']")
    password_input = self.selenium.find_element_by_xpath("//form[@class='signup']//input[@id='id_password1']")
    confirm_password_input = self.selenium.find_element_by_xpath("//form[@class='signup']//input[@id='id_password2']")
    username_input.send_keys('testerman')
    email_input.send_keys('testerman@test.com')
    password_input.send_keys('1234')
    confirm_password_input.send_keys('1234')
    self.selenium.find_element_by_xpath("//form[@class='signup']//input[@value='Register']").click()
    body = self.selenium.find_element_by_tag_name('body')
    self.assertIn('Club Directory', body.text)

  def test_UserNameExists(self):
    url = urljoin(self.live_server_url, '/login/')
    self.selenium.get(url)
    username_input = self.selenium.find_element_by_xpath("//form[@class='signup']//input[@id='id_username']")
    email_input = self.selenium.find_element_by_xpath("//form[@class='signup']//input[@id='id_email']")
    password_input = self.selenium.find_element_by_xpath("//form[@class='signup']//input[@id='id_password1']")
    confirm_password_input = self.selenium.find_element_by_xpath("//form[@class='signup']//input[@id='id_password2']")
    username_input.send_keys('test')
    email_input.send_keys('test@test.com')
    password_input.send_keys('1234')
    confirm_password_input.send_keys('1234')
    self.selenium.find_element_by_xpath("//form[@class='signup']//input[@value='Register']").click()
    body = self.selenium.find_element_by_tag_name('body')
    self.assertIn('A user with that username already exists', body.text)

  def test_noUserName(self):
    url = urljoin(self.live_server_url, '/login/')
    self.selenium.get(url)
    email_input = self.selenium.find_element_by_xpath("//form[@class='signup']//input[@id='id_email']")
    password_input = self.selenium.find_element_by_xpath("//form[@class='signup']//input[@id='id_password1']")
    confirm_password_input = self.selenium.find_element_by_xpath("//form[@class='signup']//input[@id='id_password2']")
    email_input.send_keys('test@test.com')
    password_input.send_keys('1234')
    confirm_password_input.send_keys('1234')
    self.selenium.find_element_by_xpath("//form[@class='signup']//input[@value='Register']").click()
    body = self.selenium.find_element_by_tag_name('body')
    self.assertIn('This field is required', body.text)
  
  def test_noPassword(self):
    url = urljoin(self.live_server_url, '/login/')
    self.selenium.get(url)
    username_input = self.selenium.find_element_by_xpath("//form[@class='signup']//input[@id='id_username']")
    email_input = self.selenium.find_element_by_xpath("//form[@class='signup']//input[@id='id_email']")
    
    confirm_password_input = self.selenium.find_element_by_xpath("//form[@class='signup']//input[@id='id_password2']")
    username_input.send_keys('test')
    email_input.send_keys('test@test.com')

    confirm_password_input.send_keys('1234')
    self.selenium.find_element_by_xpath("//form[@class='signup']//input[@value='Register']").click()
    body = self.selenium.find_element_by_tag_name('body')
    self.assertIn('This field is required', body.text)

  def test_noPasswordConfirmation(self):
    url = urljoin(self.live_server_url, '/login/')
    self.selenium.get(url)
    username_input = self.selenium.find_element_by_xpath("//form[@class='signup']//input[@id='id_username']")
    email_input = self.selenium.find_element_by_xpath("//form[@class='signup']//input[@id='id_email']")
    password_input = self.selenium.find_element_by_xpath("//form[@class='signup']//input[@id='id_password1']")
    
    username_input.send_keys('test')
    email_input.send_keys('test@test.com')
    password_input.send_keys('1234')

    self.selenium.find_element_by_xpath("//form[@class='signup']//input[@value='Register']").click()
    body = self.selenium.find_element_by_tag_name('body')
    self.assertIn('This field is required', body.text)

  def test_noEmail(self):
    url = urljoin(self.live_server_url, '/login/')
    self.selenium.get(url)
    username_input = self.selenium.find_element_by_xpath("//form[@class='signup']//input[@id='id_username']")
    
    password_input = self.selenium.find_element_by_xpath("//form[@class='signup']//input[@id='id_password1']")
    confirm_password_input = self.selenium.find_element_by_xpath("//form[@class='signup']//input[@id='id_password2']")
    username_input.send_keys('test')
 
    password_input.send_keys('1234')
    confirm_password_input.send_keys('1234')
    self.selenium.find_element_by_xpath("//form[@class='signup']//input[@value='Register']").click()
    body = self.selenium.find_element_by_tag_name('body')
    self.assertIn('This field is required', body.text)
  
  def test_PasswordsDontMatch(self):
    url = urljoin(self.live_server_url, '/login/')
    self.selenium.get(url)
    username_input = self.selenium.find_element_by_xpath("//form[@class='signup']//input[@id='id_username']")
    email_input = self.selenium.find_element_by_xpath("//form[@class='signup']//input[@id='id_email']")
    password_input = self.selenium.find_element_by_xpath("//form[@class='signup']//input[@id='id_password1']")
    confirm_password_input = self.selenium.find_element_by_xpath("//form[@class='signup']//input[@id='id_password2']")
    username_input.send_keys('test')
    email_input.send_keys('test@test.com')
    password_input.send_keys('1234')
    confirm_password_input.send_keys('1234566')
    self.selenium.find_element_by_xpath("//form[@class='signup']//input[@value='Register']").click()
    body = self.selenium.find_element_by_tag_name('body')
    self.assertIn("The two password fields didn't match", body.text)





