from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from urlparse import urljoin

class CreateOrganizationTest(LiveServerTestCase):
  fixtures = ['test_data.json']

  @classmethod
  def setUpClass(cls):
    cls.selenium = WebDriver()
    cls.selenium.implicitly_wait(3)
    super(CreateOrganizationTest, cls).setUpClass()


  @classmethod
  def tearDownClass(cls):
    cls.selenium.quit()
    super(CreateOrganizationTest, cls).tearDownClass()


  def test_successfulCreateOrganization(self):
    #login the user
    url = urljoin(self.live_server_url, '/login/')
    self.selenium.get(url)
    username_input = self.selenium.find_element_by_xpath("//form[@class='login']//input[@id='id_username']")
    password_input = self.selenium.find_element_by_xpath("//form[@class='login']//input[@id='id_password']")
    username_input.send_keys('test')
    password_input.send_keys('1234')
    self.selenium.find_element_by_xpath("//form[@class='login']//input[@value='Log In']").click()
    body = self.selenium.find_element_by_tag_name('body')
    self.assertIn('Dashboard', body.text)

    #click on club tab
    self.selenium.find_element_by_xpath("//div[@class='header-button first']").click()
    body = self.selenium.find_element_by_tag_name('body')
    self.assertIn('Club Directory', body.text)

    #click on add club
    self.selenium.find_element_by_xpath("//a[contains(@href,'/clubs/new')]").click()
    body = self.selenium.find_element_by_tag_name('body')
    self.assertIn('Add a New Organization', body.text)

    #input add organization stuff
    name_input = self.selenium.find_element_by_xpath("//input[@id='id_name']")
    description_input = self.selenium.find_element_by_xpath("//textarea[@id='id_description']")
    organization_input = self.selenium.find_element_by_xpath("//select[@id='id_organization_type']/option[text()='Business']").click()
    name_input.send_keys('Test Club')
    description_input.send_keys('This is a Test Club')
    self.selenium.find_element_by_xpath("//form//input[@value='Submit']").click()
    body = self.selenium.find_element_by_tag_name('body')
    self.assertIn('Test Club', body.text)
  
  def test_successfulCreateOrganizationWithNoDescription(self):
    #login the user
    url = urljoin(self.live_server_url, '/login/')
    self.selenium.get(url)
    username_input = self.selenium.find_element_by_xpath("//form[@class='login']//input[@id='id_username']")
    password_input = self.selenium.find_element_by_xpath("//form[@class='login']//input[@id='id_password']")
    username_input.send_keys('test')
    password_input.send_keys('1234')
    self.selenium.find_element_by_xpath("//form[@class='login']//input[@value='Log In']").click()
    body = self.selenium.find_element_by_tag_name('body')
    self.assertIn('Dashboard', body.text)

    #click on club tab
    self.selenium.find_element_by_xpath("//div[@class='header-button first']").click()
    body = self.selenium.find_element_by_tag_name('body')
    self.assertIn('Club Directory', body.text)

    #click on add club
    self.selenium.find_element_by_xpath("//a[contains(@href,'/clubs/new')]").click()
    body = self.selenium.find_element_by_tag_name('body')
    self.assertIn('Add a New Organization', body.text)

    #input add organization stuff
    name_input = self.selenium.find_element_by_xpath("//input[@id='id_name']")
   
    organization_input = self.selenium.find_element_by_xpath("//select[@id='id_organization_type']/option[text()='Business']").click()
    name_input.send_keys('Test Club No Description')
    
    self.selenium.find_element_by_xpath("//form//input[@value='Submit']").click()
    body = self.selenium.find_element_by_tag_name('body')
    self.assertIn('Test Club No Description', body.text)

  def test_noOrganizationName(self):
    #login the user
    url = urljoin(self.live_server_url, '/login/')
    self.selenium.get(url)
    username_input = self.selenium.find_element_by_xpath("//form[@class='login']//input[@id='id_username']")
    password_input = self.selenium.find_element_by_xpath("//form[@class='login']//input[@id='id_password']")
    username_input.send_keys('test')
    password_input.send_keys('1234')
    self.selenium.find_element_by_xpath("//form[@class='login']//input[@value='Log In']").click()
    body = self.selenium.find_element_by_tag_name('body')
    self.assertIn('Dashboard', body.text)

    #click on club tab
    self.selenium.find_element_by_xpath("//div[@class='header-button first']").click()
    body = self.selenium.find_element_by_tag_name('body')
    self.assertIn('Club Directory', body.text)

    #click on add club
    self.selenium.find_element_by_xpath("//a[contains(@href,'/clubs/new')]").click()
    body = self.selenium.find_element_by_tag_name('body')
    self.assertIn('Add a New Organization', body.text)

    #input add organization stuff
    description_input = self.selenium.find_element_by_xpath("//textarea[@id='id_description']")
    organization_input = self.selenium.find_element_by_xpath("//select[@id='id_organization_type']/option[text()='Business']").click()

    description_input.send_keys('This is a Test Club')
    self.selenium.find_element_by_xpath("//form//input[@value='Submit']").click()
    body = self.selenium.find_element_by_tag_name('body')
    self.assertIn('This field is required', body.text)

  def test_noOrganizationType(self):
    #login the user
    url = urljoin(self.live_server_url, '/login/')
    self.selenium.get(url)
    username_input = self.selenium.find_element_by_xpath("//form[@class='login']//input[@id='id_username']")
    password_input = self.selenium.find_element_by_xpath("//form[@class='login']//input[@id='id_password']")
    username_input.send_keys('test')
    password_input.send_keys('1234')
    self.selenium.find_element_by_xpath("//form[@class='login']//input[@value='Log In']").click()
    body = self.selenium.find_element_by_tag_name('body')
    self.assertIn('Dashboard', body.text)

    #click on club tab
    self.selenium.find_element_by_xpath("//div[@class='header-button first']").click()
    body = self.selenium.find_element_by_tag_name('body')
    self.assertIn('Club Directory', body.text)

    #click on add club
    self.selenium.find_element_by_xpath("//a[contains(@href,'/clubs/new')]").click()
    body = self.selenium.find_element_by_tag_name('body')
    self.assertIn('Add a New Organization', body.text)

    #input add organization stuff
    name_input = self.selenium.find_element_by_xpath("//input[@id='id_name']")
    description_input = self.selenium.find_element_by_xpath("//textarea[@id='id_description']")
    
    name_input.send_keys('Test Club')
    description_input.send_keys('This is a Test Club')
    self.selenium.find_element_by_xpath("//form//input[@value='Submit']").click()
    body = self.selenium.find_element_by_tag_name('body')
    self.assertIn('This field is required', body.text)




