'''
Created on July 25, 2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2204998
TestCase Name = Project-147267 AHTML:JSCHART: unable to apply chart filter condition
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, active_miscelaneous
from common.lib import utillity


class C2204998_TestClass(BaseTestCase):

    def test_C2204998(self):
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(self.driver)
        Test_Case_ID="C2204998"
        
        
        """ Step 1: Run the 147627.fex in adhoc procedure
        """
        utillobj.active_run_fex_api_login("147627.fex", "S7074", 'mrid', 'mrpass')
        parent_css="#MAINTABLE_wbody0 text[class*='xaxisOrdinal-labels!g0!mgroupLabel']"
        result_obj.wait_for_property(parent_css, 1, string_value='ENGLAND', with_regular_exprestion=True)
        time.sleep(2)
        result_obj.verify_xaxis_title('MAINTABLE_wbody0', 'COUNTRY', """Step 1: Verify Chart X-Title 'COUNTRY' """)
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0','DEALER_COST, RETAIL_COST by COUNTRY','Step 1.1 : Verify chart title')
        expected_xval_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list,'Step 1.2 :')
        result_obj.verify_riser_legends('MAINTABLE_wbody0',['DEALER_COST', 'RETAIL_COST'],'Step 1.3 : Verify chart legend label')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0',1,10,'Step 1.4 : Verify number of chart risers')
        utillobj.verify_chart_color('MAINTABLE_wbody0','riser!s0!g0!mbar','cerulean_blue_1','Step 1.5 : Verify chart riser color')
        tooltip_value=['DEALER_COST, ENGLAND: 37,853']
        miscelaneous_obj.verify_active_chart_tooltip('MAINTABLE_wbody0','riser!s0!g0!mbar',tooltip_value,'Step 1.6 : Verify chart tooltip value')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart'],"Step 1.7 : Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 1.8 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 1.9 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)  
        time.sleep(5)
        ele=driver.find_element_by_css_selector("#orgdiv0")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step_1', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """ Step 2: Hover mouse on any bar field in the chart and verify filter chart condition appears.
        """
        object_elem = driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class*='riser!s1!g0!mbar!']")
        utillobj.click_on_screen(object_elem, 'middle', click_type=0)
        time.sleep(1)
        
        
        """ Step 3: Click Filter Chart and see that filter condition applied properly.
        """
        miscelaneous_obj.select_active_lasso_menu('Filter Chart')
        parent_css="#MAINTABLE_wbody0 text[class*='xaxisOrdinal-labels']"
        result_obj.wait_for_property(parent_css, 1, expire_time=50)
        time.sleep(2)
        result_obj.verify_xaxis_title('MAINTABLE_wbody0', 'COUNTRY', """Step 3: Verify Chart X-Title 'COUNTRY' """)
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0','DEALER_COST, RETAIL_COST by COUNTRY','Step 3.1 : Verify chart title')
        expected_xval_list=['ENGLAND']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list,'Step 3.2 :')
        result_obj.verify_riser_legends('MAINTABLE_wbody0',['DEALER_COST', 'RETAIL_COST'],'Step 3.3 : Verify chart legend label')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0',1,2,'Step 3.4 : Verify number of chart risers')
        utillobj.verify_chart_color('MAINTABLE_wbody0','riser!s0!g0!mbar','cerulean_blue_1','Step 3.5 : Verify chart riser color')
        tooltip_value=['DEALER_COST, ENGLAND: 37,853']
        miscelaneous_obj.verify_active_chart_tooltip('MAINTABLE_wbody0','riser!s0!g0!mbar',tooltip_value,'Step 3.6 : Verify chart tooltip value')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart'],"Step 3.7 : Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 3.8 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 3.9 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Remove Filter'],"Step 3.10 : Verify Chart toolbar", custom_css="div[title='Remove Filter']")
        time.sleep(5)
        ele=driver.find_element_by_css_selector("#orgdiv0")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step_3', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(3)
        
        
       
        
        
if __name__ == '__main__':
    unittest.main()