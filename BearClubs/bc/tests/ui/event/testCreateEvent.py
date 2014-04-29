from django.test import LiveServerTestCase
from selenium.webdriver.phantomjs.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from urlparse import urljoin

class CreateEventTest(LiveServerTestCase):
  fixtures = ['test_data.json']

  @classmethod
  def setUpClass(cls):
    cls.selenium = WebDriver()
    cls.selenium.implicitly_wait(3)
    cls.selenium.set_page_load_timeout(3)
    super(CreateEventTest, cls).setUpClass()


  @classmethod
  def tearDownClass(cls):
    cls.selenium.refresh()
    cls.selenium.quit()
    super(CreateEventTest, cls).tearDownClass()

 
  def test_successfulCreateEvent(self):
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

    url = urljoin(self.live_server_url, '/events/new')
    self.selenium.get(url)

    #input add event stuff
    name_input = self.selenium.find_element_by_xpath("//input[@id='id_name']")
    description_input = self.selenium.find_element_by_xpath("//textarea[@id='id_description']")
    organization_input = self.selenium.find_element_by_xpath("//select[@id='id_organization']/option[text()='Organization: Test Club']").click()
    start_time_input = self.selenium.find_element_by_xpath("//input[@id='id_start_time']")
    end_time_input = self.selenium.find_element_by_xpath("//input[@id='id_end_time']")
    location_input = self.selenium.find_element_by_xpath("//input[@id='id_location']")
    name_input.send_keys('Test Event')
    description_input.send_keys('This is a Test Event')
    start_time_input.send_keys('12/12/2030 12:00:00 PM')
    end_time_input.send_keys('12/13/2030 12:00:00 PM')
    location_input.send_keys('Dwinelle Hall')
    self.selenium.find_element_by_xpath("//form//input[@value='Submit']").click()
    body = self.selenium.find_element_by_tag_name('body')
    self.assertIn('Test Event', body.text)

  def test_successfulCreateEventNoLocation(self):
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

    url = urljoin(self.live_server_url, '/events/new')
    self.selenium.get(url)

    #input add event stuff
    name_input = self.selenium.find_element_by_xpath("//input[@id='id_name']")
    description_input = self.selenium.find_element_by_xpath("//textarea[@id='id_description']")
    organization_input = self.selenium.find_element_by_xpath("//select[@id='id_organization']/option[text()='Organization: Test Club']").click()
    start_time_input = self.selenium.find_element_by_xpath("//input[@id='id_start_time']")
    end_time_input = self.selenium.find_element_by_xpath("//input[@id='id_end_time']")
    name_input.send_keys('Test Event')
    description_input.send_keys('This is a Test Event')
    start_time_input.send_keys('12/12/2030 12:00:00 PM')
    end_time_input.send_keys('12/13/2030 12:00:00 PM')
    self.selenium.find_element_by_xpath("//form//input[@value='Submit']").click()
    body = self.selenium.find_element_by_tag_name('body')
    self.assertIn('Test Event', body.text)

  def test_successfulCreateEventNoDescription(self):
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

    url = urljoin(self.live_server_url, '/events/new')
    self.selenium.get(url)

    #input add event stuff
    name_input = self.selenium.find_element_by_xpath("//input[@id='id_name']") 
    organization_input = self.selenium.find_element_by_xpath("//select[@id='id_organization']/option[text()='Organization: Test Club']").click()
    start_time_input = self.selenium.find_element_by_xpath("//input[@id='id_start_time']")
    end_time_input = self.selenium.find_element_by_xpath("//input[@id='id_end_time']")
    name_input.send_keys('Test Event')
    start_time_input.send_keys('12/12/2030 12:00:00 PM')
    end_time_input.send_keys('12/13/2030 12:00:00 PM')
    self.selenium.find_element_by_xpath("//form//input[@value='Submit']").click()
    body = self.selenium.find_element_by_tag_name('body')
    self.assertIn('Test Event', body.text)

  def test_noEventName(self):
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

    url = urljoin(self.live_server_url, '/events/new')
    self.selenium.get(url)

    #input add event stuff
    organization_input = self.selenium.find_element_by_xpath("//select[@id='id_organization']/option[text()='Organization: Test Club']").click()
    start_time_input = self.selenium.find_element_by_xpath("//input[@id='id_start_time']")
    end_time_input = self.selenium.find_element_by_xpath("//input[@id='id_end_time']")

    start_time_input.send_keys('12/12/2030 12:00:00 PM')
    end_time_input.send_keys('12/13/2030 12:00:00 PM')
    self.selenium.find_element_by_xpath("//form//input[@value='Submit']").click()
    body = self.selenium.find_element_by_tag_name('body')
    self.assertIn('This field is required', body.text)

  def test_noOrganization(self):
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

    url = urljoin(self.live_server_url, '/events/new')
    self.selenium.get(url)

    #input add event stuff
    name_input = self.selenium.find_element_by_xpath("//input[@id='id_name']") 
    start_time_input = self.selenium.find_element_by_xpath("//input[@id='id_start_time']")
    end_time_input = self.selenium.find_element_by_xpath("//input[@id='id_end_time']")
    name_input.send_keys('Test Event')
    start_time_input.send_keys('12/12/2030 12:00:00 PM')
    end_time_input.send_keys('12/13/2030 12:00:00 PM')
    self.selenium.find_element_by_xpath("//form//input[@value='Submit']").click()
    body = self.selenium.find_element_by_tag_name('body')
    self.assertIn('This field is required', body.text)

  def test_noStartTime(self):
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

    url = urljoin(self.live_server_url, '/events/new')
    self.selenium.get(url)

    #input add event stuff
    name_input = self.selenium.find_element_by_xpath("//input[@id='id_name']") 
    organization_input = self.selenium.find_element_by_xpath("//select[@id='id_organization']/option[text()='Organization: Test Club']").click()
    end_time_input = self.selenium.find_element_by_xpath("//input[@id='id_end_time']")
    name_input.send_keys('Test Event')
    end_time_input.send_keys('12/13/2030 12:00:00 PM')
    self.selenium.find_element_by_xpath("//form//input[@value='Submit']").click()
    body = self.selenium.find_element_by_tag_name('body')
    self.assertIn('This field is required', body.text)
