'''
Created on July 20, 2017

@author: Nasir

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2204953
TestCase Name = Chart Rollup using a Numeric field by an Alphanumeric field.

'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea,active_miscelaneous,active_chart_rollup,ia_resultarea,ia_run
from common.lib import utillity

class C2204968_TestClass(BaseTestCase):

    def test_C2204968(self):
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID="C2204968"
        driver = self.driver #Driver reference object created
        
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        iarun=ia_run.IA_Run(driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(driver)
        rollupobj =active_chart_rollup.Active_Chart_Rollup(driver)
        iaresult=ia_resultarea.IA_Resultarea(driver)
        fun=['Sum','Avg','Min','Max','Count','Distinct']
        
        def verify_bar_chart(yaxis_list,tooltip_value,step_num):
            time.sleep(4)
            miscelaneous_obj.verify_chart_title('wbody1_ft','D10.2 Unit Price BY ALPHA Store Code','Step '+step_num+'.1 : Verify chart title')
            expected_xval_list=['R1019','R1020','R1040','R1041','R1044','R1088','R1100','R1109','R1200','R1244','R1248','R1250']
            expected_yval_list=yaxis_list
            result_obj.verify_riser_chart_XY_labels('wbody1_f', expected_xval_list, expected_yval_list,'Step '+step_num+'.2 :')
            result_obj.verify_riser_legends('wbody1_f',['D10.2 Unit Price'],'Step '+step_num+'.3 : Verify chart legend label')
            result_obj.verify_number_of_riser('wbody1_f',1,12,step_num+'.4 : Verify number of chart risers')
            utillobj.verify_chart_color('wbody1_f','riser!s0!g5!mbar!','cerulean_blue_1','Step '+step_num+'.5 : Verify chart riser color')
            miscelaneous_obj.verify_active_chart_tooltip('wbody1_f','riser!s0!g5!mbar!',tooltip_value,'Step '+step_num+'.6 : Verify chart tooltip value')
            ele=driver.find_element_by_css_selector("#wall1")
            utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step_'+step_num, image_type='actual',x=1, y=1, w=-1, h=-1)
            time.sleep(8)
        def verify_pie_chart(tooltip_value,expected_data_label,legend_label,step_num):
            parent_css="#wall1 g.chartPanel g text"
            result_obj.wait_for_property(parent_css, 12)
            miscelaneous_obj.verify_chart_title('wbody1_ft','D10.2 Unit Price BY ALPHA Store Code','Step '+step_num+'.1 : Verify chart title')
            expected_legend_label=legend_label
            result_obj.verify_riser_legends('wbody1_f',expected_legend_label,'Step '+step_num+'.2 : Verify chart legend label')
            iaresult.verify_number_of_chart_segment('wbody1_f', 11,'Step '+step_num+'.3 : Verify number of chart risers')
            result_obj.verify_data_labels('wbody1_f',expected_data_label, 'Step '+step_num+'.4 : Verify pie chart data labels',custom_css=".chartPanel text[class^='dataLabels']")
            result_obj.verify_riser_pie_labels_and_legends('wbody1_f',['D10.2 Unit Price'],'Step '+step_num+'.4 : ',same_group=True)
            utillobj.verify_chart_color('wbody1_f','riser!s5!g0!mwedge!','milky_blue','Step '+step_num+'.5 : Verify chart riser color')
            miscelaneous_obj.verify_active_chart_tooltip('wbody1_f','riser!s5!g0!mwedge!',tooltip_value,'Step '+step_num+'.6 : Verify chart tooltip value')
            ele=driver.find_element_by_css_selector("#wall1")
            utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step_'+step_num, image_type='actual',x=1, y=1, w=-1, h=-1)
            time.sleep(8)
        def verify_line_chart(yaxis_list,tooltip_value,step_num):
            time.sleep(4)
            miscelaneous_obj.verify_chart_title('wbody1_ft','D10.2 Unit Price BY ALPHA Store Code','Step '+step_num+'.1 : Verify chart title')
            expected_xval_list=['R1019','R1020','R1040','R1041','R1044','R1088','R1100','R1109','R1200','R1244','R1248','R1250']
            expected_yval_list=yaxis_list
            result_obj.verify_riser_chart_XY_labels('wbody1_f', expected_xval_list, expected_yval_list,'Step '+step_num+'.2 :')
            iaresult.verify_number_of_chart_segment('wbody1_f', 13,'Step '+step_num+'.3 : Verify number of chart risers')
            result_obj.verify_riser_legends('wbody1_f',['D10.2 Unit Price'],'Step '+step_num+'.4 : Verify chart legend label')
            utillobj.verify_chart_color('wbody1_f','riser!s0!g0!mline!','cerulean_blue_1','Step '+step_num+'.5 : Verify chart riser color',attribute_type='stroke')
            miscelaneous_obj.verify_active_chart_tooltip('wbody1_f','marker!s0!g5!mmarker!',tooltip_value,'Step '+step_num+'.6 : Verify chart tooltip value')
            ele=driver.find_element_by_css_selector("#wall1")
            utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step_'+step_num, image_type='actual',x=1, y=1, w=-1, h=-1) 
            time.sleep(8)
        """
        Step 01:Execute attached AR-RP-141CA.fex
        """
        utillobj.active_run_fex_api_login('AR-RP-141CA.fex', "S7074", 'mrid', 'mrpass')
        parent_css="#MAINTABLE_wbody0 .arGrid [id^='TCOL']"
        utillobj.synchronize_with_number_of_element(parent_css, 8, 65)
        
        miscelaneous_obj.verify_page_summary(0,'1000of1000records,Page1of18','Step 01.1 : Verify page summary')
        column_list=['Order Number INTEGER', 'ALPHA Store Code', 'Date YYMD', 'Date MDYY', 'Date DMYY', 'D10.2 Unit Price', 'P9.2M Unit Price', 'DATETIME HYYMDSA']
        miscelaneous_obj.verify_column_heading('ITableData0', column_list, 'Step 01.2 : Verify the column heading')
        #iarun.verify_table_data_set('#MAINTABLE_wbody0 #ITableData0',Test_Case_ID+'_Ds_01.xlsx','Step 01.2 : Verify data set')
        
        """
        Step 02 : Select D10.2 Unit Price, ROLLUP, then ALPHA Store Code as the rollup column.
        """
        miscelaneous_obj.select_menu_items('ITableData0',5,'Rollup','ALPHA Store Code')
        parent_css="#wall1 #wtitle1"
        utillobj.synchronize_with_visble_text(parent_css, 'D10.2 Unit Price BY ALPHA Store Code', 40)
        miscelaneous_obj.verify_popup_title('wall1','D10.2 Unit Price BY ALPHA Store Code','Step 02.1 : Verify popup title')
        
        """
        Step 02.1 : Expect to see a 12 line report with one row for each unique ALPHA Store Code value
        """
        miscelaneous_obj.verify_page_summary(1,'12of12records,Page1of1','Step 02.3 : Verify page summary')
        iarun.verify_table_data_set('#wall1 #ITableData1', Test_Case_ID+'_Sum_Ds.xlsx','Step 02.4 : Verify expect to see a 12 line report with one row for each unique ALPHA Store Code value')
        miscelaneous_obj.verify_arChartToolbar('wall1', ['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Rollup', 'Advanced Chart', 'Original Chart'],"Step 02.5 : Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('wall1', ['Aggregation'],"Step 02.6 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('wall1', ['Sum'],"Step 02.7 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)  
        utillobj.verify_object_visible("#wall1 .arChartMenuBarContainer [id^='LINKIMG'] img",True,'Step 02.8 : Verify Rollup chart lock icon')
          
        
        """
        Step 03.0 : Switch from the ROLLUP report to a BAR Chart by selecting the second option from the tool bar. 
        Then select the last icon and change SUM to AVG, MIN, MAX, COUNT & DISTINCT. Switch back to SUM for the next step.
        """
        rollupobj.click_chart_menu_bar_items('wall1',1)
        bar_yaxis={'Sum':['0','1000','2000','3000','4000','5000','6000'],'Avg':['0','10','20','30','40','50','60'],'Min':['0','4','8','12','16'],
                   'Max':['0','40','80','120','160','200'],'Count':['0','20','40','60','80','100'],'Distinct':['0','2','4','6','8','10','12']}
          
        bar_tooltip={'Sum':['D10.2 Unit Price: 5,358', 'X: R1088'],'Avg':['D10.2 Unit Price: 59.5', 'X: R1088'],'Min':['D10.2 Unit Price: 13', 'X: R1088'],
                   'Max':['D10.2 Unit Price: 140', 'X: R1088'],'Count':['D10.2 Unit Price: 90', 'X: R1088'],'Distinct':['D10.2 Unit Price: 1', 'X: R1088']}
        for i in range(len(fun)) :
            print("----------------"+fun[i]+" Function for Bar chart------------")
            rollupobj.select_aggregate_function('wall1', 1,fun[i])
            verify_bar_chart(bar_yaxis[fun[i]],bar_tooltip[fun[i]],'03.'+str(i))
           
        """
        Step 04.0 : Switch from the BAR Chart to a PIE Chart by selecting the third option in the tool bar. Check the other Summation options as stated in Step 2.
        """
        rollupobj.click_chart_menu_bar_items('wall1',2)
        pie_tooltip={'Sum':['R1088', 'D10.2 Unit Price: 5,358', '9.0% of 59,503'],'Avg':['R1088', 'D10.2 Unit Price: 59.5', '8.3% of 714.2'],'Min':['R1088', 'D10.2 Unit Price: 13', '8.3% of 156'],
                   'Max':['R1088', 'D10.2 Unit Price: 140', '8.3% of 1,680'],'Count':['R1088', 'D10.2 Unit Price: 90', '9.0% of 1,000'],'Distinct':['R1088', 'D10.2 Unit Price: 1', '4.5% of 22']}
         
        data_label={'Sum':['9%', '9%', '9%', '9%', '9%', '9%', '9%', '8%', '8%', '8%', '15%'],'Avg':['8%', '8%', '8%', '8%', '8%', '9%', '8%', '8%', '8%', '8%', '16%'],'Min':['8%', '8%', '8%', '8%', '8%', '8%', '8%', '8%', '8%', '8%', '17%'],
                   'Max':['8%', '8%', '8%', '8%', '8%', '8%', '8%', '8%', '8%', '8%', '17%'],'Count':['9%', '9%', '9%', '9%', '9%', '9%', '9%', '8%', '8%', '8%', '15%'],'Distinct':['45%', '5%', '9%', '5%', '5%', '5%', '5%', '5%', '5%', '5%', '9%']}
         
        legend_label={'Sum':['R1019', 'R1020', 'R1040', 'R1041', 'R1044', 'R1088', 'R1100', 'R1109', 'R1244', 'R1248', 'Other'],'Avg':['R1019', 'R1040', 'R1041', 'R1044', 'R1088', 'R1100', 'R1109', 'R1200', 'R1244', 'R1248', 'Other'],'Min':['R1019', 'R1020', 'R1040', 'R1041', 'R1044', 'R1088', 'R1100', 'R1109', 'R1200', 'R1244', 'Other'],
                   'Max':['R1019', 'R1020', 'R1040', 'R1041', 'R1044', 'R1088', 'R1100', 'R1109', 'R1200', 'R1244', 'Other'],'Count':['R1019', 'R1020', 'R1040', 'R1041', 'R1044', 'R1088', 'R1100', 'R1109', 'R1200', 'R1244', 'Other'],'Distinct':['R1019', 'R1020', 'R1040', 'R1041', 'R1044', 'R1088', 'R1100', 'R1109', 'R1200', 'R1244', 'Other']}
        for i in range(len(fun)) :
            print("----------------"+fun[i]+" Function for Pie chart------------")
            rollupobj.select_aggregate_function('wall1', 1,fun[i])
            verify_pie_chart(pie_tooltip[fun[i]],data_label[fun[i]],legend_label[fun[i]],'04.'+str(i))
            
        """
        Step 05.0 : Switch from the PIE Chart to a Line Graph by selecting the fourth option from the tool bar. 
        Then select the last icon and change SUM to AVG, MIN, MAX, COUNT & DISTINCT.
        """
        rollupobj.click_chart_menu_bar_items('wall1',3)
        line_yaxis={'Sum':['0','1000','2000','3000','4000','5000','6000'],'Avg':['0','10','20','30','40','50','60'],'Min':['0','4','8','12','16'],
                   'Max':['0','40','80','120','160','200'],'Count':['0','20','40','60','80','100'],'Distinct':['0','2','4','6','8','10','12']}
          
        line_tooltip={'Sum':['D10.2 Unit Price: 5,358', 'X: R1088'],'Avg':['D10.2 Unit Price: 59.5', 'X: R1088'],'Min':['D10.2 Unit Price: 13', 'X: R1088'],
                   'Max':['D10.2 Unit Price: 140', 'X: R1088'],'Count':['D10.2 Unit Price: 90', 'X: R1088'],'Distinct':['D10.2 Unit Price: 1', 'X: R1088']}
        for i in range(len(fun)) :
            print("----------------"+fun[i]+" Function for Line chart------------")
            rollupobj.select_aggregate_function('wall1', 1,fun[i])
            verify_line_chart(line_yaxis[fun[i]],line_tooltip[fun[i]],'05.'+str(i))
          
        """
        Step 06 : Switch from the Line Graph to a Scatter Diagram by selecting the fifth option from the tool bar.
        Expect to see a multipoint scatter diagram. This will produce a detail diagram. No Summation options are available.
        """
        rollupobj.select_aggregate_function('wall1', 1, 'Sum')
        rollupobj.click_chart_menu_bar_items('wall1',4)
        time.sleep(4)
        miscelaneous_obj.verify_chart_title('wbody1_ft','D10.2 Unit Price BY ALPHA Store Code','Step 6.1 : Verify chart title')
        expected_xval_list=['R1019','R1020','R1040','R1041','R1044','R1088','R1100','R1109','R1200','R1244','R1248','R1250']
        expected_yval_list=['0','1000','2000','3000','4000','5000','6000']
        result_obj.verify_riser_chart_XY_labels('wbody1_f', expected_xval_list, expected_yval_list,'Step 6.2 :')
        iaresult.verify_number_of_chart_segment('wbody1_f', 12,'Step 6.3 : Verify number of chart risers')
        result_obj.verify_riser_legends('wbody1_f',['D10.2 Unit Price'],'Step 6.4 : Verify chart legend label')
        
        ele=driver.find_element_by_css_selector("#wall1")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step_06.0', image_type='actual',x=1, y=1, w=-1, h=-1)        
        total_summation=len(driver.find_elements_by_css_selector("#dt0_SUM_1_0 [id^='t0_SUM_1_0']"))
        utillobj.asequal(0,total_summation,'Step 06.1 : Verify No summation options are available for scatter diagram')
          
        """
        Step 07 : Switch from the Scatter diagram back to the Rollup Report by using the first icon and select RESTORE ORIGINAL.
        Expect to see the report to reflect Sum, Averages, Minimums, Maximums, Counts and Distinct Counts. 
        """
        rollupobj.select_chartmenubar_option('wall1',1,'Restore Original',0,custom_css='cpop')
        time.sleep(2)
        fun=['Sum','Avg','Min','Max','Count','Distinct']
        for i in range(len(fun)) :
            print("----------------"+fun[i]+" Function for Report------------")
            rollupobj.select_aggregate_function('wall1', 1,fun[i])
            time.sleep(2)
            miscelaneous_obj.verify_page_summary(1,'12of12records,Page1of1','Step 07.'+str(i)+'.1 : Verify page summary')
            iarun.verify_table_data_set('#wall1 #ITableData1', Test_Case_ID+'_'+fun[i]+'_Ds.xlsx','Step 07.'+str(i)+'.2 : Verify expect to see the report to reflect '+fun[i])

if __name__ == '__main__':
    unittest.main()     