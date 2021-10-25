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
import time,re

class Mobile_Setup():
    
    def __init__(self):
        self.driver=webdriver.Chrome("/usr/local/lib/driver/chromedriver")
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
    
    def mobile_setup(self):
        
        try :
          
            '----------- Login into WebFocus ---------------'
            
            self.invoke_webfocu()
            time.sleep(5)
            node = self.parseinitfile('nodeid')
            port = self.parseinitfile('httpport')
            context = self.parseinitfile('wfcontext')
            setup_url = 'http://' + node + ':' + port + context + '/legacyhome'
            self.driver.get(setup_url)
            time.sleep(30)
            folder_img=(By.CSS_SELECTOR,"#bipTreePanel #treeView table>tbody>tr>td img[src*='folder']")
            WebDriverWait(self.driver,150).until(EC.visibility_of_any_elements_located(folder_img))
            
            '----------- Expand Repository Tree ---------------'
            
            folder_path=self.parseinitfile('folder_path')
            BIPtree_rows_css = "#bipTreePanel #treeView table>tbody>tr"
            folder_list=folder_path.split('->')
            for path in folder_list :
                repository_items=self.driver.find_elements_by_css_selector(BIPtree_rows_css)
                for i in range(len(repository_items)) :
                    if repository_items[i].text.strip()==path :
                        folder_img = repository_items[i].find_element_by_css_selector("td>img")
                        img_src=folder_img.get_attribute("src")
                        if 'triangle_collapsed' in img_src:
                            action = ActionChains(self.driver)
                            action.move_to_element(folder_img).click(folder_img).perform()
                            del action
                            time.sleep(4)
                            break
            
            time.sleep(4)
            
            '---------------- Select All Fex --------------'
            
            repository_items = self.driver.find_elements_by_css_selector(BIPtree_rows_css)
            first_fext=repository_items[i+1].find_element_by_css_selector("td>img.icon")
            action = ActionChains(self.driver)
            action.move_to_element(first_fext).click(first_fext).perform()
            total_fex=0
            for j in range(i+1,len(repository_items)) :
                folder_img_src=repository_items[j].find_element_by_css_selector("img[class='icon']").get_attribute('src')
                if 'folder_closed' in folder_img_src :
                    break
                else :
                    total_fex=total_fex+1
            action.send_keys(Keys.SHIFT).send_keys(Keys.ARROW_DOWN*int(total_fex-1)).perform()
            time.sleep(5)
            # this for windows os action.key_down(Keys.CONTROL).key_down(Keys.SHIFT).context_click(first_fext).perform()
            action.key_down(Keys.COMMAND).key_down(Keys.SHIFT).context_click(first_fext).perform()
            time.sleep(5)
            
            
            '------------------ Click on Add To Mobile Favorites ---------------------- '
            
            menu_items=self.driver.find_elements_by_css_selector("div[id^='BiPopup'][style*='inherit'] table>tbody>tr")
            for item in menu_items :
                if item.text.strip()=='Add To Mobile Favorites' :
                    item.click()
                    break
            
            time.sleep(10)
            self.driver.save_screenshot('Mobile_Setup_Success.png')
            self.driver.close()
            self.driver.quit()
            
        except :
            self.driver.save_screenshot('Mobile_Setup_Error.png')
            self.driver.close()
            self.driver.quit()
            
                        
obj=Mobile_Setup()
obj.mobile_setup()
    