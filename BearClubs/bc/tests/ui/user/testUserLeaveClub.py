from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from urlparse import urljoin

class UserLeaveClubTest(LiveServerTestCase):
  fixtures = ['test_data.json']

  @classmethod
  def setUpClass(cls):
    cls.selenium = WebDriver()
    cls.selenium.implicitly_wait(3)
    super(UserLeaveClubTest, cls).setUpClass()


  @classmethod
  def tearDownClass(cls):
    cls.selenium.quit()
    super(UserLeaveClubTest, cls).tearDownClass()
    
  def test_successfulLeaveClub(self):
    #login the user
    url = urljoin(self.live_server_url, '/login/')
    self.selenium.get(url)
    username_input = self.selenium.find_element_by_xpath("//form[@class='login']//input[@id='id_username']")
    password_input = self.selenium.find_element_by_xpath("//form[@class='login']//input[@id='id_password']")
    username_input.send_keys('tester1')
    password_input.send_keys('test')
    self.selenium.find_element_by_xpath("//form[@class='login']//input[@value='Log In']").click()
    body = self.selenium.find_element_by_tag_name('body')
    self.assertIn('Dashboard', body.text)

    #click on club tab
    self.selenium.find_element_by_xpath("//div[@class='header-button first']").click()
    body = self.selenium.find_element_by_tag_name('body')
    self.assertIn('Club Directory', body.text)

    #click on club
    self.selenium.find_element_by_xpath("//a[contains(@href,'/clubs/1')]").click()
    body = self.selenium.find_element_by_tag_name('body')
    self.assertIn('Description: test123', body.text)

    #click on join club
    self.selenium.find_element_by_xpath("//input[@name='join-club-button']").click()
    body = self.selenium.find_element_by_tag_name('body')
    self.assertIn('You are a member of this club.', body.text)

    #click on leave club
    self.selenium.find_element_by_xpath("//input[@name='leave-club-button']").click()
    body = self.selenium.find_element_by_xpath("//input[@name='join-club-button']")
    self.assertIn('Join Club', body.get_attribute('value'))