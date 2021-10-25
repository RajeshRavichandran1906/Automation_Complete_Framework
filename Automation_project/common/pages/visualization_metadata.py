from common.lib.utillity import UtillityMethods as utillityobject
from common.lib.core_utility import CoreUtillityMethods as coreutillityobject
from common.lib.base import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pyautogui, time, re, os
from pynput.keyboard import Key, Controller
from common.pages import visualization_ribbon, visualization_resultarea
from selenium.webdriver.support.color import Color
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from common.pages.core_metadata import CoreMetaData as core_metadata
from configparser import ConfigParser
from common.lib.global_variables import Global_variables
from common.lib.root_path import ROOT_PATH
import sys
if sys.platform == 'linux':
    from pykeyboard import PyKeyboard
    pykeyboard = PyKeyboard()
else:
    import keyboard

class Visualization_Metadata(BasePage):
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(Visualization_Metadata, self).__init__(driver)

    def _validate_page(self, locator):
        self.longwait.until(EC.visibility_of_element_located(locator))
    
        ''' Data Pane '''
    
    def search_metadata_field(self, field_name, field_position):
        """
        :Description: This function is used to search the metadata field by typing on the search box and then left click on the field 
        under tree.
        """
        element = self.driver.find_element_by_id("iaMetaDataBrowser").find_element_by_id("metaDataSearchTxtFld")
        utillityobject.set_text_to_textbox_using_keybord(self, field_name, text_box_elem=element)
        row_css="#iaMetaDataBrowser div[id^='QbMetaDataTree-'] td[class='']"
        try:
            l=[el for el in self.driver.find_elements_by_css_selector(row_css) if el.text.strip().replace(' ','')==field_name.replace(' ','')]
            l[field_position-1].find_element_by_css_selector("img[class='icon']").click()
        except:
            print("except")
            l=[el for el in self.driver.find_elements_by_css_selector(row_css) if el.text.strip().replace(' ','')==field_name.replace(' ','')]
            l[field_position-1].find_element_by_css_selector("img[class='icon']").click()
        time.sleep(2)
        
    def select_datatree_field(self, field_name, click_type, field_position, context_menu_path=None):
        '''
        :Description: This function is used to select field in data tree. We can do left/right/double click on the field.
        We can select the context menu by right clicking.
        :Param: click_type= 'left' OR 'right' OR 'double'
        '''
        core_metadata.select_data_field_using_master_file_data(self, field_name, field_position)
        row_css="#iaMetaDataBrowser div[id^='QbMetaDataTree-'] tr[class*='selected'] img[class='icon']"
        newelement = self.driver.find_element_by_css_selector(row_css)
        if click_type == 'left':
            coreutillityobject.left_click(self, newelement)
            time.sleep(1)
        elif click_type == 'right':
            coreutillityobject.right_click(self, newelement)
            if context_menu_path != None:
                for menu_item in context_menu_path.split('->'):
                    utillityobject.select_bipopup_list_item(self, menu_item)
            time.sleep(6)
        elif click_type == 'double':
            coreutillityobject.double_click(self, newelement)
            time.sleep(5)  
        scrollable_element_css="[id^='QbMetaDataTree']>div[class='bi-tree-view-body']"
        scroll_script_syntax='document.querySelector("{0}").scrollTop=0'.format(scrollable_element_css)
        self.driver.execute_script(scroll_script_syntax)
    
    def verify_datatree_context_menu(self,field_name, field_position, context_menu_list, msg):
        '''
        :Description: This function is used to verify the right click context menu of a data tree field item
        '''
        Visualization_Metadata.select_datatree_field(self, field_name, 'right', field_position)
        utillityobject.verify_bipopup_list_item(self, context_menu_list, msg)

    def select_querytree_field(self, field_name, click_type, field_position, context_menu_path=None):
        '''
        :Description: This function is used to select field in data tree. We can do left/right/double click on the field.
        We can select the context menu by right clicking.
        :Param: click_type= 'left' OR 'right'
        '''
        browser=Global_variables.browser_name
        row_css="#queryTreeColumn td[class='']"
        try:
            l=[el for el in self.driver.find_elements_by_css_selector(row_css) if el.text.strip()==field_name]
            filed_element = l[field_position-1].find_element_by_css_selector("img[class='icon']")
            if browser in ['ie', 'edge']:
                coreutillityobject.python_left_click(self, filed_element)
            else :
                filed_element.click()
        except:
            print("except")
            l=[el for el in self.driver.find_elements_by_css_selector(row_css) if el.text.strip()==field_name]
            filed_element = l[field_position-1].find_element_by_css_selector("img[class='icon']")
            if browser in ['ie', 'edge'] :
                coreutillityobject.python_left_click(self, filed_element)
            else :
                filed_element.click()
        time.sleep(5)
        row_css="#queryTreeColumn tr[class*='selected'] img[class='icon']"
        newelement = self.driver.find_element_by_css_selector(row_css)
        if click_type == 'left':
            coreutillityobject.left_click(self, newelement)
            time.sleep(1)
        elif click_type == 'right':
            coreutillityobject.right_click(self, newelement)
            time.sleep(1)
            if context_menu_path != None:
                for menu_item in context_menu_path.split('->'):
                    utillityobject.select_bipopup_list_item(self, menu_item)
                    time.sleep(3)
        time.sleep(3)
    
    def verify_querytree_context_menu(self,field_name, field_position, context_menu_list, msg):
        '''
        :Description: This function is used to verify the right click context menu of a data tree field item
        '''
        Visualization_Metadata.select_querytree_field(self, field_name, 'right', field_position)
        utillityobject.verify_bipopup_list_item(self, context_menu_list, msg)
        
    def verify_field_in_data_pane(self,field_type, field_name, position, msg='Step X', color_to_verify=None):
        '''
        Desc: This function is used to verify whether a field is available under data tree.
        :param field_type : 'Dimension' or 'expected_list'
        :param field_name: "Sale,Year" or "Gross Profit"
        :param position: 1,2,3.... always starts from 0     e.g.. ['Query Variables' (0), 'Measures'(1), 'Sales'(2), 'Cost of Goods,Local Currency'(3),.......] 
                        OR ['Dimensions'(0), 'Sales_Related'(1), 'Transaction Date, Simple'(2)......]
        :Usage: verify_data_pane_field('Dimension',"Product,Subcategory",12,"Step 02")
        :author: Nasir
        '''
        actual_list=[]
        datatree_items = self.driver.find_elements_by_css_selector("[id^=QbMetaDataTree] table>tbody>tr")
        actual_list.extend([i.text for i in datatree_items])
        item_index = actual_list.index(field_type) + position
        actual_name = actual_list[item_index]
        custom_msg=msg + ": verify the " + field_name + " listed under " + field_type + " in Data pane."
        utillityobject.asequal(self, field_name, actual_name, custom_msg)
        if color_to_verify != None:
            actual_color=Color.from_string(datatree_items[item_index].value_of_css_property("color")).rgba
            expected_color=utillityobject.color_picker(self, color_to_verify,'rgba')
            custom_msg=msg + ': verify the field color is ' + color_to_verify + '.'
            utillityobject.asequal(self, expected_color, actual_color, custom_msg)
    
    def verify_field_in_data_pane_list_view(self,field_name,msg,color_to_verify=None):
        '''
        Desc: This function is used to verify whether a field is available under data tree in data pane as list view.
        :param field_name: "Sale,Year" or "Gross Profit"
        :Usage: verify_data_pane_field("Product,Subcategory",12,"Step 02")
        :author: vpriya
        '''
        actual_list=[]
        datatree_items = self.driver.find_elements_by_css_selector("[id^=QbMetaDataTree] table>tbody>tr")
        actual_list.extend([i.text for i in datatree_items])
        item_index = actual_list.index(field_name)
        actual_name = actual_list[item_index]
        custom_msg=msg + ": verify the " + field_name + " listed under " + field_name + " in Data pane."
        utillityobject.asequal(self, field_name, actual_name, custom_msg)
        if color_to_verify != None:
            actual_color=Color.from_string(datatree_items[item_index].value_of_css_property("color")).rgba
            expected_color=utillityobject.color_picker(self, color_to_verify,'rgba')
            custom_msg=msg + ': verify the field color is ' + color_to_verify + '.'
            utillityobject.asequal(self, expected_color, actual_color, custom_msg)

    def click_datapane_toggle_button(self):
        '''
        Description : This function will click toggle button in the datapane
        '''
        button_css="[id^='BiToolBarToggleButton'][class*='bi-tool-bar-button']"
        button_elem=utillityobject.validate_and_get_webdriver_object(self, button_css, 'Datapane toggle button')
        coreutillityobject.python_left_click(self, button_elem)
        
    def verify_datapane_toggle_button_tooltip(self, expected_tooltip):
        '''
        This function will hover on toggle button to verify it's tooltip value
        expected_tooltip
        '''
        button_css="[id^='BiToolBarToggleButton'][class*='bi-tool-bar-button']"
        button_elem=utillityobject.validate_and_get_webdriver_object(self, button_css, 'Datapane toggle button')
        coreutillityobject.python_move_to_element(self, button_elem, element_location='middle')
        time.sleep(2)
        tooltip_css="[id^='BiToolTip']:not([style*='hidden'])"
        utillityobject.synchronize_with_number_of_element(self, tooltip_css, 1, 15)
        toggle_tooltip_elem=utillityobject.validate_and_get_webdriver_object(self, tooltip_css, 'Tooltip of IA metadata')
        actual_tooltip=toggle_tooltip_elem.text
        custom_msg='Step X : Verify datapane toggle button tooltip shown as ' + expected_tooltip + '.'
        utillityobject.asequal(self, expected_tooltip, actual_tooltip, custom_msg)
        
    def verify_field_in_query_pane(self,bucket_type,field_name, position, msg='Step X', color_to_verify=None, font_to_verify=None):
        '''
        Desc: This function is used to verify whether a field is available under data tree.
        :param bucket_type : 'Vertical Axis' or 'Rows'
        :param field_name: "Sale,Year" or "Gross Profit"
        :param position: 1,2,3.... always starts from 0
        :Usage: verify_query_pane_field('Rows',"Product,Subcategory",2,"Step 02")
        :author: Nasir
        '''
        actual_list=[]
        querytree_items = self.driver.find_elements_by_css_selector("#queryTreeColumn table>tbody>tr")
        actual_list.extend([i.text for i in querytree_items])
        item_index = actual_list.index(bucket_type) + position
        actual_name = actual_list[item_index]
        utillityobject.asequal(self,field_name,actual_name,msg + ": verify the " + field_name + " listed under " + bucket_type + " in Query pane")
        if color_to_verify != None:
            actual_color=Color.from_string(querytree_items[item_index].value_of_css_property("color")).rgba
            expected_color=utillityobject.color_picker(self, color_to_verify,'rgba')
            custom_msg=msg + ': verify the field color is ' + color_to_verify + '.'
            utillityobject.asequal(self, expected_color, actual_color, custom_msg)
        if font_to_verify != None:
            actual_font_style=querytree_items[item_index].value_of_css_property("font-style")
            custom_msg=msg + ': verify the field font style is ' + font_to_verify + '.'
            utillityobject.asequal(self, font_to_verify, actual_font_style, custom_msg)
            
    def verify_field_available_in_query_pane(self,start_bucket,field_name, end_bucket, msg='Step X', availability=True):
        '''
        :param bucket_type : 'Vertical Axis' or 'Rows'
        :param field_name: "Sale,Year" or "Gross Profit"
        :param position: 1,2,3.... always starts from 0
        :Usage: verify_query_pane_field('Rows',"Product,Subcategory",2,"Step 02")
        :author: Nasir
        '''
        actual_list=[]
        querytree_items = self.driver.find_elements_by_css_selector("#queryTreeColumn table>tbody>tr")
        actual_list.extend([i.text for i in querytree_items])
        actual_list = actual_list[actual_list.index(start_bucket)+1:actual_list.index(end_bucket)]
        if availability==True:
            utillityobject.asin(self,field_name, actual_list, msg + ": verify the " + field_name + " is listed under " + start_bucket + " in Query pane")
        else:
            utillityobject.as_notin(self,field_name, actual_list, msg + ": verify the " + field_name + " is no listed under " + start_bucket + " in Query pane")
    
    def verify_field_in_filter_pane(self,field_name=None, position=1, msg='Step X'):
        """
        :param field_type : 'Dimension' or 'Measures'
        :param field_name: "Sale,Year" or "Gross Profit"
        :param position: 1,2,3.... always starts from 0     e.g.. ['Query Variables' (0), 'Measures'(1), 'Sales'(2), 'Cost of Goods,Local Currency'(3),.......] 
                        OR ['Dimensions'(0), 'Sales_Related'(1), 'Transaction Date, Simple'(2)......]
        :Usage: verify_data_pane_field('Dimension',"Product,Subcategory",12,"Step 02")
        :Usage: verify_data_pane_field('Dimension',"Product,Subcategory",12,"Step 02",expected_len = 0) To verify filter pane is empty
        :author: Nasir
        """
        if field_name == None:
            custom_msg = msg + ": verify Filter pane is empty."
            actual_len= len(self.driver.find_element_by_css_selector("#qbFilterBox table>tbody").text.strip())
            utillityobject.asequal(self, actual_len, 0, custom_msg)
        else:
            actual_list=[]
            filtertree_items = self.driver.find_elements_by_css_selector("#qbFilterBox table>tbody>tr")
            actual_list.extend([i.text.strip() for i in filtertree_items])
            actual_name = actual_list[position-1]
            custom_msg = msg + ": verify the " + field_name + " listed under in Filter pane"
            utillityobject.asequal(self, field_name, actual_name, custom_msg)      
            
    def drag_and_drop_from_data_tree_to_query_tree(self, field_name, field_position, bucket_type,bucket_position,ele_loc="bottom_middle"):
        '''
        :Description: This function is used to drag and drop data field to the specified bucket in query tree.
        :param - field_position: 1,2 .. (first match is 1)
        :param - bucket_position: 1,2 .. (first match is 1)
        :param - ele_loc="middle" if we need to replace one field with other in query pane
        '''
        timeout=0       
        core_metadata.select_data_field_using_master_file_data(self, field_name, field_position)
        row_css="#iaMetaDataBrowser div[id^='QbMetaDataTree-'] tr[class*='selected'] > td"
        source_elem = self.driver.find_element_by_css_selector(row_css)
        source_elem_coordinate=coreutillityobject.get_web_element_coordinate(self, source_elem, element_location='middle_left', xoffset=55)
        x1=source_elem_coordinate['x']
        y1=source_elem_coordinate['y']
        querytree_items = self.driver.find_elements_by_css_selector("#queryTreeColumn table>tbody>tr>td")
        querytree_list=[i.text.strip() for i in querytree_items]
        target_elem=querytree_items[querytree_list.index(bucket_type)+bucket_position-1].find_element_by_css_selector("img[class='icon']")
        target_elem_coordinate=coreutillityobject.get_web_element_coordinate(self, target_elem, element_location=ele_loc, yoffset=-1)
        x2=target_elem_coordinate['x']
        y2=target_elem_coordinate['y']
        coreutillityobject.drag_and_drop(self, x1, y1, x2, y2)
        field_name = field_name if '->' not in field_name else field_name.split('->')[-1]
        while True:
            oBooln = field_name in self.driver.find_element_by_css_selector("#queryTreeColumn").text
            if not oBooln:
                time.sleep(1)
                if timeout == self.chart_short_timesleep:
                    raise ValueError('Drag drop [ {0} ] to [ {1} ] not successful'.format(field_name, bucket_type))
            else:
                break
            timeout+=1
#         close_ele = self.driver.find_element_by_css_selector("#iaMetaDataBrowser [id^='BiToolBarButton'][class*='text-field']")
#         close_ele.click()
#         time.sleep(1)
    
    def drag_and_drop_within_query_tree(self, source_item_name, target_item_name):
        '''
        :Description: This function is used to drag and drop data field within query tree.
        '''       
        querytree_items = self.driver.find_elements_by_css_selector("#queryTreeColumn table>tbody>tr>td")
        querytree_list=[el.text.strip() for el in querytree_items]
        source_elem=querytree_items[querytree_list.index(source_item_name)].find_element_by_css_selector("img[class='icon']")
        source_elem_coordinate=coreutillityobject.get_web_element_coordinate(self, source_elem, element_location='middle', xoffset=25)
        x1=source_elem_coordinate['x']
        y1=source_elem_coordinate['y']
        target_elem=querytree_items[querytree_list.index(target_item_name)].find_element_by_css_selector("img[class='icon']")
        target_elem_coordinate=coreutillityobject.get_web_element_coordinate(self, target_elem, element_location='bottom_middle', yoffset=1)
        x2=target_elem_coordinate['x']
        y2=target_elem_coordinate['y']
        coreutillityobject.drag_and_drop(self, x1, y1, x2, y2)
        time.sleep(5)
        
    def drag_and_drop_from_data_tree_to_filter(self, field_name, field_position):
        '''
        :Description: This function is used to drag and drop data field within query tree.
        '''       
        core_metadata.select_data_field_using_master_file_data(self, field_name, field_position)
        row_css="#iaMetaDataBrowser div[id^='QbMetaDataTree-'] tr[class*='selected'] > td"
        source_elem = self.driver.find_element_by_css_selector(row_css)
        source_elem_coordinate=coreutillityobject.get_web_element_coordinate(self, source_elem, element_location='middle_left', xoffset=55)
        x1=source_elem_coordinate['x']
        y1=source_elem_coordinate['y']
        target_elem=self.driver.find_element_by_css_selector("#qbFilterBox")
        target_elem_coordinate=coreutillityobject.get_web_element_coordinate(self, target_elem, element_location='middle')
        x2=target_elem_coordinate['x']
        y2=target_elem_coordinate['y']
        coreutillityobject.drag_and_drop(self, x1, y1, x2, y2)
        time.sleep(5)          
        
    def select_filterbox_field(self, field_name, field_position, click_type, context_menu_path=None):
        '''
        :Description: This function is used to select field in Filter box. We can do left/right on the field.
        We can select the context menu by right clicking.
        :Param: click_type= 'left' OR 'right'
        '''
        row_css="#qbFilterBox td"
        try:
            l=[el for el in self.driver.find_elements_by_css_selector(row_css) if el.text.strip()==field_name]
            l[field_position-1].find_element_by_css_selector("img[class='icon']").click()
        except:
            print("except")
            l=[el for el in self.driver.find_elements_by_css_selector(row_css) if el.text.strip()==field_name]
            l[field_position-1].find_element_by_css_selector("img[class='icon']").click()
        time.sleep(2)
        row_css="#qbFilterBox td[class*='selected'] img[class='icon']"
        newelement = self.driver.find_element_by_css_selector(row_css)
        if click_type == 'left':
            coreutillityobject.left_click(self, newelement)
            time.sleep(1)
        elif click_type == 'right':
            coreutillityobject.right_click(self, newelement)
            if context_menu_path != None:
                for menu_item in context_menu_path.split('->'):
                    utillityobject.select_bipopup_list_item(self, menu_item)
                    time.sleep(3)
        time.sleep(3)
    
    def set_bins_format(self, set_format_dict):
        '''
        :Description: This function is used to set the options in the format dialog.
        :Param: set_format_dict= {'field_type_value':'xxx',
                                    'check_box_list':[],
                                    'currency_symbol_value':'xxx',
                                    'field_length_value':'xxx',
                                    'decimals_value':'xxx',
                                    'ok_btn_click':'ok' OR 'reset' OR 'cancel'
                                    }
        check_box_list=['Percent (%)', 'Use Comma (C)', 'Suppress Comma (c)', 'Leading Zeros (L)', 'Suppress Zeros (S)']
        '''
        format_dialog_css= "div[id^='QbDialog'] div[class*='bi-window active window'] #fmtDlgOk"
        utillityobject.synchronize_with_number_of_element(self, format_dialog_css, 1, 30)
        parent_obj= self.driver.find_elements_by_css_selector("div[id^='QbDialog'] div[class*='bi-window active window']")[-1]
        if 'field_type_value' in set_format_dict:
            elems=parent_obj.find_elements_by_css_selector("#format-types-list [id^='BiListItem']")
            for elem in elems:
                if elem.text.strip()==set_format_dict['field_type_value']:
                    elem.click()
                    break
        if 'check_box_list' in set_format_dict:
            btns=parent_obj.find_elements_by_css_selector("[id$='RadioBtn'][class='bi-label']")
            btn_texts=[el.text.strip() for el in btns]
            for item in set_format_dict['check_box_list']:
                btns[btn_texts.index(item)].find_element_by_css_selector("input").click()
    
        if 'currency_symbol_value' in set_format_dict:
            elem=parent_obj.find_element_by_css_selector("#currencySymbolCBox")
            utillityobject.select_combo_box_item(self, set_format_dict['currency_symbol_value'], combobox_dropdown_elem=elem)
            
        if 'field_length_value' in set_format_dict:
            elem=parent_obj.find_element_by_css_selector("#fieldLenSpinner input")
            utillityobject.set_text_to_textbox_using_keybord(self, set_format_dict['field_length_value'], text_box_elem=elem)
            
        if 'decimals_value' in set_format_dict:
            elem=parent_obj.find_element_by_css_selector("#decimalLenSpinner input")
            utillityobject.set_text_to_textbox_using_keybord(self, set_format_dict['decimals_value'], text_box_elem=elem)
            
        if 'ok_btn_click' in set_format_dict:
            close_button_name='Ok' if set_format_dict['ok_btn_click'] == 'ok' else 'Cancel' if set_format_dict['ok_btn_click'] == 'cancel' else 'Reset'
            parent_obj.find_element_by_css_selector('#fmtDlg' + close_button_name).click()
    
    def create_bins(self, field_name, name_textbox_value=None, format_textbox_value=None, format_button_dict=None, bin_width=None, btn_click='OK'):
        '''
        :Description: This function is used to set the values in create a bins dialog.
        '''
        imputs={'name_textbox_value':'qbBinsTextFld', 'format_textbox_value':'qbBinFormatTextField', 'bin_width':'qbBinWidthTextField'}
        input_parent_css="div[id^='QbDialog'] div[class*='bi-window active window'] input#"
        bins_format_dialog= self.driver.find_elements_by_css_selector("div[id^='QbDialog'] div[class*='bi-window active window']")[-1] 
        default_bin_name=self.driver.find_element_by_css_selector(input_parent_css + imputs['name_textbox_value']).get_attribute("value")
        utillityobject.asin(self, field_name, default_bin_name, "Step X: Verify if the default bin name shows " + field_name + ".")
        if name_textbox_value != None:
            elem=self.driver.find_element_by_css_selector(input_parent_css + imputs['name_textbox_value'])
            utillityobject.set_text_to_textbox_using_keybord(self, name_textbox_value, text_box_elem=elem)
            
        if format_textbox_value != None:
            elem=self.driver.find_element_by_css_selector(input_parent_css + imputs['format_textbox_value'])
            utillityobject.set_text_to_textbox_using_keybord(self, format_textbox_value, text_box_elem=elem)
            
        if format_button_dict != None:
            format_btn_obj=self.driver.find_element_by_css_selector("div[id^='QbDialog'] div[class*='bi-window active window'] #qbBinBtnFormat")
            format_btn_obj.click()
            Visualization_Metadata.set_bins_format(self, format_button_dict)
            
        if bin_width != None:
            elem=self.driver.find_element_by_css_selector(input_parent_css + imputs['bin_width'])
            coreutillityobject.update_current_working_area_browser_specification(self)
            coreutillityobject.python_left_click(self, elem)
            time.sleep(1)
            if sys.platform == 'linux':
                pykeyboard.tap_key(pykeyboard.backspace_key)
                time.sleep(1)
                pykeyboard.tap_key(pykeyboard.backspace_key)
                time.sleep(1)
                pykeyboard.tap_key(pykeyboard.backspace_key)
                time.sleep(1)
                pykeyboard.tap_key(pykeyboard.backspace_key)
                time.sleep(1)
                pykeyboard.type_string(str(bin_width), interval=1)
            else:
                keyboard.send('backspace')
                time.sleep(1)
                keyboard.send('backspace')
                time.sleep(1)
                keyboard.send('backspace')
                time.sleep(1)
                keyboard.send('backspace')
                time.sleep(1)
                keyboard.write(bin_width,delay=1)
            time.sleep(1)
            #utillityobject.set_text_to_textbox_using_keybord(self, bin_width, text_box_elem=elem)
            
        close_button_name='#qbBinsOkBtn' if btn_click=='OK' else '#qbBinsCancelBtn' if btn_click == 'cancel' else None
        if close_button_name != None:
            bins_format_dialog.find_element_by_css_selector(close_button_name).click()
      
    def verify_bins_dialog(self, bin_dialog_title=None, name_textbox_value=None, format_textbox_value=None, format_button_visible=True, bin_width_value=None, ok_btn_status='Enabled', btn_click='OK', msg='Step X'):
        '''
        :Description: This function is used to verify different controls in create a bins dialog.
        '''
        inputs={'name_textbox_value':'qbBinsTextFld', 'format_textbox_value':'qbBinFormatTextField', 'bin_width_value':'qbBinWidthTextField'}
        input_parent_css="div[id^='QbDialog'] div[class*='bi-window active window'] input#" 
        bins_format_dialog= self.driver.find_elements_by_css_selector("div[id^='QbDialog'] div[class*='bi-window active window']")[-1]
        if bin_dialog_title != None:
            actual_bin_title=self.driver.find_element_by_css_selector("div[id^='QbDialog'] div[class*='bi-window active window'] div[class*='window-caption']").text.strip()
            utillityobject.asequal(self, bin_dialog_title, actual_bin_title, msg+": Verify the Create bin window title - " + bin_dialog_title)
            
        if name_textbox_value != None:
            default_bin_name=self.driver.find_element_by_css_selector(input_parent_css + inputs['name_textbox_value']).get_attribute("value")
            utillityobject.asin(self, name_textbox_value, default_bin_name, msg+": Verify the default bin name " + name_textbox_value)
        
        if format_textbox_value != None:
            default_bin_format=self.driver.find_element_by_css_selector(input_parent_css + inputs['format_textbox_value']).get_attribute("value")
            utillityobject.asequal(self, format_textbox_value, default_bin_format, msg+": Verify the default bin format - "+ format_textbox_value)
        
        if format_button_visible == True:
            format_btn_obj_css="div[id^='QbDialog'] div[class*='bi-window active window'] #qbBinBtnFormat"
            utillityobject.verify_object_visible(self, format_btn_obj_css, format_button_visible, msg+": Verify the format button state - "+ str(format_button_visible))
        
        if bin_width_value != None:
            default_bin_width=self.driver.find_element_by_css_selector(input_parent_css + inputs['bin_width_value']).get_attribute("value")
            utillityobject.asequal(self, bin_width_value, default_bin_width, msg+": Verify the bin width - "+ bin_width_value)
        
        ok_btn_enabled="div[id^='QbDialog'] div[class*='bi-window active window'] [id='qbBinsOkBtn']"
        ok_btn_disabled="div[id^='QbDialog'] div[class*='bi-window active window'] [id='qbBinsOkBtn'][class*='button-disabled']"
        btn_css=ok_btn_enabled if ok_btn_status=='Enabled' else ok_btn_disabled
        utillityobject.verify_object_visible(self, btn_css, True, msg+": Verify the Ok button status - "+ str(ok_btn_status))
        
        close_button_name='#qbBinsOkBtn' if btn_click=='OK' else '#qbBinsCancelBtn' if btn_click == 'cancel' else None
        if close_button_name != None:
            bins_format_dialog.find_element_by_css_selector(close_button_name).click()
            
    def change_text_field_for_group(self, change_field_txt):
        field_name_css="div[id^='QbDialog'][tabindex='0'] #dynaTextFld"
        utillityobject.set_text_field_using_actionchains(self, self.driver.find_element_by_css_selector(field_name_css), change_field_txt)
    
    def choose_value_list_for_group(self, group_value_list):
        css="div[id^='QbDialog'] [class*='active'] #dynaGrpsValuesTree[class*='tree'] table tr td[class='']"
        total_row = self.driver.find_elements_by_css_selector(css)
        if sys.platform == 'linux':
            pykeyboard.press_key(pykeyboard.control_key)
        else:
            keyboard = Controller()
            keyboard.press(Key.ctrl)
        for i in range(len(total_row)):
            total_row = self.driver.find_elements_by_css_selector(css)
            text_val = total_row[i].text.strip()
            if text_val in group_value_list:
                coreutillityobject.python_left_click(self, total_row[i])
            pyautogui.press('down')
        if sys.platform == 'linux':
            pykeyboard.release_key(pykeyboard.control_key)
        else:
            keyboard.release(Key.ctrl) 
    
    def select_options_for_group(self, btn_name):
        btns={'Group':'groupSelValuesBtn','Rename':'renameGrpBtn','Ungroup':'ungroupBtn','Ungroup All':'ungroupAllBtn','Show Other':'toggleOtherBtn'}
        btn_css="div[id^='QbDialog'] div[id=" + btns[btn_name] + "]"
        button_obj = self.driver.find_element_by_css_selector(btn_css)
        coreutillityobject.python_left_click(self, button_obj)
    
    def rename_group(self, rename_field):
        Visualization_Metadata.select_options_for_group(self,'Rename')
        if sys.platform == 'linux':
            pykeyboard.type_string(str(rename_field))
            pykeyboard.tap_key(pykeyboard.enter_key)
        else:
            keyboard = Controller()
            keyboard.type(rename_field)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
        time.sleep(10)
    
    def extend_values_in_group(self, group_value_list, group_name):
        Visualization_Metadata.choose_value_list_for_group(self,group_value_list)
        utillityobject.select_combobox_item(self, 'lstGroups', group_name)
    
    def close_group_dialog(self, btn_type):
        """
        :kwargs close_button='ok' or 'cancel' or 'Apply'          (Click ok\cancel\Apply any one button in Create IA group Dialog)
        :Usage close_ia_group_dialog(close_button='ok')
        """
        button_obj = {'ok':'dynaGrpsOkBtn','cancel':'dynaGrpsCancelBtn','Apply':'dynaGrpsApplyBtn'}
        button_css = "div[id^='QbDialog'] [class*='active'] [id=" + button_obj[btn_type] + "] img"
        ok_button_obj = self.driver.find_element_by_css_selector(button_css)
        coreutillityobject.left_click(self, ok_button_obj)
        time.sleep(3)
        
    def verify_fields_in_groupdialog(self, expected_element_list,msg, **kwargs):
        """
        :params btn_name='Show Other'
        :params expected_element_list=['Accessories', 'Televisions']    (This is value to verify from create group)
        :kwargs close_button='ok' or 'cancel' or 'Apply'
        :kwargs cord_type='middle'
        :kwargs click_opt=0(left Click)default, 1(right click), 2(double click), 3(move)
        :Usage verify_fields_in_ia_groupdialog(expected_element_list, btn_name='Show Other', close_button='ok', msg='Step16: Verify it created the groups as shown')
        """
        css="div[id^='QbDialog'] [class*='active'] #dynaGrpsValuesTree[class*='tree'] table tr td[class='']"
        actual_element_list=[]    
        legends=self.driver.find_elements_by_css_selector(css)
        for i in range(0,len(legends)):
            actual_element_list.append(legends[i].text.strip())
        print(actual_element_list)
        utillityobject.asequal(self,expected_element_list, actual_element_list, msg)
    
    def multiselect_querytree_field(self, field_name_list, context_menu_path=None):
        '''
        :Description: This function is used to multi select fields in query tree.
            We can select the context menu by right clicking.
        '''
        row_css="#queryTreeColumn td[class='']"
        if sys.platform == 'linux':
            pykeyboard.press_key(pykeyboard.control_key)
        else:
            keyboard.press('ctrl')
        for field_name in field_name_list:
            row_elems=[el for el in self.driver.find_elements_by_css_selector(row_css)]
            for row_elem in row_elems:
                if row_elem.text.strip() == field_name:
                    coreutillityobject.python_left_click(self, row_elem, mouse_move_duration=2.5)
                    time.sleep(2)
                    break
        if sys.platform == 'linux':
            pykeyboard.release_key(pykeyboard.control_key)
        else:
            keyboard.release('ctrl') 
        time.sleep(1)  
        row_css="#queryTreeColumn tr[class*='selected']"
        newelement=self.driver.find_elements_by_css_selector(row_css)[-1]
        coreutillityobject.right_click(self, newelement)
        time.sleep(1)
        if context_menu_path != None:
            for menu_item in context_menu_path.split('->'):
                utillityobject.select_bipopup_list_item(self, menu_item)
                time.sleep(2)
        time.sleep(2)
        
    def create_visualization_filters_(self, field_type, *args, close_dialog_button=None):
        """
        field_type='alpha' OR 'numeric'
        Usage: l=['[All]','EMEA']
        Usage: l=['Jan','01','2008'] For 'Starting Date' Or 'Ending Date'
        metaobj.create_visualization_filters('alpha',['Aggregation','Sum'],['Operator','Not equal to'],['GridItems',l],['Starting Date',l],['Ending Date',l])
        """
        browser=Global_variables.browser_name
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        Visualization_Metadata._validate_page(self, elem)
        if field_type=='alpha':
            operator_combo_elem=self.driver.find_element_by_css_selector("#alphaFieldPanel #avAlphaOperatorComboBox div[id^='BiButton']")
        else:
            operator_combo_elem=self.driver.find_element_by_css_selector("#numericAndDateFieldPanel #avOperatorComboBox div[id^='BiButton']")
        
        for arg in args:  
            if arg[0] == 'Aggregation':
                utillityobject.select_combobox_item(self, 'AggregationComboBox', arg[1])
                time.sleep(1)
            if arg[0] == 'By':
                utillityobject.select_combobox_item(self, 'ByFieldsComboBox', arg[1])
                time.sleep(1)
            if arg[0] == 'Operator':
                utillityobject.select_any_combobox_item(self, operator_combo_elem, arg[1])
                time.sleep(1)
            if arg[0] == 'From':
                from_element = self.driver.find_element_by_css_selector("[id*='RangeValuesBox'] [id*='From'] > input")
                from_element.clear()
                time.sleep(2)
                from_element.click()
                time.sleep(2)
                if sys.platform == 'linux':
                    pykeyboard.type_string(str(arg[1]), interval=1)
                else:
                    keyboard.write(str(arg[1]), delay=1)
                time.sleep(1)
            if arg[0] == 'To':
                from_element = self.driver.find_element_by_css_selector("[id*='RangeValuesBox'] [id*='To'] > input")
                from_element.clear()
                time.sleep(2)
                from_element.click()
                time.sleep(2)
                if sys.platform == 'linux':
                    pykeyboard.type_string(str(arg[1]), interval=1)
                else:
                    keyboard.write(str(arg[1]), delay=1)
                time.sleep(1)
            if arg[0] == 'Sort':
                utillityobject.select_combobox_item(self, 'SortValuesComboBox', arg[1])
                time.sleep(1)
            if arg[0] == 'ShowPrompt':
                self.driver.find_element_by_css_selector("#avFilterShowPrompt input:enabled").click()
                time.sleep(1)
            if arg[0] == 'SearchValues':
                search_element = self.driver.find_element_by_css_selector("#avSearchBox > input")
                search_element.click()
                time.sleep(3)
                search_element.clear()
                if browser in ['ie', 'edge']:
                    time.sleep(7)
                    pyautogui.typewrite(arg[1])
                else:
                    time.sleep(3)
                    search_element.send_keys(arg[1])
                time.sleep(1)
            if arg[0] == 'GridItems':
                self.select_or_verify_visualization_filter_values(arg[1])
            if arg[0] == 'Starting Date':
                for combo_id, date_item in zip(['dateInputCmb1', 'dateInputCmb2', 'dateInputCmb3'], arg[1]):
                    combo_btn_css=self.driver.find_element_by_css_selector("#dateTimePickerFrom #" + combo_id + " div[id^='BiButton']")
                    utillityobject.select_any_combobox_item(self, combo_btn_css, date_item)
                    time.sleep(1)
            if arg[0] == 'Ending Date':
                for combo_id, date_item in zip(['dateInputCmb1', 'dateInputCmb2', 'dateInputCmb3'], arg[1]):
                    combo_btn_css=self.driver.find_element_by_css_selector("#dateTimePickerTo #" + combo_id + " div[id^='BiButton']")
                    utillityobject.select_any_combobox_item(self, combo_btn_css, date_item)
                    time.sleep(1)
        if close_dialog_button != None:
            if close_dialog_button=='ok':
                action1 = ActionChains(self.driver)
                action1.move_to_element(self.driver.find_element_by_id("avFilterOkBtn")).click(self.driver.find_element_by_id("avFilterOkBtn")).perform()
                del action1
            elif close_dialog_button=='cancel':
                action1 = ActionChains(self.driver)
                action1.move_to_element(self.driver.find_element_by_id("avFilterCancelBtn")).click(self.driver.find_element_by_id("avFilterCancelBtn")).perform()
                del action1
        time.sleep(2)
        
    def verify_visualization_filters(self, field_type, *args, **kwargs):
        """
        field_type='alpha' OR 'numeric'
        args = ['Aggregation','(None)','false'] - [title, value, disable status('true' if disabled, 'false' if enabled)
        args = ['ShowPrompt','true'] - [title, checked status('true' if checked, 'false' if unchecked)
        metaobj.verify_visualization_filters('numeric',['Aggregation','(None)','false'],['By','(None)','true'],['Operator','Range','false'],['Sort','Ascending','true'],
        ['ShowPrompt','true'],msg="Step10:")
        author: Kiruthika
        """
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        Visualization_Metadata._validate_page(self, elem)
        if field_type=='alpha':
            operator_combo_elem=self.driver.find_element_by_css_selector("#alphaFieldPanel #avAlphaOperatorComboBox div[id^='BiButton']")
        else:
            operator_combo_elem=self.driver.find_element_by_css_selector("#numericAndDateFieldPanel #avOperatorComboBox div[id^='BiButton']")
        combo={'Aggregation':"#avAggregationComboBox",'By':"#avByFieldsComboBox",'Operator':"#avOperatorComboBox",'From':"#avfFromValue",'To':'#avfToValue',
               'Sort':'#avfSortValuesComboBox'}
        for arg in args:  
            if arg[0] == 'ShowPrompt':
                show_prompt_ele = self.driver.find_element_by_css_selector("#avFilterShowPrompt input")
                checked_status = show_prompt_ele.get_attribute("checked")
                utillityobject.asequal(self, checked_status, arg[1], kwargs['msg']+" Verify ShowPrompt checked/unchecked status")
                time.sleep(1)
            else:
                if arg[0] in combo.keys():
                    ele = self.driver.find_element_by_css_selector(combo[arg[0]])
                    utillityobject.asequal(self, ele.text.strip().replace('\n ',''), arg[1], kwargs['msg']+" Verify "+arg[0]+" value")
                    disabled_status = 'false' if ele.get_attribute("disabled")==None else 'true'
                    utillityobject.asequal(self, disabled_status, arg[2], kwargs['msg']+" Verify "+arg[0]+" combo box enable/disable status")
                    time.sleep(1)

    def verify_filter_dialog_item_list(self, expected_item_list, msg):
        """
        expected_item_list=['[All]', 'Blu Ray', 'Boom Box', 'CRT TV']
        Usage: verify_filter_dialog_item_list(expected_item_list, "Step10:")
        """
        items=self.driver.find_elements_by_css_selector("div[id*='CheckBoxItem'] div[id*='BiCheckBox']")
        if Global_variables.browser_name != 'edge':
            actual_item_list=[el.text for el in items][: len(expected_item_list)]
        else:
            actual_item_list=[el.text for el in items][::-1][: len(expected_item_list)]
        utillityobject.as_List_equal(self, expected_item_list, actual_item_list, msg+ "- Verify filter dialog item list at the time of creation")
     
    """========================================Old functions===============================================""""""""" 
    def create_visualization_filters(self, field_type, *args, ok=True):
        """
        field_type='alpha' OR 'numeric'
        Usage: l=['[All]','EMEA']
        Usage: l=['Jan','01','2008'] For 'Starting Date' Or 'Ending Date'
        metaobj.create_visualization_filters('alpha',['Aggregation','Sum'],['Operator','Not equal to'],['GridItems',l],['Starting Date',l],['Ending Date',l])
        """
        browser=Global_variables.browser_name
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        Visualization_Metadata._validate_page(self, elem)
        if field_type=='alpha':
            operator_combo_elem=self.driver.find_element_by_css_selector("#alphaFieldPanel #avAlphaOperatorComboBox div[id^='BiButton']")
        else:
            operator_combo_elem=self.driver.find_element_by_css_selector("#numericAndDateFieldPanel #avOperatorComboBox div[id^='BiButton']")
        
        for arg in args:  
            if arg[0] == 'Aggregation':
                utillityobject.select_combobox_item(self, 'AggregationComboBox', arg[1])
                time.sleep(1)
            if arg[0] == 'By':
                utillityobject.select_combobox_item(self, 'ByFieldsComboBox', arg[1])
                time.sleep(1)
            if arg[0] == 'Operator':
                utillityobject.select_any_combobox_item(self, operator_combo_elem, arg[1])
                time.sleep(1)
            if arg[0] == 'From':
                from_element = self.driver.find_element_by_css_selector("[id*='RangeValuesBox'] [id*='From'] > input")
                from_element.clear()
                time.sleep(2)
                from_element.click()
                time.sleep(2)
                if sys.platform == 'linux':
                    pykeyboard.type_string(str(arg[1]), interval=1)
                else:
                    keyboard.write(str(arg[1]), delay=1)
                time.sleep(1)
            if arg[0] == 'To':
                from_element = self.driver.find_element_by_css_selector("[id*='RangeValuesBox'] [id*='To'] > input")
                from_element.clear()
                time.sleep(2)
                from_element.click()
                time.sleep(2)
                if sys.platform == 'linux':
                    pykeyboard.type_string(str(arg[1]), interval=1)
                else:
                    keyboard.write(str(arg[1]), delay=1)
                time.sleep(1)
            if arg[0] == 'Sort':
                utillityobject.select_combobox_item(self, 'SortValuesComboBox', arg[1])
                time.sleep(1)
            if arg[0] == 'ShowPrompt':
                self.driver.find_element_by_css_selector("#avFilterShowPrompt input:enabled").click()
                time.sleep(1)
            if arg[0] == 'SearchValues':
                search_element = self.driver.find_element_by_css_selector("#avSearchBox > input")
                search_element.click()
                time.sleep(3)
                search_element.clear()
                if browser in ['ie', 'edge']:
                    time.sleep(7)
                    pyautogui.typewrite(arg[1])
                else:
                    time.sleep(3)
                    search_element.send_keys(arg[1])
                time.sleep(1)
            if arg[0] == 'GridItems':
                self.select_or_verify_visualization_filter_values(arg[1])
            if arg[0] == 'Starting Date':
                for combo_id, date_item in zip(['dateInputCmb1', 'dateInputCmb2', 'dateInputCmb3'], arg[1]):
                    combo_btn_css=self.driver.find_element_by_css_selector("#dateTimePickerFrom #" + combo_id + " div[id^='BiButton']")
                    utillityobject.select_any_combobox_item(self, combo_btn_css, date_item)
                    time.sleep(1)
            if arg[0] == 'Ending Date':
                for combo_id, date_item in zip(['dateInputCmb1', 'dateInputCmb2', 'dateInputCmb3'], arg[1]):
                    combo_btn_css=self.driver.find_element_by_css_selector("#dateTimePickerTo #" + combo_id + " div[id^='BiButton']")
                    utillityobject.select_any_combobox_item(self, combo_btn_css, date_item)
                    time.sleep(1)
        if ok==True:
            action1 = ActionChains(self.driver)
            action1.move_to_element(self.driver.find_element_by_id("avFilterOkBtn")).click(self.driver.find_element_by_id("avFilterOkBtn")).perform()
            del action1
        else:
            action1 = ActionChains(self.driver)
            action1.move_to_element(self.driver.find_element_by_id("avFilterCancelBtn")).click(self.driver.find_element_by_id("avFilterCancelBtn")).perform()
            del action1
        time.sleep(2)
    
    def wait_for_data_tree_search_field_text(self, element_, visble_element_text, expire_time, pause_time=1):
        '''
        This function check data tree search filed value.
        '''
        timeout=0
        run_ = True
        while run_:
            timeout+=1
            if timeout == int(expire_time)+1:
                raise ValueError("Unable to type field value '" + str(visble_element_text) + "' in Data tree search field Input Box.")
                run_=False
                break
            try:
                temp_str_value=element_.get_attribute('value').replace('\n','')
            except NoSuchElementException:
                time.sleep(pause_time)
                continue
            except StaleElementReferenceException:
                time.sleep(pause_time)
                continue
            str_value = re.sub(' ','',temp_str_value)
            if str_value == str(visble_element_text.replace(' ','')):
                run_=False
                break
        time.sleep(pause_time)
    
    def datatree_field_click(self, field_name, click_type, position, *args, **kwargs):
        #row_css="#iaMetaDataBrowser div[id^='QbMetaDataTree-'] tr[class*='selected']"
        Visualization_Metadata.select_data_field(self, field_name)
        #utillityobject.synchronize_with_visble_text(self, row_css, field_name, 10)
        data_pane_tooltip_css=".bi-tool-tip[style*='inherit']:not([style*='display'])"
        row_css="#iaMetaDataBrowser div[id^='QbMetaDataTree-'] tr[class*='selected'] img[class='icon']"
        newelement = self.driver.find_element_by_css_selector(row_css)
        coreutillityobject.move_to_element(self, newelement)
        utillityobject.synchronize_until_element_disappear(self, data_pane_tooltip_css, 45)
        newelement = self.driver.find_element_by_css_selector(row_css)
        if click_type == 1 :
            utillityobject.default_click(self, newelement, click_option=1, x_offset=30)
            utillityobject.synchronize_with_number_of_element(self, "div[id^='BiPopup'][style*='inherit']", 1, 30)
            count=0
            for arg in args:
                count+=1
                utillityobject.select_or_verify_bipop_menu(self, arg, sync_expected_number=count, **kwargs)
        if click_type == 2:
            utillityobject.default_click(self, newelement, click_option=2,  x_offset=30)
            time.sleep(2)
        scrollable_element_css="[id^='QbMetaDataTree']>div[class='bi-tree-view-body']"
        scroll_script_syntax='document.querySelector("{0}").scrollTop=0'.format(scrollable_element_css)
        try:
            self.driver.execute_script(scroll_script_syntax)
        except TimeoutException:
            time.sleep(1)
        
    def drag_drop_data_tree_items_to_query_tree(self,field_name,field_position,bucket_type,position, **kwargs):
        """
        Usage: self.drag_drop_data_tree_items_to_query_tree('Discount', 1, 'Error Low',0)
        field_name: Discount (data tree field name)
        field_position: 1(always 1, if there are 2 matches with same name, then 2 for 2nd selection)
        bucket_type: Row (bucket type in query tree)
        position: 0 ( always 0, if want to drop as 2nd item in same bucket then 1)
        """       
        source_cord=kwargs['source_cord'] if 'source_cord' in kwargs else 'left'
        target_cord=kwargs['target_cord'] if 'target_cord' in kwargs else 'bottom_middle'
        source_xoff_set=kwargs['source_Xoffset'] if 'source_Xoffset' in kwargs else 55
        target_xoff_set=kwargs['target_Xoffset'] if 'target_Xoffset' in kwargs else 55
        data_pane_tooltip_css=".bi-tool-tip[style*='inherit']:not([style*='display'])"
        row_css="#iaMetaDataBrowser div[id^='QbMetaDataTree-'] tr[class*='selected']"
        Visualization_Metadata.select_data_field(self, field_name)
        #utillityobject.synchronize_with_visble_text(self, row_css, field_name, 10)
        source_elem = self.driver.find_element_by_css_selector(row_css)
        coreutillityobject.move_to_element(self, source_elem)
        utillityobject.synchronize_until_element_disappear(self, data_pane_tooltip_css, 45)
        source_elem = self.driver.find_element_by_css_selector(row_css)
        time.sleep(2)
        querytree_items = self.driver.find_elements_by_css_selector("#queryTreeColumn table>tbody>tr>td")
        querytree_list=[i.text.strip() for i in querytree_items]
        target_elem=querytree_items[querytree_list.index(bucket_type)+position]
        time.sleep(4)
        utillityobject.drag_drop_using_uisoup(self, source_elem, target_elem, src_cord_type=source_cord, trg_cord_type=target_cord, sx_offset=source_xoff_set, tx_offset=target_xoff_set, ty_offset=-1, **kwargs)
        time.sleep(2)
        scrollable_element_css="[id^='QbMetaDataTree']>div[class='bi-tree-view-body']"
        scroll_script_syntax='document.querySelector("{0}").scrollTop=0'.format(scrollable_element_css)
        try:
            self.driver.execute_script(scroll_script_syntax)
        except TimeoutException:
            time.sleep(1)
    
    def drag_drop_data_tree_items_to_filter(self, field_name, field_position, **kwargs):
        '''
        :Description: This function is used to drag and drop data field to filter
        '''   
        source_cord=kwargs['source_cord'] if 'source_cord' in kwargs else 'left'
        target_cord=kwargs['target_cord'] if 'target_cord' in kwargs else 'middle'
        source_xoff_set=kwargs['source_Xoffset'] if 'source_Xoffset' in kwargs else 55
        target_xoff_set=kwargs['target_Xoffset'] if 'target_Xoffset' in kwargs else 55
        data_pane_tooltip_css=".bi-tool-tip[style*='inherit']:not([style*='display'])"
        row_css="#iaMetaDataBrowser div[id^='QbMetaDataTree-'] tr[class*='selected']"
        Visualization_Metadata.select_data_field(self, field_name)
        #utillityobject.synchronize_with_visble_text(self, row_css, field_name, 10)
        source_elem = self.driver.find_element_by_css_selector(row_css)
        coreutillityobject.move_to_element(self, source_elem, element_location='middle_left', xoffset=45)
        utillityobject.synchronize_until_element_disappear(self, data_pane_tooltip_css, 45)
        source_elem = self.driver.find_element_by_css_selector(row_css)
        time.sleep(2)
        target_elem=self.driver.find_element_by_css_selector("#qbFilterBox")
        time.sleep(4)
        utillityobject.drag_drop_using_uisoup(self, source_elem, target_elem, src_cord_type=source_cord, trg_cord_type=target_cord, sx_offset=source_xoff_set, tx_offset=target_xoff_set, ty_offset=-1, **kwargs)
        time.sleep(2)
        scrollable_element_css="[id^='QbMetaDataTree']>div[class='bi-tree-view-body']"
        scroll_script_syntax='document.querySelector("{0}").scrollTop=0'.format(scrollable_element_css)
        try:
            self.driver.execute_script(scroll_script_syntax)
        except TimeoutException:
            time.sleep(1)
        
    def drag_drop_data_tree_items_to_query_tree_(self,field_name,field_position,bucket_type,position, **kwargs):
        """
        Usage: self.drag_drop_data_tree_items_to_query_tree('Discount', 1, 'Error Low',0)
        field_name: Discount (data tree field name)
        field_position: 1(always 1, if there are 2 matches with same name, then 2 for 2nd selection)
        bucket_type: Row (bucket type in query tree)
        position: 0 ( always 0, if want to drop as 2nd item in same bucket then 1)
        """       
        source_cord=kwargs['source_cord'] if 'source_cord' in kwargs else 'left'
        target_cord=kwargs['target_cord'] if 'target_cord' in kwargs else 'bottom_middle'
        source_xoff_set=kwargs['source_Xoffset'] if 'source_Xoffset' in kwargs else 55
        target_xoff_set=kwargs['target_Xoffset'] if 'target_Xoffset' in kwargs else 55
        data_pane_tooltip_css=".bi-tool-tip[style*='inherit']:not([style*='display'])"
        row_css="#iaMetaDataBrowser div[id^='QbMetaDataTree-'] tr[class*='selected']"
        Visualization_Metadata.select_data_field(self, field_name)
        #utillityobject.synchronize_with_visble_text(self, row_css, field_name, 10)
        source_elem = self.driver.find_element_by_css_selector(row_css)
        coreutillityobject.move_to_element(self, source_elem)
        utillityobject.synchronize_until_element_disappear(self, data_pane_tooltip_css, 45)
        source_elem = self.driver.find_element_by_css_selector(row_css)
        time.sleep(2)
        querytree_items = self.driver.find_elements_by_css_selector("#queryTreeColumn table>tbody>tr>td")
        querytree_list=[i.text.strip() for i in querytree_items]
        target_elem=querytree_items[querytree_list.index(bucket_type)+position]
        time.sleep(4)
        utillityobject.drag_drop_using_uisoup(self, source_elem, target_elem, src_cord_type=source_cord, trg_cord_type=target_cord, sx_offset=source_xoff_set, tx_offset=target_xoff_set, ty_offset=-2, **kwargs)
        time.sleep(2)
        scrollable_element_css="[id^='QbMetaDataTree']>div[class='bi-tree-view-body']"
        scroll_script_syntax='document.querySelector("{0}").scrollTop=0'.format(scrollable_element_css)
        try:
            self.driver.execute_script(scroll_script_syntax)
        except TimeoutException:
            time.sleep(1)
    
    def select_data_field(self, field_name):
        """
        This method used exapnd and select data fields and click on fields based on click type
        """
        data_pane_tooltip_css=".bi-tool-tip[style*='inherit']:not([style*='display'])"
        row_css="#iaMetaDataBrowser div[id^='QbMetaDataTree-'] tr[class*='selected']"
        privouse_field=None
        if bool(re.match('.*->.*', field_name)):
            field_path_list = field_name.split('->')
        else:
            master_file_name=self.driver.find_element_by_css_selector("#iaMetaDataBox [id^='BiGroupBoxTitle']").text.lower().strip().split(' ')[-1]
            master_file_data=os.path.join(ROOT_PATH, "master_file.data")
            parser = ConfigParser()
            parser.optionxform=str
            parser.read(master_file_data)
            parser_key=master_file_name + '_' + field_name
            check_masterfile_msg = "The Requested master file " + master_file_name + " is not listed in " + master_file_data + "."
            check_fieldname_msg = "The Requested Field name  " + field_name + " is not listed in " + master_file_data + " under " + master_file_name + " section."
            if parser.has_section(master_file_name) == False:
                raise ValueError(check_masterfile_msg)
            if parser.has_option(master_file_name, parser_key) == False:
                raise ValueError(check_fieldname_msg)
            field_path = parser[master_file_name][parser_key]
            field_path_list=field_path.split('->')
        for field_name in field_path_list :
            current_field=field_name
            if current_field == privouse_field :
                field_td_obj=Visualization_Metadata.get_required_row(self, field_name, 1)
            else:
                field_td_obj=Visualization_Metadata.get_required_row(self, field_name, 0)
            if field_name == field_path_list[-1] :
                field_icon = field_td_obj.find_element_by_css_selector("img[class='icon']")
                utillityobject.synchronize_until_element_disappear(self, data_pane_tooltip_css, 45)
                field_icon.click()
                #utillityobject.left_click_with_offset(self, field_icon)
                utillityobject.synchronize_with_visble_text(self, row_css, field_name, 10)
#                 utillityobject.click_on_screen(self, field_icon, 'middle', click_type=0)
            else :
                field_expand_icons = field_td_obj.find_elements_by_css_selector("img[src*='closed']")
                if len(field_expand_icons)>0 :
                    utillityobject.synchronize_until_element_disappear(self, data_pane_tooltip_css, 45)
                    field_expand_icons[0].click()
                    #utillityobject.left_click_with_offset(self, field_expand_icons[0])
                    time.sleep(2)
            privouse_field=field_name
            
    def scroll_and_show_data_field(self, field_name, index):
        scrolltop_offset=0
        scrollable_element_css="[id^='QbMetaDataTree']>div[class='bi-tree-view-body']"
        scroll_check_script="return arguments[0].offsetHeight + arguments[0].scrollTop == arguments[0].scrollHeight"
        scrollable_element=self.driver.find_element_by_css_selector(scrollable_element_css)
        table_row_css="[id^='QbMetaDataTree'] table[class='bi-tree-view-table']>tbody>tr>td"
        run_=True
        while  run_ :
            field_elements=self.driver.find_elements_by_css_selector(table_row_css)
            field_list=self.driver.execute_script("text=[];for(i=0;i<arguments[0].length;i++){text.push(arguments[0][i].textContent.trim())}return text", field_elements)
            scroll_status=self.driver.execute_script(scroll_check_script, scrollable_element)
            if field_name not in field_list and scroll_status==False:
                scrolltop_offset+=self.driver.execute_script('return arguments[0].offsetTop', field_elements[field_list.index(field_list[-1])])
                scroll_script_syntax='document.querySelector("{0}").scrollTop={1}'.format(scrollable_element_css, scrolltop_offset)
                self.driver.execute_script(scroll_script_syntax)
                time.sleep(1)
            else :
                scrolltop_offset+=self.driver.execute_script('return arguments[0].offsetTop', field_elements[field_list.index(field_name)])
                scroll_script_syntax='document.querySelector("{0}").scrollTop={1}'.format(scrollable_element_css, scrolltop_offset)
                #self.driver.execute_script(scroll_script_syntax)
                time.sleep(2)
                run_=False
                break
          
    def get_required_row(self, field_name, index):
        table_row_css="[id^='QbMetaDataTree'] table[class='bi-tree-view-table']>tbody>tr>td"
        Visualization_Metadata.scroll_and_show_data_field(self, field_name, index)
        field_elements=self.driver.find_elements_by_css_selector(table_row_css)
        script_cod="elements=[]; for (i=0;i<arguments[0].length;i++){if(arguments[0][i].textContent.trim()=='" + field_name + "'){elements.push(arguments[0][i])}} return elements"
        field_td_objs=self.driver.execute_script(script_cod, field_elements)
        if len(field_td_objs) == 0 :
            msg="Could not find [{0}] field in data panel".format(field_name)
            raise NoSuchElementException(msg)
        else :
            return field_td_objs[index]

        
#     def datatree_field_click(self, field_name, click_type, position, *args, **kwargs):
#         """
#         :Usage: ia.datatree_field_click('Sale,Year', 1, 2, 'Query', 'Vertical')
#         :Usage: datatree_field_click('CURR_SAL', type=2, position=1)
#         :param: type =0 : left click, type =1 : right click, type=2 : doubleclick
#         :param: option: position=1 : 1st selection, position=2 is 2nd Selection
#         __author = Niranjan 
#         16Jun2016
#         """
#         max_search_field_wait_time = 60*3
#         browser=utillityobject.parseinitfile(self,'browser') 
#         element = self.driver.find_element_by_id("iaMetaDataBrowser").find_element_by_id("metaDataSearchTxtFld")
#         exec("element.clear()")
#         exec("element.send_keys(field_name)")
#         Visualization_Metadata.wait_for_data_tree_search_field_text(self, element, field_name, max_search_field_wait_time)
# #         utillityobject.set_text_field_using_actionchains(self, element, field_name, keyboard_type=True)
#         action = ActionChains(self.driver)
#         action1 = ActionChains(self.driver)
#         row_css="#iaMetaDataBrowser div[id^='QbMetaDataTree-'] td[class='']"
#         try:
#             l=[el for el in self.driver.find_elements_by_css_selector(row_css) if el.text.strip().replace(' ','')==field_name.replace(' ','')]
#             l[position-1].find_element_by_css_selector("img[class='icon']").click()
#         except:
#             print("except")
#             l=[el for el in self.driver.find_elements_by_css_selector(row_css) if el.text.strip().replace(' ','')==field_name.replace(' ','')]
#             l[position-1].find_element_by_css_selector("img[class='icon']").click()
#         time.sleep(2)
#         row_css="#iaMetaDataBrowser div[id^='QbMetaDataTree-'] tr[class*='selected'] img[class='icon']"
#         newelement = self.driver.find_element_by_css_selector(row_css)
#         if click_type == 1:
#             if browser == 'Firefox':
#                 utillityobject.click_on_screen(self, newelement, coordinate_type='middle',click_type=1)
#                 time.sleep(3)
#             else:
#                 try:
#                     action.context_click(newelement).perform()
#                     time.sleep(3)
#                 except:
#                     print('Exception happen during context click')
#                     action1.context_click(newelement).perform()  
#                     time.sleep(3)
#             for arg in args:
#                 utillityobject.select_or_verify_bipop_menu(self, arg, **kwargs)
#             time.sleep(6)
#         if click_type == 2:
#             if browser == 'Firefox':
#                 utillityobject.click_on_screen(self, newelement, coordinate_type='middle',x_offset=20,click_type=2)
#                 time.sleep(2)
#             else:
#                 action.double_click(newelement).perform()
#             time.sleep(6)
#         #element.clear()
#         time.sleep(1)
    
#     def drag_drop_data_tree_items_to_query_tree(self,field_name,field_position,bucket_type,position, **kwargs):
#         """
#         Usage: self.drag_drop_data_tree_items_to_query_tree('Discount', 1, 'Error Low',0)
#         field_name: Discount (data tree field name)
#         field_position: 1(always 1, if there are 2 matches with same name, then 2 for 2nd selection)
#         bucket_type: Row (bucket type in query tree)
#         position: 0 ( always 0, if want to drop as 2nd item in same bucket then 1)
#         """       
#         source_cord=kwargs['source_cord'] if 'source_cord' in kwargs else 'left'
#         target_cord=kwargs['target_cord'] if 'target_cord' in kwargs else 'bottom_middle'
#         source_xoff_set=kwargs['source_Xoffset'] if 'source_Xoffset' in kwargs else 55
#         target_xoff_set=kwargs['target_Xoffset'] if 'target_Xoffset' in kwargs else 55
#         element = self.driver.find_element_by_id("iaMetaDataBrowser").find_element_by_id("metaDataSearchTxtFld")
#         utillityobject.set_text_field_using_actionchains(self, element, field_name, keyboard_type=True)
#         
#         row_css="#iaMetaDataBrowser div[id^='QbMetaDataTree-'] td[class='']"
#         try:
#             l=[el for el in self.driver.find_elements_by_css_selector(row_css) if el.text.strip()==field_name]
#             l[field_position-1].find_element_by_css_selector("img[class='icon']").click()
#         except:
#             print("except")
#             l=[el for el in self.driver.find_elements_by_css_selector(row_css) if el.text.strip()==field_name]
#             l[field_position-1].find_element_by_css_selector("img[class='icon']").click()
#         time.sleep(2)
#         row_css="#iaMetaDataBrowser div[id^='QbMetaDataTree-'] tr[class*='selected'] > td"
#         source_elem = self.driver.find_element_by_css_selector(row_css)
#         time.sleep(2)
#         querytree_items = self.driver.find_elements_by_css_selector("#queryTreeColumn table>tbody>tr>td")
#         querytree_list=[i.text.strip() for i in querytree_items]
#         target_elem=querytree_items[querytree_list.index(bucket_type)+position]
#         time.sleep(4)
#         utillityobject.drag_drop_using_uisoup(self, source_elem, target_elem, src_cord_type=source_cord, trg_cord_type=target_cord, sx_offset=source_xoff_set, tx_offset=target_xoff_set, ty_offset=-1, **kwargs)
#         time.sleep(2)
    
    def drag_drop_data_tree_items_to_slicers(self,field_name,field_position,group_index, **kwargs):
        """
        Usage: self.drag_drop_data_tree_items_to_slicers('Discount', 1, 1)
        field_name: Discount (data tree field name)
        field_position: 1(always 1, if there are 2 matches with same name, then 2 for 2nd selection)
        group_index: 1 
        """ 
        source_cord=kwargs['source_cord'] if 'source_cord' in kwargs else 'left'
        target_cord=kwargs['target_cord'] if 'target_cord' in kwargs else 'left'
        source_xoff_set=kwargs['source_Xoffset'] if 'source_Xoffset' in kwargs else 55
        target_xoff_set=kwargs['target_Xoffset'] if 'target_Xoffset' in kwargs else 55
        visualization_ribbon.Visualization_Ribbon.switch_ia_tab(self, 'Slicers', **kwargs)
        parent_css="#SlicersOptionsVBox #createSlicerGroupBtn [id^='BiLabel']"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, parent_css, 1, string_value='NewGroup', with_regular_exprestion=True)
        time.sleep(1)
        element = self.driver.find_element_by_id("iaMetaDataBrowser").find_element_by_id("metaDataSearchTxtFld")
        element.clear()
        time.sleep(1)
        element.click()
        time.sleep(3)
        element.send_keys(field_name)
        time.sleep(3)
        row_css="#iaMetaDataBrowser div[id^='QbMetaDataTree-'] td[class='']"
        try:
            l=[el for el in self.driver.find_elements_by_css_selector(row_css) if el.text.strip()==field_name]
            l[field_position-1].find_element_by_css_selector("img[class='icon']").click()
        except:
            print("except")
            l=[el for el in self.driver.find_elements_by_css_selector(row_css) if el.text.strip()==field_name]
            l[field_position-1].find_element_by_css_selector("img[class='icon']").click()
        time.sleep(2)
        row_css="#iaMetaDataBrowser div[id^='QbMetaDataTree-'] tr[class*='selected'] > td"
        source_elem = self.driver.find_element_by_css_selector(row_css)
        time.sleep(2)
        group_css="#SlicersTab #SlicersCluster_" + str(group_index)
        target_elem=self.driver.find_element_by_css_selector(group_css)
        time.sleep(2)
        utillityobject.drag_drop_using_uisoup(self, source_elem, target_elem, src_cord_type=source_cord, trg_cord_type=target_cord, sx_offset=source_xoff_set, tx_offset=target_xoff_set, **kwargs)   
        time.sleep(2)
    
    def drag_drop_data_tree_group_to_slicers(self, group_name, group_position, slicer_group_index, **kwargs):
        """
        param: group_name='Product'    
        param: group_position=2
        param: slicer_group_index=1
        usage: drag_drop_to_slicers(1, 'Product', 1)
        """
        source_cord=kwargs['source_cord'] if 'source_cord' in kwargs else 'left'
        target_cord=kwargs['target_cord'] if 'target_cord' in kwargs else 'left'
        source_xoff_set=kwargs['source_Xoffset'] if 'source_Xoffset' in kwargs else 55
        target_xoff_set=kwargs['target_Xoffset'] if 'target_Xoffset' in kwargs else 55
        visualization_ribbon.Visualization_Ribbon.switch_ia_tab(self, 'Slicers', **kwargs)
        parent_css="#SlicersOptionsVBox #createSlicerGroupBtn [id^='BiLabel']"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, parent_css, 1, string_value='NewGroup', with_regular_exprestion=True)
        time.sleep(1)
        row_css = "#iaMetaDataBrowser div[id^='QbMetaDataTree'] table>tbody>tr"    
        l=[el for el in self.driver.find_elements_by_css_selector(row_css) if el.text.strip()==group_name]
        source_elem = l[group_position-1]
        time.sleep(2)
        group_css="#SlicersTab #SlicersCluster_" + str(slicer_group_index)
        target_elem=self.driver.find_element_by_css_selector(group_css)
        time.sleep(2)
        utillityobject.drag_drop_using_uisoup(self, source_elem, target_elem, src_cord_type=source_cord, trg_cord_type=target_cord, sx_offset=source_xoff_set, tx_offset=target_xoff_set, **kwargs) 
        time.sleep(2)
              
        
    def drag_and_drop_query_items(self, item1, item2, **kwargs):
        querytree_items = self.driver.find_elements_by_css_selector("#queryTreeColumn table>tbody>tr>td")
        querytree_list=[el.text.strip() for el in querytree_items]
        source_elem=querytree_items[querytree_list.index(item1)].find_element_by_css_selector("img[class='icon']")
        target_elem=querytree_items[querytree_list.index(item2)].find_element_by_css_selector("img[class='icon']")
        src_x=kwargs['src_x'] if 'src_x' in kwargs else 40
        src_y=kwargs['src_y'] if 'src_y' in kwargs else 0
        trg_x=kwargs['trg_x'] if 'trg_x' in kwargs else 40
        trg_y=kwargs['trg_y'] if 'trg_y' in kwargs else -1
        utillityobject.drag_drop_using_uisoup(self, source_elem, target_elem, src_cord_type='middle', trg_cord_type='bottom_middle', sx_offset=src_x, sy_offset=src_y, tx_offset=trg_x, ty_offset=trg_y, **kwargs)
        time.sleep(5)

    
    def querytree_field_click(self, field_name, position, click_type = 0, *args, **kwargs):
        """
        :param self:
        :param field_name:'Sale, Year' 
        :param position:1,2...  
        :param click_type: 0 is default perform only click , 1 perform right click.
        :param args: after right click --> selection menu option-- Such as 'More', 'Aggregation', 'Minimum'
        :Usage: metaobj.querytree_field_click("Product,Category",1, "Create Group")
        __author : Niranjan Das - Gobinath T
        """
        browser=Global_variables.browser_name
        row_css="#queryTreeColumn td[class='']"
        try:
            l=[el for el in self.driver.find_elements_by_css_selector(row_css) if el.text.strip()==field_name]
            elem=l[position-1].find_element_by_css_selector("img[class='icon']")
            coreutillityobject.left_click(self, elem)
        except:
            print("except")
            l=[el for el in self.driver.find_elements_by_css_selector(row_css) if el.text.strip()==field_name]
            elem=l[position-1].find_element_by_css_selector("img[class='icon']")
            coreutillityobject.left_click(self, elem)
        time.sleep(2)
        action = ActionChains(self.driver)
        action1 = ActionChains(self.driver)
        row_css="#queryTreeColumn tr[class*='selected'] img[class='icon']"
        utillityobject.synchronize_with_number_of_element(self, row_css, 1, 90)
        new_element = self.driver.find_element_by_css_selector(row_css)
        if click_type != 0:
            if browser in ['Firefox']:
                utillityobject.click_on_screen(self, new_element, coordinate_type='middle',click_type=1)
                time.sleep(3)
            else:
                try:
                    action.context_click(new_element).perform()
                    time.sleep(3)
                except:
                    print('Exception happen during context click')
                    row_css="#queryTreeColumn tr[class*='selected'] img[class='icon']"
                    new_element1 = self.driver.find_element_by_css_selector(row_css)
                    action1.context_click(new_element1).perform()  
        time.sleep(3)
        for arg in args:
                utillityobject.select_or_verify_bipop_menu(self, arg, **kwargs)
        time.sleep(6)
        
    def filter_tree_field_click(self, field_name, position, click_type=0, *args):
        """
        Usage: filter_tree_field_click(self, Revenue, type=1, 'Delete')
        _author: Niranjan
        """
        browser=Global_variables.browser_name
        row_css="#qbFilterBox td"
        try:
            l=[el for el in self.driver.find_elements_by_css_selector(row_css) if el.text.strip()==field_name]
            l[position-1].find_element_by_css_selector("img[class='icon']").click()
        except:
            print("except")
            l=[el for el in self.driver.find_elements_by_css_selector(row_css) if el.text.strip()==field_name]
            l[position-1].find_element_by_css_selector("img[class='icon']").click()
        time.sleep(2)
        action = ActionChains(self.driver)
        action1 = ActionChains(self.driver)
        row_css="#qbFilterBox td[class*='selected'] img[class='icon']"
        utillityobject.synchronize_with_number_of_element(self, row_css, 1, 90)
        new_element = self.driver.find_element_by_css_selector(row_css)
        if click_type != 0:
            if browser in ['Firefox']:
                utillityobject.click_on_screen(self, new_element, coordinate_type='middle',click_type=1)
                time.sleep(3)
            else:
                try:
                    action.context_click(new_element).perform()
                    time.sleep(3)
                except:
                    print('Exception happen during context click')
                    row_css="#qbFilterBox td[class*='selected'] img[class='icon']"
                    new_element1 = self.driver.find_element_by_css_selector(row_css)
                    action1.context_click(new_element1).perform()  
        time.sleep(3)
        for arg in args:
                utillityobject.select_or_verify_bipop_menu(self, arg)
        time.sleep(6)
    
    def select_or_verify_visualization_filter_values(self, item_list, **kwargs):
        """
        :param verify='true' or None 
        Usage: item_list=['[All','EMEA']
        metaobj.select_or_verify_visualization_filter_values(item_list, verify='true', Ok_button=True, msg = 'step06:')
        verify='true' -> To verify check box is checked
                OR
        metaobj.select_or_verify_visualization_filter_values(item_list, verify=None, Ok_button, msg = 'step06:')
        verify=None -> To verify check box is Unchecked
        """ 
        if 'msg' in kwargs:
            kwargs['msg'] =  kwargs['msg']
        else:
            kwargs['msg'] = 'Step X:'
        for item in item_list:
            flag = 0
            checkbox_item_css="div[id$='ValuesBox']  div[id^='CheckBoxItem']"
            while flag < 200:
                elem=utillityobject.validate_and_get_webdriver_objects(self, checkbox_item_css, 'visualization_filter')
                elem_list=[el.text.strip() for el in elem]
                if item in elem_list:
                    if 'verify' in kwargs: 
                    #kwargs[verify==True]:
                        status= utillityobject.get_element_attribute(self, utillityobject.validate_and_get_webdriver_object(self, 'input', 'visualization_filter_values', parent_object=elem[elem_list.index(item)]), 'checked')
#                         status=elem[elem_list.index(item)].find_element_by_css_selector("input").get_attribute("checked")
#                         status=elem[elem_list.index(item)].find_element_by_css_selector("input").is_selected()
                        if status == 'true':
                            utillityobject.asequal(self, status, kwargs['verify'], kwargs['msg']+" verify " + item + " is checked in filter box.")
                        else:
                            utillityobject.asequal(self, status, kwargs['verify'], kwargs['msg']+" verify " + item + " is Unchecked in filter box.")
                    else:
                        elem = utillityobject.validate_and_get_webdriver_object(self, 'input', 'visualization_filter_values', parent_object=elem[elem_list.index(item)])
                        coreutillityobject.left_click(self, elem)
                        
                    flag = 200
                else:
                    for _ in range(7):
                        elem = utillityobject.validate_and_get_webdriver_object(self, "div[id$='ValuesBox'] [class*='scroll-bar-vertical'] [class*='scroll-bar-inc-button']", 'visualization_filter values')
                        coreutillityobject.left_click(self, elem)
                    flag = flag + 7
                    time.sleep(1)
            try:
                if flag > 200:
                    raise ValueError(item + "does not exist in filter grid")
            except ValueError as err:
                print(err.args)
        
        if 'Ok_button' in kwargs:
            elem = utillityobject.validate_and_get_webdriver_object(self, "#avFilterOkBtn", 'visualization_filter ok button')
            coreutillityobject.left_click(self, elem)
        time.sleep(1)
                
    def verify_data_pane_field(self,field_type, field_name, position, msg):
        """
        :param field_type : 'Dimension' or 'expected_list'
        :param field_name: "Sale,Year" or "Gross Profit"
        :param position: 1,2,3.... always starts from 0     e.g.. ['Query Variables' (0), 'Measures'(1), 'Sales'(2), 'Cost of Goods,Local Currency'(3),.......] 
                        OR ['Dimensions'(0), 'Sales_Related'(1), 'Transaction Date, Simple'(2)......]
        :Usage: verify_data_pane_field('Dimension',"Product,Subcategory",12,"Step 02")
        :author: Nasir
        """
        actual_list=[]
        datatree_items = utillityobject.validate_and_get_webdriver_objects(self, "[id^=QbMetaDataTree] table>tbody>tr", 'data_pane_field')
        actual_list.extend([i.text for i in datatree_items])
        item_index = actual_list.index(field_type) + position
        actual_name = actual_list[item_index]
        utillityobject.asequal(self,field_name,actual_name,msg + ": verify the " + field_name + " listed under " + field_type + " in Data pane")

    def verify_query_pane_field(self,bucket_type,field_name, position, msg, **kwargs):
        """
        :param bucket_type : 'Vertical Axis' or 'Rows'
        :param field_name: "Sale,Year" or "Gross Profit"
        :param position: 1,2,3.... always starts from 0
        :Usage: verify_query_pane_field('Rows',"Product,Subcategory",2,"Step 02")
        :author: Nasir
        """
        actual_list=[]
        querytree_items = self.driver.find_elements_by_css_selector("#queryTreeColumn table>tbody>tr")
        actual_list.extend([i.text for i in querytree_items])
        item_index = actual_list.index(bucket_type) + position
        actual_name = actual_list[item_index]
        utillityobject.asequal(self,field_name,actual_name,msg + ": verify the " + field_name + " listed under " + bucket_type + " in Query pane")
        if 'color' in kwargs:
            actual_color=Color.from_string(querytree_items[item_index].value_of_css_property("color")).rgba
            expected_color=utillityobject.color_picker(self, kwargs['color'],'rgba')
            utillityobject.asequal(self, expected_color, actual_color, msg)
        if 'font_style' in kwargs:
            actual_font_style=querytree_items[item_index].value_of_css_property("font-style")
            utillityobject.asequal(self,kwargs['font_style'], actual_font_style, msg)
            
    def verify_query_pane_field_available(self,start_bucket,field_name, end_bucket, msg, availability=True):
        """
        :param bucket_type : 'Vertical Axis' or 'Rows'
        :param field_name: "Sale,Year" or "Gross Profit"
        :param position: 1,2,3.... always starts from 0
        :Usage: verify_query_pane_field('Rows',"Product,Subcategory",2,"Step 02")
        :author: Nasir
        """
        actual_list=[]
        querytree_items = self.driver.find_elements_by_css_selector("#queryTreeColumn table>tbody>tr")
        actual_list.extend([i.text for i in querytree_items])
        actual_list = actual_list[actual_list.index(start_bucket)+1:actual_list.index(end_bucket)]
        if availability==True:
            utillityobject.asin(self,field_name, actual_list, msg + ": verify the " + field_name + " is listed under " + start_bucket + " in Query pane")
        else:
            utillityobject.as_notin(self,field_name, actual_list, msg + ": verify the " + field_name + " is no listed under " + start_bucket + " in Query pane")
    
    def verify_filter_pane_field(self,field_name, position, msg, **kwargs):
        """
        :param field_type : 'Dimension' or 'Measures'
        :param field_name: "Sale,Year" or "Gross Profit"
        :param position: 1,2,3.... always starts from 0     e.g.. ['Query Variables' (0), 'Measures'(1), 'Sales'(2), 'Cost of Goods,Local Currency'(3),.......] 
                        OR ['Dimensions'(0), 'Sales_Related'(1), 'Transaction Date, Simple'(2)......]
        :Usage: verify_data_pane_field('Dimension',"Product,Subcategory",12,"Step 02")
        :Usage: verify_data_pane_field('Dimension',"Product,Subcategory",12,"Step 02",expected_len = 0) To verify filter pane is empty
        :author: Nasir
        """
        if "expected_len" in kwargs:
            actual_len= len(self.driver.find_element_by_css_selector("#qbFilterBox table>tbody").text.strip())
            utillityobject.asequal(self, actual_len,kwargs['expected_len'],msg)
        else:
            actual_list=[]
            filtertree_items = self.driver.find_elements_by_css_selector("#qbFilterBox table>tbody>tr")
            actual_list.extend([i.text.strip() for i in filtertree_items])
            actual_name = actual_list[position-1]
            utillityobject.asequal(self,field_name,actual_name,msg + ": verify the " + field_name + " listed under in Filter pane")

    def expand_field_tree(self, folder_path,**kwargs):
        """
        :Param : folder_path='Store->Store->Store,Country'
        :kwargs : click_opt=0 or 1  {0(left Click), 1(right click), 2(double click), 3(move)default}     (only interger number)
        Syntax: expand_field_tree('Store->Store->Store,Country')
        Syntax: expand_field_tree('2014 Q2', click_opt=1, x_offset=35)
        @author = Nasir
        """
        source_cord=kwargs['source_cord'] if 'source_cord' in kwargs else 'left'
        target_cord=kwargs['target_cord'] if 'target_cord' in kwargs else 'left'
        source_xoff_set=kwargs['source_Xoffset'] if 'source_Xoffset' in kwargs else 55
        target_xoff_set=kwargs['target_Xoffset'] if 'target_Xoffset' in kwargs else 55
        Datatree_rows = "#iaMetaDataBrowser div[id^='QbMetaDataTree']>.bi-tree-view-body-content tr"
        click_opt=kwargs['click_opt'] if 'click_opt' in kwargs else 0
        folder_list=folder_path.split('->')
        for item in folder_list:
            datetree_items = self.driver.find_elements_by_css_selector(Datatree_rows)
            for i in range(len(datetree_items)-1):
                folder_img = datetree_items[i].find_element_by_css_selector("td>img")
                img_src=folder_img.get_attribute("src")
                if datetree_items[i].text.strip() == item and ('path_arrow_tree_closed' in img_src or 'blank_icon' in img_src):
                    try:
                        print("inside try")
                        datetree_items = self.driver.find_elements_by_css_selector(Datatree_rows)
                        time.sleep(2)
                        obj_cell_css=datetree_items[i].find_element_by_css_selector("td>img")
                        utillityobject.default_click(self, obj_cell_css, click_opt, **kwargs)
                        time.sleep(1)
                        break
                    except:
                        print("except")
                        datetree_items = self.driver.find_elements_by_css_selector(Datatree_rows)
                        obj_cell_css=datetree_items[i].find_element_by_css_selector("td>img")
                        utillityobject.default_click(self, obj_cell_css, click_opt, **kwargs)
                        time.sleep(1)
                        break
        if 'dragdrop' in kwargs:
            row_css="#iaMetaDataBrowser div[id^='QbMetaDataTree-'] tr[class*='selected'] > td"
            source_elem = self.driver.find_element_by_css_selector(row_css)
            time.sleep(2)
            querytree_items = self.driver.find_elements_by_css_selector("#queryTreeColumn table>tbody>tr>td")
            querytree_list=[i.text.strip() for i in querytree_items]
            target_elem=querytree_items[querytree_list.index(kwargs['bucket_type'])+kwargs['position']]
            time.sleep(4)
            utillityobject.drag_drop_using_uisoup(self, source_elem, target_elem, src_cord_type=source_cord, trg_cord_type=target_cord, sx_offset=source_xoff_set, tx_offset=target_xoff_set, ty_offset=-1, **kwargs)
            time.sleep(2)
            

# Function 21: Verify Filter Pane checkbox checked values
    def verification_filter_pane_checkbox(self, value, text):
        #####################################
        """
            :param value: filter pane checked values (eg: ia.verification_filter_pane_checkbox(['EMEA', 'North America'], "Step10: Verify Filter Pane Checkbox")
            @author = Kiruthika Date : 12May
        """
        total = []
        total.extend(value)
        for i in range(0,len(total)):
            equal = self.driver.find_element_by_xpath("//div[contains(text(), '"+total[i]+"')]/input")
            utillityobject.asequal(self, equal.get_attribute("checked"), 'true', text)
            # assert equal.get_attribute("checked") == 'true', "The value "+total[i]+" is not checked in filter pane"
    
    def create_ia_group(self, btn_name, element_list, **kwargs):
        """
        :params btn_name='Group' or 'Rename'
        :params element_list=['Accessories', 'Televisions']    (This is value to select from create group)
        :kwargs change_field_txt='BUSINESS_GROUP'      (To change the title text)
        :kwargs close_button='ok' or 'cancel' or 'Apply'
        :kwargs cord_type='middle'
        :kwargs click_opt=0(left Click)default, 1(right click), 2(double click), 3(move)
        :Usage1: create_ia_group('Group', ['Accessories', 'Televisions'], close_button='ok')
        element_list=['North America and South America']
        :Usage2: create_ia_group('Rename', element_list, rename_field='America')
        """
        elem=(By.CSS_SELECTOR,"div[id^='QbDialog'][tabindex='0'] #dynaTextFld")
        Visualization_Metadata._validate_page(self, elem)
        cord_type=kwargs['cord_type'] if 'cord_type' in kwargs else 'middle'
        click_opt=kwargs['click_opt'] if 'click_opt' in kwargs else 0
        if 'change_field_txt' in kwargs:
            field_name_css="div[id^='QbDialog'][tabindex='0'] #dynaTextFld"
            utillityobject.set_text_field_using_actionchains(self, self.driver.find_element_by_css_selector(field_name_css), kwargs['change_field_txt'])
        css="div[id^='QbDialog'] [class*='active'] #dynaGrpsValuesTree[class*='tree'] table tr td[class='']"
        total_row = self.driver.find_elements_by_css_selector(css)
        if sys.platform == 'linux':
            pykeyboard.press_key(pykeyboard.control_key)
        else:
            keyboard = Controller()
            keyboard.press(Key.ctrl)
        for i in range(len(total_row)):
            total_row = self.driver.find_elements_by_css_selector(css)
            text_val = total_row[i].text.strip()
            if text_val in element_list:
                utillityobject.click_on_screen(self, total_row[i], cord_type, click_opt, **kwargs)
            pyautogui.press('down')
        if sys.platform == 'linux':
            pykeyboard.release_key(pykeyboard.control_key)
        else:
            keyboard.release(Key.ctrl)
        btns={'Group':'groupSelValuesBtn','Rename':'renameGrpBtn','Ungroup':'ungroupBtn','Ungroup All':'ungroupAllBtn','Show Other':'toggleOtherBtn'}
        btn_css="div[id^='QbDialog'] div[id=" + btns[btn_name] + "]"
        button_obj = self.driver.find_element_by_css_selector(btn_css)
        utillityobject.default_left_click(self,object_locator=button_obj, **kwargs)
        if 'rename_field' in kwargs:
            if sys.platform == 'linux':
                pykeyboard.type_string(str(kwargs['rename_field']))
                pykeyboard.tap_key(pykeyboard.enter_key)
            else:
                keyboard.type(kwargs['rename_field'])
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
            time.sleep(10)
        if 'close_button' in kwargs:
            parent_css="div[id^='QbDialog'] [class*='active'] div[id='dynaGrpsOkBtn']:not([disabled]) img"
            visualization_resultarea.Visualization_Resultarea.wait_for_property(self,parent_css,1,45)
            Visualization_Metadata.close_ia_group_dialog(self, **kwargs)
        
    def verify_fields_in_ia_groupdialog(self, expected_element_list,msg, **kwargs):
        """
        :params btn_name='Show Other'
        :params expected_element_list=['Accessories', 'Televisions']    (This is value to verify from create group)
        :kwargs close_button='ok' or 'cancel' or 'Apply'
        :kwargs cord_type='middle'
        :kwargs click_opt=0(left Click)default, 1(right click), 2(double click), 3(move)
        :kwargs scroll_time='15'    (The no of times you want to click on the down arrow in the scrollbar)
        :Usage verify_fields_in_ia_groupdialog(expected_element_list, btn_name='Show Other', close_button='ok', msg='Step16: Verify it created the groups as shown')
        """
        if 'scroll_time' in kwargs:
            range_val=int(kwargs['scroll_time'])
            css="#dynaGrpsValuesTree div[id^='BiScrollBar'][class*='scroll-bar-vertical'] div[id^='BiRepeatButton'][class*='scroll-bar-inc-button']"
            for i in range(range_val):
                self.driver.find_element_by_css_selector(css).click()
                time.sleep(0.3)
        if 'btn_name' in kwargs:
            btns={'Group':'groupSelValuesBtn','Rename':'renameGrpBtn','Ungroup':'ungroupBtn','Ungroup All':'ungroupAllBtn','Show Other':'toggleOtherBtn'}
            btn_css="div[id^='QbDialog'] div[id=" + btns[kwargs['btn_name']] + "]"
            button_obj = self.driver.find_element_by_css_selector(btn_css)
            utillityobject.default_left_click(self,object_locator=button_obj, **kwargs)
        time.sleep(10)
        css="div[id^='QbDialog'] [class*='active'] #dynaGrpsValuesTree[class*='tree'] table tr td[class='']"
        actual_element_list=[]    
        legends=self.driver.find_elements_by_css_selector(css)
        for i in range(0,len(legends)):
            actual_element_list.append(legends[i].text.strip())
        print(actual_element_list)
        utillityobject.asequal(self,expected_element_list, actual_element_list, msg)
        if 'close_button' in kwargs:
            Visualization_Metadata.close_ia_group_dialog(self, **kwargs)
     
    def close_ia_group_dialog(self, **kwargs):
        """
        :kwargs close_button='ok' or 'cancel' or 'Apply'          (Click ok\cancel\Apply any one button in Create IA group Dialog)
        :Usage close_ia_group_dialog(close_button='ok')
        """
        button_obj = {'ok':'dynaGrpsOkBtn','cancel':'dynaGrpsCancelBtn','Apply':'dynaGrpsApplyBtn'}
        button_css = "div[id^='QbDialog'] [class*='active'] [id=" + button_obj[kwargs['close_button']] + "] img"
        ok_button_obj = self.driver.find_element_by_css_selector(button_css)
        #utillityobject.default_left_click(self,object_locator=ok_button_obj, **kwargs)
        coreutillityobject.left_click(self,ok_button_obj)
        
    def verify_fields_in_datatree(self, folder_path, items_list, msg, **kwargs):
        """
        :Param : folder_path='Store->Store->Store,Country'
        :kwargs : click_opt=0 or 1  {0(left Click), 1(right click), 2(double click), 3(move)default}     (only interger number)
        items_list = ['GLXYT10716','GLXYT10732','GLXYT3B','GLXYT3W','GLXYT70'] ("item_list->should be a list")
        Syntax: verify_fields_in_datatree('Tablet', items_list, 'step 03: verify list of values in datatree')
        """
        self.expand_field_tree(folder_path, **kwargs)
        time.sleep(3)
        Field_items=self.driver.find_elements_by_css_selector("div[id^='QbMetaDataTree'] .bi-tree-view-table tr")
        next_item=(i.text.strip() for i in Field_items)
        while next(next_item)!=items_list[0]:
            continue
        for item in items_list[1:]:
            if next(next_item)==item:
                status=True
            else:
                status=False
                break
        del next_item
        utillityobject.asequal(self, True, status, msg)  
    
    
    def create_bin(self, field_name, btn_click='OK', **kwargs):

        '''
        bin_name : input text for bin name.
        bin_format : input text for bin format.
        bin_width : input text for bin width .
        '''
        imputs={'bin_name':'qbBinsTextFld', 'bin_format_edit':'qbBinFormatTextField', 'bin_width':'qbBinWidthTextField'}
        input_parent_css="div[id^='QbDialog'] div[class*='bi-window active window'] input#" 
        default_bin_name=self.driver.find_element_by_css_selector(input_parent_css + imputs['bin_name']).get_attribute("value")
        utillityobject.asin(self, field_name, default_bin_name, "Step X: Verify if the default bin name shows " + field_name + ".")
        if "bin_name" in kwargs:
            elem=self.driver.find_element_by_css_selector(input_parent_css + imputs['bin_name'])
            utillityobject.set_text_field_using_actionchains(self, elem, kwargs['bin_name'])
        if "bin_format_edit" in kwargs:
            elem=self.driver.find_element_by_css_selector(input_parent_css + imputs['bin_format_edit'])
            utillityobject.set_text_field_using_actionchains(self, elem, kwargs['bin_format_edit'])
        if "bin_format_btn" in kwargs:
            format_btn_obj=self.driver.find_element_by_css_selector("div[id^='QbDialog'] div[class*='bi-window active window'] #qbBinBtnFormat")
            format_btn_obj.click()
            Visualization_Metadata.set_bin_format(self, **kwargs)
        if "bin_width" in kwargs:
            elem=self.driver.find_element_by_css_selector(input_parent_css + imputs['bin_width'])
            coreutillityobject.update_current_working_area_browser_specification(self)
            coreutillityobject.python_left_click(self, elem)
            time.sleep(1)
            if sys.platform == 'linux':
                pykeyboard.tap_key(pykeyboard.backspace_key)
                time.sleep(1)
                pykeyboard.tap_key(pykeyboard.backspace_key)
                time.sleep(1)
                pykeyboard.tap_key(pykeyboard.backspace_key)
                time.sleep(1)
                pykeyboard.tap_key(pykeyboard.backspace_key)
                time.sleep(1)
                pykeyboard.type_string(str(kwargs['bin_width']), interval=1)
            else:
                keyboard.send('backspace')
                time.sleep(1)
                keyboard.send('backspace')
                time.sleep(1)
                keyboard.send('backspace')
                time.sleep(1)
                keyboard.send('backspace')
                time.sleep(1)
                keyboard.write(kwargs['bin_width'],delay=1)
            time.sleep(1)
        btn_css='#qbBinsOkBtn' if btn_click=='OK' else '#qbBinsCancelBtn'
        self.driver.find_element_by_css_selector(btn_css).click()
      
    def verify_bin(self, **kwargs):
        '''
        verify_bin_name : input text for bin name.
        verify_bin_format_edit : input text for bin format.
        verify_bin_width : input text for bin width .
        verify_bin_format_btn : format button 
        verify_bin_ok_btn : OK button
        '''
        inputs={'bin_name':'qbBinsTextFld', 'bin_format_edit':'qbBinFormatTextField', 'bin_width':'qbBinWidthTextField'}
        input_parent_css="div[id^='QbDialog'] div[class*='bi-window active window'] input#" 
        if "verify_bin_name" in kwargs:
            default_bin_name=self.driver.find_element_by_css_selector(input_parent_css + inputs['bin_name']).get_attribute("value")
            utillityobject.asin(self, kwargs['verify_bin_name'], default_bin_name, kwargs['msg']+": Verify the default bin name " + kwargs['verify_bin_name'])
        if "verify_bin_format_edit" in kwargs:
            default_bin_format=self.driver.find_element_by_css_selector(input_parent_css + inputs['bin_format_edit']).get_attribute("value")
            utillityobject.asequal(self, kwargs['verify_bin_format_edit'], default_bin_format, kwargs['msg']+": Verify the default bin format - "+ kwargs['verify_bin_format_edit'])
        if "verify_bin_format_btn" in kwargs:
            format_btn_obj_css="div[id^='QbDialog'] div[class*='bi-window active window'] #qbBinBtnFormat"
            utillityobject.verify_object_visible(self, format_btn_obj_css, kwargs['verify_bin_format_btn'], kwargs['msg']+": Verify the format button state - "+ str(kwargs['verify_bin_format_btn']))
        if "verify_bin_width" in kwargs:
            default_bin_width=self.driver.find_element_by_css_selector(input_parent_css + inputs['bin_width']).get_attribute("value")
            utillityobject.asequal(self, kwargs['verify_bin_width'], default_bin_width, kwargs['msg']+": Verify the bin width - "+ kwargs['verify_bin_width'])
        if "verify_bin_ok_btn" in kwargs:
            ok_btn_enabled="div[id^='QbDialog'] div[class*='bi-window active window'] [id='qbBinsOkBtn']"
            ok_btn_disabled="div[id^='QbDialog'] div[class*='bi-window active window'] [id='qbBinsOkBtn'][class*='button-disabled']"
            btn_css=ok_btn_enabled if kwargs['verify_bin_ok_btn']=='Enabled' else ok_btn_disabled
            utillityobject.verify_object_visible(self, btn_css, True, kwargs['msg']+": Verify the Ok button status - "+ str(kwargs['verify_bin_ok_btn']))
           
    def set_bin_format(self, **kwargs):
        '''
            check_box_list=['Percent (%)', 'Use Comma (C)', 'Suppress Comma (c)', 'Leading Zeros (L)', 'Suppress Zeros (S)']
        '''
        parent_css= "div[id^='QbDialog'] div[class*='bi-window active window'] #fmtDlgOk"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, parent_css, 1)
        parent_obj= self.driver.find_elements_by_css_selector("div[id^='QbDialog'] div[class*='bi-window active window']")[-1]
        if 'field_type' in kwargs:
            elems=parent_obj.find_elements_by_css_selector("#format-types-list [id^='BiListItem']")
            for elem in elems:
                if elem.text.strip()==kwargs['field_type']:
                    elem.click()
                    break
        if 'check_box_list' in kwargs:
            btns=parent_obj.find_elements_by_css_selector("[id$='RadioBtn'][class='bi-label']")
            btn_texts=[el.text.strip() for el in btns]
            for item in kwargs['check_box_list']:
                btns[btn_texts.index(item)].find_element_by_css_selector("input").click()
    
        if 'currency_symbol' in kwargs:
            elem=parent_obj.find_element_by_css_selector("#currencySymbolCBox")
            utillityobject.select_any_combobox_item(self, elem, kwargs['currency_symbol'])
    
        if 'field_length' in kwargs:
            elem=parent_obj.find_element_by_css_selector("#fieldLenSpinner input")
            utillityobject.set_text_field_using_actionchains(self, elem, kwargs['field_length'])
    
        if 'decimals' in kwargs:
            elem=parent_obj.find_element_by_css_selector("#decimalLenSpinner input")
            utillityobject.set_text_field_using_actionchains(self, elem, kwargs['decimals'])
            
        if 'ok_btn' in kwargs:
            parent_obj.find_element_by_css_selector('#fmtDlgOk').click()
        
    
    def verify_datatree_tooltip(self, field_name, position, expected_list,msg, **kwargs):
        """
        field_name=The field you wanted to take tooltip in data tree
        position= 1 if there is only one entry
        expected_list=the expected list for the tooltip
        msg=Msg to be printed
        ***kwgs like x_offset, y_offset
        """ 

        aele=self.driver.find_element_by_id("resultArea")
        Visualization_Metadata.select_data_field(self, field_name)
        row_css="#iaMetaDataBrowser div[id^='QbMetaDataTree-'] td[class='']"
        try:
            l=[el for el in self.driver.find_elements_by_css_selector(row_css) if el.text.strip()==field_name]
            l[position-1].find_element_by_css_selector("img[class='icon']").click()
        except:
            print("except")
            l=[el for el in self.driver.find_elements_by_css_selector(row_css) if el.text.strip()==field_name]
            l[position-1].find_element_by_css_selector("img[class='icon']").click()
        time.sleep(2)
            
        utillityobject.click_on_screen(self, aele, coordinate_type='middle',mouse_duration=1)
        row_css="#iaMetaDataBrowser div[id^='QbMetaDataTree-'] tr[class*='selected'] img[class='icon']"
        newelement = self.driver.find_element_by_css_selector(row_css)
        time.sleep(3)
        try:
            #action.context_click(newelement).perform()
            #action.move_to_element(newelement).perform()
            utillityobject.click_on_screen(self, newelement, coordinate_type='middle',mouse_duration=5,**kwargs)
            time.sleep(1)
        except:
            print('Exception happen during context click')
            #action.move_to_element(newelement).perform()
            utillityobject.click_on_screen(self, newelement, coordinate_type='middle',mouse_duration=5, **kwargs)
            time.sleep(1)
            
        tooltip_elems=self.driver.find_elements_by_css_selector("[id^='BiToolTip']:not([style*='hidden']) > table tr")
        actual_list=[el.text for el in tooltip_elems]
        print('Actual list in tooltip', actual_list)
        utillityobject.asequal(self, expected_list, actual_list, msg)
    
    
    def create_large_ia_group(self, btn_name, element_list,totla_list, **kwargs):
        """
        :params btn_name='Group' or 'Rename'
        :params totla_list=42 (total values of group)
        :params element_list=['Accessories', 'Televisions']    (This is value to select from create group)
        :kwargs change_field_txt='BUSINESS_GROUP'      (To change the title text)
        :kwargs close_button='ok' or 'cancel' or 'Apply'
        :kwargs cord_type='middle'
        :kwargs click_opt=0(left Click)default, 1(right click), 2(double click), 3(move)
        :Usage1: create_ia_group('Group', ['Accessories', 'Televisions'],42, close_button='ok')
        element_list=['North America and South America']
        :Usage2: create_ia_group('Rename', element_list,42, rename_field='America')
        """
        time.sleep(3)
        elem=(By.CSS_SELECTOR,"div[id^='QbDialog'][tabindex='0'] #dynaTextFld")
        Visualization_Metadata._validate_page(self, elem)
        cord_type=kwargs['cord_type'] if 'cord_type' in kwargs else 'middle'
        click_opt=kwargs['click_opt'] if 'click_opt' in kwargs else 0
        if 'change_field_txt' in kwargs:
            field_name_css="div[id^='QbDialog'][tabindex='0'] #dynaTextFld"
            utillityobject.set_text_field_using_actionchains(self, self.driver.find_element_by_css_selector(field_name_css), kwargs['change_field_txt'])
        css="div[id^='QbDialog'] [class*='active'] #dynaGrpsValuesTree[class*='tree'] table tr td[class='']"
        self.driver.find_element_by_css_selector("#dynaGrpsValuesTree div[id^='BiScrollBar'][class*='scroll-bar-vertical'] div[id^='BiRepeatButton'][class*='scroll-bar-dec-button']").click()
#         keyboard = Controller()
#         keyboard.press(Key.ctrl)
        total_page_down=0
        for value in element_list:
            loop=True
            while loop :
                total_row = self.driver.find_elements_by_css_selector(css)
                row_values = [row.text.strip() for row in total_row]
                if value in row_values :
                    element_index=row_values.index(value)
                    if element_index==(len(total_row)-1) :
#                         pyautogui.press('down')
                        utillityobject.mouse_scroll(self, 'down', totla_list, option='uiautomation')
                        total_row = self.driver.find_elements_by_css_selector(css)
                        row_values = [row.text.strip() for row in total_row]
                        element_index=row_values.index(value)
                    row_element=total_row[element_index]
                    if sys.platform == 'linux':
                        pykeyboard.press_key(pykeyboard.control_key)
                    else:
                        keyboard.press('ctrl')
                    utillityobject.click_on_screen(self, row_element, cord_type, click_opt, **kwargs)
                    if sys.platform == 'linux':
                        pykeyboard.release_key(pykeyboard.control_key)
                    else:
                        keyboard.release('ctrl')
                    loop=False
                else :
                    if total_page_down==totla_list :
                        loop=False
#                     pyautogui.press('down')
                    utillityobject.mouse_scroll(self, 'down', totla_list, option='uiautomation')
                    total_page_down+=1
#         keyboard.release(Key.ctrl)
        btns={'Group':'groupSelValuesBtn','Rename':'renameGrpBtn','Ungroup':'ungroupBtn','Ungroup All':'ungroupAllBtn','Show Other':'toggleOtherBtn'}
        btn_css="div[id^='QbDialog'] div[id=" + btns[btn_name] + "]"
        button_obj = self.driver.find_element_by_css_selector(btn_css)
        utillityobject.default_left_click(self,object_locator=button_obj, **kwargs)
        if 'rename_field' in kwargs:
            if sys.platform == 'linux':
                pykeyboard.type_string(str(kwargs['rename_field']))
                pykeyboard.tap_key(pykeyboard.enter_key)
            else:    
                keyboard.type(kwargs['rename_field'])
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
            time.sleep(10)
        if 'close_button' in kwargs:
            parent_css="div[id^='QbDialog'] [class*='active'] div[id='dynaGrpsOkBtn']:not([disabled]) img"
            visualization_resultarea.Visualization_Resultarea.wait_for_property(self,parent_css,1,45)
            Visualization_Metadata.close_ia_group_dialog(self, **kwargs)
    
    def verify_query_panel_all_field(self,expected_fields,msg):
        '''
        description : This function used to verify all query panel field values
        :Param :expected_fields=['Bar Stacked1', 'Matrix', 'Rows', 'Columns', 'Axis', 'Vertical Axis', 'Cost of Goods', 'Horizontal Axis', 'Product,Category', 'Marker', 'Color', 'Size', 'Tooltip']
        :Usage :verify_query_panel_all_field(expected_fields,'Step 02.0 : Verify query panel fields')
        '''
        querytree_items = self.driver.find_elements_by_css_selector("#queryTreeColumn table>tbody>tr")
        actual_fields=[field.text.strip() for field in querytree_items if field.text.strip()!='']
        utillityobject.asequal(self,actual_fields,expected_fields,msg)
        
    def verify_all_data_panel_fields(self,expected_fields,msg, comparison_type='asequal'):
        '''
        description : This function used to verify all data panel field values
        :Param :expected_fields=['Dimensions', 'Product,Category', 'Product,Subcategory', 'Model', 'Measures/Properties', 'Quantity,Sold']
        :Usage :verify_all_data_panel_fields(expected_fields,'Step 02.0 : Verify query panel fields')
        '''
        datatree_items = self.driver.find_elements_by_css_selector("[id^=QbMetaDataTree] table>tbody>tr")
        actual_fields=[field.text.strip() for field in datatree_items if field.text.strip()!='']
        utillityobject.verify_list_values(self, expected_fields, actual_fields, msg, assert_type=comparison_type)
    
    def verify_querytree_tooltip(self, field_name, position, expected_list,msg):
        """
        field_name=The field_name you wanted to verify tooltip in querytree
        position= 1 if there is only one entry
        expected_list=the expected list for the tooltip
        msg=Msg to be printed
        ***kwgs like x_offset, y_offset
        """ 
        row_css="#queryTreeColumn td[class='']"
        l=[el for el in self.driver.find_elements_by_css_selector(row_css) if el.text.strip()==field_name]
        field_icon=l[position-1].find_element_by_css_selector("img[class='icon']")
        utillityobject.click_on_screen(self, field_icon, 'middle')
        time.sleep(1)
        tooltip_elems=self.driver.find_elements_by_css_selector("[id^='BiToolTip']:not([style*='hidden']) > table tr")
        actual_list=[el.text for el in tooltip_elems]
        print('Actual list in tooltip', actual_list)
        utillityobject.asequal(self, expected_list, actual_list, msg)