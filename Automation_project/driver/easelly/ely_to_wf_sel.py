'''
Created on Sep 13, 2018

@author: Lawrence
@description: This program uses Selenium and Pyautogui to upload files to a chosen WebFocus environment.
'''

import time, sys
from selenium import webdriver
from common.lib.core_utility import CoreUtillityMethods as core_utils
from common.lib.javascript import JavaScript as j_script
from pyautogui import typewrite, hotkey
import configparser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

host = sys.argv[1]
port = sys.argv[2]
appspath = sys.argv[3]
username = sys.argv[4]
password = sys.argv[5]
local_file_path = sys.argv[6]
folder_path = sys.argv[7]
templates_string = sys.argv[8]

class Ely_to_wf_sel(object):

    def __init__(self):
        '''
        Start Selenium WebDriver and log into WebFocus.
        '''
        config = configparser.ConfigParser()
        conf_file = 'config.ini'
        config.read(conf_file)
        options = webdriver.ChromeOptions()
        prefs = {"download.prompt_for_download": True}
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--start-maximized")
        options.add_argument('--disable-infobars')
        options.add_argument('--disable-print-preview')
        browser_driver = config['DEFAULT']['CHROMEDRIVER']
        self.driver = webdriver.Chrome(browser_driver, chrome_options = options)
        apps_path = "/" + appspath

        url = host + ":" + port + apps_path
        self.login(url, username, password)
        
    def login(self, url, username, password):
        '''
        Log into WebFocus.
        '''
        driver = self.driver
        user_css = ".user-id > input"
        pass_css = ".password > input"
        sign_in_css = "#SignonbtnLogin"
        driver.get(url)
        driver.find_element_by_css_selector(user_css).send_keys(username)
        driver.find_element_by_css_selector(pass_css).send_keys(password)
        driver.find_element_by_css_selector(sign_in_css).click()
          
    def expand_repository_folders(self, folder_path):
        """
        Descriptions : This method used to expand home page domains folder 
        example usage : expand_repository_folders('Retail Samples->Reports->Auto Link Targets')
        @author:Aftab_Alam_Khan
        """
        scroll_css="div[class='ibfs-tree']"
        folder_css="div[class='ibfs-tree'] div[data-ibfs-path]>div[class*='home-tree-node']"
        expand_icon_css="div[class*='ibx-icons'][class*='ibx-glyph-plus-small']"
        folder_list=folder_path.split('->')
        index=0
        time.sleep(20)
        for folder in folder_list :
            folder_obj_list=self.driver.find_elements_by_css_selector(folder_css)
            folder_index=j_script.find_element_index_by_text(self, folder_obj_list, folder, index)
            folder_not_found_error="[{0}] folder not found under the domains".format(folder)
            if folder_index == None :
                raise FileNotFoundError(folder_not_found_error)
            else :
                folder_obj=folder_obj_list[folder_index]
                j_script.scrollTop(self, scroll_css, folder_obj, wait_time=1)
                expand_icon_obj=folder_obj.find_elements_by_css_selector(expand_icon_css)
                if len(expand_icon_obj)>0 :
                    core_utils.left_click(self, expand_icon_obj[0])
                if folder_list[-1] == folder:
                    time.sleep(2)
                    core_utils.left_click(self, folder_obj)
            index=folder_index + 1
            
    def select_tab_from_menu_list(self, menu_css, element_text, tab_css):
        index=0
        time.sleep(5)
        menu_list=self.driver.find_elements_by_css_selector(menu_css)[0].find_elements_by_css_selector(tab_css)
        for menu_item in menu_list:
            item_index=j_script.find_element_index_by_text(self, menu_list, element_text, index)
            item_not_found_error="[{0}] text not found".format(menu_item)
            if item_index == None:
                raise FileNotFoundError(item_not_found_error)
            index = index + 1
        menu_list[item_index].click()
        
    def upload_files_to_folder(self, menu_locator, element_text, template_list, file_path):
        driver = self.driver      
        for template in template_list:
            menu_elem_list = driver.find_elements(*menu_locator)
            index = 0
            for menu_item in menu_elem_list:
                if menu_item.text == element_text:
                    item_index = index
                    break
                index = index + 1
            menu_elem_list[item_index].click()
            time.sleep(3)
            #typewrite(r'\\ibirisc2\bipgqashare\easel_ly\latest_templates' +  '\\' + template)
            typewrite(file_path.strip("\'") + '\\' + template)
            hotkey('enter')
            time.sleep(2)
            overwrite_css = ".ibx-dialog-ok-button[role='button']"
            try:
                element = WebDriverWait(driver, 2).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, overwrite_css)))
                element[1].click()
            except:
                pass    
            time.sleep(1) 
        
if __name__ == '__main__':
    etws_obj = Ely_to_wf_sel()
    #folder_path = 'P413_S18040->ELY Templates'
    menu_css = ".ibx-csl-items-container > .ibx-csl-items-box"
    element_text = "Other"
    etws_obj.expand_repository_folders(folder_path)
    tab_css = ".ibx-tab-button"
    etws_obj.select_tab_from_menu_list(menu_css, element_text, tab_css)
    menu_locator = (By.CSS_SELECTOR, ".action-bar-tab > .action-hbox.ibx-widget.ibx-flexbox > .create-new-item")#etws_obj.driver.find_elements_by_css_selector(".action-bar-tab > .action-hbox.ibx-widget.ibx-flexbox > .create-new-item")
    element_text = "Upload File"
    #templates = 'United_Way.ely,ggcafedemo3.ely,easelly_bubble.ely,easelly_charts.ely,fonts_part1.ely,fonts.ely,alignment.ely,template.ely,summit_new.ely'
    template_list = templates_string.split(',')
    etws_obj.upload_files_to_folder(menu_locator, element_text, template_list, local_file_path)
            