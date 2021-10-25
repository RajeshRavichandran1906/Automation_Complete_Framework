'''
Created on Oct 27, 2017

@author: BM13368
Test_Case_ID : http://172.19.2.180/testrail/index.php?/cases/view/2323680
Testcase_Name : New Bucketized Vertical Dual-axis Absolute Line Chart
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity, core_utility
from common.pages import visualization_metadata, visualization_ribbon, visualization_resultarea, ia_ribbon, ia_resultarea, active_miscelaneous


class C2323691_TestClass(BaseTestCase):


    def test_C2323691(self):
        driver = self.driver #Driver reference object created
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2323691'
        utillobj = utillity.UtillityMethods(driver)
        core_utils = core_utility.CoreUtillityMethods(driver)
        metadataobj = visualization_metadata.Visualization_Metadata(driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(driver)
        ia_resultarea_obj=ia_resultarea.IA_Resultarea(driver)
        miscobj=active_miscelaneous.Active_Miscelaneous(self.driver)
        default_chart_css="#TableChart_1 rect[class^='riser']"
        default_chart_expected_number=25
        
        """
           Step 01 :Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660&tool=chart&master=ibisamp/car
        """
        
        utillobj.infoassist_api_login('chart','ibisamp/car','P292/S10660_chart_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element(default_chart_css, default_chart_expected_number, 65)
        
        """
            Step 02: Format > Chart Type > Other > Line Charts > Vertical Dual-axis Absolute Line Chart.
        """
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbonobj.select_other_chart_type('line', 'vertical_dual_axis_stacked_line', 5, ok_btn_click=True)
        """
            Verification : Expect to see the following HTML5
            Vertical dual-axis stacked line Chart Preview..
        """
        parent_css="#TableChart_1 .legend text"
        utillobj.synchronize_with_number_of_element(parent_css, 5, 35)
        expected_yval_list=['0', '20', '40', '60', '80', '100', '120']
        expected_xval_list=['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 02:01: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mline!", "bar_blue", "Step 02:02: Verify first bar color", attribute_type='stroke')
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mline!", "pale_green", "Step 02:03: Verify second bar color", attribute_type='stroke')
        utillobj.verify_chart_color("TableChart_1", "riser!s2!g0!mline!", "dark_green", "Step 02:04: Verify third bar color", attribute_type='stroke')
        utillobj.verify_chart_color("TableChart_1", "riser!s3!g0!mline!", "pale_yellow", "Step 02:05: Verify four bar color", attribute_type='stroke')
        resultobj.verify_riser_legends('TableChart_1',['Series0','Series1','Series2','Series3','Series4'], 'Step 02.07 : Verify chart legends')
        resultobj.verify_number_of_riser('TableChart_1', 1, 0, 'Step 02.08: Verify Number chart segment')
        expected_data_labels=['0', '10', '20', '30', '40', '50', '60', '70', '80']
        resultobj.verify_data_labels('TableChart_1', expected_data_labels, "Step 02:09 : Verify data labels right side x labels", custom_css="g.chartPanel text[class*='y2axis-labels!']")
        time.sleep(2)
           
        """
            Step 03: Add Car to the Horizontal axis bucket.
            Add Dealer_Cost & Retail_Cost to the Vertical axis 1 bucket.
            Add Length & Width to the Vertical axis 2 bucket. 
        """
        metadataobj.datatree_field_click('CAR', 2, 1)
        time.sleep(4)
        metadataobj.datatree_field_click('DEALER_COST', 2, 1)
        time.sleep(4)
        metadataobj.datatree_field_click('RETAIL_COST', 2, 1)
        time.sleep(4)
        metadataobj.drag_drop_data_tree_items_to_query_tree_("LENGTH", 1,'Vertical Axis 2', 0)
        time.sleep(10)
        
        metadataobj.drag_drop_data_tree_items_to_query_tree_("WIDTH", 1,'Vertical Axis 2', 1)
        time.sleep(8)
          
        """
            Verification : Expect to see the following
            Vertical dual-axis stacked line Chart Preview.
        """
        parent_css="#TableChart_1 text[class^='xaxis'][class$='title']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 45)
        
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K', '120K']
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 03:01: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mline!", "bar_blue", "Step 03:02: Verify first bar color", attribute_type='stroke')
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mline!", "pale_green", "Step 03:03: Verify second bar color", attribute_type='stroke')
        utillobj.verify_chart_color("TableChart_1", "riser!s2!g0!mline!", "dark_green", "Step 03:04: Verify third bar color", attribute_type='stroke')
        utillobj.verify_chart_color("TableChart_1", "riser!s3!g0!mline!", "pale_yellow", "Step 03:05: Verify four bar color", attribute_type='stroke')
        resultobj.verify_riser_legends('TableChart_1',['DEALER_COST', 'RETAIL_COST', 'LENGTH', 'WIDTH'], 'Step 03.06 : Verify chart legends', attribute_type='stroke')
        ia_resultarea_obj.verify_number_of_chart_segment('jschart_HOLD_0', 0, 'Step 03.07: Verify Number of riser', custom_css="path[class^='riser']")
        expected_data_labels=['0', '400', '800', '1,200', '1,600']
        resultobj.verify_data_labels('TableChart_1', expected_data_labels, "Step 03:08 : Verify data labels right side x labels", custom_css="g.chartPanel text[class*='y2axis-labels!']")
        time.sleep(1)
        resultobj.verify_xaxis_title('TableChart_1', 'CAR', "Step 03:09: Verify X-Axis Title")
         
        """
            Step 04: Click the Run button.
            Hover over the bottom point (Dealer_Cost) for Alfa Romeo.
            Hover over the top point(Width) for Alfa Romeo
        """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 45)
        
        utillobj.switch_to_frame(pause=2)
        parent_css="#jschart_HOLD_0 [class='riser!s3!g0!mline!']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """
            Verification : Expect to see the following
            Vertical Dual-axis Absolute Line Chart, including Tool tip information.
            Note that the Legend contains one entry for each of the 4 Measures.
            Dealer_Cost & Retail_Cost uses the left-side axis:
        """
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K', '120K']
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, 'Step 04:01: X and Y axis labels')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mline!", "bar_blue", "Step 04:02: Verify first bar color", attribute_type='stroke')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s1!g0!mline!", "pale_green", "Step 04:03: Verify second bar color", attribute_type='stroke')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s2!g0!mline!", "dark_green", "Step 04:04: Verify third bar color", attribute_type='stroke')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s3!g0!mline!", "pale_yellow", "Step 04:05: Verify four bar color", attribute_type='stroke')
        ia_resultarea_obj.verify_number_of_chart_segment('jschart_HOLD_0', 4, 'Step 04.06: Verify Number of riser', custom_css="path[class^='riser']")
        expected_data_labels=['0', '400', '800', '1,200', '1,600']
        resultobj.verify_data_labels('jschart_HOLD_0', expected_data_labels, "Step 04:07 : Verify data labels right side x labels", custom_css="g.chartPanel text[class*='y2axis-labels!']")
        time.sleep(1)
        riser_legends=['DEALER_COST', 'RETAIL_COST', 'LENGTH', 'WIDTH']
        resultobj.verify_riser_legends('jschart_HOLD_0', riser_legends, 'Step 04:08 : Verify chart legends')
        resultobj.verify_xaxis_title("jschart_HOLD_0", 'CAR', "Step 04:09: Verify X-Axis Title")
        
        move_elem = self.driver.find_element_by_css_selector("#jschart_HOLD_0 text[class^='xaxis'][class$='title']")
        core_utils.python_move_to_element(move_elem)
        expected_tooltip_list=['CAR:ALFA ROMEO', 'DEALER_COST:16,235']
        miscobj.select_or_verify_marker_tooltip('marker!s0!g0!mmarker!', verify_tooltip_list=expected_tooltip_list, msg="step 4.10", parent_css="#jschart_HOLD_0")

        expected_tooltip_list=['CAR:ALFA ROMEO', 'WIDTH:188']
        miscobj.select_or_verify_marker_tooltip('marker!s3!g0!mmarker!', verify_tooltip_list=expected_tooltip_list, msg="step 4.11", parent_css="#jschart_HOLD_0")
         
        """
            Step 05 : Add Seats to the Color By bucket.
            Click the Run button.
            Hover over the bottom point (Dealer_Cost) for Alfa Romeo.
            Hover over the top point(Width) for Alfa Romeo.
            Expect to see the following
            Vertical dual-axis stacked line, now with the chart reflecting colors using the Color By bucket.
            Note that the Legend contains one entry for each of the 4 Measures.
            Also expect to see the Tool tip information for Retail_Cost. & Weight.
            Dealer_cost bar uses the left-side axis:
        """
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        metadataobj.datatree_field_click("SEATS",1,1,'Add To Query','Color')
        time.sleep(4)
        metadataobj.verify_query_pane_field('Color', 'SEATS', 1, "Step 05::00: Verify Quantity,Sold is visible underneath Vertical Axis")
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        parent_css="#jschart_HOLD_0 text[class^='xaxis'][class$='title']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K', '120K']
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, 'Step 05:01: X and Y axis labels')
        exected_multicolor_list=['sandy_brown', 'sorbus1','elf_green','cinnabar3','crusta1','cinnabar3','persian_red','sorbus1','cinnabar3','persian_red']
        ia_resultarea_obj.verify_multicolor("#jschart_HOLD_0", "Stroke", exected_multicolor_list, "Step 05:02: Verify line colors")
        expected_color_scale=['SEATS', '2', '8.8', '15.5', '22.3', '29']
        ia_resultarea_obj.verify_color_scale_esri_maps("jschart_HOLD_0", expected_color_scale, "Step05:03 : Verify the color scale values")
        ia_resultarea_obj.verify_number_of_chart_segment('jschart_HOLD_0', 4, 'Step 05:04: Verify Number of riser', custom_css="path[class^='riser']")
        expected_data_labels=['0', '400', '800', '1,200', '1,600']
        resultobj.verify_data_labels('jschart_HOLD_0', expected_data_labels, "Step 05:05 : Verify data labels right side x labels", custom_css="g.chartPanel text[class*='y2axis-labels!']")
        time.sleep(1)
        resultobj.verify_xaxis_title("jschart_HOLD_0", 'CAR', "Step 05:06: Verify X-Axis Title")

        expected_tooltip_list=['CAR:ALFA ROMEO', 'DEALER_COST:16,235', 'SEATS:8']
        miscobj.select_or_verify_marker_tooltip('marker!s0!g0!mmarker!', verify_tooltip_list=expected_tooltip_list, msg="step 5.07", parent_css="#jschart_HOLD_0")
        
        move_elem = self.driver.find_element_by_css_selector("#jschart_HOLD_0 text[class^='xaxis'][class$='title']")
        core_utils.python_move_to_element(move_elem)
        expected_tooltip_list=['CAR:ALFA ROMEO', 'WIDTH:188', 'SEATS:8']
        miscobj.select_or_verify_marker_tooltip('marker!s3!g0!mmarker!', verify_tooltip_list=expected_tooltip_list, msg="step 5.08", parent_css="#jschart_HOLD_0")
                
        """
            Step 06: Add Sales to the Size bucket.
            Hover over the bottom point (Dealer_Cost) for Alfa Romeo.
            Hover over the top point(Width) for Alfa Romeo.
        """
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        metadataobj.datatree_field_click("SALES",1,1,'Add To Query','Size')
        time.sleep(4)
        metadataobj.verify_query_pane_field('Size', 'SALES', 1, "Step 06::01: Verify Quantity,Sold is visible underneath Vertical Axis")
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        parent_css="#jschart_HOLD_0 text[class^='xaxis'][class$='title']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K', '120K']
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, 'Step 06:02: X and Y axis labels')
        exected_multicolor_list=['sandy_brown', 'sorbus1','elf_green','cinnabar3','crusta1','cinnabar3','persian_red','sorbus1','cinnabar3','persian_red']
        ia_resultarea_obj.verify_multicolor("#jschart_HOLD_0", "fill", exected_multicolor_list, "Step 06:03: Veirfy line colors")
        expected_color_scale=['SEATS', '2', '8.8', '15.5', '22.3', '29']
        ia_resultarea_obj.verify_color_scale_esri_maps("jschart_HOLD_0", expected_color_scale, "Step 06:04 : Verify the color scale values")
        ia_resultarea_obj.verify_number_of_chart_segment('jschart_HOLD_0', 4, 'Step 06:05: Verify Number of riser', custom_css="path[class^='riser']")
        expected_data_labels=['0', '400', '800', '1,200', '1,600']
        resultobj.verify_data_labels('jschart_HOLD_0', expected_data_labels, "Step 06:06 : Verify data labels right side x labels", custom_css="g.chartPanel text[class*='y2axis-labels!']")
        time.sleep(1)
        resultobj.verify_xaxis_title("jschart_HOLD_0", 'CAR', "Step 06:07: Verify X-Axis Title")
          
        """
            Expect to see the following
            Vertical dual-axis stacked line.
            Sales information has been added to the Tooltip.
            Notice that the width of the lines vary by total of Sales. The lines for Maserati are the thinnest because their Sales totals 0.
            Dealer_cost bar uses the left-side axis:
        """
        move_elem = self.driver.find_element_by_css_selector("#jschart_HOLD_0 text[class^='xaxis'][class$='title']")
        core_utils.python_move_to_element(move_elem)
        expected_tooltip_list=['CAR:ALFA ROMEO', 'DEALER_COST:16,235', 'SALES:30200', 'SEATS:8']
        miscobj.select_or_verify_marker_tooltip('marker!s0!g0!mmarker!', verify_tooltip_list=expected_tooltip_list, msg="step 06.08", parent_css="#jschart_HOLD_0")

        expected_tooltip_list=['CAR:ALFA ROMEO', 'WIDTH:188', 'SALES:30200', 'SEATS:8']
        miscobj.select_or_verify_marker_tooltip('marker!s3!g0!mmarker!', verify_tooltip_list=expected_tooltip_list, msg="step 6.09", parent_css="#jschart_HOLD_0")

        """
            Step 07 : Add MPG to the Tool Tip bucket.
            Click the Run button.
            Hover over the bottom point (Dealer_Cost) for Alfa Romeo.
            Hover over the top point(Width) for Alfa Romeo.
            
        """
        utillobj.switch_to_default_content(pause=1)
        metadataobj.datatree_field_click("MPG",1,0,'Add To Query','Tooltip')
        time.sleep(2)
        metadataobj.verify_query_pane_field('Tooltip', 'MPG', 1, "Step 07::01: Verify Quantity,Sold is visible underneath Vertical Axis")
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        parent_css="#jschart_HOLD_0 text[class^='xaxis'][class$='title']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K', '120K']
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, 'Step 07:02: X and Y axis labels')
        expected_color_scale=['SEATS', '2', '8.8', '15.5', '22.3', '29']
        ia_resultarea_obj.verify_color_scale_esri_maps("jschart_HOLD_0", expected_color_scale, "Step 07:03 : Verify the color scale values")
        ia_resultarea_obj.verify_number_of_chart_segment('jschart_HOLD_0', 4, 'Step 07:04: Verify Number of riser', custom_css="path[class^='riser']")
        expected_data_labels=['0', '400', '800', '1,200', '1,600']
        resultobj.verify_data_labels('jschart_HOLD_0', expected_data_labels, "Step 07:05 : Verify data labels right side x labels", custom_css="g.chartPanel text[class*='y2axis-labels!']")
        time.sleep(1)
        resultobj.verify_xaxis_title("jschart_HOLD_0", 'CAR', "Step 07:06: Verify X-Axis Title")
        exected_multicolor_list=['sandy_brown', 'sorbus1','elf_green','cinnabar3','crusta1','cinnabar3','persian_red','sorbus1','cinnabar3','persian_red']
        ia_resultarea_obj.verify_multicolor("#jschart_HOLD_0", "fill", exected_multicolor_list, "Step 07:07: Veirfy line colors")
         
        """
            Verification :
            Expect to see the following
            Vertical dual-axis stacked line chart, now with additional Tool tip information for MPG.
            Dealer_cost bar uses the left-side axis:
        """
        move_elem = self.driver.find_element_by_css_selector("#jschart_HOLD_0 text[class^='xaxis'][class$='title']")
        core_utils.python_move_to_element(move_elem)
        expected_tooltip_list=['CAR:ALFA ROMEO', 'DEALER_COST:16,235', 'SALES:30200', 'SEATS:8', 'MPG:63']
        miscobj.select_or_verify_marker_tooltip('marker!s0!g0!mmarker!', verify_tooltip_list=expected_tooltip_list, msg="step 7.08", parent_css="#jschart_HOLD_0")

        expected_tooltip_list=['CAR:ALFA ROMEO', 'WIDTH:188', 'SALES:30200', 'SEATS:8', 'MPG:63']

        miscobj.select_or_verify_marker_tooltip('marker!s3!g0!mmarker!', verify_tooltip_list=expected_tooltip_list, msg="step 7.09", parent_css="#jschart_HOLD_0")
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step_07', image_type='actual',x=1, y=1, w=-1, h=-1)
  
        """
            Step 08: Click Save in the toolbar > Save as "C2323691" > Click Save
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """
           Step 09 :Logout using API
           http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(4)
        
        """
            Step 10 :Restore the fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660%2FC2323691.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S10660_chart_1', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_number_of_element("#TableChart_1", 1, 65)
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        parent_css="#jschart_HOLD_0 text[class^='xaxis'][class$='title']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K', '120K']
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, 'Step 09:01: X and Y axis labels')
        expected_color_scale=['SEATS', '2', '8.8', '15.5', '22.3', '29']
        ia_resultarea_obj.verify_color_scale_esri_maps("jschart_HOLD_0", expected_color_scale, "Step 09:02 : Verify the color scale values")
        ia_resultarea_obj.verify_number_of_chart_segment('jschart_HOLD_0', 4, 'Step 09:03: Verify Number of riser', custom_css="path[class^='riser']")
        expected_data_labels=['0', '400', '800', '1,200', '1,600']
        resultobj.verify_data_labels('jschart_HOLD_0', expected_data_labels, "Step 09:04 : Verify data labels right side x labels", custom_css="g.chartPanel text[class*='y2axis-labels!']")
        time.sleep(1)
        resultobj.verify_xaxis_title("jschart_HOLD_0", 'CAR', "Step 09:05: Verify X-Axis Title")
        exected_multicolor_list=['sandy_brown', 'sorbus1','elf_green','cinnabar3','crusta1','cinnabar3','persian_red','sorbus1','cinnabar3','persian_red']
        ia_resultarea_obj.verify_multicolor("#jschart_HOLD_0", "fill", exected_multicolor_list, "Step 09:06: Veirfy line colors")
        
        """
            Step 11 : Logout using API
            http://machine:port/alias/service/wf_security_logout.jsp
        """


if __name__ == "__main__":
    unittest.main()