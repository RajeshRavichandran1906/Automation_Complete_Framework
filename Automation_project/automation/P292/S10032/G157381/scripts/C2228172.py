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
        
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        vis_ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        
        """ Step 1: Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=chart&master=ibisamp/employee
        """
        utillobj.infoassist_api_login('chart','ibisamp/employee','P292/S10032_chart_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#TableChart_1 text", 16, 25)
        
        """ Step 2: Verify output format as HTML5.
        """
        vis_ribbonobj.switch_ia_tab('Home')
        time.sleep(2)
        try:
            output_type_text = driver.find_element_by_css_selector("#HomeFormatVBox #HomeFormatType").text.strip()
        except NoSuchElementException:
            print("Output FormatType is not visible.")
        utillobj.asequal('HTML5', output_type_text, "Step 2: Verify output format as HTML5.")
        
        """ Step 3: Double Click "LAST_NAME", "CURR_SAL".
        """
        metaobj.datatree_field_click("LAST_NAME", 2, 1)
        parent_css = "#TableChart_1 text.xaxisOrdinal-title"
        utillobj.synchronize_with_visble_text(parent_css, "LAST_NAME", 15)
           
        metaobj.datatree_field_click("CURR_SAL", 2, 1)
        parent_css = "#TableChart_1 text.yaxis-title"
        utillobj.synchronize_with_visble_text(parent_css, "CURR_SAL", 15)
        
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
        
        """ Step 6: Logout using API (without saving)
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        time.sleep(5)
if __name__ == '__main__':
    unittest.main()