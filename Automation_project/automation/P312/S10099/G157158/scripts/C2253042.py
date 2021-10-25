'''
Created on Feb 15, 2018
@author: Praveen Ramkumar

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2253042
Test_Case Name : IA-4297:BUE: If same field is in horizontal axis and tooltip, tooltip displays garbage on drilldown
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization
from common.pages import core_metadata

class C2253042_TestClass(BaseTestCase):

    def test_C2253042(self):
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = "C2253042"
        total_no_of_riser_css="#MAINTABLE_wbody1 rect[class^='riser']"  
        wait_time_in_sec=120
        
        """
        CLASS & OBJECTS        
        """
        visual = visualization.Visualization(self.driver)
        metadataobj = core_metadata.CoreMetaData(self.driver)
        
        def verify_bar_chart(x_title,y_title,x_label, y_label,riser,total_risers,tooltip, step_num):
            visual.verify_x_axis_title(x_title, msg='Step ' + step_num + '.1:'+' Verify x-axis title')
            visual.verify_y_axis_title(y_title, msg='Step ' + step_num + '.2:'+' Verify y-axis title')
            visual.verify_x_axis_label(x_label, msg='Step ' + step_num + '.3:'+' Verify x-axis label')
            visual.verify_y_axis_label(y_label, msg='Step ' + step_num + '.4:'+' Verify y-axis label')
            visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, total_risers, msg='Step ' + step_num + '.5:'+' Verify number of risers')
            visual.verify_chart_color_using_get_css_property("rect[class*='"+riser+"']", 'lochmara',  msg='Step ' + step_num + '.6:'+' Verify riser color')
            #visual.verify_tooltip(riser,tooltip,msg='Step' + step_num + '.7:'+' Verify riser tooltip')
            
        """
        Step1: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS8358&tool=idis&master=baseapp/carolap
        """
        visual.invoke_visualization_using_api('ibisamp/carolap')
        
        """
        Step02: Double click RETAIL_COST & COUNTRY
        """
        visual.double_click_on_datetree_item('RETAIL_COST', 1)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='yaxis-title']", "RETAIL_COST", 45)
        metadataobj.double_click_on_data_filed('Dimensions->COUNTRY->COUNTRY->COUNTRY', field_position=3)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", "COUNTRY", 45)
        
        """
        Step03: Verify axis label values
        """
        no_of_riser=5
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, wait_time_in_sec) 

        x_title=['COUNTRY']
        y_title=['RETAIL_COST']
        expected_xaxis_labels=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        expected_yaxis_labels=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        England_riser="riser!s0!g0!mbar!"
        England_riser_tooltip=['COUNTRY:ENGLAND', 'RETAIL_COST:45,319', 'Filter Chart', 'Exclude from Chart', 'Drill down to CAR']
        verify_bar_chart(x_title,y_title,expected_xaxis_labels,expected_yaxis_labels,England_riser,no_of_riser,England_riser_tooltip, '03')        
        
        """
        Step04: Hover over "ENGLAND" bar.
        Verify the tool tip:
        """     
        England_riser="riser!s0!g0!mbar!"
        England_riser_tooltip=['COUNTRY:ENGLAND', 'RETAIL_COST:45,319', 'Filter Chart', 'Exclude from Chart', 'Drill down to CAR']
        visual.verify_tooltip(England_riser,England_riser_tooltip,msg='Step 04.1 Verify Boom_Box_riser tooltip')
     
        """
        Step05:Drag COUNTRY to Tooltip bucket
        """
        visual.drag_field_from_data_tree_to_query_pane("COUNTRY", 3, "Tooltip", 1)
        
        """
        Step06:Verify query pane
        """
        visual.verify_field_listed_under_querytree('Vertical Axis', 'RETAIL_COST', 1, "Step 06.1: Verify RETAIL_COST in Query Pane")  
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'COUNTRY', 1, "Step 06.2: Verify COUNTRY in Query Pane") 
        visual.verify_field_listed_under_querytree('Tooltip', 'FST.COUNTRY', 1, "Step 06.3: Verify FST.COUNTRY in Query Pane")
         
        """
        Step07:Hover over ENGLAND bar > Drill Down
        Verify query added to filter pane
        """
        
        England_riser="riser!s0!g0!mbar"
        visual.select_tooltip(England_riser, 'Drill down to CAR')
        
        visual.verify_field_in_filterbox('COUNTRY', 1, "Step 07.1: Verify COUNTRY added to Filter pane")
        
        """
        Step08:Hover over "JAGUAR" bar.
        Verify the tool tip:
        """
        Jaguar_riser="riser!s0!g0!mbar!"
        Jaguar_tooltip=['CAR:JAGUAR', 'RETAIL_COST:22,369', 'FST COUNTRY:ENGLAND', 'Filter Chart', 'Exclude from Chart', 'Drill up to COUNTRY', 'Drill down to MODEL']
        visual.verify_tooltip(Jaguar_riser,Jaguar_tooltip,msg='Step 08.1 Verify Jaguar_tooltip')
        
        """
        Step09:Click Run in the toolbar
        Verify output
        Step 10:Close the output window
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        no_of_riser1=3
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser1, wait_time_in_sec) 
        expected_xaxis_labels=['JAGUAR', 'JENSEN', 'TRIUMPH']
        expected_yaxis_labels=['0', '4K', '8K', '12K', '16K', '20K', '24K']
        verify_bar_chart(['CAR'],['RETAIL_COST'],expected_xaxis_labels,expected_yaxis_labels,Jaguar_riser,no_of_riser1,Jaguar_tooltip, '09')  
#         visual.take_run_window_snapshot(Test_Case_ID, '11')
        visual.switch_to_previous_window()
        
        """
        Step13 :Click "Save" in the toolbar > Type C2141649 > Click "Save" in the Save As dialog
        Step15: Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser1, wait_time_in_sec)  
        visual.save_visualization_from_top_toolbar(Test_Case_ID)


if __name__ == '__main__':
    unittest.main()