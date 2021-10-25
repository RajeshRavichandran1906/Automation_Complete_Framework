'''
Created on July 27, 2017

@author: Pavithra

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2204972
TestCase Name = Chart Rollup using a Datetime field by an Alphanumeric field.
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, active_miscelaneous, ia_resultarea, active_chart_rollup, ia_run
from common.lib import utillity


class C2204972_TestClass(BaseTestCase):

    def test_C2204972(self):
        
        Test_Case_ID="C2204972"
         
        """            
        TESTCASE VARIABLES
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(driver)
        rollupobj =active_chart_rollup.Active_Chart_Rollup(driver)
        ia_runobj=ia_run.IA_Run(driver) 
  
        """ 
            Step 01: Execute attached AR-RP-141CA.fex
        """
        utillobj.active_run_fex_api_login("AR-RP-141CA.fex", "S7074", 'mrid', 'mrpass')
        parent_css="#MAINTABLE_wbody0 .arGrid [id^='TCOL']"
        utillobj.synchronize_with_number_of_element(parent_css, 8, 30)
        
        miscelaneous_obj.verify_page_summary(0,'1000of1000records,Page1of18', 'Step 01.1: Verify Page summary')
#         ia_runobj.create_table_data_set("table[id='ITableData0']", Test_Case_ID+"_Ds01.xlsx")
        column_list=['Order Number INTEGER', 'ALPHA Store Code', 'Date YYMD', 'Date MDYY', 'Date DMYY', 'D10.2 Unit Price', 'P9.2M Unit Price', 'DATETIME HYYMDSA']
        miscelaneous_obj.verify_column_heading('ITableData0', column_list, 'Step 01.2 : Verify the column heading')
        time.sleep(2)
        
        """ 
            Step 02: Select Datetime HYYMDSA, ROLLUP, then ALPHA Store Code as the rollup column.      
        """
        miscelaneous_obj.select_menu_items('ITableData0',7,'Rollup','ALPHA Store Code')
        parent_css="#wall1 span[id='wtitle1']"
        #resobj.wait_for_property(parent_css, 1,string_value='DATETIMEHYYMDSAbyALPHAStoreCode',with_regular_exprestion=True)
        utillobj.synchronize_with_visble_text(parent_css, 'DATETIMEHYYMDSAbyALPHAStoreCode', 25)
        miscelaneous_obj.verify_popup_title('wall1','DATETIME HYYMDSA by ALPHA Store Code','Step 02.1 : Verify popup title')
        
        """ 
            Step 03: Expect to see a 12 line report with one row for each unique ALPHA Store Code value. 
                     Use these Count values to verify the data on the Pie, Bar, Line & Scatter graphs.
        """
        miscelaneous_obj.verify_page_summary(1,'12of12records,Page1of1','Step 3.1 : Verify page summary')
#         ia_runobj.create_table_data_set("#wall1 #ITableData1", Test_Case_ID+"_Ds02.xlsx")
        ia_runobj.verify_table_data_set('#wall1 #ITableData1', Test_Case_ID+'_Ds02.xlsx','Step 3.2 : Verify expect to see a 12 line report with one row for each unique D10.2 Unit Price value')
        miscelaneous_obj.verify_arChartToolbar('wall1', ['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Rollup', 'Advanced Chart', 'Original Chart'],"Step 3.3 : Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('wall1', ['Aggregation'],"Step 3.4 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('wall1', ['Count'],"Step 3.5 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)  
        utillobj.verify_object_visible("#wall1 .arChartMenuBar div[onclick*='toggleFiltLink']", True, 'Step 3.6 Verify chart rollup lock icon')        
#         
        
        """ 
            step 04: Switch from the ROLLUP report to a BAR Chart by selecting the second option from the tool bar.
        """
        rollupobj.click_chart_menu_bar_items('wall1',1)
        time.sleep(3)
        miscelaneous_obj.verify_chart_title('wbody1_ft','DATETIME HYYMDSA by ALPHA Store Code','Step 4.1 : Verify chart title')
        expected_xval_list=['R1019','R1020','R1040','R1041','R1044','R1088','R1100','R1109','R1200','R1244','R1248','R1250']
        expected_yval_list=['0','20', '40','60', '80', '100']
        resobj.verify_riser_chart_XY_labels('wbody1_f', expected_xval_list, expected_yval_list,'Step 4.2 :')
        resobj.verify_riser_legends('wbody1_f',['DATETIME HYYMDSA'],'Step 4.3 : Verify chart legend label')
        resobj.verify_number_of_riser('wbody1_f',1,12,'Step 4.4 : Verify number of chart risers')
        utillobj.verify_chart_color('wbody1_f','riser!s0!g5!mbar','cerulean_blue_1','Step 4.5 : Verify chart riser color')
        
        ele=driver.find_element_by_css_selector("#wall1")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step_4', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """ 
            Step 05: Switch from the BAR Chart to a PIE Chart by selecting the third option in the tool bar.
        """
        rollupobj.click_chart_menu_bar_items('wall1',2)
        time.sleep(4)
        miscelaneous_obj.verify_chart_title('wbody1_ft','DATETIME HYYMDSA by ALPHA Store Code','Step 5.1 : Verify chart title')
        expected_datalabel=['9%', '9%', '9%', '9%', '9%', '9%', '9%', '8%', '8%', '8%', '15%']
        resobj.verify_data_labels('wbody1_f', expected_datalabel, 'Step 5.2 : verify data_label', custom_css=".chartPanel text[class^='dataLabels']")
        resobj.verify_riser_legends('wbody1_f',['R1019','R1020','R1040','R1041','R1044','R1088','R1100','R1109','R1200','R1244','Other'],'Step 5.3 : Verify chart legend label')
        resobj.verify_riser_pie_labels_and_legends('wbody1_f', ['DATETIME HYYMDSA'], "Step 5.4:",custom_css="text[class*='pieLabel']",same_group=True)
        ia_resultobj.verify_number_of_chart_segment('wbody1_f',11,'Step 5.5 : Verify number of chart risers')
        utillobj.verify_chart_color('wbody1_f','riser!s0!g0!mwedge','cerulean_blue_1','Step 5.6 : Verify chart riser color')
        
        ele=driver.find_element_by_css_selector("#wall1")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step_5', image_type='actual',x=1, y=1, w=-1, h=-1)
#         
        """
            Step 06: Switch from the PIE Chart to a Line Graph by selecting the fourth option from the tool bar.
        """
        rollupobj.click_chart_menu_bar_items('wall1',3)
        time.sleep(4)
        miscelaneous_obj.verify_chart_title('wbody1_ft','DATETIME HYYMDSA by ALPHA Store Code','Step 6.1 : Verify chart title')
        expected_xval_list=['R1019','R1020','R1040','R1041','R1044', 'R1088', 'R1100', 'R1109', 'R1200', 'R1244', 'R1248', 'R1250']
        expected_yval_list=['0','20', '40','60', '80', '100']
        resobj.verify_riser_chart_XY_labels('wbody1_f', expected_xval_list, expected_yval_list,'Step 6.2 :')
        resobj.verify_riser_legends('wbody1_f',['DATETIME HYYMDSA'],'Step 6.3 : Verify chart legend label')
        ia_resultobj.verify_number_of_chart_segment('wbody1_f',13,'Step 6.4 : Verify number of chart risers')
        utillobj.verify_chart_color('wbody1_f','riser!s0!g0!mline!','cerulean_blue_1','Step 6.5 : Verify chart riser color',attribute_type='stroke')
        
        ele=driver.find_element_by_css_selector("#wall1")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step_6', image_type='actual',x=1, y=1, w=-1, h=-1)
            
        """ 
            Step 07: Switch from the LINE Graph to a SCATTER Diagram by selecting the fifth option from the tool bar.
        """
        rollupobj.click_chart_menu_bar_items('wall1',4)
        time.sleep(4)
        miscelaneous_obj.verify_chart_title('wbody1_ft','DATETIME HYYMDSA by ALPHA Store Code','Step 7.1 : Verify chart title')
        expected_xval_list=['R1019','R1020','R1040','R1041','R1044','R1088','R1100','R1109','R1200','R1244','R1248','R1250']
        expected_yval_list=['0','20', '40','60', '80', '100']
        resobj.verify_riser_chart_XY_labels('wbody1_f', expected_xval_list, expected_yval_list,'Step 7.2 :')
        resobj.verify_riser_legends('wbody1_f',['DATETIME HYYMDSA'],'Step 7.3 : Verify chart legend label')
        ia_resultobj.verify_number_of_chart_segment('wbody1_f',12,'Step 7.4 : Verify number of chart risers')
        utillobj.verify_chart_color('wbody1_f','riser!s0!g0!mmarker','cerulean_blue_1','Step 7.5 : Verify chart riser color',attribute_type='stroke')
        
        total_summation=len(driver.find_elements_by_css_selector("#dt0_SUM_1_0 [id^='t0_SUM_1_0']"))
        utillobj.asequal(0,total_summation,'Step 7.7 : Verify No summation options are available for scatter diagram')
        ele=driver.find_element_by_css_selector("#wall1")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step_7', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """ 
            Step 08:Switch from the Scatter diagram back to the Rollup Report by using the first icon and select RESTORE ORIGINAL. 
                    Select the last icon labeled Count. The only option that will change the report is Distinct, 
                    as the graphs represent Counts and not Sums that can accept Min, Max, etc.
        """
        rollupobj.select_chartmenubar_option('wall1',1,'Restore Original',0,custom_css='cpop')
        time.sleep(2)
        summation=['Sum','Avg','Min','Max','Count','Distinct']
        for i in range(len(summation)) :
            if i < 4:
                rollupobj.select_aggregate_function('wall1', 1,summation[i],verify=False)
            else:
                rollupobj.select_aggregate_function('wall1', 1,summation[i])
            time.sleep(2)
            miscelaneous_obj.verify_page_summary(1,'12of12records,Page1of1','Step 8.'+str(i+1)+': Verify page summary')
#             ia_runobj.create_table_data_set("#wall1 #ITableData1", Test_Case_ID+'_'+summation[i]+'_Ds.xlsx')
            ia_runobj.verify_table_data_set('#wall1 #ITableData1', Test_Case_ID+'_'+summation[i]+'_Ds.xlsx','Step 8.'+str(i+1)+': Verify expect to see the report to reflect '+summation[i])
        time.sleep(2)
        miscelaneous_obj.close_popup_dialog('1')
        time.sleep(3)
        
        
if __name__ == '__main__':
    unittest.main()