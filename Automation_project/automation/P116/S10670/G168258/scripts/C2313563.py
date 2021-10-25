'''
Created on Sep 20, 2017

@author: Pavithra

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10670&group_by=cases:section_id&group_id=168200&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2313563
TestCase Name = AHTML: Vertical Dual-Axis Clustered Bar Chart procedure creation.
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon,visualization_resultarea,active_miscelaneous,visualization_metadata,ia_ribbon
from common.lib import utillity


class C2313563_TestClass(BaseTestCase):

    def test_C2313563(self):
        
        Test_Case_ID="C2313563"
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
            Step 01 : Launch new chart using the IA API
            http://machine:port/{alias}/ia?tool=Report&master=ibisamp/car&item=IBFS%3A%2FWFC%2FRepository%2FS10670%2FDualAxisBucketizedBarCharts.
        """
        utillobj.infoassist_api_login('Chart', 'ibisamp/car', 'P116/S10670', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element(default_chart_css, default_chart_expected_number, 65)
         
        """
            Step 02:Select the CAR file.
            Select Active Report as the format.
            From the Format tab, select the Other option..
            Expect to see the Vertical Dual-Axis Clustered Bars option.
        """
        ribbonobj.change_output_format_type('active_report', location='Home')
        parent_css="#pfjTableChart_1 g.chartPanel"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 15)
        
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbobj.select_other_chart_type('bar', 'vertical_dual_axis_clustered_bars', 10, ok_btn_click=True)
              
        """
            Step 03:Select the Vertical Dual-Axis Clustered Bars chart option.
            Click OK.
            Expect to see the following Preview pane, including axis on both sides of the canvas.
        """
        expected_xval_list=['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4']
        expected_yval1_list=['0', '10', '20', '30', '40', '50']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 02.4: Verify XY labels")
        expected_yval2_list=['0', '5', '10', '15', '20', '25', '30', '35', '40', '45']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 02.4: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("TableChart_1", 1, 25, 'Step 02.3: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue1", "Step 02.6: Verify  bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mbar", "bar_green", "Step 02.7: Verify  bar color")
        legend=["Series0","Series1","Series2","Series3","Series4"]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 02.8: Verify Y-Axis legend")
 
        """
            Step 04:Add CAR to the Horizontal axis.
            Add DEALER_COST to Vertical Axis 1.
            Add LENGTH to Vertical axis 2.
 
            Expect to see the following Preview pane.
        """
        metadataobj.datatree_field_click('CAR', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(9) td"
        utillobj.synchronize_with_visble_text(parent_css, "CAR", 10)
        
        metadataobj.datatree_field_click('DEALER_COST', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(7) td"
        utillobj.synchronize_with_visble_text(parent_css, "DEALER_COST", 10)
        
        metadataobj.drag_drop_data_tree_items_to_query_tree_('LENGTH', 1, 'Vertical Axis 2',0)
        parent_css="#queryTreeWindow table tr:nth-child(9) td"
        utillobj.synchronize_with_visble_text(parent_css, "LENGTH", 10)
       
        resobj.verify_xaxis_title("TableChart_1", "CAR", "Step 04.1: Verify -xAxis Title")
        resobj.verify_yaxis_title('TableChart_1', "DEALER_COST", "Step 04.2: Verify -xAxis Title") 
        resobj.verify_yaxis_title('TableChart_1', "LENGTH", "Step 04.3: Verify -xAxis Title",custom_css="text[class='y2axis-title']")       
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 04.4: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 04.5: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("TableChart_1", 1, 20, 'Step 04.6: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue1", "Step 04.7: Verify  bar color")
        legend=['DEALER_COST','LENGTH']
        resobj.verify_riser_legends("TableChart_1", legend, "Step 04.8: Verify Y-Axis legend")
 
        """
            Step 05:Click the Run button.
            Hover over the first blue bar for Alfa Romeo..
 
            Expect to see the following Tooltip information.Dealer_Cost uses the left-side axis scale.
        """
         
        ribbonobj.select_top_toolbar_item('toolbar_run')
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0 text[class^='xaxis'][class$='title']", "CAR", 15)
        
        expected_tooltip_list=['CAR:ALFA ROMEO', 'DEALER_COST:16,235', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g0!mbar!", expected_tooltip_list, "Step 05.1: Verify bar value")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR", "Step 05.2: Verify -xAxis Title")
        resobj.verify_yaxis_title('MAINTABLE_wbody0', "DEALER_COST", "Step 05.3: Verify -xAxis Title") 
        resobj.verify_yaxis_title('MAINTABLE_wbody0', "LENGTH", "Step 05.4: Verify -xAxis Title",custom_css="text[class='y2axis-title']")       
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 05.5: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 05.6: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 05.7: Verify the total number of risers displayed on preview')
        
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue1", "Step 05.8: Verify  bar color")
        legend=['DEALER_COST','LENGTH']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 05.9: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, LENGTH by CAR', 'Step 05.10: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.11: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.12: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.13: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
  
        """
            Step 06:Hover over the green blue bar for Triumph.
     
            Expect to see the following Tooltip information.Length uses the right-side axis scale.
        """
        expected_tooltip_list=['CAR:TRIUMPH', 'LENGTH:164', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s1!g9!mbar!", expected_tooltip_list, "Step 06.1: Verify bar value")
        time.sleep(2)
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step_06', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
         
        """
            Step 07:Save the procedure as Vertical_Cluster_Bar and exit IA+.
            Expect to see the saved procedure in the tree.
        """
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