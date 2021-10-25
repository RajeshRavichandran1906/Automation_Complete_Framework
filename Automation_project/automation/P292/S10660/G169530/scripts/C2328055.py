'''
Created on Oct 31, 2017

@author: BM13368
Testcase_Name : Extend Annotation feature in JSCHART(HTML5)
Testcase_ID :http://172.19.2.180/testrail/index.php?/cases/view/2328055&group_by=cases:section_id&group_id=169530&group_order=asc
Chart_Validation Suite 8202 New features

'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea
from common.lib import utillity
from common.lib import core_utility

class C2328055_TestClass(BaseTestCase):

    def test_C2328055(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2328055a.fex'
        Test_Case_ID1 = 'C2328055b.fex'
        
        
        driver = self.driver #Driver reference object created
        
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        core_utility_obj = core_utility.CoreUtillityMethods(self.driver)
        
        """
            Step 01 : Run from bip using API.
            http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_LAUNCH&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292%252FS10660_chart_2%252F&BIP_item=C2326015a.FEX
        """
        utillobj.active_run_fex_api_login(Test_Case_ID, "S10660_chart_2", 'mrid', 'mrpass')
        innerHeight = self.driver.execute_script("return window.innerHeight")
        availHeight = self.driver.execute_script("return screen.availHeight")
        browser_height = availHeight - innerHeight
        utillity.UtillityMethods.browser_y=browser_height
        parent_css="#jschart_HOLD_0 text[class^='xaxis'][class$='title']"
        utillobj.synchronize_with_visble_text(parent_css, "COUNTRY", resultobj.home_page_medium_timesleep)
      
        """
            Step 02 : Verify the following output displayed
        """
        
        resultobj.verify_yaxis_title("jschart_HOLD_0", 'SALES', "Step 01:01: Verify -yAxis Title")
        resultobj.verify_xaxis_title("jschart_HOLD_0", 'COUNTRY', "Step 01:02: Verify -xAxis Title")
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 5, 'Step 01:03: Verify the total number of risers displayed on livepreview Chart')
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K']
        expected_xval_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 01:04: X and Y axis labels')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar", "bar_blue", "Step 01:05: Verify first bar color")
        """
            Verification : Expected to see Annotation marker on top-right corner (black color)
        """
        utillobj.verify_object_visible("#jschart_HOLD_0 rect[class*='annotation']", True, "Step 01:06 Verify annotation is visible in the chart")
        obj1=driver.find_element_by_css_selector("#jschart_HOLD_0")
        time.sleep(1)
        utillobj.take_screenshot(obj1,Test_Case_ID + '_Actual_step02', image_type='actual', x=1, y=1, w=-1, h=-1)
        time.sleep(3)
        """
           Step 03:  Hover on icon
           Step 04 : Verify following tooltip text displayed as Expected to see tooltip text "Click to launch a google search
        """
        expected_tooltip_list=['Click to launch a google search']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "annotation", expected_tooltip_list, "Step 03:01: Verify Salary bar value",y_offset=-21)
        
        """
            Step 05 : Click on the annotation icon
        """
        annotation_obj=driver.find_element_by_css_selector("#jschart_HOLD_0 rect[class*='annotation']")
        core_utility_obj.python_left_click(annotation_obj)
        time.sleep(3)
        
        """
            Step 06 : Verify Google website opened in newtab
        """
        utillobj.switch_to_window(1)
        time.sleep(1)
        driver.maximize_window()
        time.sleep(5)
        obj=driver.find_element_by_css_selector("[href*='ServiceLogin']")
        gtext=obj.get_attribute("text")
        utillobj.asequal('Sign in', gtext, "Step 06: Verify the google-page text")
        
        """
            Step 07 : Dismiss Google and run window
        """
        self.driver.close()
        time.sleep(5)
        utillobj.switch_to_window(0)
        time.sleep(1)
        utillobj.infoassist_api_logout()
        time.sleep(5)
        
        """
            Step 08 : Run from bip using API
            http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_LAUNCH&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292%252FS10660_chart_2%252F&BIP_item=C2326015b.FEX 
        """
        utillobj.active_run_fex_api_login(Test_Case_ID1, "S10660_chart_2", 'mrid', 'mrpass')
        innerHeight = self.driver.execute_script("return window.innerHeight")
        availHeight = self.driver.execute_script("return screen.availHeight")
        browser_height = availHeight - innerHeight
        utillity.UtillityMethods.browser_y=browser_height
        parent_css="#jschart_HOLD_0 text[class^='xaxis'][class$='title']"
        utillobj.synchronize_with_visble_text(parent_css, "COUNTRY", resultobj.home_page_medium_timesleep)
        
        """
            Step 09 : Verify the following output displayed
            Verification : Expected to see Annotation marker on top-right corner (green color)
        """
        
        resultobj.verify_yaxis_title("jschart_HOLD_0", 'SALES', "Step 09:01: Verify -yAxis Title")
        resultobj.verify_xaxis_title("jschart_HOLD_0", 'COUNTRY', "Step 09:02: Verify -xAxis Title")
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 5, 'Step 09:03: Verify the total number of risers displayed on live-preview Chart')
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K']
        expected_xval_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 09:04: X and Y axis labels')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar", "bar_blue", "Step 09:05: Verify first bar color")
        obj1=driver.find_element_by_css_selector("#jschart_HOLD_0")
        time.sleep(1)
        utillobj.take_screenshot(obj1,Test_Case_ID + '_Actual_step09', image_type='actual', x=1, y=1, w=-1, h=-1)
        time.sleep(3)
        
        """
            Step 10 : Hover on icon
            Step 11 : Verify following tooltip text displayed
            Verification : Expected to see tooltip text "Click to launch a Information builders"
        """
        expected_tooltip_list=['Click to launch a Information builders']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "annotation", expected_tooltip_list, "Step 10:01: Verify Salary bar value",y_offset=-21)
        
        """
            Step 12 : Click on the annotation icon
        """
        annotation_obj=driver.find_element_by_css_selector("#jschart_HOLD_0 rect[class*='annotation']")
        core_utility_obj.python_left_click(annotation_obj)
        
        """
            Step 13 : Verify Information builders website opened in new tab
        """
        utillobj.switch_to_window(1,window_title='Data and Analytics Company | ibi')
        expected='Global Leader in Integration and Analytics Software | TIBCO Software'
        actual=driver.title
        utillobj.asin(expected, actual,"Step 13.2: Verify Information Builders webpage is displayed in a new window")
        
        """
            Step 14 : Dismiss Information builders and run window
        """
        self.driver.close()
        time.sleep(5)
        utillobj.switch_to_window(0)
     
        
                              
if __name__ == "__main__":
    unittest.main()
        
        
        



