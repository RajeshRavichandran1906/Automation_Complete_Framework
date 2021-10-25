import os
import sys
suite=sys.argv[1]
parent=os.path.abspath('..')
parent=parent + '/' + suite
os.chdir(parent)
sys.path.append(parent)
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from common.locators.loginpage_locators import LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time,re

class Mobile_Setup():
    
    def __init__(self):
        
        self.driver=webdriver.Chrome("/usr/local/lib/driver/chromedriver")
        #self.driver=webdriver.Chrome("D:\chromedriver")
        self.driver.maximize_window()
        
    def parseinitfile(self, key):
        init_file = 'config.init'
        config_pair = {}
        try:
            fileObj = open(init_file, "r")
            line = fileObj.readline()
            while line:
                lineObjbj = re.match(r'(\S*)\s(.*)', line)
                keyName = lineObjbj.group(1)
                config_pair[keyName] = lineObjbj.group(2)
                line = fileObj.readline()

        except IOError:
            exit()

        if key in config_pair:
            return (config_pair[key])
        else:
            return ('Key not found')
    
    def invoke_webfocu(self):
        
        node = self.parseinitfile('nodeid')
        port = self.parseinitfile('httpport')
        context = self.parseinitfile('wfcontext')
        setup_url = 'http://' + node + ':' + port + context + '/'
        self.driver.get(setup_url)
        loginid = self.parseinitfile('mrid')
        loginpwd = self.parseinitfile('mrpass')
        uname1=(By.CSS_SELECTOR, 'input[id=SignonUserName]')
        longwait = WebDriverWait(self.driver, 150)
        longwait.until(EC.visibility_of_element_located(uname1))
        usename= self.driver.find_element(*LoginPageLocators.uname)
        usename.click()
        time.sleep(2)
        usename.send_keys(loginid)
        time.sleep(1)
        if loginpwd!=None:
            passwd =self.driver.find_element(*LoginPageLocators.pword)
            passwd.send_keys(loginpwd)
            time.sleep(1)
        sign_in =self.driver.find_element(*LoginPageLocators.submit)
        sign_in.click()
        time.sleep(4)
        baneer_icon=(By.CSS_SELECTOR,"div[class^='main-box'] div[class^='home-banner'] div[class='banner-logo']")
        WebDriverWait(self.driver,150).until(EC.visibility_of_any_elements_located(baneer_icon))
        time.sleep(10)
        
    def expand_folders(self):
        
        folder_path=self.parseinitfile('folder_path')
        content=self.driver.find_element_by_css_selector("div[class^='main-panel'] div[class^='left-main-panel'] div[title='Content View']")
        content.click()
        time.sleep(5)
        domain=self.driver.find_elements_by_css_selector("div[data-ibx-type='breadCrumbTrail'] div[class*='crumb-button']")[0]
        domain.click()
        time.sleep(5)
        tree_rows=".ibfs-tree div[class^='ibfs-children'] div[data-ibx-type='ibxVBox'][class^='ibx-widget']"
        folder_list=folder_path.split('->')
        for item in folder_list:
            repository_items = self.driver.find_elements_by_css_selector(tree_rows)
            for i in range(len(repository_items)):
                if repository_items[i].text.strip() == item:
                    try:
                        plus_img = repository_items[i].find_element_by_css_selector("label[class*='ibx-glyph-plus-small']")
                        ActionChains(self.driver).move_to_element(plus_img).click().perform()
                        time.sleep(5)
                        if repository_items[i].text.strip() == folder_list[-1]:
                            repository_items[i].click()
                            time.sleep(5)
                        break
                    except NoSuchElementException:
                        pass
   
    def mobile_setup(self):
        
        '----------- Login into WebFocus ---------------'
        
        self.invoke_webfocu()
        time.sleep(10)
        
        '----------- Expand Repository Tree ---------------'
        self.expand_folders()
        time.sleep(5)
        
        '----------- Select All fexs ---------------'
        all_fex=self.driver.find_elements_by_css_selector("div[class^='content-box'] div[class^='files-box'] div[class^='fbx-block']>div[class^='file-item']")
        ActionChains(self.driver).send_keys(Keys.SHIFT).send_keys(Keys.COMMAND).click(all_fex[0]).move_to_element(all_fex[-1]).click().perform()
        time.sleep(3)
        ActionChains(self.driver).context_click(all_fex[-1]).perform()
        time.sleep(3)
        
        '------------------ Click on Add To Mobile Favorites ---------------------- '
        
        menu_items=self.driver.find_elements_by_css_selector("div[class$='pop-top'][data-ibx-type='ibxMenu'] div[data-ibx-type='ibxMenuItem']")
        for item in menu_items :
            if item.text.strip()=='Add To Mobile Favorites' :
                item.click()
                break
        
        time.sleep(5)
        self.driver.save_screenshot('Mobile_Setup_Success.png')
        self.driver.close()
        self.driver.quit()
        
       
obj=Mobile_Setup()
obj.mobile_setup()
    