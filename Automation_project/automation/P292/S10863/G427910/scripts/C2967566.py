'''
Created on May 11, 2018

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10863
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5751691
TestCase Name = Verify report with Title Popup, Accordion, Repeat Sort Value, Stack Measures
'''

import unittest, time
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase

class C2967566_TestClass(BaseTestCase):

    def test_C2967566(self):
        
        TestCase_ID = "C2967566"
        driver=self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_runobj=ia_run.IA_Run(self.driver)
        
        """
        Step 01: Launch IA Report mode:http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/GGSALES&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """         
        utillobj.invoke_infoassist_api_login('report','ibisamp/car','P292_S10863/G427910', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
         
        """
        Step 02: Add fields: country, car, model, bodytype, retail_cost, dealer_cost, sales
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
        Step 05: Run > Verify output
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
        Step 07: Verify output
        """
#         ia_runobj.create_table_data_set("table#treetable",TestCase_ID+'_Ds02.xlsx') 
        ia_runobj.verify_table_data_set("table#treetable",TestCase_ID+"_Ds02.xlsx", 'Step 07: Verify the report is displayed.')
        utillobj.switch_to_default_content(pause=3)
        time.sleep(5)
        
        """
        Step 08: Select Save > Save as "C2967566" > Save
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(TestCase_ID)
        time.sleep(3)
        
        """
        Step 09: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
        Step 10: Restore the saved Fex:
        http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/S10863/C2967566.fex&tool=Report
        """
        utillobj.infoassist_api_edit_(TestCase_ID,'Report','P292_S10863/G427910',mrid='mrid',mrpass='mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """
        Step 11: Select Format Tab > Verify Accordion remains enabled
        """
        elem=self.driver.find_element_by_css_selector("#FormatTab_tabButton")
        utillobj.click_on_screen(elem, 'middle', click_type=0)
        time.sleep(5)        
        elem=driver.find_element_by_css_selector("#FormatAccordion")
        utillobj.verify_checked_class_property(elem, "Step 11: Verify Accordion remains enabled", check_property=True)
        
        """
        Step 12: Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()