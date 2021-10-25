'''
Created on Jul 04, 2017
@author: Nasir
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea
from common.lib import utillity


class C2204988_TestClass(BaseTestCase):

    def test_C2204988(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = '131773'
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
        Step 01: Execute 131773.fex
        """
        utillobj.active_run_fex_api_login(Test_Case_ID + ".fex", "S7074", 'mrid', 'mrpass')
        time.sleep(7)
        parent_css="#MAINTABLE_wbody0 rect[class^='riser']"
        result_obj.wait_for_property(parent_css, 5)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0","COUNTRY", "Step 01a: Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0","DEALER_COST", "Step 01b: Verify Y-Axis Title")
        expected_xval_list=['ENGLAND','FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 01c: ')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 5, 'Step 01d: Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g3!mbar!", 'cerulean_blue_1', 'Step 01e: Verify bar Color')
        miscelaneousobj.verify_active_chart_tooltip('MAINTABLE_wbody0',"riser!s0!g2!mbar!", ['DEALER_COST, ITALY: 41,235'],"Step 01f: Verify Chart piebevel tooltip for Unit Sales")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST by COUNTRY', 'Step 01g: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 01h: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 01i: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 01j: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        oHeight=driver.find_element_by_css_selector("#orgdiv0").value_of_css_property('height')
        print(oHeight)
        oWidth=driver.find_element_by_css_selector("#orgdiv0").value_of_css_property('width')
        print(oWidth)
        if (oHeight=='304px') and (oWidth=='500px'):
            utillobj.asequal(True, True, 'Step 01x: Verify the Chart displayed with default size')
        else:
            utillobj.asequal(True, False, 'Step 01x: Verify the Chart displayed with default size')
        ele=driver.find_element_by_css_selector("#orgdiv0")   
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step01', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        utillobj.infoassist_api_logout()
        time.sleep(5)
        
        """
        Step 02: Execute Revised_131773.fex
        """
        utillobj.active_run_fex_api_login("Revised_" + Test_Case_ID + ".fex", "S7074", 'mrid', 'mrpass')
        time.sleep(7)
        parent_css="#MAINTABLE_wbody0 rect[class^='riser']"
        result_obj.wait_for_property(parent_css, 5)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0","COUNTRY", "Step 02a: Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0","DEALER_COST", "Step 02b: Verify Y-Axis Title")
        expected_xval_list=['ENGLAND','FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 02c: ')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 5, 'Step 02d: Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", 'cerulean_blue_1', 'Step 02e: Verify bar Color')
        miscelaneousobj.verify_active_chart_tooltip('MAINTABLE_wbody0',"riser!s0!g2!mbar!", ['DEALER_COST, ITALY: 41,235'],"Step 02f: Verify Chart piebevel tooltip for Unit Sales")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST by COUNTRY', 'Step 02g: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 02h: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02i: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02j: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        oHeight=driver.find_element_by_css_selector("#orgdiv0").value_of_css_property('height')
        oWidth=driver.find_element_by_css_selector("#orgdiv0").value_of_css_property('width')
        print(oHeight)
        print(oWidth)
        if (oHeight=='404px') and (oWidth=='769px'):
            utillobj.asequal(True, True, 'Step 02x: Verify the Chart displayed with smaller size - 405.0 & 770.0')
        else:
            utillobj.asequal(True, False, 'Step 02x: Verify the Chart displayed with smaller size - 405.0 & 770.0')
        ele=driver.find_element_by_css_selector("#orgdiv0")   
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step02', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        utillobj.infoassist_api_logout()
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()
    
    
    