'''
Created on Nov 21, 2017

@author: Praveen Ramkumar
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2334623
TestCase Name = AHTML: Advanced Chart Tool fails to convert Extension Charts.(ACT-1199)

'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea,active_miscelaneous,ia_resultarea,active_chart_rollup
from common.lib import utillity

class C2334623_TestClass(BaseTestCase):

    def test_C2334623(self):
        
        Test_Case_ID="C2334623"
        """
            TESTCASE VARIABLES
        """
        
        
        utillobj = utillity.UtillityMethods(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        rollupobj=active_chart_rollup.Active_Chart_Rollup(self.driver)
        
        """
        Step 01:Execute the attached repro - act-1199.fex.This will create an initial Bar Chart.
        Expect to see the following Arc chart.
        """
        
        utillobj.active_run_fex_api_login("act-1199.fex", "S7074", 'mrid', 'mrpass')
        parent_css="#MAINTABLE_wbody0_ft table tbody"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 60, 1)
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'RETAIL_COST BY CAR', 'Step 01.1: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 01.2: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 01.3: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 01.04: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_datalabel=['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K', '40K', '45K', '50K', '55K']
        resobj.verify_data_labels("MAINTABLE_wbody0_f", expected_datalabel,"Step 01.05: Verify Xlabels",custom_css=" g text.label")
        utillobj.verify_chart_color("MAINTABLE_wbody0", " riser!s0!g3!mbar!", "brick_red", "Step 01.06: Verify  riser color",custom_css=".chartPanel .group-main path[class*='riser']")#MAINTABLE_wbody0 .chartPanel .group-main path[class*='riser']
        
        expected_datalabel=['DATSUN', 'TOYOTA', 'TRIUMPH', 'PEUGEOT', 'AUDI', 'JENSEN','ALFA ROMEO','JAGUAR','MASERATI','BMW']
        resobj.verify_data_labels("MAINTABLE_wbody0", expected_datalabel,"Step 01.08: Verify Xlabels",custom_css=" g.group-labels text")
         
        """
        Step 02:From the Arc Chart, select the Advanced Chart tab, then Charts, then select Bar Column.
        Click OK.Expect to see the following Bar chart.
        """
          
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        time.sleep(3)
        rollupobj.select_advance_chart('wall1', 'column')
        time.sleep(3)
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'RETAIL_COST BY CAR', 'Step 02.1: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 02.2: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02.3: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02.04: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K','70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 02.5: Verify XY labels")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", "bar_blue", "Step 02.06: Verify  riser color")#MAINTABLE_wbody0 .chartPanel .group-main path[class*='riser'] ,custom_css=".chartPanel .group-main path[class*='riser']"
        
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 02.8: Verify X-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", 'RETAIL_COST', "Step 02.9: Verify X-Axis Title")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 10, 'Step 02.10: Verify the total number of risers displayed on preview')
          
          
        """
        Step 03:Click the Restore Original button.From the Arc Chart, select the Advanced Chart tab, then Charts, then select PIE chart.
        Click OK,Expect to see the following PIE chart.        
        """
          
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 2)
        time.sleep(3)
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'RETAIL_COST BY CAR', 'Step : Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step : Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_datalabel=['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K', '40K', '45K', '50K', '55K']
        resobj.verify_data_labels("MAINTABLE_wbody0_f", expected_datalabel,"Step : Verify Xlabels",custom_css=" g text.label")
        utillobj.verify_chart_color("MAINTABLE_wbody0", " riser!s0!g3!mbar!", "brick_red", "Step : Verify  riser color",custom_css=".chartPanel .group-main path[class*='riser']")#MAINTABLE_wbody0 .chartPanel .group-main path[class*='riser']
        
        expected_datalabel=['DATSUN', 'TOYOTA', 'TRIUMPH', 'PEUGEOT', 'AUDI', 'JENSEN','ALFA ROMEO','JAGUAR','MASERATI','BMW']
        resobj.verify_data_labels("MAINTABLE_wbody0", expected_datalabel,"Step : Verify Xlabels",custom_css=" g.group-labels text")
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        time.sleep(3)
        rollupobj.select_advance_chart('wall1', 'piebevel')
        time.sleep(3)
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0_ft","RETAIL_COST BY CAR", "Step 03.1 : Verify chart title ")
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s2!g0!mwedge!', 'dark_green', 'Step 03.2: Verify Color')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03.3: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.4: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.5: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 03.6: Verify Legends ')
        
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['RETAIL_COST'], "Step 03.8:",custom_css="text[class*='pieLabel']",same_group=True) 
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 10, "Step 03.9: Verify number of pie")
        expected_datalabel=['11%', '3%', '34%', '2%', '13%', '10%', '18%', '3%', '2%', '3%']
        resobj.verify_data_labels('MAINTABLE_wbody0', expected_datalabel, 'Step 03.10: Verify datalabels ',custom_css=".chartPanel text[class^='dataLabels']") 
          
          
        """
        Step 04:Click the Restore Original button.From the Arc Chart, select the Advanced Chart tab, then Charts, then select Line chart.
        Click OK.Expect to see the following Line chart.
        """
          
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 2)
        time.sleep(3)
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'RETAIL_COST BY CAR', 'Step : Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step : Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_datalabel=['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K', '40K', '45K', '50K', '55K']
        resobj.verify_data_labels("MAINTABLE_wbody0_f", expected_datalabel,"Step : Verify Xlabels",custom_css=" g text.label")
        utillobj.verify_chart_color("MAINTABLE_wbody0", " riser!s0!g3!mbar!", "brick_red", "Step : Verify  riser color",custom_css=".chartPanel .group-main path[class*='riser']")#MAINTABLE_wbody0 .chartPanel .group-main path[class*='riser']
        
        expected_datalabel=['DATSUN', 'TOYOTA', 'TRIUMPH', 'PEUGEOT', 'AUDI', 'JENSEN','ALFA ROMEO','JAGUAR','MASERATI','BMW']
        resobj.verify_data_labels("MAINTABLE_wbody0", expected_datalabel,"Step : Verify Xlabels",custom_css=" g.group-labels text")
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        time.sleep(3)
        rollupobj.select_advance_chart('wall1', 'line')
        time.sleep(3)
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0_ft","RETAIL_COST BY CAR", "Step 04.1 : Verify chart title ")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04.2: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.3: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.4: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K','70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 04.6: Verify XY labels")
        
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 04.6: Verify X-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", 'RETAIL_COST', "Step 04.7: Verify X-Axis Title")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 11, 'Step 04.8: Verify Number of riser')
          
        """
        Step 05:Click the Restore Original button.From the Arc Chart, select the Advanced Chart tab, then Charts, then select Area chart.
        Expect to see the following Area chart.
        """
          
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 2)
        time.sleep(3)
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'RETAIL_COST BY CAR', 'Step : Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step : Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_datalabel=['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K', '40K', '45K', '50K', '55K']
        resobj.verify_data_labels("MAINTABLE_wbody0_f", expected_datalabel,"Step : Verify Xlabels",custom_css=" g text.label")
        utillobj.verify_chart_color("MAINTABLE_wbody0", " riser!s0!g3!mbar!", "brick_red", "Step : Verify  riser color",custom_css=".chartPanel .group-main path[class*='riser']")#MAINTABLE_wbody0 .chartPanel .group-main path[class*='riser']
        
        expected_datalabel=['DATSUN', 'TOYOTA', 'TRIUMPH', 'PEUGEOT', 'AUDI', 'JENSEN','ALFA ROMEO','JAGUAR','MASERATI','BMW']
        resobj.verify_data_labels("MAINTABLE_wbody0", expected_datalabel,"Step : Verify Xlabels",custom_css=" g.group-labels text")
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        time.sleep(3)
        rollupobj.select_advance_chart('wall1', 'area')
        time.sleep(3)
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0_ft","RETAIL_COST BY CAR", "Step 05.1 : Verify chart title ")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.2: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.3: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.4: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K','70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 05.5: Verify XY labels")
        
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 05.7: Verify X-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", 'RETAIL_COST', "Step 05.8: Verify X-Axis Title")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0',11, 'Step 05.9: Verify Number of riser')
          
        """
        Step 06:Click the Restore Original button.From the Arc Chart, select the Advanced Chart tab, then Charts, then select Scatter chart.
        Expect to see the following Scatter chart.
        """
        
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 2)
        time.sleep(3)
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'RETAIL_COST BY CAR', 'Step : Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step : Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_datalabel=['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K', '40K', '45K', '50K', '55K']
        resobj.verify_data_labels("MAINTABLE_wbody0_f", expected_datalabel,"Step : Verify Xlabels",custom_css=" g text.label")
        utillobj.verify_chart_color("MAINTABLE_wbody0", " riser!s0!g3!mbar!", "brick_red", "Step : Verify  riser color",custom_css=".chartPanel .group-main path[class*='riser']")#MAINTABLE_wbody0 .chartPanel .group-main path[class*='riser']
        
        expected_datalabel=['DATSUN', 'TOYOTA', 'TRIUMPH', 'PEUGEOT', 'AUDI', 'JENSEN','ALFA ROMEO','JAGUAR','MASERATI','BMW']
        resobj.verify_data_labels("MAINTABLE_wbody0", expected_datalabel,"Step : Verify Xlabels",custom_css=" g.group-labels text")
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        time.sleep(3)
        rollupobj.select_advance_chart('wall1', 'scatter(xy_plot)')
        time.sleep(3)
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0_ft","RETAIL_COST BY CAR", "Step 06.1 : Verify chart title ")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 06.2: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 06.3: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 06.4: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K','70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 06.5: Verify XY labels")
        
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 06.7: Verify X-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", 'RETAIL_COST', "Step 06.8: Verify X-Axis Title")
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g2!mmarker!', 'bar_blue', 'Step 06.9: Verify Color',attribute_type='stroke')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0',10, 'Step 06.10: Verify Number of riser')
        
        element= self.driver.find_element_by_css_selector("#MAINTABLE_wbody0")
        utillobj.take_screenshot(element, Test_Case_ID+"_Step_6")
        time.sleep(1)
if __name__ == '__main__':
    unittest.main()