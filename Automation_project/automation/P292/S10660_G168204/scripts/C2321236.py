'''
Created on Nov 7, 2017

@author: BM13368
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
from common.pages import visualization_metadata, visualization_ribbon, visualization_resultarea, ia_resultarea, ia_ribbon

class C2321236_TestClass(BaseTestCase):


    def test_C2321236(self):
        driver = self.driver #Driver reference object created
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2321236'
        utillobj = utillity.UtillityMethods(driver)
        metadataobj = visualization_metadata.Visualization_Metadata(driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(driver)
        ia_resultarea_obj = ia_resultarea.IA_Resultarea(driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(driver)
        
        """
            Step 01 : Invoke IA Chart tool with wf_retail
            http://domain:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660&tool=chart&master=wf_retail
        """
        utillobj.infoassist_api_login('chart','ibisamp/car','P292/S10660_chart_1', 'mrid', 'mrpass')
        elem1="#TableChart_1"
        resultobj.wait_for_property(elem1, 1)
         
        """
            Step 02 : Format > Chart Type > Other > HTML5 > stream_graph
        """
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbonobj.select_other_chart_type('html5', 'stream_graph', 3, ok_btn_click=True)
         
        """
            Verification : Expect to see the following Streamgraph Preview.
        """
        elem1="#TableChart_1 [class='riser!s4!g0!marea!']"
        resultobj.wait_for_property(elem1, 1)
        expected_xval_list=['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4']
        expected_yval_list=[]
        resultobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 02: Verify XY Label')
        expected_label_list=['Series0', 'Series1', 'Series2', 'Series3', 'Series4']
        resultobj.verify_riser_legends('TableChart_1', expected_label_list, 'Step 02:01 Verify Legends ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s4!g0!marea!', 'brick_red', 'Step 02:03 Verify Color')
        ia_resultarea_obj.verify_number_of_chart_segment('TableChart_1', 5, 'Step 02:04: Verify Number of riser', custom_css="path[class^='riser']")
        time.sleep(0.5)
        """
            Step 03: Add Car to the Horizontal axis bucket.
            Add Dealer_Cost to the Vertical axis bucket.
        """
        metadataobj.datatree_field_click('CAR', 2, 1)
        time.sleep(1)
        metadataobj.datatree_field_click('DEALER_COST', 2, 1)
        time.sleep(1)
        """
            Verification : Expect to see the following Streamgraph Preview.
        """
        resultobj.verify_xaxis_title("TableChart_1", 'CAR', "Step 03.01: Verify X-Axis Title")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=[]
        resultobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 03:02: Verify XY Label')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!marea!', 'bar_blue', 'Step 03:03: Verify Color')
        ia_resultarea_obj.verify_number_of_chart_segment('TableChart_1', 1, 'Step 03:04: Verify Number of riser', custom_css="path[class^='riser']")
        
        """
            Step 04: Click the Run button.
            Hover over the area for Alfa Romeo.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        css="#jschart_HOLD_0 .chartPanel"
        resultobj.wait_for_property(css, 1)
        parent_obj = self.driver.find_element_by_css_selector("#jschart_HOLD_0 [class='marker!s0!g0!mmarker!']")
        utillobj.click_on_screen(parent_obj,'middle', javascript_marker_enable=True, mouse_duration=2.5)
        time.sleep(2)
        expected_tooltip_list=['CAR:ALFA ROMEO', 'DEALER_COST:16,235']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", 'marker!s0!g0!mmarker!', expected_tooltip_list, 'Step 04.1: verify the default tooltip values')  
        """
            Step 05: Add Retail_Cost to the Vertical axis bucket.
            Click the Run button.
            Hover over the upper area for Alfa Romeo.
        """
        time.sleep(0.5)
        utillobj.switch_to_default_content(pause=1)
        metadataobj.datatree_field_click('RETAIL_COST', 2, 1)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        utillobj.switch_to_frame(pause=2)
        css="#jschart_HOLD_0 [class='marker!s1!g0!mmarker!']"
        resultobj.wait_for_property(css, 1)
        parent_obj = self.driver.find_element_by_css_selector("#jschart_HOLD_0 [class='marker!s1!g0!mmarker!']")
        utillobj.click_on_screen(parent_obj,'middle', javascript_marker_enable=True, mouse_duration=2.5)
        time.sleep(2)
        expected_tooltip_list=['CAR:ALFA ROMEO', 'RETAIL_COST:19,565']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", 'marker!s1!g0!mmarker!', expected_tooltip_list, 'Step 05.1: verify the default tooltip values')
         
        """
            Verify the chart
        """
        resultobj.verify_xaxis_title("jschart_HOLD_0", 'CAR', "Step 5.1: Verify X-Axis Title")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=[]
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 5.2: Verify XY Label')
        expected_label_list=['DEALER_COST', 'RETAIL_COST']
        resultobj.verify_riser_legends('jschart_HOLD_0', expected_label_list, 'Step : 5.3 Verify Legends ')
        utillobj.verify_chart_color('jschart_HOLD_0', 'riser!s1!g0!marea!', 'pale_green', 'Step 5.4: Verify Color')
        utillobj.verify_chart_color('jschart_HOLD_0', 'riser!s0!g0!marea!', 'bar_blue1', 'Step 5.5: Verify Color')
        ia_resultarea_obj.verify_number_of_chart_segment('jschart_HOLD_0', 2, 'Step 5.6: Verify Number of riser', custom_css="path[class^='riser']")
         
        """
            Step 06: Add Country to the Color By bucket.
            Click the Run button.
        """
        utillobj.switch_to_default_content(pause=1)
        metadataobj.datatree_field_click("COUNTRY",1,0,'Add To Query','Color')
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        css="#jschart_HOLD_0 [class='marker!s1!g0!mmarker!']"
        resultobj.wait_for_property(css, 1)
         
        """
            Verification : Expect to see the following Stream-graph, now with the chart reflecting colors using the Color By bucket.
            Also expect to see the Tool tip information for Retail_Cost.
        """
        resultobj.verify_xaxis_title("jschart_HOLD_0", 'CAR', "Step 06:00: Verify X-Axis Title")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=[]
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 06:01: Verify XY Label')
        expected_label_list=['DEALER_COST : ENGLAND', 'RETAIL_COST : ENGLAND', 'DEALER_COST : FRANCE', 'RETAIL_COST : FRANCE', 'DEALER_COST : ITALY', 'RETAIL_COST : ITALY', 'DEALER_COST : JAPAN', 'RETAIL_COST : JAPAN', 'DEALER_COST : W GERMANY', 'RETAIL_COST : W GERMANY']
        resultobj.verify_riser_legends('jschart_HOLD_0', expected_label_list, 'Step 06:02: Verify Legends ')
        utillobj.verify_chart_color('jschart_HOLD_0', 'riser!s9!g0!marea!', 'pale_yellow1', 'Step 06:03: Verify Color')
        ia_resultarea_obj.verify_number_of_chart_segment('jschart_HOLD_0', 10, 'Step 06:04: Verify Number of riser', custom_css="path[class^='riser']")
        time.sleep(5)
        css="#jschart_HOLD_0 .chartPanel"
        resultobj.wait_for_property(css, 1)
        parent_obj = self.driver.find_element_by_css_selector("#jschart_HOLD_0 [class='marker!s1!g0!mmarker!']")
        utillobj.click_on_screen(parent_obj,'middle', javascript_marker_enable=True, mouse_duration=2.5)
        time.sleep(2)
        expected_tooltip_list=['CAR:ALFA ROMEO', 'DEALER_COST:0', 'COUNTRY:ENGLAND']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", 'marker!s1!g0!mmarker!', expected_tooltip_list, 'Step 06:05: verify the default tooltip values')
        time.sleep(0.5)
         
        """
            Step 07: Add Sales to the Tool Tip bucket.
            Click the Run button.
            Hover over the lower area for Jaguar.
        """
        utillobj.switch_to_default_content(pause=1)
        metadataobj.datatree_field_click("SALES",1,0,'Add To Query','Tooltip')
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        css="#jschart_HOLD_0 [class='marker!s0!g4!mmarker!']"
        resultobj.wait_for_property(css, 1)
        parent_obj = self.driver.find_element_by_css_selector("#jschart_HOLD_0 [class='marker!s0!g4!mmarker!']")
        utillobj.click_on_screen(parent_obj,'middle', javascript_marker_enable=True, mouse_duration=2.5)
        time.sleep(2)
        expected_tooltip_list=['CAR:ALFA ROMEO', 'DEALER_COST:16,235', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", 'marker!s0!g4!mmarker', expected_tooltip_list, 'Step 07:01: verify the default tooltip values')
        """
            Expect to see the following strem graph
        """
        resultobj.verify_xaxis_title("jschart_HOLD_0", 'CAR', "Step 06:00: Verify X-Axis Title")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=[]
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 07:02: Verify XY Label')
        expected_label_list=['DEALER_COST : ENGLAND', 'RETAIL_COST : ENGLAND', 'DEALER_COST : FRANCE', 'RETAIL_COST : FRANCE', 'DEALER_COST : ITALY', 'RETAIL_COST : ITALY', 'DEALER_COST : JAPAN', 'RETAIL_COST : JAPAN', 'DEALER_COST : W GERMANY', 'RETAIL_COST : W GERMANY']
        resultobj.verify_riser_legends('jschart_HOLD_0', expected_label_list, 'Step 07:03: Verify Legends ')
        utillobj.verify_chart_color('jschart_HOLD_0', 'riser!s9!g0!marea!', 'pale_yellow1', 'Step 07:04: Verify Color')
        ia_resultarea_obj.verify_number_of_chart_segment('jschart_HOLD_0', 10, 'Step 07:05: Verify Number of riser', custom_css="path[class^='riser']")
         
        """
            Step 08: Save with name C2321236 and close.
        """
        utillobj.switch_to_default_content(pause=1)
        time.sleep(1)
        obj1=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(obj1,Test_Case_ID + '_Actual_step06', image_type='actual',x=1, y=1, w=-1, h=-1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        utillobj.infoassist_api_logout()
        time.sleep(2)
        """
            Step 09: Restore using IA API:
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660%C2321236.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S10660_chart_1', mrid='mrid', mrpass='mrpass')
        elem1="#TableChart_1 [class='riser!s9!g0!marea!']"
        resultobj.wait_for_property(elem1, 1)
        """
            Expect to see the regenerated Streamgraph.
        """
        resultobj.verify_xaxis_title("TableChart_1", 'CAR', "Step 09:00: Verify X-Axis Title")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=[]
        resultobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 09:01: Verify XY Label')
        expected_label_list=['DEALER_COST : ENGLAND', 'RETAIL_COST : ENGLAND', 'DEALER_COST : FRANCE', 'RETAIL_COST : FRANCE', 'DEALER_COST : ITALY', 'RETAIL_COST : ITALY', 'DEALER_COST : JAPAN', 'RETAIL_COST : JAPAN', 'DEALER_COST : W GERMANY', 'RETAIL_COST : W GERMANY']
        resultobj.verify_riser_legends('TableChart_1', expected_label_list, 'Step 09:02: Verify Legends ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s9!g0!marea!', 'pale_yellow1', 'Step 09:03: Verify Color')
        ia_resultarea_obj.verify_number_of_chart_segment('TableChart_1', 10, 'Step 09:04: Verify Number of riser', custom_css="path[class^='riser']")
         
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
        
        
        
        
        
        