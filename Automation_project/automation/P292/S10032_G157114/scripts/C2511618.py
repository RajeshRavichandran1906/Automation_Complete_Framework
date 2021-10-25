'''
Created on Jan 03, 2018

@author: Praveen Ramkumar/Updated by : Bhagavathi

Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227748
TestCase Name = Report-Other: Verify JSFUSION chart output for AHTML.
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, active_miscelaneous,active_chart_rollup
from common.lib import utillity
from common.wftools import active_report

class C2511618_TestClass(BaseTestCase):

    def test_C2511618(self):
        
        """
            TESTCASE VARIABLES
        """
        
        Test_Case_ID='C2511618'
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        rollobj=active_chart_rollup.Active_Chart_Rollup(self.driver) 
        active_reportobj=active_report.Active_Report(self.driver)
        fex_name = "AHTML_JSFUSION.fex"
        
        """
            Step 01 : Sign in to WebFOCUS as a Basic user http://machine:port/{alias}
            Step 02 :Expand folder P292_S10032_G157266 Execute the following URL:http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10032_G157266%252FAHTML_OFF&BIP_item=AHTML_JSFUSION.fex
        """
        active_reportobj.run_active_report_using_api(fex_name)
        result_obj.wait_for_property("#MAINTABLE_wbody0_ft tbody", 1, string_value='DEALER_COST,RETAIL_COSTBYCOUNTRY', with_regular_exprestion=True)
        
        """
             Step 03 : Verify the report is generated.
        """
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, RETAIL_COST BY COUNTRY", "Step 03.1 : Verify chart title ")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 03.2: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.3: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.4: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        def label(expected, msg):
            css_val = "#MAINTABLE_wbody0 span[id*='Piet']  text[text-anchor] tspan"
            chart_text = [elem.text.strip() for elem in self.driver.find_elements_by_css_selector(css_val) if elem != '']
            actual_value = [elem for elem in chart_text if elem != '']
            utillity.UtillityMethods.asequal(self, chart_text, expected, msg)
            print(actual_value)
        ele=driver.find_element_by_css_selector("#MAINTABLE_wbody0")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step03', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)    
        expected=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY', '0', '14,000', '28,000', '42,000', '56,000', '70,000', '', '', '', '', '', '', '', '', '', '']
        label(expected,"Step 03.5:expected labels")
              
        """
             Step 04 :  Click on first icon and select Add Y > RETAIL_COST to remove that field from the chart.
                        Verify user is able to remove Y-axis fields.
                        Verify only Dealer_Cost is displayed on chart.
        """
        rollobj.select_chartmenubar_option('MAINTABLE_0', 0, 'Add (Y)->RETAIL_COST', 0, custom_css='cpop')
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST BY COUNTRY", "Step 04.1 : Verify chart title ")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 04.2: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.3: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.4: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)   
        expected=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY', '0', '12,000', '24,000', '36,000', '48,000', '60,000', '', '', '', '', '']
        label(expected,"Step 4.5:expected labels")
        ele=driver.find_element_by_css_selector("#MAINTABLE_wbody0")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step03', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0","DEALER_COST","Step 04.6: Verify Xaxis title",custom_css="svg g[class='highcharts-legend']")
            
        """
             Step 05: Click Scatter chart option from the toolbar.Verify chart type is changed from Line to Scatter without any error.
        """
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST BY COUNTRY", "Step 05.1 : Verify chart title ")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 05.2: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.3: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.4: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)   
        result_obj.verify_xaxis_title("MAINTABLE_wbody0","DEALER_COST","Step 05.5: Verify Xaxis title",custom_css="svg g[class='highcharts-legend']")
        rollobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 4)
        time.sleep(3)
        expected=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W', 'GERMANY', '0', '12,000', '24,000', '36,000', '48,000', '60,000', '37,853', '4,631', '41,235', '5,512', '54,563']
        label(expected,"Step 5.6:expected labels")
        ele=driver.find_element_by_css_selector("#MAINTABLE_wbody0")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step03', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        
        """
             Step 06: Dismiss the window and logout.http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()     
        