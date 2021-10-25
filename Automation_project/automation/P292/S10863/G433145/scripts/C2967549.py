'''
Created on May 14, 2018

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10863
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2967549
TestCase Name = Verify enabling Adaptive Dashboard 
'''

import unittest, time
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, active_miscelaneous
 
class C2967549_TestClass(BaseTestCase):
    
    def test_C2967549(self):
        
        """
            Testcase Variable
        """
        Test_Case_ID = "C2967549"
        
        """
            Class & Objects
        """
        utillobj = utillity.UtillityMethods(self.driver)
        iaresult= ia_resultarea.IA_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        
        """
        Step 01: Launch Document with CAR: http://machine:port/ibi_apps/ia?tool=Document&master=ibisamp/car&item=IBFS:/WFC/Repository/S10863
        """
        utillobj.invoke_infoassist_api_login('document','ibisamp/car','P292_S10863/G433145','mrid','mrpass')
        parent_css="#applicationButton img"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
         
        """
        Step 02: Add fields: country, sales
        """
        metaobj.datatree_field_click('COUNTRY',2,1)
        query_css="#queryTreeWindow"
        resultobj.wait_for_property(query_css, 1,expire_time=25, string_value='COUNTRY', with_regular_exprestion=True)
        metaobj.datatree_field_click('SALES',2,1)
        resultobj.wait_for_property(query_css, 1,expire_time=25, string_value='SALES', with_regular_exprestion=True)
         
        """
        Step 03: Select Layout Tab > Adaptive Dashboard 
        """
        ribbonobj.select_ribbon_item("Layout", "active_dashboard")
        time.sleep(2)
        
        """
        Step 04: Select View Source > Verify syntax
        ARJSONOPTIONS='{"arDisplayMode": "adaptive"}'
        """
        expected_syntax_list=['''SECTION=Section_1, LAYOUT=ON, PAGESIZE=LETTER, ORIENTATION=LANDSCAPE, SHOW_GLOBALFILTER=OFF, ACTIVE_UNITS=PTS, PAGECOLOR=RGB(255 255 255), ARJSONOPTIONS='{"arDisplayMode": "adaptive"}', $''']
        iaresult.verify_fexcode_syntax(expected_syntax_list,'Step 04.01: verify Expected syntax')
        
        """
        Step 05: Select Save > Save as "C2967549" > Save
        """
        utillobj.switch_to_default_content(pause=3)
        time.sleep(4)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """
        Step 06: Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
        """
        Step 07:Restore saved Fex: http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/S10863/C2967549.fex&tool=Report 
        """
        time.sleep(5)
        utillobj.infoassist_api_edit_(Test_Case_ID, 'document', 'P292_S10863/G433145',mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """
        Step 08:Select Layout Tab > Adaptive Dashboard > Verify button remains enabled
        """
        ribbonobj.switch_ia_tab('Layout')
        selected=self.driver.find_element_by_css_selector("#LayoutAdaptiveDashboard")
        utillobj.verify_checked_class_property(selected, "Step 08.01: verify Adaptive Dashboard is enabled", check_property=True)
        
        """ 
        Step 09:Click Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        parent_css="#resultArea [id^='ReportIframe-']"
        resultobj.wait_for_property(parent_css, 1, expire_time=15)
        time.sleep(1)
        utillobj.switch_to_frame(pause=2)
        
        """  
        Verify output
        """
        time.sleep(5)
        expected_list=['COUNTRY', 'SALES']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 09.01: Verify report heading')
        miscelanousobj.verify_page_summary('0','5of5records,Page1of1', 'Step 09.02: Verify report1 Page summary')
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_run_Ds01.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+'_run_Ds01.xlsx', "Step 09.03: Verify report1")
        utillobj.switch_to_default_content(pause=3)

        """
        Step 10:Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
       
if __name__ == "__main__":
    unittest.main()