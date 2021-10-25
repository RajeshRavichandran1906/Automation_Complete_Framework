'''
Created on Sep 6, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053793

'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection,active_chart_rollup, visualization_resultarea
from common.lib import utillity

class C2053793_TestClass(BaseTestCase):

    def test_C2053793(self):
        """
            TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_filter = active_filter_selection.Active_Filter_Selection(self.driver)
        rollobj=active_chart_rollup.Active_Chart_Rollup(self.driver)
        resobj= visualization_resultarea.Visualization_Resultarea(self.driver)
        
        """
        Step 01: Execute the AR-RP-001.fex
        """
        utillobj.active_run_fex_api_login('AR-RP-001A.fex','S7074','mrid','mrpass')
        utillobj.synchronize_with_visble_text("#ITableData0 tr:nth-child(2) td:nth-child(2)", "C141", 65)
        active_misobj.verify_page_summary('0','107of107records,Page1of2', 'Step 01.1: Verify Page summary 107of107')
        
        """
        Step 02: Select State > Chart > Pie > Category
        Verify that 'State By Category' pop up window for the Bar chart is displayed. 
        Verify that chart toolbar is present with all the options.
        """
        active_misobj.select_menu_items('ITableData0', 3, 'Chart','Pie','Category')
        utillobj.synchronize_with_number_of_element("#wall1", 1, 10)
        #screenshot
        utillobj
        element = self.driver.find_element_by_css_selector("#wall1")
        utillobj.take_screenshot(element, 'C2053793_Actual_Step02', image_type='actual_images')
        #Tooltip & Color
        time.sleep(5)
        utillobj.verify_chart_color('wall1', 'riser!s0!g0!mwedge','cerulean_blue',"Step 02.1a: Verify Chart piebevel Color ")
        
        #Pie Label
        resobj.verify_riser_pie_labels_and_legends('wall1', ['State'],"Step 02.1b: Verify Chart Label")
        #Pie Legend
        resobj.verify_riser_legends('wall1', ['Coffee','Food','Gifts'], "Step 02.1c: Verify Chart Legends")
        #Title
        active_misobj.verify_popup_title('wall1', 'State by Category', 'Step 02.1d: Verify the dialog title')
        #Menu
        rollobj.verify_arChartMenu('wall1',"Step 02.1e: Verify the chart Menu")
        
        """
        Step 03: Click Freeze icon on chart
        Verify the lock on chart tool menu bar.
        """
        unlock = "//div[@id='LINKIMG1_-1']//img[contains(@src,'i3AAAAAElFTkSuQmCC')]"
        lock = "//div[@id='LINKIMG1_-1']//img[contains(@src,'TfAAAAAElFTkSuQmCC')]"
        rollobj.click_chart_menu_bar_items('wall1', 8)
        utillobj.asequal(len(self.driver.find_elements_by_xpath(lock)),1,"Step 03.1: Verify freeze icon is locked")
        
        """
        Step 04: Now go back to report and filter for Category EQ Food & Gifts.
        Verify that report has been filtered for Food & Gifts, 
        Coffee should not be present.
        Also verify that the PIE chart still shows 3 slices for 3 Categories.
        """
        active_misobj.move_active_popup("1", "500", "200")
        active_misobj.select_menu_items('ITableData0', 0, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',popup_id='wall2', value1='Food',value2='Gifts')
        active_filter.verify_filter_selection_dialog(True,'Step 04.1: Verify filter row.','Category',popup_id='wall2')
        active_filter.filter_button_click('Filter',popup_id="wall2")
        active_misobj.verify_page_summary('0','77of107records,Page1of2', 'Step 04.2: Verify Page summary 77of107')
        column=['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        active_misobj.verify_column_heading('ITableData0', column,'Step 04.3: Verify column heading')
        utillobj.create_data_set('ITableData0','I0r','C2053793_Ds01.xlsx')
        utillobj.verify_data_set('ITableData0','I0r','C2053793_Ds01.xlsx','Step 04.4: Verify Dataset after Filter Category = Food and Gifts')
        
        #screenshot
        active_misobj.move_active_popup("2", "-500", "-200")
        time.sleep(5)
        element = self.driver.find_element_by_css_selector("#wall1")
        utillobj.take_screenshot(element, 'C2053793_Actual_Step04', image_type='actual_images')
        #Tooltip & Color
        utillobj.verify_chart_color('wall1', 'riser!s0!g0!mwedge','cerulean_blue',"Step 04.5a: Verify Chart piebevel Color ")        
        
        #Pie Label
        resobj.verify_riser_pie_labels_and_legends('wall1', ['State'],"Step 04.5b: Verify Chart Label")
        #Pie Legend
        resobj.verify_riser_legends('wall1', ['Coffee','Food','Gifts'], "Step 04.5c: Verify Chart Legends")
        
        """
        Step 05: Click the LOCK icon again to release it.
        Expect to see the PIE chart now filtered as the Report, with no Coffee slice.
        """   
        rollobj.click_chart_menu_bar_items('wall1', 8)  
        utillobj.asequal(len(self.driver.find_elements_by_xpath(unlock)),1,"Step 05.1: Verify freeze icon is unlocked") 
        
        #screenshot
        time.sleep(5)
        element = self.driver.find_element_by_css_selector("#wall1")
        utillobj.take_screenshot(element, 'C2053793_Actual_Step05', image_type='actual_images')
        #Tooltip & Color
        utillobj.verify_chart_color('wall1', 'riser!s0!g0!mwedge','cerulean_blue',"Step 05.2a: Verify Chart piebevel Color ")
        
        #Pie Label
        resobj.verify_riser_pie_labels_and_legends('wall1', ['State'],"Step 05.2b: Verify Chart Label")
        #Pie Legend
        resobj.verify_riser_legends('wall1', ['Food','Gifts'], "Step 05.3c: Verify Chart Legends")
        
        """
        Step 06: Clear the Filter Menu.
        Expect to see the report and PIE chart return to display all three Categories, Coffee, Food & Gifts.
        """
        active_filter.close_filter_dialog(popup_id='wall2')
        
        #screenshot
        time.sleep(8)
        element = self.driver.find_element_by_css_selector("#wall1")
        utillobj.take_screenshot(element, 'C2053793_Actual_Step06', image_type='actual_images')
        #Tooltip & Color
        time.sleep(5)
        active_misobj.verify_active_chart_tooltip('wall1',"riser!s0!g0!mwedge", ['Coffee','State: 30','28.0% of 107'],"Step 06.1a: Verify Chart tooltip and color")
        utillobj.verify_chart_color('wall1', 'riser!s0!g0!mwedge','cerulean_blue',"Step 06.1a: Verify Chart piebevel Color ")
        
        #Pie Label
        resobj.verify_riser_pie_labels_and_legends('wall1', ['State'],"Step 06.1b: Verify Chart Label")
        #Pie Legend
        resobj.verify_riser_legends('wall1', ['Coffee','Food','Gifts'], "Step 06.1c: Verify Chart Legends")
        #Title
        active_misobj.verify_popup_title('wall1', 'State by Category', 'Step 06.1d: Verify the dialog title')
        
        """
        Step 07: Back in the report Filter again for Food & Gifts.
        Expect to see the report and PIE chart both filtered to eliminate the Coffee data. This is because the Lock has been disabled.
        """
        active_misobj.select_menu_items('ITableData0', 0, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',popup_id='wall2', value1='Food',value2='Gifts')
        active_filter.verify_filter_selection_dialog(True,'Step 07.1: Verify filter row.','Category',popup_id='wall2')
        active_filter.filter_button_click('Filter',popup_id="wall2")
        active_misobj.verify_page_summary('0','77of107records,Page1of2', 'Step 07.2: Verify Page summary 77of107')
        column=['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        active_misobj.verify_column_heading('ITableData0', column,'Step 07.3: Verify column heading')
        utillobj.verify_data_set('ITableData0','I0r','C2053793_Ds01.xlsx','Step 07.4: Verify Dataset after Filter Category = Food and Gifts')
        
        #screenshot
        
        element = self.driver.find_element_by_css_selector("#wall1")
        utillobj.take_screenshot(element, 'C2053793_Actual_Step07', image_type='actual_images')
        #Tooltip & Color
        active_misobj.verify_active_chart_tooltip('wall1',"riser!s0!g0!mwedge", ['Food','State: 33','42.9% of 77'],"Step 07.5a: Verify Chart tooltip")
        utillobj.verify_chart_color('wall1', 'riser!s0!g0!mwedge','cerulean_blue',"Step 07.5a: Verify Chart piebevel Color ")
        
        #Pie Label
        resobj.verify_riser_pie_labels_and_legends('wall1', ['State'],"Step 07.5b: Verify Chart Label")
        #Pie Legend
        resobj.verify_riser_legends('wall1', ['Food','Gifts'], "Step 07.5c: Verify Chart Legends")
        
         
        
        
if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
