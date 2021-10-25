'''
Created on Feb 14, 2017

@author: ly14557
'''
import time
from selenium.webdriver import ActionChains
import pyautogui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from common.lib import utillity
from common.lib.base import BasePage
from common.locators.visualization_run_locators import VisualizationRunLocators
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, StaleElementReferenceException
import re
from pynput.mouse import Button, Controller
from selenium.webdriver.support.color import Color
from common.locators.as_ribbon_locators import AsRibbonLocators  

class ESRI_Map():
    ''''''
    pyautogui.PAUSE = 1
    
    def open_panel(self, driver, panel_name):
        options = { 
                   'Tasks & Animations': 0,
                   'Requests & Data Sources': 1,
                   'Settings': 2,
                   'Properties': 3,
                   'File/Folder Properties': 4}
        if panel_name in options:
            panels = driver.find_elements_by_id("1")
            panels[options[panel_name]].click()
        else:
            print("Panel name not found. Did not open panel.")
        

    def open_panel_general(self, driver, panel_name):
        panels = driver.find_elements_by_id("1")
      
        for index in enumerate(panels):
                panels[index].click()
                try:
                    driver.find_element_by_name(panel_name)
                    break
                except:
                    pass              
           
    def select_application_menu(self, driver, menu_option):
        driver.find_element_by_name("Application Menu").click()
        #Entire box appears as a single element currently
        #driver.find_element_by_name(menu_option).click()
        
    def click_components(self, driver, component_name):
        driver.find_element_by_name("Components").click()
        driver.find_element_by_name(component_name).click()
        time.sleep(1)
        
    def create_html(self, driver, server, folder, project):
        #ac0 = ActionChains(driver)
        #ac0.double_click(driver.find_element_by_name("Configured Environments")).perform()
        #time.sleep(1)
        #TODO: change folder to path
        ac = ActionChains(driver)
        ac.double_click(driver.find_element_by_name(server)).perform()
        time.sleep(1)
        ac2 = ActionChains(driver)
        ac2.double_click(driver.find_element_by_name("Domains")).perform()
        time.sleep(1)
        ac3 = ActionChains(driver)
        ac3.double_click(driver.find_element_by_name(project)).perform()
        time.sleep(1)
        driver.find_element_by_name(folder).click()
        time.sleep(1)
        driver.find_element_by_name("HTML / Document").click()
        time.sleep(1)
        driver.find_element_by_name("Next >").click()
        time.sleep(1)
        driver.find_element_by_name("Finish").click()
        time.sleep(1)
        
    def create_new_esri(self, driver):
        driver.find_element_by_name("ESRI Map").click()
        time.sleep(1)
        ac = ActionChains(driver)
        html = driver.find_element_by_name("HtmlPage")
        ac.move_to_element_with_offset(html, 80, 120)
        ac.click_and_hold()
        ac.move_to_element_with_offset(html, 650, 690)
        ac.release().perform()
        time.sleep(1)
        
    def set_properties_panel(self, driver, **kwargs):
        self.open_panel(driver, 'Properties')
        time.sleep(1)
        
    def set_requests_panel(self, driver, **kwargs):
        #driver.find_elements_by_id("1")[2].click()
        self.open_panel(driver, 'Requests & Data Sources')
        time.sleep(1)
        #pyautogui.click(1625, 180)
        '''
        driver.find_element_by_id("23001").find_element_by_name("New").click()#find_element_by_name("Open").click()
        ac_requests = ActionChains(driver)
        ac_requests.move_to_element_with_offset(driver.find_element_by_id("23001").find_element_by_name("New"), 25, 10).click()
        ac_requests.perform()
        driver.find_element_by_id("23001").find_element_by_name("Delete").click()  
        driver.find_element_by_id("23001").find_element_by_name("Refresh parameters").click()
        driver.find_element_by_id("23001").find_element_by_name("Save Selection").click()
        driver.find_element_by_id("23001").find_element_by_name("Clear Selection").click()
        '''
        ac_requests = ActionChains(driver)
        ac_requests.move_to_element_with_offset(driver.find_element_by_id("23001").find_element_by_name("New"), 25, 10).click()
        ac_requests.perform()
        time.sleep(1)
        '''
        ac = ActionChains(driver)
        ac.move_to_element(driver.find_element_by_name("External Request")).perform()
        time.sleep(1)
        driver.find_element_by_name("WebFOCUS Procedure...").click()
        '''
        driver.find_element_by_name("Requests->Parameters...").click()
        time.sleep(1)
        driver.find_element_by_name(kwargs['fex'] + ".fex").click()
        time.sleep(1)
        driver.find_element_by_name("OK").click()
        time.sleep(1)
        
    def set_settings_panel(self, driver, **kwargs):
        self.open_panel(driver, "Settings")
        time.sleep(1)
        if 'Layer_Name' in kwargs:
            layers = driver.find_elements_by_name("Symbol Settings")[1]
            ac_layer = ActionChains(driver)
            ac_layer.move_to_element_with_offset(layers, 14, 5)
            ac_layer.double_click()
            time.sleep(1)
            ac_layer.click()
            ac_layer.perform()
            time.sleep(1)
            pyautogui.typewrite(kwargs['Layer_Name'])
            time.sleep(1)
        if 'Request' in kwargs:
            ac_request = ActionChains(driver)
            ac_request.move_to_element_with_offset(driver.find_element_by_name('Request'), 100, 5).click().perform()
            driver.find_element_by_name(kwargs['Request']).click()
            time.sleep(1)
        if 'Geographic_Role' in kwargs:
            ac_geo = ActionChains(driver)
            ac_geo.move_to_element_with_offset(driver.find_element_by_name('Geographic Role'), 100, 5).click().perform()         
            driver.find_element_by_name(kwargs['Geographic_Role']).click()
            time.sleep(1)
        if 'Column' in kwargs:       
            ac_col = ActionChains(driver)
            ac_col.move_to_element_with_offset(driver.find_element_by_name("Column(s) that match the role"), 250, 5).click().perform() 
            elem = driver.find_element_by_id("3")
            elem.click()
            elem_name = elem.get_attribute("Name")
            time.sleep(1)
            while elem_name != kwargs['Column']:
                pyautogui.press('down')
                elem_name = elem.get_attribute("Name")       
                time.sleep(1)   
        if 'Layer_Attributes' in kwargs:
            ac_la = ActionChains(driver)
            ac_la.move_to_element_with_offset(driver.find_element_by_name('Layer Attributes'), 280, -10).click().perform()
            time.sleep(1)           
            for x in kwargs['Layer_Attributes']:
                layer_elem = driver.find_element_by_name(x)
                ac = ActionChains(driver)
                ac.key_down(Keys.CONTROL)
                ac.click(layer_elem)
                ac.key_up(Keys.CONTROL)
                ac.perform()
            driver.find_element_by_name("Button1").click()
        if 'Unique_Id' in kwargs: 
            if kwargs['Unique_Id'] == 'Disabled':
                self.verify_unique_id(driver)
            else:
                #TODO: For scenarios where a unique id is requested, click through to select it and verify that the info matches
                time.sleep(1)
        if 'Transparency' in kwargs:
            ac_trans = ActionChains(driver)
            ac_trans.move_to_element_with_offset(driver.find_element_by_name('Layer Visualizations'), 200, 20).click().perform()
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.typewrite(kwargs['Transparency'])
            time.sleep(1)
        if 'Enable_Popups' in kwargs:
            ac_ep = ActionChains(driver)
            ac_ep.move_to_element_with_offset(driver.find_element_by_name('Layer Visualizations'), 200, 40).click().perform()
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.typewrite(kwargs['Enable_Popups'])
            time.sleep(1)
        if 'Default_Visibility' in kwargs:
            ac_dv = ActionChains(driver)
            ac_dv.move_to_element_with_offset(driver.find_element_by_name('Layer Visualizations'), 200, 60).click().perform()
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.typewrite(kwargs['Default_Visibility'])
            time.sleep(1)
        if 'Default_Extent' in kwargs:
            ac_de = ActionChains(driver)
            ac_de.move_to_element_with_offset(driver.find_element_by_name('Layer Visualizations'), 200, 80).click().perform()
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.typewrite(kwargs['Default_Extent'])
            time.sleep(1)
        if 'Use' in kwargs:
            ac_use = ActionChains(driver)
            ac_use.move_to_element_with_offset(driver.find_element_by_name('Use'), 150, 5).click().perform()
            driver.find_element_by_name(kwargs['Use']).click()
            time.sleep(1)
        if 'Color' in kwargs and kwargs['Color'] != "default":
            coordinates = kwargs['Color_Coordinates']
            self.color_picker(driver, coordinates['x'], coordinates['y'], "Color")
        #TODO: Outline color, thickness, style
        if 'Outline_Color' in kwargs or 'Outline_Thickness' in kwargs or 'Outline_Style' in kwargs:
            self.outline_settings(driver, **kwargs)
        time.sleep(1)
      
    '''  
    def click_on_menu_item_old(self, driver, menu, click_type, item_list, menu_item, **kwargs): #include a parameter to import a list for menu items
        #TODO: Accept name of menu/menu item and then parse into locator name
        click_types = {'Left': 'click', 'Right': 'context_click', 'Double': 'double_click'}
        ac_menu = ActionChains(driver)
        menu_locator = (AsRibbonLocators.__dict__[menu])
        menu_item_locator = (AsRibbonLocators.__dict__[menu_item])
        if 'offset' in kwargs:
            ac_menu.move_to_element_with_offset(driver.find_element(menu), kwargs['offset'][x], kwargs['offset'][y]).click_types[click_type]().perform()
        else:
            ac_menu.move_to_element(driver.find_element(*menu_locator)).click_types[click_type]().perform()
        time.sleep()
        driver.find_element(*menu_item_locator).click()  '''
    '''
    def click_on_menu_item(self, driver, menu_elem, find_by, click_type, item_dict, menu_item, offset = {'x': 1, 'y': 1}):
    #TODO: Accept name of menu/menu item and then parse into locator name
        #driver = self.driver
        click_types = {'Left': 'click', 'Right': 'context_click', 'Double': 'double_click'}
        ac_menu = ActionChains(driver)
        menu_locator = (find_by, menu_elem)
        menu_item_locator = (item_dict[menu_item], menu_item)
        ac_menu.move_to_element_with_offset(driver.find_element(*menu_locator), offset['x'], offset['y'])
        getattr(ac_menu, click_types[click_type])()
        ac_menu.perform()
        time.sleep(1)
        driver.find_element(*menu_item_locator).click()  
        '''
    def select_item_from_dropdown_menu(self, driver, parent_object, click_type, menu_item, move_type, *args):
        '''
        select_item_from_dropdown_menu((By.ID, "23456"), "Left", "City", "no offset")
        select_item_from_dropdown_menu((By.NAME, "Geographic Role"), "Left", "City", "offset", 100, 0)
        
        parent_object: takes in a tuple starting with find method and ending with the find value
        click_type: left, right, double - these are mouse clicks
        menu_item: select key from item_dict by item name
        move_type: offset, no offset - tell the function whether or not you will be including an offset when opening the menu
        *args: either input nothing more or two ints, x and y, to include an offset
        '''
        driver = self.driver
        click_types = {'Left': 'click', 'Right': 'context_click', 'Double': 'double_click'}
        move_types = {'no offset': 'move_to_element', 'offset': 'move_to_element_with_offset'}
        ac_menu = ActionChains(driver)
        getattr(ac_menu, move_types[move_type])(driver.find_element(*parent_object), *args)
        getattr(ac_menu, click_types[click_type])()
        ac_menu.perform()
        time.sleep(1)
        driver.find_element_by_name(menu_item).click()  
        time.sleep(1)
        
    def element_clicker(self, driver, object, click_type, move_type, *args):
        #driver = self.driver
        click_types = {'left': 'click', 'right': 'context_click', 'double': 'double_click', 'hold': 'click_and_hold'}
        move_types = {'no offset': 'move_to_element', 'offset': 'move_to_element_with_offset'}
        ac_menu = ActionChains(driver)
        getattr(ac_menu, move_types[move_type])(driver.find_element(*object), *args)
        getattr(ac_menu, click_types[click_type.lower()])().perform()
        time.sleep(1) 
        
    def get_html_attribute(self, driver, obj_css, attribute_name):
        attributes = driver.find_element_by_css_selector(obj_css).get_attribute("outerHTML").split()
        snip = len(attribute_name)
        for x in attributes:
            if x[:snip] == attribute_name:
                print (x[(snip+1):].strip('"'))

    def release(self, driver, *args):
        ac_release = ActionChains(driver)
        ac_release.release(*args).perform()
        time.sleep(1)
        
    def settings_geo_role(self, driver, request, geographic_role, **kwargs):
        #replace rest of function with this one line when available
        #edit variable names so that they become locators to be passed in?
        self.click_on_menu_item(driver, "as_menu_request", "Left", request, 100, 5)
        self.click_on_menu_item(driver, "as_menu_geographic_role", "Left", geographic_role, 100, 5)
        
        #if(geographic_role != "Point Of Interest"):
            
        
        if 'Column' in kwargs:       
            ac_col = ActionChains(driver)
            ac_col.move_to_element_with_offset(driver.find_element_by_name("Column(s) that match the role"), 250, 5).click().perform() 
            elem = driver.find_element_by_id("3")
            elem.click()
            elem_name = elem.get_attribute("Name")
            time.sleep(1)
            while elem_name != kwargs['Column']:
                pyautogui.press('down')
                elem_name = elem.get_attribute("Name")       
                time.sleep(1) 

        
    def outline_settings(self, driver, **kwargs):
        if 'Outline_Color' in kwargs and kwargs['Outline_Color'] != "default":
            coordinates = kwargs['Outline_Coordinates']
            self.color_picker(driver, coordinates['x'], coordinates['y'], "Outline")
        if 'Outline_Thickness' in kwargs:
            driver.find_element_by_id("23521").click()
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.typewrite(kwargs['Outline_Thickness'])
            time.sleep(1)
        if  'Outline_Style' in kwargs:
            driver.find_element_by_id("23518").click()
            time.sleep(1)
            driver.find_element_by_name(kwargs['Outline_Style']).click()
            time.sleep(1)
        time.sleep(1)
        
    def get_style(self, driver, obj_css):
        attributes = driver.find_element_by_css_selector(obj_css).get_attribute("outerHTML").split()
        for x in attributes:
            if x[:4] == "dojo":
                print (x[19:].strip('"'))
            
    def save(self, driver, **kwargs):
        driver.find_element_by_name("Save").click()
        #TODO: Check if the name already exists. If so, overwrite it. (Or am I supposed to throw an error instead?)
        #Otherwise, find name box within save screen, clear it, and enter the requested name
        try:
            if 'File_Name' in kwargs:
                pyautogui.typewrite(kwargs['File_Name'])
                time.sleep(1)
                driver.find_element_by_name("OK").click()
            time.sleep(1)    
            try:
                driver.find_element_by_id("65535")
                driver.find_element_by_name("Yes").click()
                time.sleep(1)
            except: 
                print("Not prompted to overwrite existing HTML")
        except:
            pass
        
        
        
    def run(self, driver, **kwargs):
        #Open the browser to the webfocus site and navigate through to open the html from the appropriate folder?
        driver.find_element_by_name("Run").click()
        time.sleep(1)
        
    def wf_run(self, driver, **kwargs):
        if 'Server' in kwargs:
            website = "http://" + kwargs['Server'] + ":8080/ibi_apps/signin" 
            driver.get(website)
            time.sleep(2)
            driver.find_element_by_id("SignonUserName").send_keys(kwargs['User'])
            driver.find_element_by_id("SignonPassName").send_keys(kwargs['Pass'])
            driver.find_element_by_id("SignonbtnLogin").click()
            time.sleep(2)
        if 'Path' in kwargs:
            text_site = kwargs['Server'] + ":8080/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository"          
            website = []
            #obtain path to html recursively
            self.path_to_html(kwargs['Path'], website)
            for x in website:
                text_site = text_site + x

            driver.get(text_site)
            time.sleep(1)  
    
    def path_to_html(self, path, website):
        if len(path) == 1:
            website.append("&BIP_item=" + path[0] + ".htm")
        elif len(path) > 1: 
            website.append("%252F" + path.pop(0))
            self.path_to_html(path, website)  
        else:
            print("Illegal path length. Did not append.")
    
    def verify_unique_id(self, driver):
        #result isn't accurate yet - only tests to see if the field unique id exists on the screen
        self.open_panel(driver, "Settings")
        time.sleep(1)
        enabled = driver.find_element_by_id("15081").get_attribute("IsEnabled")

        if enabled == "true":
            print("Unique Id field is enabled")
        elif enabled == "false":
            print("Unique Id field is disabled")
        else:
            print("Error during verification")   
        
    def looped_color_click(self, driver):
        driver.find_element_by_name("Shape").click()
        time.sleep(1)
        palette = driver.find_element_by_name("Web Palette Colors")
        height_distance = (267/18.0)
        width_distance = 27
        rows = 18
        columns = 12       

        for y in range (1, rows+1):
            v_offset = y*height_distance - .5 * height_distance
            for x in range (1, columns+1):
                h_offset = x*width_distance - .5 * width_distance
                ac = ActionChains(driver)
                ac.move_to_element_with_offset(palette, h_offset, v_offset)
                ac.click()
                ac.perform()       
        time.sleep(1)
        
    def color_picker(self, driver, column, row, option = "none"):
        if option == "Color":
            driver.find_element_by_name("Shape").click()
        elif option == "Outline":
            driver.find_element_by_id("23721").click()
        #else:
            #print("Didn't open Web Palette selector manually")
        time.sleep(1)
        palette = driver.find_element_by_name("Web Palette Colors")
        height_distance = (267/18.0)
        width_distance = 27     
        v_offset = row*height_distance - .5 * height_distance
        h_offset = column*width_distance - .5 * width_distance
        ac = ActionChains(driver)
        ac.move_to_element_with_offset(palette, h_offset, v_offset)
        ac.click()
        ac.perform()       
        driver.find_element_by_name("OK").click()
        #This option typically closes the Settings menu unintentionally, so this extracts some of the code needed to fix that
        self.open_panel(driver, "Settings")
        time.sleep(1)
     
    def color_picker_named_colors(self):
        time.sleep(1) 
        
    def color_picker_system_colors(self):
        time.sleep(1) 
    
    def color_picker_custom_color(self):
        time.sleep(1) 
    
    def using_field(self, driver, **kwargs):
        driver.find_element_by_name("...").click()
        driver.find_element_by_name(kwargs['Using_Field']).click()
        driver.find_element_by_name("Button1").click()
             
    def symbol_settings_unique(self, driver, **kwargs):
        if 'Using_Field' in kwargs:
            self.using_field(driver, **kwargs)
        if 'Labels' in kwargs: #list of labels
            labels = kwargs['Labels']
            driver.find_element_by_name(labels.pop(0)).click()
            #This doesn't check if the element is visible currently
            for x in labels:
                label_elem = driver.find_element_by_name(x)
                ac = ActionChains(driver)
                ac.key_down(Keys.CONTROL)
                ac.click(label_elem)
                ac.key_up(Keys.CONTROL)
                ac.perform()
            driver.find_element_by_name(">").click()
            time.sleep(1)
            #TODO: Adjust color/outline color for each label call
            #DOESN'T SCROLL CURRENTLY IF TOO MANY VALUES
            for x, y in zip(kwargs['Label_Ids'], kwargs['Label_Names']):
                driver.find_element_by_name(x).click()
                driver.find_element_by_id("23605").click()
                driver.find_element_by_id("23605").send_keys(y)
        time.sleep(1)
    
    def symbol_settings_color(self, driver, **kwargs):
        if 'Using_Field' in kwargs:
            self.using_field(driver, **kwargs)
        if 'By' in kwargs:
            driver.find_element_by_name("Color Scheme").click()
            driver.find_element_by_name(kwargs['By']).click()
        if 'Number_Of_Classes' in kwargs:
            driver.find_element_by_id("23454").click()
            driver.find_element_by_name(kwargs['Number_Of_Classes']).click()
        if 'Number_Of_Classes' in kwargs:
            driver.find_element_by_id("23454").click()
            driver.find_element_by_name(kwargs['Number_Of_Classes']).click()    
        if 'Color_Scheme' in kwargs:
            scheme_elem = driver.find_element_by_id("23453")
            scheme_elem.click()
            color_number = 16 * kwargs['Color_Scheme'] + 270
            cs = ActionChains(driver)
            cs.move_to_element_with_offset(scheme_elem, 1700, color_number)
            cs.click()
            cs.perform()
        time.sleep(1)
        
    def symbol_settings_dynamic(self, driver, **kwargs):
        if 'Dynamic_Label' in kwargs:
            time.sleep(1)
        if 'Dynamic_Color' in kwargs:
            driver.find_element_by_name("Image Source").click()
        time.sleep(1)
        '''        
def pull_color_hex(driver):
driver.find_element_by_name("Shape").click()
time.sleep(1)
palette = driver.find_element_by_name("Web Palette Colors")
height_distance = (267/18.0)
width_distance = 27
rows = 18
columns = 12       

for y in range (1, rows+1):
    v_offset = y*height_distance - .5 * height_distance
    for x in range (1, columns+1):
        h_offset = x*width_distance - .5 * width_distance
        ac = ActionChains(driver)
        ac.move_to_element_with_offset(palette, h_offset, v_offset)
        ac.click()
        ac.perform()
        name = driver.find_element_by_id("15453").get_attribute("Name")
        print(webcolors.hex_to_name(name) + "=" + name)       
    time.sleep(1)
    '''      
     
    def verify_map(self):
        time.sleep(1)
        
    def navigate_map(self):
        time.sleep(1)
        
    def close_application(self, driver):
        driver.close()
        time.sleep(1)
            