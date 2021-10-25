from common.lib.base import BasePage
from selenium.common.exceptions import NoSuchElementException
from common.lib.javascript import JavaScript
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from common.lib.utillity import UtillityMethods as utillityobject
from common.lib.core_utility import CoreUtillityMethods as coreutillityobject
from common.lib.global_variables import Global_variables
from common.lib import root_path
import time, os, re, keyboard

class CoreMetaData(BasePage) :
    
    DATA_FIELDS_CSS="#iaMetaDataBrowser [id^='QbMetaDataTree'] table[class='bi-tree-view-table']>tbody>tr>td[class='']"
    DATA_FIELDS_SCROLL_ELEMENT_CSS="#iaMetaDataBrowser [id^='QbMetaDataTree']>div[class='bi-tree-view-body']"
    SELECTED_DATA_FIELD_CSS="#iaMetaDataBrowser [id^='QbMetaDataTree'] table[class='bi-tree-view-table']>tbody>tr[class*='selected']>td>img[class*='icon']"
    SELECTED_DATATREE_ROW_CSS="#iaMetaDataBrowser [id^='QbMetaDataTree'] table[class='bi-tree-view-table']>tbody>tr[class*='selected']"
    
    def __init__(self, driver):
        super(CoreMetaData, self).__init__(driver)
        
    def double_click_on_data_filed(self, data_file_name, field_position=1):
        """
        This method used to expand and double click on specific data field
        data_field_path = 'Dimensions->COUNTRY->COUNTRY->COUNTRY'
        field_position = 1 , 2, 3
        Example Usage : double_click_on_data_filed('Dimensions->COUNTRY->COUNTRY->COUNTRY', field_position=3)
        """
        CoreMetaData.select_data_field_using_master_file_data(self, data_file_name, field_position)
        field_object=self.driver.find_element_by_css_selector(CoreMetaData.SELECTED_DATA_FIELD_CSS)
        coreutillityobject.double_click(self, field_object, xoffset=30, mouse_move_duration=0)
        time.sleep(1)
        
    def right_click_on_data_filed(self, data_file_name, field_position=1):
        """
        This method used to expand and right click on specific data field
        data_field_path = 'Dimensions->COUNTRY->COUNTRY->COUNTRY'
        field_position = 1 , 2, 3
        Example Usage : right_click_on_data_filed('Dimensions->COUNTRY->COUNTRY->COUNTRY', field_position=3)
        """
        CoreMetaData.select_data_field_using_master_file_data(self, data_file_name, field_position)
        field_object=self.driver.find_element_by_css_selector(CoreMetaData.SELECTED_DATA_FIELD_CSS)
        coreutillityobject.right_click(self, field_object, xoffset=30 , mouse_move_duration=0)
        utillityobject.synchronize_with_number_of_element(self, "div[id^='BiPopup'][style*='inherit']", 1, expire_time=4)
    
    def select_data_field_context_menu(self, data_field_path, context_menu_path, field_position=1):
        """
        This method used to expand and right click on specific data field and select context menu
        :usage : select_data_field_context_menu("CAR", "Sort")
        """
        CoreMetaData.right_click_on_data_filed(self, data_field_path, field_position)
        context_menu_list=context_menu_path.split('->')
        for context_menu in context_menu_list :
            utillityobject.select_bipopup_list_item(self, context_menu)
    
    def select_data_field(self, data_field_path, field_position=1, ctrl=False):
        """
        This method used to click on specific field row
        """
        data_pane_tooltip_css=".bi-tool-tip[style*='inherit']:not([style*='display'])"
        JavaScript.scroll_element(self, CoreMetaData.DATA_FIELDS_SCROLL_ELEMENT_CSS, 0, wait_time=1)
        data_field_path_list=data_field_path.rsplit('->', 1)
        data_field_section_path=None if len(data_field_path_list) == 1 else data_field_path_list[0]
        field_name=data_field_path_list[-1]
        if data_field_section_path != None :
            CoreMetaData.expand_data_field_section(self, data_field_section_path, find_from_top=False)
        filed_object=CoreMetaData.find_data_field(self, field_name, field_position)
        filed_icon_obj=filed_object.find_element_by_css_selector("img[class*='icon']")
        if ctrl :
            if Global_variables.browser_name != 'chrome' :
                keyboard.press('ctrl')
            else :
                ActionChains(self.driver).key_down(Keys.CONTROL).perform()
        utillityobject.synchronize_until_element_disappear(self, data_pane_tooltip_css, 20)
        coreutillityobject.left_click(self, filed_icon_obj,  xoffset=25, action_chain_click=True, mouse_move_duration=0)
        utillityobject.synchronize_until_element_is_visible(self, CoreMetaData.SELECTED_DATATREE_ROW_CSS, expire_time=4)
        if ctrl :
            if Global_variables.browser_name != 'chrome' :
                keyboard.release('ctrl')
            else :
                ActionChains(self.driver).key_up(Keys.CONTROL).perform()
                
    def collapse_data_field_section(self, data_field_section_path, find_from_top=True):
        """
        This method used to collapse the data field. data_field_section_path should be in reverse order. for example if 'Product->Product->Model' already expanded then 
        we should pass data_field_section_path as 'Model->Product->Product' to close section
        """
        CoreMetaData.__expand_or_close_data_field_section(self, data_field_section_path, 'CLOSE', find_from_top)

    def expand_data_field_section(self, data_field_section_path, find_from_top=True):
        """
        This method used to expand the data field
        """
        CoreMetaData.__expand_or_close_data_field_section(self, data_field_section_path, 'EXPAND', find_from_top)

    def find_data_field(self, field_name, field_position):
        """
        Pass
        """
        CoreMetaData.scroll_data_field_table(self, field_name)
        data_fields_object=self.driver.find_elements_by_css_selector(CoreMetaData.DATA_FIELDS_CSS)
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
            data_fields_object=self.driver.find_elements_by_css_selector(CoreMetaData.DATA_FIELDS_CSS)
            data_field_name_list=JavaScript.get_elements_text(self, data_fields_object)
            scroll_completed=JavaScript.check_scroll_is_completed(self, CoreMetaData.DATA_FIELDS_SCROLL_ELEMENT_CSS)
            if field_name not in data_field_name_list and scroll_completed == False :
                last_data_field_obj=data_fields_object[-1]
                scroll_offset+=JavaScript.get_element_property_value(self, last_data_field_obj, 'offsetTop')
                JavaScript.scroll_element(self, CoreMetaData.DATA_FIELDS_SCROLL_ELEMENT_CSS, scroll_offset)
            else :
                field_obj=data_fields_object[data_field_name_list.index(field_name)]
                scroll_offset+=JavaScript.get_element_property_value(self, field_obj, 'offsetTop')
                #JavaScript.scroll_element(self, CoreMetaData.DATA_FIELDS_SCROLL_ELEMENT_CSS, scroll_offset)
                time.sleep(2)
                break
            time.sleep(1)    
    
    def __expand_or_close_data_field_section(self, data_field_section_path, target, find_from_top=True):
        """
        This method used to expand or close the data field section.  
        """
        data_pane_tooltip_css=".bi-tool-tip[style*='inherit']:not([style*='display'])"
        if find_from_top == True :
            JavaScript.scroll_element(self, CoreMetaData.DATA_FIELDS_SCROLL_ELEMENT_CSS, 0, wait_time=1)
        if target.upper() == 'EXPAND' :
            icon_css="img[src*='closed']"
        if target.upper() == 'CLOSE' :
            icon_css="img[src*='open']"
        previous_section=None
        field_section_list=data_field_section_path.split('->')
        for section in field_section_list :
            current_section=section
            field_position=2 if previous_section==current_section else 1
            section_obj=CoreMetaData.find_data_field(self, section, field_position)
            icon_obj=section_obj.find_elements_by_css_selector(icon_css)
            if len(icon_obj) > 0 : #check whether field section is already closed or expanded. section is closed or expanded if icon_obj length is 0
                utillityobject.synchronize_until_element_disappear(self, data_pane_tooltip_css, 20)
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
    
    def select_data_field_using_master_file_data(self, data_file_name, field_position=1, ctr=False):
        """
        This method used to select data file using maste_file.data
        """
        if bool(re.match('.*->.*', data_file_name)):
            field_path = data_file_name
        else:
            master_file_name=self.driver.find_element_by_css_selector("#iaMetaDataBox [id^='BiGroupBoxTitle']").text.lower().strip().split(' ')[-1]
            filed_key=master_file_name + '_' + data_file_name
            field_path=CoreMetaData.get_masterfile_field_path(self, master_file_name, filed_key)
        CoreMetaData.select_data_field(self, field_path, field_position, ctr)
    
    def drag_multiple_data_fields_to_query_tree(self, field_name_list, query_bucket_name, field_position_list=[], query_bucket_position=1, query_bucket_loc='bottom_middle', query_bucket_x=0, query_bucket_y=-1):
        """
        Description : Drag multiple data fields to query tree.
        Usage : drag_multiple_data_fields_to_query_tree(['Gross Profit', 'Revenue', 'Quantity,Sold'], 'Tooltip')
        """
        CoreMetaData.select_multiple_data_fields(self, field_name_list, field_position_list)
        selected_data_field = utillityobject.validate_and_get_webdriver_objects(self, CoreMetaData.SELECTED_DATATREE_ROW_CSS, "Selected data field")[-1]
        selected_data_loc = coreutillityobject.get_web_element_coordinate(self, selected_data_field, 'middle_left', xoffset=55)
        query_bucket_obj = CoreMetaData._get_query_bucket_object(self, query_bucket_name, query_bucket_position)
        query_bucket_loc = coreutillityobject.get_web_element_coordinate(self, query_bucket_obj, query_bucket_loc, query_bucket_x, query_bucket_y)
        x1, y1 = selected_data_loc['x'], selected_data_loc['y']
        x2, y2 = query_bucket_loc['x'], query_bucket_loc['y']
        if Global_variables.browser_name != 'chrome' :
            keyboard.press('ctrl')
            coreutillityobject.python_left_click(self, selected_data_field, 'middle_left', xoffset=55)
        coreutillityobject.drag_and_drop(self, x1, y1, x2, y2)
        (Global_variables.browser_name != 'chrome')  and keyboard.release('ctrl')
    
    def select_multiple_data_fields(self, field_name_list, field_position_list=[]):
        """
        Description : Select the multiple data fields using Ctrl
        :arg - field_name_list - List of data fields name to multiple select.
        :arg - field_position_list - List of field position. exp [1, 2, 1]
        """
        field_positions = [1 for _ in range(len(field_name_list))] if field_position_list == [] else field_position_list
        loop = 0
        for field, position in zip(field_name_list, field_positions) :
            ctr = True if loop !=0 else False
            CoreMetaData.select_data_field_using_master_file_data(self, field, position, ctr)
            loop += 1
            
    def _get_query_bucket_object(self, query_bucket_name, position=1):
        """
        Description : This method will return the query tree bucket object.
        """
        xpath = "//div[@id='queryTreeColumn']//table[@class='bi-tree-view-table']//td[normalize-space()='{0}']/img[2]".format(query_bucket_name)
        buckets_object = self.driver.find_elements_by_xpath(xpath)
        if buckets_object != [] :
            if len(buckets_object) < int(position) :
                msg = "'{0}' not exists in '{1}' position in query tree".format(query_bucket_name)
                raise IndexError(msg)
            else :
                return buckets_object[position-1]
        else :
            msg = "'{0}' not exists in query tree".format(query_bucket_name)
            raise KeyError(msg)
    
    def verify_grayedout_fields_in_query_pane(self, expected_fields_list, step_num, comparison_type='asequal'):
        """
        Description : Verify grayed out fields in query pane
        """
        grayout_filed_css = "#queryTreeColumn .bi-tree-view-table>tbody>tr[style*='gray']"
        grayout_fileds_object = self.driver.find_elements_by_css_selector(grayout_filed_css)
        actual_fields_list = [field.text.strip() for field in grayout_fileds_object]
        msg = "Step {0} : Verify {0} field grayed out".format(step_num, expected_fields_list)
        utillityobject.verify_list_values(self, expected_fields_list, actual_fields_list, msg, comparison_type)
    
    def verify_descending_fields_in_query_pane(self, expected_fields_list, step_num, comparison_type='asequal'):
        """
        Description : Verify descending fields in query pane
        """
        descending_icon_css = "img[src*='column_sort_decending_16']"
        filed_css = "#queryTreeColumn .bi-tree-view-table>tbody>tr"
        fileds_object = self.driver.find_elements_by_css_selector(filed_css)
        actual_fields_list = [field.text.strip() for field in fileds_object if len(field.find_elements_by_css_selector(descending_icon_css)) == 1]
        msg = "Step {0} : Verify {0} fields are in descending order".format(step_num, expected_fields_list)
        utillityobject.verify_list_values(self, expected_fields_list, actual_fields_list, msg, comparison_type)
    
    def drag_query_filed_to_another_query_field(self, source_field, target_field, source_field_position=1, target_field_position=1, source_field_loc='middle', target_field_loc='bottom_middle'):
        """
        Description : Drag the query field to another query filed.
        :Usage - drag_query_filed_to_another_query_field("SALES", "DEALER_COST", target_field_loc='top_middle')
        """
        source_field_obj = CoreMetaData._get_query_bucket_object(self, source_field, source_field_position)
        target_field_obj = CoreMetaData._get_query_bucket_object(self, target_field, target_field_position)
        source_field_loc = coreutillityobject.get_web_element_coordinate(self, source_field_obj, source_field_loc)
        target_field_loc = coreutillityobject.get_web_element_coordinate(self, target_field_obj, target_field_loc)
        coreutillityobject.drag_and_drop(self, source_field_loc['x'], source_field_loc['y'], target_field_loc['x'], target_field_loc['y'])