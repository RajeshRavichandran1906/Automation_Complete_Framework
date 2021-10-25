'''
Created on Sep 20, 2017

@author: Pavithra

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10670&group_by=cases:section_id&group_id=168200&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2313567
TestCase Name = AHTML: Vertical Dual-Axis Stacked Bar Chart procedure creation.
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon,visualization_resultarea,active_miscelaneous,visualization_metadata,ia_ribbon
from common.lib import utillity

class C2313567_TestClass(BaseTestCase):

    def test_C2313567(self):
        
        Test_Case_ID="C2313567"
        """
            TESTCASE VARIABLES
        """     
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
       
        time_out = 15
        default_chart_css="#TableChart_1 rect[class^='riser']"
        default_chart_expected_number=25 
            
        """
            Step 01:Launch new chart using the IA API
            http://machine:port/{alias}/ia?tool=Report&master=ibisamp/car&item=IBFS%3A%2FWFC%2FRepository%2FS10670%2FDualAxisBucketizedBarCharts.
        """
        utillobj.infoassist_api_login('Chart', 'ibisamp/car', 'P116/S10670', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element(default_chart_css, default_chart_expected_number, 75)
        
        """
            Step 02:Create a new Chart using the CAR file.
            Select Active Report as the format.
            From the Format tab, select the Other option.
            
            Expect to see the Vertical Dual-Axis Stacked Bars option.
        """
        ribbonobj.change_output_format_type('active_report', location='Home')
        parent_css="#TableChart_1 g.chartPanel"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 15)
        
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbobj.select_other_chart_type('bar', 'vertical_dual_axis_stacked_bars', 11, ok_btn_click=True) 

        """
            Step 03:Select the Vertical Dual-Axis Stacked Bars chart option.
            Click OK.
            Expect to see the following Preview pane, including axis on both sides of the canvas.
        """
        expected_xval_list=['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4']
        expected_yval1_list=['0', '20', '40', '60', '80', '100', '120']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 02.01: Verify XY labels")
        expected_yval2_list=['0', '10', '20', '30', '40', '50', '60', '70', '80']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 02.02: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("TableChart_1", 1, 25, 'Step 02.03: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue1", "Step 02.04: Verify  bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mbar", "bar_green", "Step 02.05: Verify  bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s2!g0!mbar", "med_green", "Step 02.06: Verify  bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s3!g0!mbar", "pale_yellow_2", "Step 02.07: Verify  bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s4!g0!mbar", "brick_red", "Step 02.08: Verify  bar color")
        legend=["Series0","Series1","Series2","Series3","Series4"]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 02.09: Verify Y-Axis legend")
        
        """
            Step 04:Add CAR to the Horizontal axis.
            Add DEALER_COST & WEIGHT to Vertical Axis 1.
            Add LENGTH & HEIGHT to Vertical axis 2.
    
            Expect to see the following Preview pane.

        """
        metadataobj.datatree_field_click('CAR', 2, 0)
        parent_css="#queryTreeWindow"
        utillobj.synchronize_with_visble_text(parent_css, visble_element_text='CAR', expire_time=time_out)
        
        metadataobj.datatree_field_click('DEALER_COST', 2, 0)
        parent_css="#queryTreeWindow"
        utillobj.synchronize_with_visble_text(parent_css, visble_element_text='DEALER_COST', expire_time=time_out)
        
        metadataobj.datatree_field_click('WEIGHT', 2, 0)
        utillobj.synchronize_with_visble_text(parent_css, visble_element_text='WEIGHT', expire_time=time_out)
        
        metadataobj.drag_drop_data_tree_items_to_query_tree_('LENGTH', 1, 'Vertical Axis 2',0)
        utillobj.synchronize_with_visble_text(parent_css, visble_element_text='LENGTH', expire_time=time_out)
        
        metadataobj.drag_drop_data_tree_items_to_query_tree_('HEIGHT', 1, 'Vertical Axis 2', 1)
        utillobj.synchronize_with_visble_text(parent_css, visble_element_text='HEIGHT', expire_time=time_out)
        
        resobj.verify_xaxis_title("TableChart_1", "CAR", "Step 04.01: Verify -xAxis Title")   
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 04.02: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 04.03: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("TableChart_1", 1, 40, 'Step 04.04: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue1", "Step 04.05: Verify  bar color")
        legend=['DEALER_COST', 'WEIGHT', 'LENGTH', 'HEIGHT']
        resobj.verify_riser_legends("TableChart_1", legend, "Step 04.06: Verify Y-Axis legend")
        
        """
            Step 05:Click the Run button.
            Hover over the lower bar on the first set of bars for Alfa Romeo.
            Hover over the upper bar on the first set of bars for Alfa Romeo.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 [class*='riser!s0!g0!mbar!']" , 1, 30)
        
        """"
            Expect to see the following Tooltip information.
            Dealer_Cost uses the left-side axis scale and has a value of 16,235.
        """
        expected_tooltip_list=['CAR:ALFA ROMEO', 'DEALER_COST:16,235', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g0!mbar!", expected_tooltip_list, "Step 05.01: Verify bar value")
        
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR", "Step 05.02: Verify -xAxis Title")  
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 05.03: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 05.04: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 40, 'Step 05.05: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue1", "Step 05.06: Verify  bar color")
        legend=['DEALER_COST', 'WEIGHT', 'LENGTH', 'HEIGHT']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 05.07: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, WEIGHT, LENGTH, HEIGHT by CAR', 'Step 05.08: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.09: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.10: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.11: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        """
            Weight uses the left-side and has a value of 7,215.
            The total is 23,450 and maps to the left-side scale.
        """
        expected_tooltip_list=['CAR:ALFA ROMEO', 'WEIGHT:7,215', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s1!g0!mbar!", expected_tooltip_list, "Step 05.12: Verify bar value")
        time.sleep(3)

        """
            Step 06:Hover over the lower bar of the last set of bars for Triumph.
            Hover over the upper bar of the last set of bars for Triumph.
            Expect to see the following Tooltip information.
            Length uses the right-side axis scale and has a value of 164.
        """
        expected_tooltip_list=['CAR:TRIUMPH', 'LENGTH:165', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s2!g9!ay2!mbar!", expected_tooltip_list, "Step 06.01: Verify bar value")
        
        """
            Expect to see the following Tooltip information.
            Height uses the right-side axis scale and has a value of 49.
            The total is 213 and maps to the right-side scale.
        """
        time.sleep(6)
        parent_elem=driver.find_element_by_css_selector("#MAINTABLE_wbody0")
        utillobj.click_on_screen(parent_elem, 'right')
        time.sleep(2)
        expected_tooltip_list=['CAR:TRIUMPH', 'HEIGHT:50', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s3!g9!ay2!mbar!", expected_tooltip_list, "Step 06.02: Verify bar value", cord_type='right')
        time.sleep(2)
        
        """
            Step 07:Save the procedure as Vertical_Dual_Axis_Stacked_Bar and exit IA+.
        """
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        """
            Step 08:Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == '__main__':
    unittest.main() 