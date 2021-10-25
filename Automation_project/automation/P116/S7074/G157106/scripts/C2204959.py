'''
Created on July 24, 2017

@author: Prabhakaran

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2204959
TestCase Name = Chart Rollup using an Integer by a Date field.

'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea,active_miscelaneous,active_chart_rollup,ia_resultarea,ia_run
from common.lib import utillity

class C2204959_TestClass(BaseTestCase):

    def test_C2204959(self):
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID="C2204959"
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
            miscelaneous_obj.verify_chart_title('wbody1_ft','Order Number INTEGER by Date YYMD','Step '+step_num+'.1 : Verify chart title')
            expected_xval_list=['1996/01/01','1996/02/01','1996/03/01','1996/03/01','1996/05/01','1996/06/01']
            expected_yval_list=yaxis_list
            result_obj.verify_riser_chart_XY_labels('wbody1_f', expected_xval_list, expected_yval_list,'Step '+step_num+'.2 :')
            result_obj.verify_riser_legends('wbody1_f',['Order Number INTEGER'],'Step '+step_num+'.3 : Verify chart legend label')
            result_obj.verify_number_of_riser('wbody1_f',1,6,step_num+'.4 : Verify number of chart risers')
            utillobj.verify_chart_color('wbody1_f','riser!s0!g3!mbar!','cerulean_blue_1','Step '+step_num+'.5 : Verify chart riser color')
            miscelaneous_obj.verify_active_chart_tooltip('wbody1_f','riser!s0!g3!mbar!',tooltip_value,'Step '+step_num+'.6 : Verify chart tooltip value')
            ele=driver.find_element_by_css_selector("#wall1")
            utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step_'+step_num, image_type='actual',x=1, y=1, w=-1, h=-1)
            time.sleep(8)
        def verify_pie_chart(tooltip_value,expected_data_label,step_num):
            time.sleep(4)
            miscelaneous_obj.verify_chart_title('wbody1_ft','Order Number INTEGER by Date YYMD','Step '+step_num+'.1 : Verify chart title')
            expected_legend_label=['1996/01/01','1996/02/01','1996/03/01','1996/03/01','1996/05/01','1996/06/01']
            result_obj.verify_riser_legends('wbody1_f',expected_legend_label,'Step '+step_num+'.2 : Verify chart legend label')
            iaresult.verify_number_of_chart_segment('wbody1_f',6,'Step '+step_num+'.3 : Verify number of chart risers')
            result_obj.verify_data_labels('wbody1_f',expected_data_label, 'Step '+step_num+'.4 : Verify pie chart data labels',custom_css=".chartPanel text[class^='dataLabels']")
            result_obj.verify_riser_pie_labels_and_legends('wbody1_f',['Order Number INTEGER'],'Step '+step_num+'.4 : ',same_group=True)
            utillobj.verify_chart_color('wbody1_f','riser!s5!g0!mwedge!','milky_blue','Step '+step_num+'.5 : Verify chart riser color')
            miscelaneous_obj.verify_active_chart_tooltip('wbody1_f','riser!s5!g0!mwedge!',tooltip_value,'Step '+step_num+'.6 : Verify chart tooltip value')
            ele=driver.find_element_by_css_selector("#wall1")
            utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step_'+step_num, image_type='actual',x=1, y=1, w=-1, h=-1)
            time.sleep(8)
        def verify_line_chart(yaxis_list,tooltip_value,step_num):
            time.sleep(4)
            miscelaneous_obj.verify_chart_title('wbody1_ft','Order Number INTEGER by Date YYMD','Step '+step_num+'.1 : Verify chart title')
            expected_xval_list=['1996/01/01','1996/02/01','1996/03/01','1996/03/01','1996/05/01','1996/06/01']
            expected_yval_list=yaxis_list
            result_obj.verify_riser_chart_XY_labels('wbody1_f', expected_xval_list, expected_yval_list,'Step '+step_num+'.2 :')
            iaresult.verify_number_of_chart_segment('wbody1_f', 7,'Step '+step_num+'.3 : Verify number of chart risers')
            result_obj.verify_riser_legends('wbody1_f',['Order Number INTEGER'],'Step '+step_num+'.4 : Verify chart legend label')
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
        
        """
        Step 02 : Select Order Number INTEGER, ROLLUP, then Date YYMD as the rollup column.
        """
        miscelaneous_obj.select_menu_items('ITableData0',0,'Rollup','Date YYMD')
        parent_css="#wall1 #wtitle1"
        utillobj.synchronize_with_visble_text(parent_css, 'Order Number INTEGER by Date YYMD', 45)
        
        miscelaneous_obj.verify_popup_title('wall1','Order Number INTEGER by Date YYMD','Step 02.1 : Verify popup title')
        
        """
        Step 02.1 : Expect to see a 6 line report with one row for each unique Date YYMD value
        """
        miscelaneous_obj.verify_page_summary(1,'6of6records,Page1of1','Step 02.3 : Verify page summary')
        iarun.verify_table_data_set('#wall1 #ITableData1', Test_Case_ID+'_Sum_Ds.xlsx','Step 02.4 : Verify expect to see a 6 line report with one row for each unique Date YYMD value')
        miscelaneous_obj.verify_arChartToolbar('wall1', ['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Rollup', 'Advanced Chart', 'Original Chart'],"Step 02.5 : Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('wall1', ['Aggregation'],"Step 02.6 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('wall1', ['Sum'],"Step 02.7 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)  
        utillobj.verify_object_visible("#wall1 .arChartMenuBarContainer [id^='LINKIMG'] img",True,'Step 02.8 : Verify Rollup char lock icon')
          
        
        """
        Step 03.0 : Switch from the ROLLUP report to a BAR Chart by selecting the second option from the tool bar. Then select the last icon and change SUM to AVG, MIN, MAX, COUNT & DISTINCT. Switch back to SUM for the next step..
           
        """
        rollupobj.click_chart_menu_bar_items('wall1',1)
        bar_yaxis={'Sum':['0','40K','80K','120K','160K'],'Avg':['0','200','400','600','800','1000'],'Min':['0','200','400','600','800','1000'],
                    'Max':['0','200','400','600','800','1000','1200'],'Count':['0','40','80','120','160','200'],'Distinct':['0','40','80','120','160','200']}
           
        bar_tooltip={'Sum':['Order Number INTEGER: 113K','X: 1996/04/01'],'Avg':['Order Number INTEGER: 630.5','X: 1996/04/01'],'Min':['Order Number INTEGER: 541', 'X: 1996/04/01'],
                    'Max':['Order Number INTEGER: 720', 'X: 1996/04/01'],'Count':['Order Number INTEGER: 180', 'X: 1996/04/01'],'Distinct':['Order Number INTEGER: 180', 'X: 1996/04/01']}
        for i in range(len(fun)) :
            print("----------------"+fun[i]+" Function for Bar chart------------")
            rollupobj.select_aggregate_function('wall1', 1,fun[i])
            verify_bar_chart(bar_yaxis[fun[i]],bar_tooltip[fun[i]],'03.'+str(i))
            
        """
        Step 04.0 : Switch from the BAR Chart to a PIE Chart by selecting the third option in the tool bar. Check the other Summation options as stated in Step 2.
        Expect to see a 6 slice PIE chart. Use the values from the Rollup Report to verify the values on the bars. Verify the other Summation options.
        """
        rollupobj.click_chart_menu_bar_items('wall1',2)
        pie_tooltip={'Sum':['1996/06/01', 'Order Number INTEGER: 95,050', '19.0% of 501K'],'Avg':['1996/06/01', 'Order Number INTEGER: 950.5', '29.7% of 3,203'],'Min':['1996/06/01', 'Order Number INTEGER: 901', '33.3% of 2,706'],
                    'Max':['1996/06/01', 'Order Number INTEGER: 1,000', '27.0% of 3,700'],'Count':['1996/06/01', 'Order Number INTEGER: 100', '10.0% of 1,000'],'Distinct':['1996/06/01', 'Order Number INTEGER: 100', '10.0% of 1,000']}
           
        data_label={'Sum':['3%', '10%', '16%', '23%', '29%', '19%'],'Avg':['3%', '8%', '14%', '20%', '25%', '30%'],'Min':['0%', '7%', '13%', '20%', '27%', '33%'],
                    'Max':['5%', '10%', '15%', '19%', '24%', '27%'],'Count':['18%', '18%', '18%', '18%', '18%', '10%'],'Distinct':['18%', '18%', '18%', '18%', '18%', '10%']}
           
        for i in range(len(fun)) :
            print("----------------"+fun[i]+" Function for Pie chart------------")
            rollupobj.select_aggregate_function('wall1', 1,fun[i])
            verify_pie_chart(pie_tooltip[fun[i]],data_label[fun[i]],'04.'+str(i))
              
        """
        Step 05.0 : Switch from the PIE Chart to a Line Graph by selecting the fourth option from the tool bar. Then select the last icon and change Count to Distinct. Check the other Summation options as stated in Step 2.
        """
        rollupobj.click_chart_menu_bar_items('wall1',3)
        line_yaxis={'Sum':['0','40K','80K','120K','160K'],'Avg':['0','200','400','600','800','1000'],'Min':['0','200','400','600','800','1000'],
                    'Max':['0','200','400','600','800','1000','1200'],'Count':['0','40','80','120','160','200'],'Distinct':['0','40','80','120','160','200']}
           
        line_tooltip={'Sum':['Order Number INTEGER: 113K','X: 1996/04/01'],'Avg':['Order Number INTEGER: 630.5','X: 1996/04/01'],'Min':['Order Number INTEGER: 541', 'X: 1996/04/01'],
                    'Max':['Order Number INTEGER: 720', 'X: 1996/04/01'],'Count':['Order Number INTEGER: 180', 'X: 1996/04/01'],'Distinct':['Order Number INTEGER: 180', 'X: 1996/04/01']}
         
        for i in range(len(fun)) :
            print("----------------"+fun[i]+" Function for Line chart------------")
            rollupobj.select_aggregate_function('wall1', 1,fun[i])
            verify_line_chart(line_yaxis[fun[i]],line_tooltip[fun[i]],'05.'+str(i))
           
        """
        Step 06 : Switch from the Line Graph to a Scatter Diagram by selecting the fifth option from the tool bar.
        Expect to see a multipoint scatter diagram. This will produce a detail diagram. No Summation options are available..
        """
        rollupobj.select_aggregate_function('wall1', 1, 'Sum')
        rollupobj.click_chart_menu_bar_items('wall1',4)
        time.sleep(4)
        miscelaneous_obj.verify_chart_title('wbody1_ft','Order Number INTEGER by Date YYMD','Step 6.1 : Verify chart title')
        expected_xval_list=['1996/01/01','1996/02/01','1996/03/01','1996/03/01','1996/05/01','1996/06/01']
        expected_yval_list=['0','40K','80K','120K','160K']
        result_obj.verify_riser_chart_XY_labels('wbody1_f', expected_xval_list, expected_yval_list,'Step 6.2 :')
        iaresult.verify_number_of_chart_segment('wbody1_f', 6,'Step 6.3 : Verify number of chart risers')
        result_obj.verify_riser_legends('wbody1_f',['Order Number INTEGER'],'Step 6.4 : Verify chart legend label')
#         miscelaneous_obj.verify_active_chart_tooltip('wbody1_f','riser!s0!g5!mmarker!',['Order Number INTEGER', 'X:', 'Y: 95,050'],'Step 6.5 : Verify chart tooltip value')
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
        fun=['Sum','Avg','Min','Max','Count','Distinct']
        for i in range(len(fun)) :
            print("----------------"+fun[i]+" Function for Report------------")
            rollupobj.select_aggregate_function('wall1', 1,fun[i])
            time.sleep(2)
            miscelaneous_obj.verify_page_summary(1,'6of6records,Page1of1','Step 07.'+str(i)+'.1 : Verify page summary')
            iarun.verify_table_data_set('#wall1 #ITableData1', Test_Case_ID+'_'+fun[i]+'_Ds.xlsx','Step 07.'+str(i)+'.2 : Verify expect to see the report to reflect '+fun[i])
            
if __name__ == '__main__':
    unittest.main()     