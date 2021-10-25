'''
Created on Oct 13, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7215
Test Case =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2203708
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon,visualization_metadata,active_miscelaneous
from common.lib.global_variables import Global_variables
from common.lib import utillity
import unittest,time

class C2203708_TestClass(BaseTestCase):

    def test_C2203708(self):
        
        
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
        Step 01: Create IA report using CAR master file and change the report to AHTML format
        """
        utillobj.infoassist_api_login('report', 'ibisamp/car', 'P116/S7074', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#singleReportCaptionLabel", 1, 65)
        
        ribbonobj.change_output_format_type('active_report', location='Home')
        
        """
        Step 02: Add Country as a by field, Sales as SUM, and Dealer Cost as PRINT. Run the report
        From query pane, right click on sales field and select More -> Aggregation functions -> Sum
        """
        time.sleep(5)
        metadataobj.datatree_field_click('COUNTRY', 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 6, expire_time=15)
        
        metadataobj.datatree_field_click('SALES', 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 12, expire_time=15)
        
        metadataobj.datatree_field_click('DEALER_COST', 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 18, expire_time=15)
         
        metadataobj.querytree_field_click('SALES', 1, 1,'More', 'Aggregation Functions', 'Sum')
        time.sleep(5)
        metadataobj.verify_query_pane_field('Sum', 'SUM.SALES', 1, 'Step 02.1: Expect to see the following report with two measure fields')
        metadataobj.verify_query_pane_field('Sum', 'DEALER_COST', 2, 'Step 02.2: Expect to see the following report with two measure fields')
        metadataobj.verify_query_pane_field('By', 'COUNTRY', 1, 'Step 02.3: Expect to see the following report with one by field')
        time.sleep(3)
        
        ribbonobj.select_tool_menu_item('menu_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 40)
        utillobj.switch_to_frame(pause=3)
    
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2203708_Ds01.xlsx','Step 02: Expect to see the following report with two measure fields and one by field')
        
        """
        Step 03: Click on the dealer cost down arrow and select Chart -> Pie -> Dealer Cost
        """
        miscelaneousobj.select_menu_items('ITableData0', 2, 'Chart','Pie','DEALER_COST')
        parent_css="#wall1 #wbody1_ft table td"
        utillobj.synchronize_with_visble_text(parent_css, 'DEALER_COST by DEALER_COST', 15)
        
        miscelaneousobj.verify_popup_title('wall1', 'DEALER_COST by DEALER_COST', 'Step 03: Expect to see the following chart created within AHTML report without any error')
      
        """
        Step 04: Drag it out of the way, click the dealer cost down arrow again and select Window -> Tabs
        """
        miscelaneousobj.move_active_popup('1', 300+Global_variables.current_working_area_browser_x, 150+Global_variables.current_working_area_browser_y)
        time.sleep(2)
        miscelaneousobj.select_menu_items('ITableData0', 2, 'Window','Tabs')
        time.sleep(3)
        val_1 = self.driver.find_element_by_css_selector('[id="MAINTABLE_wmenu0"]').text
        utillobj.asequal(val_1,' Report \nChart','Step 04: Expect to see the following AHTML report and chart in tab view')
        
        """
        Step 05: From the Report tab, click the down arrow of SALES and select Chart -> Pie -> Sales
        """
        miscelaneousobj.navigate_tabbed_report(0,1)
        time.sleep(1)
        miscelaneousobj.select_menu_items('ITableData0', 1, 'Chart','Pie','SALES')
        time.sleep(3)
        heading = self.driver.find_element_by_xpath("//div[@id='wbody2_fmg']/div[1]")
        utillobj.asequal(heading.text, 'SALES by SALES', 'Step 05: Expect to see the following "SALES by SALES" chart')
        val_2 = self.driver.find_element_by_css_selector('[id="MAINTABLE_wmenu0"]').text
        utillobj.asequal(val_2,' Report \nChart\nChart','Step 05: Verify that the report and charts are in tab view')
        
        """
        Step 06: Click back over to Report again and select Window -> Cascade from any of the field dropdown menu
        """
        
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
        utillobj.switch_to_frame(pause=3)
        time.sleep(3)
        miscelaneousobj.navigate_tabbed_report(0,1)
#         self.driver.find_element_by_css_selector('[id="tab_0"]').click()
        time.sleep(3)
        miscelaneousobj.select_menu_items('ITableData0', 2, 'Window','Cascade')
        time.sleep(5)
        before_x = self.driver.find_element_by_css_selector('[id="wall1"]').location['x']
        miscelaneousobj.move_active_popup('2', Global_variables.current_working_area_browser_x+450, Global_variables.current_working_area_browser_y+200)
        time.sleep(3)
        miscelaneousobj.move_active_popup('1', Global_variables.current_working_area_browser_x+300, Global_variables.current_working_area_browser_y+200)
        time.sleep(2)
        after_x = self.driver.find_element_by_css_selector('[id="wall1"]').location['x']
        utillobj.as_GE(after_x, before_x, 'Step 06: Verify that the first chart created has controls drag it around')
        utillobj.switch_to_default_content(pause=3)
        
if __name__ == "__main__":
    unittest.main()