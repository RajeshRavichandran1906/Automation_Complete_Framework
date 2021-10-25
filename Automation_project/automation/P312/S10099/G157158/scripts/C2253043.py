'''
Created on Feb 17, 2018
@author: Praveen Ramkumar

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2253043
Test_Case Name : IA-4254:BUE: If hierarchy field in color, drill down gives wrong results
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization
from common.pages import core_metadata

class C2253043_TestClass(BaseTestCase):

    def test_C2253043(self):
        
        Test_Case_ID = "C2253043"
        total_no_of_riser_css="#MAINTABLE_wbody1 rect[class^='riser']"  
        wait_time_in_sec=120
        visual = visualization.Visualization(self.driver)
        
        def verify_bar_chart(x_title,y_title,x_label, y_label,riser,total_risers,tooltip, step_num):
            visual.verify_x_axis_title(x_title, msg='Step' + step_num + '.1:'+' Verify x-axis title')
            visual.verify_y_axis_title(y_title, msg='Step' + step_num + '.2:'+' Verify y-axis title')
            visual.verify_x_axis_label(x_label, msg='Step ' + step_num + '.3'+' Verify x-axis label')
            visual.verify_y_axis_label(y_label, msg='Step ' + step_num + '.4'+' Verify y-axis label')
            visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, total_risers, msg='Step' + step_num + '.5:'+' Verify number of risers')
            visual.verify_chart_color_using_get_css_property("rect[class*='"+riser+"']", 'bar_blue',  msg='Step' + step_num + '.6:'+' Verify riser color')
            #visual.verify_tooltip(riser,tooltip,msg='Step' + step_num + '.7:'+' Verify riser tooltip')
            
        """
        Step1: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS8358&tool=idis&master=baseapp/carolap
        """
        visual.invoke_visualization_using_api('ibisamp/carolap')
        
        """
        Step02: Double click DEALER_COST & BODYTYPE
        """
        visual.double_click_on_datetree_item('DEALER_COST', 1)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='yaxis-title']", "DEALER_COST", 45)
        visual.double_click_on_datetree_item('BODYTYPE->BODYTYPE->BODYTYPE', 3)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", "BODYTYPE", 45)
        
        """
        Step03: Verify axis label values
        Step04: Verify each bar riser values

                BODYTYPE:DEALER_COST
                
                CONVERTIBLE:7,427
                COUPE:30,660
                HARDTOP:4,292
                ROADSTER:5,660
                SEDAN:95,755     
        """
        
        no_of_riser=5
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, wait_time_in_sec) 
        x_title=['BODYTYPE']
        y_title=['DEALER_COST']
        expected_xaxis_labels=['CONVERTIBLE', 'COUPE', 'HARDTOP', 'ROADSTER', 'SEDAN']
        expected_yaxis_labels=['0', '20K', '40K', '60K', '80K', '100K', '120K']
        England_riser="riser!s0!g1!mbar!"
        England_riser_tooltip=['BODYTYPE:COUPE', 'DEALER_COST:30,660', 'Filter Chart', 'Exclude from Chart', 'Drill down to LENGTH']
        verify_bar_chart(x_title,y_title,expected_xaxis_labels,expected_yaxis_labels,England_riser,no_of_riser,England_riser_tooltip, '03.1')        
        
        CONVERTIBLE_riser="riser!s0!g0!mbar!"
        CONVERTIBLE_riser_tooltip=['BODYTYPE:CONVERTIBLE', 'DEALER_COST:7,427', 'Filter Chart', 'Exclude from Chart', 'Drill down to LENGTH']
        COUPE_riser="riser!s0!g1!mbar!"
        COUPE_tooltip=['BODYTYPE:COUPE', 'DEALER_COST:30,660', 'Filter Chart', 'Exclude from Chart', 'Drill down to LENGTH']
        HARDTOP_riser="riser!s0!g2!mbar!"
        HARDTOP_tooltip=['BODYTYPE:HARDTOP', 'DEALER_COST:4,292', 'Filter Chart', 'Exclude from Chart', 'Drill down to LENGTH']
        ROADSTER_riser="riser!s0!g3!mbar"
        ROADSTER_tooltip=['BODYTYPE:ROADSTER', 'DEALER_COST:5,660', 'Filter Chart', 'Exclude from Chart', 'Drill down to LENGTH']
        SEDAN_riser="riser!s0!g4!mbar"
        SEDAN_tooltip=['BODYTYPE:SEDAN', 'DEALER_COST:95,755', 'Filter Chart', 'Exclude from Chart', 'Drill down to LENGTH']
        visual.verify_tooltip(CONVERTIBLE_riser,CONVERTIBLE_riser_tooltip,msg='Step04.1 Verify Boom_Box_riser tooltip')
        visual.verify_tooltip(COUPE_riser,COUPE_tooltip,msg='Step04.2 Verify CRT_TV_riser tooltip')
        visual.verify_tooltip(HARDTOP_riser,HARDTOP_tooltip,msg='Step04.3 Verify Universal_Remote_Controls_riser tooltip')
        visual.verify_tooltip(ROADSTER_riser,ROADSTER_tooltip,msg='Step04.4 Verify Video_Editing_riser tooltip')
        visual.verify_tooltip(SEDAN_riser,SEDAN_tooltip,msg='Step04.5 Verify iPod_Docking_Stationy_riser tooltip')
        
        """
        Step05:Drag COUNTRY to Color bucket
        """
        visual.drag_field_from_data_tree_to_query_pane("COUNTRY", 3, "Color", 1)
        
        """
        Step06:Verify query pane
        """
        visual.verify_field_listed_under_querytree('Vertical Axis', 'DEALER_COST', 1, "Step06.1: Verify RETAIL_COST in Query Pane")  
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'BODYTYPE', 1, "Step06.2: Verify COUNTRY in Query Pane") 
        visual.verify_field_listed_under_querytree('Color BY', 'COUNTRY', 1, "Step06.2: Verify COUNTRY in Query Pane")
        
         
        """
        Step07:Verify color legend title and values
        """                 
#         verify_bar_chart(x_title,y_title,expected_xaxis_labels,expected_yaxis_labels,England_riser,no_of_riser,England_riser_tooltip, '07.1')
        expected_legend_list=['COUNTRY','ENGLAND','FRANCE','ITALY','JAPAN','W GERMANY']
        visual.verify_legends(expected_legend_list,"#MAINTABLE_wbody1_f",2,"Step 7:verify legend")        
         
        """
        Step08:Hover over one of the bars(SEDAN:WGERMANY) > Drill Down > CAR
        """
        
        SEDAN_riser="riser!s4!g4!mbar!"
        visual.select_tooltip(SEDAN_riser, 'Drill down to->CAR')
        
        """
        Step09:Verify query added to filter pane
        """
        visual.verify_field_in_filterbox('COUNTRY and BODYTYPE', 1, "Step09: Verify COUNTRY added to Filter pane")
   
        """
        Step10:Verify drill down bar riser values
        """
        SEDAN_riser="riser!s1!g0!mbar!"
        SEDAN_riser_tooltip=['BODYTYPE:SEDAN', 'DEALER_COST:49,500', 'CAR:BMW', 'Filter Chart', 'Exclude from Chart', 'Drill up to COUNTRY', 'Drill down to']
        SEDAN_riser1="riser!s0!g0!mbar!"
        SEDAN_riser_tooltip1=['BODYTYPE:SEDAN', 'DEALER_COST:5,063', 'CAR:AUDI', 'Filter Chart', 'Exclude from Chart', 'Drill up to COUNTRY', 'Drill down to']
        visual.verify_tooltip(SEDAN_riser,SEDAN_riser_tooltip,msg='Step10.1 Verify SEDAN_riser_tooltip tooltip')
        visual.verify_tooltip(SEDAN_riser1,SEDAN_riser_tooltip1,msg='Step10.2 Verify SEDAN_riser_tooltip1')
        
        """
        Step11:Click Run in the toolbar
        Step12:Verify output
        step 13:Close the output window
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        no_of_riser1=2
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser1, wait_time_in_sec) 
        expected_xaxis_labels=['SEDAN']
        expected_yaxis_labels=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        visual.verify_x_axis_label(expected_xaxis_labels,'#MAINTABLE_wbody1_f',"svg > g text[class^='xaxis'][class*='labels']",2, msg='Step 12 x axis label')
        visual.verify_y_axis_label(expected_yaxis_labels,'#MAINTABLE_wbody1_f',"svg > g text[class^='yaxis-labels']",msg='step 12 y axis label')
        SEDAN_riser1="riser!s0!g0!mbar!"
        #SEDAN_riser_tooltip1=['BODYTYPE:COUPE', 'DEALER_COST:30,660', 'Filter Chart', 'Exclude from Chart', 'Drill down to LENGTH']
        #visual.verify_tooltip(SEDAN_riser,SEDAN_riser_tooltip,msg='Step12.1 Verify SEDAN_riser_tooltip tooltip')
        expected_legend_list=['CAR','AUDI','BMW']
        visual.verify_legends(expected_legend_list,"#MAINTABLE_wbody1_f",2,"Step 12.2:verify legend")
        visual.verify_chart_color_using_get_css_property("rect[class*='riser!s0!g0!mbar']", 'bar_blue',  msg='Step12.2: Verify riser color')
        visual.take_run_window_snapshot(Test_Case_ID, '12')
        visual.switch_to_previous_window()
        
        """
        Step14:Click "Save" in the toolbar > Type C2141649 > Click "Save" in the Save As dialog
        Step15: Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser1, wait_time_in_sec)  
        visual.save_as_visualization_from_menubar(Test_Case_ID)


if __name__ == '__main__':
    unittest.main()
