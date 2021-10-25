'''
Created on Nov 7, 2017

@author: BM13368
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
from common.pages import visualization_metadata, visualization_ribbon, visualization_resultarea, ia_resultarea, ia_ribbon, active_miscelaneous

class C2321236_TestClass(BaseTestCase):

    def test_C2321236(self):
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2321236'
        utillobj = utillity.UtillityMethods(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ia_resultarea_obj = ia_resultarea.IA_Resultarea(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        miscobj=active_miscelaneous.Active_Miscelaneous(self.driver)
        default_chart_css="#TableChart_1 rect[class^='riser']"
        default_chart_expected_number=25
        
        """
            Step 01 : Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660&tool=chart&master=ibisamp/car
        """
        utillobj.infoassist_api_login('chart','ibisamp/car','P292/S10660_chart_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element(default_chart_css, default_chart_expected_number, 65)
         
        """
            Step 02 : Format > Chart Type > Other > HTML5 > stream_graph
        """
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbonobj.select_other_chart_type('html5', 'stream_graph', 3, ok_btn_click=True)
         
        """
            Verification : Expect to see the following Streamgraph Preview.
        """
        expected_xval_list=['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4']
        expected_yval_list=[]
        elem1="#TableChart_1 [class='riser!s4!g0!marea!']"
        resultobj.wait_for_property(elem1, 1)
        resultobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 02: Verify XY Label')
        expected_label_list=['Series0', 'Series1', 'Series2', 'Series3', 'Series4']
        resultobj.verify_riser_legends('TableChart_1', expected_label_list, 'Step 02:01 Verify Legends ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s4!g0!marea!', 'brick_red', 'Step 02:03 Verify Color')
        ia_resultarea_obj.verify_number_of_chart_segment('TableChart_1', 5, 'Step 02:04: Verify Number of riser', custom_css="path[class^='riser']")
        
        """
            Step 03: Add Car to the Horizontal axis bucket.
            Add Dealer_Cost to the Vertical axis bucket.
        """
        metadataobj.datatree_field_click('CAR', 2, 1)
        time.sleep(4)
        
        metadataobj.datatree_field_click('DEALER_COST', 2, 1)
        time.sleep(4)
        
        """
            Verification : Expect to see the following Streamgraph Preview.
        """
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=[]
        resultobj.verify_xaxis_title("TableChart_1", 'CAR', "Step 03.01: Verify X-Axis Title")
        resultobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 03:02: Verify XY Label')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!marea!', 'bar_blue', 'Step 03:03: Verify Color')
        ia_resultarea_obj.verify_number_of_chart_segment('TableChart_1', 1, 'Step 03:04: Verify Number of riser', custom_css="path[class^='riser']")
        
        """
            Step 04: Click the Run button.
            Hover over the area for Alfa Romeo.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 35)
        utillobj.switch_to_frame(pause=2)
        css="#jschart_HOLD_0 .chartPanel"
        utillobj.synchronize_with_number_of_element(css, 1, 35)
        
        parent_obj = self.driver.find_element_by_css_selector("#jschart_HOLD_0")
        utillobj.click_on_screen(parent_obj, 'left')
        expected_tooltip_list=['CAR:ALFA ROMEO', 'DEALER_COST:16,235']
        miscobj.select_or_verify_marker_tooltip('marker!s0!g0!mmarker!', verify_tooltip_list=expected_tooltip_list, msg="step 4.01 : Verify tooltip", parent_css="#jschart_HOLD_0")
        
        """
            Step 05: Add Retail_Cost to the Vertical axis bucket.
            Click the Run button.
            Hover over the upper area for Alfa Romeo.
        """
        utillobj.switch_to_default_content(pause=1)
        
        metadataobj.datatree_field_click('RETAIL_COST', 2, 1)
        time.sleep(4)
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        utillobj.switch_to_frame(pause=2)
        
        parent_obj = self.driver.find_element_by_css_selector("#jschart_HOLD_0")
        utillobj.click_on_screen(parent_obj, 'left')
        expected_tooltip_list=['CAR:ALFA ROMEO', 'RETAIL_COST:19,565']
        miscobj.select_or_verify_marker_tooltip('marker!s1!g0!mmarker!', verify_tooltip_list=expected_tooltip_list, msg="step 5.01 : Verify tooltip", parent_css="#jschart_HOLD_0")
         
        """
            Verify the chart
        """
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=[]
        resultobj.verify_xaxis_title("jschart_HOLD_0", 'CAR', "Step 5.1: Verify X-Axis Title")
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
        time.sleep(3)
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)
        utillobj.switch_to_frame(pause=2)
        
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

        expected_tooltip_list=['CAR:ALFA ROMEO', 'DEALER_COST:16,235', 'COUNTRY:ITALY']
        parent_obj = self.driver.find_element_by_css_selector("#jschart_HOLD_0")
        utillobj.click_on_screen(parent_obj, 'left')
        miscobj.select_or_verify_marker_tooltip('marker!s4!g0!mmarker!', verify_tooltip_list=expected_tooltip_list, msg="step 6.05 : Verify Tool tip information for Retail_Cost", parent_css="#jschart_HOLD_0", y_offset=5)
        time.sleep(2)
         
        """
            Step 07: Add Sales to the Tool Tip bucket. Click the Run button.
            Hover over the lower area for Jaguar.
        """
        utillobj.switch_to_default_content(pause=1)
        metadataobj.datatree_field_click("SALES",1,0,'Add To Query','Tooltip')
        time.sleep(4)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 35)
        utillobj.switch_to_frame(pause=2)
        
        parent_obj = self.driver.find_element_by_css_selector("#jschart_HOLD_0 svg .eventPanel g[transform]")
        utillobj.click_on_screen(parent_obj, 'bottom_middle')
        expected_tooltip_list=['CAR:JAGUAR', 'DEALER_COST:18,621', 'COUNTRY:ENGLAND', 'SALES:12000']
        miscobj.select_or_verify_marker_tooltip('marker!s0!g4!mmarker!', verify_tooltip_list=expected_tooltip_list, msg="Step 7.01", parent_css="#jschart_HOLD_0", y_offset=3)
        
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
            Step 08: Click Save in the toolbar > Save as "C2321236" > Click Save
        """
        utillobj.switch_to_default_content(pause=1)
        time.sleep(3)
        obj1=self.driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(obj1,Test_Case_ID + '_Actual_step06', image_type='actual',x=1, y=1, w=-1, h=-1)
        ribbonobj.select_tool_menu_item('menu_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        """
            Step 09: Logout using API
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(4)
        
        """
        Step 10:Restore the fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660%2FC2321236.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S10660_chart_1', mrid='mrid', mrpass='mrpass')
        elem1="#TableChart_1 [class='riser!s9!g0!marea!']"
        utillobj.synchronize_with_number_of_element(elem1, 1, 65)
        
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
        
        """
        Step 11: Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
    
if __name__ == "__main__" :
    unittest.main()