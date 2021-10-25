'''
Created on Oct 12, 2017

@author: Pavithra

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10670&group_by=cases:section_id&group_id=168200&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2313415
TestCase Name = AHTML: Mekko chart Basic chart Active Controls.
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon,visualization_resultarea,active_miscelaneous,active_chart_rollup,ia_resultarea
from common.lib import utillity

class C2313415_TestClass(BaseTestCase):

    def test_C2313415(self):
        
        Test_Case_ID="C2313415"
        
        """
            TESTCASE VARIABLES
        """     
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        rollupobj=active_chart_rollup.Active_Chart_Rollup(self.driver)
        
        """      
            Step 01:Open FEX:
                    http://machine:port/ibiapps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10670%2FMekkoBucketizedCharts%2FMekkoBasic.fex&tool=Chart
        """
        utillobj.infoassist_api_edit("Mekko_Basic", 'chart', 'P116/S10670', mrid='mrid', mrpass='mrpass')
        parent_css="#pfjTableChart_1 g.chartPanel"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(8)
 
        """
            Step 02:Click the Run button.
            
            Expect to see the following Active Mekko Chart.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 02.01: Verify X-Axis Title")
        expected_xval_list=['BMW', 'MASERATI', 'JAGUAR', 'ALFA ROMEO', 'JENSEN', 'AUDI', 'PEU...', 'TRI...', 'T...', 'D...']
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 02.02: Verify XY Label',  x_axis_label_length=1)
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 02.03: Verify the total number of risers displayed on run')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g2!mbar!', 'bar_blue1', 'Step 02.04: Verify Color')                  
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST by CAR', 'Step 02.05: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 02.06: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02.07: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02.08: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label_list=['DEALER_COST', 'RETAIL_COST']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step : 02.09 Verify Legends ')       
        expected_datalabel=['108K', '56,500', '40,990', '35,800', '32,790', '11,033', '10,241', '9,392', '6,...', '5,...']
        resobj.verify_data_labels('MAINTABLE_wbody0', expected_datalabel, 'Step 02.10: Verify datalabels ',data_label_length=1, custom_css=".chartPanel text[class^='stackTotalLabel']") 
 
        """
            Step 03:Using the first icon in the Active Tool bar, select the Chart/Rollup Tool.
             
            Expect to see the following Chart/Rollup Chart options menu.
        """
        rollupobj.select_chartmenubar_option('MAINTABLE_wmenu0',0,'Chart/Rollup Tool',0,custom_css='cpop')
        time.sleep(3)
        parent_css="#wall1"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(5)
 
        """
            Step 04:Select the Column option.
                    Click OK.
            Expect to see the following Vertical Bar Chart.
        """
        rollupobj.select_advance_chart('wall1', 'column')
        time.sleep(3)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR", "Step 04.01: Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K','60K','70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 04.02: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 04.03: Verify Number of riser')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", "bar_blue1", "Step 04.04: Verify  bar color")
        expected_label_list=['DEALER_COST', 'RETAIL_COST']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 04.05: Verify Legends')      
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST by CAR', 'Step 04.06: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04.07: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.08: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.09: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        """
            Step 05:Using the third icon in the Active Tool bar, click Original Chart.
            Expect to see the original Mekko Chart.
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 2)
        time.sleep(3)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 05.01: Verify X-Axis Title")
        expected_xval_list=['BMW', 'MASERATI', 'JAGUAR', 'ALFA ROMEO', 'JENSEN', 'AUDI', 'PEU...', 'TRI...', 'T...', 'D...']
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 05.02: Verify XY Label',  x_axis_label_length=1)
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 05.03: Verify the total number of risers displayed on run')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g2!mbar!', 'bar_blue1', 'Step 05.04: Verify Color')                  
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST by CAR', 'Step 05.05: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.06: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.07: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.08: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label_list=['DEALER_COST', 'RETAIL_COST']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step : 05.09 Verify Legends ')       
        expected_datalabel=['108K', '56,500', '40,990', '35,800', '32,790', '11,033', '10,241', '9,392', '6,...', '5,...']
        resobj.verify_data_labels('MAINTABLE_wbody0', expected_datalabel, 'Step 05.10: Verify datalabels ',data_label_length=1, custom_css=".chartPanel text[class^='stackTotalLabel']") 
          
        """
            Step 06:Using the second icon in the Active Tool bar, select the Advanced Chart option.            
            Expect to see the following Chart/Rollup Chart options menu.
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        parent_css="#wall1"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(3)
         
        """
            Step 07:Select the Bar option.
                    Click OK.
            Expect to see the following Horizontal Bar Chart.
        """
        rollupobj.select_advance_chart('wall1', 'bar')
        time.sleep(3)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR", "Step 07.01: Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K','60K','70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 07.02: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 07.03: Verify Number of riser')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", "bar_blue1", "Step 07.04: Verify  bar color")
        expected_label_list=['DEALER_COST', 'RETAIL_COST']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step : 07.05: Verify Legends')      
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST by CAR', 'Step 07.06: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 07.07: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 07.08: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 07.09: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)

        """
            Step 08:Using the second icon in the Active Tool bar, select the Advanced Chart option.
                    Scroll down and select the second PIE option,
                    PIE with Depth.
                    Click OK.

            Expect to see following PIE charts with Depth, one for each Measure.
        """
        time.sleep(8)
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        parent_css="#wall1"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(3)
        element= driver.find_element_by_css_selector("#wall1")
        utillobj.take_screenshot(element, Test_Case_ID+"_Step_05")
        time.sleep(3)
        rollupobj.select_advance_chart('wall1', 'piewithdepth')
        time.sleep(3)
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['DEALER_COST', 'RETAIL_COST'], "Step 08.01:",same_group=True)
        expected_label_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 08.02: Verify pie lablesList')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mwedge!", "bar_blue", "Step 08.03: Verify first bar color")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST by CAR', 'Step 08.04: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 08.05: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 08.06: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 08.07: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 104, "Step 08.08: Verify number of pie", custom_css=".chartPanel path[class*='riser!s']")

        """
            step 09:Using the second icon in the Active Tool bar, select the Advanced Chart option.
                    Scroll down and select the second Line chart option,Curved.
                    Click OK.
            Expect to see the following Curved Line chart.
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        time.sleep(3)
        rollupobj.select_advance_chart('wall1', 'curvedline')
        time.sleep(3)
        resobj.verify_xaxis_title('MAINTABLE_wbody0', 'CAR', 'Step 09.01: Verify X-axis title')
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K','60K','70K']
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 09.02: Verify XY labels')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 09.03: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue", "Step 09.04: Verify line1 color",attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mline!", "pale_green", "Step 09.05: Verify line2 color",attribute_type='stroke')
        expected_legend_list=['DEALER_COST','RETAIL_COST']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_legend_list, 'Step 09.06: Verify Legend Title')
        time.sleep(3)
        parent_elem=driver.find_element_by_css_selector("#MAINTABLE_wbody0")
        utillobj.click_on_screen(parent_elem, 'middle')
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class*='marker!s0!g2!mmarker!']")
        utillobj.click_on_screen(parent_elem, 'middle',javascript_marker_enable=True,mouse_duration=2.5)
        time.sleep(1)
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST by CAR', 'Step 09.07: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 09.08: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 09.09: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 09.10: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(3)

        """
            Step 10:Using the third icon in the Active Tool bar, click Original Chart.
            
            Expect to see the original Mekko Chart.
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 2)
        time.sleep(3)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 10.01: Verify X-Axis Title")
        expected_xval_list=['BMW', 'MASERATI', 'JAGUAR', 'ALFA ROMEO', 'JENSEN', 'AUDI', 'PEU...', 'TRI...', 'T...', 'D...']
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 10.02: Verify XY Label',  x_axis_label_length=1)
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 10.03: Verify the total number of risers displayed on run')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g2!mbar!', 'bar_blue1', 'Step 10.04: Verify Color')                  
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST by CAR', 'Step 10.05: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 10.06: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 10.07: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 10.08: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label_list=['DEALER_COST', 'RETAIL_COST']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step : 10.09 Verify Legends ')       
        expected_datalabel=['108K', '56,500', '40,990', '35,800', '32,790', '11,033', '10,241', '9,392', '6,...', '5,...']
        resobj.verify_data_labels('MAINTABLE_wbody0', expected_datalabel, 'Step 10.10: Verify datalabels ',data_label_length=1, custom_css=".chartPanel text[class^='stackTotalLabel']") 

        """
            Step 11:Using the first icon in the Active Tool bar, select the Export To Excel option.
                    Click OK to any Excel/ActiveX messages.
            
            Step 12:Open the Excel file.Expect to see the Excel content of a report and a chart.
        """
        browser=utillobj.parseinitfile('browser')
        if browser=='IE' :
            rollupobj.select_chartmenubar_option('MAINTABLE_wmenu0',0,'Export to->Excel',0,custom_css='cpop')
            time.sleep(60)
            utillobj.take_monitor_screenshot('C2204883_Actual_Step_02', image_type='actual', left=0, top=20, right=600, bottom=40)  
            utillobj.kill_process('EXCEL')
            time.sleep(2)
        else :
            print("Export option available only in IE browser")
        
        """
            Step 13: Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__=='__main__' :
    unittest.main()