'''
Created on 08-NOV-2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227552
TestCase Name = Verify promoting HOLD file to Document mode
'''
import unittest
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea
from common.lib import utillity, core_utility 
import time
from common.lib.basetestcase import BaseTestCase

class C2227552_TestClass(BaseTestCase):

    def test_C2227552(self):
        
        Test_Case_ID = "C2227552"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        core_utilobj = core_utility.CoreUtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        browser=utillobj.parseinitfile('browser')
        
        """ 1. Launch the IA API with CAR, Report mode:    """
        utillobj.infoassist_api_login('report','ibisamp/car','P137/S7385', 'mrid', 'mrpass')
        utillobj.synchronize_until_element_is_visible("#TableChart_1", metaobj.chart_long_timesleep)
        
        """ 2. Double click "COUNTRY", "CAR", "DEALER_COST", "RETAIL_COST".     """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_1", 'COUNTRY', metaobj.chart_long_timesleep)
        metaobj.datatree_field_click("CAR", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_1", 'CAR', metaobj.chart_long_timesleep)
        metaobj.datatree_field_click("DEALER_COST", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_1", 'DEALER_COST', metaobj.chart_long_timesleep)
        metaobj.datatree_field_click("RETAIL_COST", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_1", 'RETAIL_COST', metaobj.chart_long_timesleep)
        
        """ 3. Verify the following report is displayed.       """
        coln_list = ['COUNTRY', 'CAR' ,'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 03.00: Verify column titles")
        ia_resultobj.verify_report_data_set('TableChart_1', 9, 4, 'C2227552_Ds01.xlsx', 'Step 03.01: Verify report dataset', no_of_cells=4)
        
        """ 4. Select "Home" > "File" button      """
        ribbonobj.select_ribbon_item('Home', 'File')
        
        """ 5. Save with Default file name "File1"   """
        """ 6. File type as Binary (*.ftm)            """
        """ 7. Click Save                            """
        utillobj.synchronize_until_element_is_visible("#IbfsOpenFileDialog7_cbFileName input", metaobj.home_page_short_timesleep)
        utillobj.ibfs_save_as("File1", "Binary (*.ftm)")
        utillobj.synchronize_until_element_is_visible("#createFromHoldButton #createFromHoldMenuBtn", metaobj.home_page_medium_timesleep)
        
        """ 8. Notice "Create Report" button at the bottom of report.    """
        btn_css='#createFromHoldButton #createFromHoldMenuBtn'
        bol=driver.find_element_by_css_selector(btn_css).is_displayed()
        utillobj.asequal(True, bol, "Step 08.00: Verify 'Create Report' button at the bottom of report ")
        
        """ 9. Click on the Create Report to create hold report.    """
        ia_resultobj.create_hold_type('Create Report')
        
        """ 10. Click "Home" Tab > "Document".                      """
        ribbonobj.select_ribbon_item('Home', 'Document') 
             
        """ 11. Click Active Report dropdown > Select PDF        """
        utillobj.synchronize_until_element_is_visible("#theCanvas", metaobj.chart_long_timesleep)
        ribbonobj.change_output_format_type('pdf', 'Home')
        
        """ 12. Click on the canvas.                             """
        time.sleep(2)
        core_utilobj.left_click(driver.find_element_by_id('TableChart_2'))
        
        """ 13. Double click "COUNTRY", "CAR", "DEALER_COST".    """
        metaobj.datatree_field_click('Dimensions->COUNTRY', 2, 1)
        utillobj.synchronize_with_visble_text('#TableChart_2', 'COUNTRY', metaobj.chart_long_timesleep)
        metaobj.datatree_field_click('Dimensions->CAR', 2, 1)
        utillobj.synchronize_with_visble_text('#TableChart_2', 'CAR', metaobj.chart_long_timesleep)
        metaobj.datatree_field_click('Measures/Properties->DEALER_COST', 2, 1)
        utillobj.synchronize_with_visble_text('#TableChart_2', 'DEALER_COST', metaobj.chart_long_timesleep)
        
        """ 14. Verify the following report is displayed.        """
        coln_list = ['COUNTRY', 'CAR' ,'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_2", coln_list, "Step 14.01: Verify column titles")
        ia_resultobj.verify_report_data_set('TableChart_2', 10, 3, 'C2227552_Ds02.xlsx', 'Step 14.02: Verify report dataset', no_of_cells=3)
        
        """ 15. Click "Run".                    """
        ribbonobj.select_tool_menu_item('menu_run')
        utillobj.synchronize_until_element_is_visible("#resultArea div[class$='window-content-pane']", metaobj.chart_long_timesleep)
        
        """ 16. Verify the report is displayed. """
        ele=self.driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step16' + "_" + browser, image_type='actual',x=125, y=30, w=-360, h=-300)
        utillobj.synchronize_until_element_is_visible("#resultArea div[class$='window-close-button']", metaobj.home_page_medium_timesleep)
        core_utilobj.left_click(driver.find_element_by_css_selector("#resultArea div[class$='window-close-button']"))
        
        """ 17. Click "IA" > "Save".             """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        
        """ 18. Enter Title = "C2227552".        """
        """ 19. Click "Save".                    """
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        ribbonobj.select_tool_menu_item('close')
        time.sleep(3)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID+"_report")
        
        """ 20. Logout: 'http://machine:port/ibi_apps/service/wf_security_logout.jsp'    """
        time.sleep(2)
        utillobj.infoassist_api_logout()
        
        """ 21. Reopen fex using IA API: 'http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS7385%2FC2227552.fex&tool=document'    """
        utillobj.infoassist_api_edit(Test_Case_ID, 'document', 'S7385', mrid='mrid', mrpass='mrpass')
        
        """ 22. Verify "Hold"Report is preserved        """
        utillobj.synchronize_with_visble_text("#TableChart_2", 'DEALER_COST', metaobj.chart_long_timesleep)
        metaobj.verify_data_pane_field('Dimensions', 'COUNTRY', 1, 'Step: 22.00')
        metaobj.verify_data_pane_field('Dimensions', 'CAR', 2, 'Step: 22.01')
        metaobj.verify_data_pane_field('Measures/Properties', 'DEALER_COST', 1, 'Step: 22.02')
        metaobj.verify_data_pane_field('Measures/Properties', 'RETAIL_COST', 2, 'Step: 22.03')
        metaobj.verify_query_pane_field('Files', 'File1 (car)', 1, 'Step 22.04')
        coln_list = ['COUNTRY', 'CAR' ,'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_2", coln_list, "Step 22.05: Verify column titles")
        ia_resultobj.verify_report_data_set('TableChart_2', 10, 3, 'C2227552_Ds02.xlsx', 'Step 22.06: Verify report dataset', no_of_cells=3)
        time.sleep(2)
        
if __name__ == '__main__':
    unittest.main()