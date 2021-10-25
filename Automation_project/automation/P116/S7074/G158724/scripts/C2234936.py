'''
Created on May 17, 2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2234936
TestCase Name = Verify PIE in others tab under Format menu.
'''
import unittest
import time, re
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, visualization_ribbon, visualization_metadata, ia_resultarea, active_miscelaneous, ia_ribbon
from common.lib import utillity
from common.locators.ia_ribbon_locators import IaRibbonLocators


class C2234936_TestClass(BaseTestCase):

    def test_C2234936(self):
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        Test_Case_ID="C2234936"
        
        def check_visible_chart_list(expected_visible, msg):
            actual_visible=[]
            chart_elements=self.driver.find_elements(*IaRibbonLocators.__dict__['pie_buttons'])
            for i in range(len(chart_elements)):
                if bool(re.match('.*disabled*.', chart_elements[i].get_attribute("class"))):
                    pass
                else:
                    visible_obj=chart_elements[i].find_element_by_css_selector('img').get_attribute("id").replace('ChartTypeButton_Icon_','')
                    actual_visible.append(visible_obj)
            utillobj.as_List_equal(expected_visible,actual_visible, msg)
        
        """ Step 1: Right click on folder created in IA and select New > Chart and select Reporting server as GGSALES.
                    On the Format tab, in the Output Types group, click Active report.
        """
        utillobj.infoassist_api_login('chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        parent_css="#TableChart_1 g.chartPanel g text"
        result_obj.wait_for_property(parent_css, 11)
        time.sleep(1)
        ribbonobj.change_output_format_type('active_report')
        time.sleep(1)
        parent_css="#HomeTab #HomeFormatType [class='bi-button-label']"
        result_obj.wait_for_property(parent_css, 1, string_value='ActiveReport', with_regular_exprestion=True)
        time.sleep(1)
         
         
        """ Step 2: Select data from the left pane (Dimensions and Measures)
                    Category under Horizontal Axis
                    Unit Sales under Vertical Axis
        """
        metadataobj.datatree_field_click('Category', 2, 1)
        parent_css="#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']"
        result_obj.wait_for_property(parent_css, 1, string_value='Category', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Unit Sales', 2, 1)
        parent_css="#TableChart_1 g.chartPanel g text[class='yaxis-title']"
        result_obj.wait_for_property(parent_css, 1, string_value='UnitSales', with_regular_exprestion=True)
         
         
        """ Step 3: Expect to see the following Preview Pane.
        """        
        result_obj.verify_xaxis_title("TableChart_1", 'Category', "Step 3.1: Verify X-Axis Title")
        result_obj.verify_yaxis_title("TableChart_1", 'Unit Sales', "Step 3.2: Verify Y-Axis Title")
        expected_xval_list=['Coffee']
        expected_yval_list=['0', '100K', '200K', '300K', '400K', '500K', '600K']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 3.3: ')
        result_obj.verify_number_of_riser('TableChart_1', 1, 1, 'Step 3.4: ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar!', 'bar_blue1', 'Step 3.5: Verify Color')
         
         
        """ Step 4: Select Format > Other
        """
        ribbonobj.select_ribbon_item("Format", "Other")
        time.sleep(5)
         
         
        """ Step 5: Switch to Pie on Others tab and verify available pie types
                    Verify it shows 4 different Pie chart types as follows:
                    - Pie
                    - Ring Pie
                    - Pie
                    - Ring Pie
        """
        ia_ribbonobj.select_other_chart_type('pie', 'pie', 1)
        time.sleep(1)
        expected_visible=['Pie_Pie', 'Pie_Ring', 'Pie_Multi', 'Pie_Multi_Ring']
        check_visible_chart_list(expected_visible, 'Step 5: Verify it shows 4 different Pie chart types')
        time.sleep(2)
         
                 
        """ Step 6: Select first Pie (The most widely used chart for displaying percentages of a total.)
                    Click OK.
        """
        driver.find_element_by_css_selector("div[id*='Chart'][id$='OkBtn']").click()
         
         
        """ Step 7: Click RUN.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 3, 'Step 7.1: Expect to see the three PIE Chart Visible.')
        expected_label_list=['Category', 'Coffee', 'Food', 'Gifts']
        result_obj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 7.2: ')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!mwedge', 'bar_blue', 'Step 7.3: Verify second pie color.')  
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Category', 'Step 7.4: Verify pie Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 7.5: Verify pie Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 7.6: Verify pie Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 7.7: Verify pie Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        result_obj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['Unit Sales'],"'Step 7.8: Verify pie Chart labels'",custom_css="text[class^='pieLabel!g']",same_group=True)
        parent_elem=driver.find_element_by_css_selector("#MAINTABLE_wbody0")
        utillobj.click_on_screen(parent_elem, coordinate_type='start')
        parent_elem=driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class*='riser!s0!g0!mwedge']")
        utillobj.click_on_screen(parent_elem, coordinate_type='middle', x_offset=5, y_offset=9, mouse_duration=2.5)
        expected_tooltip_list=['Category:Coffee', 'Unit Sales:1376266  (37.31%)', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g0!mwedge', expected_tooltip_list, 'Step 7.9: verify the default tooltip values',default_move=True)
        utillobj.switch_to_default_content(pause=5)
        time.sleep(10)
         
        """ Step 8: Back in the PIE menu under Others, select the Ring PIE.
                    Click Run.
                    Expect to see an alternate PIE from the Others/PIE menu.
        """
        ribbonobj.select_ribbon_item("Format", "Other")
        time.sleep(5)
        ia_ribbonobj.select_other_chart_type('pie', 'ring_pie', 4, ok_btn_click=True)
        time.sleep(5)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 3, 'Step 8.1: Expect to see the three PIE Chart Visible.')
        expected_label_list=['Category', 'Coffee', 'Food', 'Gifts']
        result_obj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 8.2: ')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!mwedge', 'bar_blue', 'Step 8.3: Verify second pie color.')  
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Category', 'Step 8.4: Verify pie Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 8.5: Verify pie Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 8.6: Verify pie Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 8.7: Verify pie Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        result_obj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['3.7M'],"'Step 8.8: Verify pie Chart labels'",custom_css="text[class^='totalLabel!g']",same_group=True)
        result_obj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['Unit Sales'],"'Step 8.9: Verify pie Chart labels'",custom_css="text[class^='pieLabel!g']",same_group=True)
        parent_elem=driver.find_element_by_css_selector("#MAINTABLE_wbody0")
        utillobj.click_on_screen(parent_elem, coordinate_type='start')
        parent_elem=driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class*='riser!s0!g0!mwedge']")
        utillobj.click_on_screen(parent_elem, coordinate_type='start', x_offset=5, y_offset=20, mouse_duration=2.5)
        expected_tooltip_list=['Category:Coffee', 'Unit Sales:1376266  (37.31%)', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g0!mwedge', expected_tooltip_list, 'Step 8.10: verify the default tooltip values',default_move=True)
        utillobj.switch_to_default_content(pause=5)
         
        utillobj.switch_to_default_content(pause=2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()