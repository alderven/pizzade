import os
import configparser
import selenium_methods

CONFIG = 'config.cfg'


class Base(object):

    def __init__(self, driver):
        self.driver = driver

    @property
    def config(self):
        cfg = configparser.ConfigParser()
        cfg_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), CONFIG)
        cfg.read(cfg_path)
        return cfg


class Home(Base):

    def open_page(self):
        return self.driver.get(self.config['SITE']['URL'])

    def einloggen(self):
        selenium_methods.click(self.driver, self.config['HOME']['EINLOGGEN'])

    def login(self, email, password):
        selenium_methods.enter_text(self.driver, self.config['HOME']['EMAIL'], email)
        selenium_methods.enter_text(self.driver, self.config['HOME']['PASSWORD'], password)
        selenium_methods.click(self.driver, self.config['HOME']['ANMELDEN'])

        # Return True if "Abmelden (Logout) element found, otherwise False
        return selenium_methods.element_exists(self.driver, self.config['HOME']['ABMELDEN'])
