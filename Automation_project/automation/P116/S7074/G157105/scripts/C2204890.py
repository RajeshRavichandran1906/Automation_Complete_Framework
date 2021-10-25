'''
Created on JUL 18, 2017

@author: Pavithra @fixed by : Bhagavathi

Attached testrail fex name has to be changed in testrail.

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2204890
TestCase Name = Verify that Restore Chart type icon is available in chart window toolbar (128394)
'''
import unittest, time
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea,active_miscelaneous,ia_resultarea,active_chart_rollup

class C2204890_TestClass(BaseTestCase):

    def test_C2204890(self):
        
        """
            TESTCASE OBJECTS
        """        
        utillobj = utillity.UtillityMethods(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        rollupobj=active_chart_rollup.Active_Chart_Rollup(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
            Step 01:Execute attached fex "Chart_AHTML.fex" in IA. ( Modified fex name as Chart_AHTML.fex)
        """
        utillobj.active_run_fex_api_login("Chart_AHTML_1.fex", "S7074", 'mrid', 'mrpass')
        parent_css="div [id='MAINTABLE_wmenu0']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 65)
        
        """
            Step 02:see attached fex "Chart_AHTML.fex" in IA. ( Modified fex name as Chart_AHTML.fex)
        """
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 02.1 Verify -yAxis Title")
        resobj.verify_xaxis_title("MAINTABLE_wbody0_f", "Category : Product", "Step 02.2 Verify -xAxis Title")
        expected_xval_list=['Coffee/Capuccino', 'Coffee/Espresso', 'Coffee/Latte', 'Food/Biscotti', 'Food/Croissant', 'Food/Scone', 'Gifts/Coffee Grinder', 'Gifts/Coffee Pot', 'Gifts/Mug', 'Gifts/Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0_f", expected_xval_list, expected_yval_list, "Step 02.3:Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0_f", 1, 10, 'Step 02.4: Verify the total number of risers displayed on preview')
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody0_f", "riser!s0!g0!mbar!", "bar_blue", "Step 02.5: Verify  bar color")
        expected_tooltip_list=['Category:  Coffee', 'Product:  Latte', 'Unit Sales:  878063', 'Filter Chart', 'Exclude from Chart']
        miscelaneous_obj.verify_active_chart_tooltip('MAINTABLE_wbody0', 'riser!s0!g2!mbar!', expected_tooltip_list, "Step 02.6: verify tooltip values")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales by Category, Product', 'Step 02.7: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart', 'Original Chart'],"Step 02.8: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02.9: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02.10: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
       
        """
            Step 02:Click on Chart/Rollup icon
        """ 
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        time.sleep(4)
        """ 
            Step 03:From the 'Chart' tab, select 'Donut (Bevel)' and click ok
        """
        
        rollupobj.select_advance_chart('wall1', 'donutbevel')
        time.sleep(1)
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['Unit Sales','Unit Sales','Unit Sales'], "Step 04.1 :",same_group=True,expected_total_label_list=['1.4M','1.4M','928K'])
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['1.4M','1.4M','928K'], "Step 04.2 :",custom_css=" text[class^='totalLabel']",same_group=True)
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['Coffee','Food','Gifts'], "Step 04.3 : ",custom_css=" text[class^='colLabel']",same_group=True)
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['Category : Product'], "Step 04.4 :",custom_css=" text[class^='colHeader-label!']",same_group=True)
        expected_legend_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        resobj.verify_riser_legends('MAINTABLE_wbody0 ', expected_legend_list,'Step 04.5 : Verify chart legends')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mwedge!", "bar_blue", "Step 04.6 : Verify first bar color")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales by Category, Product', 'Step 04.7 : Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart', 'Original Chart'],"Step 04.8 : Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.9 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.10  : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 30, "Step 04.11 : Verify number of pie", custom_css=".chartPanel g path[class*='riser!s']")    
        
        """
            Step 04:Click on 'Original chart' icon in chart window toolbar
        """
#         rollupobj.select_chartmenubar_option('MAINTABLE_wmenu0',1,'Original Chart',0,custom_css='cpop')
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 2)
        time.sleep(2)
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 05.1 Verify -yAxis Title")
        resobj.verify_xaxis_title("MAINTABLE_wbody0_f", "Category : Product", "Step 05.2 Verify -xAxis Title")
        expected_xval_list=['Coffee/Capuccino', 'Coffee/Espresso', 'Coffee/Latte', 'Food/Biscotti', 'Food/Croissant', 'Food/Scone', 'Gifts/Coffee Grinder', 'Gifts/Coffee Pot', 'Gifts/Mug', 'Gifts/Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0_f", expected_xval_list, expected_yval_list, "Step 05.3:Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0_f", 1, 10, 'Step 05.4: Verify the total number of risers displayed on preview')
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody0_f", "riser!s0!g0!mbar!", "bar_blue", "Step 05.5: Verify  bar color")
        
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales by Category, Product', 'Step 05.7: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart', 'Original Chart'],"Step 05.8: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.9: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.10: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
      
if __name__ == '__main__':
    unittest.main()          