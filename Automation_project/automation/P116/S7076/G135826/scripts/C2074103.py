'''
Created on Aug 26, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7076&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2074103

'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_chart_rollup, visualization_resultarea, active_tools
from common.lib import utillity,core_utility

class C2074103_TestClass(BaseTestCase):

    def test_C2074103(self):
        
        """
            TESTCASE OBJECTS
        """
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        rollobj=active_chart_rollup.Active_Chart_Rollup(self.driver)
        resobj= visualization_resultarea.Visualization_Resultarea(self.driver)
        toolobj= active_tools.Active_Tools(self.driver)
        
        """
        Step 01: Execute the attached repro - act-246
        """
        utillobj.active_run_fex_api_login('act-246.fex','S7076','mrid','mrpass') 
        active_misobj.verify_page_summary('0','10of10records,Page1of1', 'Step 01.01: Verify Page summary 10of10')
        column=['Category','Product ID','Unit Sales','Dollar Sales']
        active_misobj.verify_column_heading('ITableData0', column, "Step 01.02: Verify Column heading of act-246.fex")
        utillobj.verify_data_set('ITableData0','I0r','act-246.xlsx',"Step 01.03: Verify act-246.fex dataset")        
        
        """
        Step 02: From the drop down control for Unit Sales, select the Chart/Rollup Tool.
        """
        time.sleep(5)
        active_misobj.select_menu_items('ITableData0', 2, 'Chart/Rollup Tool')
        """Expect to see the following Chart/Rollup Menu."""
        toolobj.chart_rollup_tool_verify_columns('charttoolt1','tpanel_0_1_0', 2,['Group By','Drag Column Here'], 'Step 02.01:Verify Chart/Rollup Tool is added')
        
        """
        Step 03: Drag Unit Sales and Dollar Sales to the Measure area.
        Drag Category to the Group By area.
        """
        toolobj.chart_rollup_tool_drag_drop_items('charttoolt1', 'Columns', 'Category', 1, 'Group By', 0)
        toolobj.chart_rollup_tool_drag_drop_items('charttoolt1', 'Columns', 'Unit Sales', 1, 'Measure', 0)
        toolobj.chart_rollup_tool_drag_drop_items('charttoolt1', 'Columns', 'Dollar Sales', 1, 'Measure', 1)
        """Expect to see the Chart/Rollup menu with the following values."""
        toolobj.chart_rollup_tool_verify_columns('charttoolt1','tpanel_0_1_0', 2,['Group By', 'Category'], 'Step 03.01: Verify Category in Group By')
        
        """
        Step 04: Click the Charts button in the Chart/Rollup Menu.
        Scroll down until the 5 PIE options are displayed.
        Expect to see the following PIE Chart display options.
        """
        time.sleep(5)   
        self.verify_advance_chart('wall1', 'piebevel',True,"Step 04.01: Verify Chart piebevel is displayed")  
        self.verify_advance_chart('wall1', 'piewithdepth',True,"Step 04.02: Verify Chart piewithdepth is displayed") 
        self.verify_advance_chart('wall1', 'dountcylinder',True,"Step 04.03: Verify Chart dountcylinder is displayed")
        self.verify_advance_chart('wall1', 'dountwithDepth',True,"Step 04.04: Verify Chart dountwithDepth is displayed")
        self.verify_advance_chart('wall1', 'donutbevel',True,"Step 04.05: Verify Chart donutbevel is displayed")
        
        """
        Step 05:Click the first PIE option, then click OK.
        Expect to see two PIEs that appear as below.
        """
        time.sleep(5)
        rollobj.select_advance_chart('wall1', 'piebevel')
        utillobj.wait_for_page_loads(20)
        time.sleep(5)
        utillobj.verify_chart_color('wall2',"riser!s0!g0!mwedge!",'cerulean_blue',"Step 05.01:Verify Fill Color")
        utillobj.verify_chart_color('wall2',"riser!s0!g1!mwedge!",'cerulean_blue',"Step 05.02:Verify Fill Color")
        resobj.verify_riser_pie_labels_and_legends('wall2', ['Unit Sales','Dollar Sales'],"Step 05.03: Verify Chart piebevel Label & Legend")     
        resobj.verify_riser_legends('wall2', ['Coffee','Food','Gifts'], "Step 05.04: Verify Chart piebevel Legends")     
        active_misobj.verify_popup_title('wall2', 'Unit Sales, Dollar Sales by Category', 'Step 05.05: Verify the dialog title')
        rollobj.verify_arChartMenu('wall2',"Step 05.06: Verify the chart Menu")
         
        """
        Step 06:Click the first icon for Chart/Rollup Tool in the PIE output.
        Move the PIE display so the Chart/Rollup Menu is again visible. 
        Click the Charts button, scroll down to the PIE options again, then click the second PIE and click OK.
        Expect to see two PIEs that appear as below.
        """
        time.sleep(5)
        rollobj.create_new_item(0, 'Chart/Rollup Tool',False,'wall2')
        time.sleep(5)
        active_misobj.move_active_popup("2", "600", "10")
        time.sleep(10) #need this time sleep as it avoid automation error
        rollobj.select_advance_chart('wall1', 'piewithdepth')
        utillobj.wait_for_page_loads(20)
        time.sleep(5)
        utillobj.verify_chart_color('wall2',"riser!s1!g0!mwedge!",'gold_tips',"Step 06.01:Verify Fill Color")        
        utillobj.verify_chart_color('wall2',"riser!s0!g1!mwedge!",'cerulean_blue',"Step 06.02:Verify Fill Color")        
        resobj.verify_riser_pie_labels_and_legends('wall2', ['Unit Sales','Dollar Sales'],"Step 06.03: Verify Chart piebevel Label & Legend")
        resobj.verify_riser_legends('wall2', ['Coffee','Food','Gifts'], "Step 06.04: Verify Chart piebevel Legends")        
        active_misobj.verify_popup_title('wall2', 'Unit Sales, Dollar Sales by Category', 'Step 06.05: Verify the dialog title')
         
        """
        Step 07:Click the first icon for Chart/Rollup Tool in the PIE output.
        Move the PIE display so the Chart/Rollup Menu is again visible. 
        Click the Charts button, scroll down to the PIE options again, then click the third PIE and click OK.
        """
        time.sleep(5)
        rollobj.create_new_item(1, 'Chart/Rollup Tool',False,'wall2')
        time.sleep(10)
        rollobj.select_advance_chart('wall1', 'dountcylinder')
        utillobj.wait_for_page_loads(20)
        time.sleep(5)
        utillobj.verify_chart_color('wall2',"riser!s0!g1!mwedge!",'cerulean_blue',"Step 07.01:Verify Fill Color")        
        resobj.verify_riser_pie_labels_and_legends('wall2', ['Unit Sales','Dollar Sales'],"Step 07.02: Verify Chart dountcylinder Label & Legend")
        resobj.verify_riser_legends('wall2', ['Coffee','Food','Gifts'], "Step 07.03: Verify Chart dountcylinder Legends")
        active_misobj.verify_popup_title('wall2', 'Unit Sales, Dollar Sales by Category', 'Step 07.04: Verify the dialog title')
        
        """
        Step 08:Click the first icon for Chart/Rollup Tool in the PIE output.
        Move the PIE display so the Chart/Rollup Menu is again visible. 
        Click the Charts button, scroll down to the PIE options again, then click the fourth PIE and click OK.
        """
        time.sleep(5)
        rollobj.create_new_item(1, 'Chart/Rollup Tool',False,'wall2')
        time.sleep(10)
        rollobj.select_advance_chart('wall1', 'dountwithDepth')
        utillobj.wait_for_page_loads(20)
        time.sleep(5)
        utillobj.verify_chart_color('wall2',"riser!s1!g0!mwedge!",'gold_tips',"Step 08.01:Verify Fill Color") 
        utillobj.verify_chart_color('wall2',"riser!s0!g1!mwedge!",'cerulean_blue',"Step 08.02:Verify Fill Color")
        resobj.verify_riser_pie_labels_and_legends('wall2', ['Unit Sales','Dollar Sales'],"Step 08.03: Verify Chart dountwithDepth Label & Legend")
        resobj.verify_riser_legends('wall2', ['Coffee','Food','Gifts'], "Step 08.04: Verify Chart dountwithDepth Legends")
        active_misobj.verify_popup_title('wall2', 'Unit Sales, Dollar Sales by Category', 'Step 08.05: Verify the dialog title')
        
        """
        Step 09:Click the first icon for Chart/Rollup Tool in the PIE output.
        Move the PIE display so the Chart/Rollup Menu is again visible. 
        Click the Charts button, scroll down to the PIE options again, then click the fifth PIE and click OK.
        """
        time.sleep(5)
        rollobj.create_new_item(1, 'Chart/Rollup Tool',False,'wall2')
        time.sleep(15) #this is required to avoid element intercept error
        rollobj.select_advance_chart('wall1', 'donutbevel')
        utillobj.wait_for_page_loads(20)
        time.sleep(5)
        utillobj.verify_chart_color('wall2',"riser!s0!g1!mwedge!",'cerulean_blue',"Step 09.01:Verify Fill Color")       
        resobj.verify_riser_pie_labels_and_legends('wall2', ['Unit Sales','Dollar Sales'],"Step 09.02: Verify Chart donutbevel Label & Legend")
        resobj.verify_riser_legends('wall2', ['Coffee','Food','Gifts'], "Step 09.03: Verify Chart donutbevel Legends")        
        active_misobj.verify_popup_title('wall2', 'Unit Sales, Dollar Sales by Category', 'Step 09.04: Verify the dialog title')
        
    def verify_advance_chart(self,popup_id, chart_name,verify,msg):
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

        time.sleep(1)
        ele = self.driver.find_element_by_css_selector("#" + popup_id + " #ttpanel_1_"+index+"_0")
        core_utility.CoreUtillityMethods.python_left_click(self, ele)
        time.sleep(1)
        display=len(self.driver.find_elements_by_id(chart_ids[chart_name]))
        utillity.UtillityMethods.asequal(self,1,display,msg)        
        time.sleep(1)
        
if __name__ == '__main__':
    unittest.main()