'''
Created on Aug 23, 2016

@author: Gobizen

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053779
TestCase Name = Verify TOP option displays the top values
'''
import unittest, time
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.wftools.active_chart import Active_Chart
from common.pages import active_miscelaneous,active_chart_rollup, visualization_resultarea

class C2053779_TestClass(BaseTestCase):

    def test_C2053779(self):
        
        """
            Class Objects
        """
        act_obj = Active_Chart(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        rollupobj = active_chart_rollup.Active_Chart_Rollup(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        
        """
            Step 01: Execute the AR-RP-001.fex
        """
        utillobj.active_run_fex_api_login('AR-RP-001.fex','S7074','mrid','mrpass')      
        time.sleep(8)      
        active_misobj.verify_page_summary('0','107of107records,Page1of2', 'Step 01.01: Verify Page summary')
        
        """Step 02: Select State > Chart > Pie > Product"""
        
        active_misobj.select_menu_items('ITableData0', 3, 'Chart','Pie','Product')
        time.sleep(5)
        
        #Verify that 'State By Product' pop up window for the chart is displayed.
        
        active_misobj.verify_popup_title('wall1', 'State by Product', 'Step 02.01: Verify that State By Product pop up window for the chart is displayed')
        
        
        
        """Step 03: Click New icon (dropdown) > Top (hover over Top option)"""
        """Step 04: Click on Top 3 option"""
        
        #Verify that following options are displayed: - Top 3 - Top 5 - Top 10 - Clear Top
        
        
        rollupobj.create_new_item(0,'Top->Top 3', verify=True, expected_list=['Top 3', 'Top 5', 'Top 10', 'Clear Top'], msg='Step 03.01: Verify that following options are displayed: - Top 3 - Top 5 - Top 10 - Clear Top')
        time.sleep(6)
        #Verify that top 3 products with highest state are displayed. 
        
        #Pie Legend
        resobj.verify_riser_legends('wall1',['Biscotti', 'Coffee Grinder', 'Coffee Pot', 'Other'], "Step 04.01: Verify Chart piebevel Legends for Top 5")
        #title
        active_misobj.verify_popup_title('wall1', 'State by Product', 'Step 04.02: Verify that State By Product pop up window for the chart is displayed for top 5')
 
        #Tooltip & Color
        active_misobj.verify_active_chart_tooltip('wall1',"riser!s0!g0!mwedge", ['Biscotti','State: 11','10.3% of 107'],"Step 04.03: Verify Chart piebevel tooltip for Unit Sales")
        time.sleep(5)
        
        utillobj.verify_chart_color('wall1', 'riser!s0!g0!mwedge','cerulean_blue',"Step 04.04: Verify Chart piebevel Color ")
        
        
        
        """Step 05: Likewises, Top 5, Top 10 shows results as per selection.
        Verify correct output displayed for Top 5 and Top 10 options."""
        
        #Top 5 
#         rollupobj.create_new_item(1,'Top->Top 5')
        act_obj.create_new_item('wall1', 'Top->Top 5')
#         act_obj.create_new_item('wall1', 'Top 5')
        time.sleep(7)
        #Pie Label
        resobj.verify_riser_pie_labels_and_legends('wall1', ['State'],"Step 05.01: Verify Chart pie Label & Legend")
        #Pie Legend
        resobj.verify_riser_legends('wall1', ['Biscotti', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Other'], "Step 05.02: Verify Chart piebevel Legends for Top 5")
        #title
        active_misobj.verify_popup_title('wall1', 'State by Product', 'Step 05.03: Verify that State By Product pop up window for the chart is displayed for top 5')
        time.sleep(5)
        #Tooltip & Color
        active_misobj.verify_active_chart_tooltip('wall1',"riser!s0!g0!mwedge", ['Biscotti','State: 11','10.3% of 107'],"Step 05.04: Verify Chart piebevel tooltip for Unit Sales")
        
        utillobj.verify_chart_color('wall1', 'riser!s0!g0!mwedge','cerulean_blue',"Step 05.05: Verify Chart piebevel Color ")
        
        time.sleep(5)
        

        #Top 10 
        act_obj.create_new_item('wall1', 'Top->Top 10')
#         rollupobj.create_new_item(1,'Top->Top 10')
        time.sleep(6)
        #Pie Label
        resobj.verify_riser_pie_labels_and_legends('wall1', ['State'],"Step 05.06: Verify Chart pie Label & Legend")
        #Pie Legend
        resobj.verify_riser_legends('wall1', ['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos'], "Step 05.07: Verify Chart piebevel Legends for Top 5")
               
        #title
        active_misobj.verify_popup_title('wall1', 'State by Product', 'Step 05.08: Verify that State By Product pop up window for the chart is displayed for top 10')
        #Tooltip & Color
        active_misobj.verify_active_chart_tooltip('wall1',"riser!s0!g0!mwedge", ['Biscotti','State: 11','10.3% of 107'], "Step 05.09: Verify Chart piebevel tooltip for Unit Sales")
        utillobj.verify_chart_color('wall1', 'riser!s0!g0!mwedge','cerulean_blue',"Step 05.10: Verify Chart piebevel Color ")
        time.sleep(5)
        
        
        """Step 06: Click Clear Top option
        Verify Clear Top option wipes out previously selected option and shows original chart.""" 
        act_obj.create_new_item('wall1', 'Top->Clear Top')
        time.sleep(6)
        #Pie Legend
        resobj.verify_riser_legends('wall1', ['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos'], "Step 06.01: Verify original hart")
       
if __name__ == '__main__':
    unittest.main()