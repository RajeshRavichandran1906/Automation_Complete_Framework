'''
Created on 08-NOV-2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227552
TestCase Name = Verify promoting HOLD file to Document mode
'''
import unittest
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2227552_TestClass(BaseTestCase):

    def test_C2227552(self):
        
        Test_Case_ID = "C2227552"
        driver = self.driver
        driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        browser=utillobj.parseinitfile('browser')
        
        """ 1. Launch the IA API with CAR, Report mode:    """
        utillobj.infoassist_api_login('report','ibisamp/car','P137/S7385', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """ 2. Double click "COUNTRY", "CAR", "DEALER_COST", "RETAIL_COST".     """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("CAR", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("DEALER_COST", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("RETAIL_COST", 2, 1)
        
        """ 3. Verify the following report is displayed.       """
        coln_list = ['COUNTRY', 'CAR' ,'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 3: Verify column titles")
        time.sleep(4)
        ia_resultobj.verify_report_data_set('TableChart_1', 9, 4, 'C2227552_Ds01.xlsx', 'Step 3.1: Verify report dataset', no_of_cells=4)
        
        """ 4. Select "Home" > "File" button      """
        time.sleep(2)
        ribbonobj.select_ribbon_item('Home', 'File')
        
        """ 5. Save with Default file name "File1"   """
        """ 6. File type as Binary (*.ftm)            """
        """ 7. Click Save                            """
        time.sleep(2)
        utillobj.ibfs_save_as("File1", "Binary (*.ftm)")
        
        """ 8. Notice "Create Report" button at the bottom of report.    """
        btn_css='#createFromHoldButton #createFromHoldMenuBtn'
        bol=driver.find_element_by_css_selector(btn_css).is_displayed()
        utillobj.asequal(True, bol, "Step 8: Verify 'Create Report' button at the bottom of report ")
        
        """ 9. Click on the Create Report to create hold report.    """
        ia_resultobj.create_hold_type('Create Report')
        
        """ 10. Click "Home" Tab > "Document".                      """
        ribbonobj.select_ribbon_item('Home', 'Document') 
        time.sleep(5) 
             
        """ 11. Click Active Report dropdown > Select PDF        """
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        ribbonobj.change_output_format_type('pdf', 'Home')
        
        """ 12. Click on the canvas.                             """
        time.sleep(2)
        driver.find_element_by_id('TableChart_1').click()
        
        """ 13. Double click "COUNTRY", "CAR", "DEALER_COST".    """
        time.sleep(2)
        metaobj.datatree_field_click('COUNTRY', 2, 1)
        time.sleep(8)
        metaobj.datatree_field_click('CAR', 2, 1)
        time.sleep(8)
        metaobj.datatree_field_click('DEALER_COST', 2, 1)
        time.sleep(8)
        
        """ 14. Verify the following report is displayed.        """
        coln_list = ['COUNTRY', 'CAR' ,'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 14.1: Verify column titles")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 3, 'C2227552_Ds02.xlsx', 'Step 14.2: Verify report dataset', no_of_cells=3)
        
        """ 15. Click "Run".                    """
        ribbonobj.select_tool_menu_item('menu_run')
        
        """ 16. Verify the report is displayed. """
        ele=self.driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step16' + "_" + browser, image_type='actual',x=125, y=30, w=-360, h=-300)
        time.sleep(8)
        driver.find_element_by_css_selector("#resultArea div[class$='window-close-button']").click()
        time.sleep(8)
        
        """ 17. Click "IA" > "Save".             """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(4)
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
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        utillobj.login_wf('mrid', 'mrpass')
        time.sleep(2)
        utillobj.infoassist_api_edit(Test_Case_ID, 'document', 'S7385')
        
        """ 22. Verify "Hold"Report is preserved        """
        time.sleep(10)
        elem1=(By.CSS_SELECTOR, "#theCanvas")
        resultobj._validate_page(elem1)
        metaobj.verify_data_pane_field('Dimensions', 'COUNTRY', 1, 'Step: 22.a.1')
        metaobj.verify_data_pane_field('Dimensions', 'CAR', 2, 'Step: 22.a.2')
        metaobj.verify_data_pane_field('Measures/Properties', 'DEALER_COST', 1, 'Step: 22.b.1')
        metaobj.verify_data_pane_field('Measures/Properties', 'RETAIL_COST', 2, 'Step: 22.b.1')
        time.sleep(5)
        metaobj.verify_query_pane_field('Files', 'File1 (car)', 1, 'Step 22.c')
        coln_list = ['COUNTRY', 'CAR' ,'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 22.d: Verify column titles")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 3, 'C2227552_Ds02.xlsx', 'Step 22.e: Verify report dataset', no_of_cells=3)
        time.sleep(2)
        
if __name__ == '__main__':
    unittest.main()