'''
Created on Oct 05, 2017

@author: Pavithra

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10670&group_by=cases:section_id&group_id=168200&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2313072
TestCase Name = AHTML: Mekko chart ColorBy procedure creation.
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon,visualization_resultarea,active_miscelaneous,visualization_metadata,ia_ribbon
from common.lib import utillity

class C2313072_TestClass(BaseTestCase):

    def test_C2313072(self):
        
        Test_Case_ID="C2313072"
        """
            TESTCASE VARIABLES
        """     
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        time_out=15
           
        """
            Step 01:Launch new chart using the IA API
            http://machine:port/{alias}/ia?tool=chart&master=ibisamp/car&item=IBFS%3A%2FWFC%2FRepository%2FS10670%2FMekkoBucketizedCharts
        """
        utillobj.infoassist_api_login('Chart', 'ibisamp/car', 'P116/S10670', 'mrid', 'mrpass')
        parent_css="#pfjTableChart_1 g.chartPanel"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 65)
        
        """
            Step 02:Select Active Report.
            Click the Format tab and select Other.
            Select the HTML5 group, then select Mekko chart.
            Click OK.
        """
        ribbonobj.change_output_format_type('active_report', location='Home')
        parent_css="#pfjTableChart_1 g.chartPanel"
        utillobj.synchronize_with_number_of_element(parent_css, 1, time_out)
        
        ribbonobj.select_ribbon_item('Format', 'Other')
        parent_css="[id^='SelectChartTypeDlg'] [class*='active'] [class*='window-caption'] [class*='bi-label']"
        utillobj.synchronize_with_visble_text(parent_css, visble_element_text='Selectachart', expire_time=time_out)
        ia_ribbobj.select_other_chart_type('html5', 'html5_Mekko', 2, ok_btn_click=True)
        time.sleep(3)
        
        """
            Expect to see the following Preview pane for Mekko chart.
        """
        expected_xval_list=['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4']
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 02.1: Verify XY Label')
        expected_label_list=['Series0', 'Series1', 'Series2', 'Series3', 'Series4']
        resobj.verify_riser_legends('TableChart_1', expected_label_list, 'Step 02.2: Verify Legends ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s4!g4!mbar!', 'brick_red', 'Step 02.3: Verify Color')
        resobj.verify_number_of_riser("TableChart_1", 1, 25, 'Step 02.4: Verify the total number of risers displayed on preview')
        expected_datalabel=['175', '150', '125', '100', '75']
        resobj.verify_data_labels('TableChart_1', expected_datalabel, 'Step 02.5: Verify datalabels ', custom_css=".chartPanel text[class^='stackTotalLabel']") 

        """
            Step 03:Add fields CAR to the Horizontal axis, then DEALER_COST & RETAIL_COST to the Vertical axis.
        """
        metadataobj.datatree_field_click('CAR', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(5) td"
        utillobj.synchronize_with_visble_text(parent_css, visble_element_text='CAR', expire_time=time_out)
        
        metadataobj.datatree_field_click('DEALER_COST', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(4) td"
        utillobj.synchronize_with_visble_text(parent_css, visble_element_text='DEALER_COST', expire_time=time_out)
        
        metadataobj.datatree_field_click('RETAIL_COST', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(5) td"
        utillobj.synchronize_with_visble_text(parent_css, visble_element_text='RETAIL_COST', expire_time=time_out)
        
        """
            Expect to see the following Preview pane.
        """
        
        expected_xval_list=['BMW', 'MASERATI', 'JAGUAR', 'ALFA ROMEO', 'JENSEN', 'AUDI', 'PEU...', 'TRI...', 'T...', 'D...']
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 03.1: Verify XY Label', x_axis_label_length=1)
        expected_label_list=['DEALER_COST', 'RETAIL_COST']
        resobj.verify_riser_legends('TableChart_1', expected_label_list, 'Step 03.2: Verify Legends ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g2!mbar!', 'bar_blue1', 'Step 03.3: Verify Color')
        resobj.verify_number_of_riser("TableChart_1", 1, 20, 'Step 03.4: Verify the total number of risers displayed on preview')
        expected_datalabel=['108K', '56,500', '40,990', '35,800', '32,790', '11,033', '10,241', '9,392', '6,...', '5,...']
        resobj.verify_data_labels('TableChart_1', expected_datalabel, 'Step 03.5: Verify datalabels ',data_label_length=1, custom_css=".chartPanel text[class^='stackTotalLabel']") 
 
        """
            Step 04:Drag field COUNTRY to the Color area under Marker in the design pane.
            Expect to see the following Preview pane, with Color By added to the design pane.
            Also expect to see the Color By appear as distinct entries in the chart legend.
        """
        metadataobj.drag_drop_data_tree_items_to_query_tree('COUNTRY', 1, 'Color',0)
        parent_css="#queryTreeWindow table tr:nth-child(10) td"
        utillobj.synchronize_with_visble_text(parent_css, visble_element_text='COUNTRY', expire_time=time_out)
        
        
        resobj.verify_xaxis_title("TableChart_1", 'CAR', "Step 04.1: Verify X-Axis Title")
        expected_xval_list=['BMW', 'MASERATI', 'JAGUAR', 'ALFA ROMEO', 'JENSEN', 'AUDI', 'PEU...', 'TRI...', 'T...', 'D...']
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 04.2: Verify XY Label', x_axis_label_length=1)
        expected_label_list=['DEALER_COST : ENGLAND', 'RETAIL_COST : ENGLAND', 'DEALER_COST : FRANCE', 'RETAIL_COST : FRANCE','DEALER_COST : ITALY', 'RETAIL_COST : ITALY', 'DEALER_COST : JAPAN', 'RETAIL_COST : JAPAN', 'DEALER_COST : W GERMANY', 'RETAIL_COST : W GERMANY']
        resobj.verify_riser_legends('TableChart_1', expected_label_list, 'Step 04.3: Verify Legends ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s2!g7!mbar!', 'dark_green', 'Step 04.4: Verify Color')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g5!mbar!', 'bar_blue1', 'Step 04.5: Verify Color')
        utillobj.verify_chart_color('TableChart_1', 'riser!s4!g0!mbar!', 'brick_red', 'Step 04.6: Verify Color')
        resobj.verify_number_of_riser("TableChart_1", 1, 20, 'Step 04.7: Verify the total number of risers displayed on preview')
        expected_datalabel=['108K', '56,500', '40,990', '35,800', '32,790', '11,033', '10,241', '9,392', '6,...', '5,...']
        resobj.verify_data_labels('TableChart_1', expected_datalabel, 'Step 04.8: Verify datalabels ',data_label_length=1, custom_css=".chartPanel text[class^='stackTotalLabel']") 
        time.sleep(5)
        element= driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(element, Test_Case_ID+"_Actual_step_04")
        time.sleep(1)
        

        """
            Step 05:Click the Run button.
            Expect to see the following Active Mekko chart.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 05.1: Verify X-Axis Title")
        expected_xval_list=['BMW', 'MASERATI', 'JAGUAR', 'ALFA ROMEO', 'JENSEN', 'AUDI', 'PEU...', 'TRI...', 'T...', 'D...']
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 05.2: Verify XY Label', x_axis_label_length=1)
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 05.3: Verify the total number of risers displayed on run')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s2!g7!mbar!', 'dark_green', 'Step 05.4: Verify Color')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g5!mbar!', 'bar_blue1', 'Step 05.5: Verify Color')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s4!g0!mbar!', 'brick_red', 'Step 05.6: Verify Color')            
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST by COUNTRY, CAR', 'Step 05.7: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.8: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.9: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.10: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label_list=['DEALER_COST : ENGLAND', 'RETAIL_COST : ENGLAND', 'DEALER_COST : FRANCE', 'RETAIL_COST : FRANCE','DEALER_COST : ITALY', 'RETAIL_COST : ITALY', 'DEALER_COST : JAPAN', 'RETAIL_COST : JAPAN', 'DEALER_COST : W GERMANY', 'RETAIL_COST : W GERMANY']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 05.11: Verify Legends ')
        
        expected_datalabel=['108K', '56,500', '40,990', '35,800', '32,790', '11,033', '10,241', '9,392', '6,...', '5,...']
        resobj.verify_data_labels('MAINTABLE_wbody0', expected_datalabel, 'Step 05.13: Verify datalabels ', data_label_length=1,custom_css=".chartPanel text[class^='stackTotalLabel']") 
        time.sleep(2)
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step_05', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        
        """
            Step 06 : Save & close the IA procedure as MekkoColorBy.
        """
        ribbonobj.select_tool_menu_item('menu_save')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """
            Step 07 : Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
        
if __name__ == '__main__':
    unittest.main()
        

