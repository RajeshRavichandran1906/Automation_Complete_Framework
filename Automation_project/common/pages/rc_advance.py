from common.lib import utillity
from common.lib.base import BasePage
from common.pages import rc_misc
from common.locators.rc_advance_locators import RCAdvanceLocators
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time, re, os


class RC_Advance(BasePage):
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(RC_Advance, self).__init__(driver)

    def _validate_page(self, locator):
        self.longwait.until(EC.visibility_of_element_located(locator))
    
    def select_rc_ribbon_button(self, ribbon_button_name): 
        """
        param ribbon_button_name: 'save_and_close' OR 'properties'.... (Refer to the locator file to understand the ribbon object naming convention)
        Syntax: select_rc_ribbon_button('properties')
        @author = Niranjan
        """
        button_name = "ribbon_" + ribbon_button_name.lower()
        self.driver.find_element(*RCAdvanceLocators.__dict__[button_name]).click()
        time.sleep(2)
    
    def select_rc_menu_item(self, menu_item_name):
        """
        param menu_item_name: 'Save', 'Save As..'.... (any item to be clicked from the RC menu)
        Syntax: select_rc_menu_item('Save')
        @author = Niranjan
        """
        self.driver.find_element(*RCAdvanceLocators.rc_menu_btn).click()
        time.sleep(2)
        utillity.UtillityMethods.select_or_verify_bipop_menu(self, menu_item_name)  
        time.sleep(2)  
        
    def create_properties(self, **kwargs): 
        """
        param title: 'Your title'
        Syntax: create_properties(title='Your title')
        @author = Niranjan
        """
        self.select_rc_ribbon_button('properties')
        time.sleep(2)
        if 'title' in kwargs:
            title_elem=self.driver.find_element(*RCAdvanceLocators.input_title)
            utillity.UtillityMethods.set_text_field_using_actionchains(self, title_elem, kwargs['title'])
            
    def verify_rc_grid_table(self, patern, **kwargs):
        """
        param patern='Enabled'....(The pattern to be matched)
        Syntax: verify_rc_grid_table('Enabled')
        @author = Niranjan
        """
        time.sleep(2)
        verify_str=self.driver.find_element_by_css_selector("##ScheduleEditor_recurrenceGrid2 table.bi-tree-view-table").text.strip()
        verify_pat=bool(re.match(".*" + patern, verify_str))
        utillity.UtillityMethods.asequal(self, True, verify_pat, "Step X: Verify the recurrence is enabled.")
           
    def schedule_recurrence(self, **kwargs): 
        """
        param schedule_recurrence='run_once' OR 'minutes'....(Refer to the locator file to understand the object naming convention)
        Syntax: schedule_recurrence('Layout')
        @author = Niranjan
        """
        self.select_rc_ribbon_button('recurrences')
        time.sleep(2)
        if 'schedule_recurrence' in kwargs:
            self.select_rc_ribbon_button('recurrences_new')
            self._validate_page(RCAdvanceLocators.recurrence_ok)
            self.driver.find_element(*RCAdvanceLocators.__dict__[kwargs['schedule_recurrence']]).click()
            time.sleep(1)
            self.driver.find_element(*RCAdvanceLocators.recurrence_ok).click()
            self.verify_rc_grid_table('Enabled')
    
    def invoke_task_type(self, task_type):
        """
        param btn_type: 'WebFOCUS Server Procedure' OR 'WebFOCUS Report' OR 'File' OR 'FTP, OR 'URL' 
        Syntax: invoke_task_type('WebFOCUS Server Procedure')
        @author = Niranjan
        """
        self.select_rc_ribbon_button('task')
        time.sleep(2)
        new_elem=self.driver.find_element(*RCAdvanceLocators.ribbon_task_new)
        utillity.UtillityMethods.select_any_combobox_item(self, new_elem, task_type)
        time.sleep(4)
        
    def set_task_password(self, task_type, id_elem, password_btn_elem, **kwargs):
        """
        param: task_type='frp' OR 'eda'
        param: execution_id_elem
        params: password_btn_elem
        Syntax: set_task_password('eda',execution_id_elem, password_btn_elem)
        @author = Niranjan
        """
        if task_type in ('ftp'):
            userid = utillity.UtillityMethods.parseinitfile(self,'ftpuser')
            passwd = utillity.UtillityMethods.parseinitfile(self,'ftppass')
        else:
            userid = utillity.UtillityMethods.parseinitfile(self,'rsuser')
            passwd = utillity.UtillityMethods.parseinitfile(self,'rspass')
        if id_elem.get_attribute("value")=='':
            utillity.UtillityMethods.set_text_field_using_actionchains(self, id_elem, userid)
            password_btn_elem.click()
            time.sleep(2)
            first_password_elem=self.driver.find_element_by_css_selector("#rcBiTaskPasswordDlg #TaskPasswordDlg_firstPasswordField")
            utillity.UtillityMethods.set_text_field_using_actionchains(self, first_password_elem, passwd)
            second_password_elem=self.driver.find_element_by_css_selector("#rcBiTaskPasswordDlg #TaskPasswordDlg_confirmPasswordField")
            utillity.UtillityMethods.set_text_field_using_actionchains(self, second_password_elem, passwd)
            self.driver.find_element_by_css_selector("#rcBiTaskPasswordDlg #TaskPasswordDlg_btnOK").click()
            time.sleep(2)
    
    def create_wf_server_procedure_task_general(self, **kwargs): 
        """
        param server_procedure_path: 'ibisamp->carinst'
        burst_report: True(Means we need to check) OR False(Means we need to uncheck)
        override_format: True(Means we need to check) OR False(Means we need to uncheck)
        Syntax: create_wf_server_procedure_task_general('Layout')
        @author = Niranjan
        """
        execution_id_elem=self.driver.find_element(*RCAdvanceLocators.wfserverproc_execution_id)
        password_btn_elem=self.driver.find_element(*RCAdvanceLocators.wfserverproc_password_btn)
        self.set_task_password('eda', execution_id_elem, password_btn_elem)
        if 'server_procedure_path' in kwargs:
            self.driver.find_element(*RCAdvanceLocators.wfserverproc_browse_btn).click()
            time.sleep(2)
            utillity.UtillityMethods.seletct_tree_view_plus_node(self,'#WFServerProcDlg_procTree2 table', kwargs['server_procedure_path'])
            self.driver.find_element_by_css_selector("#rcBiWFServerProcDlg #WFServerProcDlg_btnOK").click()
            selected_fex=self.driver.find_element(*RCAdvanceLocators.wfserverproc_procedure_name).get_attribute("value").strip()
            verify_pat=bool(re.match(".*"+kwargs['server_procedure_path'].split('->')[-1], selected_fex))    
            utillity.UtillityMethods.asequal(self, True, verify_pat, "Step X: Verify " + kwargs['server_procedure_path'].split('->')[-1] + " is selected.")
        if 'burst_report' in kwargs:
            if kwargs['burst_report']==True:
                status=self.driver.find_element(*RCAdvanceLocators.wfserverproc_burst_report_checkbox).is_selected()
                utillity.UtillityMethods.asequal(self, False, status, "Step X: Verify burst report is unchecked previously.")
                self.driver.find_element(*RCAdvanceLocators.wfserverproc_burst_report_checkbox).click()
                time.sleep(1)
            if kwargs['burst_report']==False:
                status=self.driver.find_element(*RCAdvanceLocators.wfserverproc_burst_report_checkbox).is_selected()
                utillity.UtillityMethods.asequal(self, True, status, "Step X: Verify burst report is checked previously.")
                self.driver.find_element(*RCAdvanceLocators.wfserverproc_burst_report_checkbox).click()
                time.sleep(1)
        if 'override_format' in kwargs:    
            if kwargs['override_format']==True:
                status=self.driver.find_element(*RCAdvanceLocators.wfserverproc_override_checkbox).is_selected()
                utillity.UtillityMethods.asequal(self, False, status, "Step X: Verify Override format is unchecked previously.")
                self.driver.find_element(*RCAdvanceLocators.wfserverproc_override_checkbox).click()
                time.sleep(1)
            if kwargs['override_format']==False:
                status=self.driver.find_element(*RCAdvanceLocators.wfserverproc_override_checkbox).is_selected()
                utillity.UtillityMethods.asequal(self, True, status, "Step X: Verify Override format is checked previously.")
                self.driver.find_element(*RCAdvanceLocators.wfserverproc_override_checkbox).click()
                time.sleep(1)
    
    def create_wf_server_procedure_task_parameters(self, **kwargs): 
        """
        param server_procedure_path: 'ibisamp->carinst'
        burst_report: True(Means we need to check) OR False(Means we need to uncheck)
        override_format: True(Means we need to check) OR False(Means we need to uncheck)
        Syntax: create_wf_server_procedure_general_task('Layout')
        @author = Niranjan
        """
    
    def create_wf_server_procedure_task_pre_post_procedure(self, **kwargs): 
        """
        param server_procedure_path: 'ibisamp->carinst'
        burst_report: True(Means we need to check) OR False(Means we need to uncheck)
        override_format: True(Means we need to check) OR False(Means we need to uncheck)
        Syntax: create_wf_server_procedure_general_task('Layout')
        @author = Niranjan
        """
        
    def create_wf_server_procedure_task_advanced_options(self, **kwargs): 
        """
        param server_procedure_path: 'ibisamp->carinst'
        burst_report: True(Means we need to check) OR False(Means we need to uncheck)
        override_format: True(Means we need to check) OR False(Means we need to uncheck)
        Syntax: create_wf_server_procedure_general_task('Layout')
        @author = Niranjan
        """

    def create_wf_report_task_general(self, **kwargs): 
        """
        param wf_report_path: 'carinst'
        burst_report: True(Means we need to check) OR False(Means we need to uncheck)
        override_format: True(Means we need to check) OR False(Means we need to uncheck)
        Syntax: create_wf_report_task_general('Layout')
        @author = Niranjan
        """
        execution_id_elem=self.driver.find_element(*RCAdvanceLocators.standardreport_execution_id)
        password_btn_elem=self.driver.find_element(*RCAdvanceLocators.standardreport_password_btn)
        self.set_task_password('eda', execution_id_elem, password_btn_elem)
        if 'wf_report_name' in kwargs:
            self.driver.find_element(*RCAdvanceLocators.standardreport_browse_btn).click()
            time.sleep(2)
            utillity.UtillityMethods.ibfs_save_as(self, kwargs['wf_report_path'])
            time.sleep(1)
            selected_fex=self.driver.find_element(*RCAdvanceLocators.standardreport_save_report_as_input).get_attribute("value").strip()
            utillity.UtillityMethods.asequal(self, selected_fex, kwargs['wf_report_name'], "Step X: Verify " + kwargs['wf_report_path'] + " is selected.")
        if 'burst_report' in kwargs:
            if kwargs['burst_report']==True:
                status=self.driver.find_element(*RCAdvanceLocators.standardreport_burst_report_checkbox).is_selected()
                utillity.UtillityMethods.asequal(self, False, status, "Step X: Verify burst report is unchecked previously.")
                self.driver.find_element(*RCAdvanceLocators.standardreport_burst_report_checkbox).click()
                time.sleep(1)
            if kwargs['burst_report']==False:
                status=self.driver.find_element(*RCAdvanceLocators.standardreport_burst_report_checkbox).is_selected()
                utillity.UtillityMethods.asequal(self, True, status, "Step X: Verify burst report is checked previously.")
                self.driver.find_element(*RCAdvanceLocators.standardreport_burst_report_checkbox).click()
                time.sleep(1)
        if 'override_format' in kwargs:    
            if kwargs['override_format']==True:
                status=self.driver.find_element(*RCAdvanceLocators.standardreport_override_checkbox).is_selected()
                utillity.UtillityMethods.asequal(self, False, status, "Step X: Verify Override format is unchecked previously.")
                self.driver.find_element(*RCAdvanceLocators.standardreport_override_checkbox).click()
                time.sleep(1)
            if kwargs['override_format']==False:
                status=self.driver.find_element(*RCAdvanceLocators.standardreport_override_checkbox).is_selected()
                utillity.UtillityMethods.asequal(self, True, status, "Step X: Verify Override format is checked previously.")
                self.driver.find_element(*RCAdvanceLocators.standardreport_override_checkbox).click()
                time.sleep(1)
    def create_wf_report_task_parameters(self, **kwargs): 
        """
        param wf_report_path: 'carinst'
        burst_report: True(Means we need to check) OR False(Means we need to uncheck)
        override_format: True(Means we need to check) OR False(Means we need to uncheck)
        Syntax: create_wf_report_task_general('Layout')
        @author = Niranjan
        """
    def create_wf_report_task_pre_post_procedure(self, **kwargs): 
        """
        param wf_report_path: 'carinst'
        burst_report: True(Means we need to check) OR False(Means we need to uncheck)
        override_format: True(Means we need to check) OR False(Means we need to uncheck)
        Syntax: create_wf_report_task_general('Layout')
        @author = Niranjan
        """
    def create_wf_report_task_advanced_options(self, **kwargs): 
        """
        param wf_report_path: 'carinst'
        burst_report: True(Means we need to check) OR False(Means we need to uncheck)
        override_format: True(Means we need to check) OR False(Means we need to uncheck)
        Syntax: create_wf_report_task_general('Layout')
        @author = Niranjan
        """
    def create_file_task(self, **kwargs): 
        """
        param file_name: The input file name along with the path
        Syntax: create_file_task('Layout')
        @author = Niranjan
        """
        if 'file_name' in kwargs:
            file_location=os.getcwd() + "\data\\" + kwargs['file_name']
            file_name_elem=self.driver.find_element(*RCAdvanceLocators.file_name)
            utillity.UtillityMethods.set_text_field_using_actionchains(self, file_name_elem, file_location)
            time.sleep(1)
            verify_save_report=self.driver.find_element(*RCAdvanceLocators.file_save_report_as_input).get_attribute("value").strip()
            utillity.UtillityMethods.asequal(self, kwargs['file_name'], verify_save_report, "Step X: Verify " + kwargs['file_name'] + "is displaying in save as report box..")
        if 'delete_file' in kwargs:
            self.driver.find_element(*RCAdvanceLocators.file_delete_the_file_checkbox).click()
    
    def create_url_task(self, **kwargs): 
        """
        param tab_name: 'Home' OR 'Data' OR 'Layout'....
        Syntax: create_url_task('Layout')
        @author = Niranjan
        """
        time.sleep(1)
        if 'user_id' in kwargs:
            user_id_elem=self.driver.find_element(*RCAdvanceLocators.url_user_id)
            password_btn_elem=self.driver.find_element(*RCAdvanceLocators.url_password_btn)
            self.set_task_password('eda', user_id_elem, password_btn_elem)
            time.sleep(1)
    
    def create_ftp_task(self, **kwargs): 
        """
        param server_name: 'edared30' 
        Syntax: create_ftp_task('Layout')
        @author = Niranjan
        """
        if 'server_name' in kwargs:
            server_name_elem=self.driver.find_element(*RCAdvanceLocators.ftp_server_name)
            if server_name_elem.get_attribute("value")=='':
                utillity.UtillityMethods.set_text_field_using_actionchains(self, server_name_elem, kwargs['server_name'])
                acount_id_elem=self.driver.find_element(*RCAdvanceLocators.ftp_account_name)
                password_btn_elem=self.driver.find_element(*RCAdvanceLocators.ftp_password_btn)
                self.set_task_password('eda', acount_id_elem, password_btn_elem)
                time.sleep(1)
            else:
                pass
        if 'file_name' in kwargs:
            file_location=os.getcwd() + "\data\\" + kwargs['file_name']
            file_name_elem=self.driver.find_element(*RCAdvanceLocators.ftp_file_name)
            utillity.UtillityMethods.set_text_field_using_actionchains(self, file_name_elem, file_location)
            time.sleep(1)
            verify_save_report=self.driver.find_element(*RCAdvanceLocators.ftp_save_report_as_input).get_attribute("value").strip()
            utillity.UtillityMethods.asequal(self, kwargs['file_name'], verify_save_report, "Step X: Verify " + kwargs['file_name'] + "is displaying in save as report box..") 
    
    def task_dialog_close(self, btn_type):
        """
        param btn_type: 'ok' OR 'cancel' 
        Syntax: task_dialog_close('ok')
        @author = Niranjan
        """
        button_name = "task_dialog_" + btn_type.lower()
        self.driver.find_element(*RCAdvanceLocators.__dict__[button_name]).click()
        time.sleep(2)
        self.verify_rc_grid_table('Enabled')
        
    def create_email_distribution_general(self, **kwargs): 
        """
        param type: 'Distribution List' OR 'Distribution File', OR 'Email Address(s)', OR 'Dynamic Distribution List'
        param to: To address
        param from: From Address
        param reply_address: Reply Address
        param subject: Subject of the email
        Syntax: create_email_distribution_general(type='Distribution List', to='xxx', from='xxx', reply_address='xxx', subject='xxx')
        @author = Niranjan
        """
        if 'type' in kwargs:
            type_elem=self.driver.find_element(*RCAdvanceLocators.email_type)
            utillity.UtillityMethods.select_any_combobox_item(self, type_elem, kwargs['type'])
            time.sleep(2)
        if 'to' in kwargs:
            to_elem=self.driver.find_element(*RCAdvanceLocators.email_to)
            utillity.UtillityMethods.set_text_field_using_actionchains(self, to_elem, kwargs['to'])
            time.sleep(1)
        if 'from' in kwargs:
            from_elem=self.driver.find_element(*RCAdvanceLocators.email_from)
            utillity.UtillityMethods.set_text_field_using_actionchains(self, from_elem, kwargs['from'])
            time.sleep(1)
        if 'reply_address' in kwargs:
            reply_elem=self.driver.find_element(*RCAdvanceLocators.email_reply_address)
            utillity.UtillityMethods.set_text_field_using_actionchains(self, reply_elem, kwargs['reply_address'])
            time.sleep(1)
        if 'subject' in kwargs:
            subject_elem=self.driver.find_element(*RCAdvanceLocators.email_subject)
            utillity.UtillityMethods.set_text_field_using_actionchains(self, subject_elem, kwargs['subject'])
            time.sleep(1)
    
    def create_email_distribution_options(self): 
        """
        param tab_name: 'Home' OR 'Data' OR 'Layout'....
        Syntax: create_email_distribution_options('Layout')
        @author = Niranjan
        """
        time.sleep(1)
            
    def create_ftp_distribution_general(self, **kwargs): 
        """
        param type: 'Distribution List' OR 'Distribution File', OR 'Single File', OR 'Dynamic Distribution List'
        param to: To address
        param from: From Address
        param reply_address: Reply Address
        param subject: Subject of the email
        Syntax: create_email_distribution_general(type='Distribution List', to='xxx', from='xxx', reply_address='xxx', subject='xxx')
        @author = Niranjan
        """
        if 'type' in kwargs:
            type_elem=self.driver.find_element(*RCAdvanceLocators.ftp_type)
            utillity.UtillityMethods.select_any_combobox_item(self, type_elem, kwargs['type'])
            time.sleep(2)
        if 'name_btn' in kwargs:
            self.driver.find_element(*RCAdvanceLocators.ftp_name_btn).click()
            time.sleep(2)
            utillity.UtillityMethods.select_item_from_ibfs_explorer_list(kwargs['name_btn'])
            time.sleep(1)
            selected_elem=self.driver.find_element(*RCAdvanceLocators.ftp_name_input).get_attribute("value").strip()
            verify_pat = bool(re.match(".*"+kwargs['name_btn']+"\.adr", selected_elem))
            utillity.UtillityMethods.asequal(self, True, verify_pat, "Step X: Verify the " + kwargs['name_btn'] + " is selected.")
        if 'name_input' in kwargs:
            name_input_elem=self.driver.find_element(*RCAdvanceLocators.ftp_name_input)
            utillity.UtillityMethods.set_text_field_using_actionchains(self, name_input_elem, kwargs['name_input_text'])
            time.sleep(1)
        if 'directory_input' in kwargs:
            name_input_elem=self.driver.find_element(*RCAdvanceLocators.ftp_directory_input)
            utillity.UtillityMethods.set_text_field_using_actionchains(self, name_input_elem, kwargs['directory_input'])
            time.sleep(1)
        if 'radio_selection' in kwargs:
            radio_elems=self.driver.find_elements(*RCAdvanceLocators.ftp_radio_input)
            radio_elems[[el.text.strip() for el in radio_elems].index(kwargs['radio_selection'])].click()
            time.sleep(1)
        if 'zip_file_input' in kwargs:
            name_input_elem=self.driver.find_element(*RCAdvanceLocators.ftp_zip_input)
            utillity.UtillityMethods.set_text_field_using_actionchains(self, name_input_elem, kwargs['zip_file_input'])
            time.sleep(1)
        if 'index_file_input' in kwargs:
            name_input_elem=self.driver.find_element(*RCAdvanceLocators.ftp_index_file_input)
            utillity.UtillityMethods.set_text_field_using_actionchains(self, name_input_elem, kwargs['index_file_input'])
            time.sleep(1)
                
    def create_ftp_distribution_options(self, **kwargs): 
        """
        param type: 'Distribution List' OR 'Distribution File', OR 'Email Address(s)', OR 'Dynamic Distribution List'
        param to: To address
        param from: From Address
        param reply_address: Reply Address
        param subject: Subject of the email
        Syntax: create_email_distribution_general(type='Distribution List', to='xxx', from='xxx', reply_address='xxx', subject='xxx')
        @author = Niranjan
        """
        time.sleep(1)
    
    
    def create_printer_distribution(self, **kwargs): 
        """
        param type='Distribution List'
        Syntax: create_printer_distribution('Layout')
        @author = Niranjan
        """
        if 'type' in kwargs:
            type_elem=self.driver.find_element(*RCAdvanceLocators.printer_type)
            utillity.UtillityMethods.select_any_combobox_item(self, type_elem, kwargs['type'])
            time.sleep(2)
        if 'name_btn' in kwargs:
            self.driver.find_element(*RCAdvanceLocators.printer_name_btn).click()
            time.sleep(2)
            utillity.UtillityMethods.select_item_from_ibfs_explorer_list(kwargs['name_btn'])
            time.sleep(1)
            selected_elem=self.driver.find_element(*RCAdvanceLocators.printer_name_input).get_attribute("value").strip()
            verify_pat = bool(re.match(".*"+kwargs['name_btn']+"\.adr", selected_elem))
            utillity.UtillityMethods.asequal(self, True, verify_pat, "Step X: Verify the " + kwargs['name_btn'] + " is selected.")
        if 'name_input' in kwargs:
            name_input_elem=self.driver.find_element(*RCAdvanceLocators.printer_name_input)
            utillity.UtillityMethods.set_text_field_using_actionchains(self, name_input_elem, kwargs['name_input_text'])
            time.sleep(1)
    
    def create_report_library_distribution_general(self, kwargs): 
        """
        param tab_name: 'Home' OR 'Data' OR 'Layout'....
        Syntax: create_report_library_distribution('Layout')
        @author = Niranjan
        """
        if 'radio_selection' in kwargs:
            radio_elems=self.driver.find_elements(*RCAdvanceLocators.library_radio_input)
            radio_elems[[el.text.strip() for el in radio_elems].index(kwargs['radio_selection'])].click()
            time.sleep(1)
        if 'access_list_btn' in kwargs:
            self.driver.find_element(*RCAdvanceLocators.library_access_list_btn).click()
            time.sleep(2)
            utillity.UtillityMethods.select_item_from_ibfs_explorer_list(kwargs['access_list_btn'])
            time.sleep(1)
            selected_elem=self.driver.find_element(*RCAdvanceLocators.library_access_list_input).get_attribute("value").strip()
            verify_pat = bool(re.match(".*"+kwargs['name_btn']+"\.adr", selected_elem))
            utillity.UtillityMethods.asequal(self, True, verify_pat, "Step X: Verify the " + kwargs['name_btn'] + " is selected.")

    def create_report_library_distribution_options(self): 
        """
        param tab_name: 'Home' OR 'Data' OR 'Layout'....
        Syntax: create_report_library_distribution('Layout')
        @author = Niranjan
        """
        time.sleep(1)
    def create_repository_distribution(self): 
        """
        param tab_name: 'Home' OR 'Data' OR 'Layout'....
        Syntax: create_repository_distribution('Layout')
        @author = Niranjan
        """
        time.sleep(1)
        
    def distribution_dialog_close(self, btn_type):
        """
        param btn_type: 'ok' OR 'cancel' 
        Syntax: distribution_dialog_close('ok')
        @author = Niranjan
        """
        button_name = "distribution_dialog_" + btn_type.lower()
        self.driver.find_element(*RCAdvanceLocators.__dict__[button_name]).click()
        time.sleep(2)
        self.verify_rc_grid_table('Enabled')
               
    def create_notification(self): 
        """
        param tab_name: 'Home' OR 'Data' OR 'Layout'....
        Syntax: create_notification('Layout')
        @author = Niranjan
        """
        time.sleep(1) 
        
    def verify_log_reports(self):
        """
        param tab_name: 'Home' OR 'Data' OR 'Layout'....
        Syntax: verify_log_reports('Layout')
        @author = Niranjan
        """
        time.sleep(1) 
