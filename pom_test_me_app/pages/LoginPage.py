from selenium.webdriver.common.by import By

class LoginPage(object):
    USER_NAME=(By.NAME,"userName")
    PASSWORD=(By.NAME,"password")
    SIGN_IN=(By.XPATH,"//input[@name='Login']")
    #some comments
    
    def login(self):
#         self.driver.find_element_by_link_text("SignIn").click()
        self.driver.find_element(*LoginPage.USER_NAME).send_keys("lalitha")
#         self.driver.find_element(*LoginPage.USER_NAME).send_keys("laitha")
        self.driver.find_element(*LoginPage.PASSWORD).send_keys("password123")
        self.driver.find_element(*LoginPage.SIGN_IN).click()
        return self.driver.title
    def __init__(self,driver):
        self.driver=driver