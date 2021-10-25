'''
Created on Sep 7, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053791

'''
import unittest,re
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, \
    active_chart_rollup, visualization_resultarea,\
    active_tools
from common.lib import utillity, core_utility

class C2053791_TestClass(BaseTestCase):

    def test_C2053791(self):
        
        """
            Class Objects
        """
        toolobj= active_tools.Active_Tools(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        core_utils = core_utility.CoreUtillityMethods(self.driver)
        rollobj=active_chart_rollup.Active_Chart_Rollup(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        resobj= visualization_resultarea.Visualization_Resultarea(self.driver)
        
        """
        Step 01: Execute the AR-RP-001A.fex
        """
        utillobj.active_run_fex_api_login('AR-RP-001A.fex','S7074','mrid','mrpass') 
        active_misobj.verify_page_summary('0','107of107records,Page1of2', 'Step 01.01: Verify Page summary 107of107')
        
        """
        Step 02: Select State > Chart > Pie > Category
        Verify that 'State By Category' pop up window for the Bar chart is displayed. 
        Verify that chart toolbar is present with all the options.
        """
        time.sleep(8)
        active_misobj.select_menu_items('ITableData0', 3, 'Chart','Pie','Category')        
        time.sleep(8)
        #Tooltip & Color
        time.sleep(5)
        active_misobj.verify_active_chart_tooltip('wall1',"riser!s0!g0!mwedge", ['Coffee','State: 30','28.0% of 107'],"Step 02.01: Verify Chart tooltip and color")
        utillobj.verify_chart_color('wall1', 'riser!s0!g0!mwedge','cerulean_blue',"Step 02.02: Verify Chart piebevel Color ")
        time.sleep(5)
        #Pie Label
        resobj.verify_riser_pie_labels_and_legends('wall1', ['State'],"Step 02.03: Verify Chart Label")
        #Pie Legend
        resobj.verify_riser_legends('wall1', ['Coffee','Food','Gifts'], "Step 02.04: Verify Chart Legends")
        #Title
        active_misobj.verify_popup_title('wall1', 'State by Category', 'Step 02.05: Verify the dialog title')
        #Menu
        rollobj.verify_arChartMenu('wall1',"Step 02.06: Verify the chart Menu")
        
        """
        Step 03: Click Advanced Chart icon from the toolbar
        Verify that Chart/Rollup tool is opened and it shows 2 tabs: Series and Charts.See attached screenshot..
        """
        rollobj.click_chart_menu_bar_items('wall1', 6)
        tabs="#charttoolt2 .arToolColumnBorder tr"
        actual_tab=[el.strip() for el in self.driver.find_element_by_css_selector(tabs).text.split("\n") if bool(re.match('\S', el))]
        utillobj.asequal(['Series','Charts'],actual_tab,"Step 03.01: Verify Chart/Rollup Tool 2 tabs")
        
        toolobj.chart_rollup_tool_verify_columns('charttoolt2','tpanel_0_2_0', 1,['Columns','Category','Product ID','Product','State', 'Unit Sales','Dollar Sales'],"Step 03.02: Verify Chart/Rollup Columns")
        toolobj.chart_rollup_tool_verify_columns('charttoolt2','tpanel_0_2_0', 2,['Group By', 'Category'],"Step 03.03: Verify Chart/Rollup Group By")
        toolobj.chart_rollup_tool_verify_columns('charttoolt2','tpanel_0_2_0', 3,['Measure', 'Count:', 'State'],"Step 03.04: Verify Chart/Rollup Measure")
        
        """
        Step 04: Click on Charts tab
        Verify multiple chart types are displayed. Like: Bar, Stacked Bar, Percent Bar etc.
        """
        chart_tab = self.driver.find_element_by_css_selector("#charttoolt2 #ttpanel_1_2_0")
        core_utils.python_left_click(chart_tab)
        time.sleep(5)   
        self.verify_advance_chart('wall2', 'bar',"Step 04.01: Verify Bar chart is displayed")  
        self.verify_advance_chart('wall2', 'stackedbar',"Step 04.02: Verify Stacked barchart is displayed") 
        self.verify_advance_chart('wall2', 'percentbar',"Step 04.03: Verify percent bar is displayed")
        
        """
        Step 05: On Series tab we have 'Category' column under Group By and 'State' column under Measure. 
        Now select 'Donut' chart type under Chart tab and click OK
        Verify that 'State by Category' chart shows Donut shape chart. See attached screenshot.
        """
        rollobj.select_advance_chart('wall2', 'dountcylinder')
        time.sleep(8)
        import pyautogui
        pyautogui.hotkey('pageup')
        time.sleep(2)

        #Tooltip & Color
        time.sleep(5)
        active_misobj.verify_active_chart_tooltip('wall1',"riser!s0!g0!mwedge", ['Coffee','State: 30','28.0% of 107'],"Step 05.01: Verify Chart tooltip and color")
        utillobj.verify_chart_color('wall1', 'riser!s0!g0!mwedge','cerulean_blue',"Step 05.02: Verify Chart piebevel Color ")
        time.sleep(5)
        #Pie Label
#         resobj.verify_riser_pie_labels_and_legends('wall1', ['State'],"Step 05.1b: Verify Chart Label",expected_total_label_list=['107'])
        resobj.verify_riser_pie_labels_and_legends('wall1', ['State'],"Step 05.03: Verify Chart Label")
        #Pie Legend
        resobj.verify_riser_legends('wall1', ['Coffee','Food','Gifts'], "Step 05.04: Verify Chart Legends")
        #Title
        active_misobj.verify_popup_title('wall1', 'State by Category', 'Step 05.05: Verify the dialog title')
        #Menu
        rollobj.verify_arChartMenu('wall1',"Step 05.06: Verify the chart Menu")
        
        
    def verify_advance_chart(self,popup_id, chart_name,msg):
        """
        Usage: select_advance_chart('wall1', 'bar')
        """
        index=list(popup_id)[-1]
        chart_ids={'bar':'chticon_'+index+'_0_bar1',
                        'stackedbar':'chticon_'+index+'_0_bar2',
                        'percentbar':'chticon_'+index+'_0_bar3',
                        'column':'chticon'+index+'_0_column',
                        'stackedcolumn':'chticon_'+index+'_0_column2',
                        'percentcolumn':'chticon_'+index+'_0_column3',
                        'columndepth':'chticon_'+index+'_0_column4',
                        'stackeddepth':'chticon_'+index+'_0_column5',
                        'percentdepth':'chticon_'+index+'_0_column6',
                        '3Dcolumn':'chticon_'+index+'_0_bar3d',
                        'piebevel':'chticon_'+index+'_0_pie',
                        'piewithdepth':'chticon_'+index+'_0_pie2',
                        'dountcylinder':'chticon_'+index+'_0_donut',
                        'dountwithDepth':'chticon_'+index+'_0_donut2',
                        'donutbevel':'chticon_'+index+'_0_donut3'}
        element = self.driver.find_element_by_css_selector("#" + popup_id + " #ttpanel_1_"+index+"_0")
        core_utility.CoreUtillityMethods.python_left_click(self,element)
        time.sleep(1)
        display=self.driver.find_element_by_id(chart_ids[chart_name]).is_displayed()
        utillity.UtillityMethods.asequal(self,True,display,msg)
        time.sleep(1)
        
if __name__ == '__main__':
    unittest.main()   