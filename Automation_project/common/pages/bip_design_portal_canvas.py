from common.lib import utillity
from common.lib.base import BasePage
from common.locators.visualization_run_locators import VisualizationRunLocators
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, StaleElementReferenceException
import time, os,re,operator
from selenium.webdriver.support.color import Color
from common.locators.bip_design_ribbon_locators import BIPDesignRibbonLocators


class BIP_Design_Portal_Canvas(BasePage):
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(BIP_Design_Portal_Canvas, self).__init__(driver)
    
    def _validate_page(self, locator):
        self.longwait.until(EC.visibility_of_element_located(locator))
    
    def get_panel_reference(self, panel_index):
        panels = self.driver.find_elements_by_css_selector("#canvasmainpanel [class*='bip-page'][style*='inherit'] [class*='bip-container']")
        
        return(panels[panel_index])
    def select_canvas_panel_options(self, panel_index, btn_name, **kwargs):
        
        action = ActionChains(self.driver)
        action.move_to_element(self.get_panel_reference(panel_index)).perform()
        del action
        panel_btn_css="div[id^='BipConvertControl'] [class*='bip-convert-button-convert'] img"
        panel_elem=self.driver.find_element_by_css_selector(panel_btn_css)
        elem=(By.CSS_SELECTOR, panel_elem)
        self._validate_page(elem)
        action = ActionChains(self.driver)
        action.move_to_element(elem).perform()
        del action
        time.sleep(2)
        panel_sub_btn_css="div[id^='BipConvertControl'] [class*=' bip-convert-button ']"
        panel_sub_elems=self.driver.find_elements_by_css_selector(panel_sub_btn_css)
        panel_sub_elems[[el.text.strip() for el in panel_sub_elems].index(btn_name)].click()
    
    
    def switch_ia_tab(self, tab_name): 
        """
        param tab_name: 'Insert' OR 'Style' OR 'Layout'....
        Syntax: switch_ia_tab('Layout')
        @author = Niranjan
        """
        tab_css=BIPDesignRibbonLocators.tab_css.format(tab_name)
        self.driver.find_element_by_css_selector(tab_css).click() 
        time.sleep(1)
    
    def select_ribbon_item(self, tab_name, ribbon_button_name, **kwargs):
        """
        param: tab_name: 'Layout' or 'Style' 
        param: ribbon_button_name: 'Document' or 'Data_from_Source' (The button name as displayed in ribbon bar. If space is there, then replace it by underscore.)
        param: opt: The dropdown menu list from a ribbon button.
        Syntax: select_ribbon_item('Layout', 'LayoutMargins', opt='Custom')
        @author : Nasir
        """
        self.switch_ia_tab(tab_name)
        time.sleep(2)
        button_name = tab_name.lower() + "_" + ribbon_button_name.lower()
        self._validate_page(BIPDesignRibbonLocators.__dict__[button_name])
        self.driver.find_element(*BIPDesignRibbonLocators.__dict__[button_name]).click()
        time.sleep(5)
        if 'opt' in kwargs:
            utillity.UtillityMethods.select_or_verify_bipop_menu(self, kwargs['opt'])
        time.sleep(2)
    
        