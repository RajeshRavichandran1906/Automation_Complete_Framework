'''
Created on 18-Dec-2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2228172
TestCase Name = Verify HOLD button is disabled (82xx)
'''
import unittest, time
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from selenium.common.exceptions import NoSuchElementException
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon

class C2228172_TestClass(BaseTestCase):

    def test_C2228172(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = "C2228172"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        vis_ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        
        """ Step 1: Launch WF, New > Chart with EMPLOYEE.MAS.
        """
        utillobj.infoassist_api_login('chart','ibisamp/employee','P292/S10032_chart_1', 'mrid', 'mrpass')
        resultobj.wait_for_property("#TableChart_1 text", 16, expire_time=25)    
        
        """ Step 2: Verify output format as HTML5.
        """
        vis_ribbonobj.switch_ia_tab('Home')
        time.sleep(2)
        try:
            output_type_text = driver.find_element_by_css_selector("#HomeFormatVBox #HomeFormatType").text
        except NoSuchElementException:
            print("Output FormatType is not visible.")
        utillobj.asequal('HTML5', output_type_text, "Step 2: Verify output format as HTML5.")
        
        """ Step 3: Double Click "LAST_NAME", "CURR_SAL".
        """
        metaobj.datatree_field_click("LAST_NAME", 2, 1)
        parent_css = "#TableChart_1 text.xaxisOrdinal-title"
        resultobj.wait_for_property(parent_css, 0, expire_time=25, string_value='LAST_NAME', with_regular_exprestion=True)    
        metaobj.datatree_field_click("CURR_SAL", 2, 1)
        parent_css = "#TableChart_1 text.yaxis-title"
        resultobj.wait_for_property(parent_css, 0, expire_time=25, string_value='CURR_SAL', with_regular_exprestion=True)    
        
        """ Step 4: Verify the following chart is displayed.
        """
        resultobj.verify_xaxis_title('TableChart_1', 'LAST_NAME', "Step 4: Verify X axis title.")
        resultobj.verify_yaxis_title('TableChart_1', 'CURR_SAL', "Step 4.1: Verify Y axis title.")
        time.sleep(1)
        expected_xval_list=[]
        expected_yval_list=[]
        resultobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, "Step 4.2: Verify XY lables.")
        resultobj.verify_number_of_riser('TableChart_1', 1, 11, "Step 4.3: Verify number of riser.")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g2!mbar!", "bar_blue", "Step 4.4: Verify  riser color")
        
        """ Step 5: On "Home" tab, verify the "File" button has been disabled.
        """
        home_file_button = driver.find_element_by_css_selector("#HomeFormatVBox #HomeDestFile")
        actual_value = home_file_button.get_attribute('disabled')
        utillobj.asequal('true', actual_value, 'Step 5: On "Home" tab, verify the "File" button has been disabled.')
        
        """ Step 6: Dismiss the tool window.
        """
        time.sleep(2)
        vis_ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()