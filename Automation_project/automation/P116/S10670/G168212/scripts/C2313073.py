'''
Created on Oct 06, 2017

@author: Pavithra

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10670&group_by=cases:section_id&group_id=168200&group_order=asc
Test Case =http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2313073
TestCase Name =AHTML: Mekko chart Basic chart Filtering/Exclusions.
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon,visualization_resultarea,active_miscelaneous
from common.lib import utillity

class C2313073_TestClass(BaseTestCase):

    def test_C2313073(self):
        
        Test_Case_ID="C2313073"
        """
            TESTCASE VARIABLES
        """     
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(15) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(driver)
        
        """
            Step 01:Open FEX:

            http://machine:port/ibiapps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10670%2FMekkoBucketizedCharts%2FMekkocolorBy.fex&tool=Chart
        """
        utillobj.infoassist_api_edit("Mekko_Basic", 'chart', 'P116/S10670', mrid='mrid', mrpass='mrpass')
        parent_css="#pfjTableChart_1 g.chartPanel"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(8)
        expected_xval_list=['BMW', 'MASERATI', 'JAGUAR', 'ALFA ROMEO', 'JENSEN', 'AUDI', 'PEU...', 'TRI...', 'T...', 'D...']
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list,'Step 01.1: Verify XY Label', x_axis_label_length=1)
        expected_label_list=['DEALER_COST', 'RETAIL_COST']
        resobj.verify_riser_legends('TableChart_1', expected_label_list, 'Step 01.2: Verify Legends ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g2!mbar!', 'bar_blue1', 'Step 01.3: Verify Color')
        resobj.verify_number_of_riser("TableChart_1", 1, 20, 'Step 01.4: Verify the total number of risers displayed on preview')
        expected_datalabel=['108K', '56,500', '40,990', '35,800', '32,790', '11,033', '10,241', '9,392', '6,...', '5,...']
        resobj.verify_data_labels('TableChart_1', expected_datalabel, 'Step 01.5: Verify datalabels ', data_label_length=1, custom_css=".chartPanel text[class^='stackTotalLabel']") 
    
 
        """
            Step 02:Click the Run button.
            
            Expect to see the following Active Mekko chart, sorted in Descending Measure order.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 02.1: Verify X-Axis Title")
        expected_xval_list=['BMW', 'MASERATI', 'JAGUAR', 'ALFA ROMEO', 'JENSEN', 'AUDI', 'PEU...', 'TRI...', 'T...', 'D...']
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 02.2: Verify XY Label',  x_axis_label_length=1)
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 02.3: Verify the total number of risers displayed on run')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g2!mbar!', 'bar_blue1', 'Step 02.4: Verify Color')                  
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST by CAR', 'Step 02.5: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 02.6: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label_list=['DEALER_COST', 'RETAIL_COST']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step : 02.9 Verify Legends ')       
        expected_tooltip_list=['CAR:BMW', 'DEALER_COST:49,500', 'Filter Chart', 'Exclude from Chart']
#         resobj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g2!mbar!', expected_tooltip_list, 'Step 02.10: verify the default tooltip values')
        expected_datalabel=['108K', '56,500', '40,990', '35,800', '32,790', '11,033', '10,241', '9,392', '6,...', '5,...']
        resobj.verify_data_labels('MAINTABLE_wbody0', expected_datalabel, 'Step 02.11: Verify datalabels ',data_label_length=1, custom_css=".chartPanel text[class^='stackTotalLabel']") 
        time.sleep(2)
 
  
        """
            Step 03:Hover over the lower area(blue) for Alfa Romeo.
              
            Expect to see the following Tooltip information for Alfa Romeo. 
        """
        expected_tooltip_list=['CAR:ALFA ROMEO', 'DEALER_COST:16,235  (45.35%)', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g0!mbar!', expected_tooltip_list, 'Step 03.1: verify the default tooltip values')
          
          
        """
            Step 04:Select the Exclude from Chart option.
              
            Expect to see the following Active Mekko, with Alfa Romeo excluded.
        """
        resobj.select_default_tooltip_menu("MAINTABLE_wbody0","riser!s0!g0!mbar!", 'Exclude from Chart')
        time.sleep(5)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 04.1: Verify X-Axis Title")
        expected_xval_list=['BMW', 'MASERATI', 'JAGUAR', 'JENSEN', 'AUDI', 'PEUG..', 'TRI...', 'T...', 'D...']
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 05.2: Verify XY Label', x_axis_label_length=1)
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 18, 'Step 04.3: Verify the total number of risers displayed on run')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g1!mbar!', 'bar_blue1', 'Step 04.4: Verify Color')                  
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST by CAR', 'Step 04.5: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04.6: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label_list=['DEALER_COST', 'RETAIL_COST']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step : 04.9 Verify Legends ')
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 04.10 Filter Button Visible')
        expected_datalabel=['108K', '56,500', '40,990', '32,790', '11,033', '10,241', '9,392', '6,2...', '5,...']
        resobj.verify_data_labels('MAINTABLE_wbody0', expected_datalabel, 'Step 04.11: Verify datalabels ',data_label_length=1, custom_css=".chartPanel text[class^='stackTotalLabel']") 
        time.sleep(2)
         
        """
            Step 05:Hover over the upper area(light green) for BMW.
                    Select the Exclude from Chart option.
            
            Expect to see the following Active Mekko chart, with Alfa Romeo and BMW excluded.
       """
        resobj.select_default_tooltip_menu("MAINTABLE_wbody0","riser!s1!g1!mbar!", 'Exclude from Chart')
        time.sleep(5)
        """
            Step 06:Hover over the lower area(blue) for Audi and click the Remove Filter option.
              
            Expect to see the Filter removed and all CARs restored.
              
        """
        resobj.select_default_tooltip_menu("MAINTABLE_wbody0","riser!s0!g0!mbar!", 'Remove Filter')
        time.sleep(5)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 06.1: Verify X-Axis Title")
        expected_xval_list=['BMW', 'MASERATI', 'JAGUAR', 'ALFA ROMEO', 'JENSEN', 'AUDI', 'PEU...', 'TRI...', 'T...', 'D...']
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 05.2: Verify XY Label',x_axis_label_length=1)
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 06.3: Verify the total number of risers displayed on run')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g2!mbar!', 'bar_blue1', 'Step 06.4: Verify Color')                  
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST by CAR', 'Step 06.5: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 06.6: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 06.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 06.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label_list=['DEALER_COST', 'RETAIL_COST']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step : 06.9 Verify Legends ')
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", False, 'Step 06.10: Filter Button Removed')
        expected_datalabel=['108K', '56,500', '40,990', '35,800', '32,790', '11,033', '10,241', '9,392', '6,...', '5,...']
        resobj.verify_data_labels('MAINTABLE_wbody0', expected_datalabel, 'Step 02.5: Verify datalabels ',data_label_length=1, custom_css=".chartPanel text[class^='stackTotalLabel']") 
        time.sleep(2)
        """
            Step 07:Left click and draw a box that touches BMW and Maserati.
     
            Expect to see the following box around BMW and Maserati.
        """ 
        time.sleep(5)
        elem1=driver.find_element_by_css_selector("#MAINTABLE_wbody0 .risers g rect[class='riser!s0!g2!mbar!']")
        source_elem=utillobj.get_object_screen_coordinate(elem1, 'left', move=True)
        time.sleep(6) 
        elem2=driver.find_element_by_css_selector("#MAINTABLE_wbody0 .risers g rect[class='riser!s0!g6!mbar!']")
        target_elem=utillobj.get_object_screen_coordinate(elem2, 'middle', move=True)  
        time.sleep(6)
        utillobj.drag_drop_on_screen(sx_offset=source_elem['x']-15,sy_offset=source_elem['y'],tx_offset=target_elem['x']+25,ty_offset=target_elem['y'])
        """
            Step 08:Select the Exclude from Chart option.
             
            Expect to see both BMW and Maserati removed.
        """
        resobj.select_or_verify_lasso_filter(select='Exclude from Chart')
        time.sleep(2)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 08.1: Verify X-Axis Title")
        expected_xval_list=['JAGUAR', 'ALFA ROMEO', 'JENSEN', 'AUDI', 'PEUGEOT', 'TRIUMPH', 'TOYOTA', 'DATS...']
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 05.2: Verify XY Label',x_axis_label_length=1)
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 16, 'Step 08.3: Verify the total number of risers displayed on run')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g2!mbar!', 'bar_blue1', 'Step 08.4: Verify Color')                  
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST by CAR', 'Step 08.5: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 08.6: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 08.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 08.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label_list=['DEALER_COST', 'RETAIL_COST']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step : 08.9 Verify Legends ')
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 08.10 Filter Button Visible')
        expected_datalabel=['40,990', '35,800', '32,790', '11,033', '10,241', '9,392', '6,225', '5,765']
        resobj.verify_data_labels('MAINTABLE_wbody0', expected_datalabel, 'Step 02.5: Verify datalabels ',data_label_length=1, custom_css=".chartPanel text[class^='stackTotalLabel']") 
        time.sleep(2)
 
        """
            Step 09:Hover over the lower area(blue) for JAGUAR and select the Remove Filter option.
             
            Expect to see the Filter removed and all CARs restored.
        """
         
        resobj.select_default_tooltip_menu("MAINTABLE_wbody0", "riser!s0!g3!mbar!",'Remove Filter')
        time.sleep(5)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 09.1: Verify X-Axis Title")
        expected_xval_list=['BMW', 'MASERATI', 'JAGUAR', 'ALFA ROMEO', 'JENSEN', 'AUDI', 'PEU...', 'TRI...', 'T...', 'D...']
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 09.2: Verify XY Label',  x_axis_label_length=1)
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 09.3: Verify the total number of risers displayed on run')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g2!mbar!', 'bar_blue1', 'Step 09.4: Verify Color')                  
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST by CAR', 'Step 09.5: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 09.6: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 09.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 09.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label_list=['DEALER_COST', 'RETAIL_COST']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step : 09.9 Verify Legends ')
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", False, 'Step 09.10: Filter Button Removed')
        expected_datalabel=['108K', '56,500', '40,990', '35,800', '32,790', '11,033', '10,241', '9,392', '6,...', '5,...']
        resobj.verify_data_labels('MAINTABLE_wbody0', expected_datalabel, 'Step 10.11: Verify datalabels ',data_label_length=1, custom_css=".chartPanel text[class^='stackTotalLabel']") 
        time.sleep(2)
        """
            Step 10:Left click and draw a box that touches 
                    Triumph, Toyota & Datsun, the last three blocks.
                    Select the Filter Chart option.

            Expect to see only data blocks for Triumph, Toyota & Datsun.
        """
        time.sleep(5)
        elem1=driver.find_element_by_css_selector("#MAINTABLE_wbody0 .risers g rect[class='riser!s0!g3!mbar!']")
        source_elem=utillobj.get_object_screen_coordinate(elem1, 'right', move=True)   
        time.sleep(6) 
        elem2=driver.find_element_by_css_selector("#MAINTABLE_wbody0 .risers g rect[class='riser!s0!g9!mbar!']")
        target_elem=utillobj.get_object_screen_coordinate(elem2, 'middle', move=True)  
        time.sleep(6) 
        utillobj.drag_drop_on_screen(sx_offset=source_elem['x']+10,sy_offset=source_elem['y'],tx_offset=target_elem['x'],ty_offset=target_elem['y'])
        resobj.select_or_verify_lasso_filter(select='Filter Chart')
        time.sleep(2)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 10.1: Verify X-Axis Title")
        expected_xval_list=['TRIUMPH', 'TOYOTA', 'DATSUN']
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 05.2: Verify XY Label')
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 6, 'Step 10.3: Verify the total number of risers displayed on run')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g2!mbar!', 'bar_blue1', 'Step 10.4: Verify Color')                  
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST by CAR', 'Step 10.5: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 10.6: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 10.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 10.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label_list=['DEALER_COST', 'RETAIL_COST']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step : 10.9 Verify Legends ')
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 10.10 Filter Button Visible')
        expected_datalabel=['9,392', '6,225', '5,765']
        resobj.verify_data_labels('MAINTABLE_wbody0', expected_datalabel, 'Step 02.5: Verify datalabels ', custom_css=".chartPanel text[class^='stackTotalLabel']") 
        time.sleep(2)

        """
            Step 11:Hover over the lower area(blue) for Triumph and select the Remove Filter option.
            
            Expect to see all CARs restored.
        """
        resobj.select_default_tooltip_menu("MAINTABLE_wbody0","riser!s0!g2!mbar!", 'Remove Filter')
        time.sleep(5)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 11.1: Verify X-Axis Title")
        expected_xval_list=['BMW', 'MASERATI', 'JAGUAR', 'ALFA ROMEO', 'JENSEN', 'AUDI', 'PEU...', 'TRI...', 'T...', 'D...']
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 02.2: Verify XY Label',  x_axis_label_length=1)
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 11.3: Verify the total number of risers displayed on run')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g2!mbar!', 'bar_blue1', 'Step 11.4: Verify Color')                  
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST by CAR', 'Step 11.5: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 11.6: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 11.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 11.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label_list=['DEALER_COST', 'RETAIL_COST']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step : 11.9 Verify Legends ')
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", False, 'Step 11.10: Filter Button Removed')
        expected_datalabel=['108K', '56,500', '40,990', '35,800', '32,790', '11,033', '10,241', '9,392', '6,...', '5,...']
        resobj.verify_data_labels('MAINTABLE_wbody0', expected_datalabel, 'Step 11.5: Verify datalabels ', data_label_length=1,custom_css=".chartPanel text[class^='stackTotalLabel']") 
        time.sleep(5)
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step_11', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)

        """
            Step 12:Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()
                
 
