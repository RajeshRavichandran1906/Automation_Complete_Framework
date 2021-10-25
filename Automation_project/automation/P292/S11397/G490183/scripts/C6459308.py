'''
Created on Jul 2, 2019

@author:Vishnu_priya
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6459308
TestCase Name : Create, Edit and Run Document 
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.wf_mainpage import Wf_Mainpage,Run
from common.lib import utillity
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.login import Login
from common.wftools.page_designer import Design
from common.wftools.report import Report

class C6459308_TestClass(BaseTestCase):

    def test_C6459308(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        main_page = Wf_Mainpage(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        utils = utillity.UtillityMethods(self.driver)
        main_page_run = Run(self.driver)
        pd_design = Design(self.driver)
        docreport_obj = Report(self.driver)
        
        """
            TESTCASE CSS
        """
        content_css = "[class*='content-button'][data-ibxp-text='Content']>.ibx-label-text" 
        explorer_css = "div[class^='file-item file-item-published']"
        querypane_css = "#queryBoxColumn"
                
        """
            COMMON TEST CASE VARIABLES 
        """
        project_id  = core_utils.parseinitfile('project_id')
        suite_id    = core_utils.parseinitfile('suite_id')
        group_id    = core_utils.parseinitfile('group_id')
        repository_folder = 'Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        case_id = 'C6459308'
        DATA_SET_NAME1 = case_id + '_DataSet_01.xlsx'
        DATA_SET_NAME2 = case_id + '_DataSet_02.xlsx'
        DATA_SET_NAME3 = case_id + '_DataSet_03.xlsx'
        DATA_SET_NAME4 = case_id + '_DataSet_04.xlsx'
        
        '''
        1 : Login WF as domain developer
        '''
        login.invoke_home_page('mriddev', 'mrpassdev')
        utils.synchronize_with_visble_text(content_css, "Content", 60)
          
        '''
        2 : Click on Content view from side bar
        '''
        main_page.select_content_from_sidebar()
        
        '''
        3 : Expand 'P292_S11397' domain -> 'G490183' folder;
            Double click on 'Explorer Widget page'
        '''
        main_page.expand_repository_folder(repository_folder)
        utils.synchronize_with_visble_text(explorer_css, "Explorer", 30)
          
        pd_design.run_page_designer_by_double_click("Explorer Widget page")
        main_page_run.switch_to_frame()
        pd_design.switch_to_container_frame("Panel 1")
        utils.synchronize_with_visble_text(explorer_css, "Explorer", 30)
          
        '''
        4 : Click on Document action tile from under InfoAssist category;
        '''
        main_page.select_action_bar_tab("InfoAssist")
        main_page.select_action_bar_tabs_option("Document")
         
        '''
        5 : Select car.mas under ibisamp folder and Click open
        '''
        core_utils.switch_to_new_window()
        utils.select_masterfile_in_open_dialog('ibisamp', 'car')
         
        '''
        6 : Double click on 'CAR' from Dimensions and 'SALES' from Measures
        '''
        docreport_obj.double_click_on_datetree_item('CAR', 1)
        docreport_obj.wait_for_visible_text(querypane_css,'CAR')
        docreport_obj.double_click_on_datetree_item('SALES', 1)
        docreport_obj.wait_for_visible_text(querypane_css,'SALES')
         
        '''
        6.01 : Verify Live Preview appears as below
        '''
        docreport_obj.create_acrossreport_data_set_in_preview('TableChart_1', 1, 2, 10, 2, DATA_SET_NAME1)
        docreport_obj.verify_across_report_data_set_in_preview('TableChart_1', 1, 2, 10, 2, DATA_SET_NAME1,msg='Step 6.01: Verify data set')
         
        '''
        7 : Click Run
        '''
        docreport_obj.run_report_from_toptoolbar()
        docreport_obj.switch_to_frame()
         
        '''
        7.01 : Verify chart runs without any error as below
        '''
        docreport_obj.create_table_data_set('#IWindowBodyFTB_0_0', DATA_SET_NAME2)
        docreport_obj.verify_table_data_set('#IWindowBodyFTB_0_0', DATA_SET_NAME2,"Step 7.01 : Verify Document report")
        docreport_obj.verify_column_heading('.arGridColumnHeading','CAR   SALES',"Step 7.2")
         
        '''
        8 : Click save;       
            Enter title as 'Doc' and Click Save
        '''
        docreport_obj.switch_to_default_content()
        docreport_obj.save_report_from_toptoolbar()
        docreport_obj.save_file_in_save_dialog('Doc')
         
        '''
        9 : Close IA
        '''
        docreport_obj.select_visualization_application_menu_item('exit')
         
        '''
        9.01 : Verify 'Doc' is available under 'G490183' folder in content area as below
        '''
        core_utils.switch_to_previous_window(window_close=False)
        main_page_run.switch_to_default_content()
        main_page_run.switch_to_frame()
        pd_design.switch_to_container_frame("Panel 1")
        utils.synchronize_with_visble_text(explorer_css, "Explorer", 30)
        main_page.verify_items_in_grid_view(["Doc"], 'asin', "Step 9.01: Verify")
        
        '''
        10 : Double click on 'Doc' from content area
        '''
        main_page.double_click_on_content_area_items('Doc')
        
        '''
        10.01 : Verify 'Doc' runs from explorer widget page without any error as below
        '''
        main_page_run.switch_to_frame()
        docreport_obj.create_table_data_set('#IWindowBodyFTB_0_0', DATA_SET_NAME3)
        docreport_obj.verify_table_data_set('#IWindowBodyFTB_0_0', DATA_SET_NAME3,"Step 10.01 : Verify Document report")
        
        '''
        11 : Close document
        '''
        main_page_run.switch_to_default_content()
        main_page_run.switch_to_frame()
        pd_design.switch_to_container_frame("Panel 1")
        main_page_run.close()
         
        '''
        12 : Right click on 'Doc' and select Edit
        '''
        utils.synchronize_with_visble_text(explorer_css, "Explorer", 30)
        main_page.right_click_folder_item_and_select_menu("Doc", 'Edit')
        core_utils.switch_to_new_window()
        docreport_obj.wait_for_visible_text('#canvasContainer', "BMW")
        
        '''
        12.01 : Verify document opens in a new tab with the live preview canvas as below
        '''
        docreport_obj.create_acrossreport_data_set_in_preview('TableChart_1', 1, 2, 10, 2, DATA_SET_NAME4)
        docreport_obj.verify_across_report_data_set_in_preview('TableChart_1', 1, 2, 10, 2, DATA_SET_NAME4, msg='Step 12.01: Verify data set')
        
        '''
        13 : Click IA application main menu and click on Exit
        '''
        docreport_obj.select_visualization_application_menu_item('exit')
        core_utils.switch_to_previous_window(window_close=False)
        main_page_run.switch_to_default_content()
        main_page_run.switch_to_frame()
        pd_design.switch_to_container_frame("Panel 1")
        
        '''
        14 : Close the 'Explorer widget' page run window
        '''
        pd_design.switch_to_default_page()
        main_page_run.close()
        main_page_run.switch_to_default_content()
        utils.synchronize_with_visble_text(content_css, "Content", 60)
        
        '''
        14.01 : Verify 'Doc' is displayed under 'P292_S11397' domain -> 'G490183' folder in Home page
        '''
        self.driver.refresh()
        utils.synchronize_with_visble_text("#files-box-area", "Doc", 30)
        
        main_page.verify_items_in_grid_view(["Doc"], "asin", "Step 14.01 : Verify 'Doc' is displayed under 'P292_S11397' domain -> 'G490183' folder in Home page")
        
        '''
        15 : Sign Out WF
        '''
        main_page.signout_from_username_dropdown_menu()
 
if __name__ == '__main__':
    unittest.main() 