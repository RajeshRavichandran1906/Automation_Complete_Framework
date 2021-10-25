'''
Created on July 26, 2017

@author: Prabhakaran

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2204965
TestCase Name = Chart Rollup using a Date field by an Alpha field.

'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea,active_miscelaneous,active_chart_rollup,ia_resultarea,ia_run
from common.lib import utillity

class C2204965_TestClass(BaseTestCase):

    def test_C2204965(self):
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID="C2204965"
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
            miscelaneous_obj.verify_chart_title('wbody1_ft','Date MDYY by ALPHA Store Code','Step '+step_num+'.1 : Verify chart title')
            expected_xval_list=['R1019','R1020','R1040','R1041','R1044','R1088','R1100','R1109','R1200','R1244','R1248','R1250']
            expected_yval_list=yaxis_list
            result_obj.verify_riser_chart_XY_labels('wbody1_f', expected_xval_list, expected_yval_list,'Step '+step_num+'.2 :')
            result_obj.verify_riser_legends('wbody1_f',['Date MDYY'],'Step '+step_num+'.3 : Verify chart legend label ')
            result_obj.verify_number_of_riser('wbody1_f',1,12,'Step '+step_num+'.4 : Verify number of chart risers')
            utillobj.verify_chart_color('wbody1_f','riser!s0!g3!mbar!','cerulean_blue_1','Step '+step_num+'.5 : Verify chart riser color')
            miscelaneous_obj.verify_active_chart_tooltip('wbody1_f','riser!s0!g3!mbar!',tooltip_value,'Step '+step_num+'.6 : Verify chart tooltip value')
            ele=driver.find_element_by_css_selector("#wall1")
            utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step_'+step_num, image_type='actual',x=1, y=1, w=-1, h=-1)
            time.sleep(8)
            
        def verify_pie_chart(tooltip_value,expected_data_label,step_num):
            time.sleep(4)
            miscelaneous_obj.verify_chart_title('wbody1_ft','Date MDYY by ALPHA Store Code','Step '+step_num+'.1 : Verify chart title')
            expected_legend_label=['R1019','R1020','R1040','R1041','R1044','R1088','R1100','R1109','R1200','R1244','Other']
            result_obj.verify_riser_legends('wbody1_f',expected_legend_label,'Step '+step_num+'.2 : Verify chart legend label ')
            iaresult.verify_number_of_chart_segment('wbody1_f',11,'Step '+step_num+'.3 : Verify number of chart risers')
            result_obj.verify_data_labels('wbody1_f',expected_data_label, 'Step '+step_num+'.4 : Verify pie chart data labels',custom_css=".chartPanel text[class^='dataLabels']")
            result_obj.verify_riser_pie_labels_and_legends('wbody1_f',['Date MDYY'],'Step '+step_num+'.4 : ',same_group=True)
            utillobj.verify_chart_color('wbody1_f','riser!s0!g0!mwedge!','cerulean_blue_1','Step '+step_num+'.5 : Verify chart riser color')
            miscelaneous_obj.verify_active_chart_tooltip('wbody1_f','riser!s0!g0!mwedge!',tooltip_value,'Step '+step_num+'.6 : Verify chart tooltip value')
            ele=driver.find_element_by_css_selector("#wall1")
            utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step_'+step_num, image_type='actual',x=1, y=1, w=-1, h=-1)
            time.sleep(8)
            
        def verify_line_chart(yaxis_list,tooltip_value,step_num):
            time.sleep(4)
            miscelaneous_obj.verify_chart_title('wbody1_ft','Date MDYY by ALPHA Store Code','Step '+step_num+'.1 : Verify chart title')
            expected_xval_list=['R1019','R1020','R1040','R1041','R1044','R1088','R1100','R1109','R1200','R1244','R1248','R1250']
            expected_yval_list=yaxis_list
            result_obj.verify_riser_chart_XY_labels('wbody1_f', expected_xval_list, expected_yval_list,'Step '+step_num+'.2 :')
            iaresult.verify_number_of_chart_segment('wbody1_f', 13,'Step '+step_num+'.3 : Verify number of chart risers')
            result_obj.verify_riser_legends('wbody1_f',['Date MDYY'],'Step '+step_num+'.4 : Verify chart legend label ')
            utillobj.verify_chart_color('wbody1_f','riser!s0!g0!mline!','cerulean_blue_1','Step '+step_num+'.5 : Verify chart riser color',attribute_type='stroke')
            miscelaneous_obj.verify_active_chart_tooltip('wbody1_f','marker!s0!g3!mmarker!',tooltip_value,'Step '+step_num+'.6 : Verify chart tooltip value')
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
        #iarun.verify_table_data_set('#MAINTABLE_wbody0 #ITableData0',Test_Case_ID+'_Ds_01.xlsx','Step 01.2 : Verify data set')
        
        """
        Step 02 : Select Date MDYY, ROLLUP, then ALPHA Store Code as the rollup column.
        """
        miscelaneous_obj.select_menu_items('ITableData0',3,'Rollup','ALPHA Store Code')
        parent_css="#wall1 #wtitle1"
        utillobj.synchronize_with_visble_text(parent_css, 'Date MDYY by ALPHA Store Code', 30)
        
        miscelaneous_obj.verify_popup_title('wall1','Date MDYY by ALPHA Store Code','Step 02.1 : Verify popup title')
        
        """
        Step 02.1 : Expect to see a 12 line report with one row for each unique ALPHA Store Code value.
        """
        miscelaneous_obj.verify_page_summary(1,'12of12records,Page1of1','Step 02.3 : Verify page summary')
        iarun.verify_table_data_set('#wall1 #ITableData1', Test_Case_ID+'_Count_Ds.xlsx','Step 02.4 : Verify expect to see a 12 line report with one row for each unique ALPHA Store Code value.')
        miscelaneous_obj.verify_arChartToolbar('wall1', ['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Rollup', 'Advanced Chart', 'Original Chart'],"Step 02.5 : Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('wall1', ['Aggregation'],"Step 02.6 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('wall1', ['Count'],"Step 02.7 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)  
        utillobj.verify_object_visible("#wall1 .arChartMenuBarContainer [id^='LINKIMG'] img",True,'Step 02.8 : Verify Rollup char lock icon')
          
        
        """
        Step 03.0 : Switch from the ROLLUP report to a BAR Chart by selecting the second option from the tool bar.
        Then select the last icon and change Count to Distinct. All other Summation options do not apply.
        """
        rollupobj.click_chart_menu_bar_items('wall1',1)
        bcommon_yaxis=['0','20','40','60','80','100']
        bcommon_tooltip=['Date MDYY: 90', 'X: R1041']
        bar_yaxis={'Sum':bcommon_yaxis,'Avg':bcommon_yaxis,'Min':bcommon_yaxis,'Max':bcommon_yaxis,'Count':bcommon_yaxis,'Distinct':['0','1','2','3','4','5','6','7','8']}
        bar_tooltip={'Sum':bcommon_tooltip,'Avg':bcommon_tooltip,'Min':bcommon_tooltip,'Max':bcommon_tooltip,'Count':bcommon_tooltip,'Distinct':['Date MDYY: 1', 'X: R1041']}
        for i in range(len(fun)) :
            print("\n----------------"+fun[i]+" Function for Bar chart------------\n")
            verify=True if fun[i]=='Count' or fun[i]=='Distinct' else False
            rollupobj.select_aggregate_function('wall1', 1,fun[i],9,verify)
            verify_bar_chart(bar_yaxis[fun[i]],bar_tooltip[fun[i]],'03.'+str(i))
            
        """
        Step 04.0 : Switch from the BAR Chart to a PIE Chart by selecting the third option in the tool bar.
        Then select the last icon and change Count to Distinct. All other Summation options do not apply.
        Expect to only see a change for Distinct.
        """
        rollupobj.click_chart_menu_bar_items('wall1',2)
        pcommon_tooltip=['R1019', 'Date MDYY: 90', '9.0% of 1,000']
        pcommon_datalabel=['9%', '9%', '9%', '9%', '9%', '9%', '9%', '8%', '8%', '8%', '15%']
        pie_tooltip={'Sum':pcommon_tooltip,'Avg':pcommon_tooltip,'Min':pcommon_tooltip,'Max':pcommon_tooltip,'Count':pcommon_tooltip,'Distinct':['R1019', 'Date MDYY: 7', '38.9% of 18']}
        data_label={'Sum':pcommon_datalabel,'Avg':pcommon_datalabel,'Min':pcommon_datalabel,'Max':pcommon_datalabel,'Count':pcommon_datalabel,'Distinct':['39%', '6%', '6%', '6%', '6%', '6%', '6%', '6%', '6%', '6%', '11%']}
        for i in range(len(fun)) :
            print("\n----------------"+fun[i]+" Function for Pie chart------------\n")
            verify=True if fun[i]=='Count' or fun[i]=='Distinct' else False
            rollupobj.select_aggregate_function('wall1', 1,fun[i],9,verify)
            verify_pie_chart(pie_tooltip[fun[i]],data_label[fun[i]],'04.'+str(i))
               
        """
        Step 05.0 : Switch from the PIE Chart to a Line Graph by selecting the fourth option from the tool bar.
        Then select the last icon and change Count to Distinct. All other Summation options do not apply.
        Expect to only see a change for Distinct.
        """
        rollupobj.click_chart_menu_bar_items('wall1',3)
        lcommon_yaxis=['0','20','40','60','80','100']
        lcommon_tooltip=['Date MDYY: 90', 'X: R1041']
        line_yaxis={'Sum':lcommon_yaxis,'Avg':lcommon_yaxis,'Min':lcommon_yaxis,'Max':lcommon_yaxis,'Count':lcommon_yaxis,'Distinct':['0','1','2','3','4','5','6','7','8']}
        line_tooltip={'Sum':lcommon_tooltip,'Avg':lcommon_tooltip,'Min':lcommon_tooltip,'Max':lcommon_tooltip,'Count':lcommon_tooltip,'Distinct':['Date MDYY: 1', 'X: R1041']}
        for i in range(len(fun)) :
            print("\n----------------"+fun[i]+" Function for Line chart------------\n")
            verify=True if fun[i]=='Count' or fun[i]=='Distinct' else False
            rollupobj.select_aggregate_function('wall1', 1,fun[i],9,verify)
            verify_line_chart(line_yaxis[fun[i]],line_tooltip[fun[i]],'05.'+str(i))
            
        """
        Step 06 : Switch from the Line Graph to a Scatter Diagram by selecting the fifth option from the tool bar.
        Expect to see a multipoint scatter diagram. This will produce a detail diagram. No Summation options are available.
        Three points represent small values and will appear as zero values.
        """
        rollupobj.select_aggregate_function('wall1', 1, 'Count')
        rollupobj.click_chart_menu_bar_items('wall1',4)
        time.sleep(4)
        miscelaneous_obj.verify_chart_title('wbody1_ft','Date MDYY by ALPHA Store Code','Step 6.1 : Verify chart title')
        expected_xval_list=['R1019','R1020','R1040','R1041','R1044','R1088','R1100','R1109','R1200','R1244','R1248','R1250']
        expected_yval_list=['0','20','40','60','80','100']
        result_obj.verify_riser_chart_XY_labels('wbody1_f', expected_xval_list, expected_yval_list,'Step 6.2 :')
        iaresult.verify_number_of_chart_segment('wbody1_f', 12,'Step 6.3 : Verify number of chart risers')
        result_obj.verify_riser_legends('wbody1_f',['Date MDYY'],'Step 6.4 : Verify chart legend label')
        miscelaneous_obj.verify_active_chart_tooltip('wbody1_f','riser!s0!g3!mmarker!',['Date MDYY', 'X: R1041', 'Y: 90'],'Step 6.5 : Verify chart tooltip value')
        ele=driver.find_element_by_css_selector("#wall1")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step_06.0', image_type='actual',x=1, y=1, w=-1, h=-1)        
        total_summation=len(driver.find_elements_by_css_selector("#dt0_SUM_1_0 [id^='t0_SUM_1_0']"))
        utillobj.asequal(0,total_summation,'Step 06.6 : Verify No summation options are available for scatter diagram')
            
        """
        Step 07 : Switch from the Scatter diagram back to the Rollup Report by using the first icon and select RESTORE ORIGINAL.
        Expect to see the report to reflect Sum, Averages, Minimums, Maximums, Counts and Distinct Counts. 
        """
        rollupobj.select_chartmenubar_option('wall1',1,'Restore Original',0,custom_css='cpop')
        time.sleep(2)
        for i in range(len(fun)) :
            print("\n----------------"+fun[i]+" Function for Report------------\n")
            verify=True if fun[i]=='Count' or fun[i]=='Distinct' else False
            rollupobj.select_aggregate_function('wall1', 1,fun[i],9,verify)
            time.sleep(2)
            DataSet_Name=Test_Case_ID+'_Distinct_Ds.xlsx' if fun[i]=='Distinct' else Test_Case_ID+'_Count_Ds.xlsx'
            miscelaneous_obj.verify_page_summary(1,'12of12records,Page1of1','Step 07.'+str(i)+'.1 : Verify page summary')
            iarun.verify_table_data_set('#wall1 #ITableData1', DataSet_Name,'Step 07.'+str(i)+'.2 : Expect to see a Distinct Count for each value of Datetime HYYMDSA')
            
if __name__ == '__main__':
    unittest.main()     