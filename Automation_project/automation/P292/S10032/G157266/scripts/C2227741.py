'''
Created on May 14, 2018

@author: BM13368
Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227741
TestCase Name =Chart: Verify that user is able to filter AHTML chart(82xx)
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, active_miscelaneous
from common.lib import utillity
from common.wftools import visualization

class C2227741_TestClass(BaseTestCase):

    def test_C2227741(self):
        
        """
            TESTCASE VARIABLES
        """
        visual_obj = visualization.Visualization(self.driver)
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
               
        """
            Step 01 :Sign in to WebFOCUS as a Basic user http://machine:port/{alias}
            Step 02 :Expand folder P292_S10032_G157266 Execute the following URL:
            http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10032_G157266%252FAHTML_OFF&BIP_item=NB_AR_AHTML-002.fex
            Step 03:Verify the report is generated.
        """
        
        utillobj.active_run_fex_api_login('NB_AR_AHTML_002.fex', 'S10032_ahtml_off', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 svg g.risers >g>rect[class^='riser']", 10, 65)
        
        """
           Step 03:Verify the report is generated.
        """
        
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","Unit Sales by Category, Product", "Step 03.01: Verify chart title ")
        expected_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval1_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 03.02: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 10, 'Step 03.03: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g4!mbar!r0!c1!", "bar_blue", "Step 03.04: Verify  riser color")
#         resobj.verify_xaxis_title("MAINTABLE_wbody0","Product","Step 03.5: Verify Xaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 03.05: Verify yaxis title")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03.06: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.07: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.08: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label=['Coffee','Food','Gifts']
        resobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody0", "Columns", "Category : Product",expected_label,"Step 03.09: Verify visualization column header lables")       
        
        """
           Step 04:Select Espresso and Latte bars from Coffee section in the chart via lasso.

            Verify these menu items appear on the chart:
            
            2 points
            Filter Chart
            Exclude from Chart
        """
        source_element = utillobj.validate_and_get_webdriver_object("rect[class='riser!s0!g5!mbar!r0!c0!']",'source')
        target_element = utillobj.validate_and_get_webdriver_object("rect[class='riser!s0!g6!mbar!r0!c0!']",'target')
        visual_obj.create_lasso(source_element, target_element)
        resobj.select_or_verify_lasso_filter(verify=['2 points','Filter Chart','Exclude from Chart'],msg='Step 04.01: Verify these menu items appear on the chart')
        
        
        """
           Step 05:Click Filter Chart menu option. Verify Espresso and Latte bars are filtered on a chart. Verify filter icon appears on active tool bar.
        """
        resobj.select_or_verify_lasso_filter(select='Filter Chart') 
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","Unit Sales by Category, Product", "Step 05.01 : Verify chart title ")
        expected_xval_list=['Espresso', 'Latte']
        expected_yval1_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 05.02: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 2, 'Step 05.03: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g1!mbar!r0!c0!", "bar_blue", "Step 05.04: Verify  riser color")
#         resobj.verify_xaxis_title("MAINTABLE_wbody0","Product","Step 05.05: Verify Xaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 05.05: Verify yaxis title")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.06: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.07: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.08: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 05.09: Filter Button Visible')
        
        """
           Step 06:Mouse over on Latte bar and verify context menu appears. It displays:

                Category: Coffee
                Product: Latte
                
                Unit Sales: 878,063
                
                Filter Chart
                Exclude from Chart
                Remove Filter
        """
        
        expected_tooltip_list=['Category:Coffee', 'Product:Latte', 'Unit Sales:878063', 'Filter Chart', 'Exclude from Chart', 'Remove Filter']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g1!mbar!r0!c0!", expected_tooltip_list, "Step 06.01: Verify bar value")
        
        """
           Step 07:Click Remove filter menu option. Verify original chart appears on the screen.
        """
        
        css="#MAINTABLE_wbody0 .chartPanel"
        move=driver.find_element_by_css_selector(css)
        utillobj.click_on_screen(move, 'top_right')
        time.sleep(5)
        parent_obj = driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class='riser!s0!g1!mbar!r0!c0!']")
        utillobj.click_on_screen(parent_obj,'bottom_middle', javascript_marker_enable=True, mouse_duration=2.5)
        time.sleep(2)
        resobj.select_default_tooltip_menu("MAINTABLE_wbody0","riser!s0!g1!mbar!r0!c0!",  'Remove Filter')
        time.sleep(5)
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","Unit Sales by Category, Product", "Step 07.01: Verify chart title ")
        expected_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval1_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 07.02: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 10, 'Step 07.03: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g4!mbar!r0!c1!", "bar_blue", "Step 07.04: Verify  riser color")
#         resobj.verify_xaxis_title("MAINTABLE_wbody0","Product","Step 07.5: Verify Xaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 07.05: Verify yaxis title")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 07.06: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 07.07: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 07.08: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label=['Coffee','Food','Gifts']
        resobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody0", "Columns", "Category : Product",expected_label,"Step 07.09: Verify visualization column header lables")       
        
        """
           Step 08:Select Espresso and Latte bars from Coffee section in the chart via lasso.

            Verify these menu items appear on the chart:
            
            2 points
            Filter Chart
            Exclude from Chart
        """
        source_element = utillobj.validate_and_get_webdriver_object("rect[class='riser!s0!g5!mbar!r0!c0!']",'source')
        target_element = utillobj.validate_and_get_webdriver_object("rect[class='riser!s0!g6!mbar!r0!c0!']",'target')
        visual_obj.create_lasso(source_element, target_element)
        resobj.select_or_verify_lasso_filter(verify=['2 points','Filter Chart','Exclude from Chart'],  msg='Step 08.01:Verify these menu items appear on the chart')
        move=driver.find_element_by_css_selector(css)
        utillobj.click_on_screen(move, 'top_right', click_type=0)
        source_element = utillobj.validate_and_get_webdriver_object("rect[class='riser!s0!g5!mbar!r0!c0!']",'source')
        target_element = utillobj.validate_and_get_webdriver_object("rect[class='riser!s0!g6!mbar!r0!c0!']",'target')
        visual_obj.create_lasso(source_element, target_element)
        
        """
           Step 09:Click Exclude from Chart menu option. Verify Coffee category is removed from a chart. Verify filter icon appears on active tool bar.
        """
        resobj.select_or_verify_lasso_filter(select='Exclude from Chart') 
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","Unit Sales by Category, Product", "Step 09.01 : Verify chart title ")
        expected_xval_list=['Capuccino', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval1_list=['0', '100K', '200K', '300K', '400K', '500K','600K','700K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 09.02: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 8, 'Step 09.03: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g4!mbar!r0!c1!", "bar_blue", "Step 09.04: Verify  riser color")
#         resobj.verify_xaxis_title("MAINTABLE_wbody0","Product","Step 09.5: Verify Xaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 09.05: Verify yaxis title")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 09.06: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 09.07: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 09.08: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 09.09: Filter Button Visible')
         
        """
           Step 10:Mouse over on Coffee Pot bar and verify context menu appears. It displays:
 
            Category: Gifts
            Product: Coffee Pot
             
            Unit Sales: 190,695
             
            Filter Chart
            Exclude from Chart
            Remove Filter
        """
        expected_tooltip_list=['Category:Gifts', 'Product:Coffee Pot', 'Unit Sales:190695', 'Filter Chart', 'Exclude from Chart', 'Remove Filter']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g3!mbar!r0!c2!", expected_tooltip_list, "Step 10.01: Verify bar value")
         
        """
           Step 11:Click Remove filter menu option. Verify original chart appears on the screen.
        """
        css="#MAINTABLE_wbody0 .chartPanel"
        move=driver.find_element_by_css_selector(css)
        utillobj.click_on_screen(move, 'start')
        time.sleep(5)
        parent_obj = driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class='riser!s0!g1!mbar!r0!c0!']")
        utillobj.click_on_screen(parent_obj,'middle', javascript_marker_enable=True, mouse_duration=2.5)
        resobj.select_default_tooltip_menu("MAINTABLE_wbody0","riser!s0!g1!mbar!r0!c0!", 'Remove Filter')
        time.sleep(5)
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","Unit Sales by Category, Product", "Step 11.01 : Verify chart title ")
        expected_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval1_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 11.02: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 10, 'Step 11.03: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g4!mbar!r0!c1!", "bar_blue", "Step 11.04: Verify  riser color")
#         resobj.verify_xaxis_title("MAINTABLE_wbody0","Product","Step 11.5: Verify Xaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 11.05: Verify yaxis title")
        expected_tooltip_list=['Category:Food', 'Product:Croissant', 'Unit Sales:630054', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g4!mbar!r0!c1!", expected_tooltip_list, "Step 11.06: Verify bar value")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 11.07: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 11.08: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 11.09: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label=['Coffee','Food','Gifts']
        resobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody0", "Columns", "Category : Product",expected_label,"Step 11.10: Verify visualization column header lables")       
        
        """
           Step 12:Dismiss the window and logout.http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """ 
        
if __name__ == '__main__':
    unittest.main() 