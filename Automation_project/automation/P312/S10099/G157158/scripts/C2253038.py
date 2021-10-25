'''
Created on Feb 22, 2018

@author: Robert

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2253038
TestCase Name = Drill Down available in Visualization
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization


class C2253038_TestClass(BaseTestCase):

    def test_C2253038(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2253038'
        visual = visualization.Visualization(self.driver)
        sleep_time=4
        position=1
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS8358&tool=idis&master=baseapp/car
        """
        visual.invoke_visualization_using_api('ibisamp/car')
        time.sleep(sleep_time)
         
        
        """
        Step 02. Add fields car, sales
        """
        field_name='CAR'
        visual.double_click_on_datetree_item(field_name, position)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 10, 30)
        field_name="SALES"
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 10, 30)
        visual.double_click_on_datetree_item(field_name,position)
        parent_css="#MAINTABLE_wbody1 text[class^='yaxis-title']"
        visual.wait_for_visible_text(parent_css, visble_element_text='SALES', time_out=50)
         
        """
        Step 03. Verify axis label values
        """
        x_axis_title=['CAR']
        visual.verify_x_axis_title(x_axis_title, msg='Step 3.1')
        y_axis_title=['SALES']
        visual.verify_y_axis_title(y_axis_title, msg='Step 3.2')
        expected_xaxis_label=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 3.3')
        expected_yaxis_label=['0', '20K', '40K', '60K', '80K', '100K']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 3.4')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 10, msg='Step 3.5')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!']", "bar_blue", msg='Step 3.6')
        
        """
        Step 04. Verify query pane
        """
        
        visual.verify_field_listed_under_querytree('Vertical Axis', 'SALES', position, "Step 04.2:")
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'CAR', position, "Step 04.3:")
         
        """
        Step 05. Verify tooltip value (CAR: SALES)
        BMW: 80390
        """           
        expected_tooltip_list=['CAR:BMW', 'SALES:80390', 'Filter Chart', 'Exclude from Chart']
        visual.verify_tooltip('riser!s0!g2!mbar!', expected_tooltip_list,'Step 5: Verify Tooltip') 
        time.sleep(sleep_time)
        
        """
        Step 06. Click car in the Query Pane, select Traffic Lights from the Field Tab Ribbon
        STEP 06:1. Traffic light disabled in 8200.
        """
        
        visual.select_field_under_query_tree('CAR', 1)
        
        visual.wait_for_number_of_element("#FieldTrafficLights", 1, 30)
        element=self.driver.find_element_by_css_selector("#FieldTrafficLights")
        
        visual.verify_element_disable(element, expected_element_status=True, msg='Step 6.1. Verify Traffic Lights is disabled')
            
        
        """
        Step 7: Click "Save" in the toolbar > Type C2141626  > Click "Save" in the Save As dialog
        """
    
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
        Step 8: Logout of the IA API using the following URL: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(sleep_time)
        
if __name__ == '__main__':
    unittest.main()