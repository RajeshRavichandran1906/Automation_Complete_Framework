'''
Created on Sep 15, 2017

@author: Pavithra

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10670&group_by=cases:section_id&group_id=168200&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2312999
TestCase Name = AHTML: StreamGraph Basic chart using additional Buckets.
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon,visualization_resultarea,active_miscelaneous,ia_resultarea,visualization_metadata
from common.lib import utillity
from common.wftools import visualization

class C2312999_TestClass(BaseTestCase):

    def test_C2312999(self):
        
        Test_Case_ID="C2312999"
        """
            TESTCASE VARIABLES
        """     
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(15) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        visual_obj=visualization.Visualization(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        """
            Step 01:Open FEX:http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10670%2FStreamBasic.fex&tool=Chart
                    Click the Run button.
            Expect to see the following Active Streamgraph.
        """
        utillobj.infoassist_api_edit("StreamBasic", 'chart', 'P116/S10670', mrid='mrid', mrpass='mrpass')
        parent_css="#pfjTableChart_1 g.chartPanel"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 01.1: Verify X-Axis Title")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=[]
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 01.2: Verify XY Label')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 01.3: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!marea', 'bar_blue1', 'Step 01.4: Verify Color')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST BY CAR', 'Step 01.5: Verify Chart Title')
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
            Step 02:Drag the field SALES to the Tooltip area.
                   
            Expect to see the SALES field under the Tooltip area in the Query panel.
        """
        metadataobj.drag_drop_data_tree_items_to_query_tree('SALES', 1, 'Tooltip',0)
        parent_css="#queryTreeWindow table tr:nth-child(11) td"
        resobj.wait_for_property(parent_css, 1, string_value='SALES', with_regular_exprestion=True)
        time.sleep(5)
        metadataobj.verify_query_pane_field('Tooltip', 'SALES', 1, "Step 02:")
       
        """
            Step 03:Click the Run button.
                    Hover over lower area(blue) for Alfa Romeo.
           
            Expect to see the SALES field added to the Tooltip information.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        visual_obj.wait_for_number_of_element("#MAINTABLE_wbody0 [class*='riser']", 2, 40)
        expected_tooltip_list=['CAR:ALFA ROMEO', 'DEALER_COST:16,235', 'SALES:30200', 'Filter Chart', 'Exclude from Chart']
        miscelaneousobj.select_or_verify_marker_tooltip(marker_class='marker!s0!g0!mmarker!',verify_tooltip_list=expected_tooltip_list, msg='Step 03 : Verify tooltip')
        time.sleep(1)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 03.2: Verify X-Axis Title")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=[]
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 03.3: Verify XY Label')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 03.4: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!marea', 'bar_blue1', 'Step 03.5: Verify Color')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST, SALES BY CAR', 'Step 03.6: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03.7: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label_list=['DEALER_COST', 'RETAIL_COST']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 03.10: Verify Legends ')
        time.sleep(9)
      
        """
            Step 04:Drag the field SEATS to the Multigraph area.
                           
            Expect to see the SEATS field under the Multigraph area in the Query panel.
        """
        time.sleep(3)
        utillobj.switch_to_default_content(pause=2)
        time.sleep(5)
        metadataobj.drag_drop_data_tree_items_to_query_tree('SEATS', 1, 'Multi-graph',0)
        parent_css="#queryTreeWindow table tr:nth-child(13) td"
        resobj.wait_for_property(parent_css, 1, string_value='SEATS', with_regular_exprestion=True)
        time.sleep(5)
        metadataobj.verify_query_pane_field('Multi-graph', 'SEATS', 1, "Step 04:")
         
        """
            Step 05: Click the Run button.
                 
            Expect to see the data reordered, with Alfa Romeo first and Peugeot last.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        time.sleep(2)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 05.1: Verify X-Axis Title")
        expected_xval_list=['ALFA ROMEO', 'JAGUAR', 'MASERATI', 'TRIUMPH', 'BMW', 'DATSUN', 'JENSEN', 'TOYOTA', 'AUDI', 'PEUGEOT']                          
        expected_yval_list=[]
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 05.2: Verify XY Label')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 05.3: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!marea', 'bar_blue1', 'Step 05.4: Verify Color')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST, SALES BY CAR', 'Step 05.5: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.6: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label_list=['DEALER_COST', 'RETAIL_COST']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step : 05.9 Verify Legends ')
     
        """
            Step 06:Hover over the lower area(blue) for Alfa Romeo.
                        
                    Expect to see 2 Seats for Alfa Romeo.
            This is the lowest value of SEATS.
        """
         
        expected_tooltip_list=['SEATS:2', 'CAR:ALFA ROMEO', 'DEALER_COST:16,235', 'SALES:30200', 'Filter Chart', 'Exclude from Chart']
        miscelaneousobj.select_or_verify_marker_tooltip(marker_class='marker!s0!g0!mmarker!',verify_tooltip_list=expected_tooltip_list, msg='Step 06 : Verify tooltip')
        
        """
            Step 07:Hover over the lower area(blue) for Peugeot.
               
            Expect to see 5 Seats for Peugeot. This is the highest value of SEATS.
        """
        time.sleep(6)
        expected_tooltip_list=['SEATS:5', 'CAR:PEUGEOT', 'DEALER_COST:4,631', 'SALES:0', 'Filter Chart', 'Exclude from Chart']
        miscelaneousobj.select_or_verify_marker_tooltip(marker_class='marker!s0!g9!mmarker!',verify_tooltip_list=expected_tooltip_list, msg='Step 07 : Verify tooltip')
        time.sleep(1)
   
        """
            step 08:Move the SEATS field from the Multigraph area to the Animate area.
               
            Expect to see the SEATS field under the Animate area in the Query panel.
        """
        utillobj.switch_to_default_content(pause=3)
        time.sleep(5)
        elem1=driver.find_element_by_css_selector("#queryTreeWindow table tr:nth-child(13) td")
        utillobj.click_on_screen(elem1, 'middle', click_type=0)
        time.sleep(6)   
        elem1=driver.find_element_by_css_selector("#queryTreeWindow table tr:nth-child(13) td img.icon")
        source_elem=utillobj.get_object_screen_coordinate(elem1, 'middle', move=True)   
        elem2=driver.find_element_by_css_selector("#queryTreeWindow table tr:nth-child(14) td img.icon")
        target_elem=utillobj.get_object_screen_coordinate(elem2, 'middle', move=True)  
        utillobj.drag_drop_on_screen(sx_offset=source_elem['x'],sy_offset=source_elem['y'],tx_offset=target_elem['x'],ty_offset=target_elem['y'])
        parent_css="#queryTreeWindow table tr:nth-child(14) td"
        resobj.wait_for_property(parent_css, 1, string_value='SEATS', with_regular_exprestion=True)
        time.sleep(8)
        metadataobj.verify_query_pane_field('Animate', 'SEATS', 1, "Step 08.1:")
        resobj.verify_xaxis_title("TableChart_1", 'CAR', "Step 08.2: Verify X-Axis Title")
        expected_xval_list=['ALFA ROMEO', 'JAGUAR', 'MASERATI', 'TRIUMPH']
        expected_yval_list=[]
        resobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 08.3: Verify XY Label')
        expected_label_list=['DEALER_COST', 'RETAIL_COST']
        resobj.verify_riser_legends('TableChart_1', expected_label_list, 'Step : 08.3 Verify Legends ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s1!g0!marea', 'bar_green', 'Step 08.4: Verify Color')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!marea', 'bar_blue1', 'Step 08.5: Verify Color')
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 2, 'Step 08.6: Verify Number of riser', custom_css="path[class^='riser']")
        time.sleep(5)
        element= driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(element, Test_Case_ID+"_Step_08")
        time.sleep(1)
        """
            Step 09:Click the Run button.
                    Hover over the lower area(blue) for Jaguar.
            Expect to see the following Streamgraph, showing only CARs with 2 SEATS.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        expected_tooltip_list=['SEATS:2', 'CAR:JAGUAR', 'DEALER_COST:7,427', 'SALES:0', 'Filter Chart', 'Exclude from Chart']
        miscelaneousobj.select_or_verify_marker_tooltip(marker_class='marker!s0!g1!mmarker!',verify_tooltip_list=expected_tooltip_list, msg='Step 09 : Verify tooltip')
        time.sleep(1)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 09.1: Verify X-Axis Title")
        expected_xval_list=['ALFA ROMEO', 'JAGUAR', 'MASERATI', 'TRIUMPH']
        expected_yval_list=[]
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 09.2: Verify XY Label')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 09.3: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!marea', 'bar_blue1', 'Step 09.4: Verify Color')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST, SALES BY SEATS, CAR', 'Step 09.5: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 09.6: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 09.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 09.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label_list=['DEALER_COST', 'RETAIL_COST']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step : 09.9 Verify Legends ')
        time.sleep(5)
        utillobj.switch_to_default_content(pause=2)
        element= driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(element, Test_Case_ID+"_Step_09")
        time.sleep(1)

        """
            Step 10: Move the slider control at the top to position 4.
                    Hover over the lower area(blue) for Jensen.
            Expect to see the following Streamgraph, showing only CARs with 4 SEATS.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        parentobj = driver.find_element_by_css_selector("#MAINTABLE_wbody0 .sliderContainer rect[class^='sliderBody']")
        utillobj.click_on_screen(parentobj,'middle', click_type=0)
        time.sleep(5)
        expected_tooltip_list=['SEATS:  4', 'CAR:  JENSEN', 'DEALER_COST:  14,940', 'SALES:  0', 'Filter Chart', 'Exclude from Chart']
        miscelaneousobj.select_or_verify_marker_tooltip(marker_class='marker!s0!g6!mmarker!',verify_tooltip_list=expected_tooltip_list, msg='Step 10.1 : Verify tooltip')
        time.sleep(1)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 10.2: Verify X-Axis Title")
        expected_xval_list=['ALFA ROMEO', 'BMW', 'DATSUN', 'JENSEN', 'TOYOTA']
        expected_yval_list=[]
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 10.3: Verify XY Label')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 10.4: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!marea', 'bar_blue1', 'Step 10.5: Verify Color')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST, SALES BY SEATS, CAR', 'Step 10.6: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 10.7: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 10.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 10.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label_list=['DEALER_COST', 'RETAIL_COST']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step10.10: Verify Legends ')
        time.sleep(5)
        utillobj.switch_to_default_content(pause=2)
        element= driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(element, Test_Case_ID+"_Step_12")
        time.sleep(1)

        """
            Step 11:Move the slider control at the top to position 5.
                    Hover over the lower area(blue) for Audi.

            Expect to see the following Streamgraph, showing only CARs with 5 SEATS.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        time.sleep(1)
        parentobj = driver.find_element_by_css_selector("#MAINTABLE_wbody0 .sliderContainer rect[class^='sliderBody']")
        utillobj.click_on_screen(parentobj,'right', click_type=0, x_offset=-15)
        time.sleep(2)        
        expected_tooltip_list=['SEATS:5', 'CAR:AUDI', 'DEALER_COST:5,063', 'SALES:7800', 'Filter Chart', 'Exclude from Chart']
        miscelaneousobj.select_or_verify_marker_tooltip(marker_class='marker!s0!g8!mmarker!',verify_tooltip_list=expected_tooltip_list, msg='Step 11 : Verify tooltip')
        time.sleep(1)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 11.2: Verify X-Axis Title")
        expected_xval_list=['JAGUAR',  'BMW', 'AUDI', 'PEUGEOT']
        expected_yval_list=[]
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 11.3: Verify XY Label')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 11.4: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g1!marea', 'bar_blue1', 'Step 11.5: Verify Color')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST, SALES BY SEATS, CAR', 'Step 11.6: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 11.7: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 11.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 11.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label_list=['DEALER_COST', 'RETAIL_COST']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 11.10: Verify Legends ')
        time.sleep(3)
        utillobj.switch_to_default_content(pause=2)
        element= driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(element, Test_Case_ID+"_Step_11")
        time.sleep(1)
        """
            Step 12: Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()       