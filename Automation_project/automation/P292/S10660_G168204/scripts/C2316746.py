'''
Created on Nov 2, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10660
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2316746
TestCase Name = Runtime filter options on bins
'''

import unittest, time
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea
from common.lib import utillity
from selenium.webdriver import ActionChains

class C2316746_TestClass(BaseTestCase):

    def test_C2316746(self):
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID_1 = 'C2316743'
        Test_Case_ID = 'C2316746'

        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        
        """
        Step 01: Use API call to run visualization created in previous test case
        http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10660&BIP_item=C2316743.fex
        """
        utillobj.active_run_fex_api_login(Test_Case_ID_1+'.fex','S10660_visual_2','mrid','mrpass')
        time.sleep(10)
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(10) 
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 18)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 5)
        time.sleep(3)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'PRICE_DOLLARS_BIN_1', "Step01:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Quantity Sold', "Step01:a(ii) Verify Y-Axis Title")
        expected_xval_list=['.00', '100.00', '200.00', '300.00', '400.00', '500.00', '600.00', '700.00', '800.00', '900.00', '1,100.00', '1,200.00', '1,300.00', '1,900.00', '2,200.00', '3,300.00', '3,400.00', '3,900.00']
        expected_yval_list=['0', '0.3M', '0.6M', '0.9M', '1.2M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step01:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 18, 'Step01.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step01.c: Verify first bar color")
        time.sleep(5)
        expected_tooltip=['PRICE_DOLLARS_BIN_1:100.00', 'Quantity Sold:1,137,404']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g1!mbar!", expected_tooltip,"Step01.d: Verify bar value")
        
        """
        Step 02: Lasso on first five riser
        """
        time.sleep(2)
        raiser="#MAINTABLE_wbody1 [class*='riser!s0!g0!mbar!']"
        utillobj._validate_page((By.CSS_SELECTOR,raiser))
        move1 = driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(move1, 'start')
        time.sleep(3)
        browser = utillobj.parseinitfile('browser')
        move_riser = driver.find_element_by_css_selector(raiser)
        if browser == 'Firefox':
            utillobj.click_type_using_pyautogui(move_riser)
        else:
            action = ActionChains(driver)
            action.move_to_element(move_riser).perform()
        resultobj.create_lasso('MAINTABLE_wbody1','rect', 'riser!s0!g0!mbar', target_tag='rect', target_riser='riser!s0!g4!mbar')
        
        """
        Step 03: Verify no filter options displayed and only points count
        """
        time.sleep(2)
        resultobj.select_or_verify_lasso_filter(verify=['5 points'], msg='Step 03: Verify no filter options displayed and only 5 points count')
        time.sleep(5)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step03', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(3)
        
        """
        Step 04: Close run window
        """
        
if __name__ == '__main__':
    unittest.main()