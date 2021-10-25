'''
Created on July 18, 2017

@author: Prabhakaran

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2204953
TestCase Name = Verify that series tab shows Column, Group By, Measures.

'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea,active_miscelaneous,active_chart_rollup,active_tools
from common.lib import utillity

class C2204953_TestClass(BaseTestCase):

    def test_C2204953(self):
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID="C2204953"
        driver = self.driver #Driver reference object created
        
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(driver)
        rollupobj =active_chart_rollup.Active_Chart_Rollup(driver)
        active_toolsobj = active_tools.Active_Tools(self.driver)
        
        """
        Step 01:Execute attached fex 'AR-CH-033.fex' in IA.
        """
        utillobj.active_run_fex_api_login('AR-CH-033.fex', "S7074", 'mrid', 'mrpass')
        parent_css="#MAINTABLE_wbody0 g.chartPanel g text"
        utillobj.synchronize_with_number_of_element(parent_css, 18, 65)
       
        utillobj.take_monitor_screenshot(Test_Case_ID+'_Actual_Step_01','actual',0,60,0,40)
        
        """
        Verify Chart
        """
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft','Unit Sales by Category, Product','Step 01 : Verify chart title')
        result_obj.verify_xaxis_title('MAINTABLE_wbody0','Category : Product', "Step 03.2 : Verify X-Axis Title")
        result_obj.verify_yaxis_title('MAINTABLE_wbody0','Unit Sales','Step 01.3 : Verify Y-Axis Title')
        expected_xval_list=['Coffee/Capuccino','Coffee/Espresso','Coffee/Latte','Food/Biscotti','Food/Croissant','Food/Scone','Gifts/Coffee Grinder','Gifts/Coffee Pot','Gifts/Mug','Gifts/Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 01.4 :')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0',1,10,'Step 01.5 : Verify number of chart risers')
        utillobj.verify_chart_color('MAINTABLE_wbody0','riser!s0!g4!mbar!','cerulean_blue','Step 01.6 : Verify chart riser color')
        miscelaneous_obj.verify_active_chart_tooltip('MAINTABLE_wbody0','riser!s0!g4!mbar!',['Unit Sales, Food/Croissant: 630,054'],'Step 01.7 : Verify chart tooltip value')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 01.8 : Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 01.09 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 01.10 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)                
        
        """
        Step 02 : Click Chart/Rollup Tool option from the dropdown menu   
        """
        rollupobj.select_chartmenubar_option('MAINTABLE_wmenu0', 0, 'Chart/Rollup Tool', 0, custom_css='cpop')
        parent_css="#wtop1 #wtitle1"
        utillobj.synchronize_with_visble_text(parent_css, 'Chart/Rollup Tool', 45)
        
        """
        Verify that Chart/Rollup Tool pop up opened. Verify that two tabs are displayed: Series and Charts
        """
        miscelaneous_obj.verify_popup_appears('wall1','Chart/Rollup Tool','Step 02.1 : Verify that Chart/Rollup Tool pop up opened')
        actual_tabs=[tab.text.strip() for tab in self.driver.find_elements_by_css_selector("#wall1 .arToolColumnBorder [id^='ttpanel']")]
        utillobj.asequal(actual_tabs,['Series','Charts'],'Step 02.2 : Verify that two tabs are displayed: Series and Charts')
        
        """
        Step 03 : By Default user is on Series tab; Verify that Series tab shows Columns, Group By and Measures sub-sections.
        """
        active_toolsobj.chart_rollup_tool_verify_columns('charttoolt1', 'tpanel_0_1_0', 1,['Columns', 'Category', 'Product', 'Unit Sales'], 'Step 02.3: Verify that Series tab shows Columns sub-sections')
        active_toolsobj.chart_rollup_tool_verify_columns('charttoolt1', 'tpanel_0_1_0', 2,['Group By', 'Category' ,'Product'], 'Step 02.4: Verify that Series tab shows Group By sub-sections')
        active_toolsobj.chart_rollup_tool_verify_columns('charttoolt1', 'tpanel_0_1_0', 3,['Measure', 'Sum:', 'Unit Sales'], 'Step 02.5: Verify that Series tab shows Measures sub-sections')
        ele=driver.find_element_by_css_selector("#wall1")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_Step_03', image_type='actual',x=1, y=1, w=-1, h=-1)
        
if __name__ == '__main__':
    unittest.main()
        
        