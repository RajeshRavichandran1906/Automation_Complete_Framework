'''
Created on Jan 30, 2018

@author: Magesh/Updated by :  Bhagavathi

Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227746
TestCase Name = Report-Other: Verify FUSION chart output for AHTML.
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, active_miscelaneous,active_chart_rollup,ia_resultarea
from common.lib import utillity
from common.wftools import active_report

class C2511616_TestClass(BaseTestCase):

    def test_C2511616(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID='C2511616'
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        rollobj=active_chart_rollup.Active_Chart_Rollup(self.driver) 
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        fex_name = "AHTML_FUSION.fex"
        
        """
        Step 01 : Sign in to WebFOCUS as a Basic user
        Step 02 :Expand folder P292_S10032_G157266
        Execute the following URL:
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10032_G157266%252FAHTML_OFF&BIP_item=AHTML_FUSION.fex
        """
        active_reportobj.run_active_report_using_api(fex_name, column_css="#MAINTABLE_wbody0_ft", synchronize_visible_element_text='DEALER_COST, RETAIL_COST by COUNTRY')
        result_obj.wait_for_property("#MAINTABLE_wbody0_ft tbody", 1, string_value='DEALER_COST,RETAIL_COSTbyCOUNTRY', with_regular_exprestion=True)
        
        
        """
        Step 03 : Verify the report is generated.
        Verify correct output displayed on run. Chart toolbar is present on the top.
        """
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, RETAIL_COST by COUNTRY", "Step 03.1 : Verify chart title ")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Original Chart'],"Step 03.2: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.3: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.4: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
#         browser=utillobj.parseinitfile('browser')
#         if browser == 'chrome' and 'firefox':
        def label(expected, msg):
            css_val = "#MAINTABLE_wbody0 span[id*='Piet']  text[text-anchor] tspan"
            chart_text = [elem.text.strip() for elem in self.driver.find_elements_by_css_selector(css_val) if elem != '']
            actual_value = [elem for elem in chart_text if elem != '']
            print(actual_value)
            utillity.UtillityMethods.asequal(self, chart_text, expected, msg)
        expected=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY', '0', '14,000', '28,000', '42,000', '56,000', '70,000', '', '', '', '', '', '', '', '', '', '']
        label(expected,"Step 03.5:expected labels")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 10, 'Step 03.6: Verify number of bar risers.', custom_css="span[id*='Piet'] svg>g[class='highcharts-tracker'] rect")
        riser_css = driver.find_elements_by_css_selector("#MAINTABLE_wbody0 span[id*='Piet'] svg>g[class='highcharts-tracker'] rect")
        act_fill_opacity = riser_css[0].get_attribute("fill-opacity")
        print(act_fill_opacity)
        exp_fill_opacity = '0.000001'
        utillobj.asequal(act_fill_opacity, exp_fill_opacity, 'Step 03.7: Verify fill_opacity.')
        time.sleep(3) 
#         ele=driver.find_element_by_css_selector("#MAINTABLE_wbody0")
#         utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step03_'+browser, image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 04 :  Click on first icon and select Add Y > RETAIL_COST to remove that field from the chart. 
        Verify user is able to remove Y-axis fields.
        Verify only Dealer_Cost is displayed on chart.
        """
        time.sleep(3)
        rollobj.select_chartmenubar_option('MAINTABLE_0', 0, 'Add (Y)->RETAIL_COST', 0, custom_css='cpop')
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST by COUNTRY", "Step 04.1 : Verify chart title ")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Original Chart'],"Step 04.2: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.3: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.4: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)   
#         browser=utillobj.parseinitfile('browser')
#         if browser == 'chrome' and 'firefox':
        result_obj.verify_xaxis_title("MAINTABLE_wbody0","DEALER_COST","Step 04.5: Verify Xaxis title",custom_css="svg g[class='highcharts-legend']")
        expected=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY', '0', '12,000', '24,000', '36,000', '48,000', '60,000', '', '', '', '', '']
        label(expected,"Step 4.6:expected labels")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 5, 'Step 04.7: Verify number of bar risers.', custom_css="span[id*='Piet'] svg>g[class='highcharts-tracker'] rect")
        riser_css = driver.find_elements_by_css_selector("#MAINTABLE_wbody0 span[id*='Piet'] svg>g[class='highcharts-tracker'] rect")
        act_fill_opacity = riser_css[0].get_attribute("fill-opacity")
        print(act_fill_opacity)
        exp_fill_opacity = '0.000001'
        utillobj.asequal(act_fill_opacity, exp_fill_opacity, 'Step 04.8: Verify fill_opacity.')
        time.sleep(3)
#         ele=driver.find_element_by_css_selector("#MAINTABLE_wbody0")
#         utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step04_'+browser, image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 05: Click Scatter chart option from the toolbar.Verify chart type is changed from Bar to Scatter without any error.
        """
        time.sleep(3)
        rollobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 4)
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST by COUNTRY", "Step 05.1 : Verify chart title ")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Original Chart'],"Step 05.2: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.3: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.4: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)   
#         browser=utillobj.parseinitfile('browser')

        result_obj.verify_xaxis_title("MAINTABLE_wbody0","DEALER_COST","Step 05.5: Verify Xaxis title",custom_css="svg g[class='highcharts-legend']")
        expected=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W', 'GERMANY', '0', '12,000', '24,000', '36,000', '48,000', '60,000', '37,853', '4,631', '41,235', '5,512', '54,563']
        label(expected,"Step 5.6:expected labels")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 5, 'Step 05.7: Verify number of scatter.', custom_css="span[id*='Piet'] svg>g[class='highcharts-series-group'] path")
        time.sleep(3)
#         ele=driver.find_element_by_css_selector("#MAINTABLE_wbody0")
#         utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step05_'+browser, image_type='actual',x=1, y=1, w=-1, h=-1)
#         time.sleep(2)
         
        """
        Step 06: Dismiss the window and logout.http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()