'''
Created on JUL 7, 2017

@author: Pavithra

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2204981
TestCase Name = Verify NOPRINT values is not shown in output
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea,active_miscelaneous
from common.lib import utillity

class C2204981_TestClass(BaseTestCase):

    def test_C2204981(self):
        
        Test_Case_ID="C2204981"
        """
            TESTCASE VARIABLES
        """     
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(driver)
        """
            Step 01:Run the attached fex T1121457.
        """    
        utillobj.active_run_fex_api_login("T1121457.fex", "S7074", 'mrid', 'mrpass')
        time.sleep(6)
        parent_css="div [id='MAINTABLE_wmenu0']"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(3)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "COUNTRY : CAR", "Step 01.1: Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['ENGLAND/JAGUAR', 'ENGLAND/JENSEN', 'ENGLAND/TRIUMPH', 'FRANCE/PEUGEOT', 'ITALY/ALFA ROMEO', 'ITALY/MASERATI', 'JAPAN/DATSUN', 'JAPAN/TOYOTA', 'W GERMANY/AUDI', 'W GERMANY/BMW']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 01.2: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 01.3: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", "cerulean_blue", "Step 01.4 Verify  bar color")
        expected_tooltip_list=['RETAIL_COST, ITALY/ALFA ROMEO: 19,565']
        miscelaneous_obj.verify_active_chart_tooltip('MAINTABLE_wbody0', 'riser!s1!g4!mbar!', expected_tooltip_list, "Step 1.4: verify tooltip values")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST by COUNTRY, CAR', 'Step 1.5: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options', 'Column','Pie','Line', 'Scatter', 'Advanced Chart', 'Original Chart'],"Step 1.6: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 1.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 1.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        legend=["DEALER_COST", "RETAIL_COST"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 1.9: Verify labels")
        time.sleep(3)
        utillobj.infoassist_api_logout()
        """
            Step 02: Edit the Fex and add NOPRINT to the line - SUM CAR.BODY.DEALER_COST.
        """ 
    
        utillobj.active_run_fex_api_login("T1121457_NOPRINT.fex", "S7074", 'mrid', 'mrpass')
        time.sleep(6)
        parent_css="div [id='MAINTABLE_wmenu0']"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(3)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "COUNTRY : CAR", "Step 02.1: Verify -xAxis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "RETAIL_COST", "Step 02.2: Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['ENGLAND/JAGUAR', 'ENGLAND/JENSEN', 'ENGLAND/TRIUMPH', 'FRANCE/PEUGEOT', 'ITALY/ALFA ROMEO', 'ITALY/MASERATI', 'JAPAN/DATSUN', 'JAPAN/TOYOTA', 'W GERMANY/AUDI', 'W GERMANY/BMW']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 02.3: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 10, 'Step 02.4: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", "cerulean_blue", "Step 02.4 Verify  bar color")
        expected_tooltip_list=['RETAIL_COST, ITALY/ALFA ROMEO: 19,565']
        miscelaneous_obj.verify_active_chart_tooltip('MAINTABLE_wbody0', 'riser!s0!g4!mbar!', expected_tooltip_list, "Step 2.5: verify tooltip values")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'RETAIL_COST by COUNTRY, CAR', 'Step 2.6: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options', 'Column','Pie','Line', 'Scatter', 'Advanced Chart', 'Original Chart'],"Step 2.7: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 2.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 2.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(3)
        ele=driver.find_element_by_css_selector("#orgdivouter0")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step2', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
if __name__ == '__main__':
    unittest.main()
