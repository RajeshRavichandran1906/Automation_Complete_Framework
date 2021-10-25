'''
Created on Oct 30, 2017

@author: BM13368
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_ribbon, ia_resultarea
from common.lib import utillity
from selenium.webdriver.common.by import By


class C2324210_TestClass(BaseTestCase):

    def test_C2324210(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2324210'
        
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        
        
        """
            Step 01: Launch IA API with chart in edit mode using wf_retail.mas file (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660&tool=chart&master=wf_retail
        """
        utillobj.infoassist_api_login('chart','new_retail/wf_retail','P292/S10660_chart_1', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        
        """
            Step 02 : Select Format tab > Chart Type > Other > Special > "Pyramid chart"
        """
        time.sleep(4)
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbonobj.select_other_chart_type('special', 'pyramid', 7, ok_btn_click=True)
        
        """
            Step 03: Verify the following Funnel chart Preview and query pane buckets.
        """
        metaobj.verify_query_pane_field('Measure', 'Color', 1, "Step 03::00: Verify query-pane bucket color and Measure are available")
        metaobj.verify_query_pane_field('Color', 'Tooltip', 1, "Step 03::01: Verify query-pane Color and Tooltip are avilable")
        metaobj.verify_query_pane_field('Multi-graph', 'Animate', 1, "Step 03::02: Verify Multi-graph and Animate bucket are available")
        
        """
            Verify Funnel chart colors
        """
        time.sleep(5)
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mriser!", "pale_green", "Step 03:04: Verify funnel chart second bar color from top level")
        utillobj.verify_chart_color("TableChart_1", "riser!s4!g0!mriser!", "brick_red", "Step 03:05: Verify funnel chart last bar color from bottom level")
        expected_label_list=['Series0', 'Series1', 'Series2', 'Series3', 'Series4']
        resultobj.verify_riser_legends('TableChart_1', expected_label_list, 'Step 03:06: Verify pie chart Legends')
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 10, 'Step 03:07 Verify Number of chart segment', custom_css="path[class^='riser']")
        
        """
            Step 04 : Double click "Cost of Goods" to add the field to Measure bucket.
        """
        metaobj.datatree_field_click('Cost of Goods', 2, 1)
        metaobj.verify_query_pane_field('Measure', 'Cost of Goods', 1, "Step 04::01: Verify Cost of Goods added underneath Measure bucket")
        """
            Step 05 : Drag and drop "Sale, Year" to Color bucket
        """
        metaobj.datatree_field_click("Sale,Year",1,1,'Add To Query','Color')
        metaobj.verify_query_pane_field('Color', 'Sale,Year', 1, "Step 04::02: Verify Sale,Year added underneath Color bucket")
        
        """
            Step 06 : Verify the following chart preview displayed
        """
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mriser!", "pale_green", "Step 06:01: Verify funnel chart color")
        utillobj.verify_chart_color("TableChart_1", "riser!s4!g0!mriser!", "brick_red", "Step 06:02: Verify funnel chart chart color")
        expected_label_list=['Sale Year', '2011', '2012', '2013', '2014', '2015', '2016']
        resultobj.verify_riser_legends('TableChart_1', expected_label_list, 'Step 06:03: Verify funnel chart Legends')
        utillobj.verify_chart_color("TableChart_1", "riser!s5!g0!mriser!", "orange", "Step 06:04: Verify funnel chart chart color")
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 6, 'Step 06:05 Verify Number of riser', custom_css="path[class^='riser']")
        
        """
            Step 07: Click Run and Hover on chart.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        parent_css="#jschart_HOLD_0 text[class='legend-title']"
        resultobj.wait_for_property(parent_css, 1)
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s1!g0!mriser!", "pale_green", "Step 07:01: Verify funnel chart color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s4!g0!mriser!", "brick_red", "Step 07:02: Verify funnel chart chart color")
        expected_label_list=['Sale Year', '2011', '2012', '2013', '2014', '2015', '2016']
        resultobj.verify_riser_legends('jschart_HOLD_0', expected_label_list, 'Step 07:03: Verify funnel chart Legends')
        ia_resultobj.verify_number_of_chart_segment('jschart_HOLD_0', 6, 'Step 07:04 Verify Number of riser', custom_css="path[class^='riser']")
        
        
        """
            Step 08 : Verify following run time chart and tooltip value displayed.
        """
        expected_tooltip=['Sale Year:2011', 'Cost of Goods:$34,631,123.00  (4.55%)']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0","riser!s0!g0!mriser!",expected_tooltip, "Step 08:01 verify the default tooltip values")
        """
            Step 09: Close run time chart by clicking "X" on right most corner.
        """
        utillobj.switch_to_default_content(pause=1)
        elem=self.driver.find_element_by_css_selector("#resultArea div[class*='window-close-button']")
        elem.click()
        time.sleep(3)
                
        """
            Step 10: Right click on "Revenue" in data pane "Add To Query" > Measure (Pull right) field to measure bucket.
            Right click on "Gross Profit" in data pane "Add To Query" > Tooltip (Pull right) field to Tooltip bucket.
        """
        metaobj.datatree_field_click("Revenue",1,1,'Add To Query','Measure')
        metaobj.datatree_field_click("Gross Profit",1,1,'Add To Query','Tooltip')
        metaobj.verify_query_pane_field('Tooltip', 'Gross Profit', 1, "Step 10:01: Verify Sale,Year added underneath Color bucket")
        
        """
            Step 11: Click Run and Hover on second pyramid riser "Yellow color"
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        parent_css="#jschart_HOLD_0 text[class='legend-title']"
        resultobj.wait_for_property(parent_css, 1)
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mriser!", "bar_blue", "Step 11:01: Verify funnel chart color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s2!g0!mriser!", "dark_green", "Step 11:02: Verify funnel chart chart color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s4!g0!mriser!", "brick_red", "Step 11:03: Verify funnel chart chart color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g1!mriser!", "bar_blue", "Step 11:04: Verify funnel chart color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s2!g1!mriser!", "dark_green", "Step 11:05: Verify funnel chart chart color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s4!g1!mriser!", "brick_red", "Step 11:06: Verify funnel chart chart color")
        expected_label_list=['Sale Year', '2011', '2012', '2013', '2014', '2015', '2016']
        resultobj.verify_riser_legends('jschart_HOLD_0', expected_label_list, 'Step 11:07: Verify funnel chart Legends')
        ia_resultobj.verify_number_of_chart_segment('jschart_HOLD_0', 12, 'Step 11:08: Verify Number of riser', custom_css="path[class^='riser']")
        
        """
            Step 12: Verify following run time chart and tooltip value displayed.
            Verify tooltip information
        """
        expected_tooltip=['Sale Year:2014', 'Revenue:$126,675,660.19  (11.94%)', 'Gross Profit:$36,298,871.19']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0","riser!s3!g1!mriser!",expected_tooltip, "Step 11:09 Expect to see Revenue and Gross Profit added.")
        
        """
            Step 13 :Click Save in the toolbar and save as "C2324204" > Click Save
            Step 14 : Close the tool window
        """
        utillobj.switch_to_default_content(pause=1)
        time.sleep(1)
        obj1=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(obj1,Test_Case_ID + '_Actual_step12', image_type='actual',x=1, y=1, w=-1, h=-1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
            Step 15 : Restore using IA API:
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660%C2324204.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S10660_chart_1', mrid='mrid', mrpass='mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mriser!", "bar_blue", "Step 15:01: Verify funnel chart color")
        utillobj.verify_chart_color("TableChart_1", "riser!s2!g0!mriser!", "dark_green", "Step 15:02: Verify funnel chart chart color")
        utillobj.verify_chart_color("TableChart_1", "riser!s4!g0!mriser!", "brick_red", "Step 15:03: Verify funnel chart chart color")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g1!mriser!", "bar_blue", "Step 15:04: Verify funnel chart color")
        utillobj.verify_chart_color("TableChart_1", "riser!s2!g1!mriser!", "dark_green", "Step 15:05: Verify funnel chart chart color")
        utillobj.verify_chart_color("TableChart_1", "riser!s4!g1!mriser!", "brick_red", "Step 15:06: Verify funnel chart chart color")
        expected_label_list=['Sale Year', '2011', '2012', '2013', '2014', '2015', '2016']
        resultobj.verify_riser_legends('TableChart_1', expected_label_list, 'Step 15:07: Verify funnel chart Legends')
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 12, 'Step 15:08: Verify Number of riser', custom_css="path[class^='riser']")
               

if __name__ == "__main__":
    unittest.main()