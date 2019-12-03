from selenium.webdriver.common.by import By
from selenium import webdriver
class RegisterPage (object):
    USER_NAME=(By.ID,"username")
    FIRST_NAME=(By.ID,"firstname")
    LAST_NAME=(By.ID,"lastname")
    PASSWORD=(By.NAME,"password")
    CONF_PASS=(By.NAME,"confirmpassword")
    SUBMIT=(By.NAME,"register")
    SIGN_OFF=(By.LINK_TEXT,"SIGN-OFF")
    
    def register(self):
#         self.driver.find_element_partial_link_("SignUp").click()
#         self.driver.find_element(*RegisterPage.)
        self.driver.find_element(*RegisterPage.USER_NAME).send_keys("pravin123")
        self.driver.find_element(*RegisterPage.FIRST_NAME).send_keys("pravin")
        self.driver.find_element(*RegisterPage.LAST_NAME).send_keys("singh")
        self.driver.find_element(*RegisterPage.PASSWORD).send_keys("pravin")
        self.driver.find_element(*RegisterPage.CONF_PASS).send_keys("pravin")
        