import time, os, re
from common.lib import root_path
from common.lib.global_variables import Global_variables
from common.lib.javascript import JavaScript as javascript
from common.lib.utillity import UtillityMethods as utilobject
from common.locators.loginpage_locators import LoginPageLocators
from common.locators.wf_reporting_object_locators import WfReportingObjectLocators
from common.locators.visualization_ribbon_locators import VisualizationRibbonLocators
from common.pages.core_metadata import CoreMetaData as coremetadataobject
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class Wf_Smoketest(object):
    
    MEASURE_PARENT_CSS = None
    DIMENSIONS_PARENT_CSS = None
    QUERYBOX_PARENT_CSS = ".wfc-bucket-acc-page"
    QUERYTOOL_PARENT_CSS = QUERYBOX_PARENT_CSS + " [data-ibx-name='bucketToolbar']"
    QUERYBUCKET_PARENT_CSS = QUERYBOX_PARENT_CSS + " [data-ibx-name='bucketGroup']"
    CHART_PICKER_PARENT_CSS = '.chart-picker-box'
    FILTER_BAR_PARENT_CSS = '.filter-bar'
    DATA_FIELDS_CSS="#iaMetaDataBrowser [id^='QbMetaDataTree'] table[class='bi-tree-view-table']>tbody>tr>td[class='']"
    DATA_FIELDS_SCROLL_ELEMENT_CSS="#iaMetaDataBrowser [id^='QbMetaDataTree']>div[class='bi-tree-view-body']"
    SELECTED_DATA_FIELD_CSS="#iaMetaDataBrowser [id^='QbMetaDataTree'] table[class='bi-tree-view-table']>tbody>tr[class*='selected']>td>img[class*='icon']"
    SELECTED_DATATREE_ROW_CSS="#iaMetaDataBrowser [id^='QbMetaDataTree'] table[class='bi-tree-view-table']>tbody>tr[class*='selected']"
    
    
    def double_click_dimension_field_in_metadata_tree(self, field_name):
        dimension_tree_css="div[class*='metadata-container'][class*='dimension-tree-box'] div[class*='tnode-label']"
        dimension_tree_description = field_name+' listed under dimension tree'
        field_obj=utilobject.validate_and_get_webdriver_objects(self, dimension_tree_css, dimension_tree_description)
        for elem in field_obj:
            if elem.text.strip()==field_name:
                ActionChains(self.driver).move_to_element(elem).double_click().perform()
                time.sleep(Global_variables.longwait)
                break
    
    def select_bipopup_list_item(self, list_item_name, bipopup_item_css="table tr", action_chain_click=False,**kwargs):
        '''
        Desc:- This function is for selecting a single item from a BiPopup list items.
        :param list_item_name:- 'Add to Query' or 'Delete' or 'Horizontal Axis' 
        :param bipopup_item_css:- need to pass the css if there is any other type of css
        ''' 
        bipopups=self.driver.find_elements_by_css_selector("div[id^='BiPopup'][style*='inherit']")
        menu_items=bipopups[len(bipopups)-1].find_elements_by_css_selector(bipopup_item_css)
        actual_popup_list=[el.text.strip() for el in menu_items]
        ActionChains(self.driver).move_to_element_with_offset(menu_items[actual_popup_list.index(list_item_name)], xoffset=-9, yoffset=0).click().perform()
    
    def expand_data_field_section(self, data_field_section_path, find_from_top=True):
        """
        This method used to expand the data field
        """
        Wf_Smoketest.__expand_or_close_data_field_section(self, data_field_section_path, 'EXPAND', find_from_top)
    
    def __expand_or_close_data_field_section(self, data_field_section_path, target, find_from_top=True):
        """
        This method used to expand or close the data field section.  
        """
        if find_from_top == True :
            javascript.scroll_element(self, Wf_Smoketest.DATA_FIELDS_SCROLL_ELEMENT_CSS, 0, wait_time=1)
        if target.upper() == 'EXPAND' :
            icon_css="img[src*='closed']"
        if target.upper() == 'CLOSE' :
            icon_css="img[src*='open']"
        previous_section=None
        field_section_list=data_field_section_path.split('->')
        for section in field_section_list :
            current_section=section
            field_position=2 if previous_section==current_section else 1
            section_obj=coremetadataobject.find_data_field(self, section, field_position)
            icon_obj=section_obj.find_elements_by_css_selector(icon_css)
            if len(icon_obj) > 0 : #check whether field section is already closed or expanded. section is closed or expanded if icon_obj length is 0
                ActionChains(self.driver).move_to_element_with_offset(icon_obj[0], xoffset=0, yoffset=0).click().perform()
            previous_section=section    
        
    def select_data_field(self, data_field_path, field_position=1):
        """
        This method used to click on specific field row
        """
        javascript.scroll_element(self, Wf_Smoketest.DATA_FIELDS_SCROLL_ELEMENT_CSS, 0, wait_time=1)
        data_field_path_list=data_field_path.rsplit('->', 1)
        data_field_section_path=None if len(data_field_path_list) == 1 else data_field_path_list[0]
        field_name=data_field_path_list[-1]
        if data_field_section_path != None :
            Wf_Smoketest.expand_data_field_section(self, data_field_section_path, find_from_top=False)
        filed_object=coremetadataobject.find_data_field(self, field_name, field_position)
        filed_icon_obj=filed_object.find_element_by_css_selector("img[class*='icon']")
        ActionChains(self.driver).move_to_element_with_offset(filed_icon_obj, xoffset=25, yoffset=0).click().perform()
        utilobject.synchronize_with_number_of_element(self, Wf_Smoketest.SELECTED_DATATREE_ROW_CSS, 1, expire_time=4)
        
    def get_masterfile_field_path(self, master_file, filed_key):
        """
        This method used to get data file path from master_file.data
        """
        MASTER_FILE_NAME='master_file.data'
        MASTER_FILE_PATH=os.path.join(root_path.ROOT_PATH, MASTER_FILE_NAME)
        field_path=utilobject.read_configparser_key_value(self, MASTER_FILE_PATH, master_file, filed_key)
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
            field_path=Wf_Smoketest.get_masterfile_field_path(self, master_file_name, filed_key)
        Wf_Smoketest.select_data_field(self, field_path, field_position)
                        
    def select_datatree_field(self, data_file_name, click_type, field_position, context_menu_path=None):
        '''
        :Description: This function is used to select field in data tree. We can do left/right/double click on the field.
        We can select the context menu by right clicking.
        :Param: click_type= 'left' OR 'right' OR 'double'
        '''
        Wf_Smoketest.select_data_field_using_master_file_data(self, data_file_name, field_position)
        row_css="#iaMetaDataBrowser div[id^='QbMetaDataTree-'] tr[class*='selected'] img[class='icon']"
        newelement = self.driver.find_element_by_css_selector(row_css)
        if click_type == 'left':
            newelement.click()
            time.sleep(1)
        elif click_type == 'right':
            ActionChains(self.driver).move_to_element_with_offset(newelement, xoffset=0, yoffset=0).context_click().perform()
            if context_menu_path != None:
                for menu_item in context_menu_path.split('->'):
                    Wf_Smoketest.select_bipopup_list_item(self, menu_item)
            time.sleep(6)
        elif click_type == 'double':
            ActionChains(self.driver).move_to_element_with_offset(newelement, xoffset=0, yoffset=0).double_click().perform()
            time.sleep(Global_variables.longwait)
    
    def dialog_box(self, button_name_to_click=False, close_dialog=False, title_text=False, dialog_msg=False):
        """
        Descriptions : This method used to handle dialog box such as click on Ok, Yes, No and etc
        example usage : dialog_box(button_name_to_click = 'Yes')
        """
        dialogbox_parent_css = "div[data-ibx-type='ibxDialog'][class*='pop-top']"
        dialog_buttons_css = dialogbox_parent_css + " div[data-ibx-type='ibxButton']:not([style*='none'])>div[class='ibx-label-text']"
        utilobject.synchronize_with_number_of_element(self, dialogbox_parent_css, expected_number=1, expire_time=10)
        dialogbox_parent_obj=self.driver.find_element_by_css_selector(dialogbox_parent_css)
        if title_text==True :
            pass
        if dialog_msg==True :
            pass
        if button_name_to_click != None :
            dialog_buttons_obj = self.driver.find_elements_by_css_selector(dialog_buttons_css)
            dialog_button_index = javascript.find_element_index_by_text(self, dialog_buttons_obj, button_name_to_click)
            if dialog_button_index == None :
                error = '{0} button not displayed in dialog box'
                raise KeyError(error)
            else :
                dialog_button_obj = dialog_buttons_obj[dialog_button_index]
                dialog_button_obj.click()
        if close_dialog == True :
            close_btn_obj=dialogbox_parent_obj.find_element_by_css_selector("div[data-ibx-name='titleClose']")
            close_btn_obj.click()
        time.sleep(2)
    
    def enter_filename_in_open_dialog_resources(self, folder_path=None, title=None, name=None, ok_button=False, cancel_button=False):
        """
        Descriptions : This method used to perform different operation such as save page, save as page, open page, etc
        example usage1 : page_designer_open_dialog_resources(folder_path='P116->S7074', title='Test')
        example usage2 : page_designer_open_dialog_resources(ok_button=True)
        """
        parent_css="div[class*='open-dialog-resources']"
        cancel_btn_css=parent_css + " div[data-ibx-name='btnCancel']"
        utilobject.synchronize_with_visble_text(self, cancel_btn_css, visble_element_text='Cancel', expire_time=15)
        if folder_path !=None :
            pass # Need to implement
        if title !=None :
            title_textbox_css = "div[data-ibx-name='sdtxtFileTitle']"
            title_textbox_obj = utilobject.validate_and_get_webdriver_object(self, title_textbox_css, 'Save dialog title text box')
            title_textbox_input_obj = utilobject.validate_and_get_webdriver_object(self, 'input', 'Save dialog title text box input', parent_object=title_textbox_obj)
            title_textbox_input_obj.clear()
            ActionChains(self.driver).send_keys_to_element(title_textbox_input_obj,title).click(title_textbox_input_obj).perform()
            utilobject.synchronize_with_visble_text_within_parent_object(self, title_textbox_obj, 'input', title, 90, text_option='text_value')
        if name !=None :
            pass # Need to implement
        if ok_button == True :
            ok_button_css=parent_css + " div[data-ibx-name='btnOK']"
            ok_button_obj=self.driver.find_element_by_css_selector(ok_button_css)
            ok_button_obj.click()
        if cancel_button == True :
            cancel_button_obj=self.driver.find_element_by_css_selector(cancel_btn_css)
            cancel_button_obj.click()
        time.sleep(2)
        try : #Checking whether already file exits dialog box appear
            dialog_box_obs=self.driver.find_elements_by_css_selector("div[data-ibx-type='ibxDialog'][class*='pop-top']")
            if len(dialog_box_obs)>0 :
                Wf_Smoketest.dialog_box(self,  button_name_to_click='OK')
        except :
            pass    
    
    def select_combobox_item(self, combo_id, combo_item, **kwargs):
        """
        Syntax: utillobj.select_combobox_item('comboSourceFields', 'Equals to')
        """
        combo_btn=self.driver.find_element_by_css_selector("div[id*=" + combo_id + "] div[id^='BiButton']")
        combo_btn.click()
        menu_items=self.driver.find_elements_by_css_selector("div[id^='BiPopup'][style*='inherit'] div[id^='BiComboBoxItem']")
        actual_popup_list=[el.text.strip() for el in menu_items]
        menu_items[actual_popup_list.index(combo_item)].click()
        time.sleep(1)
    
    def click_toolbar_save(self):
        """
        Descriptions : This method used to click on toolbar save button 
        """
        save_btn_css="[class^='ibxtool-toolbar-group'] div[class^='ibxtool-toolbar-button'][class*='toolbar-save']"
        save_btn_description = 'Save button available in toolbar'
        save_btn_obj=utilobject.validate_and_get_webdriver_object(self, save_btn_css, save_btn_description)
        save_btn_obj.click()
            
    def ibfs_save_as(self, file_name, file_type=None,**kwargs):  
        """
        Param: file_name: '<fex_name to be saved>'
        Syntax: utillobj.ibfs_save("test1")
        @author = Niranjan
        """
        time.sleep(9)
        file_name_input_css="#IbfsOpenFileDialog7_cbFileName input"
        elem1=(By.CSS_SELECTOR, file_name_input_css)
        self._validate_page(elem1)
        action = ActionChains(self.driver) 
        self.driver.find_element_by_css_selector(file_name_input_css).clear()
        element = self.driver.find_element_by_css_selector(file_name_input_css)
        action.send_keys_to_element(element,file_name).click(element).perform()
        time.sleep(1)
        if file_type != None:
            Wf_Smoketest.select_combobox_item(self,'IbfsOpenFileDialog7_cbFilterType', file_type)
        if 'save_folder' in kwargs :
            time.sleep(3)
            folder_tree=self.driver.find_elements_by_css_selector("#paneIbfsExplorer_exTree div[class='bi-tree-view-body-content']>table>tbody>tr>td")
            for item in folder_tree :
                if item.text.strip()==kwargs['save_folder'] :
                    folder_icon=item.find_element_by_css_selector("img[src*='folder_closed']")
                    folder_icon.click()
                    break
            time.sleep(4)
        self.driver.find_element_by_id("IbfsOpenFileDialog7_btnOK").click()
        self.driver.implicitly_wait=3
        try:
            if self.driver.find_element_by_css_selector("div[id^='BiDialog'] img[src*='exclamation']").is_displayed():
                btn_css="div[id^='BiDialog'] div[class=bi-button-label]"
                dialog_btns=self.driver.find_elements_by_css_selector(btn_css)
                btn_text_list=[el.text.strip() for el in dialog_btns]
                dialog_btns[btn_text_list.index('Yes')].click()
        except:
            pass
        time.sleep(2)
                    
    def save_chart_from_toolbar(self, title_to_save, wait_time=3):
        """
        Descriptions : This method used to click on save button on tool bar and save current page with default name  
        """
        Wf_Smoketest.click_toolbar_save(self)
        Wf_Smoketest.enter_filename_in_open_dialog_resources(self, title=title_to_save, ok_button=True)
        time.sleep(wait_time)  
        
    def select_top_toolbar_item(self, item_name, **kwargs):
        """
        param: item_name: 'toptoolbar_new' OR 'toptoolbar_run' - these need to be get it from Wf_Reporting_Object_Locators.
        This function is specific to click on toolbar buttons - new, run, undo, redo, run
        """
        top_toolbar_obj=self.driver.find_element(*WfReportingObjectLocators.__dict__[item_name])
        top_toolbar_obj.click()
        time.sleep(Global_variables.longwait)
    
    def select_ia_top_toolbar_item(self, top_toolbar_item_name):
        '''
        Desc: This function is specific to click on top toolbar buttons - new, run, undo, redo, run.
        param: item_name: 'new' OR 'run'.
        '''
        time.sleep(Global_variables.longwait)
        toolbar_item=self.driver.find_element(*VisualizationRibbonLocators.__dict__['toolbar_'+top_toolbar_item_name])
        toolbar_item.click()
        time.sleep(Global_variables.longwait)  
        