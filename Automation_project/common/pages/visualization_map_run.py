from common.lib import utillity
from common.lib.base import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import re
import time

class Visualization_Map_Run(BasePage):
    
    def __init__(self, driver):
        super(Visualization_Map_Run, self).__init__(driver)

    def _validate_page(self, locator):
        self.longwait.until(EC.visibility_of_element_located(locator)) 

    def esri_move_map_toc_popup(self, x, y):
        """
        Syntax:  miscelanousobj.move_active_popup(600", "200")
        """
        toc_popup=self.driver.find_element_by_css_selector("div[class='dojoxFloatingPaneTitle']")
        action=ActionChains(self.driver)
        action.drag_and_drop_by_offset(toc_popup, x, y).perform()
        del action
        
    def esri_select_map_main_menu(self, btn_name):
        """
        params: btn_name = 'home' OR 'toc', OR 'select_tool', OR 'change_map', OR 'find_location'
        Syntax: select_map_main_menu('home')
        """
        main_menu="#mainMenu"
        btn_title={'home':"div[title='Default extent']",
                  'toc':"li[title='Table of Contents']",
                  'select_tool':"li[title='Selection Tools']",
                  'change_map':"li[title='Change Base Map']",
                  'find_location':"div[title='Find my location']"}
        btn_css= main_menu + " " + btn_title[btn_name]
        self.driver.find_element_by_css_selector(btn_css).click()
        time.sleep(1)
    
    def esri_select_map_tools_in_toc(self, layer_name, opt):
        """
        params: btn_name = 'zoom_to_layer' OR 'toggle_options', OR 'toggle_layer'
        Syntax: select_map_tools_in_toc('toggle_layer')
        """
        layers=self.driver.find_elements_by_css_selector("#lwFloatingPane .layerList")
        elem=layers[[el.text.strip() for el in layers].index(layer_name)]
        options={'show_tool':'li.optionsBoxBtn',
                 'zoom_to_layer':'li.goToLyr',
                  'toggle_options':'li.optsIcon',
                  'toggle_layer':'li.legIcon'}
        
        if not elem.find_element_by_css_selector(options[opt]).is_displayed():
            elem.find_element_by_css_selector(options['show_tool']).click()
            time.sleep(1)
        elem.find_element_by_css_selector(options[opt]).click()
        time.sleep(1)
        
    def esri_verify_map_fill_color(self, circle_index, color, msg):
        """
        params: circle_index = 0, 1, 2...
        params: color = 'red', OR 'green'...here for example purpose i used 'demo_color'
        Syntax: verify_fill_color('demo_color')
        """
        circle_css="#emfobject1 svg circle"
        circles=self.driver.find_elements_by_css_selector(circle_css)
        colors={'demo_color':'rgb(227, 26, 28)'}
        bool_color=colors[color]==circles[circle_index].get_attribute("fill")
        utillity.UtillityMethods.asequal(self,True, bool_color, msg + " : Verify fill color")
        

    def esri_select_base_map(self, map_title):
        """
        params: select_base_map = 'Imaginary', OR 'Streets' ...
        Syntax: select_base_map('demo_color')
        """ 
        img_css="#imDijit img[title='" + map_title + "']"   
        self.driver.find_element_by_css_selector(img_css).click()
        time.sleep(2)
    
    def esri_check_uncheck_layer(self, layer_name, default_check):
        """
        params: layer_name = 'Layer 1', OR 'Layer 2' ...
        params: default_check = True OR False
        Syntax: esri_check_uncheck_layer('Layer 1', True)
        """ 
        layers=self.driver.find_elements_by_css_selector("#lwFloatingPane .layerList")
        checked=layers[[el.text.strip() for el in layers].index(layer_name)].find_element_by_css_selector("li[class^='LyrCb']").get_attribute("class")
        checked_status = True if bool(re.match(r'.*icon-check.*', checked)) else False
        if default_check==True:
            utillity.UtillityMethods.asequal(self,True, checked_status, "Step X: " + layer_name + " Layer is Checked.")
        else:
            utillity.UtillityMethods.asequal(self,False, checked_status, "Step X: " + layer_name + " Layer is Unchecked.")
        layers[[el.text.strip() for el in layers].index(layer_name)].find_element_by_css_selector("li[class^='LyrCb']").click()
        time.sleep(2)
    
    def esri_zoom_in_out(self, zoom_type, zoom_times):
        """
        params: zoom_type = 'in', OR 'out'
        params: zoom_times = 1, 2, 3...(Any integer value, Means the number of times you want to zoom in or zoom out)
        Syntax: esri_zoom_in_out('out', 2)
        """
        if zoom_type=='out':
            zoom_css="#emfobject1_zoom_slider .esriSimpleSliderIncrementButton > span"
        else:
            zoom_css="#emfobject1_zoom_slider .esriSimpleSliderDecrementButton > span" 
        self.driver.find_element_by_css_selector(zoom_css).click()
        time.sleep(2)
           
    def esri_close_toc_popup(self):
        close_css="span.dojoxFloatingCloseIcon"
        self.driver.find_element_by_css_selector(close_css).click()
        time.sleep(2)


