'''
Created on Jan 02, 2019

@author: Magesh

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8320684
Test Case Title =  Launch IA Chart, save and restore 
'''

import unittest,time
#from common.lib.basetestcase import BaseTestCase
from common.lib.basetestcasedocker import BaseTestCaseDocker
from common.wftools import designer_chart, chart, smoketest

#class C8320684_TestClass(BaseTestCase):
class C8320684_TestClass(BaseTestCaseDocker):

    def test_C8320684(self):
       
        """
        CLASS OBJECTS
        """
        designer_chartobj = designer_chart.Designer_Chart(self.driver)
        chartobj = chart.Chart(self.driver)
        smoketestobj = smoketest.Smoketest(self.driver)
        
        """
        COMMON VARIABLES
        """
        Test_Case_ID="c8320684"
        SHORT_WAIT_TIME = 5
        preview_parent_css = "#TableChart_1"
        
        """
        STEP 1 : Launch Designer Chart with car
        http://machine:port/ibi_apps/designer?&master=ibisamp/car&item=IBFS:/WFC/Repository/Smoke&tool=workbook
        """
        designer_chartobj.invoke_ia_using_api('ibisamp/car')
        designer_chartobj.wait_for_visible_text("text[class='legend-labels!s0!']", 'Series 0', smoketestobj.home_page_long_timesleep)
        
        """
        STEP 1.1 : Verify the Expected Result in Preview
        """
        expected_xval_list=['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4']
        designer_chartobj.verify_x_axis_label_in_preview(expected_xval_list, parent_css=preview_parent_css, msg="Step 01.01: Verify x_axis_label_in_preview")
        expected_yval_list=['0', '10', '20', '30', '40', '50']
        designer_chartobj.verify_y_axis_label_in_preview(expected_yval_list, parent_css=preview_parent_css, msg="Step 01.02: Verify Y_axis_label_in_preview")
        designer_chartobj.verify_number_of_risers("#TableChart_1 rect", 1, 25, msg="Step 01.03: Verify number of risers_in_preview")
        legend=['Series 0', 'Series 1', 'Series 2', 'Series 3', 'Series 4']
        designer_chartobj.verify_legends_in_preview(legend, parent_css=preview_parent_css, msg="Step 01.04: Verify legend_in_preview")
        
        """
        STEP 02 : Double click SALES
        """
        smoketestobj.double_click_on_datetree_item('SALES', 1)
        
        """
        STEP 2.1 : Verify the Expected Result in Preview
        """
        designer_chartobj.wait_for_number_of_element("#TableChart_1 rect[class*='riser!']", 1, smoketestobj.home_page_medium_timesleep)
        expected_yval_list=['0', '40K', '80K', '120K', '160K', '200K', '240K']
        designer_chartobj.verify_y_axis_label_in_preview(expected_yval_list, parent_css=preview_parent_css, msg="Step 02.01: Verify y_axis_label_in_preview")
        designer_chartobj.verify_y_axis_title_in_preview(['SALES'], parent_css=preview_parent_css, msg="Step 02.02: Verify y_axis title in_preview")
        designer_chartobj.verify_number_of_risers("#TableChart_1 rect", 1, 1, msg="Step 02.03: Verify number of risers_in_preview")
        designer_chartobj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g0!mbar!']", 'bar_blue', parent_css=preview_parent_css, msg='Step 02.04')
        chartobj.verify_field_listed_under_querytree('Vertical Axis', 'SALES', 1, msg='Step 02.05')
        
        """
        STEP 03 : Click on Save button > Type C8320684 > Click on 'Save'
        """
        smoketestobj.select_item_in_top_toolbar('save')
        smoketestobj.save_file_in_save_dialog(Test_Case_ID)
        time.sleep(SHORT_WAIT_TIME)
        
        """
        STEP 4 : Select IA > Exit
        """
        #Since testcase is invoked using API. Hence logout is implemented. 
        designer_chartobj.api_logout()
        
        """
        STEP 5 : Edit the saved FEX
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/Smoke/C8320684.fex&tool=chart
        """
        designer_chartobj.invoke_ia_in_edit_mode_using_api(Test_Case_ID)
        
        """
        STEP 5.1 : Verify the Expected Result in Preview
        """
        designer_chartobj.wait_for_number_of_element("#TableChart_1 rect[class*='riser!']", 1, smoketestobj.home_page_long_timesleep)
        expected_xval_list=['0', '40K', '80K', '120K', '160K', '200K', '240K']
        designer_chartobj.verify_y_axis_label_in_preview(expected_xval_list, parent_css=preview_parent_css, msg="Step 05.01: Verify y_axis_label_in_preview")
        designer_chartobj.verify_y_axis_title_in_preview(['SALES'], parent_css=preview_parent_css, msg="Step 05.02: Verify y_axis title in_preview")
        designer_chartobj.verify_number_of_risers("#TableChart_1 rect", 1, 1, msg="Step 05.03: Verify number of risers_in_preview")
        designer_chartobj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g0!mbar!']", 'bar_blue', parent_css=preview_parent_css, msg='Step 05.04')
        chartobj.verify_field_listed_under_querytree('Vertical Axis', 'SALES', 1, msg='Step 05.05')
        
        """
        STEP 6 : Select IA > Exit
        """
        #Since testcase is invoked using API. Hence logout is implemented. 
        designer_chartobj.api_logout()
        
if __name__ == "__main__":
    unittest.main()