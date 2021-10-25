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

class C2050537_TestClass(BaseTestCase):

    def test_C2050537(self):
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
        
        
        """Step 02: Select data from the left pane (Dimensions and Measures) Country, Car, Model & Seats fields."""
        ribbonobj.change_output_format_type('active_report')
#         
#         driver.find_element(*VisualizationRibbonLocators.HOME_FORMAT_TYPE).click()
#         time.sleep(3)
#         driver.find_element(*VisualizationRibbonLocators.ACTIVE_REPORT).click()
        
        metaobj.datatree_field_click("COUNTRY",2,1)
        metaobj.datatree_field_click("CAR", 2, 1)
        metaobj.datatree_field_click("MODEL",2,1)
        metaobj.datatree_field_click("SEATS",2,1)
        
        utillobj.synchronize_with_number_of_element("div[class^='x']", 55, 40, 1)
        #See corresponding data is displayed in the Live Preview pane.
        
        expected_list= ['COUNTRY','CAR','MODEL','SEATS']
        
        resobj.verify_report_titles_on_preview(4, 4,'TableChart_1',expected_list, 'Step 02: See corresponding data is displayed in the Live Preview pane.')
        
        """Step 03: Click Run command."""
        
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=3)
        utillobj.synchronize_with_number_of_element("td[id^='I0']", 72, 40, 1)
        
        #WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        
        
        """Step 04: Click the arrow in the heading of column Country and select Chart/Rollup option."""
        
        
        miscelanousobj.select_menu_items("ITableData0", "0", "Chart/Rollup Tool")
        time.sleep(6)
        
        active_toolsobj.chart_rollup_tool_verify_columns('charttoolt1', 'tpanel_0_1_0', 1,['Columns', 'COUNTRY', 'CAR', 'MODEL', 'SEATS'], 'Step 10: Expect to see the following Advanced Chart menu.')
        active_toolsobj.chart_rollup_tool_verify_columns('charttoolt1', 'tpanel_0_1_0', 2,['Group By', 'Drag Column Here'], 'Step 10: Expect to see the following Advanced Chart menu.')
        active_toolsobj.chart_rollup_tool_verify_columns('charttoolt1', 'tpanel_0_1_0', 3,['Measure', 'Drag Column Here'], 'Step 10: Expect to see the following Advanced Chart menu.')
        
 
        """Step 05: Drag Country to Group By and Seats to Measure to verify the Chart/Rollup functionality."""
        
        active_toolsobj.chart_rollup_tool_drag_drop_items('charttoolt1', 'Columns', 'COUNTRY', 1, 'Group By', 0)
        active_toolsobj.chart_rollup_tool_drag_drop_items('charttoolt1', 'Columns', 'SEATS', 1, 'Measure', 0)
        
        driver.find_element_by_css_selector("div.arToolButton").click()
        
        
        #Expect to see the following Bar chart
        utillobj.switch_to_default_content(pause=3)
        #driver.switch_to_default_content()
        element= driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']")
        utillobj.take_screenshot(element, 'C2050537_Actual_Step05', image_type='actual',x=1, w=-700, h=-350)
        
        utillobj.switch_to_frame(pause=3)
        
        #Tooltip & Color
        active_misobj.verify_active_chart_tooltip('wall2',"riser!s0!g0!mbar", ['SEATS: 13', 'X: ENGLAND'],"Step 05.1a: Verify Chart piebevel tooltip for Unit Sales")
        utillobj.verify_chart_color('wall2', 'riser!s0!g0!mbar','bar_blue',"Step 05.1b: Verify the bar riser First Pie Chart Color ")
        time.sleep(5)
        utillobj.verify_chart_color('wall2', 'riser!s0!g0!mbar','bar_blue',"Step 05.1a: Verify the bar riser First Pie Chart Color ")
        #Title
        active_misobj.verify_popup_title('wall2', 'SEATS by COUNTRY', 'Step 05.2: Verify the dialog title')
        #Menu
        rollobj.verify_arChartMenu('wall2',"Step 05.3: Verify the chart Menu")
    
if __name__ == '__main__':
    unittest.main()