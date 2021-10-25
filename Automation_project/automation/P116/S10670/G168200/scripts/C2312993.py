'''
Created on Sep 13, 2017

@author: Pavithra

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10670&group_by=cases:section_id&group_id=168200&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2312993
TestCase Name = AHTML: StreamGraph Basic chart Filtering/Exclusions.
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon,visualization_resultarea,active_miscelaneous,ia_resultarea
from common.lib import utillity

class C2312993_TestClass(BaseTestCase):

    def test_C2312993(self):
        
        Test_Case_ID="C2312993"
        """
            TESTCASE VARIABLES
        """     
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        
        """        
            Step 01:Open FEX: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10670%2FStreamBasic.fex&tool=Chart

            Click the Run button.
            
            Expect to see the following Active Streamgraph.
        """
        utillobj.infoassist_api_edit("StreamBasic", 'chart', 'P116/S10670', mrid='mrid', mrpass='mrpass')
        parent_css="#pfjTableChart_1 g.chartPanel"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 60)
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        parent_css="#MAINTABLE_wbody0 svg > g text[class^='xaxis'][class*='labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 10, 30)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 01.1: Verify X-Axis Title")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=[]
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 01.2: Verify XY Label')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 01.3: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!marea', 'bar_blue1', 'Step 01.4: Verify Color')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST by CAR', 'Step 01.5: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 01.6: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 01.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 01.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label_list=['DEALER_COST', 'RETAIL_COST']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step : 01.9 Verify Legends ')
        time.sleep(1)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(5)
        element= driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(element, Test_Case_ID+"_Step_01")
        time.sleep(1)
        
        """
            Step 02: Hover over the lower area(blue) for Alfa Romeo.
            Expect to see the following Tooltip information
            Step 03:Select the Exclude from Chart option.
            Expect to see the following Active Streamgraph, with Alfa Romeo excluded.
        """
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        parent_elem=driver.find_element_by_css_selector("#MAINTABLE_wbody0")
        utillobj.click_on_screen(parent_elem, 'left')
        time.sleep(2)
        expected_tooltip_list=['CAR:ALFA ROMEO', 'DEALER_COST:16,235', 'Filter Chart', 'Exclude from Chart']
        miscelaneousobj.select_or_verify_marker_tooltip('marker!s0!g0!mmarker!', select_tooltip="Exclude from Chart", verify_tooltip_list=expected_tooltip_list, msg='Step 03.01 : Verify marker tooltip values and select exclude from chart', parent_css='#MAINTABLE_wbody0')

        parent_css="#MAINTABLE_wbody0 svg > g text[class^='xaxis'][class*='labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 9, 20)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 03.1: Verify X-Axis Title")
        expected_xval_list=['AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=[]
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 03.2: Verify XY Label')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 03.3: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!marea', 'bar_blue1', 'Step 03.4: Verify Color')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST by CAR', 'Step 03.5: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03.6: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 03.9: Filter Button Visible')
        expected_label_list=['DEALER_COST', 'RETAIL_COST']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step : 03.10: Verify Legends')
        time.sleep(1)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(5)
        element= driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(element, Test_Case_ID+"_Step_03")
        time.sleep(1)

        """
            Step 04:Hover over the upper area(light green) for BMW.
            Select the Exclude from Chart option.
                  
            Expect to see the following Active Streamgraph, with Alfa Romeo and BMW excluded.
        """
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        parent_elem=driver.find_element_by_css_selector("#MAINTABLE_wbody0")
        utillobj.click_on_screen(parent_elem, 'left')
        time.sleep(2)
        miscelaneousobj.select_or_verify_marker_tooltip('marker!s1!g1!mmarker!', select_tooltip="Exclude from Chart", msg='Step 4.1 : Verify marker tooltip', parent_css='#MAINTABLE_wbody0')
        
        parent_css="#MAINTABLE_wbody0 svg > g text[class^='xaxis'][class*='labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 8, 20)
        
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 04.1: Verify X-Axis Title")
        expected_xval_list=['AUDI', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=[]
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 04.2: Verify XY Label')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 04.3: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!marea', 'bar_blue1', 'Step 04.4: Verify Color')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST by CAR', 'Step 04.5: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04.6: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 04.9: Filter Button Visible')
        expected_label_list=['DEALER_COST', 'RETAIL_COST']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step : 04.10: Verify Legends')
        time.sleep(1)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(5)
        element= driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(element, Test_Case_ID+"_Step_04")
        time.sleep(1)

        """
            Step 05:Hover over the lower area(blue) for Audi and click the Remove Filter option.
                    
                    Expect to see the Filter removed and all CARs restored.
        """
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        parent_elem=driver.find_element_by_css_selector("#MAINTABLE_wbody0")
        utillobj.click_on_screen(parent_elem, 'left')
        time.sleep(2)
        miscelaneousobj.select_or_verify_marker_tooltip('marker!s0!g0!mmarker!', select_tooltip="Remove Filter", msg='Step 5.1 : Verify marker tooltip', parent_css='#MAINTABLE_wbody0')
        
        parent_css="#MAINTABLE_wbody0 svg > g text[class^='xaxis'][class*='labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 10, 20)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 05.1: Verify X-Axis Title")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=[]
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 05.2: Verify XY Label')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 05.3: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!marea', 'bar_blue1', 'Step 05.4: Verify Color')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST by CAR', 'Step 05.5: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.6: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", False, 'Step 05.9: Filter Button Removed')
        expected_label_list=['DEALER_COST', 'RETAIL_COST']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step : 05.10: Verify Legends')
        time.sleep(1)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(5)
        element= driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(element, Test_Case_ID+"_Step_05")
        time.sleep(1)

        """
            Step 06:Left click and draw a box that touches Alfa Romeo and Audi.
                    
            Expect to see the following box around Alfa Romeo and Audi.
        """
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        elem1=driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class='marker!s0!g0!mmarker!']")
        source_elem=utillobj.enable_marker_using_javascript(elem1)
        elem2=driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class='marker!s1!g1!mmarker!']")
        target_elem=utillobj.enable_marker_using_javascript(elem2)  
        time.sleep(3)
        utillobj.drag_drop_on_screen(sx_offset=source_elem['x']-40,sy_offset=source_elem['y']+40,tx_offset=target_elem['x']+10,ty_offset=target_elem['y']-50)
        
        """
            Step 07:Select the Exclude from Chart option.
    
            Expect to see both Alfa Romeo and Audi removed.
        """
        time.sleep(1)
        resobj.select_or_verify_lasso_filter(select='Exclude from Chart')
        parent_css="#MAINTABLE_wbody0 svg > g text[class^='xaxis'][class*='labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 8, 20)
        
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 07.1: Verify X-Axis Title")
        expected_xval_list=['BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=[]
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 07.2: Verify XY Label')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 07.3: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!marea', 'bar_blue1', 'Step 07.4: Verify Color')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST by CAR', 'Step 07.5: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 07.6: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 07.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 07.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 07.9: Filter Button Visible')
        expected_label_list=['DEALER_COST', 'RETAIL_COST']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step : 07.10: Verify Legends')
        time.sleep(1)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(5)
        element= driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(element, Test_Case_ID+"_Step_07")
        time.sleep(1)

        """
            Step 08:Hover over the lower area(blue) for BMW and select the Remove Filter option.
            
            Expect to see the Filter removed and all CARs restored.
        """
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        parent_elem=driver.find_element_by_css_selector("#MAINTABLE_wbody0")
        utillobj.click_on_screen(parent_elem, 'left')
        time.sleep(2)
        miscelaneousobj.select_or_verify_marker_tooltip('marker!s0!g3!mmarker!', select_tooltip="Remove Filter", msg='Step 8.1 : Verify marker tooltip', parent_css='#MAINTABLE_wbody0')
        
        parent_css="#MAINTABLE_wbody0 svg > g text[class^='xaxis'][class*='labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 10, 20)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 08.1: Verify X-Axis Title")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=[]
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 08.2: Verify XY Label')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 08.3: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!marea', 'bar_blue1', 'Step 08.4: Verify Color')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST by CAR', 'Step 08.5: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 08.6: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 08.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 08.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", False, 'Step 08.9: Filter Button Removed')
        expected_label_list=['DEALER_COST', 'RETAIL_COST']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step : 08.10: Verify Legends')
        time.sleep(1)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(5)
        element= driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(element, Test_Case_ID+"_Step_08")
        time.sleep(1)
    
        """
            Step 09: Left click and draw a box that touches Peugeot, Toyota and Triumph.
                    Select the Filter Chart option.
                    
            Expect to see only data for Peugeot, Toyota & Triumph.
        """
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        elem1=driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class='marker!s0!g7!mmarker!']")
        source_elem=utillobj.enable_marker_using_javascript(elem1)
        elem2=driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class='marker!s1!g9!mmarker!']")
        target_elem=utillobj.enable_marker_using_javascript(elem2)  
        time.sleep(3)
        utillobj.drag_drop_on_screen(sx_offset=source_elem['x']-5,sy_offset=source_elem['y']+50,tx_offset=target_elem['x']+30,ty_offset=target_elem['y']-50)
        time.sleep(1)
        resobj.select_or_verify_lasso_filter(select='Filter Chart')
        
        parent_css="#MAINTABLE_wbody0 svg > g text[class^='xaxis'][class*='labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 3, 20)
        
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 09.1: Verify X-Axis Title")
        expected_xval_list=['PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=[]
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 09.2: Verify XY Label')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 09.3: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!marea', 'bar_blue1', 'Step 09.4: Verify Color')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST by CAR', 'Step 09.5: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 09.6: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 09.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 09.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 09.9: Filter Button Visible')
        expected_label_list=['DEALER_COST', 'RETAIL_COST']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step : 09.10: Verify Legends')
        time.sleep(1)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(5)
        element= driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(element, Test_Case_ID+"_Step_09")
        time.sleep(3)

        """
            Step 10:Hover over the lower area(blue) for Peugeot and select the Remove Filter option.
    
            Expect to see all CARs restored.
        """
        utillobj.switch_to_frame(pause=2)
        time.sleep(3)
        parent_elem=driver.find_element_by_css_selector("#MAINTABLE_wbody0")
        utillobj.click_on_screen(parent_elem, 'left')
        time.sleep(2)
        miscelaneousobj.select_or_verify_marker_tooltip('marker!s0!g0!mmarker!', select_tooltip="Remove Filter", msg='Step 10.1 : Verify marker tooltip')
        
        parent_css="#MAINTABLE_wbody0 svg > g text[class^='xaxis'][class*='labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 10, 20)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 10.1: Verify X-Axis Title")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=[]
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 10.2: Verify XY Label')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 10.3: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!marea', 'bar_blue1', 'Step 10.4: Verify Color')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST by CAR', 'Step 10.5: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 10.6: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 10.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 10.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", False, 'Step 10.9: Filter Button Removed')
        expected_label_list=['DEALER_COST', 'RETAIL_COST']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step : 10.10: Verify Legends')
        time.sleep(1)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(5)
        element= driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(element, Test_Case_ID+"_Step_10")

        """
            Step 11:Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()       