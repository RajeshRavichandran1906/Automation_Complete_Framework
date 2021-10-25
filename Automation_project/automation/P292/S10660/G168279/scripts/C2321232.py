'''
Created on Mar 22, 2017

@author: Robert

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2321232
Test case Name =  Verify the expected qualified NAME is displayed while setting is "Use field titles" and MFD does not have titles
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, visualization_metadata, define_compute
from common.lib import utillity 
import time
from common.lib.basetestcase import BaseTestCase
from common.wftools.report import Report
from common.lib.core_utility import CoreUtillityMethods

class C2321232_TestClass(BaseTestCase):

    def test_C2321232(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        defcomp=define_compute.Define_Compute(self.driver)
        report = Report(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = "C2321232"
        query_tree_css = "#queryTreeColumn"

        
        """    1. Launch IA Report mode using car.mas,    """
        utillobj.infoassist_api_login('report','ibisamp/car','P292/S10660_infoassist_2', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)  
          
        '''    2. Double click field "SALES"    '''
        metaobj.datatree_field_click("SALES", 2, 1)
        report.wait_for_visible_text(query_tree_css, "SALES")
        
        
        """    3. Select the Data Tab > Click "Detail(Define)"   """
        
        
        defcomp.invoke_define_compute_dialog('define')
        elem1="#fname"
        resultobj.wait_for_property(elem1, expected_number=1, expire_time=20)
        
        '''    4. Click on the "Additional Options" button, Verify "Use Field Titles" is displayed and selected by default,    '''
        '''    5. Double-click "COUNTRY", Verify Define text area displays the qualified NAME "CAR.ORIGIN.COUNTRY "    '''
        '''    6. Change the Format to A50V > Click OK    '''
        settings_btn=self.driver.find_element_by_css_selector("div[id='defineMetaData'] div[id^='BiToolBarMenuButton'] img[src*='settings']")
        utillobj.default_left_click(object_locator=settings_btn)
        utillobj.select_or_verify_bipop_menu(verify='true', expected_popup_list=['Use field titles', 'Preserve null value', 'Missing Values'], expected_ticked_list=['Use field titles'], msg='Step 04:01 Verify popup menu')
        utillobj.default_left_click(object_locator=settings_btn)
        time.sleep(8)
        defcomp.enter_define_compute_parameter("Define_1", 'A50V', 'Dimensions->COUNTRY', 1)
        time.sleep(10)
        textarea=self.driver.find_element_by_css_selector("div[id^='QbDialog'] [class*='active'] #fldCreatorSplitPane #ftext")
        txtele=textarea.get_attribute("value").strip()
        deftxt='CAR.ORIGIN.COUNTRY'
        utillobj.asequal(txtele,deftxt, 'Step 5. Verify Define Field Text in textarea')
        
        ok_button_obj = utillobj.validate_and_get_webdriver_object("#fldCreatorOkBtn", "Ok button css")
        core_utils.python_left_click(ok_button_obj)
        report.wait_for_visible_text("#iaMetaDataBrowser", "Define_1")
        
        '''   7. Double click on "Define_1" in data pane, Verify Data pane, Query pane, and Live Preview,    '''
        
        metaobj.datatree_field_click("Dimensions->Define_1", 2, 1)
        report.wait_for_visible_text(query_tree_css, "Define_1")
        
        define_obj = utillobj.validate_and_get_webdriver_object("#queryTreeColumn  table  tbody tr:nth-child(5)", "define_1 css")
        actual_result = define_obj.is_displayed()
        msg = "Step 07 : Verify Data pane, Query pane, and Live Preview,"
        utillobj.asequal(True, actual_result, msg)
        
        coln_list = ['Define_1', 'SALES']
        resultobj.verify_report_titles_on_preview(2, 2, "TableChart_1", coln_list, "Step 07: Verify the following report is displayed")
        
        '''    8. Click "Save" in the toolbar    '''
        '''    9. Save As "C2321232" > Click Save    '''

        time.sleep(5)
        
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        '''    10. Logout:    '''
        '''    11. Reopen the saved fex:    '''
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10660_infoassist_2',mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        
        coln_list = ['Define_1', 'SALES']
        resultobj.verify_report_titles_on_preview(2, 2, "TableChart_1", coln_list, "Step 11: Verify Live preview titles")
        
        '''    12. Right-click "Define_1" in the Data pane > Edit...    '''
        '''    12.1 Verify field Title is displayed in the Text area    '''
        '''    13. Click Cancel    '''
        '''    14. Logout:    '''
        metaobj.datatree_field_click("Dimensions->Define_1", 1, 1, 'Edit...')
        resultobj.wait_for_property("div[id^='QbDialog']", expected_number=1, expire_time=20)
        utillobj.asequal(txtele,deftxt, 'Step 12.1 Verify Define Field Text in textarea')
           
        cancel_obj = utillobj.validate_and_get_webdriver_object("#fldCreatorCancelBtn", "Cancel button css")
        core_utils.python_left_click(cancel_obj)
        utillobj.infoassist_api_logout()
    
if __name__ == '__main__':
    unittest.main()