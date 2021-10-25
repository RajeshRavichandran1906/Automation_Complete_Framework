'''
Created on Jun 7, 2018

@author: BM13368
TestCase ID : http://172.19.2.180/testrail/index.php?/cases/view/2204957&group_by=cases:section_id&group_id=157106&group_order=asc
TestCase Name : Verify that chart based on the Area is displayed correctly
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea, ia_resultarea, active_chart_rollup
from common.lib import utillity

class C2204957_TestClass(BaseTestCase):

    def test_C2204957(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        activeobj = active_chart_rollup.Active_Chart_Rollup(self.driver)
        
        fex_name = "AR-CH-033.fex"
        
        """
            Step 01 :Sign in to WebFOCUS as a basic user
            http://machine:port/{alias}
            Step 02:Execute the following URL:
            http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP116%252FS7074&BIP_item=AR-CH-033.fex
        """
        utillobj.active_run_fex_api_login(fex_name, "S7074", 'mrid', 'mrpass')
        
        parent_css="#MAINTABLE_wbody0 [class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 21, 65)
        
        xaxis_value="Category : Product"
        yaxis_value="Unit Sales"
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 1(i) Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step 1(ii) Verify Y Axis Title")
        expected_xval_list=['Coffee/Capuccino', 'Coffee/Espresso', 'Coffee/Latte', 'Food/Biscotti', 'Food/Croissant', 'Food/Scone', 'Gifts/Coffee Grinder', 'Gifts/Coffee Pot', 'Gifts/Mug', 'Gifts/Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 01.a: Verify XY labels')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 10, 'Step 01.b: Verify number of risers', custom_css ="g[class^='riser'] rect[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g5!mbar!", "cerulean_blue", "Step 01.c: Verify bar color")
        expected_tooltip_list=['Unit Sales, Coffee/Latte: 878,063']
        miscelaneousobj.verify_active_chart_tooltip('MAINTABLE_wbody0', 'riser!s0!g2!mbar!', expected_tooltip_list, 'Step 01.d: verify the default tooltip values')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0', 'Unit Sales by Category, Product', 'Step 04.e: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 04.f: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.g: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.h: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        
        """
            Step 03 :Click Chart/Rollup Tool option from the dropdown menu
            Step 04 :Now click Chart tab
            Select 'Area' chart type and click OK.
        """
        activeobj.select_chartmenubar_option('MAINTABLE_wmenu0', 1, 'Chart/Rollup Tool', elem_index=0, custom_css='cpop')
        css="#wall1 #charttoolt1 #tpanel_0_1_0"
        utillobj.synchronize_with_number_of_element(css, 1, 30)
        
        utillobj.verify_object_visible(css, True, 'Step 3.1: Verify that Chart/Rollup Tool pop up opened')
        series_tab="#charttoolt1 #ttpanel_0_1_0[class*='arToolTabSelected']"
        
        utillobj.verify_object_visible(series_tab, True, 'Step 3.2: Verify that Series tab is displayed: Series and Charts.')
        chart_tab="#charttoolt1 #ttpanel_1_1_0[class*='arToolTab']"
        
        utillobj.verify_object_visible(chart_tab, True, 'Step 3.3: Verify that Charts tab is displayed: Series and Charts.')
        
        elem=self.driver.find_element_by_css_selector(".arChartMenuBarContainer div[title='More Options']")
        utillobj.default_click(elem)
        time.sleep(2)
        elem=self.driver.find_element_by_css_selector("table tbody span[id='set0_cpop-999_x__0_2i_t']")
        utillobj.default_click(elem)
        utillobj.synchronize_with_number_of_element("#wall1", 1, 15)
        activeobj.select_advance_chart('wall1', 'area')
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 [class*='riser!s0!g0!marea!']", 1, 25)
        
        """
            Step 05:
            Verify that corresponding chart is displayed correctly.
        """
        
        expected_xval_list=['Coffee/Capuccino', 'Coffee/Espresso', 'Coffee/Latte', 'Food/Biscotti', 'Food/Croissant', 'Food/Scone', 'Gifts/Coffee Grinder', 'Gifts/Coffee Pot', 'Gifts/Mug', 'Gifts/Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 05a: Verify XY labels')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!marea!", "cerulean_blue", "Step 05.b: Verify bar color")
        
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0', 'Unit Sales by Category, Product', 'Step 04.e: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 04.f: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.g: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.h: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)    

if __name__ == "__main__":
    unittest.main()