'''
Created on Aug 22, 2016

@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050536

Test case Name = Verify Pivot Table status for problem - Filter/Equals options are not accessible.

'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_tools, visualization_metadata,visualization_ribbon,visualization_resultarea,active_chart_rollup
from common.lib import utillity
import unittest,time


class C2050536_TestClass(BaseTestCase):

    def test_C2050536(self):
        """
            TESTCASE VARIABLES
        """
        
        """
        Step 01: Right click on folder created in IA and select New > Report and select Reporting server as car
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_toolsobj = active_tools.Active_Tools(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        rollobj=active_chart_rollup.Active_Chart_Rollup(self.driver)
        
        utillobj.infoassist_api_login('report','ibisamp/car','P116/S7068', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#topToolBar #runButton img", 1, 50)
        
        
        """Step 02: Select data from the left pane (Dimensions and Measures) Country, Car, Model & Seats fields."""
        
        ribbonobj.switch_ia_tab('Home')
        ribbonobj.change_output_format_type("active_report")
        time.sleep(3)
        output_type = self.driver.find_element_by_css_selector("#HomeFormatType").text.strip()
        utillobj.asequal('Active Report', output_type, "Step 1: Verify output format as Active report.")
        
        metaobj.datatree_field_click("COUNTRY",2,1)
        time.sleep(3)
        metaobj.datatree_field_click("CAR", 2, 1)
        time.sleep(3)
        metaobj.datatree_field_click("MODEL",2,1)
        time.sleep(3)
        metaobj.datatree_field_click("SEATS",2,1)
        utillobj.synchronize_with_number_of_element("div[class^='x']", 55, 40, 1)
        #See corresponding data is displayed in the Live Preview pane.
        
        
        expected_list= ['COUNTRY','CAR','MODEL','SEATS']
        
        resobj.verify_report_titles_on_preview(4, 4, 'TableChart_1', expected_list, 'Step 02: See corresponding data is displayed in the Live Preview pane.')
        
        """Step 03: Click Run command."""
        
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=3)
        utillobj.synchronize_with_number_of_element("td[id^='I0']", 72, 40, 1) 
        #Expect to see an 18 row report with Country, Car, Model, Seats.
        
        utillobj.verify_data_set('ITableData0','I0r','C2050536_Ds01.xlsx',"Step 03: Expect to see an 18 row report with Country, Car, Model, Seats")
         
        #utillobj.create_data_set('ITableData0','I0r','C2050536_Ds01.xlsx')
        
        
        
        """Step 04: Click the arrow in the heading of column CAR, select Chart, then Pie, then from submenu select MODEL."""
        
        time.sleep(2)
        miscelanousobj.select_menu_items("ITableData0", "1", "Chart","Pie","MODEL")
        
        #Expect to see the following PIE chart
        utillobj.switch_to_default_content(pause=3)
        
        element= driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']")
        utillobj.take_screenshot(element, 'C2050536_Actual_Step05', image_type='actual',x=1, w=-740, h=-370)
        utillobj.switch_to_frame(pause=3) 
        
        #Tooltip & Color
#         active_misobj.verify_active_chart_tooltip('wall1',"riser!s0!g0!mwedge", ['100 LS 2 DOOR AUTO', 'CAR: 1', '5.6% of 18'],"Step 04.1a: Verify Chart piebevel tooltip for Unit Sales")
        utillobj.verify_chart_color('wall1', 'riser!s0!g0!mwedge','bar_blue',"Step 04.1b: Verify the bar riser First Pie Chart Color ")
        time.sleep(5)
        #Pie Label
        resobj.verify_riser_pie_labels_and_legends('wall1', ['CAR'],"Step 04.2: Verify Chart piebevel Label & Legend")
        #Pie Legend
        legend=['100 LS 2 DOOR AUTO', '2000 4 DOOR BERLINA', '2000 GT VELOCE', '2000 SPIDER VELOCE', '2002 2 DOOR', '2002 2 DOOR AUTO', '3.0 SI 4 DOOR', '3.0 SI 4 DOOR AUTO', '504 4 DOOR', '530I 4 DOOR', 'Other']
        resobj.verify_riser_legends('wall1', legend, "Step 04.3: Verify Chart piebevel Legends")
        #Title
        active_misobj.verify_popup_title('wall1', 'CAR BY MODEL', 'Step 04.4: Verify the dialog title')
        #Menu
        rollobj.verify_arChartMenu('wall1',"Step 04.5: Verify the chart Menu")
        
         
         
        """Step 05: Click on Advanced chart icon"""
        
        
        rollobj.click_chart_menu_bar_items('wall1', 6)
        time.sleep(10)
        
        active_toolsobj.chart_rollup_tool_verify_columns('wall2', 'tpanel_0_2_0', 1,['Columns', 'COUNTRY', 'CAR', 'MODEL', 'SEATS'], 'Step 10: Expect to see the following Advanced Chart menu.')
        active_toolsobj.chart_rollup_tool_verify_columns('wall2', 'tpanel_0_2_0', 2,['Group By', 'MODEL'], 'Step 10: Expect to see the following Advanced Chart menu.')
        active_toolsobj.chart_rollup_tool_verify_columns('wall2', 'tpanel_0_2_0', 3,['Measure', 'Count:', 'CAR'], 'Step 10: Expect to see the following Advanced Chart menu.')
        
   
        
if __name__ == '__main__':
    unittest.main()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        