'''
Created on Aug 28, 2018

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/18161
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6668198
TestCase Name = Verify new Accordion Report
'''

import unittest, time
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase

class C6668198_TestClass(BaseTestCase):

    def test_C6668198(self):
        
        TestCase_ID = "C6668198"
        driver=self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_runobj=ia_run.IA_Run(self.driver)
        
        """
        Step 01: Launch Report with CAR: http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/car&item=IBFS:/WFC/Repository/P292_S11397/G513048
        """         
        utillobj.invoke_infoassist_api_login('report','ibisamp/car','P292_S18161/G513117', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
         
        """
        Step 02: Double click fields country, car, model, bodytype, retail_cost, dealer_cost, sales
        """
        metaobj.datatree_field_click('COUNTRY', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(4) td"
        resultobj.wait_for_property(parent_css, 1,expire_time=25, string_value='COUNTRY', with_regular_exprestion=True)
        metaobj.datatree_field_click('CAR', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(5) td"
        resultobj.wait_for_property(parent_css, 1,expire_time=25, string_value='CAR', with_regular_exprestion=True)
        metaobj.datatree_field_click('MODEL', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(6) td"
        resultobj.wait_for_property(parent_css, 1,expire_time=25, string_value='MODEL', with_regular_exprestion=True)
        metaobj.datatree_field_click('BODYTYPE', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(7) td"
        resultobj.wait_for_property(parent_css, 1,expire_time=25, string_value='BODYTYPE', with_regular_exprestion=True)
        metaobj.datatree_field_click('RETAIL_COST', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(3) td"
        resultobj.wait_for_property(parent_css, 1,expire_time=25, string_value='RETAIL_COST', with_regular_exprestion=True)
        metaobj.datatree_field_click('DEALER_COST', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(4) td"
        resultobj.wait_for_property(parent_css, 1,expire_time=25, string_value='DEALER_COST', with_regular_exprestion=True)
        metaobj.datatree_field_click('SALES', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(5) td"
        resultobj.wait_for_property(parent_css, 1,expire_time=25, string_value='SALES', with_regular_exprestion=True)
         
        """
        Step 03: Select Format Tab > Accordion
        """
        ribbonobj.select_ribbon_item('Format','accordion')
        time.sleep(3)
        
        """
        Step 04: Select View Source > Verify syntax and close window
        ON TABLE SET EXPANDABLE ON
        ON TABLE SET EXPANDBYROWTREE ON
        ON TABLE SET DROPBLNKLINE ON
        """
        expected_syntax_list=["ON TABLE SET EXPANDABLE ON","ON TABLE SET EXPANDBYROWTREE ON", "ON TABLE SET DROPBLNKLINE ON"]
        ia_resultobj.verify_fexcode_syntax(expected_syntax_list,'Step 04: Verify syntax')
        
        """
        Step 05: Click Run from toolbar
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
         
        """
        Verify output
        """
#         ia_runobj.create_table_data_set("table#treetable",TestCase_ID+'_Ds01.xlsx') 
        ia_runobj.verify_table_data_set("table#treetable",TestCase_ID+"_Ds01.xlsx", 'Step 05: Verify the run report is displayed.')      
         
        """
        Step 06: Expand ENGLAND > JAGUAR > V12XKE AUTO
        """
        elem=self.driver.find_element_by_css_selector("#divTreeTable tr[data-tt-id='1'] a[href]")
        utillobj.click_on_screen(elem, 'middle', click_type=0)
        time.sleep(3)
        elem=self.driver.find_element_by_css_selector("#divTreeTable tr[data-tt-id='1-1'] a[href]")
        utillobj.click_on_screen(elem, 'middle', click_type=0)
        time.sleep(3)
        elem=self.driver.find_element_by_css_selector("#divTreeTable tr[data-tt-id='1-1-1'] a[href]")
        utillobj.click_on_screen(elem, 'middle', click_type=0)
        time.sleep(3)
        
        """
        Verify output
        """
#         ia_runobj.create_table_data_set("table#treetable",TestCase_ID+'_Ds02.xlsx') 
        ia_runobj.verify_table_data_set("table#treetable",TestCase_ID+"_Ds02.xlsx", 'Step 06: Verify the report is displayed.')
        time.sleep(8)
        ele=driver.find_element_by_css_selector("div[id*='divTreeTable']")
        utillobj.take_screenshot(ele,TestCase_ID+'_Actual_step06', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 07: Close output window
        Step 08: Click Save from toolbar
        Step 09: Enter "C6668198" and click save from Save As dialog
        """
        utillobj.switch_to_default_content(pause=3)
        time.sleep(5)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(TestCase_ID)
        time.sleep(3)
        
        """
        Step 10: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
        Step 11: Restore the saved Fex
        http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/P292_S18161/G513048/C6668198.fex&tool=Report
        """
        utillobj.infoassist_api_edit_(TestCase_ID,'report','P292_S18161/G513117',mrid='mrid',mrpass='mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """
        Step 12: Select Format Tab > Verify Accordion remains enabled
        """
        elem=self.driver.find_element_by_css_selector("#FormatTab_tabButton")
        utillobj.click_on_screen(elem, 'middle', click_type=0)
        time.sleep(5)        
        elem=driver.find_element_by_css_selector("#FormatAccordion")
        utillobj.verify_checked_class_property(elem, "Step 12: Verify Accordion remains enabled", check_property=True)
        
        """
        Step 13: Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()