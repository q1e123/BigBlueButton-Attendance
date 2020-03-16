import time

from driver_ff import DriverFirefox

class Engine:
    def __init__(self,dict={}):
        self.driver = DriverFirefox()
        self.settings = dict
    def join_sesssion(self):
        self.__login()
        self.driver.goto(self.settings["link"])
        time.sleep(5)
        self.driver.click('//*[@id="join_button_input"]')
    
    def get_current_users(self):
        users = []
       

    def __login(self):
        self.driver.goto(self.settings['login'])
        self.driver.send_keys('//*[@id="username"]',self.settings['user']) 
        self.driver.send_keys('//*[@id="password"]',self.settings['pass'])
        self.driver.click('//*[@id="loginbtn"]')
 

def get_settings(file_name):
    settings = {}
    f = open(file_name,'r')
    lines = f.readlines()
    for line in lines:
        split = line.replace('\n',' ').split(' ')
        settings[split[0]] = split[1]
    return settings

d = get_settings('config')

e = Engine(d)
e.join_sesssion()

