from common.lib import utillity
from common.lib.base import BasePage
from selenium.common.exceptions import NoSuchElementException
from common.locators.wf_reporting_object_locators import WfReportingObjectLocators
from selenium.webdriver.support import expected_conditions as EC
from common.lib.javascript import JavaScript
import time, re

class Wf_Reporting_Object(BasePage):
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(Wf_Reporting_Object, self).__init__(driver)
    
    def _validate_page(self, locator):
        self.longwait.until(EC.visibility_of_element_located(locator))
        
    def select_ro_tree_item(self, ro_tool_name, click_type = 0, *args,**kwargs):
        """
        :param self:
        :param field_name:'Sale, Year' 
        :param position:1,2...  
        :param click_type: 0 -> left click, 1 -> right click, 2 -> double click.
        :param args: after right click --> selection menu option.
        """
        ro_tool_elems=self.driver.find_elements_by_css_selector("#roTree table span")
        ro_tool_values=[el.text.strip() for el in ro_tool_elems]
        required_ro_tool_elem=ro_tool_elems[ro_tool_values.index(ro_tool_name)]
        if 'verify' in kwargs :
            utillity.UtillityMethods.asequal(self,kwargs['verify'],kwargs['msg'])
        utillity.UtillityMethods.click_on_screen(self, required_ro_tool_elem, coordinate_type='middle',click_type=click_type)
        time.sleep(2)
        if len(args)>0:
            for arg in args:
                utillity.UtillityMethods.select_or_verify_bipop_menu(self, arg)
                
    def select_run_option(self, run_option_input_value='table', submit_type='Submit'):
        '''
        :Param -> run_option_input_value='table' OR 'graph' OR 'Submit' OR 'Reset'
        :Usage1 -> wfreportobj.select_run_option(run_option_input_value='graph', submit_type='Submit')
        '''
        value_elem=self.driver.find_element_by_css_selector("html table > tbody > tr input[value='"+run_option_input_value+"']")
        value_elem.click()
        time.sleep(2)
        type_elem=self.driver.find_element_by_css_selector("html table > tbody > tr input[type='"+submit_type+"']")
        type_elem.click()
        time.sleep(5)
        
    def select_ro_tool_menu_item(self, item_name, **kwargs):
        """
        param: item_name: 'menu_save_as' OR 'menu_run' - these need to be get it from Wf_Reporting_Object_Locators.
        """
        ro_btn=self.driver.find_element(*WfReportingObjectLocators.Appbtn)
        utillity.UtillityMethods.click_on_screen(self, ro_btn, coordinate_type='middle',click_type=0)
        time.sleep(2)
        elem1=WfReportingObjectLocators.__dict__[item_name]
        self._validate_page(elem1)
        ro_tool_menu=self.driver.find_element(*WfReportingObjectLocators.__dict__[item_name])
        utillity.UtillityMethods.click_on_screen(self, ro_tool_menu, coordinate_type='middle',click_type=0)
        time.sleep(8)
   
    def select_top_toolbar_item(self, item_name, **kwargs):
        """
        param: item_name: 'toptoolbar_new' OR 'toptoolbar_run' - these need to be get it from Wf_Reporting_Object_Locators.
        This function is specific to click on toolbar buttons - new, run, undo, redo, run
        """
    
        top_toolbar_obj=self.driver.find_element(*WfReportingObjectLocators.__dict__[item_name])
        utillity.UtillityMethods.click_on_screen(self, top_toolbar_obj, coordinate_type='middle',click_type=0)
        time.sleep(8)

    def verify_ro_tree_item(self, ro_tool_name, msg):
        """
        :param - ro_tool_name -> Must be a list
        :ro_tool_name=['Reporting Object', 'Preprocessing Other', 'Joins', 'Defines', 'Filters', 'Where Statements', 'Report', 'Chart', 'Postprocessing Other']
        :Usage- wfreportobj.verify_ro_tree_item(ro_tool_name,"Step 28: Verify successful restore")
        """
        ro_tool_elems=self.driver.find_elements_by_css_selector("#roTree table span")
        ro_tool_values=[el.text.strip() for el in ro_tool_elems]
        utillity.UtillityMethods.as_List_equal(self, ro_tool_name, ro_tool_values, msg)

    def ro_where_filter_field_click(self, field_name, position, **kwargs):
        """
        :Usage: datatree_field_click('CURR_SAL', position=1)
        :param: option: position=1 : 1st selection, position=2 is 2nd Selection
        """
        master_file_css="#wndWhereFieldPopup [id^='BiTabButton']>div[class='bi-button-label']"
        if bool(re.match('.*->.*', field_name)):
            field_path = field_name
        else :
            master_file_list=self.driver.find_element_by_css_selector(master_file_css).text.strip().split('/')
            master_file_name=master_file_list[0] if len(master_file_list)==1 else master_file_list[1]
            field_path_key=master_file_name + '_' + field_name
            field_path=utillity.UtillityMethods.get_masterfile_field_path(self, master_file_name, field_path_key)
        Wf_Reporting_Object.select_data_field(self, field_path, position)
        selected_row_css="#metaDataBrowser div[id*='MetaDataTree-'] tr[class*='selected'] img[class*='icon']"
        newelement = self.driver.find_element_by_css_selector(selected_row_css)
        utillity.UtillityMethods.double_click_with_offset(self, newelement, x_offset=40)
        time.sleep(5)
        
    def ro_create_filter_group(self, input_textvalue, msg):
        """
        @Param : input_textvalue ->'Product' or 'Product, Category'
        @Usage : ro_create_filter_group('Product', "Step X: Verify the given input value is valid")
        """
        input_css=self.driver.find_element_by_css_selector("#promptDlg #inputBox input")
        utillity.UtillityMethods.set_text_field_using_actionchains(self, input_css, input_textvalue)
        expected_text_value=input_css.get_attribute('value')
        utillity.UtillityMethods.asequal(self, expected_text_value, input_textvalue, msg)
        filter_btn="#btnOK"
        parent_css=self.driver.find_element_by_css_selector(filter_btn)
        utillity.UtillityMethods.click_on_screen(self, parent_css, "middle", click_type=0)

    def select_data_field(self, data_field_path, field_position=1):
        """
        This method used to click on specific field row
        """
        datatree_scrollable_css="#metaDataBrowser div[class='bi-tree-view-body']"
        selected_data_field_css="#metaDataBrowser  table[class='bi-tree-view-table']>tbody>tr[class*='selected']>td>img[class='icon']"
        data_field_path_list=data_field_path.rsplit('->', 1)
        data_field_section_path=None if len(data_field_path_list) == 1 else data_field_path_list[0]
        field_name=data_field_path_list[-1]
        if data_field_section_path != None :
            Wf_Reporting_Object.expand_data_field_section(self, data_field_section_path)
        else :
            JavaScript.scroll_element(self, datatree_scrollable_css, 0)
            Wf_Reporting_Object.move_to_data_tree_field_element(self)
        filed_object=Wf_Reporting_Object.__get_datatree_filed_row_object(self, field_name, field_position)
        filed_icon_obj=filed_object.find_element_by_css_selector("img[class*='icon']")
        utillity.UtillityMethods.left_click_with_offset(self, filed_icon_obj, x_offset=40)
        utillity.UtillityMethods.synchronize_with_number_of_element(self, selected_data_field_css, 1, expire_time=5)
    
    def collapse_data_field_section(self, data_field_section_path, find_from_top=True):
        """
        This method used to collapse the data field. data_field_section_path should be in reverse order. for example if 'Product->Product->Model' already expanded then 
        we should pass data_field_section_path as 'Model->Product->Product' to close section
        """
        Wf_Reporting_Object.__expand_or_collapse_data_filed_section(self, data_field_section_path, 'CLOSE', find_from_top)

    def expand_data_field_section(self, data_field_section_path, find_from_top=True):
        """
        This method used to expand the data field
        """
        Wf_Reporting_Object.__expand_or_collapse_data_filed_section(self, data_field_section_path, 'EXPAND', find_from_top)
    
    def __expand_or_collapse_data_filed_section(self, data_field_section_path, target, find_from_top=True):
        """
        This method used to expand or close data field section
        """
        if find_from_top==True :
            datatree_scrollable_css="#metaDataBrowser div[class='bi-tree-view-body']"
            JavaScript.scroll_element(self, datatree_scrollable_css, 0, wait_time=1)
        Wf_Reporting_Object.move_to_data_tree_field_element(self)
        if target.upper() == 'EXPAND' :
            icon_css="img[src*='view-plus']"
        if target.upper() == 'CLOSE' :
            icon_css="img[src*='view-minus']"
        data_field_section_list=data_field_section_path.split('->')
        previous_section=None
        for section in data_field_section_list :
            current_section=section
            field_position=2 if previous_section==current_section else 1
            section_object=Wf_Reporting_Object.__get_datatree_filed_row_object(self, section,  field_position)
            icon_obj=section_object.find_elements_by_css_selector(icon_css)
            if len(icon_obj) > 0 : #check whether field section is already closed or expanded. section is closed or expanded if icon_obj length is 0
                utillity.UtillityMethods.default_click(self, icon_obj[0])
            previous_section=section
    
    def __get_datatree_filed_row_object(self, row_field_name, field_position):
        """
        This method used get specific data field row object
        """
        ERROR_MSG="[{0}] data field not found in data tree".format(row_field_name)
        data_field_rows_css="#metaDataBrowser table[class='bi-tree-view-table']>tbody>tr>td"
        utillity.UtillityMethods.scroll_down_and_find_item_using_mouse(self, data_field_rows_css, row_field_name)
        data_field_rows_object=self.driver.find_elements_by_css_selector(data_field_rows_css)
        row_objects=JavaScript.find_elements_by_text(self, data_field_rows_object, row_field_name)
        if len(row_objects)==0 :
            raise NoSuchElementException(ERROR_MSG)
        else :
            return row_objects[field_position-1]
    
    def move_to_data_tree_field_element(self):
        """
        This method used to move mouse cursor to data tree field area. Mouse cursor should be move to data tree field area when we want use mouse scroll or page down
        """
        data_tree_obj=self.driver.find_element_by_id('metaDataBrowser')
        utillity.UtillityMethods.click_on_screen(self, data_tree_obj, 'middle')