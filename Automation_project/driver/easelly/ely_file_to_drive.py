'''
Created on Jun 14, 2018

@author: Lawrence
'''

from selenium import webdriver
import shutil
import time
import sys
import os
import configparser
import getpass

link = sys.argv[1]
destination_folder = sys.argv[2]

class ElyFileToDrive(object):
    
    #selenium to pull link
    #input link, place in location
    ##login#password
    def __init__(self):
        
        login_css = "a.button.is-info.log_in"
        user_css = "#login"
        pass_css = "#password"
        login_button_css = "#loginBtn"
        config = configparser.ConfigParser()
        conf_file = 'config.ini'
        config.read(conf_file)
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--disable-infobars')
        #options.add_argument('--headless')
        browser_driver = config['DEFAULT']['CHROMEDRIVER']
        driver = webdriver.Chrome(browser_driver, chrome_options = options)
        username = config['DEFAULT']['USERNAME']
        password = config['DEFAULT']['PASSWORD']
        url = config['DEFAULT']['URL']
        driver.get(url)
        #driver.find_element_by_css_selector("#easel-container > nav > div.navbar-menu > div > div:nth-child(5) > a").click()
        #driver.find_element_by_css_selector(login_css).click()
        driver.find_element_by_css_selector(user_css).send_keys(username)
        driver.find_element_by_css_selector(pass_css).send_keys(password)
        driver.find_element_by_css_selector(login_button_css).click()
        self.driver = driver
    
    def selenium_navigation_for_link(self, visual_name):

        driver = self.driver
        visual_msg = "Requested Visual not found. Exiting program."
        
        '''Click the desired visual'''
        my_visuals = driver.find_elements_by_css_selector("#block-visual > div.content-block > div.content-left > div > a")
        position = -1
        for index, visual in enumerate(my_visuals):
            if visual.get_attribute("innerText").lower() == visual_name.lower():
                position = index
                break
            
        if position == -1:
            print(visual_msg)
            exit(1)
            
        my_visuals[position].click()
        '''Derive the sharable link'''
        driver.find_element_by_css_selector("#main-content > div > div.menu > div.main-menu > div.action-menu > div.dropdown.share > a").click()
        driver.find_element_by_css_selector("#main-content > div > div.menu > div.main-menu > div.action-menu > div.dropdown.share.open > ul > li:nth-child(3) > a").click()
        time.sleep(3)
        link = driver.find_element_by_id("share-url").get_attribute("innerHTML")
        print(link)
        return link
    
    def post_link_contents_to_drive(self, link, post_location):
        
        driver = self.driver
        invalid_link_msg = "Invalid link was passed in."
        overwrite_file_msg = "Overwriting existing file: "
        download_location = "C:/Users/"  + getpass.getuser() + "/Downloads/" #os.path.expanduser('~/Downloads') + "/"
        file_dropdown_css = ".dropdown.file"
        save_css = ".dropdown-menu > li:nth-child(1) > a"
        download_dropdown_css = ".dropdown.download"
        download_export_css = ".fa.fa-inbox"
        title_css = ".menu-canvas-name-input"
        
        if len(link)==0:
            print(invalid_link_msg)
            exit(1)
        driver.get(link)
        file_name = download_location + driver.find_element_by_css_selector(title_css).get_attribute("value") + ".ely"

        '''Remove the file if it already exists so we can replace it with a new copy'''
        if os.path.exists(file_name):
            print(overwrite_file_msg, file_name)
            os.remove(file_name)
        
        '''Save the template (required in order for the exported file to work properly)'''
        time.sleep(5)
        driver.find_element_by_css_selector(file_dropdown_css).click()
        driver.find_element_by_css_selector(save_css).click()
        time.sleep(2)
        
        '''Download the file'''
        driver.find_element_by_css_selector(download_dropdown_css).click()
        driver.find_element_by_css_selector(download_export_css).click()
        time.sleep(15)
        '''Copy file to desired location (through a guaranteed overwrite)'''
        shutil.copy(file_name, post_location)
        time.sleep(1)
     
def main():
    elyObj = ElyFileToDrive()
    #link = elyObj.selenium_navigation_for_link(visual_name)
    #link = "https://www.easel.ly/infographic/bkk2p3"
    elyObj.post_link_contents_to_drive(link, destination_folder)

if __name__ == '__main__':
    main()