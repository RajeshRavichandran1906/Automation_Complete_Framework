'''
Created on Dec 31, 2018

@author: Magesh

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8320662
Test Case Title =  Launch Designer chart, save and restore
'''

import unittest,time
#from common.lib.basetestcase import BaseTestCase
from common.lib.basetestcasedocker import BaseTestCaseDocker
from common.wftools import designer_chart
from common.wftools import smoketest

#class C8320662_TestClass(BaseTestCase):
class C8320662_TestClass(BaseTestCaseDocker):

    def test_C8320662(self):
       
        """
        CLASS OBJECTS
        """
        designer_chartobj = designer_chart.Designer_Chart(self.driver)
        smoketestobj = smoketest.Smoketest(self.driver)
        
        """
        COMMON VARIABLES
        """
        Test_Case_ID="c8320662"
        
        """
        STEP 1 : Launch Designer Chart with car
        http://machine:port/ibi_apps/designer?&master=ibisamp/car&item=IBFS:/WFC/Repository/Smoke&tool=chart
        """
        designer_chartobj.invoke_designer_chart_using_api('ibisamp/car')
        designer_chartobj.wait_for_visible_text("text[class='legend-labels!s0!']", 'Series 0', smoketestobj.home_page_long_timesleep)
        
        """
        STEP 1.2 : Verify the Expected Result in Preview
        """
        expected_xval_list=['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4']
        designer_chartobj.verify_x_axis_label_in_preview(expected_xval_list, msg="Step 01.01: Verify x_axis_label_in_preview")
        expected_yval_list=['0', '40', '80', '120', '160', '200']
        designer_chartobj.verify_y_axis_label_in_preview(expected_yval_list, msg="Step 01.02: Verify Y_axis_label_in_preview")
        designer_chartobj.verify_number_of_risers("[id*='chartpreview'] rect", 5, 5, msg="Step 01.03: Verify number of risers_in_preview")
        legend=['Series 0', 'Series 1', 'Series 2', 'Series 3', 'Series 4']
        designer_chartobj.verify_legends_in_preview(legend, msg="Step 01.04: Verify legend_in_preview")
        
        """
        STEP 02 : Double click COUNTRY
        """
        smoketestobj.double_click_on_dimension_field('COUNTRY')
        
        """
        STEP 2.2 : Verify the Expected Result in Preview
        """
        designer_chartobj.wait_for_visible_text("div.wfc-bc-output-div", "COUNTRY")
        expected_xval_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        designer_chartobj.verify_x_axis_label_in_preview(expected_xval_list, msg="Step 02.01: Verify x_axis_label_in_preview")
        designer_chartobj.verify_x_axis_title_in_preview(['COUNTRY'], msg="Step 02.02: Verify x_axis title in_preview")
        designer_chartobj.verify_number_of_risers("div.wfc-bc-output-div rect", 1, 5, msg="Step 02.03: Verify number of risers_in_preview")
        designer_chartobj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g0!mbar!']", 'bar_blue', msg='Step 02.04')
        
        """
        STEP 3 : Click on Save button > Type C8320662 > Click on 'Save'
        """
        smoketestobj.save_designer_chart_from_toolbar(Test_Case_ID)
        time.sleep(smoketestobj.home_page_short_timesleep)
        
        """
        STEP 4 : Click on the application menu > Close
        """
        #Since testcase is invoked using API, application menu > Close not working. Hence logout is implemented. 
        designer_chartobj.api_logout()
        
        """
        STEP 5 : Edit the saved FEX:
        http://machine:port/{alias}/designer?item=IBFS:/WFC/Repository/Smoke/C8320662.fex&tool=chart
        """
        designer_chartobj.invoke_designer_chart_in_edit_mode_using_api(Test_Case_ID)
        
        """
        STEP 5.1 : Verify the Expected Result in Preview
        """
        designer_chartobj.wait_for_visible_text("div.wfc-bc-output-div", "COUNTRY")
        expected_xval_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        designer_chartobj.verify_x_axis_label_in_preview(expected_xval_list, msg="Step 05.01: Verify x_axis_label_in_preview")
        designer_chartobj.verify_x_axis_title_in_preview(['COUNTRY'], msg="Step 05.02: Verify x_axis title in_preview")
        designer_chartobj.verify_number_of_risers("div.wfc-bc-output-div rect", 1, 5, msg="Step 05.03: Verify number of risers_in_preview")
        designer_chartobj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g0!mbar!']", 'bar_blue', msg='Step 05.04')
        
        """
        STEP 6 : Click on the application menu > Close 
        """
        #Since testcase is invoked using API, application menu > Close not working. Hence logout is implemented. 
        designer_chartobj.api_logout()
        
if __name__ == "__main__":
    unittest.main()