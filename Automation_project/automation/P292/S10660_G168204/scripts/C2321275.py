'''
Created on Oct 17, 2017

@author: BM13368
Test_Case_ID : http://172.19.2.180/testrail/index.php?/cases/view/2321275
Testcase_Name :New Bucketized Vertical Dual-axis Stacked Bar Chart
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
from common.pages import visualization_metadata, visualization_ribbon, visualization_resultarea, ia_ribbon

class C2321275_TestClass(BaseTestCase):


    def test_C2321275(self):
        
        driver = self.driver #Driver reference object created
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2321275'
        utillobj = utillity.UtillityMethods(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        default_chart_css="#TableChart_1 rect[class^='riser']"
        default_chart_expected_number=25
        
        """
            Step 01 : Invoke IA Chart tool with wf_retail
            http://domain:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660&tool=chart&master=wf_retail
        """
        
        utillobj.infoassist_api_login('chart','ibisamp/car','P292/S10660_chart_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element(default_chart_css, default_chart_expected_number, 65)
       
        """
            Step 02: Format > Chart Type > Other > Bar Charts > Vertical Dual-axis Stacked Bar Chart.
        """
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbonobj.select_other_chart_type('bar', 'vertical_dual_axis_stacked_bars', 11, ok_btn_click=True)
        
        utillobj.synchronize_with_number_of_element(default_chart_css, 25, 45)
        
        """
            Verification : Expect to see the following
            Vertical Vertical Dual-axis Stacked Bar Chart Preview.
        """
        
        expected_yval_list=['0', '20', '40', '60', '80', '100', '120']
        expected_xval_list=['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 02:01: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue", "Step 02:02: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mbar!", "pale_green", "Step 02:03: Verify second bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s2!g0!mbar!", "dark_green", "Step 02:04: Verify third bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s3!g0!mbar!", "pale_yellow", "Step 02:05: Verify four bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s4!g0!mbar!", "brick_red", "Step 02:06: Verify five bar color")
        resultobj.verify_riser_legends('TableChart_1',['Series0','Series1','Series2','Series3','Series4'], 'Step 02.07 : Verify chart legends')
        resultobj.verify_number_of_riser('TableChart_1', 1, 25, 'Step 02.08: Verify Number chart segment')
        expected_data_labels=['0', '10', '20', '30', '40', '50', '60', '70', '80']
        resultobj.verify_data_labels('TableChart_1', expected_data_labels, "Step 02:09 : Verify data labels right side x labels", custom_css="g.chartPanel text[class*='y2axis-labels!']")
        time.sleep(2)
        
          
        """
            Step 03: Add Car to the Horizontal axis bucket.
            Add Dealer_Cost & Retail_Cost to the Vertical axis 1 bucket.
            Add Length & Width to the Vertical axis 2 bucket. 
        """
        number_of_riser_css="#TableChart_1  svg g.risers >g>rect[class^='riser']"
        yaxis_title_css="#TableChart_1 text[class='yaxis-title']"
        
        metadataobj.datatree_field_click('CAR', 2, 1)
        utillobj.synchronize_with_number_of_element(number_of_riser_css, 10, 20)
        
        metadataobj.datatree_field_click('DEALER_COST', 2, 1)
        utillobj.synchronize_with_number_of_element(yaxis_title_css, "DEALER_COST", 15)
        
        metadataobj.datatree_field_click('RETAIL_COST', 2, 1)
        utillobj.synchronize_with_number_of_element(number_of_riser_css, 20, 20)
       
        metadataobj.drag_drop_data_tree_items_to_query_tree("LENGTH", 0,'Vertical Axis 2', 0)
        utillobj.synchronize_with_number_of_element(number_of_riser_css, 30, 20)
        
        metadataobj.drag_drop_data_tree_items_to_query_tree("WIDTH", 1,'Vertical Axis 2', 1)
        utillobj.synchronize_with_number_of_element(number_of_riser_css, 40, 40)
         
        """
            Verification : Expect to see the following
            Vertical Dual-axis Clustered Bar Chart Preview.
        """
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K', '120K']
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 03:01: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue", "Step 03:02: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mbar!", "pale_green", "Step 03:03: Verify second bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s2!g0!mbar!", "dark_green", "Step 03:04: Verify third bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s3!g0!mbar!", "pale_yellow", "Step 03:05: Verify four bar color")
        resultobj.verify_riser_legends('TableChart_1',['DEALER_COST', 'RETAIL_COST', 'LENGTH', 'WIDTH'], 'Step 03.06 : Verify chart legends')
        resultobj.verify_number_of_riser('TableChart_1', 1, 40, 'Step 03.07: Verify Number chart segment')
        expected_data_labels=['0', '400', '800', '1,200', '1,600']
        resultobj.verify_data_labels('TableChart_1', expected_data_labels, "Step 03:08 : Verify data labels right side x labels", custom_css="g.chartPanel text[class*='y2axis-labels!']")
        time.sleep(1)
        resultobj.verify_xaxis_title('TableChart_1', 'CAR', "Step 03:09: Verify X-Axis Title")
        
        """
            Step 04: Click the Run button.
            Hover over the left bar(Dealer_Cost) for Alfa Romeo.
            Hover over the right bar(Width) for Alfa Romeo.
            Verification : Expect to see the following HTML5
            Vertical Dual-axis Clustered Bar Chart, including Tool tip information.
            Note that the Legend contains one entry for each of the 4 Measures.
            Dealer_Cost & Retail_Cost uses the left-side axis:
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        frame_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(frame_css, 1, 35)
        
        utillobj.switch_to_frame(pause=2)
        parent_css="#jschart_HOLD_0 [class='riser!s0!g0!mbar!']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 40)
        
        """
            Verification : Verify runtime chart
        """
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K', '120K']
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, 'Step 04:01: X and Y axis labels')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue", "Step 04:02: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s1!g0!mbar!", "pale_green", "Step 04:03: Verify second bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s2!g0!mbar!", "dark_green", "Step 04:04: Verify third bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s3!g0!mbar!", "pale_yellow", "Step 04:05: Verify four bar color")
        resultobj.verify_riser_legends('jschart_HOLD_0',['DEALER_COST', 'RETAIL_COST', 'LENGTH', 'WIDTH'], 'Step 04.06 : Verify chart legends')
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 40, 'Step 04.07: Verify Number chart segment')
        expected_data_labels=['0', '400', '800', '1,200', '1,600']
        resultobj.verify_data_labels('jschart_HOLD_0', expected_data_labels, "Step 04:08 : Verify data labels right side x labels", custom_css="g.chartPanel text[class*='y2axis-labels!']")
        time.sleep(1)
        resultobj.verify_xaxis_title("jschart_HOLD_0", 'CAR', "Step 04:09: Verify X-Axis Title")
        expected_tooltip_list=['CAR:ALFA ROMEO', 'RETAIL_COST:19,565']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s1!g0!mbar!", expected_tooltip_list, "Step 04:10 Verify left top bar width for alfa romeo")
        expected_tooltip_list=['CAR:ALFA ROMEO', 'WIDTH:188']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s3!g0!mbar!", expected_tooltip_list, "Step 04:11 Verify right top bar width for alfa romeo")
         
        """
            Step 05 : Add Country to the Color By bucket.
            Click the Run button.
            Hover over the left bar(Dealer_Cost) for Alfa Romeo.
            Hover over the right bar(Width) for Alfa Romeo.
            Verification:
            Expect to see the following
            Vertical Dual-axis Stacked Bar Chart, now with the chart reflecting colors using the Color By bucket.
            Note that the Legend contains one entry for each of the 4 Measures.
            Note that the bars have been significantly reduced in width.
            Also expect to see the Tool tip information for Retail_Cost. & Weight.
            Dealer_cost bar uses the left-side axis:
        """
        utillobj.switch_to_default_content(pause=1)
        
        metadataobj.datatree_field_click("COUNTRY",1,0,'Add To Query','Color')
        parent_css="#queryTreeWindow table tr:nth-child(16) td"
        utillobj.synchronize_with_visble_text(parent_css, "COUNTRY", 20)
        
        metadataobj.verify_query_pane_field('Color BY', 'COUNTRY', 1, "Step 08::01: Verify Quantity,Sold is visible underneath Vertical Axis")
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        frame_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(frame_css, 1, 35)
        
        utillobj.switch_to_frame(pause=2)
        parent_css="#jschart_HOLD_0 text[class^='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(parent_css, "CAR", 30)
        
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K', '120K']
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, 'Step 05:01: X and Y axis labels')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s8!g0!mbar!", "dark_green1", "Step 05:02: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s9!g0!mbar!", "pale_yellow4", "Step 05:03: Verify second bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s10!g0!mbar!", "orange1", "Step 05:04: Verify third bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s11!g0!mbar!", "pale_brown", "Step 05:05: Verify four bar color")
        riser_legends=['DEALER_COST : ENGLAND', 'RETAIL_COST : ENGLAND', 'LENGTH : ENGLAND', 'WIDTH : ENGLAND', 'DEALER_COST : FRANCE', 'RETAIL_COST : FRANCE', 'LENGTH : FRANCE', 'WIDTH : FRANCE', 'DEALER_COST : ITALY', 'RETAIL_COST : ITALY', 'LENGTH : ITALY', 'WIDTH : ITALY', 'DEALER_COST : JAPAN', 'RETAIL_COST : JAPAN', 'LENGTH : JAPAN', 'WIDTH : JAPAN', 'DEALER_COST : W GERMANY', 'RETAIL_COST : W GERMANY', 'LENGTH : W GERMANY', 'WIDTH : W GERMANY']
        resultobj.verify_riser_legends('jschart_HOLD_0', riser_legends, 'Step 05:06 : Verify chart legends')
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 40, 'Step 05:07: Verify Number chart segment')
        expected_data_labels=['0', '400', '800', '1,200', '1,600']
        resultobj.verify_data_labels('jschart_HOLD_0', expected_data_labels, "Step 05:08 : Verify data labels right side x labels", custom_css="g.chartPanel text[class*='y2axis-labels!']")
        time.sleep(1)
        resultobj.verify_xaxis_title("jschart_HOLD_0", 'CAR', "Step 05:09: Verify X-Axis Title")
        expected_tooltip_list=['CAR:ALFA ROMEO', 'RETAIL_COST:19,565', 'COUNTRY:ITALY']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s9!g0!mbar!", expected_tooltip_list, "Step 05:10 Verify top left bar width for alfa romeo")
        expected_tooltip_list=['CAR:ALFA ROMEO', 'WIDTH:188', 'COUNTRY:ITALY']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s11!g0!mbar!", expected_tooltip_list, "Step 05:11 Verify top rightbar width for alfa romeo")
        
        """
            Verify width of the first riser bar
        """
        bmw_barobj_before=self.driver.find_element_by_css_selector("#jschart_HOLD_0 rect[class*='riser!s16!g2!mbar!']")
        bar_width_before=bmw_barobj_before.get_attribute("width")
        
        """
            Step 06: Add Sales to the Size bucket.
            Hover over the left bar(Dealer_Cost) for Alfa Romeo.
            Hover over the right bar(Width) for Alfa Romeo.
        """
        utillobj.switch_to_default_content(pause=1)
        metadataobj.datatree_field_click("SALES",1,1,'Add To Query','Size')
        time.sleep(4)
        metadataobj.verify_query_pane_field('Size', 'SALES', 1, "Step 08::01: Verify Quantity,Sold is visible underneath Vertical Axis")
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        frame_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(frame_css, 1, 35)
        
        utillobj.switch_to_frame(pause=2)
        parent_css="#jschart_HOLD_0 text[class^='xaxis'][class$='title']"
        utillobj.synchronize_with_visble_text(parent_css, 'CAR', 35)
       
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K', '120K']
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, 'Step 06:01: X and Y axis labels')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s8!g0!mbar!", "dark_green1", "Step 06:02: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s9!g0!mbar!", "pale_yellow4", "Step 06:03: Verify second bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s10!g0!mbar!", "orange1", "Step 06:04: Verify third bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s11!g0!mbar!", "pale_brown", "Step 06:05: Verify four bar color")
        legend_items=['DEALER_COST : ENGLAND', 'RETAIL_COST : ENGLAND', 'LENGTH : ENGLAND', 'WIDTH : ENGLAND', 'DEALER_COST : FRANCE', 'RETAIL_COST : FRANCE', 'LENGTH : FRANCE', 'WIDTH : FRANCE', 'DEALER_COST : ITALY', 'RETAIL_COST : ITALY', 'LENGTH : ITALY', 'WIDTH : ITALY', 'DEALER_COST : JAPAN', 'RETAIL_COST : JAPAN', 'LENGTH : JAPAN', 'WIDTH : JAPAN', 'DEALER_COST : W GERMANY', 'RETAIL_COST : W GERMANY', 'LENGTH : W GERMANY', 'WIDTH : W GERMANY']
        resultobj.verify_riser_legends('jschart_HOLD_0', legend_items, 'Step 06:06 : Verify chart legends')
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 40, 'Step 06:07: Verify Number chart segment')
        expected_data_labels=['0', '400', '800', '1,200', '1,600']
        resultobj.verify_data_labels('jschart_HOLD_0', expected_data_labels, "Step 06:08 : Verify data labels right side y labels", custom_css="g.chartPanel text[class*='y2axis-labels!']")
        time.sleep(1)
        resultobj.verify_xaxis_title("jschart_HOLD_0", 'CAR', "Step 06:09: Verify X-Axis Title")
        
        """
            Expect to see the following
            Vertical Dual-axis Clustered Bar Chart.
            Sales information has been added to the Tooltip.
            Dealer_cost bar uses the left-side axis:
        """
        expected_tooltip_list=['CAR:ALFA ROMEO', 'DEALER_COST:16,235', 'SALES:30200', 'COUNTRY:ITALY']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s8!g0!mbar!", expected_tooltip_list, "Step 06:10 Verify leftbar width for alfa romeo")
        time.sleep(1)
        expected_tooltip_list=['CAR:ALFA ROMEO', 'WIDTH:188', 'SALES:30200', 'COUNTRY:ITALY']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s11!g0!mbar!", expected_tooltip_list, "Step 06:11 Verify rightbar width for alfa romeo")
        """
        
            Verify width of the BMW riser bar
        """
        bmw_barobj_before=self.driver.find_element_by_css_selector("#jschart_HOLD_0 rect[class*='riser!s16!g2!mbar!']")
        bar_width_after=bmw_barobj_before.get_attribute("width")
        verify_bar_width=float(bar_width_after)-float(bar_width_before)
        if verify_bar_width >= 5:
            utillobj.asequal(True, True, 'Step 06:13 : Bar width is expanded to 14 and above')
        else:
            utillobj.asequal(False, True, 'Step 06:14 : Bar width is not expanded to 14 and above')
        """
            Step 07 : Add MPG to the Tool Tip bucket.
            Click the Run button.
            Hover over the left bar(Dealer_Cost) for Alfa Romeo.
            Hover over the right bar(Width) for Alfa Romeo.
        """
        utillobj.switch_to_default_content(pause=1)
        metadataobj.datatree_field_click("MPG",1,1,'Add To Query','Tooltip')
        time.sleep(2)
        metadataobj.verify_query_pane_field('Tooltip', 'MPG', 1, "Step 08::01: Verify Quantity,Sold is visible underneath Vertical Axis")
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        frame_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(frame_css, 1, 25)
        
        utillobj.switch_to_frame(pause=2)
        parent_css="#jschart_HOLD_0 text[class^='xaxis'][class$='title']"
        utillobj.synchronize_with_visble_text(parent_css, "CAR", 30)
        
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K', '120K']
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, 'Step 07:01: X and Y axis labels')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s8!g0!mbar!", "dark_green1", "Step 07:02: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s9!g0!mbar!", "pale_yellow4", "Step 07:03: Verify second bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s10!g0!mbar!", "orange1", "Step 07:04: Verify third bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s11!g0!mbar!", "pale_brown", "Step 07:05: Verify four bar color")
        legends_item=['DEALER_COST : ENGLAND', 'RETAIL_COST : ENGLAND', 'LENGTH : ENGLAND', 'WIDTH : ENGLAND', 'DEALER_COST : FRANCE', 'RETAIL_COST : FRANCE', 'LENGTH : FRANCE', 'WIDTH : FRANCE', 'DEALER_COST : ITALY', 'RETAIL_COST : ITALY', 'LENGTH : ITALY', 'WIDTH : ITALY', 'DEALER_COST : JAPAN', 'RETAIL_COST : JAPAN', 'LENGTH : JAPAN', 'WIDTH : JAPAN', 'DEALER_COST : W GERMANY', 'RETAIL_COST : W GERMANY', 'LENGTH : W GERMANY', 'WIDTH : W GERMANY']
        resultobj.verify_riser_legends('jschart_HOLD_0', legends_item, 'Step 07:06 : Verify chart legends')
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 40, 'Step 07:07: Verify Number chart segment')
        expected_data_labels=['0', '400', '800', '1,200', '1,600']
        resultobj.verify_data_labels('jschart_HOLD_0', expected_data_labels, "Step 07:08 : Verify data labels right side x labels", custom_css="g.chartPanel text[class*='y2axis-labels!']")
        time.sleep(1)
        resultobj.verify_xaxis_title("jschart_HOLD_0", 'CAR', "Step 07:09: Verify X-Axis Title")
        """
            Verification :Expect to see the following
            Vertical Dual-axis Clustered Bar Chart, now with additional Tool tip information for MPG.
            Dealer_cost bar uses the left-side axis:
        """
        expected_tooltip_list=['CAR:ALFA ROMEO', 'DEALER_COST:16,235', 'SALES:30200', 'COUNTRY:ITALY', 'MPG:63']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s8!g0!mbar!", expected_tooltip_list, "Step 07:10 Verify leftbar width for alfa romeo")
        expected_tooltip_list=['CAR:ALFA ROMEO', 'WIDTH:188', 'SALES:30200', 'COUNTRY:ITALY', 'MPG:63']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s11!g0!mbar!", expected_tooltip_list, "Step 07:11 Verify rightbar width for alfa romeo")
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        obj1=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(obj1,Test_Case_ID + '_Actual_step07', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
            Step 08: Save with name C2321275 and close.
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """
           Step 09 :  Restore using IA API:
           http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660%C2321241.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S10660_chart_1', mrid='mrid', mrpass='mrpass')
        xaxis_title_css="#TableChart_1 text[class^='xaxis'][class$='title']"
        utillobj.synchronize_with_visble_text(xaxis_title_css, "CAR", 60)
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        frame_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(frame_css, 1, 25)
        
        utillobj.switch_to_frame(pause=2)
        parent_css="#jschart_HOLD_0 [class='riser!s0!g0!mbar!']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 40)
        
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K', '120K']
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, 'Step 09:01: X and Y axis labels')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s8!g0!mbar!", "dark_green1", "Step 09:02: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s9!g0!mbar!", "pale_yellow4", "Step 09:03: Verify second bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s10!g0!mbar!", "orange1", "Step 09:04: Verify third bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s11!g0!mbar!", "pale_brown", "Step 09:05: Verify four bar color")
        legends_item=['DEALER_COST : ENGLAND', 'RETAIL_COST : ENGLAND', 'LENGTH : ENGLAND', 'WIDTH : ENGLAND', 'DEALER_COST : FRANCE', 'RETAIL_COST : FRANCE', 'LENGTH : FRANCE', 'WIDTH : FRANCE', 'DEALER_COST : ITALY', 'RETAIL_COST : ITALY', 'LENGTH : ITALY', 'WIDTH : ITALY', 'DEALER_COST : JAPAN', 'RETAIL_COST : JAPAN', 'LENGTH : JAPAN', 'WIDTH : JAPAN', 'DEALER_COST : W GERMANY', 'RETAIL_COST : W GERMANY', 'LENGTH : W GERMANY', 'WIDTH : W GERMANY']
        resultobj.verify_riser_legends('jschart_HOLD_0', legends_item, 'Step 09:06 : Verify chart legends')
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 40, 'Step 09:07: Verify Number chart segment')
        expected_data_labels=['0', '400', '800', '1,200', '1,600']
        resultobj.verify_data_labels('jschart_HOLD_0', expected_data_labels, "Step 09:08 : Verify data labels right side x labels", custom_css="g.chartPanel text[class*='y2axis-labels!']")
        time.sleep(1)
        resultobj.verify_xaxis_title("jschart_HOLD_0", 'CAR', "Step 09:09: Verify X-Axis Title")

if __name__ == "__main__":
    unittest.main()