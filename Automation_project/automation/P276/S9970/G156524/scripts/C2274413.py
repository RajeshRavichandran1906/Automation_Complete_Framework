'''
Developed By  : KK14897
Developed Date: 25-Sep-2018
 
Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/9970&group_by=cases:section_id&group_id=156524&group_order=asc
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2274413
TestCase Name = Auto Drill not selected after Report or Chart conversion with auto drill enabled
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.report import Report
from common.wftools.chart import Chart
from common.lib import utillity

class C2274413_TestClass(BaseTestCase):
    
    def test_C2274413(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        report_obj = Report(self.driver)
        chart_obj = Chart(self.driver)
        
        """    
            Step 01 : Launch IA, Report using Api link
            http://machine:port/alias/ia?tool=Report&master=baseapp/wf_retail&item=IBFS%3A%2FWFC%2FRepository%2FP276_S9970/G156524   
        """
        report_obj.invoke_ia_tool_using_api_login("report", "baseapp/wf_retail", 'mrid')
        utillobj.wait_for_page_loads(120)
        
        """    
            Step 02 : Double click "Product,Category" from Product dimension
        """
        report_obj.double_click_on_datetree_item("Product->Product->Product,Category", 1)
        report_obj.wait_for_visible_text("#TableChart_1 div[class^='x']", 'Product', 20)
        
        """    
            Step 03 : Double click "Revenue" from Sales measures
        """
        report_obj.double_click_on_datetree_item("Measure Groups->Sales->Revenue", 1)
        report_obj.wait_for_number_of_element("#TableChart_1 div[class^='x']", 18, 20)
        
        """    
            Step 04 : Verify the following report is displayed.    
        """
        coln_list = ["Product", ""]
        report_obj.verify_report_titles_on_preview(2, 2, "TableChart_1 ", coln_list, "Step 04.01: Verify column titles")
        
        """    
            Step 05 : Select "Format tab" > Click "Auto Drill"   
        """
        report_obj.select_ia_ribbon_item("Format", "auto_drill")
        
        """    
            Step  6 : Select "Chart" in the Home Tab 
        """
        report_obj.select_ia_ribbon_item("Home", "chart")
        report_obj.wait_for_number_of_element('rect[class*="riser!s0!g3!mbar!"]', 1, 20)
        
        """    
            Step 07 : Verify "Report" is converted to "Chart    
        """
        x_axis_title=["Product Category"]
        y_axis_title=['Revenue']
        x_label=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        y_label=['0' ,'50M', '100M', '150M', '200M', '250M', '300M', '350M']
        report_obj.verify_element_visibility(element_css='rect[class*="riser!s0!g3!mbar!"]', visible=True, msg="Step 07.01: Very report is converted to chart")
        chart_obj.verify_number_of_risers("#pfjTableChart_1 rect", 7, 1, msg="Step 07.02")
        chart_obj.verify_chart_color("pfjTableChart_1", "riser!s0!g3!mbar!", 'bar_blue', msg="Step 07.03: verify chart color")
        chart_obj.verify_x_axis_title_in_preview(x_axis_title, msg="Step 07.04")
        chart_obj.verify_x_axis_label_in_preview(x_label, msg="Step 07.05")
        chart_obj.verify_y_axis_label_in_preview(y_label, msg="Step 07.06")
        chart_obj.verify_y_axis_title_in_preview(y_axis_title, msg="Step 07.07")
        
        """    
            Step 08 : Select "Format Tab"    
        """
#         report_obj.switch_ia_ribbon_tab("Format")
#         run_with_button = self.driver.find_element_by_css_selector("#FormatAutoDrillCluster_altButton")
#         run_with_button.click()
#         time.sleep(6)
#         report_obj.wait_for_number_of_element('div[id*="FormatAutoDrill"][class*="tool-bar-button-checked"]', 1, 20)
        report_obj.switch_ia_ribbon_tab("Format")
        report_obj.select_ia_ribbon_item("Format", "run_with")
        report_obj.select_ia_ribbon_item("Format", "auto_drill")
        #report_obj.switch_ia_ribbon_tab("Format", "run_with")
#         time.sleep(3)
#         report_obj.select_ia_ribbon_item("Format", "auto_drill")
#         time.sleep(3)
        
        """   
            Step 09 : Verify "Auto Drill" is enabled    
        """
        report_obj.verify_ribbon_item_is_enabled('format_auto_drill', '09.01')
        
#         report_obj.verify_element_visibility(element_css='div[id*="FormatAutoDrill"][class*="tool-bar-button-checked"]', visible=True, msg="Step 09: Verify Autodrill is enabled")
        """    
            Step 10 : Logout of the IA API using the following URL.
            http://machine:port/alias/service/wf_security_logout.jsp  
        """
        report_obj.api_logout()
        
        """    
            Step 11 : Launch IA, Chart using Api link
            http://machine:port/alias/ia?tool=Chart&master=baseapp/wf_retail&item=IBFS%3A%2FWFC%2FRepository%2FP276_S9970/G156524  
        """
        report_obj.invoke_ia_tool_using_api_login("chart", "baseapp/wf_retail", 'mrid')
        utillobj.wait_for_page_loads(120)
        """    
            Step 12 : Double click "Product,Category" and "Revenue"   
        """
        report_obj.double_click_on_datetree_item("Product->Product->Product,Category", 1)
        report_obj.wait_for_visible_text("#pfjTableChart_1 text[class*='xaxisOrdinal-title']", 'Product Category', 20)
        report_obj.double_click_on_datetree_item("Measure Groups->Sales->Revenue", 1)
        report_obj.wait_for_visible_text("#pfjTableChart_1 text[class*='yaxis-title']", "Revenue", 20)
        
        """    
            Step 13 : Select "Format" > "Auto Drill".   
        """
        report_obj.select_ia_ribbon_item("Format", "auto_drill")
        
        """    
            Step 14 : Select "Report" in the Home Tab
        """
        report_obj.select_ia_ribbon_item("Home", "report")
        report_obj.wait_for_visible_text("#TableChart_1 div[class^='x']", 'Product', 50)
        
        """    
            Step 15 : Verify "Chart" is converted to "Report"   
        """
        coln_list = ["Product", ""] 
        report_obj.verify_report_titles_on_preview(2, 2, "TableChart_1 ", coln_list, "Step 15.01 : Verify Chart is converted to Report")
        """    
            Step 16 : Select "Format tab" > Verify "Auto Drill" is enabled   
        """
        report_obj.switch_ia_ribbon_tab("Format")
        report_obj.wait_for_number_of_element('div[id*="FormatAutoDrill"][class*="tool-bar-button-checked"]', 1, 20)
        report_obj.verify_element_visibility(element_css='div[id*="FormatAutoDrill"][class*="tool-bar-button-checked"]', visible=True, msg="Step 16.01: Verify Autodrill is enabled")
        
        """    
            Step 17 : Logout of the IA API using the following URL.
            http://machine:port/alias/service/wf_security_logout.jsp   
        """
        
if __name__ == '__main__':
    unittest.main()