from common.lib.base import BasePage
from selenium.common.exceptions import NoSuchElementException
from common.lib.javascript import JavaScript
from common.lib.utillity import UtillityMethods as utillityobject
from common.lib.core_utility import CoreUtillityMethods as coreutillityobject
from common.lib.global_variables import Global_variables
from common.lib import root_path
import time, os, re

class FilterMetaData(BasePage) :
    
    DATA_FIELDS_CSS="[id^='wndWhere'][id$='Popup']:not([style*='hidden']) [id^='WhereMetaDataTree'] table[class='bi-tree-view-table']>tbody>tr>td[class='']"
    DATA_FIELDS_SCROLL_ELEMENT_CSS="[id^='wndWhere'][id$='Popup']:not([style*='hidden']) #metaDataBrowser [id^='WhereMetaDataTree']>div[class='bi-tree-view-body']"
    SELECTED_DATA_FIELD_CSS="[id^='wndWhere'][id$='Popup']:not([style*='hidden']) table[class='bi-tree-view-table']>tbody>tr[class*='selected']>td>img[class*='icon']"
    SELECTED_DATATREE_ROW_CSS="[id^='wndWhere'][id$='Popup']:not([style*='hidden']) [id^='WhereMetaDataTree'] table[class='bi-tree-view-table']>tbody>tr[class*='selected']"
    
    def __init__(self, driver):
        super(FilterMetaData, self).__init__(driver)
        
           
    def click_on_filter_field(self, data_field_path, field_position=1):
        """
        This method used to expand and right click on specific data field
        data_field_path = 'Dimensions->COUNTRY->COUNTRY->COUNTRY'
        field_position = 1 , 2, 3
        Example Usage : right_click_on_data_filed('Dimensions->COUNTRY->COUNTRY->COUNTRY', field_position=3)
        """
        FilterMetaData.select_data_field(self, data_field_path, field_position=field_position)
        
    def double_click_on_filter_field(self, data_field_path, field_position=1):
        """
        This method used to expand and right click on specific data field
        data_field_path = 'Dimensions->COUNTRY->COUNTRY->COUNTRY'
        field_position = 1 , 2, 3
        Example Usage : double_click_on_filter_field('Dimensions->COUNTRY->COUNTRY->COUNTRY', field_position=3)
        """
        FilterMetaData.select_data_field(self, data_field_path, field_position=field_position)
        selected_field = self.driver.find_element_by_css_selector(FilterMetaData.SELECTED_DATA_FIELD_CSS)
        coreutillityobject.double_click(self, selected_field, xoffset=10)

    def select_data_field_context_menu(self, data_field_path, context_menu_path):
        """
        This method used to expand and right click on specific data field and select context menu
        """
        FilterMetaData.right_click_on_data_filed(self, data_field_path)
        context_menu_list=context_menu_path.split('->')
        for context_menu in context_menu_list :
            utillityobject.select_bipopup_list_item(self, context_menu)
    
    def select_data_field(self, data_field_path, field_position=1):
        """
        This method used to click on specific field row
        """
        JavaScript.scroll_element(self, FilterMetaData.DATA_FIELDS_SCROLL_ELEMENT_CSS, 0, wait_time=1)
        data_field_path_list=data_field_path.rsplit('->', 1)
        data_field_section_path=None if len(data_field_path_list) == 1 else data_field_path_list[0]
        field_name=data_field_path_list[-1]
        if data_field_section_path != None :
            FilterMetaData.expand_data_field_section(self, data_field_section_path, find_from_top=False)
        filed_object=FilterMetaData.find_data_field(self, field_name, field_position)
        filed_icon_obj=filed_object.find_element_by_css_selector("img[class*='icon']")
        coreutillityobject.left_click(self,  filed_icon_obj,  xoffset=25, action_chain_click=True, mouse_move_duration=0)
        utillityobject.synchronize_until_element_is_visible(self, FilterMetaData.SELECTED_DATATREE_ROW_CSS, expire_time=4)
        
    def collapse_data_field_section(self, data_field_section_path, find_from_top=True):
        """
        This method used to collapse the data field. data_field_section_path should be in reverse order. for example if 'Product->Product->Model' already expanded then 
        we should pass data_field_section_path as 'Model->Product->Product' to close section
        """
        FilterMetaData.__expand_or_close_data_field_section(self, data_field_section_path, 'CLOSE', find_from_top)

    def expand_data_field_section(self, data_field_section_path, find_from_top=True):
        """
        This method used to expand the data field
        """
        FilterMetaData.__expand_or_close_data_field_section(self, data_field_section_path, 'EXPAND', find_from_top)

    def find_data_field(self, field_name, field_position):
        """
        Pass
        """
        utillityobject.scroll_down_and_find_item_using_mouse(self, FilterMetaData.DATA_FIELDS_CSS, field_name)
        data_fields_object=self.driver.find_elements_by_css_selector(FilterMetaData.DATA_FIELDS_CSS)
        foud_data_fields_obj=JavaScript.find_elements_by_text(self, data_fields_object, field_name)
        if len(foud_data_fields_obj) == 0 :
            msg="[{0}] data field not found in data tree".format(field_name)
            raise NoSuchElementException(msg)
        else :
            return foud_data_fields_obj[field_position-1]
    
    def scroll_data_field_table(self, field_name):
        """
        This method used to scroll the data field container table. I will search given element and scroll up to bottom of the data field table 
        """
        scroll_offset=0
        while True :
            data_fields_object=self.driver.find_elements_by_css_selector(FilterMetaData.DATA_FIELDS_CSS)
            data_field_name_list=JavaScript.get_elements_text(self, data_fields_object)
            scroll_completed=JavaScript.check_scroll_is_completed(self, FilterMetaData.DATA_FIELDS_SCROLL_ELEMENT_CSS)
            if field_name not in data_field_name_list and scroll_completed == False :
                last_data_field_obj=data_fields_object[-1]
                scroll_offset+=JavaScript.get_element_property_value(self, last_data_field_obj, 'offsetTop')
                JavaScript.scroll_element(self, FilterMetaData.DATA_FIELDS_SCROLL_ELEMENT_CSS, scroll_offset)
            else :
                field_obj=data_fields_object[data_field_name_list.index(field_name)]
                scroll_offset+=JavaScript.get_element_property_value(self, field_obj, 'offsetTop')
                JavaScript.scroll_element(self, FilterMetaData.DATA_FIELDS_SCROLL_ELEMENT_CSS, scroll_offset)
                time.sleep(2)
                break
            time.sleep(1)    
    
    def __expand_or_close_data_field_section(self, data_field_section_path, target, find_from_top=True):
        """
        This method used to expand or close the data field section.  
        """
        if find_from_top == True :
            JavaScript.scroll_element(self, FilterMetaData.DATA_FIELDS_SCROLL_ELEMENT_CSS, 0, wait_time=1)
        if target.upper() == 'EXPAND' :
            icon_css="img[src*='plus']"
        if target.upper() == 'CLOSE' :
            icon_css="img[src*='minus']"
        previous_section=None
        field_section_list=data_field_section_path.split('->')
        filter_scroll_obj=self.driver.find_element_by_css_selector(FilterMetaData.DATA_FIELDS_SCROLL_ELEMENT_CSS)
        coreutillityobject.python_move_to_element(self, filter_scroll_obj)
        for section in field_section_list :
            current_section=section
            field_position=2 if previous_section==current_section else 1
            section_obj=FilterMetaData.find_data_field(self, section, field_position)
            icon_obj=section_obj.find_elements_by_css_selector(icon_css)
            if len(icon_obj) > 0 : #check whether field section is already closed or expanded. section is closed or expanded if icon_obj length is 0
#                 if self.browser.lower() == 'ie': # For IE browser expand arrow icon actionchains clicking on offset 0,0, hence using webelement click 
                if Global_variables.browser_name in ['ie', 'edge']:
                    coreutillityobject.left_click(self,  icon_obj[0])
                else:
                    coreutillityobject.left_click(self,  icon_obj[0], action_chain_click=True, mouse_move_duration=0)
            previous_section=section
    
    def get_masterfile_field_path(self, master_file, filed_key):
        """
        This method used to get data file path from master_file.data
        """
        MASTER_FILE_NAME='master_file.data'
        MASTER_FILE_PATH=os.path.join(root_path.ROOT_PATH, MASTER_FILE_NAME)
        field_path=utillityobject.read_configparser_key_value(self, MASTER_FILE_PATH, master_file, filed_key)
        return field_path
    
    def select_data_field_using_master_file_data(self, data_file_name, field_position=1):
        """
        This method used to select data file using maste_file.data
        """
        if bool(re.match('.*->.*', data_file_name)):
            field_path = data_file_name
        else:
            master_file_name=self.driver.find_element_by_css_selector("#iaMetaDataBox [id^='BiGroupBoxTitle']").text.lower().strip().split(' ')[-1]
            filed_key=master_file_name + '_' + data_file_name
            field_path=FilterMetaData.get_masterfile_field_path(self, master_file_name, filed_key)
        FilterMetaData.select_data_field(self, field_path, field_position)