from common.lib.utillity import UtillityMethods as utillityobject
from common.lib.core_utility import CoreUtillityMethods as coreutillityobject
from common.pages.core_metadata import CoreMetaData as coremetadataobj
from common.lib.base import BasePage as local_basepage
from selenium.webdriver.support.color import Color
import time

class IA_Metadata(local_basepage):
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(IA_Metadata, self).__init__(driver)
    
    def search_metadata_field(self, field_name, field_position):
        """
        :Description: This function is used to search the metadata field by typing on the search box and then left click on the field 
        under tree.
        """
        element = self.driver.find_element_by_id("iaMetaDataBrowser").find_element_by_id("metaDataSearchTxtFld")
        utillityobject.set_text_field_using_actionchains(self, element, field_name, keyboard_type=True)
        row_css="#iaMetaDataBrowser div[id^='QbMetaDataTree-'] td[class='']"
        try:
            l=[el for el in self.driver.find_elements_by_css_selector(row_css) if el.text.strip().replace(' ','')==field_name.replace(' ','')]
            l[field_position-1].find_element_by_css_selector("img[class='icon']").click()
        except:
            print("except")
            l=[el for el in self.driver.find_elements_by_css_selector(row_css) if el.text.strip().replace(' ','')==field_name.replace(' ','')]
            l[field_position-1].find_element_by_css_selector("img[class='icon']").click()
        time.sleep(2)
        
    def select_datatree_field(self, data_file_name, click_type, field_position, context_menu_path=None):
        '''
        :Description: This function is used to select field in data tree. We can do left/right/double click on the field.
        We can select the context menu by right clicking.
        :Param: click_type= 'left' OR 'right' OR 'double'
        '''
        coremetadataobj.select_data_field_using_master_file_data(self, data_file_name, field_position)
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
            time.sleep(6)
        time.sleep(1)
    
    def verify_datatree_context_menu(self,field_name, field_position, context_menu_list, msg):
        '''
        :Description: This function is used to verify the right click context menu of a data tree field item
        '''
        IA_Metadata.select_datatree_field(self, field_name, 'right', field_position)
        utillityobject.verify_bipopup_list_item(self, context_menu_list, msg)

    def select_querytree_field(self, field_name, click_type, field_position, context_menu_path=None):
        '''
        :Description: This function is used to select field in data tree. We can do left/right/double click on the field.
        We can select the context menu by right clicking.
        :Param: click_type= 'left' OR 'right'
        '''
        row_css="#queryTreeColumn td[class='']"
        try:
            l=[el for el in self.driver.find_elements_by_css_selector(row_css) if el.text.strip()==field_name]
            l[field_position-1].find_element_by_css_selector("img[class='icon']").click()
        except:
            print("except")
            l=[el for el in self.driver.find_elements_by_css_selector(row_css) if el.text.strip()==field_name]
            l[field_position-1].find_element_by_css_selector("img[class='icon']").click()
        time.sleep(2)
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
    
    def verify_querytree_context_menu(self,field_name, field_position, context_menu_list, msg, verify_type='all'):
        '''
        :Description: This function is used to verify the right click context menu of a data tree field item
        '''
        IA_Metadata.select_querytree_field(self, field_name, 'right', field_position)
        utillityobject.verify_bipopup_list_item(self, context_menu_list, msg, verify_type=verify_type)
            
    def drag_and_drop_from_data_tree_to_query_tree(self, field_name, field_position, bucket_type, bucket_position, bucket_loc='bottom_middle'):
        '''
        :Description: This function is used to drag and drop data field to the specified bucket in query tree.
        :param - field_position: 1,2 .. (first match is 1)
        :param - bucket_position: 1,2 .. (first match is 1)
        '''       
        coremetadataobj.select_data_field_using_master_file_data(self, field_name, field_position)
        row_css="#iaMetaDataBrowser div[id^='QbMetaDataTree-'] tr[class*='selected'] > td"
        source_elem = self.driver.find_element_by_css_selector(row_css)
        source_elem_coordinate=coreutillityobject.get_web_element_coordinate(self, source_elem, element_location='middle_left', xoffset=55)
        x1=source_elem_coordinate['x']
        y1=source_elem_coordinate['y']
        querytree_items = self.driver.find_elements_by_css_selector("#queryTreeColumn table>tbody>tr>td")
        querytree_list=[i.text.strip() for i in querytree_items]
        target_elem=querytree_items[querytree_list.index(bucket_type)+bucket_position-1].find_element_by_css_selector("img[class='icon']")
        target_elem_coordinate=coreutillityobject.get_web_element_coordinate(self, target_elem, element_location=bucket_loc, yoffset=-1)
        x2=target_elem_coordinate['x']
        y2=target_elem_coordinate['y']
        coreutillityobject.drag_and_drop(self, x1, y1, x2, y2)
        time.sleep(2)
    
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
        target_elem_coordinate=coreutillityobject.get_web_element_coordinate(self, target_elem, element_location='middle', xoffset=25, yoffset=1)
        x2=target_elem_coordinate['x']
        y2=target_elem_coordinate['y']
        coreutillityobject.drag_and_drop(self, x1, y1, x2, y2)
        time.sleep(5)
        
    def drag_and_drop_from_data_tree_to_filter(self, field_name, field_position):
        '''
        :Description: This function is used to drag and drop data field within query tree.
        '''       
        IA_Metadata.search_metadata_field(self, field_name, field_position)
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
    
    def verify_field_in_data_pane(self,field_type, field_name, position, msg='Step X'):
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
            actual_list.extend([i.text for i in filtertree_items])
            actual_name = actual_list[position-1]
            custom_msg = msg + ": verify the " + field_name + " listed under in Filter pane"
            utillityobject.asequal(self, field_name, actual_name, custom_msg)