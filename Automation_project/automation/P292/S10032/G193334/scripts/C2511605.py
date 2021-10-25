'''
Created on May 14, 2018

@author: BM13368
Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2511605
TestCase Name =Chart: Verify that user is able to filter AHTML chart(82xx)
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, active_miscelaneous
from common.lib import utillity
from common.wftools import active_report
from common.wftools import visualization

class C2511605_TestClass(BaseTestCase):

    def test_C2511605(self):
        
        """
            TESTCASE VARIABLES
        """
        visual_obj = visualization.Visualization(self.driver)
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
               
        """
            Step 01 :Sign in to WebFOCUS as a Basic user http://machine:port/{alias}
            Step 02 :Expand folder P292_S10032_G19334 Execute the following URL:
            http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10032_G157266%252FAHTML_ON&BIP_item=NB_AR_AHTML-002.fex
            Step 03:Verify the report is generated.
        """
        active_reportobj.run_active_report_using_api('NB_AR_AHTML_002.fex', column_css="#MAINTABLE_wbody0_f [class='colHeader-label!']", synchronize_visible_element_text="Category")
        
        """
           Step 03:Verify the report is generated.
        """
        
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","Unit Sales by Category, Product", "Step 03.1 : Verify chart title ")
        expected_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval1_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 03.2: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 10, 'Step 03.3: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g4!mbar!r0!c1!", "bar_blue", "Step 03.4: Verify  riser color")
#         resobj.verify_xaxis_title("MAINTABLE_wbody0","Product","Step 03.5: Verify Xaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 03.5: Verify yaxis title")

        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03.6: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label=['Coffee','Food','Gifts']
        resobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody0", "Columns", "Category : Product",expected_label,"Step 03.9: Verify visualization column header lables")       
        
        """
           Step 04:Select Espresso and Latte bars from Coffee section in the chart via lasso.

            Verify these menu items appear on the chart:
            
            2 points
            Filter Chart
            Exclude from Chart
        """
        
        source_element = utillobj.validate_and_get_webdriver_object("rect[class='riser!s0!g5!mbar!r0!c0!']",'source')
        target_element = utillobj.validate_and_get_webdriver_object("rect[class='riser!s0!g6!mbar!r0!c0!']",'target')
        visual_obj.create_lasso(source_element, target_element, source_element_location='top_left')
        resobj.select_or_verify_lasso_filter(verify=['2 points','Filter Chart','Exclude from Chart'],msg='Step 04.1:Verify these menu items appear on the chart')
        
        
        """
           Step 05:Click Filter Chart menu option. Verify Espresso and Latte bars are filtered on a chart. Verify filter icon appears on active tool bar.
        """
        resobj.select_or_verify_lasso_filter(select='Filter Chart') 
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","Unit Sales by Category, Product", "Step 05.1 : Verify chart title ")
        expected_xval_list=['Espresso', 'Latte']
        expected_yval1_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 05.2: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 2, 'Step 05.3: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g1!mbar!r0!c0!", "bar_blue", "Step 05.4: Verify  riser color")
#         resobj.verify_xaxis_title("MAINTABLE_wbody0","Product","Step 05.5: Verify Xaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 05.5: Verify yaxis title")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.6: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 05.9: Filter Button Visible')
        
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
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g1!mbar!r0!c0!", expected_tooltip_list, "Step 06.1: Verify bar value")
        
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
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","Unit Sales by Category, Product", "Step 07.1 : Verify chart title ")
        expected_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval1_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 07.2: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 10, 'Step 07.3: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g4!mbar!r0!c1!", "bar_blue", "Step 07.4: Verify  riser color")
#         resobj.verify_xaxis_title("MAINTABLE_wbody0","Product","Step 07.5: Verify Xaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 07.5: Verify yaxis title")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 07.6: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 07.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 07.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label=['Coffee','Food','Gifts']
        resobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody0", "Columns", "Category : Product",expected_label,"Step 07.9: Verify visualization column header lables")       
        
        """
           Step 08:Select Espresso and Latte bars from Coffee section in the chart via lasso.

            Verify these menu items appear on the chart:
            
            2 points
            Filter Chart
            Exclude from Chart
        """
        source_element = utillobj.validate_and_get_webdriver_object("rect[class='riser!s0!g5!mbar!r0!c0!']",'source')
        target_element = utillobj.validate_and_get_webdriver_object("rect[class='riser!s0!g6!mbar!r0!c0!']",'target')
        visual_obj.create_lasso(source_element, target_element, source_element_location='top_left')
        visual_obj.verify_lasso_tooltip(['2 points','Filter Chart','Exclude from Chart'], msg='Step 08.1:Verify these menu items appear on the chart')
        
        """
           Step 09:Click Exclude from Chart menu option. Verify Coffee category is removed from a chart. Verify filter icon appears on active tool bar.
        """ 
        resobj.select_or_verify_lasso_filter(select='Exclude from Chart')
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","Unit Sales by Category, Product", "Step 09.1 : Verify chart title ")
        expected_xval_list=['Capuccino', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval1_list=['0', '100K', '200K', '300K', '400K', '500K','600K','700K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 09.2: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 8, 'Step 09.3: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g4!mbar!r0!c1!", "bar_blue", "Step 09.4: Verify  riser color")
#         resobj.verify_xaxis_title("MAINTABLE_wbody0","Product","Step 09.5: Verify Xaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 09.5: Verify yaxis title")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 09.6: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 09.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 09.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 09.9: Filter Button Visible')
         
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
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g3!mbar!r0!c2!", expected_tooltip_list, "Step 10.1: Verify bar value")
         
        """
           Step 11:Click Remove filter menu option. Verify original chart appears on the screen.
        """
        css="#MAINTABLE_wbody0 .chartPanel"
        move=driver.find_element_by_css_selector(css)
        utillobj.click_on_screen(move, 'start')
        time.sleep(5)
        parent_obj = driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class='riser!s0!g1!mbar!r0!c0!']")
        utillobj.click_on_screen(parent_obj,'start', javascript_marker_enable=True, mouse_duration=2.5)
        time.sleep(2)
        resobj.select_default_tooltip_menu("MAINTABLE_wbody0","riser!s0!g1!mbar!r0!c0!", 'Remove Filter')
        time.sleep(5)
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","Unit Sales by Category, Product", "Step 11.1 : Verify chart title ")
        expected_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval1_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 11.2: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 10, 'Step 11.3: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g4!mbar!r0!c1!", "bar_blue", "Step 11.4: Verify  riser color")
#         resobj.verify_xaxis_title("MAINTABLE_wbody0","Product","Step 11.5: Verify Xaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 11.5: Verify yaxis title")
        expected_tooltip_list=['Category:Food', 'Product:Croissant', 'Unit Sales:630054', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g4!mbar!r0!c1!", expected_tooltip_list, "Step 11.6: Verify bar value")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 11.7: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 11.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 11.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label=['Coffee','Food','Gifts']
        resobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody0", "Columns", "Category : Product",expected_label,"Step 11.10: Verify visualization column header lables")       
        
        """
           Step 12:Dismiss the window and logout.http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
       
        
if __name__ == '__main__':
    unittest.main() 