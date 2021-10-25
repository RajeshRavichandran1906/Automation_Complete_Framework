'''
Created on JUL 21, 2017

@author: Pavithra

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2204962
 TestCase Name = Chart Rollup using an Alphanumeric field by a Date field
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea,active_miscelaneous,ia_resultarea,active_chart_rollup,ia_run
from common.lib import utillity

class C2204962_TestClass(BaseTestCase):

    def test_C2204962(self):
        
        Test_Case_ID="C2204962"
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
        summation=['Sum','Avg','Min','Max','Count','Distinct']
        
        def verify_bar_chart(yaxis_list,tooltip_value,step_num):
            time.sleep(3)
            miscelaneous_obj.verify_chart_title('wbody1_ft','ALPHA Store Code BY Date MDYY','Step '+step_num+'.1 : Verify chart title')
            expected_xval_list=['01/01/1996','02/01/1996','03/01/1996','04/01/1996','05/01/1996','06/01/1996']
            expected_yval_list=yaxis_list
            resobj.verify_riser_chart_XY_labels('wbody1_f', expected_xval_list, expected_yval_list,'Step '+step_num+'.2 :')
            resobj.verify_riser_legends('wbody1_f',['ALPHA Store Code'],'Step '+step_num+'.3 : Verify chart legend label')
            resobj.verify_number_of_riser('wbody1_f',1,6,'Step '+step_num+'.4 : Verify number of chart risers')
            utillobj.verify_chart_color('wbody1_f','riser!s0!g3!mbar!','cerulean_blue_1','Step '+step_num+'.5 : Verify chart riser color')
            miscelaneous_obj.verify_active_chart_tooltip('wbody1_f','riser!s0!g3!mbar!',tooltip_value,'Step '+step_num+'.6 : Verify chart tooltip value')
            time.sleep(5)
            ele=driver.find_element_by_css_selector("#wall1")
            utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step_'+step_num, image_type='actual',x=1, y=1, w=-1, h=-1)
            
        def verify_pie_charts(expected_datalabel,tooltip_value,step_num):
            time.sleep(4)
            miscelaneous_obj.verify_chart_title('wbody1_ft','ALPHA Store Code BY Date MDYY','Step '+step_num+'.1 : Verify chart title')
            resobj.verify_data_labels('wbody1_f', expected_datalabel, 'Step '+step_num+'.2 verify pie data_labels:', custom_css=".chartPanel text[class^='dataLabels']")
            resobj.verify_riser_legends('wbody1_f',['01/01/1996','02/01/1996','03/01/1996','04/01/1996','05/01/1996','06/01/1996'],'Step '+step_num+'.3 : Verify chart legend label')
            resobj.verify_riser_pie_labels_and_legends('wbody1_f', ['ALPHA Store Code'], "Step 03.4:",custom_css="text[class*='pieLabel']",same_group=True)
            ia_resultobj.verify_number_of_chart_segment('wbody1_f',6,'Step '+step_num+'.4 : Verify number of chart risers')
            utillobj.verify_chart_color('wbody1_f','riser!s0!g0!mwedge!','cerulean_blue_1','Step '+step_num+'.5 : Verify chart riser color')
            miscelaneous_obj.verify_active_chart_tooltip('wbody1_f','riser!s0!g0!mwedge!',tooltip_value,'Step '+step_num+'.6 : Verify chart tooltip value')
            time.sleep(5)
            ele=driver.find_element_by_css_selector("#wall1")
            utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step_'+step_num, image_type='actual',x=1, y=1, w=-1, h=-1)
        
        def verify_line_charts(yaxis_list,tooltip_value,step_num):
            time.sleep(4)
            miscelaneous_obj.verify_chart_title('wbody1_ft','ALPHA Store Code BY Date MDYY','Step '+step_num+'.1 : Verify chart title')
            expected_xval_list=['01/01/1996','02/01/1996','03/01/1996','04/01/1996','05/01/1996','06/01/1996']
            expected_yval_list=yaxis_list
            resobj.verify_riser_chart_XY_labels('wbody1_f', expected_xval_list, expected_yval_list,'Step '+step_num+'.2 :')
            resobj.verify_riser_legends('wbody1_f',['ALPHA Store Code'],'Step '+step_num+'.3 : Verify chart legend label')
            ia_resultobj.verify_number_of_chart_segment('wbody1_f',7,'Step '+step_num+'.4 : Verify number of chart risers')
            utillobj.verify_chart_color('wbody1_f','marker!s0!g3!mmarker!','cerulean_blue_1','Step '+step_num+'.5 : Verify chart riser color',attribute_type='stroke')
            miscelaneous_obj.verify_active_chart_tooltip('wbody1_f','marker!s0!g3!mmarker!',tooltip_value,'Step '+step_num+'.6 : Verify chart tooltip value')
            time.sleep(5)
            ele=driver.find_element_by_css_selector("#wall1")
            utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step_'+step_num, image_type='actual',x=1, y=1, w=-1, h=-1)
            
        """
            Step 01:Execute attached AR-RP-141CA.fex
        """
        utillobj.active_run_fex_api_login("AR-RP-141CA.fex", "S7074", 'mrid', 'mrpass')
        parent_css="#MAINTABLE_wbody0 .arGrid [id^='TCOL']"
        utillobj.synchronize_with_number_of_element(parent_css, 8, 65)
        
        miscelaneous_obj.verify_page_summary(0,'1000of1000records,Page1of18', 'Step 01.1: Verify Page summary')
#         ia_runobj.create_table_data_set("table[id='ITableData0']", Test_Case_ID+"_Ds01.xlsx")
        column_list=['Order Number INTEGER', 'ALPHA Store Code', 'Date YYMD', 'Date MDYY', 'Date DMYY', 'D10.2 Unit Price', 'P9.2M Unit Price', 'DATETIME HYYMDSA']
        miscelaneous_obj.verify_column_heading('ITableData0', column_list, 'Step 01.2 : Verify the column heading')
        time.sleep(2)
         
        """
            Step 02 : Select ALPHA Store Code, ROLLUP, then Date MDYY as the rollup column.
        """
        miscelaneous_obj.select_menu_items('ITableData0',1,'Rollup','Date MDYY')
        parent_css="#wall1 span[id='wtitle1']"
        utillobj.synchronize_with_visble_text(parent_css, 'ALPHAStoreCodeBYDateMDYY', 40)
        
        miscelaneous_obj.verify_popup_title('wall1','ALPHA Store Code BY Date MDYY','Step 02.1 : Verify popup title')
        
                 
        """
            Step 02.1 :Expect to see a 6 line report with one row for each unique Date MDYY value.
                       Use these Count values to verify the data on the Pie, Bar & Line graphs.
        """
        miscelaneous_obj.verify_page_summary(1,'6of6records,Page1of1','Step 02.3 : Verify page summary')
#         ia_runobj.create_table_data_set("#wall1 #ITableData1", Test_Case_ID+"_Ds02.xlsx")
        ia_runobj.verify_table_data_set('#wall1 #ITableData1', Test_Case_ID+'_Ds02.xlsx','Step 02.4 : Verify 4 line report with one row for each unique Datetime HYYMDSA value')
        miscelaneous_obj.verify_arChartToolbar('wall1', ['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Rollup', 'Advanced Chart', 'Original Chart'],"Step 02.5 : Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('wall1', ['Aggregation'],"Step 02.6 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('wall1', ['Count'],"Step 02.7 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)  
        utillobj.verify_object_visible("#wall1 .arChartMenuBar div[onclick*='toggleFiltLink']", True, 'Step 03.10 Verify chart rollup lock icon')        
        """
            Step 03 :Switch from the ROLLUP report to a BAR Chart by selecting the second option from the tool bar.
                     Then select the last icon and change Count to Distinct. 
                     All other Summation options do not apply.
        """
        rollupobj.click_chart_menu_bar_items('wall1',1)
        bcommon_yaxis=['0','40','80','120','160','200']
        bcommon_tooltip=['ALPHA Store Code: 180', 'X: 04/01/1996']
        bar_yaxis={'Sum':bcommon_yaxis,'Avg':bcommon_yaxis,'Min':bcommon_yaxis,'Max':bcommon_yaxis,'Count':bcommon_yaxis,'Distinct':['0','3','6','9','12','15']}
        bar_tooltip={'Sum':bcommon_tooltip,'Avg':bcommon_tooltip,'Min':bcommon_tooltip,'Max':bcommon_tooltip,'Count':bcommon_tooltip,'Distinct':['ALPHA Store Code: 1', 'X: 04/01/1996']}
        for i in range(len(summation)) :
            print("\n**********"+summation[i]+" Function for bar chart**********\n")
            verify=True if summation[i]=='Count' or summation[i]=='Distinct' else False
            rollupobj.select_aggregate_function('wall1', 1,summation[i],9,verify)
            verify_bar_chart(bar_yaxis[summation[i]],bar_tooltip[summation[i]],'03.'+str(i))
 
        """
            Step 04 :Switch from the BAR Chart to a PIE Chart by selecting the third option in the tool bar. 
                    Then select the last icon and change Count to Distinct. 
                    All other Summation options do not apply.
        """
        rollupobj.click_chart_menu_bar_items('wall1',2)
        pcommon_tooltip=['01/01/1996', 'ALPHA Store Code: 180', '18.0% of 1,000']
        pcommon_datalabel=['18%','18%','18%','18%','18%','10%']                                                                                    
        pie_tooltip={'Sum':pcommon_tooltip,'Avg':pcommon_tooltip,'Min':pcommon_tooltip,'Max':pcommon_tooltip,'Count':pcommon_tooltip,'Distinct':['01/01/1996', 'ALPHA Store Code: 13', '72.2% of 18']}
        data_label={'Sum':pcommon_datalabel,'Avg':pcommon_datalabel,'Min':pcommon_datalabel,'Max':pcommon_datalabel,'Count':pcommon_datalabel,'Distinct':['72%','6%','6%','6%','6%','6%']}
        for i in range(len(summation)) :
            print("\n**********"+summation[i]+" Function for Pie chart**********\n")
            verify=True if summation[i]=='Count' or summation[i]=='Distinct' else False
            rollupobj.select_aggregate_function('wall1', 1,summation[i],9,verify)
            verify_pie_charts(data_label[summation[i]],pie_tooltip[summation[i]],'04.'+str(i))
                      
        """
            Step 05:Switch from the PIE Chart to a Line Graph by selecting the fourth option from the tool bar.
                     Then select the last icon and change Count to Distinct. 
                     All other Summation options do not apply.
        """
        rollupobj.click_chart_menu_bar_items('wall1',3)
        lcommon_yaxis=['0','40','80','120','160','200']
        lcommon_tooltip=['ALPHA Store Code: 180', 'X: 04/01/1996']
        line_yaxis={'Sum':lcommon_yaxis,'Avg':lcommon_yaxis,'Min':lcommon_yaxis,'Max':lcommon_yaxis,'Count':lcommon_yaxis,'Distinct':['0','3','6','9','12','15']}
        line_tooltip={'Sum':lcommon_tooltip,'Avg':lcommon_tooltip,'Min':lcommon_tooltip,'Max':lcommon_tooltip,'Count':lcommon_tooltip,'Distinct':['ALPHA Store Code: 1', 'X: 04/01/1996']}
        for i in range(len(summation)) :
            print("\n**********"+summation[i]+" Function for Line chart**********\n")
            verify=True if summation[i]=='Count' or summation[i]=='Distinct' else False
            rollupobj.select_aggregate_function('wall1', 1,summation[i],9,verify)
            verify_line_charts(line_yaxis[summation[i]],line_tooltip[summation[i]],'05.'+str(i))
         
        """
            Step 06:Switch from the Line Graph to a Scatter Diagram by selecting the fifth option from the tool bar.
        """
        rollupobj.select_aggregate_function('wall1', 1,"Count")
        print("\n********** Function for Scatter chart**********\n")
        rollupobj.click_chart_menu_bar_items('wall1',4)
        time.sleep(4)
        miscelaneous_obj.verify_chart_title('wbody1_ft','ALPHA Store Code BY Date MDYY','Step 06.1 : Verify chart title')
        expected_xval_list=['01/01/1996','02/01/1996','03/01/1996','04/01/1996','05/01/1996','06/01/1996']
        expected_yval_list=['0','40','80','120','160','200']
        resobj.verify_riser_chart_XY_labels('wbody1_f', expected_xval_list, expected_yval_list,'Step 06.2 :')
        resobj.verify_riser_legends('wbody1_f',['ALPHA Store Code'],'Step 06.3 : Verify chart legend label')
        ia_resultobj.verify_number_of_chart_segment('wbody1_f',6,'Step 06.4 : Verify number of chart risers')
        utillobj.verify_chart_color('wbody1_f','riser!s0!g3!mmarker!','cerulean_blue_1','Step 06.5 : Verify chart riser color',attribute_type='stroke')
#         tooltip_value=['ALPHA Store Code', 'X: ', 'Y: 180']
#         miscelaneous_obj.verify_active_chart_tooltip('wbody1_f','riser!s0!g3!mmarker!',tooltip_value,'Step 06.6 : Verify chart tooltip value')
        time.sleep(5)
        ele=driver.find_element_by_css_selector("#wall1")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step_6', image_type='actual',x=1, y=1, w=-1, h=-1)
        total_summation=len(driver.find_elements_by_css_selector("#dt0_SUM_1_0 [id^='t0_SUM_1_0']"))
        utillobj.asequal(0,total_summation,'Step 06.7 : Verify No summation options are available for scatter diagram')
        
        """
            Step 07:Switch from the Scatter diagram back to the Rollup Report by using the first icon and select RESTORE ORIGINAL. 
                    Then select the last icon, labeled Count. The only option that will change the graph is Distinct,
                    as the graphs represent Counts and not Sums that can accept Min, Max, etc.
        """
        
        rollupobj.select_chartmenubar_option('wall1',1,'Restore Original',0,custom_css='cpop')
        time.sleep(2)
        for i in range(len(summation)) :
            print("\n**********"+summation[i]+" Function for Report**********\n")
            verify=True if summation[i]=='Count' or summation[i]=='Distinct' else False
            rollupobj.select_aggregate_function('wall1', 1,summation[i],9,verify)
            time.sleep(2)
            DataSet_Name=Test_Case_ID+'_Distinct_Ds.xlsx' if summation[i]=='Distinct' else Test_Case_ID+'_Count_Ds.xlsx'
            miscelaneous_obj.verify_page_summary(1,'6of6records,Page1of1','Step 07.'+str(i)+'.1 : Verify page summary')
            ia_runobj.verify_table_data_set('#wall1 #ITableData1', DataSet_Name,'Step 07.'+str(i)+'.2 : Expect to see a Distinct Count for each value of ALPHA Store Code BY Date MDYY')
        time.sleep(2)
        miscelaneous_obj.close_popup_dialog('1')
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()         