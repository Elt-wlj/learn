from time import sleep 

def login(self,user,pwd):
    self.driver.find_element_by_id('LAY-user-login-username').send_keys('guest001')
    sleep(3)
    self.driver.find_element_by_id('LAY-user-login-password').send_keys('Qwer1234')
    self.driver.find_element_by_id('login').click()
    sleep(3)

