'''
Created on Feb 22, 2018

@author: Robert

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2253046
TestCase Name = BUE: If same field is in horizontal axis and tooltip, displays empty chart at drill down
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization
from common.pages import core_metadata

class C2253046_TestClass(BaseTestCase):

    def test_C2253046(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2253046'
        visual = visualization.Visualization(self.driver)
        metadataobj = core_metadata.CoreMetaData(self.driver)
        sleep_time=4
        position=1
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS8358&tool=idis&master=baseapp/WF_RETAIL_LITE
        """
        visual.invoke_visualization_using_api('ibisamp/carolap')
        
        """
        Step 02. Double click "RETAIL_COST" & "COUNTRY".
        """
#         field_name='COUNTRY'
#         visual.double_click_on_datetree_item(field_name, position)
        metadataobj.double_click_on_data_filed('Dimensions->COUNTRY->COUNTRY->COUNTRY', field_position=3)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 5, 30)
        field_name="RETAIL_COST"
        visual.double_click_on_datetree_item(field_name,position)
        parent_css="#MAINTABLE_wbody1 text[class*='yaxis-title']"
        visual.wait_for_visible_text(parent_css, visble_element_text='RETAIL_COST', time_out=50)
         
        """
        Step 03. Verify axis label values
        """
        x_axis_title=['COUNTRY']
        visual.verify_x_axis_title(x_axis_title, msg='Step 3.1')
        y_axis_title=['RETAIL_COST']
        visual.verify_y_axis_title(y_axis_title, msg='Step 3.2')
        expected_xaxis_label=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 3.3')
        expected_yaxis_label=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 3.4')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 5, msg='Step 3.5')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!']", "bar_blue", msg='Step 3.6')
        
        """
        Step 04. Hover over "W GERMANY" bar.
        Verify the tool tip:
        """
        expected_tooltip_list=['COUNTRY:W GERMANY', 'RETAIL_COST:64,732', 'Filter Chart', 'Exclude from Chart', 'Drill down to CAR']
#         expected_tooltip_list=['COUNTRY:W GERMANY', 'RETAIL_COST:64,732', 'Filter Chart', 'Exclude from Chart', 'Drill down to CAR']
        visual.verify_tooltip('riser!s0!g4!mbar!', expected_tooltip_list,'Step 4.1: Verify Tooltip')
        time.sleep(sleep_time)
        
        """
        Step 05. Drag COUNTRY to Tooltip bucket.
        """
        visual.drag_field_from_data_tree_to_query_pane('COUNTRY', 3, 'Tooltip', 1)
        element_css="#queryTreeColumn table>tbody>tr:nth-child(14)"
        visual.wait_for_visible_text(element_css, 'FST.COUNTRY', 30)
           
        """
        Step 06. Verify query pane   
        """
        visual.verify_field_listed_under_querytree('Vertical Axis', 'RETAIL_COST', position, "Step 6.1")
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'COUNTRY', position, "Step 6.2")
        visual.verify_field_listed_under_querytree('Tooltip', 'FST.COUNTRY', position, "Step 6.3")
        
        """
        Step 07. Hover on a bar and verify COUNTRY field value display twice in tooltip
        """
        expected_tooltip_list=['COUNTRY:W GERMANY', 'RETAIL_COST:64,732', 'COUNTRY:W GERMANY', 'Filter Chart', 'Exclude from Chart', 'Drill down to CAR']
#         expected_tooltip_list=['COUNTRY:W GERMANY', 'RETAIL_COST:64,732', 'FST COUNTRY:W GERMANY', 'Filter Chart', 'Exclude from Chart', 'Drill down to CAR']
        visual.verify_tooltip('riser!s0!g4!mbar!', expected_tooltip_list,'Step 7.1: Verify Tooltip')
        time.sleep(sleep_time)  
        """
        Step 08. Hover over ENGLAND bar > Drill Down
        """
        visual.select_tooltip("riser!s0!g0!mbar!", "Drill down to CAR")
        
        parent_css="#MAINTABLE_wbody1 text[class^='xaxisOrdinal-title']"
        visual.wait_for_visible_text(parent_css, visble_element_text='CAR', time_out=50)
        
        """
        Step 09. Verify query added to filter pane
        """
        visual.verify_field_in_filterbox('COUNTRY', position, "Step 9.1")
        
        """
        Step 10. Verify Country drill down to car
        """
   
        visual.verify_x_axis_title(['CAR'], msg='Step 10.1')
        visual.verify_y_axis_title(['RETAIL_COST'], msg='Step 10.2')
        expected_xaxis_label=['JAGUAR', 'JENSEN', 'TRIUMPH']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 10.3')
        expected_yaxis_label=['0', '4K', '8K', '12K', '16K', '20K', '24K']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 10.4')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 3, msg='Step 10.5')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!']", "bar_blue", msg='Step 10.6')
        
        """
        Step 11. Hover on a bar and verify tooltip
        """
        expected_tooltip_list=['CAR:JAGUAR', 'RETAIL_COST:22,369', 'COUNTRY:ENGLAND','Filter Chart', 'Exclude from Chart', 'Drill up to COUNTRY','Drill down to MODEL']
#         expected_tooltip_list=['CAR:JAGUAR', 'RETAIL_COST:22,369', 'FST COUNTRY:ENGLAND', 'Filter Chart', 'Exclude from Chart', 'Drill up to COUNTRY', 'Drill down to MODEL']
        visual.verify_tooltip('riser!s0!g0!mbar!', expected_tooltip_list,'Step 11.1: Verify Tooltip')
        
        """
        Step 12. Click Run in the toolbar 
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        
        """
        Step 13. Verify output
        """
        parent_css="#MAINTABLE_wbody1 text[class*='xaxis']"
        visual.wait_for_number_of_element(parent_css, 4, time_out=50)
   
        visual.verify_x_axis_title(['CAR'], msg='Step 13.1')
        visual.verify_y_axis_title(['RETAIL_COST'], msg='Step 13.2')
        expected_xaxis_label=['JAGUAR', 'JENSEN', 'TRIUMPH']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 13.3')
        expected_yaxis_label=['0', '4K', '8K', '12K', '16K', '20K', '24K']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 13.4')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 3, msg='Step 13.5')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!']", "bar_blue", msg='Step 13.6')
        
#         visual.take_run_window_snapshot(Test_Case_ID, '13')
        
        """
        Step 14. Close the output window
        """
        visual.switch_to_previous_window()
        
        """
        Step 15: Click "Save" in the toolbar > Type C2141625  > Click "Save" in the Save As dialog
        """
    
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
        Step 16: Logout of the IA API using the following URL: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(sleep_time)
        
if __name__ == '__main__':
    unittest.main()