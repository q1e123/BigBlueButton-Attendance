# Copyright (C) 2020 Robert-Nicolae Șolcă
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/

## @package main
# Main file

import time
import itertools

from driver_ff import DriverFirefox

from spreadsheets_driver import SpreadSheetDriver

## Engine behind the program
class Engine:
    ## Constructor
    def __init__(self,file_name):
        ## Firefox driver
        self.driver = DriverFirefox()
        ## Dictionary used to store settings
        self.settings = self.__get_settings(file_name)
        self.users = []

    ## Joins a session
    def join_sesssion(self):
        self.__login()
        self.driver.goto(self.settings["link"])
        time.sleep(5)
        self.driver.click('//*[@id="join_button_input"]')
        time.sleep(10)
        self.driver.click('/html/body/div[2]/div/div/header/button/span[1]/i')
        time.sleep(5)
    ## Gets the list of current users
    def get_current_users(self):
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
    ## Puts attendancein a spreadsheet
    def put_attendance(self):
        if self.settings['spreadsheet'] == '-':
            return

        ss_driver = SpreadSheetDriver(self.settings['spreadsheet'], self.settings['spreadsheet_name'],self.settings['sheetname'])
        
        if len(self.users) == 0:
            f = open(self.settings['output'])
            lines = f.readlines()
            for usr in lines:
                self.users.append(usr)

        for user in self.users:
            i = ss_driver.get_row(user[:-1],'A')
            j = chr(ord('A') + int(self.settings['week']))
            ss_driver.write(i,j,'1')
        
        ss_driver.save()

    ## Gets settings from a file
    def __get_settings(self,file_name):
        settings = {}
        f = open(file_name,'r')
        lines = f.readlines()
        for line in lines:
            split = line.replace('\n',' ').split(' ')
            settings[split[0]] = split[1]
        f.close()
        return settings
    
    ## Logs into a moodle profile
    def __login(self):
        self.driver.goto(self.settings['login'])
        self.driver.send_keys('//*[@id="username"]',self.settings['user']) 
        self.driver.send_keys('//*[@id="password"]',self.settings['pass'])
        self.driver.click('//*[@id="loginbtn"]')
 
e = Engine('config')
e.join_sesssion()
e.get_current_users()
e.put_attendance()
