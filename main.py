import time
import itertools


from driver_ff import DriverFirefox

from spreadsheets_driver import SpreadSheetDriver

class Engine:
    def __init__(self,file_name):
        self.driver = DriverFirefox()
        self.settings = self.__get_settings(file_name)
        self.users = []

    def join_sesssion(self):
        self.__login()
        self.driver.goto(self.settings["link"])
        time.sleep(5)
        self.driver.click('//*[@id="join_button_input"]')
        time.sleep(10)
        self.driver.click('/html/body/div[2]/div/div/header/button/span[1]/i')
        time.sleep(5)
    def get_current_users(self):
        # get users
        
        for i in itertools.count(1):
            try:
                user = self.driver.get_value('//*[@id="app"]/main/section/div[2]/div/div/div/div[3]/div[2]/div/div/div[{}]/div/div[1]/div/div[2]/span/span'.format(str(i)),'innerHTML')
                user = user[:-5]
                self.users.append(user)           
            except:
                print('Exited from divs')
                break
        out = open(self.settings['output'],'w+')
        for user in self.users:
           out.write(user) 
        out.close()

    def put_attendance(self):
        if self.settings['spreadsheet'] == '-':
            return

        ss_driver = SpreadSheetDriver(spreadsheet, self.settings['spreadsheet_name'])
        ss_driver.open()
        for user in self.users:
            __put_user(user)            

    def __get_settings(self,file_name):
        settings = {}
        f = open(file_name,'r')
        lines = f.readlines()
        for line in lines:
            split = line.replace('\n',' ').split(' ')
            settings[split[0]] = split[1]
        f.close()
        return settings

    def __put_user(user):
        return

    def __login(self):
        self.driver.goto(self.settings['login'])
        self.driver.send_keys('//*[@id="username"]',self.settings['user']) 
        self.driver.send_keys('//*[@id="password"]',self.settings['pass'])
        self.driver.click('//*[@id="loginbtn"]')
 
e = Engine('config')
e.join_sesssion()
e.get_current_users()
