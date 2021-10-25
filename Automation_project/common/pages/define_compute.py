import time, re
from common.lib import utillity
from common.lib.base import BasePage
from common.pages import visualization_ribbon 
from selenium.webdriver import ActionChains
from common.lib.javascript import JavaScript
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from common.locators.ia_ribbon_locators import IaRibbonLocators
from common.lib.global_variables import Global_variables
from common.lib.core_utility import CoreUtillityMethods as core_utils

class Define_Compute(BasePage):

    def calculate_define_compute(self, type, type_name, type_format, data_field, position, click_type, *args, **kwargs):
        """
        kwargs: 8201 - verify_field_text='WF_RETAIL_LITE.WF_RETAIL_PRODUCT.PRODUCT_CATEGORY ' will verify textarea area after field addition in define dialog
        kwargs: 8202 ad above - verify_field_text='''"Product,Category" '''
        Usage: calculate_define_compute('Define', 'DMMYname', 'D10.2', 'Revenue', 1, 'ok')
        """
        action = ActionChains(self.driver)
        calculate_btn = self.driver.find_element_by_xpath("//*[@id='HomeCalcMenuBtn']")
        utillity.UtillityMethods.default_left_click(self, object_locator=calculate_btn)
#         calculate_btn.click()
        option = self.driver.find_element_by_xpath("//td[contains(text(), '" + type + "')]")
        WebDriverWait(self.driver, 25).until(lambda driver: option.is_displayed())
        option.click()
        time.sleep(5)
        field_name = self.driver.find_element_by_id("fname")
        field_format = self.driver.find_element_by_id("fformat")
        field_name.send_keys(type_name)
        time.sleep(3)
        field_format.clear()
        field_format.send_keys(type_format)
        time.sleep(3)
        newelement = Define_Compute.get_metadata_field(self, data_field, position)
        time.sleep(2)
        if Global_variables.browser_name in ['firefox']:
            utillity.UtillityMethods.click_type_using_pyautogui(self, newelement, doubleClick=True, **kwargs)
        else: 
            action.double_click(newelement).perform()
        time.sleep(10)
        if 'verify_field_text' in kwargs:
            field_text = self.driver.find_element_by_css_selector("textarea").get_attribute("value")
            utillity.UtillityMethods.asequal(self, field_text,kwargs['verify_field_text'],"StepX: Verify define dialog added field text in textarea")
        if click_type == "ok":
            self.driver.find_element_by_id("fldCreatorOkBtn").click()
        else:
            self.driver.find_element_by_id("fldCreatorCancelBtn").click()
        time.sleep(3)

    def invoke_define_compute_dialog(self, calculation_type):
        visual_ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        visual_ribbonobj.switch_ia_tab('Data')
        time.sleep(1)
        if calculation_type == 'define':
            #self.driver.find_element(*IaRibbonLocators.data_define).click()
            def_elem=self.driver.find_element(*IaRibbonLocators.data_define)
            utillity.UtillityMethods.default_left_click(self, object_locator=def_elem)
        else:
            #self.driver.find_element(*IaRibbonLocators.data_compute).click()
            comp_elem=self.driver.find_element(*IaRibbonLocators.data_compute)
            utillity.UtillityMethods.default_left_click(self, object_locator=comp_elem)
        time.sleep(1)
        
    def get_metadata_field(self, data_field_path, field_position=1):
        """
        @Param : data_field = "Revenue'
        @param : position = 1
        @Usage : get_metadata_field("Revenue", 1)
        """ 
        selected_data_field_css="#defineMetaData table[class='bi-tree-view-table']>tbody>tr[class*='selected']>td>img[class='icon']"
        data_tree_scrollable_css="#defineMetaData div[class='bi-tree-view-body']"
        master_file_css="#defineMetaData table[class='bi-tree-view-table']>tbody>tr:nth-child(1)>td"
        master_file_icon_css=master_file_css + ">img[src*='cubes']"
        if bool(re.match('.*->.*', data_field_path)):
            field_path = data_field_path
        else :
            JavaScript.scroll_element(self, data_tree_scrollable_css, 0)
            utillity.UtillityMethods.synchronize_with_number_of_element(self, master_file_icon_css, 1, expire_time=3)
            master_file_name=self.driver.find_element_by_css_selector(master_file_css).text.strip()
            field_path_key=master_file_name + '_' + data_field_path
            field_path=utillity.UtillityMethods.get_masterfile_field_path(self, master_file_name, field_path_key)
        Define_Compute.select_data_field(self, field_path, field_position)
        data_field_object=self.driver.find_element_by_css_selector(selected_data_field_css)
        return (data_field_object)
        
    def drag_metadata_field_to_text_area(self, data_field_path, field_position=1, **kwargs):
        """
        @Param : data_field='Revenue'
        @Param : position=1 or 2
        @Usage : select_define_compute_field("Revenue", 1)
        """
        source_elem = Define_Compute.get_metadata_field(self, data_field_path, field_position)
        target_elem=self.driver.find_element_by_css_selector("[id^='QbDialog'] textarea")
        utillity.UtillityMethods.drag_drop_using_uisoup(self,source_elem,target_elem,**kwargs)
        time.sleep(2)
        
    def select_define_compute_field(self, data_field, field_position=1, **kwargs):
        """
        @Param : data_field='Revenue'
        @Param : position=1 or 2
        @Usage : select_define_compute_field("Revenue", 1)
        """
        newelement = Define_Compute.get_metadata_field(self, data_field, field_position)
        utillity.UtillityMethods.default_click(self, newelement, 2)
        time.sleep(2)
        
    def enter_define_compute_parameter(self, type_name, type_format, data_field, position, **kwargs):
        """
        @Param : type_name = 'Compute_1'
        @Param : type_format = '14.5'
        @Param : data_field = 'Cost of Goods'
        @Param : position = 1 position starts with 1 always
        @Usage : enter_compute_parameter('Compute_1', '14.5','Cost of Goods', 1)
        """
        field_name = self.driver.find_element_by_id("fname")
        field_format = self.driver.find_element_by_id("fformat")
        utillity.UtillityMethods.set_text_field_using_actionchains(self, field_name, type_name, keyboard_type=True)
        utillity.UtillityMethods.set_text_field_using_actionchains(self, field_format, type_format, keyboard_type=True)
        Define_Compute.select_define_compute_field(self, data_field, position, **kwargs)
        
    def close_define_compute_dialog(self, click_type):
        if click_type == "ok":
            btn_elem=self.driver.find_element_by_id("fldCreatorOkBtn")
        else:
            btn_elem=self.driver.find_element_by_id("fldCreatorCancelBtn")
        utillity.UtillityMethods.default_left_click(self, object_locator=btn_elem)
        time.sleep(3)
        
    def select_calculation_btns(self, btn_series):
        btn_css={'bitor':"# calcButtons #btnBitOr", 
                'lt':"#calcButtons #btnLT",
                'gt':"#calcButtons #btnGT",
                'plus':"#calcButtons #btnPlus",
                'seven':"#calcButtons #btn7",
                'eight':"#calcButtons #btn8",
                'nine':"#calcButtons #btn9",
                'logor':"#calcButtons #btnLogOr",
                'le':"#calcButtons #btnLE",
                'ge':"#calcButtons #btnGE",
                'minus':"#calcButtons #btnMinus",
                'four':"#calcButtons #btn4",
                'five':"#calcButtons #btn5",
                'six':"#calcButtons #btn6",
                'seven':"#calcButtons #btn7",
                'nine':"#calcButtons #btn9",
                'if':"#calcButtons #btnIf",
                'eq':"#calcButtons #btnEQ",
                'ne':"#calcButtons #btnNE",
                'mult':"#calcButtons #btnMult",
                'one':"#calcButtons #btn1",
                'two':"#calcButtons #btn2",
                'three':"#calcButtons #btn3",
                'then':"#calcButtons #btnThen",
                'and':"#calcButtons #btnAND",
                'or':"#calcButtons #btnOR",
                'div':"#calcButtons #btnDiv",
                'zero':"#calcButtons #btn0",
                'dot':"#calcButtons #btnDot",
                'else':"#calcButtons #btnElse",
                'not':"#calcButtons #btnNot",
                'exp':"#calcButtons #btnExp",
                'paren':"#calcButtons #btnParen",
                'quote':"#calcButtons #btnQuote",
                'upper':"#calcButtons #btnUppercase"}
        btns=btn_series.split('->')
        for btn in btns:
            self.driver.find_element_by_css_selector(btn_css[btn.lower()]).click()
            time.sleep(1)
            
    def select_menu_button_in_compute(self, menu_path):  
        menus=menu_path.split('->')
        arrow_btn_index={'additional_option':1,
                'view_fields_in_business_order':2,
                'view_fields_in_sortable_grid':3,
                'view_the_hierarchical_structure_of_the_data':4}
        if menus[0] != 'functions':
            arrows=self.driver.find_elements_by_css_selector("[id^='QbDialog'] #rightPane [class$='tool-bar-menu-button-drop-down-arrow']")
            required_button=arrows[arrow_btn_index[menus[0]]]
        else:
            required_button=self.driver.find_element_by_css_selector("[id^='QbDialog'] #rightPane #btnFunctions")
        utillity.UtillityMethods.click_on_screen(self, required_button, 'middle', click_type=0, pause=1)
    
    def select_data_field(self, data_field_path, field_position=1):
        """
        This method used to click on specific field row
        """
        data_field_rows_css="#defineMetaData div[class='bi-tree-view-body']"
        selected_data_field_css="#defineMetaData table[class='bi-tree-view-table']>tbody>tr[class*='selected']>td>img[class='icon']"
        data_field_path_list=data_field_path.rsplit('->', 1)
        data_field_section_path=None if len(data_field_path_list) == 1 else data_field_path_list[0]
        field_name=data_field_path_list[-1]
        if data_field_section_path != None :
            Define_Compute.expand_data_field_section(self, data_field_section_path)
        else :
            JavaScript.scroll_element(self, data_field_rows_css, 0)
            Define_Compute.move_to_data_tree_field_element(self)
        filed_object=Define_Compute.__get_datatree_row_object(self, field_name, field_position)
        filed_icon_obj=filed_object.find_element_by_css_selector("img[class*='icon']")
        utillity.UtillityMethods.click_on_screen(self, filed_icon_obj, 'right', 0, x_offset=30, mouse_duration=0, wait_time=1)
        utillity.UtillityMethods.synchronize_with_number_of_element(self, selected_data_field_css, 1, expire_time=5)
    
    def close_data_field_section(self, data_field_section_path, find_from_top=True):
        """
        This method used to close the data field. data_field_section_path should be in reverse order. for example if 'Product->Product->Model' already expanded then 
        we should pass data_field_section_path as 'Model->Product->Product' to close section
        """
        Define_Compute.__expand_or_close_data_filed_section(self, data_field_section_path, 'CLOSE', find_from_top)

    def expand_data_field_section(self, data_field_section_path, find_from_top=True):
        """
        This method used to expand the data field
        """
        Define_Compute.__expand_or_close_data_filed_section(self, data_field_section_path, 'EXPAND', find_from_top)
    
    def __get_datatree_row_object(self, row_name, field_position):
        """
        This method used get specific data field row object
        """
        ERROR_MSG="[{0}] data field not found in data tree".format(row_name)
        data_field_rows_css="#defineMetaData table[class='bi-tree-view-table']>tbody>tr>td"
        utillity.UtillityMethods.scroll_down_and_find_item_using_mouse(self, data_field_rows_css, row_name)
        data_field_rows_object=self.driver.find_elements_by_css_selector(data_field_rows_css)
        row_objects=JavaScript.find_elements_by_text(self, data_field_rows_object, row_name)
        if len(row_objects)==0 :
            raise NoSuchElementException(ERROR_MSG)
        else :
            return row_objects[field_position-1]
    
    def __expand_or_close_data_filed_section(self, data_field_section_path, target, find_from_top=True):
        """
        This method used to expand or close data field section
        """
        if find_from_top==True :
            datatree_scrollable_css="#defineMetaData div[class='bi-tree-view-body']"
            JavaScript.scroll_element(self, datatree_scrollable_css, 0, wait_time=1)
        Define_Compute.move_to_data_tree_field_element(self)
        if target.upper() == 'EXPAND' :
            icon_css="img[src*='view-plus']"
        if target.upper() == 'CLOSE' :
            icon_css="img[src*='view-minus']"
        data_field_section_list=data_field_section_path.split('->')
        previous_section=None
        for section in data_field_section_list :
            current_section=section
            field_position=2 if previous_section==current_section else 1
            section_object=Define_Compute.__get_datatree_row_object(self, section,  field_position)
            icon_obj=section_object.find_elements_by_css_selector(icon_css)
            if len(icon_obj) > 0 : #check whether field section is already closed or expanded. section is closed or expanded if icon_obj length is 0
                utillity.UtillityMethods.default_click(self, icon_obj[0])
            previous_section=section
    
    def move_to_data_tree_field_element(self):
        """
        This method used to move mouse cursor to data tree field area. Mouse cursor should be move to data tree field area when we want use mouse scroll or page down
        """
        data_tree_obj=self.driver.find_element_by_id('defineMetaData')
        utillity.UtillityMethods.click_on_screen(self, data_tree_obj, 'middle')
    
class DefineCompute :
    
    def __init__(self, driver):
        
        self.driver = driver
    
    def enter_values_in_field_textbox(self, value, clear=True):
        """
        Description : This method will enter values in field text box
        :usage : enter_values_in_field_textbox("Define_1")
        """
        field_textbox = utillity.UtillityMethods.validate_and_get_webdriver_object(self, "#fname", "Define Compute field text box")
        core_utils.left_click(self, field_textbox)
        if clear == True :
            field_textbox.clear()
        field_textbox.send_keys(value)
    
    def verify_filed_textbox_values(self, expected_value, step_num):
        """
        Description : Verify field text box value
        :usage : verify_filed_textbox_values("Define_1", "01.02")
        """
        field_textbox_obj = utillity.UtillityMethods.validate_and_get_webdriver_object(self, "#fname", "Define Compute field text box")
        actual_value = utillity.UtillityMethods.get_element_attribute(self, field_textbox_obj, 'value')
        msg = "Step {0} : Verify [{1}] value displayed in field textbox".format(step_num, expected_value)
        utillity.UtillityMethods.asequal(self, expected_value, actual_value, msg)
    
    def enter_values_in_format_textbox(self, value, clear=True):
        """
        Description : This method will enter values in field text box
        :usage : enter_values_in_field_textbox("Define_1")
        """
        format_textbox = utillity.UtillityMethods.validate_and_get_webdriver_object(self, "#fformat", "Define Compute format text box")
        core_utils.left_click(self, format_textbox)
        if clear == True :
            format_textbox.clear()
        format_textbox.send_keys(value)
    
    def verify_format_textbox_values(self, expected_value, step_num):
        """
        Description : Verify field text box value
        :usage : verify_filed_textbox_values("Define_1", "01.02")
        """
        field_textbox_obj = utillity.UtillityMethods.validate_and_get_webdriver_object(self, "#fformat", "Define Compute field text box")
        actual_value = utillity.UtillityMethods.get_element_attribute(self, field_textbox_obj, 'value')
        msg = "Step {0} : Verify [{1}] value displayed in format textbox".format(step_num, expected_value)
        utillity.UtillityMethods.asequal(self, expected_value, actual_value, msg)
    
    def double_click_on_data_field(self, field_name, field_position=1):
        """
        Description : Expand data field section double click on field
        :usage : double_click_on_data_field("car")
        """
        Define_Compute.select_define_compute_field(self, field_name, field_position)
    
    def drag_data_field_to_text_area(self, field_name, field_position=1):
        """
        Description : Drag data field to text area
        :usage : drag_data_field_to_text_area("car")
        """
        Define_Compute.drag_metadata_field_to_text_area(self, field_name, field_position)
    
    def click_on_text_area(self):
        """
        Description : Left click on text area
        """
        text_area = utillity.UtillityMethods.validate_and_get_webdriver_object(self, "#ftext", "Define Compute text area")
        core_utils.left_click(self, text_area)
    
    def click_format(self):
        """
        Description : Left click on Format
        """
        format_ = utillity.UtillityMethods.validate_and_get_webdriver_object(self, "#btnFormat", "Define Compute Format")
        core_utils.left_click(self, format_)
        utillity.UtillityMethods.synchronize_with_visble_text(self, "#fmtDlgOk", "OK", 20)
    
    def enter_values_in_text_area(self, values, clear=True):
        """
        Description : This method will enter values in text area
        :usage : enter_values_in_text_area("CAR")
        """
        text_area = utillity.UtillityMethods.validate_and_get_webdriver_object(self, "#ftext", "Define Compute text area")
        core_utils.left_click(self, text_area)
        if clear == True :
            text_area.clear()
        text_area.send_keys(values)
    
    def verify_text_area_expression(self, expected_expression, step_num):
        """
        Description : Verify text area expression values
        :usage : verify_text_area_expression("Define_1", "01.02")
        """
        field_textbox_obj = utillity.UtillityMethods.validate_and_get_webdriver_object(self, "#ftext", "Define Compute field text box")
        actual_value = utillity.UtillityMethods.get_element_attribute(self, field_textbox_obj, 'value')
        msg = "Step {0} : Verify [{1}] expression displayed in text area".format(step_num, expected_expression)
        utillity.UtillityMethods.asequal(self, expected_expression, actual_value, msg)
    
    def click_key_buttons(self, button_names_list):
        """
        Description : Click on key button
        :usage : click_key_buttons("div")
        """
        Define_Compute.select_calculation_btns(self, button_names_list)
    
    def click_ok_button(self):
        """
        Description : Left click on OK button
        """
        button_obj = utillity.UtillityMethods.validate_and_get_webdriver_object(self, "#fldCreatorOkBtn", "Define compute OK button")
        core_utils.left_click(self, button_obj)
    
    def click_cancel_button(self):
        """
        Description : Left click on Cancel button
        """
        button_obj = utillity.UtillityMethods.validate_and_get_webdriver_object(self, "#fldCreatorCancelBtn", "Define compute Cancel button")
        core_utils.left_click(self, button_obj)
    
    def search_metadata_field(self, field_name, clear=True):
        """
        Description : This method will enter field name in metadata search textbox
        :usage : search_metadata_field("CAR")
        """
        textbox = utillity.UtillityMethods.validate_and_get_webdriver_object(self, "#defineMetaData #metaDataSearchTxtFld", "Define Compute metadata search textbox")
        core_utils.left_click(self, textbox)
        if clear == True :
            textbox.clear()
        textbox.send_keys(field_name)