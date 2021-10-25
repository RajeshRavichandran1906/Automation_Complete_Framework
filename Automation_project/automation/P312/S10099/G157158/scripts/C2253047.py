'''
Created on Feb 22, 2018

@author: Robert

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2253037
TestCase Name = BUE: Restore Original doesn't restore correctly
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization
from common.lib import utillity

class C2253047_TestClass(BaseTestCase):

    def test_C2253047(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2253047'
        visual = visualization.Visualization(self.driver)
        util_obj= utillity.UtillityMethods(self.driver)
        sleep_time=4
        position=1
        
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS8358&tool=idis&master=baseapp/WF_RETAIL_LITE
        """
        visual.invoke_visualization_using_api('ibisamp/carolap')
        util_obj.wait_for_page_loads(20)
        
        """
        Step 02. Double click DEALER_COST & BODYTYPE.
        """
        field_name="DEALER_COST"
        visual.double_click_on_datetree_item(field_name,position)
        parent_css="#MAINTABLE_wbody1 text[class*='yaxis']"
        visual.wait_for_number_of_element(parent_css,6, 30)
        visual.double_click_on_datetree_item('BODYTYPE->BODYTYPE->BODYTYPE', 3)
        parent_css="#MAINTABLE_wbody1 rect[class*='riser']"
        visual.wait_for_number_of_element(parent_css,5, 30)
        
         
        """
        Step 03. Verify axis label values
        """
        x_axis_title=['BODYTYPE']
        visual.verify_x_axis_title(x_axis_title, msg='Step 03.01')
        y_axis_title=['DEALER_COST']
        visual.verify_y_axis_title(y_axis_title, msg='Step 03.02')
        expected_xaxis_label=['CONVERTIBLE', 'COUPE', 'HARDTOP', 'ROADSTER', 'SEDAN']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 03.03')
        expected_yaxis_label=['0', '20K', '40K', '60K', '80K', '100K', '120K']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 03.04')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 5, msg='Step 03.05')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!']", "bar_blue", msg='Step 03.06')
        
        """
        Step 04. Verify query pane
        """
        
        visual.verify_field_listed_under_querytree('Vertical Axis', 'DEALER_COST', position, "Step 04.01")
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'BODYTYPE', position, "Step 04.02")
         
        """
        Step 05. Verify each bar riser values
        """
        expected_tooltip_list=['BODYTYPE:COUPE', 'DEALER_COST:30,660', 'Filter Chart', 'Exclude from Chart', 'Drill down to LENGTH']
        visual.verify_tooltip('riser!s0!g1!mbar!', expected_tooltip_list,'Step 05.01: Verify Tooltip')
      
        
        """
        Step 06. Click Run in the toolbar
        """
        visual.run_visualization_from_toptoolbar()
        util_obj.wait_for_page_loads(10)
        visual.switch_to_new_window()
        
        """
        Step 07. Hover over a bar(COUPE) and select Drilldown.
        """
        visual.select_tooltip("riser!s0!g1!mbar!", "Drill down to LENGTH")
        util_obj.wait_for_page_loads(15)
#         parent_css="#MAINTABLE_wbody1 text[class^='xaxisOrdinal-title']"
#         visual.wait_for_visible_text(parent_css, visble_element_text='Length', time_out=50)
        """
        Step 8. Verify horizontal axis label (Bodytype drill down to Length)
        """
#         parent_css="#MAINTABLE_wbody1 text[class^='xaxisOrdinal-title']"
#         visual.wait_for_visible_text(parent_css, visble_element_text='LENGTH', time_out=50)
   
        visual.verify_x_axis_title(['LENGTH'], msg='Step 08.01')
        visual.verify_y_axis_title(['DEALER_COST'], msg='Step 08.02')
        expected_xaxis_label=['163', '177']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 08.03')
        expected_yaxis_label=['0', '4K', '8K', '12K', '16K', '20K', '24K', '28K']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 08.04')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 2, msg='Step 08.05')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g1!mbar!']", "bar_blue", msg='Step 08.06')
        
        """
        Step 09. Hover over "177" bar.
        """
        expected_tooltip_list=['LENGTH:177', 'DEALER_COST:25,000', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill up to BODYTYPE']
        visual.verify_tooltip('riser!s0!g1!mbar!', expected_tooltip_list,'Step 09.01: Verify Tooltip')
        time.sleep(sleep_time)

        """
        Step 10. Select Restore to Original from the UI at the bottom right of output window.
        """
        
        visual.select_bottom_right_run_menu_options('reset')
        
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 5, 30)
        
        """
        Step 11. Verify chart reset to Bodytype in x-axis
        """
        parent_css="#MAINTABLE_wbody1 text[class*='xaxisOrdinal']"
        visual.wait_for_number_of_element(parent_css, 6, 30)
        visual.verify_x_axis_title(['BODYTYPE'], msg='Step 10.01')
        visual.verify_y_axis_title(['DEALER_COST'], msg='Step 10.02')
        expected_xaxis_label=['CONVERTIBLE', 'COUPE', 'HARDTOP', 'ROADSTER', 'SEDAN']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 10.03')
        expected_yaxis_label=['0', '20K', '40K', '60K', '80K', '100K', '120K']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 10.04')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 5, msg='Step 10.05')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g1!mbar!']", "bar_blue", msg='Step 10.06')
#         visual.take_run_window_snapshot(Test_Case_ID, '10')
        
        """
        Step 12. Close the output window
        """
        visual.switch_to_previous_window()
        
        """
        Step 13: Click "Save" in the toolbar > Type C2141625  > Click "Save" in the Save As dialog
        """
    
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
        Step 14: Logout of the IA API using the following URL: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(sleep_time)
        
if __name__ == '__main__':
    unittest.main()