'''
Created on Oct 12, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2197666
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,wf_mainpage,wf_legacymainpage
from common.lib import utillity
import unittest,time,re


class C2197666_TestClass(BaseTestCase):

    def test_C2197666(self):
        
        driver = self.driver #Driver reference object created
        legacymainobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        node_name = utillobj.parseinitfile('node')
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        
        """
        Step 01: Run the attached 144459.fex from text editor in adhoc page.
        
        """
        def unxrh():
            node = utillobj.parseinitfile('nodeid')
            port = utillobj.parseinitfile('httpport')
            context = utillobj.parseinitfile('wfcontext')
            setup_url = 'http://' + node + ':' + port + context + '/'
            self.driver.get(setup_url)
            utillobj.login_wf('mrid','mrpass')
            time.sleep(20)
            legacymainobj.select_repository_folder_item_menu('P116->S7074','144459','Edit With...->Text Editor')
            legacymainobj.click_text_editor_ribbon_button('Run')
            time.sleep(2)
            utillobj.switch_to_window(1)

            time.sleep(5)
            utillobj.switch_to_window(1)
            
            time.sleep(2)
            miscelanousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'RETAIL_COST BY COUNTRY', 'Step 01: Verify Chart title')
           
            """
               Step 02: Click advanced chart icon from chart window toolbar.
            """             
            self.driver.find_element_by_css_selector('[title="Advanced Chart"]').click()
                
            """
               Step 03: Select chart tab
               """
            self.driver.find_element_by_css_selector('[id="ttpanel_1_1_0"]').click()
            
            """
            Step 04: Verify that below charts displayed clearly without an error.
            """
            time.sleep(2)
            val2 = ['Bar', 'StackedBar', 'PercentBar', 'Column', 'StackedColumn', 'PercentColumn', 'ColumnDepth', 'StackedDepth', 'PercentDepth', '3DColumn', 'Pie', 'PiewithDepth', 'Donut(Cylinder)', 'DonutwithDepth', 'Donut', 'Line', 'Curved', 'Straight', 'Curved+Markers', 'Straight+Markers', 'Step', 'Area', 'StackedArea', 'PercentArea', '3DArea', 'Scatter(XYPlot)', 'Bubble', 'Funnel', 'Pyramid', 'Heatmap', 'Waterfall', 'Histogram', 'RadarLine', 'RadarArea', 'TagCloud']
        
            val = self.driver.find_elements_by_css_selector("[id*='chticon_1'] g>text[class='title']")
            actual_val = []
            for i in range(len(val)):
                actual_val.append(val[i].text.strip("\n").replace(" ",""))
            utillobj.as_List_equal(actual_val,val2,'Step 04: Verify the chart type icons are visible, Product Failure - ACT-1075')
            driver.close()
            utillobj.switch_to_window(0)

        
        
        def wfinst():
            node = utillobj.parseinitfile('nodeid')
            port = utillobj.parseinitfile('httpport')
            context = utillobj.parseinitfile('wfcontext')
            setup_url = 'http://' + node + ':' + port + context + '/'
            self.driver.get(setup_url)
            utillobj.login_wf('mrid','mrpass')
            time.sleep(20)
            mainobj.select_repository_folder_item_menu('P116->S7074','144459','Edit With Text Editor')
            time.sleep(5)
            utillobj.switch_to_window(1)
            win=driver.window_handles
            mainobj.click_text_editor_ribbon_button('Run')
            time.sleep(3)
            utillobj.switch_to_window(2,custom_windows=win)
            time.sleep(2)
            miscelanousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'RETAIL_COST BY COUNTRY', 'Step 01: Verify Chart title')
           
            """
               Step 02: Click advanced chart icon from chart window toolbar.
            """             
            self.driver.find_element_by_css_selector('[title="Advanced Chart"]').click()
                
            """
               Step 03: Select chart tab
               """
            self.driver.find_element_by_css_selector('[id="ttpanel_1_1_0"]').click()
            
            """
            Step 04: Verify that below charts displayed clearly without an error.
            """
            time.sleep(2)
            val2 = ['Bar', 'StackedBar', 'PercentBar', 'Column', 'StackedColumn', 'PercentColumn', 'ColumnDepth', 'StackedDepth', 'PercentDepth', '3DColumn', 'Pie', 'PiewithDepth', 'Donut(Cylinder)', 'DonutwithDepth', 'Donut', 'Line', 'Curved', 'Straight', 'Curved+Markers', 'Straight+Markers', 'Step', 'Area', 'StackedArea', 'PercentArea', '3DArea', 'Scatter(XYPlot)', 'Bubble', 'Funnel', 'Pyramid', 'Heatmap', 'Waterfall', 'Histogram', 'RadarLine', 'RadarArea', 'TagCloud']
        
            val = self.driver.find_elements_by_css_selector("[id*='chticon_1'] g>text[class='title']")
            actual_val = []
            for i in range(len(val)):
                actual_val.append(val[i].text.strip("\n").replace(" ",""))  
                utillobj.as_List_equal(actual_val,val2,'Step 04: Verify the chart type icons are visible, Product Failure - ACT-1075')
            driver.close()
            utillobj.switch_to_window(1)
            driver.close()
            utillobj.switch_to_main_window()

        if bool(re.match('wfinst..', node_name)):
            wfinst()
        else:
            unxrh()

if __name__ == "__main__":
    unittest.main()