'''
Created on Jan 03, 2019

@author: Magesh

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8320904
Test Case Title =  Open an existing InfoAssist Chart FEX 
'''

import unittest
#from common.lib.basetestcase import BaseTestCase
from common.lib.basetestcasedocker import BaseTestCaseDocker
from common.wftools import designer_chart, chart

#class C8320904_TestClass(BaseTestCase):
class C8320904_TestClass(BaseTestCaseDocker):

    def test_C8320904(self):
       
        """
        CLASS OBJECTS
        """
        designer_chartobj = designer_chart.Designer_Chart(self.driver)
        chartobj = chart.Chart(self.driver)
        
        """
        COMMON VARIABLES
        """
        Restore_fex = "8204M_IA"
        preview_parent_css = "#TableChart_1"

        """
        STEP 1 : Edit an existing InfoAssist Chart FEX
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/Smoke/8204M_IA.fex&tool=chart
        """
        designer_chartobj.invoke_ia_in_edit_mode_using_api(Restore_fex)
        
        """
        STEP 1.1 : Verify the Expected Result in Preview
        """
        designer_chartobj.wait_for_number_of_element("#TableChart_1 rect[class*='riser!']", 10, chartobj.home_page_long_timesleep)
        designer_chartobj.verify_x_axis_title_in_preview(['CAR'], parent_css=preview_parent_css, msg="Step 01.01: Verify x_axis title in_preview")
        designer_chartobj.verify_y_axis_title_in_preview(['SALES'], parent_css=preview_parent_css, msg="Step 01.02: Verify y_axis title in_preview")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        designer_chartobj.verify_x_axis_label_in_preview(expected_xval_list, parent_css=preview_parent_css, msg="Step 01.03: Verify x_axis_label_in_preview")
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K']
        designer_chartobj.verify_y_axis_label_in_preview(expected_yval_list, parent_css=preview_parent_css, msg="Step 01.04: Verify y_axis_label_in_preview")
        designer_chartobj.verify_number_of_risers("#TableChart_1 rect", 1, 10, msg="Step 01.05: Verify number of risers_in_preview")
        designer_chartobj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g0!mbar!']", 'bar_blue', parent_css=preview_parent_css, msg='Step 01.06')
        chartobj.verify_field_listed_under_querytree('Vertical Axis', 'SALES', 1, msg='Step 01.07')
        chartobj.verify_field_listed_under_querytree('Horizontal Axis', 'CAR', 1, msg='Step 01.08')
        
        """
        STEP 2 : Select IA > Exit
        """
        #Since testcase is invoked using API. Hence logout is implemented. 
        designer_chartobj.api_logout()
        
if __name__ == "__main__":
    unittest.main()