class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = 'username'
        self.password_field = 'password'
        self.login_button = 'login-button'

    def open(self):
        self.driver.get('http://www.saucedemo.com')

    def enter_username(self, username):
        field = self.driver.find_element('id', 'username_field')
        field.clear()
        field.send_keys(username)
    def enter_password(self, password):
        field = self.driver.find_element('id', 'password')
        field.clear()
        field.send_keys(password)
    def click_login(self):
        button = self.driver.find_element('id', 'login_button')
        button.click()
