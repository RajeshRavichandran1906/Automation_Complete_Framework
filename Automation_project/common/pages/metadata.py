from common.lib.base import BasePage
from selenium.common.exceptions import NoSuchElementException
from common.lib.javascript import JavaScript
from common.lib.utillity import UtillityMethods as utillityobject
from common.lib import root_path
import time, os

class MetaData(BasePage) :
    
    DATA_FIELDS_CSS="#iaMetaDataBrowser [id^='QbMetaDataTree'] table[class='bi-tree-view-table']>tbody>tr>td[class='']"
    DATA_FIELDS_SCROLL_ELEMENT_CSS="#iaMetaDataBrowser [id^='QbMetaDataTree']>div[class='bi-tree-view-body']"
    SELECTED_DATA_FIELD_CSS="#iaMetaDataBrowser [id^='QbMetaDataTree'] table[class='bi-tree-view-table']>tbody>tr[class*='selected']>td>img[class*='icon']"
    SELECTED_DATATREE_ROW_CSS="#iaMetaDataBrowser [id^='QbMetaDataTree'] table[class='bi-tree-view-table']>tbody>tr[class*='selected']"
    
    def __init__(self, driver):
        super(MetaData, self).__init__(driver)
        
    def double_click_on_data_filed(self, data_field_path, field_position=1):
        """
        This method used to expand and double click on specific data field
        data_field_path = 'Dimensions->COUNTRY->COUNTRY->COUNTRY'
        field_position = 1 , 2, 3
        Example Usage : double_click_on_data_filed('Dimensions->COUNTRY->COUNTRY->COUNTRY', field_position=3)
        """
        MetaData.select_data_field(self, data_field_path, field_position=field_position)
        field_object=self.driver.find_element_by_css_selector(MetaData.SELECTED_DATA_FIELD_CSS)
        utillityobject.double_click_with_offset(self, field_object, x_offset=30, mouse_duration=0)
        time.sleep(1)
        
    def right_click_on_data_filed(self, data_field_path, field_position=1):
        """
        This method used to expand and right click on specific data field
        data_field_path = 'Dimensions->COUNTRY->COUNTRY->COUNTRY'
        field_position = 1 , 2, 3
        Example Usage : right_click_on_data_filed('Dimensions->COUNTRY->COUNTRY->COUNTRY', field_position=3)
        """
        MetaData.select_data_field(self, data_field_path, field_position=field_position)
        field_object=self.driver.find_element_by_css_selector(MetaData.SELECTED_DATA_FIELD_CSS)
        utillityobject.right_click_with_offset(self, field_object, x_offset=30, mouse_duration=0)
        utillityobject.synchronize_with_number_of_element(self, "div[id^='BiPopup'][style*='inherit']", 1, expire_time=4)
    
    def select_data_field_context_menu(self, data_field_path, context_menu_path):
        """
        This method used to expand and right click on specific data field and select context menu
        """
        MetaData.right_click_on_data_filed(self, data_field_path)
        context_menu_list=context_menu_path.split('->')
        for context_menu in context_menu_list :
            utillityobject.select_bipopup_list_item(self, context_menu)
    
    def drag_and_drop_data_field_to_filter(self, data_field_path, field_position=1, **kwargs):
        '''
        This method is used to drag and drop data field to filter
        '''   
        source_cord=kwargs['source_cord'] if 'source_cord' in kwargs else 'left'
        target_cord=kwargs['target_cord'] if 'target_cord' in kwargs else 'middle'
        source_xoff_set=kwargs['source_Xoffset'] if 'source_Xoffset' in kwargs else 55
        target_xoff_set=kwargs['target_Xoffset'] if 'target_Xoffset' in kwargs else 55
        MetaData.select_data_field(self, data_field_path, field_position=field_position)
        source_elem=self.driver.find_element_by_css_selector(MetaData.SELECTED_DATA_FIELD_CSS)
        target_elem=self.driver.find_element_by_css_selector("#qbFilterBox")
        utillityobject.drag_drop_using_uisoup(self, source_elem, target_elem, src_cord_type=source_cord, trg_cord_type=target_cord, sx_offset=source_xoff_set, tx_offset=target_xoff_set, ty_offset=-1, **kwargs)
    
    def select_data_field(self, data_field_path, field_position=1):
        """
        This method used to click on specific field row
        """
        JavaScript.scroll_element(self, MetaData.DATA_FIELDS_SCROLL_ELEMENT_CSS, 0, wait_time=1)
        data_field_path_list=data_field_path.rsplit('->', 1)
        data_field_section_path=None if len(data_field_path_list) == 1 else data_field_path_list[0]
        field_name=data_field_path_list[-1]
        if data_field_section_path != None :
            MetaData.expand_data_field_section(self, data_field_section_path, find_from_top=False)
        filed_object=MetaData.find_data_field(self, field_name, field_position)
        filed_icon_obj=filed_object.find_element_by_css_selector("img[class*='icon']")
        utillityobject.left_click_with_offset(self, filed_icon_obj, x_offset=25, mouse_duration=0)
        utillityobject.synchronize_with_number_of_element(self, MetaData.SELECTED_DATATREE_ROW_CSS, 1, expire_time=4)
        
    def collapse_data_field_section(self, data_field_section_path, find_from_top=True):
        """
        This method used to collapse the data field. data_field_section_path should be in reverse order. for example if 'Product->Product->Model' already expanded then 
        we should pass data_field_section_path as 'Model->Product->Product' to close section
        """
        MetaData.__expand_or_close_data_field_section(self, data_field_section_path, 'CLOSE', find_from_top)

    def expand_data_field_section(self, data_field_section_path, find_from_top=True):
        """
        This method used to expand the data field
        """
        MetaData.__expand_or_close_data_field_section(self, data_field_section_path, 'EXPAND', find_from_top)

    def find_data_field(self, field_name, field_position):
        """
        Pass
        """
        MetaData.scroll_data_field_table(self, field_name)
        data_fields_object=self.driver.find_elements_by_css_selector(MetaData.DATA_FIELDS_CSS)
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
            data_fields_object=self.driver.find_elements_by_css_selector(MetaData.DATA_FIELDS_CSS)
            data_field_name_list=JavaScript.get_elements_text(self, data_fields_object)
            scroll_completed=JavaScript.check_scroll_is_completed(self, MetaData.DATA_FIELDS_SCROLL_ELEMENT_CSS)
            if field_name not in data_field_name_list and scroll_completed == False :
                last_data_field_obj=data_fields_object[-1]
                scroll_offset+=JavaScript.get_element_property_value(self, last_data_field_obj, 'offsetTop')
                JavaScript.scroll_element(self, MetaData.DATA_FIELDS_SCROLL_ELEMENT_CSS, scroll_offset)
            else :
                time.sleep(1)
                break    
    
    def __expand_or_close_data_field_section(self, data_field_section_path, target, find_from_top=True):
        """
        This method used to expand or close the data field section.  
        """
        data_pane_tooltip_css=".bi-tool-tip[style*='inherit']:not([style*='display'])"
        if find_from_top == True :
            JavaScript.scroll_element(self, MetaData.DATA_FIELDS_SCROLL_ELEMENT_CSS, 0, wait_time=1)
        if target.upper() == 'EXPAND' :
            icon_css="img[src*='closed']"
        if target.upper() == 'CLOSE' :
            icon_css="img[src*='open']"
        previous_section=None
        field_section_list=data_field_section_path.split('->')
        for section in field_section_list :
            current_section=section
            field_position=2 if previous_section==current_section else 1
            section_obj=MetaData.find_data_field(self, section, field_position)
            icon_obj=section_obj.find_elements_by_css_selector(icon_css)
            if len(icon_obj) > 0 : #check whether field section is already closed or expanded. section is closed or expanded if icon_obj length is 0
                utillityobject.synchronize_until_element_disappear(self, data_pane_tooltip_css, 20)
                utillityobject.left_click_with_offset(self, icon_obj[0], mouse_duration=0)
            previous_section=section
    
    def get_masterfile_field_path(self, master_file, filed_key):
        """
        This method used to 
        """
        MASTER_FILE_NAME='master_file.data'
        MASTER_FILE_PATH=os.path.join(root_path.ROOT_PATH, MASTER_FILE_NAME)
        field_path=utillityobject.read_configparser_key_value(self, MASTER_FILE_PATH, master_file, filed_key)
        return field_path