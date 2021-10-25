'''
Created on Sep 21, 2017

@author: Pavithra/Updated by : Bhagavathi

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10670&group_by=cases:section_id&group_id=168200&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2313568
TestCase Name = AHTML: Horizontal Dual-Axis Clustered Bar Chart procedure creation.
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon,visualization_resultarea,active_miscelaneous,visualization_metadata,ia_ribbon
from common.lib import utillity

class C2313568_TestClass(BaseTestCase):

    def test_C2313568(self):
        
        Test_Case_ID="C2313568"
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
        
        default_chart_css="#TableChart_1 rect[class^='riser']"
        default_chart_expected_number=25
            
        """     
        Step 01:Launch new chart using the IA API
        http://machine:port/{alias}/ia?tool=Report&master=ibisamp/car&item=IBFS%3A%2FWFC%2FRepository%2FS10670%2FDualAxisBucketizedBarCharts.
        """
        utillobj.infoassist_api_login('Chart', 'ibisamp/car', 'P116/S10670', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element(default_chart_css, default_chart_expected_number, 65)
        
        """
            Step 02:Create a new chart using the CAR file.
            Select Active Report as the format.
            From the Format tab, select the Other option.
            
            Expect to see the Horizontal Dual-Axis Clustered Bars option.
        """
        ribbonobj.change_output_format_type('active_report', location='Home')
        parent_css="#TableChart_1 g.chartPanel"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 15)
        
        ribbonobj.select_ribbon_item('Format', 'Other')
        parent_css="[id^='SelectChartTypeDlg'] [class*='active'] [class*='window-caption'] [class*='bi-label']"
        utillobj.synchronize_with_visble_text(parent_css, 'Selectachart', 15)

        """
            Step 03:Select the Horizontal Dual-Axis Clustered Bars chart option.
                    Click OK.
            
            Expect to see the following Preview pane, including axis on both sides of the canvas.
        """
        ia_ribbobj.select_other_chart_type('bar', 'horizontal_dual_axis_clustered_bars', 16, ok_btn_click=True)
        time.sleep(5)
        
        expected_xval_list=['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4']
        expected_yval1_list=['0', '10', '20', '30', '40', '50']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 02.01: Verify XY labels")
        expected_yval2_list=['0', '5', '10', '15', '20', '25', '30', '35', '40', '45']
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
            Step 04:Add CAR to the Vertical axis.
            Add DEALER_COST to Horizontal Axis 1.
            Add LENGTH to Horizontal axis 2.
        """
        metadataobj.datatree_field_click('CAR', 2, 0)
        parent_css="#queryTreeWindow"
        utillobj.synchronize_with_visble_text(parent_css, "CAR", 15)
        
        metadataobj.datatree_field_click('DEALER_COST', 2, 0)
        utillobj.synchronize_with_visble_text(parent_css, "DEALER_COST", 15)
        
        metadataobj.drag_drop_data_tree_items_to_query_tree_('LENGTH', 1, 'Horizontal Axis 2',0)
        utillobj.synchronize_with_visble_text(parent_css, "LENGTH", 15)
        
        """
            Expect to see the following Preview pane.
        """
        resobj.verify_xaxis_title("TableChart_1", "CAR", "Step 04.01: Verify -xAxis Title")   
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 04.02: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 04.03: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("TableChart_1", 1, 20, 'Step 04.04: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue1", "Step 04.05: Verify  bar color")
        legend=['DEALER_COST', 'LENGTH']
        resobj.verify_riser_legends("TableChart_1", legend, "Step 04.06: Verify Y-Axis legend")

        """
            Step 05:Click the Run button.
            Hover over the top bar for Alfa Romeo.

            Expect to see the following Tooltip information.
            Dealer_Cost uses the bottom axis scale.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        
        parent_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 20)
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 [class*='riser!s0!g0!mbar!']", 1, 40)
        expected_tooltip_list=['CAR:ALFA ROMEO', 'DEALER_COST:16,235', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g0!mbar!", expected_tooltip_list, "Step 05.00: Verify bar value")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR", "Step 05.01: Verify -xAxis Title")
        resobj.verify_yaxis_title('MAINTABLE_wbody0', "DEALER_COST", "Step 05.02: Verify -xAxis Title") 
        resobj.verify_yaxis_title('MAINTABLE_wbody0', "LENGTH", "Step 05.03: Verify -xAxis Title",custom_css="text[class='y2axis-title']")       
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 05.04: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 05.05: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 05.06: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue1", "Step 05.07: Verify  bar color")
        legend=['DEALER_COST','LENGTH']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 05.08: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, LENGTH by CAR', 'Step 05.09: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.10: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.11: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.12: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)

        """
            Step 06:Hover over the bottom bar for Alfa Romeo.
        
            Expect to see the following Tooltip information.
            Length uses the right-side axis scale.
        """
        expected_tooltip_list=['CAR:ALFA ROMEO', 'LENGTH:510', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s1!g0!ay2!mbar!", expected_tooltip_list, "Step 06.01: Verify bar value")
        time.sleep(2)
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)
        
        """
            Step 07:Save the procedure as Horizontal_Cluster_Bar and exit IA+.
        """
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