'''
Created on Oct 24, 2017

@author: Pavithra

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10670&group_by=cases:section_id&group_id=168200&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2313689
TestCase Name = AHTML: Horizontal Dual-Axis Stacked Line Chart procedure creation.
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon,visualization_resultarea,active_miscelaneous,visualization_metadata,ia_ribbon,ia_resultarea
from common.lib import utillity

class C2313689_TestClass(BaseTestCase):

    def test_C2313689(self):
        
        Test_Case_ID="C2313689"
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
        ia_resultobj= ia_resultarea.IA_Resultarea(self.driver)
        time_out=15
        default_chart_css="#TableChart_1 rect[class^='riser']"
        default_chart_expected_number=25 
            
        """
            Step 01:Launch new chart using the IA API
            http://machine:port/{alias}/ia?tool=Report&master=ibisamp/car&item=IBFS%3A%2FWFC%2FRepository%2FS10670%2FDualAxisBucketizedLineCharts.
        """
        utillobj.infoassist_api_login('Chart', 'ibisamp/car', 'P116/S10670', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element(default_chart_css, default_chart_expected_number, 65)
     
        """
            Step 02:Create a new Chart using the CAR file.
            Select Active Report as the format.
            From the Format tab, select the Other option.
        """
        ribbonobj.change_output_format_type('active_report', location='Home')
        parent_css="#TableChart_1 g.chartPanel"
        utillobj.synchronize_with_number_of_element(parent_css, 1, time_out)
        ribbonobj.select_ribbon_item('Format', 'Other')
        time.sleep(5)
        
        """
            Step 03:Select the Horizontal Dual-Axis Stacked Line Chart option.
            Click OK.
            Expect to see the following Preview pane, including axis on both sides of the canvas.
        """
        ia_ribbobj.select_other_chart_type('line', 'horizontal_dual_axis_stacked_line', 11, ok_btn_click=True)
        time.sleep(5)

        """
            Expect to see the following Preview pane, including axis on both sides of the canvas.
        """
        expected_xval_list=['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4']
        expected_yval1_list=['0', '20', '40', '60', '80', '100', '120']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 03.1: Verify XY labels")
        expected_yval2_list=['0', '10', '20', '30', '40', '50', '60', '70', '80']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 03.2: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 5, 'Step 03.3: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mline!", "bar_blue1", "Step 03.4: Verify  bar color",attribute_type='stroke')
        legend=["Series0","Series1","Series2","Series3","Series4"]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 03.5: Verify Y-Axis legend")

        """
            Step 04:Add CAR to the Vertical axis.
            Add DEALER_COST & WEIGHT to Horizontal Axis 1.
            Add LENGTH & HEIGHT to Horizontal axis 2.
        """
        metadataobj.datatree_field_click('CAR', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(7) td"
        utillobj.synchronize_with_visble_text(parent_css, visble_element_text='CAR', expire_time=time_out)
        
        metadataobj.datatree_field_click('DEALER_COST', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(9) td"
        utillobj.synchronize_with_visble_text(parent_css, visble_element_text='DEALER_COST', expire_time=time_out)
        
        metadataobj.datatree_field_click('WEIGHT', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(10) td"
        utillobj.synchronize_with_visble_text(parent_css, visble_element_text='WEIGHT', expire_time=time_out)
        
        metadataobj.drag_drop_data_tree_items_to_query_tree('LENGTH', 1, 'Horizontal Axis 2',0)
        parent_css="#queryTreeWindow table tr:nth-child(12) td"
        utillobj.synchronize_with_visble_text(parent_css, visble_element_text='LENGTH', expire_time=time_out)
        
        metadataobj.drag_drop_data_tree_items_to_query_tree('HEIGHT', 1, 'Horizontal Axis 2', 1)
        parent_css="#queryTreeWindow table tr:nth-child(13) td"
        utillobj.synchronize_with_visble_text(parent_css, visble_element_text='HEIGHT', expire_time=time_out)
        
        """
            Expect to see the following Preview pane.
        """
        
        resobj.verify_xaxis_title("TableChart_1", "CAR", "Step 04.1: Verify -xAxis Title")   
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 04.2: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 04.3: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 4, 'Step 04.4: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mline!", "bar_blue1", "Step 04.5: Verify  bar color",attribute_type='stroke')
        legend=['DEALER_COST', 'WEIGHT', 'LENGTH', 'HEIGHT']
        resobj.verify_riser_legends("TableChart_1", legend, "Step 04.6: Verify Y-Axis legend")

        """
            Step 05:Click the Run button.
            Hover over the point on the left line for Alfa Romeo.
            Hover over the upper right bar for Alfa Romeo.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        parent_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, time_out)
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0 text[class^='xaxis'][class$='title']", "CAR", 15)
        
        """
            Expect to see the following Tooltip information.
            Dealer_Cost uses the bottom axis scale and has a value of 16,235.
        """
        expected_tooltip_list=['CAR:ALFA ROMEO', 'DEALER_COST:16,235', 'Filter Chart', 'Exclude from Chart']
        miscelaneousobj.select_or_verify_marker_tooltip(marker_class='marker!s0!g0!mmarker!',verify_tooltip_list=expected_tooltip_list, msg='Step 05.1 : Verify tooltip')
        
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR", "Step 05.2: Verify -xAxis Title")       
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 05.3: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 05.4: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 4, 'Step 05.5: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue1", "Step 05.6: Verify  bar color",attribute_type='stroke')
        legend=['DEALER_COST', 'WEIGHT', 'LENGTH', 'HEIGHT']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 05.7: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, WEIGHT, LENGTH, HEIGHT by CAR', 'Step 05.8: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.9: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.10: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.11: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        """
            Height uses the top axis scale and has a value of 158.
        """
        expected_tooltip_list=['CAR:  ALFA ROMEO', 'HEIGHT:  159', 'Filter Chart', 'Exclude from Chart']
        ia_resultobj.verify_marker_tooltip('MAINTABLE_wbody0', 'marker!s3!g0!mmarker!', expected_tooltip_list, 'Step 5.12: Verify tooltip')
        
        """
            Step 06:Hover over the point on the left line for Triumph.
            Hover over the point on the right line for Triumph.
            Expect to see the following Tooltip information.
            Dealer_Cost uses the bottom axis scale and has a value of 4,292.
        """
        expected_tooltip_list=['CAR:TRIUMPH', 'DEALER_COST:4,292', 'Filter Chart', 'Exclude from Chart']  
        miscelaneousobj.select_or_verify_marker_tooltip(marker_class='marker!s0!g9!mmarker!',verify_tooltip_list=expected_tooltip_list, msg='Step 06.1 : Verify tooltip')          
        
        """
            Expect to see the following Tooltip information.
            Height uses the top axis scale and has a value of 49.
        """
        expected_tooltip_list=['CAR:TRIUMPH', 'HEIGHT:50', 'Filter Chart', 'Exclude from Chart']
        miscelaneousobj.select_or_verify_marker_tooltip(marker_class='marker!s3!g9!mmarker!',verify_tooltip_list=expected_tooltip_list, msg='Step 06.2 : Verify tooltip')

        """
            Step 07 :Save the procedure as Horizontal_Stacked_Line and exit IA+.
        """
        
        time.sleep(2)
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step_06', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        
        ribbonobj.select_tool_menu_item('menu_save')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        """
            Step 08 : Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()