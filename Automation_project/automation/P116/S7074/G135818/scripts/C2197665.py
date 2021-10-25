'''
Created on Oct 12, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2197665
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,wf_mainpage, wf_legacymainpage
from common.lib import utillity
import unittest,time,re

class C2197665_TestClass(BaseTestCase):

    def test_C2197665(self):
        
        driver = self.driver #Driver reference object created
        legacymainobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        mainobj=wf_mainpage.Wf_Mainpage(self.driver)
        node_name = utillobj.parseinitfile('node')
        
        def unxrh():
            """
            Step 01: Run the attached 142140.fex from text editor in adhoc page. 
            
            """
            utillobj = utillity.UtillityMethods(self.driver)
            miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
            mainobj = wf_mainpage.Wf_Mainpage(self.driver)
            node = utillobj.parseinitfile('nodeid')
            port = utillobj.parseinitfile('httpport')
            context = utillobj.parseinitfile('wfcontext')
            setup_url = 'http://' + node + ':' + port + context + '/'
            self.driver.get(setup_url)
            utillobj.login_wf('mrid','mrpass')
            time.sleep(20)
            legacymainobj.select_repository_folder_item_menu('P116->S7074','142140','Edit With...->Text Editor')
            time.sleep(4)
            legacymainobj.click_text_editor_ribbon_button('Run')
            time.sleep(2)
            utillobj.switch_to_window(1)
            
            """
            Step 02: Once report opened click on any field eg: Seats click dropdown and select Chart/Rollup Tool
            """
            miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 02.1: Verify page summary")
            column_list=['COUNTRY','CAR','MODEL','SEATS']
            miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 02.1: Verify all columns listed on the report')    
            time.sleep(2)    
            miscelanousobj.select_menu_items('ITableData0', 3, 'Chart/Rollup Tool')
            time.sleep(2)
            
            """
            Step 03: Now click on Chart button from Chart/Rollup Tool.
            """
            self.driver.find_element_by_css_selector('[id="ttpanel_1_1_0"]').click()
             
            """
            Step 04: Verify the chart type icons are visible.
            """
            time.sleep(3)        
            val2 = ['Bar', 'StackedBar', 'PercentBar', 'Column', 'StackedColumn', 'PercentColumn', 'ColumnDepth', 'StackedDepth', 'PercentDepth', '3DColumn', 'Pie', 'PiewithDepth', 'Donut(Cylinder)', 'DonutwithDepth', 'Donut', 'Line', 'Curved', 'Straight', 'Curved+Markers', 'Straight+Markers', 'Step', 'Area', 'StackedArea', 'PercentArea', '3DArea', 'Scatter(XYPlot)', 'Bubble', 'Funnel', 'Pyramid', 'Heatmap', 'Waterfall', 'Histogram', 'RadarLine', 'RadarArea', 'TagCloud']
            
            val = self.driver.find_elements_by_css_selector("[id*='chticon_1'] g>text[class='title']")
            val1 = []
            for i in range(len(val)):
                val1.append(val[i].text.strip("\n").replace(" ", ""))
            utillobj.as_List_equal(val1,val2,'Step 04: Verify the chart type icons are visible')
            
            driver.close()
            utillobj.switch_to_window(0)
          
        
        def wfinst():
        
            """
            Step 01: Run the attached 142140.fex from text editor in adhoc page. 
            
            """
            utillobj = utillity.UtillityMethods(self.driver)
            miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
            mainobj = wf_mainpage.Wf_Mainpage(self.driver)
            node = utillobj.parseinitfile('nodeid')
            port = utillobj.parseinitfile('httpport')
            context = utillobj.parseinitfile('wfcontext')
            setup_url = 'http://' + node + ':' + port + context + '/'
            self.driver.get(setup_url)
            utillobj.login_wf('mrid','mrpass')
            time.sleep(20)
            mainobj.select_repository_folder_item_menu('P116->S7074','142140','Edit With Text Editor')
            time.sleep(4)
            utillobj.switch_to_window(1)
            win=driver.window_handles
            mainobj.click_text_editor_ribbon_button('Run')
            utillobj.switch_to_window(2,custom_windows=win)
            time.sleep(2)
            
            """
            Step 02: Once report opened click on any field eg: Seats click dropdown and select Chart/Rollup Tool
            """
            miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 02.1: Verify page summary")
            column_list=['COUNTRY','CAR','MODEL','SEATS']
            miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 02.1: Verify all columns listed on the report')    
            time.sleep(2)    
            miscelanousobj.select_menu_items('ITableData0', 3, 'Chart/Rollup Tool')
            time.sleep(2)
            
            """
            Step 03: Now click on Chart button from Chart/Rollup Tool.
            """
            self.driver.find_element_by_css_selector('[id="ttpanel_1_1_0"]').click()
             
            """
            Step 04: Verify the chart type icons are visible.
            """
            time.sleep(3)        
            val2 = ['Bar', 'StackedBar', 'PercentBar', 'Column', 'StackedColumn', 'PercentColumn', 'ColumnDepth', 'StackedDepth', 'PercentDepth', '3DColumn', 'Pie', 'PiewithDepth', 'Donut(Cylinder)', 'DonutwithDepth', 'Donut', 'Line', 'Curved', 'Straight', 'Curved+Markers', 'Straight+Markers', 'Step', 'Area', 'StackedArea', 'PercentArea', '3DArea', 'Scatter(XYPlot)', 'Bubble', 'Funnel', 'Pyramid', 'Heatmap', 'Waterfall', 'Histogram', 'RadarLine', 'RadarArea', 'TagCloud']
            
            val = self.driver.find_elements_by_css_selector("[id*='chticon_1'] g>text[class='title']")
            val1 = []
            for i in range(len(val)):
                val1.append(val[i].text.strip("\n").replace(" ", ""))
            utillobj.as_List_equal(val1,val2,'Step 04: Verify the chart type icons are visible')
            
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