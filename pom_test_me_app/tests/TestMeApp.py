import unittest
from selenium import webdriver
from pages.LoginPage import LoginPage
from pages.RegisterPage import RegisterPage
class Test (unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome("C:\driver9999\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("http://localhost:8099/TestMeApp")
        self.driver.find_element_by_link_text("SignIn").click()
#         sleep(2000)
        self.driver.implicitly_wait(10)
        pass
    def tearDown(self):
        self.driver.close()
        pass
    def testname(self):
        self.homepage=LoginPage(self.driver)
        self.registerpage=RegisterPage(self.driver)
        self.homepage.clickRegister()
        self.registerpage.register()
        self.registerpage.signoff()
        title=self.homepage.login()
        self.assertEquals(title,'Home')
        pass
    
#     if __name__ == "__main__":
#     #import sys;sys.argv = ['', 'Test.testName']
#      unittest.main()