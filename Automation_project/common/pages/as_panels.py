from common.lib import utillity, as_utility
from common.lib.base import BasePage
from common.locators.visualization_run_locators import VisualizationRunLocators
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, StaleElementReferenceException
import re
import time
from selenium.webdriver.support.ui import Select
from pynput.mouse import Button, Controller
from selenium.webdriver.support.color import Color
from common.locators.as_ribbon_locators import AsRibbonLocators
import time
from selenium.webdriver import ActionChains
import pyautogui
from selenium.webdriver.common.keys import Keys
import uiautomation as automation


class AS_Panels(BasePage):   
    '''def __init__(self, driver):
        super(AS_Panel, self).__init__(driver)'''
        
    def expand_panel(self, panel_name):
        options = { 'Tasks & Animations': 0,
                   'Requests & Data Sources': 1,
                   'Settings': 2,
                   'Properties': 3,
                   'File/Folder Properties': 4}
        if panel_name in options:
            panels = self.driver.find_elements_by_id("1")
            panels[options[panel_name]].click()
        else:
            print("Panel name not found. Did not open panel.")
            
    def docexpand_panel(self,panel_position):
        
        '''@author: Adithyaa AK''' 
        
        '''Description : To verify document canvas panels
           ==============================================
           Usage : as_panels_obj.docexpand_panel(1); Properties panel len=1'''
    
        panels = self.driver.find_element_by_id("59421").find_elements_by_id("1")
        panels[panel_position].click()
    
    def open_panel_general(self, panel_name):
        panels = self.driver.find_elements_by_id("1")
      
        for index, panel in enumerate(panels):
                panels[index].click()
                try:
                    self.driver.find_element_by_name(panel_name)
                    break
                except:
                    pass  
        
     
    def select_new_request_from_split_dropdown(self, fex, menu_item, *args):
        '''
        possible kwargs - fex = name of fex without extension ("" to enter none if irrelevant), menu_item = initial dropdown menu item name, *args if the menu item is further down
        '''
        driver = self.driver
        self.expand_panel('Requests & Data Sources')
        time.sleep(1)
        asutilobj = as_utility.AS_Utillity_Methods(driver)
        asutilobj.select_item_from_dropdown_menu((By.ID, "23001"), "left", menu_item, "offset", 25, 10)
        time.sleep(1)
        for arg in args:
            asutilobj.element_clicker((By.NAME, arg), "left", "no offset")
        if fex != "":
            driver.find_element_by_name(fex + ".fex").click()
            time.sleep(1)
            driver.find_element_by_name("OK").click()
            time.sleep(1)
    
    def settings_geo_role(self, request, geographic_role, **kwargs):
        '''
        settings_geo_role("zip3_baselayer", "City", columns =  [{"row": "1", "value": "POPULATION"}, {"row": 3, "value": "ZIP3"}])
        Set the first 2 parameters to "" in order to skip
        '''
        driver = self.driver
        #self.expand_panel('Settings')
        asutilobj = as_utility.AS_Utillity_Methods(driver)
        if request != "":
            asutilobj.select_item_from_dropdown_menu((By.ID, "23455"), "left", request, "no offset")
        if geographic_role != "":
            asutilobj.select_item_from_dropdown_menu((By.ID, "23456"), "left", geographic_role, "no offset") 
        if 'Columns' in kwargs:
            elem = driver.find_element_by_name("Column(s) that match the role")
            for column in kwargs['Columns']:
                self.set_grid_control_value(elem, 250, 0, int(column['row']), column['value'], "down")
        time.sleep(1)
        '''      
        if 'Columns' in kwargs:
            for index, column in enumerate(kwargs['Columns']):
                if index < 3:
                    offset_y = index*17 + 5
                else:
                    offset_y = 39
                    
                asutilobj.element_clicker((By.NAME, "Column(s) that match the role"), "left", "offset", 250, offset_y)
                elem = driver.find_element_by_name("Settings").find_element_by_id("3")
                elem.click()
                elem_name = elem.get_attribute("Name")
                time.sleep(1)
                while elem_name != column:
                    pyautogui.press('down')
                    elem_name = elem.get_attribute("Name")       
                    time.sleep(1)    
                pyautogui.press('left')    
                pyautogui.press('down')'''     
               
    def selectRequestsDataSourcesPanelToolbarMenu(self,toolbar_button_name):
        self.expand_panel("Requests & Data Sources")  
        time.sleep(1)            
        
        #button_name==[]   
        
        if toolbar_button_name == "new_split_button" :
            #Click new request (default option)
            self.driver.find_element_by_id("23001").find_element_by_name("New").click()
            #Click new request dropdown
            ac_requests = ActionChains(self.driver)
            ac_requests.move_to_element_with_offset(self.driver.find_element_by_id("23001").find_element_by_name("New"), 25, 10).click()
            ac_requests.perform()
        else:
            self.driver.find_element_by_id("23001").find_element_by_name(toolbar_button_name).click() 
            time.sleep(2) 
            """Click delete
            self.driver.find_element_by_id("23001").find_element_by_name("Delete").click()  
            #Click refresh
            self.driver.find_element_by_id("23001").find_element_by_name("Refresh parameters").click()
            #Click save
            self.driver.find_element_by_id("23001").find_element_by_name("Save Selection").click()
            #Click clear
            self.driver.find_element_by_id("23001").find_element_by_name("Clear Selection").click()
            """
    
    def SelectRequestDataSourcePanelContextMenu(self, menu_item, sub_menu_item):  
        pyautogui.click(1625, 180) #
        time.sleep(1)
        ac = ActionChains(self.self.driver)
        
        if menu_item==("Embedded Request" or "Embedded Request"):
            ac.move_to_element(self.self.driver.find_element_by_name(menu_item)).perform()
            time.sleep(2)
        else:
            ac.move_to_element(self.self.driver.find_element_by_name(menu_item)).perform()
            time.sleep(2)
            self.self.driver.find_element_by_name(sub_menu_item).click()
            time.sleep(1)
         
        '''call openfile dialog window'''                
        self.driver.find_element_by_name("zip_avg_days.fex").click()
        time.sleep(1)
        self.driver.find_element_by_name("OK").click()
        time.sleep(1)         
        """ 
        Public Sub SelectContextMenuReqAndDataPanel(ContextMenu)
        
        Select Case  ContextMenu
            Case "Empty Request"
                iCntNmr=1
            Case "Embedded Request"
                iCntNmr=2
            Case "External Request"    
                iCntNmr=3
            Case "Requests->Parameters..."
            iCntNmr=4
            Case "Requests->Parameters->Controls..."
                iCntNmr=5
            Case "New Mailto Request..."
                iCntNmr=6
            Case "Url Request..."
                iCntNmr=7
            Case "Add Data Source..."  
                iCntNmr=1   

        """   
        
    def select_html_esri_map_settings_panel_georole(self,request,georole,columnn_match_role):
        """Select request from dropdown """  
        ac_request = ActionChains(self.driver)
        ac_request.move_to_element_with_offset(self.driver.find_element_by_name('Request'), 100, 5).click().perform()
        self.driver.find_element_by_name("zip_avg_days").click()
        time.sleep(1)
        
        """Select geo role """ 
        ac_geo = ActionChains(self.driver)
        ac_geo.move_to_element_with_offset(self.driver.find_element_by_name('Geographic Role'), 100, 5).click().perform()    
        time.sleep(2)     
        self.driver.find_element_by_name("US postal code (5 digits)").click()
        time.sleep(2)

        """Select column that match the role """  
        ac_col = ActionChains(self.driver)
        ac_col.move_to_element_with_offset(self.driver.find_element_by_name("Column(s) that match the role"), 250, 5).click().perform() 
        elem = self.driver.find_element_by_id("3")# geo roles listbox
        elem.click()
        elem_name = elem.get_attribute("Name")
        time.sleep(1)
        while elem_name != "ZIP5":
            pyautogui.press('down')
            elem_name = elem.get_attribute("Name")       
            time.sleep(1) 
    
    def set_html_esri_map_layer_attributes(self, attribute_list, **kwargs):
        driver = self.driver
        ac_la = ActionChains(driver)
        ac_la.move_to_element_with_offset(driver.find_element_by_name('Layer Attributes'), 280, -10).click().perform()
        time.sleep(1)   
        #if len(attribute_list) != 1:        
        for x in attribute_list:
            layer_elem = driver.find_element_by_name(x)
            ac = ActionChains(driver)
            ac.key_down(Keys.CONTROL)
            ac.click(layer_elem)
            ac.key_up(Keys.CONTROL)
            ac.perform()
        '''if 'Row' in kwargs:
            for x in kwargs['Row']:
                ac = ActionChains(driver)
                ac.key_down(Keys.CONTROL)
                ac.perform()'''
            
        driver.find_element_by_name("Button1").click()
       
    def set_html_esri_map_layer_visulization(self,**kwargs):
        """ Default parameter = Clustering="Off",Transparency=50,Add_Heatmap="Off",Enable_Popups="Off",Default_Visibility="On",Default_Extent="Off",Spatial_Coordinate_System="4368"
        """   
        if 'Transparency' in kwargs:
                ac_trans = ActionChains(self.driver)
                ac_trans.move_to_element_with_offset(self.driver.find_element_by_name('Layer Visualizations'), 200, 20).click().perform()
                pyautogui.hotkey('ctrl', 'a')
                pyautogui.typewrite(kwargs['Transparency'])
                time.sleep(1)
        if 'Enable_Popups' in kwargs:
            ac_ep = ActionChains(self.driver)
            ac_ep.move_to_element_with_offset(self.driver.find_element_by_name('Layer Visualizations'), 200, 40).click().perform()
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.typewrite(kwargs['Enable_Popups'])
            time.sleep(1)
        if 'Default_Visibility' in kwargs:
            ac_dv = ActionChains(self.driver)
            ac_dv.move_to_element_with_offset(self.driver.find_element_by_name('Layer Visualizations'), 200, 60).click().perform()
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.typewrite(kwargs['Default_Visibility'])
            time.sleep(1)
        if 'Default_Extent' in kwargs:
            ac_de = ActionChains(self.driver)
            ac_de.move_to_element_with_offset(self.driver.find_element_by_name('Layer Visualizations'), 200, 80).click().perform()
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.typewrite(kwargs['Default_Extent'])
            time.sleep(1) 
        if 'Spatial_Coordinates' in kwargs:
            self.set_grid_control_value(kwargs['parent_obj'],kwargs['x'],kwargs['y'],kwargs['row_num'],kwargs['value'],kwargs['selection_type'])   

            
    def set_html_esri_map_layer_visualization_generic(self, *args):
        '''
        Each arg is a pair in list form where arg[0] = row and arg[1] = input value
        '''
        for x in args:
            ac_trans = ActionChains(self.driver)
            ac_trans.move_to_element_with_offset(self.driver.find_element_by_name('Layer Visualizations'), 200, 17*x[0]).click().perform()
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.typewrite(x[1])
            time.sleep(1)
        
   
    
    def symbol_settings_color(self, **kwargs):
        driver = self.driver
        if 'Using_Field' in kwargs:
            self.using_field(driver, kwargs['Using_Field'])
        if 'By' in kwargs:
            driver.find_element_by_name("Settings").find_elements_by_id("23455")[1].click()
            driver.find_element_by_name(kwargs['By']).click()
        if 'Number_Of_Classes' in kwargs:
            driver.find_element_by_id("23454").click()
            driver.find_element_by_name(kwargs['Number_Of_Classes']).click()   
        if 'Color_Scheme' in kwargs:
            asutilobj = as_utility.AS_Utillity_Methods(driver)
            asutilobj.select_item_from_dropdown_menu((By.NAME, "Color Scheme"), "left", kwargs['Color_Scheme'], "offset", 200, 10)
            '''
            scheme_elem = driver.find_elements_by_id("23453")[1]
            scheme_elem.click()
            driver.find_element_by_name("Settings").find_element_by_class_name("ComboLBox").click()
            color_number = 16 * kwargs['Color_Scheme'] + 270
            cs = ActionChains(driver)
            cs.move_to_element_with_offset(scheme_elem, 1700, color_number)
            cs.click()
            cs.perform()
            '''
        time.sleep(1)
        '''
    def click_set(driver):
        scheme_elem = driver.find_elements_by_id("23453")[1]
        scheme_elem.click()
        driver.find_element_by_name("Settings").find_element_by_class_name("ComboLBox").click()'''
    
    def using_field(self, driver, field_name):
        driver.find_element_by_name("...").click()
        driver.find_element_by_name(field_name).click()
        driver.find_element_by_name("Button1").click()
        
    def symbol_settings_dynamic(self, **kwargs):
        driver = self.driver
        if 'Dynamic_Label' in kwargs:
            driver.find_element_by_id("23713").click()
            driver.find_element_by_name(kwargs['Dynamic_Label']).click()
            driver.find_element_by_name("Button1").click()
        if 'Dynamic_Color' in kwargs:
            driver.find_element_by_id("23711").click()
            driver.find_element_by_name(kwargs['Dynamic_Color']).click()
            driver.find_element_by_name("Button1").click()  
             
    def symbol_settings_using_field(self, **kwargs):
        driver = self.driver
        if 'Use_Name' in kwargs:
            driver.find_element_by_id("23453").click()
            driver.find_element_by_name(kwargs['Use_Name']).click()
        if 'Field_Name' in kwargs:
            driver.find_element_by_id("15082").click()
            driver.find_element_by_id("15435").find_element_by_name(kwargs['Field_Name']).click()
            driver.find_element_by_id("23509").click()
            
        time.sleep(1)
         
    def set_unique_id(self,parent_object, click_type, menu_path, move_type, *args):
        as_utilobj= as_utility.AS_Utillity_Methods(self.drivers)
        driver = self.driver
        driver.find_element_by_id("15081").click()
        as_utilobj.select_item_from_dropdown_menu(parent_object, click_type, menu_path, move_type, *args)
        time.sleep(1)
        driver.find_element_by_id("23509").click()
            
        time.sleep(1)
    def symbol_settings_unique_move_visible_labels(self, direction_from, labels):
        driver = self.driver
        starting_box = {'left': driver.find_element_by_id("23669"), 'right': driver.find_element_by_id("23670")}
        confirm_buttons_to = {'left': '>', 'right': '<'}
        driver.find_element_by_name(labels.pop(0)).click()
        #This doesn't check if the element is visible currently
        for x in labels:
            asutilobj = as_utility.AS_Utillity_Methods(driver)
            asutilobj.control_click(starting_box[direction_from.lower()], (By.NAME, x))
        driver.find_element_by_name(confirm_buttons_to[direction_from.lower()]).click()
        time.sleep(1)
                  
    def symbol_settings_unique_label(self, **kwargs):
        driver = self.driver
        list_box_left = driver.find_element_by_id("12345").find_element_by_id("23669")
        list_box_right = driver.find_element_by_id("12345").find_element_by_id("23670")
        if 'Labels_Add' in kwargs: #list of labels
            labels = kwargs['Labels_Add']
            self.symbol_settings_unique_move_visible_labels("left", labels)
        if 'Labels_Not_Visible_Add' in kwargs:
            not_visible = kwargs['Labels_Not_Visible_Add']
            for x in not_visible:
                self.set_grid_control_value(list_box_left, 5, 5, x['row'], x['value'], "down")
                driver.find_element_by_name(">").click()
        if 'Labels_Remove' in kwargs: #list of labels
            labels = kwargs['Labels_Remove']
            self.symbol_settings_unique_move_visible_labels("right", labels)
        if 'Labels_Not_Visible_Remove' in kwargs:
            not_visible = kwargs['Labels_Not_Visible_Remove']
            for x in not_visible:
                self.set_grid_control_value(list_box_right, 5, 5, not_visible['row'], not_visible['value'],"down")
                driver.find_element_by_name("<").click()
    
    def symbol_settings_unique_label_names(self, label_ids, label_names):
        driver = self.driver
        if label_ids != [""]:
            for x, y in zip(label_ids, label_names):
                driver.find_element_by_name(x).click()
                if y != "":
                    driver.find_element_by_id("12345").find_elements_by_id("23605")[1].click()
                    driver.find_element_by_id("12345").find_elements_by_id("23605")[1].send_keys(y)
        
    def color_picker_web_palette(self, column, row, option = "none"):
        '''
        Column: horizontal choice from 1-12
        Row: vertical choice from 1-18
        Check the hex values to make sure you have the right shade of your color
        Note that the location of the Color Picker window is far enough from the panels that Settings will close once you click OK
        '''
        driver = self.driver
        if option != "none":
            self.color_picker_select_tab(option)
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
        #driver.find_elements_by_id("1")[0].click()
        time.sleep(1)     
        
    def color_picker_select_tab(self, option, **kwargs):
        driver = self.driver
        tabs = ["Web Palette", "Named Colors", "System Colors", "Custom Color"]
        single = {"color": (By.NAME, "Shape"), "outline": (By.ID, "23721") }
        unique = {"color": (By.ID, "23706"), "outline": (By.ID, "23730") }
        #use = ["single", "unique"]
        use = {"single": {"color": (By.NAME, "Shape"), "outline": (By.ID, "23721") }, "unique": {"color": (By.ID, "23706"), "outline": (By.ID, "23730") }}
        if option in single:
            if 'Use' in kwargs:
                driver.find_element(*use[kwargs['Use']][option.lower()]).click()
            else:
                driver.find_element(*use['single'][option.lower()]).click()
        else:
            print("Did not open color picker window")
        if 'Tab' in kwargs:
            driver.find_element_by_name(kwargs['Tab']).click()
        else:
            print("Tab selected does not exist. Did not click")
    
    def color_picker_named_colors(self, basic_additional, offset_x, offset_y, color_hex):
        driver = self.driver
        asutilobj = as_utility.AS_Utillity_Methods(driver)
        palette_id = {"basic": "15454", "additional": "15455"}
        asutilobj.element_clicker(driver.find_element_by_id("12320"), (By.ID, palette_id[basic_additional.lower()]), "left", "offset", offset_x, offset_y)
        #TODO: Change to an assertion error
        if driver.find_element_by_id("15453").get_attribute("Name") == color_hex:
            print("Verified correct color selected")
        else:
            print("Incorrect color")
        driver.find_element_by_name("OK").click()
        time.sleep(1) 
            
    def color_picker_system_colors(self, value):
        print(value)
        driver = self.driver
        asutilobj = as_utility.AS_Utillity_Methods(driver)
        asutilobj.element_clicker(driver.find_element_by_id("15456"), (By.NAME, "InactiveCaptionText"), "left", "no offset")         
        elem_name = driver.find_element_by_id("15453").get_attribute("Name").split()[0] 
        while elem_name != value:
            if(elem_name < value):
                pyautogui.press('down')
            else:
                pyautogui.press('up')    
            elem_name = driver.find_element_by_id("15453").get_attribute("Name").split()[0]    
        driver.find_element_by_name("OK").click()
        time.sleep(1) 

    def color_picker_scroll_value(self, id, color, value):
        driver = self.driver
        asutilobj = as_utility.AS_Utillity_Methods(driver)
        actual_value = int(driver.find_element_by_id(id).get_attribute("Name"))
        color_elem = color.capitalize() + ":"
        previous = 0
        while value != actual_value:
            difference = value - actual_value
            if difference < 0:
                offset_x = 50
            elif difference > 0:
                offset_x = 265
            
            if abs(difference) < 10:
                asutilobj.release()
                asutilobj.element_clicker(driver, (By.NAME, color_elem), 'left', 'offset', offset_x, 10)
            else:
                if asutilobj.is_positive(previous) != asutilobj.is_positive(difference):
                    asutilobj.release()
                asutilobj.element_clicker(driver, (By.NAME, color_elem), 'hold', 'offset', offset_x, 10)
            
            actual_value = int(driver.find_element_by_id(id).get_attribute("Name"))
            previous = difference
        asutilobj.release()
        
    def color_picker_custom_color(self, red, green, blue):
        driver = self.driver
        rgb_colors = {"red": "15457", "green": "15458", "blue": "15460"}
        self.color_picker_scroll_value(rgb_colors["red"], "red", red)
        self.color_picker_scroll_value(rgb_colors["green"], "green", green)
        self.color_picker_scroll_value(rgb_colors["blue"], "blue", blue)
        driver.find_element_by_name("OK").click()
        time.sleep(1) 
        
    def settings_outline_settings(self, **kwargs):
        driver = self.driver
        styles = ["Dot", "Dash", "None", "Solid"]
        thickness_ids = {"single": "23521", "unique": "23729"}
        style_ids = {"single": "23518", "unique": "23728"}
        if 'Outline_Thickness' in kwargs:
            if 'Use' in kwargs:
                driver.find_element_by_id(thickness_ids[kwargs['Use']]).click()
            else:
                driver.find_element_by_id("23521").click()
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.typewrite(kwargs['Outline_Thickness'])
            time.sleep(1)
        if  'Outline_Style' in kwargs and kwargs['Outline_Style'] in styles:
            if 'Use' in kwargs:
                driver.find_element_by_id(style_ids[kwargs['Use']]).click()
            else:
                driver.find_element_by_id("23518").click()
            time.sleep(1)
            driver.find_element_by_name(kwargs['Outline_Style']).click()
            time.sleep(1)
            
    def unique_symbol_settings(self, panels_obj, label_id, label_name, color_method, color, outline, thickness, style):
        """
        Usage: unique_symbol_settings(aspanelsobj, "BLUE", "BLUE", "Named Colors", ("basic", 120, 5, "#800080"), ("basic", 290, 5, "#000000"), "3", "Dash")
        """
        panels_obj.expand_panel("Settings")
        color_functions = {"named colors": "color_picker_named_colors", "system colors": "color_picker_system_colors", "custom color": "color_picker_custom_color"}
        panels_obj.symbol_settings_unique_label_names([label_id], [label_name])
        panels_obj.color_picker_select_tab("color", Tab = color_method, Use = "unique")
        getattr(panels_obj, color_functions[color_method.lower()])(*color)
        panels_obj.expand_panel("Settings")
        panels_obj.color_picker_select_tab("outline", Tab = color_method, Use = "unique")
        getattr(panels_obj, color_functions[color_method.lower()])(*outline)
        panels_obj.expand_panel("Settings")
        panels_obj.settings_outline_settings(Outline_Thickness = thickness, Outline_style = style, Use = "unique")           
    
    def set_properties_grid_control_value(self, value, *args):
        driver = self.driver
        asutilobj = as_utility.AS_Utillity_Methods(driver)
        asutilobj.element_clicker(driver, (By.ID, "842"), "left", "offset", args[0], args[1])
        elem = driver.find_element_by_id("3")      
        elem_name = elem.get_attribute("Name")
        count = 0
        while elem_name != value and count < 15:
            pyautogui.press('down')
            time.sleep(1)    
            elem_name = elem.get_attribute("Name")#driver.find_element_by_name("Style attributes").click()
            count = count + 1
        
    def set_grid_control_value(self,parent_obj,x,y,row_num,value,selection_type):
        '''
        :PARAM: parent_obj=driver.find_element_by_name("Layer Visualizations")
                x=150
                y=20
                row_num=7
                value="22222"
                selection_type=""
        '''
        driver=self.driver
        time.sleep(3)
        ac_col = ActionChains(driver)
        ac_col.move_to_element_with_offset(parent_obj, x,y).click().perform()  
        time.sleep(1)  
        pyautogui.hotkey('home')  
        time.sleep(1)  
        tmp=1
        while tmp < row_num:
            pyautogui.press('down')
            time.sleep(1)
            tmp=tmp+1
        pyautogui.hotkey("tab")
        time.sleep(1)
        elem = driver.find_element_by_id("3")      
        elem_name = elem.get_attribute("Name")
        time.sleep(1)
        
        while elem_name != value:
            print(elem_name)
            print(value)
            print(" ")
            if selection_type == "down": 
                pyautogui.press('down')
                time.sleep(1)    
            else:                    
                pyautogui.hotkey('ctrl', 'a')
                time.sleep(1)
                pyautogui.typewrite(value)
                time.sleep(1)
            elem_name = elem.get_attribute("Name")       
            time.sleep(1)
            #print(elem_name)      
    
    def settings_layer_name(self, layer_name, offset_x, offset_y):  
        #sample offset for layer1: 14, 5 
        driver = self.driver     
        layers = driver.find_element_by_id("23519")
        asutilobj = as_utility.AS_Utillity_Methods(driver)
        asutilobj.element_clicker(driver, (By.ID, "23519"), "double", "offset", offset_x, offset_y) 
        time.sleep(1)
        asutilobj.element_clicker(driver, (By.ID, "23519"), "left", "offset", offset_x, offset_y) 
        time.sleep(1)
        pyautogui.typewrite(layer_name)
        time.sleep(1)     
    
    def verify_unique_id(self):
        driver = self.driver
        enabled = driver.find_element_by_id("15081").get_attribute("IsEnabled")
        if enabled == "true":
            print("Unique Id field is enabled")
        elif enabled == "false":
            print("Unique Id field is disabled")
        else:
            print("Error during verification") 
    
    def select_unique_id(self, id):
        driver = self.driver
        driver.find_element_by_id("15081").click()
        driver.find_element_by_name(id).click()
        driver.find_element_by_id("23509").click()
        
    def symbol_settings_unique(self, **kwargs):
        driver = self.driver
        if "Size" in kwargs:
            driver.find_element_by_id("23602").click()
            driver.find_element_by_id("23602").send_keys(kwargs["Size"])
        if "Shape_Image" in kwargs:
            driver.find_element_by_id("23454").click()
            driver.find_element_by_id("12345").find_element_by_name(kwargs["Shape_Image"]).click()
            
    def settings_check_box(self, **kwargs):
        '''
        Settings panel for a check box control - inputs are all via kwargs as needed
        '''
        driver = self.driver
        if "Data_Type" in kwargs:
            driver.find_element_by_name(kwargs["Data_Type"]).click()
        if "Data_Source" in kwargs:
            driver.find_element_by_id("15078").click()
            time.sleep(1)
            asutilobj = as_utility.AS_Utillity_Methods(driver)
            asutilobj.select_tree_view_pane_item("", kwargs["Data_Source"], Parent_Object = kwargs["Data_Source_Parent"])
            driver.find_element_by_name(kwargs["Data_Source_File"]).click()
            driver.find_element_by_name("OK").click()
            #"Data Servers->EDASERVE - EDASERVE->Applications->richmondretail"
        if "Value_From" in kwargs:
            driver.find_element_by_id("15080").click()
            time.sleep(1)
            driver.find_element_by_id("5445").click()
            if "Pages_Down" in kwargs:
                for x in range(0, kwargs["Value_Pages_Down"]):
                    pyautogui.hotkey("pagedown")
            driver.find_element_by_name(kwargs["Value_From"]).click()
            driver.find_element_by_id("23509").click()
        if "Display_From" in kwargs:
            driver.find_element_by_id("15079").click()
            driver.find_element_by_id("5445").click()
            if "Pages_Down" in kwargs:
                for x in range(0, kwargs["Display_Pages_Down"]):
                    pyautogui.hotkey("pagedown")
            driver.find_element_by_name(kwargs["Display_From"]).click()
            driver.find_element_by_id("23509").click()
            
    def Verifypanel_Tooltip(self,xoffset,yoffset,component,msg,**kwargs):
    
        '''@author: Adithyaa AK : Description : To verify document canvas panel tooltips
        ================================================================================
        Usage : as_panels_obj.Verifypanel_Tooltip('5','5','Auto Hide',"Verified - Tooltip is Auto Hide",move_x=-43,move_y=-49)'''
                
        utilobj= utillity.UtillityMethods(self.driver)  
        action = ActionChains(self.driver)
        action.move_by_offset(xoffset, yoffset).perform()
        time.sleep(2)
        del action
        
        if 'move_x' in kwargs:
            action = ActionChains(self.driver)
            action.move_by_offset(kwargs['move_x'], kwargs['move_y']).perform()
            time.sleep(1)
            
        tooltip=self.driver.find_element_by_class_name('tooltips_class32').get_attribute('Name')
        utilobj.asequal(tooltip,component,msg)
        del action 
        
    def Verify_Tooltip_Using_Name(self,component,msg,**kwargs):
        
        '''@author: Adithyaa AK : Description : To verify document canvas panel tooltips 
        ================================================================================
        Usage : as_panels_obj.Verifypanel_Tooltip('5','5','Auto Hide',"Verified - Tooltip is Auto Hide",move_x=-43,move_y=-49)'''
        
        utilobj= utillity.UtillityMethods(self.driver)
        as1 = self.driver.find_element_by_name(component)
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(as1,5,5).perform()
        del action
        
        tooltip=self.driver.find_element_by_class_name('tooltips_class32').get_attribute('Name')
        utilobj.asequal(tooltip,component,msg)
        
        if 'move_x' in kwargs:
            action = ActionChains(self.driver)
            action.move_by_offset(kwargs['move_x'], kwargs['move_y']).perform()
        tooltip=self.driver.find_element_by_class_name('tooltips_class32').get_attribute('Name')
        utilobj.asequal(tooltip,component,msg)
        time.sleep(2) 
        del action 
        
    def environment_panel_file_filter(self,**kwargs):
        
        '''@adithyaa ak : Description to click filters in env panel
        ============================================================================
        Usage : as_panelsobj.environment_panel_file_filter(filter='Procedure Files')'''
        
        if "filter" in kwargs:
            automation.MenuItemControl(Name=kwargs['filter']).Click()       
            if kwargs["filter"]=="View Options":
                automation.MenuItemControl(Name=kwargs['click']).Click()
                time.sleep(1)
            
            
            
            
        