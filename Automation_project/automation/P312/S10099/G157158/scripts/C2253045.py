""" ------------------------------------------------------------------------------------------------------------
@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2253045
TestCase Name : BUE: Grid (from UI at run time) and drill down don't match (cache?)

----------------------------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.visualization import Visualization

class C2253045_TestClass(BaseTestCase):

    def test_C2253045(self):
        
        """
         TESTCASE VARIABLES
        """
        TestCase_ID='C2253045'
        visual=Visualization(self.driver)
        
        def verify_bar_chart(xaxis_title, xaxis_labels, yaxis_labels, total_risers, step_num):
            visual.verify_x_axis_title(xaxis_title, msg='Step ' + step_num + '.1')
            visual.verify_y_axis_title(['DEALER_COST'], msg='Step ' + step_num + '.2')
            visual.verify_x_axis_label(xaxis_labels, msg='Step ' + step_num + '.3')
            visual.verify_y_axis_label(yaxis_labels, msg='Step ' + step_num + '.4')
            visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, total_risers, msg='Step ' + step_num + '.5')
            visual.verify_chart_color_using_get_css_property("rect[class='riser!s0!g0!mbar!']", 'bar_blue1',  msg='Step ' + step_num + '.6 ')
            
        """
            Step 01 : Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS8358&tool=idis&master=baseapp/carolap
        """
        visual.invoke_visualization_using_api('baseapp/carolap')
        
        """
            Step 02 : Double click DEALER_COST & COUNTRY
        """
        visual.double_click_on_datetree_item('DEALER_COST', 1)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='yaxis-title']", 'DEALER_COST', 10)
        
        visual.double_click_on_datetree_item('COUNTRY->COUNTRY->COUNTRY', 3)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", 'COUNTRY', 10)
        
        """
            Step 03 : Verify axis label values
        """
        verify_bar_chart(['COUNTRY'], ['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY'], ['0', '10K', '20K', '30K', '40K', '50K', '60K'], 5, '03')
        visual.take_preview_snapshot(TestCase_ID, '03')
        
        """
            Step 04 : Verify query pane
        """
        visual.verify_field_listed_under_querytree('Vertical Axis', 'DEALER_COST', 1, 'Step 04.1 ')
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'COUNTRY', 1, 'Step 04.2 ')
        
        """
            Step 05 : Verify each bar riser values
        """
        ENGLAND_TOOLTIP=['COUNTRY:ENGLAND', 'DEALER_COST:37,853', 'Filter Chart', 'Exclude from Chart', 'Drill down to CAR']
        FRANCE_TOOLTIP=['COUNTRY:FRANCE', 'DEALER_COST:4,631', 'Filter Chart', 'Exclude from Chart', 'Drill down to CAR']
        ITALY_TOOLTIP=['COUNTRY:ITALY', 'DEALER_COST:41,235', 'Filter Chart', 'Exclude from Chart', 'Drill down to CAR']
        JAPAN_TOOLTIP=['COUNTRY:JAPAN', 'DEALER_COST:5,512', 'Filter Chart', 'Exclude from Chart', 'Drill down to CAR']
        WGERMANY_TOOLTIP=['COUNTRY:W GERMANY', 'DEALER_COST:54,563', 'Filter Chart', 'Exclude from Chart', 'Drill down to CAR']
        visual.verify_tooltip('riser!s0!g0!mbar!', ENGLAND_TOOLTIP, 'Step 05.1 : Verify ENGLAND riser tooltip')
        visual.verify_tooltip('riser!s0!g1!mbar!', FRANCE_TOOLTIP, 'Step 05.2 : Verify FRANCE riser tooltip')
        visual.verify_tooltip('riser!s0!g2!mbar!', ITALY_TOOLTIP, 'Step 05.3 : Verify ITALY riser tooltip')
        visual.verify_tooltip('riser!s0!g3!mbar!', JAPAN_TOOLTIP, 'Step 05.4 : Verify JAPAN riser tooltip')
        visual.verify_tooltip('riser!s0!g4!mbar!', WGERMANY_TOOLTIP, 'Step 05.5 : Verify W GERMANY riser tooltip')
        
        """
            Step 06 : Click Run in the toolbar
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", 'COUNTRY', 20)
        
        """
            Step 06.1 : Verify Run window output
        """
        verify_bar_chart(['COUNTRY'], ['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY'], ['0', '10K', '20K', '30K', '40K', '50K', '60K'], 5, '06')
        
        """
        Step 07 : Select the grid from the UI icons at the bottom right of window.
        """
        visual.select_bottom_right_run_menu_options('show_report_css')
        
        """    
            Step 08  : Verify data matches the chart values
        """
        #visual.create_visualization_tabular_report(TestCase_ID+'_DataSet_01.xlsx')
        visual.verify_visualization_tabular_report(TestCase_ID+'_DataSet_01.xlsx', msg='Step 08.1 :')
        
        """
            Step 09 : Select the grid again to display chart.
        """
        visual.select_bottom_right_run_menu_options('show_report_css',  toggle_button_click='no')
        
        """
            Step 10 : Hover over ENGLAND> Drill Down
        """
        visual.select_tooltip('riser!s0!g0!mbar!', 'Drill down to CAR')
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", 'CAR', 15)
        
        """
            Step 11 : Verify Verify country drilldown to CAR
        """
        verify_bar_chart(['CAR'], ['JAGUAR', 'JENSEN', 'TRIUMPH'], ['0', '4K', '8K', '12K', '16K', '20K'], 3, '11')
        visual.take_run_window_snapshot(TestCase_ID, '11')
        
        """
            Step 12 : Verify each bar riser values
        """
        JAGUAR_TOOLTIP=['CAR:JAGUAR', 'DEALER_COST:18,621', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill up to COUNTRY', 'Drill down to MODEL']
        JENSEN_TOOLTIP=['CAR:JENSEN', 'DEALER_COST:14,940', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill up to COUNTRY', 'Drill down to MODEL']
        TRIUMPH_TOOLTIP=['CAR:TRIUMPH', 'DEALER_COST:4,292', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill up to COUNTRY', 'Drill down to MODEL']
        visual.verify_tooltip('riser!s0!g0!mbar!', JAGUAR_TOOLTIP, 'Step 12.1 : Verify ENGLAND riser tooltip')
        visual.verify_tooltip('riser!s0!g1!mbar!', JENSEN_TOOLTIP, 'Step 12.2 : Verify FRANCE riser tooltip')
        visual.verify_tooltip('riser!s0!g2!mbar!', TRIUMPH_TOOLTIP, 'Step 12.3 : Verify ITALY riser tooltip')
        
        """
            Step 13 : Expand the UI icons at bottom right of window > click the grid
        """
        visual.select_bottom_right_run_menu_options('show_report_css')
        
        """
            Step 14 : verify Grid display 3 row values
        """
        #visual.create_visualization_tabular_report(TestCase_ID+'_DataSet_02.xlsx', table_css="#MAINTABLE_wbody3 .arPivot table > tbody > tr")
        visual.verify_visualization_tabular_report(TestCase_ID+'_DataSet_02.xlsx', msg='Step 14.1 :', table_css="#MAINTABLE_wbody3 .arPivot table > tbody > tr")
        
        """
            Step 15 : verify Grid display 3 row values
        """
        visual.switch_to_previous_window()
        
        """
            Step 16 : Click "Save" in the toolbar > Type C2141653 > Click "Save" in the Save As dialog
        """
        visual.save_as_visualization_from_menubar(TestCase_ID)
        
        """
            Step 17 : Logout of the IA API using the following URL.  http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        visual.logout_visualization_using_api()