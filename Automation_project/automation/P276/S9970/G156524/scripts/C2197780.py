'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2197780
TestCase Name = Test that Auto Drill works with Table of Contents option
'''
import unittest
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase
from selenium.common.exceptions import NoSuchElementException
from common.pages import visualization_ribbon, ia_run, visualization_metadata

class C2197780_TestClass(BaseTestCase):
    
    def test_C2197780(self):
        
        """
        TESTCASE OBJECTS
        """
        iarun = ia_run.IA_Run(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
       
        """
        TESTCASE VARIABLES
        """ 
        Test_ID="C2197780"
        browser_type=utillobj.parseinitfile('browser')
        Test_Case_ID = Test_ID+"_"+browser_type
        
        """    
            STEP 01 : Launch the IA report API with wf_retail_lite    
        """
        utillobj.infoassist_api_login('report','basapp/wf_retail_lite','P276/S9970', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#queryTreeColumn", 'Sum', 250)
        
        """    
            STEP 02 : Add Quantity,Sold to Sum and Store,Business,Region to By     
        """
        metaobj.datatree_field_click("Store,Business,Region", 2, 1)
        utillobj.synchronize_with_visble_text("div[class^='x']", 'Store', 60)
        
        metaobj.datatree_field_click("Quantity,Sold", 2, 1)
        utillobj.synchronize_with_number_of_element("div[class^='x']", 14, 60)
        
        """    
            STEP 03 : Click RUN     
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.synchronize_with_number_of_element("[id^='ReportIframe']", 1, 20)
        utillobj.switch_to_frame(pause=2)
        
        """
            STEP 03.1 : See no Auto Drill links since we did not select Format > Auto Drill
        """
        try:
            status=self.driver.find_element_by_css_selector("table[summary='Summary'] > tbody > tr:nth-child(3) > td:nth-child(1) > a").is_displayed()
        except NoSuchElementException:
            status=False
        utillobj.asequal(False, status, "Step 03.01: No links displayed")
        
        #iarun.create_table_data_set("[summary= 'Summary']", Test_ID+"_Ds01.xlsx")
        iarun.verify_table_data_set("[summary= 'Summary']", Test_ID+"_Ds01.xlsx", "Step 03.02: Verify dataset")
        utillobj.switch_to_default_content()
        
        """    
            STEP 04 : Click IA > Save As> Type C2197780 > click Save    
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """    
            STEP 05 : Logout of the IA API using the following URL.    
        """
        utillobj.infoassist_api_logout()
        
        """    
            STEP 06 : Run this test from a new browser window using the following url:    
        """
        setup_url_head = utillobj.get_setup_url()
        setup_url=setup_url_head.replace('home8206','')
        project_id=utillobj.parseinitfile('project_id')
        folder=utillobj.parseinitfile('suite_id') 
        api_url = setup_url + 'ia?is508=false&item=IBFS%3A%2FWFC%2FRepository%2F' + project_id + "/" + folder + '%2F' + Test_Case_ID + '.fex&tool=run'
        print(api_url)
        self.driver.get(api_url)
        utillobj.login_wf('mrid','mrpass')
        utillobj.synchronize_with_number_of_element("iframe[src]", 1, 60)
        utillobj.switch_to_frame(1, frame_css='iframe[src]',frame_height_value=0)
        utillobj.synchronize_with_visble_text("table[summary='Summary']>tbody>tr:nth-child(2)>td:nth-child(1)", 'EMEA', 60)
        
        """
            STEP 06.1 : This time you will see Auto Drill links in the report
        """
        try:
            status=self.driver.find_element_by_css_selector("table[summary='Summary'] > tbody > tr:nth-child(3) > td:nth-child(1) > a").is_displayed()
        except NoSuchElementException:
            status=False
        utillobj.asequal(True, status, "Step 06.01: Verify Links displayed")
        iarun.verify_table_data_set("[summary= 'Summary']", Test_ID+"_Ds01.xlsx", "Step 06.02: Verify dataset")
        
        """    
            STEP 07 : Click on North America and select Drill down to Store Business Sub Region to prove that the drill down works.    
        """
        iarun.select_report_autolink_tooltip("table[summary='Summary']",3,1,'Drill down to Store Business Sub Region')
        utillobj.synchronize_with_visble_text("table[summary='Summary'] span[class*='x3']>a", 'Home', 40)
        
        """
            STEP 07.1 : Verify output
        """
        #iarun.create_table_data_set("[summary= 'Summary']", Test_ID+"_Ds02.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds02.xlsx", "Step 07.01: Verify drill down dataset")  
               
        """    
            STEP 08 : Close the browser window    
        """
        
if __name__ == '__main__':
    unittest.main()