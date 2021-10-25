from common.lib import utillity
from common.lib.base import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, StaleElementReferenceException
import time,re, pyautogui
from common.locators.common_utillity_locators import CommonUtillityLocators


class Common_Utillity(BasePage):
    
    def dynamic_grouping(self, field_list, *args):
        """
        :param field_list: ["Accessories","Camcorder","Computers"]
        :Usgae: resultobj.dynamic_grouping(field_list,"group","ok")
        :author: Niranjan Date: June 28
        """
        browser_height=80
        browser=utillity.UtillityMethods.parseinitfile(self, "browser")
        if browser=='Firefox':
            for field_name in field_list:
                img_xpath = CommonUtillityLocators.grp_tree.format(field_name)
                field = self.driver.find_element_by_xpath(img_xpath)
                x_fr=field.location['x']
                y_fr=field.location['y']
                pyautogui.keyDown('ctrl')
                pyautogui.click(x_fr+20, y_fr+browser_height)
                pyautogui.keyUp('ctrl')
                time.sleep(2)
            time.sleep(1)
        else:
            action = ActionChains(self.driver)
            for field_name in field_list:
                img_xpath = CommonUtillityLocators.grp_tree.format(field_name)
                field = self.driver.find_element_by_xpath(img_xpath)
                action.key_down(keys.Keys.CONTROL).click(field).key_up(keys.Keys.CONTROL)
                time.sleep(2)
            action.perform()
            time.sleep(1)
            del action
        time.sleep(5)
        if 'group' in args:
            if browser=='Firefox':
                grp_img=self.driver.find_element(*CommonUtillityLocators.group)
                x_fr=grp_img.location['x']
                y_fr=grp_img.location['y']
                pyautogui.click(x_fr+20, y_fr+browser_height)
            else:
                self.driver.find_element(*CommonUtillityLocators.group).click()
            time.sleep(20)
        if 'rename' in args:
            self.driver.find_element(*CommonUtillityLocators.rename).click()
        if 'ungroup' in args:
            self.driver.find_element(*CommonUtillityLocators.ungroup).click()
        if 'ungroup all' in args:
            self.driver.find_element(*CommonUtillityLocators.ungroup_all).click()
        if 'show other' in args:
            self.driver.find_element(*CommonUtillityLocators.show_other).click()
        if 'ok' in args:
            self.driver.find_element(*CommonUtillityLocators.ok_button).click()
        time.sleep(10)