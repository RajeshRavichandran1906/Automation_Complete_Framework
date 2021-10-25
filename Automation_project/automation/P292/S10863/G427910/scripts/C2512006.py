'''
Created on May 11, 2018

@author: qaauto

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10863
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2512006
TestCase Name = Verify HFREEZE-SCROLLHEIGHT=AUTO
'''
 
import unittest, time
from common.lib import utillity, javascript
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea

class C2512006_TestClass(BaseTestCase):
    
    def test_C2512006(self):
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = "C2512006"
        
        """
            TESTCASE OBJECTS
        """
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        javascriptobj = javascript.JavaScript(self.driver)
        iaresult= ia_resultarea.IA_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
                
        """1. Launch API with report ggsales """
        utillobj.invoke_infoassist_api_login('report','ibisamp/ggsales','P292_S10863/G427910','mrid','mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
         
        """2. Add fields DATE,PRODUCT,UNIT SALES"""
        metaobj.datatree_field_click('Date',2,1)
        query_css="#queryTreeWindow"
        resultobj.wait_for_property(query_css, 1,expire_time=25, string_value='Date', with_regular_exprestion=True)
        metaobj.datatree_field_click('Product',2,1)
        resultobj.wait_for_property(query_css, 1,expire_time=25, string_value='Product', with_regular_exprestion=True)
        metaobj.datatree_field_click('Unit Sales',2,1)
        resultobj.wait_for_property(query_css, 1,expire_time=25, string_value='UnitSales', with_regular_exprestion=True)
         
        """3. Select "Format">"Freeze" button """
        ribbonobj.select_ribbon_item("Format", "freeze")
        time.sleep(2)
         
        """ 4.select Run """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        parent_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
         
        """5.Verify user is able to scroll to the bottom of the report"""
        parent_css="#freezeTableName1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        ele=driver.find_element_by_css_selector('div.scrollDiv')
        utillobj.click_on_screen(ele, "middle")
        utillobj.mouse_scroll("down", 45,"uiautomation")
        time.sleep(5)
        javascriptobj.check_scroll_is_completed('div.scrollDiv')
        utillobj.switch_to_default_content(pause=3)
        time.sleep(10)
         
        """6. Select View Source """
        """7.verify Expected syntax"""
        expected_syntax_list=["HFREEZE=ON, SCROLLHEIGHT=AUTO, $"]
        iaresult.verify_fexcode_syntax(expected_syntax_list,'Step 07.01: verify Expected syntax')
         
        """ 8.Select Save > Save as "C2512006" > Save"""
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
         
        """ 9.Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp"""
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """10. Reopen the saved Fex:http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/S10863/C2512006.fex&tool=Report"""
        utillobj.infoassist_api_edit_(Test_Case_ID,'Report','P292_S10863/G427910',mrid='mrid',mrpass='mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """11. verify freeze tab is enabled"""
        ribbonobj.switch_ia_tab('Format')
        selected=self.driver.find_element_by_css_selector("#FormatReportFreeze")
        utillobj.verify_checked_class_property(selected, "Step 11.01: verify freeze tab is enabled", check_property=True)
        
        """ 12.logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp"""
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """13.Run from saved fex from Resources tree using below API link:
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/S10863&BIP_item=C2512006.fex
        """
        utillobj.active_run_fex_api_login_('C2512006.fex', 'S10863_infoassist_1','mrid','mrpass')
        parent_css="#freezeTableName1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        ele=driver.find_element_by_css_selector('div.scrollDiv,table[style$="fixed"]')
        utillobj.click_on_screen(ele, "middle")
        utillobj.mouse_scroll("down", 45,"uiautomation")
        time.sleep(2)
        javascriptobj.check_scroll_is_completed('div.scrollDiv')
        
        """14.http://machine:port/ibi_apps/service/wf_security_logout.jsp"""

if __name__ == "__main__":
    unittest.main()