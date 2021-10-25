'''
Created on Sep 14, 2017

@author: Pavithra

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10670&group_by=cases:section_id&group_id=168200&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2312996
TestCase Name = AHTML: StreamGraph Basic chart Active Controls.
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon,visualization_resultarea,active_miscelaneous,ia_resultarea,active_chart_rollup
from common.lib import utillity

class C2312996_TestClass(BaseTestCase):

    def test_C2312996(self):
        
        Test_Case_ID="C2312996"
        """
            TESTCASE VARIABLES
        """     
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(15) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        rollupobj=active_chart_rollup.Active_Chart_Rollup(self.driver)
        
        """
            Step 01:Open FEX:http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10670%2FStreamBasic.fex&tool=Chart
                    Click the Run button.
    
            Expect to see the following Active Streamgraph.
        """
        utillobj.infoassist_api_edit("StreamBasic", 'chart', 'P116/S10670', mrid='mrid', mrpass='mrpass')
        parent_css="#pfjTableChart_1 g.chartPanel"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
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
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step : 01.9: Verify Legends ')
        time.sleep(5)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(5)
        element= driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(element, Test_Case_ID+"Base_Step_01")
        time.sleep(1)
  
        """
            Step 02:Using the first icon in the Active Tool bar, select the Chart/Rollup Tool.
      
            Expect to see the following Chart/Rollup Chart options menu.
        """
        utillobj.switch_to_frame(pause=2)
        rollupobj.select_chartmenubar_option('MAINTABLE_wmenu0',0,'Chart/Rollup Tool',0,custom_css='cpop')
        time.sleep(3)
        parent_css="#wall1"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        element= driver.find_element_by_css_selector("#wall1")
        utillobj.take_screenshot(element, Test_Case_ID+"Base_Step_02")
        time.sleep(1)
          
        """
            Step 03:Select the Column option.
                    Click OK.
              
            Expect to see the following Vertical Bar Chart.
        """
        rollupobj.select_advance_chart('wall1', 'column')
        time.sleep(3)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR", "Step 03.1: Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K','60K','70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 03.2: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 03.3: Verify Number of riser')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", "bar_blue1", "Step 03.4: Verify  bar color")
        expected_label_list=['DEALER_COST', 'RETAIL_COST']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step : 03.5: Verify Legends')      
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST by CAR', 'Step 03.6: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03.7: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
  
        """
            Step 04:Using the third icon in the Active Tool bar, click Original Chart.
                      
            Expect to see the original Streamgraph.
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 2)
        time.sleep(3)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 04.1: Verify X-Axis Title")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=[]
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 04.2: Verify XY Label')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 04 .3: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!marea', 'bar_blue1', 'Step 04.4: Verify Color')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST by CAR', 'Step 04.5: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04.6: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label_list=['DEALER_COST', 'RETAIL_COST']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step : 04.9: Verify Legends ')
        time.sleep(5)
          
  
        """
            Step 05:Using the second icon in the Active Tool bar, select the Advanced Chart option.
              
            Expect to see the following Chart/Rollup Chart options menu.
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        parent_css="#wall1"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(3)
        element= driver.find_element_by_css_selector("#wall1")
        utillobj.take_screenshot(element, Test_Case_ID+"_Step_05")
  
        """
            Step 06:Select the Bar option.
                    Click OK.
            Expect to see the following Horizontal Bar Chart.
        """
        rollupobj.select_advance_chart('wall1', 'bar')
        time.sleep(3)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR", "Step 06.1: Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K','60K','70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 06.2: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 06.3: Verify Number of riser')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", "bar_blue1", "Step 06.4: Verify  bar color")
        expected_label_list=['DEALER_COST', 'RETAIL_COST']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step : 06.5: Verify Legends')      
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST by CAR', 'Step 06.6: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 06.7: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 06.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 06.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
  
        """
            Step 07:Using the second icon in the Active Tool bar, select the Advanced Chart option.
                    Scroll down and select the first PIE option.
                    Click OK.
            Expect to see following PIE charts, one for each Measure.
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        time.sleep(3)
        parent_css="#wall1"
        resobj.wait_for_property(parent_css, 1)
        rollupobj.select_advance_chart('wall1', 'piebevel')
        time.sleep(3)
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['DEALER_COST', 'RETAIL_COST'], "Step 07.1:",same_group=True)
        expected_label_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 07.2: Verify pie lablesList')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mwedge!", "bar_blue1", "Step 07.3: Verify first bar color")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST by CAR', 'Step 07.5: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 07.6: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 07.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 07.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)       
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 20, "Step 07.9: Verify number of pie", custom_css=".chartPanel path[class*='riser!']")
          
        """
            Step 08:Using the second icon in the Active Tool bar, select the Advanced Chart option.
                    Scroll down and select the first Line chart option.
                    Click OK.
            Expect to see the following Line chart.
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        time.sleep(3)
        parent_css="#wall1"
        resobj.wait_for_property(parent_css, 1)
        rollupobj.select_advance_chart('wall1', 'line')
        time.sleep(3)
        expected_label_list=['DEALER_COST', 'RETAIL_COST']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step : 08.1: Verify Legends')  
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K','60K','70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 08.2: Verify XY labels")
        utillobj.verify_chart_color("MAINTABLE_wbody0", 'riser!s0!g0!mline!', 'bar_blue1', 'Step 08.3: Verify Color', attribute_type='stroke')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST by CAR', 'Step 08.4: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 08.5: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 08.6: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 08.7: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)       
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 22, "Step 08.8: Verify number of line ")
        time.sleep(5)
  
        """
            Step 09:Using the third icon in the Active Tool bar, click Original Chart.
              
            Expect to see the original Streamgraph.
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 2)
        time.sleep(3)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 09.1: Verify X-Axis Title")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=[]
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 09.2: Verify XY Label')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 09.3: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!marea', 'bar_blue1', 'Step 09.4: Verify Color')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST by CAR', 'Step 09.5: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 09.6: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 09.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 09.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label_list=['DEALER_COST', 'RETAIL_COST']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step : 09.9: Verify Legends ')
        time.sleep(5)
        time.sleep(5)

        """
            Step 10:Using the first icon in the Active Tool bar, select the Export To Excel option.
                    Click OK to any Excel/ActiveX messages.
            Expect to see the following Export To Excel option.
            
            Step 11:Open the Excel file.Expect to see the Excel content of a report and a chart.
        """
        browser=utillobj.parseinitfile('browser')
        if browser=='IE' :
            rollupobj.select_chartmenubar_option('MAINTABLE_wmenu0',0,'Export to->Excel',0,custom_css='cpop')
            time.sleep(8)
            utillobj.take_monitor_screenshot(Test_Case_ID+'_Actual_Step_02','actual', left=0, top=0, right=0, bottom=40)
            utillobj.saveas_excel_sheet(Test_Case_ID+'_DS11_.xlsx')
            time.sleep(4)
            utillobj.verify_excel_sheet(Test_Case_ID+'_DS11_.xlsx', Test_Case_ID+'_DS11_.xlsx', 'Sheet1', 'Step 10: Expect to see the Excel spreadsheet')
        else :
            print("Export option available only in IE browser")
   
        """
            Step 12:Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main() 