'''
Created on JUL 25, 2017

@author: Pavithra

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2204970
 TestCase Name = Chart Rollup using a Numeric field by a different Numeric field.
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea,active_miscelaneous,ia_resultarea,active_chart_rollup,ia_run
from common.lib import utillity

class C2204970_TestClass(BaseTestCase):

    def test_C2204970(self):
        
        Test_Case_ID="C2204970"
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
            miscelaneous_obj.verify_chart_title('wbody1_ft','P9.2M Unit Price by D10.2 Unit Price','Step '+step_num+'.1 : Verify chart title')
            expected_xval_list=['13','17','26','28','58','76','81','96','125','140']
            expected_yval_list=yaxis_list
            resobj.verify_riser_chart_XY_labels('wbody1_f', expected_xval_list, expected_yval_list,'Step '+step_num+'.2 :')
            resobj.verify_riser_legends('wbody1_f',['P9.2M Unit Price'],'Step '+step_num+'.3 : Verify chart legend label')
            resobj.verify_number_of_riser('wbody1_f',1,10,'Step '+step_num+'.4 : Verify number of chart risers')
            utillobj.verify_chart_color('wbody1_f','riser!s0!g5!mbar','cerulean_blue_1','Step '+step_num+'.5 : Verify chart riser color')
            miscelaneous_obj.verify_active_chart_tooltip('wbody1_f','riser!s0!g6!mbar',tooltip_value,'Step '+step_num+'.6 : Verify chart tooltip value')
            time.sleep(5)
            ele=driver.find_element_by_css_selector("#wall1")
            utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step_'+step_num, image_type='actual',x=1, y=1, w=-1, h=-1)
            
        def verify_pie_charts(expected_datalabel,tooltip_value,step_num):
            time.sleep(4)
            miscelaneous_obj.verify_chart_title('wbody1_ft','P9.2M Unit Price by D10.2 Unit Price','Step '+step_num+'.1 : Verify chart title')
            resobj.verify_data_labels('wbody1_f', expected_datalabel, 'Step '+step_num+'.2 verify data_label:', custom_css=".chartPanel text[class^='dataLabels']")
            resobj.verify_riser_legends('wbody1_f',['13','17','26','28','58','76','81','96','125','140'],'Step '+step_num+'.3 : Verify chart legend label')
            resobj.verify_riser_pie_labels_and_legends('wbody1_f', ['P9.2M Unit Price'], "Step 03.4:",custom_css="text[class*='pieLabel']",same_group=True)
            ia_resultobj.verify_number_of_chart_segment('wbody1_f',10,'Step '+step_num+'.4 : Verify number of chart risers')
            utillobj.verify_chart_color('wbody1_f','riser!s0!g0!mwedge!','cerulean_blue_1','Step '+step_num+'.5 : Verify chart riser color')
            miscelaneous_obj.verify_active_chart_tooltip('wbody1_f','riser!s6!g0!mwedge',tooltip_value, 'Step '+step_num+'.6 : Verify chart tooltip value',cord_type='middle')
            time.sleep(5)
            ele=driver.find_element_by_css_selector("#wall1")
            utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step_'+step_num, image_type='actual',x=1, y=1, w=-1, h=-1)
        
        def verify_line_charts(yaxis_list,tooltip_value,step_num):
            time.sleep(4)
            miscelaneous_obj.verify_chart_title('wbody1_ft','P9.2M Unit Price by D10.2 Unit Price','Step '+step_num+'.1 : Verify chart title')
            expected_xval_list=['13','17','26','28','58','76','81','96','125','140']
            expected_yval_list=yaxis_list
            resobj.verify_riser_chart_XY_labels('wbody1_f', expected_xval_list, expected_yval_list,'Step '+step_num+'.2 :')
            resobj.verify_riser_legends('wbody1_f',['P9.2M Unit Price'],'Step '+step_num+'.3 : Verify chart legend label')
            ia_resultobj.verify_number_of_chart_segment('wbody1_f',11,'Step '+step_num+'.4 : Verify number of chart risers')
            utillobj.verify_chart_color('wbody1_f','riser!s0!g0!mline!','cerulean_blue_1','Step '+step_num+'.5 : Verify chart riser color',attribute_type='stroke')
            miscelaneous_obj.verify_active_chart_tooltip('wbody1_f','marker!s0!g6!mmarker',tooltip_value,'Step '+step_num+'.6 : Verify chart tooltip value')
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
            Step 02 : Select P9.2M Unit Price, ROLLUP, then D10.2 Unit Price as the rollup column.
        """
        miscelaneous_obj.select_menu_items('ITableData0',6,'Rollup','D10.2 Unit Price')
        parent_css="#wall1 span[id='wtitle1']"
        utillobj.synchronize_with_visble_text(parent_css, 'P9.2MUnitPricebyD10.2UnitPrice', 30)
        
        miscelaneous_obj.verify_popup_title('wall1','P9.2M Unit Price by D10.2 Unit Price','Step 02.1 : Verify popup title')
        
                 
        """
            Step 02.1 : Expect to see a 10 line report with one row for each unique D10.2 Unit Price value. 
                        Use these Summed values to verify the data on the Pie, Bar & Line graphs.
        """
        miscelaneous_obj.verify_page_summary(1,'10of10records,Page1of1','Step 02.3 : Verify page summary')
        ia_runobj.create_table_data_set("#wall1 #ITableData1", Test_Case_ID+"_Ds02.xlsx")
        ia_runobj.verify_table_data_set('#wall1 #ITableData1', Test_Case_ID+'_Ds02.xlsx','Step 02.4 : Verify 4 line report with one row for each unique Datetime HYYMDSA value')
        miscelaneous_obj.verify_arChartToolbar('wall1', ['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Rollup', 'Advanced Chart', 'Original Chart'],"Step 02.5 : Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('wall1', ['Aggregation'],"Step 02.6 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('wall1', ['Sum'],"Step 02.7 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)  
        utillobj.verify_object_visible("#wall1 .arChartMenuBar div[onclick*='toggleFiltLink']", True, 'Step 03.10 Verify chart rollup lock icon')        
        """
            Step 03 :Switch from the ROLLUP report to a BAR Chart by selecting the second option from the tool bar.
                     Then select the last icon and change SUM to AVG, MIN, MAX, COUNT & DISTINCT.
                     Switch back to SUM for the next step.
        """
        
        rollupobj.click_chart_menu_bar_items('wall1',1)
        yaxis_list={'Sum':['0','30K','60K','90K','120K','150K'],'Avg':['0','100','200','300','400','500','600','700'],'Min':['0','40','80','120','160'],
                   'Max':['0','300','600','900','1200'],'Count':['0','40','80','120','160','200','240'],'Distinct':['0','40','80','120','160']}
         
        bar_tooltip={'Sum':['P9.2M Unit Price: 127K', 'X: 81'],'Avg':['P9.2M Unit Price: 580.3', 'X: 81'],'Min':['P9.2M Unit Price: 84', 'X: 81'],
                   'Max':['P9.2M Unit Price: 1,075', 'X: 81'],'Count':['P9.2M Unit Price: 218', 'X: 81'],'Distinct':['P9.2M Unit Price: 126', 'X: 81']}
        for i in range(len(summation)) :
            print("\n**********"+summation[i]+" Function for bar chart**********\n")
            rollupobj.select_aggregate_function('wall1', 1,summation[i])
            verify_bar_chart(yaxis_list[summation[i]],bar_tooltip[summation[i]],'3.'+str(i))
            
        """
            Step 04 :Switch from the BAR Chart to a PIE Chart by selecting the third option in the tool bar. 
                     Check the other Summation options as stated in Step 2.
        """
        rollupobj.click_chart_menu_bar_items('wall1',2)
        expected_datalabel={'Sum':['8%','9%','13%','14%','8%','3%','23%','7%','7%','8%'],'Avg':['9%','9%','9%','9%','10%','10%','10%','11%','11%','11%'],'Min':['3%','4%','4%','5%','8%','14%','11%','14%','17%','19%'],
                   'Max':['10%','9%','10%','10%','10%','10%','10%','10%','11%','11%'],'Count':['8%','10%','13%','15%','8%','3%','22%','7%','7%','7%'],'Distinct':['12%','15%','20%','22%','4%','5%','18%','1%','1%','3%']}
           
        pie_tooltip={'Sum':['81', 'P9.2M Unit Price: 127K', '22.6% of 560K'],'Avg':['81', 'P9.2M Unit Price: 580.3', '10.2% of 5,667'],'Min':['81', 'P9.2M Unit Price: 84', '10.9% of 770'],
                   'Max':['81', 'P9.2M Unit Price: 1,075', '10.2% of 10,589'],'Count':['81', 'P9.2M Unit Price: 218', '21.8% of 1,000'],'Distinct':['81', 'P9.2M Unit Price: 126', '18.5% of 682']}
        for i in range(len(summation)) :
            print("\n**********"+summation[i]+" Function for pie chart**********\n")
            rollupobj.select_aggregate_function('wall1', 1,summation[i])
            verify_pie_charts(expected_datalabel[summation[i]],pie_tooltip[summation[i]],'4.'+str(i))
            
        """
            Step 05:Switch from the PIE Chart to a Line Graph by selecting the fourth option from the tool bar.
                     Check the other Summation options as stated in Step 2.
                     Expect to see a 10 point line graph with one row for each unique Unit Price value. Verify the other Summation options.
        """
        rollupobj.click_chart_menu_bar_items('wall1',3)
        yaxis_list={'Sum':['0','30K','60K','90K','120K','150K'],'Avg':['0','100','200','300','400','500','600','700'],'Min':['0','40','80','120','160'],
                   'Max':['0','300','600','900','1200'],'Count':['0','40','80','120','160','200','240'],'Distinct':['0','40','80','120','160']}
         
        line_tooltip={'Sum':['P9.2M Unit Price: 127K', 'X: 81'],'Avg':['P9.2M Unit Price: 580.3', 'X: 81'],'Min':['P9.2M Unit Price: 84', 'X: 81'],
                   'Max':['P9.2M Unit Price: 1,075', 'X: 81'],'Count':['P9.2M Unit Price: 218', 'X: 81'],'Distinct':['P9.2M Unit Price: 126', 'X: 81']}
        for i in range(len(summation)) :
            print("\n**********"+summation[i]+" Function for line chart**********\n")
            rollupobj.select_aggregate_function('wall1', 1,summation[i])
            verify_line_charts(yaxis_list[summation[i]],line_tooltip[summation[i]],'5.'+str(i))
        """
            Step 06:Switch from the Line Graph to a Scatter Diagram by selecting the fifth option from the tool bar.
                    Expect to see a multipoint scatter diagram. This will produce a detail diagram. No Summation options are available.
        """
        rollupobj.select_aggregate_function('wall1', 1,"Sum")
        print("\n**********Function for Scatter chart**********\n")
        rollupobj.click_chart_menu_bar_items('wall1',4)
        time.sleep(4)
        miscelaneous_obj.verify_chart_title('wbody1_ft','P9.2M Unit Price by D10.2 Unit Price','Step 06.1 : Verify chart title')
        expected_xval_list=['0','40','80','120','160']
        expected_yval_list=['0','30K','60K','90K','120K','150K']
        resobj.verify_riser_chart_XY_labels('wbody1_f', expected_xval_list, expected_yval_list,'Step 06.2 :')
        resobj.verify_riser_legends('wbody1_f',['P9.2M Unit Price'],'Step 06.3 : Verify chart legend label')
        ia_resultobj.verify_number_of_chart_segment('wbody1_f',10,'Step 06.4 : Verify number of chart risers')
        utillobj.verify_chart_color('wbody1_f','riser!s0!g1!mmarker','cerulean_blue_1','Step 06.5 : Verify chart riser color',attribute_type='stroke')
        
        ele=driver.find_element_by_css_selector("#wall1")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step_6', image_type='actual',x=1, y=1, w=-1, h=-1)
        total_summation=len(driver.find_elements_by_css_selector("#dt0_SUM_1_0 [id^='t0_SUM_1_0']"))
        utillobj.asequal(0,total_summation,'Step 06.1 : Verify No summation options are available for scatter diagram')
        
        """
            Step 07:Switch from the Scatter diagram back to the Rollup Report by using the first icon and select RESTORE ORIGINAL.
                    Select the last icon, labeled SUM. Click Avg, then Min, Max, Count & Distinct.
        """
        rollupobj.select_chartmenubar_option('wall1',1,'Restore Original',0,custom_css='cpop')
        time.sleep(2)
        for i in range(len(summation)) :
            print("\n**********"+summation[i]+" Function for Report**********\n")
            rollupobj.select_aggregate_function('wall1', 1,summation[i])
            time.sleep(2)
            miscelaneous_obj.verify_page_summary(1,'10of10records,Page1of1','Step 07.'+str(i)+'.1 : Verify page summary')
#             ia_runobj.create_table_data_set("#wall1 #ITableData1", Test_Case_ID+'_'+summation[i]+'_Ds.xlsx')
            ia_runobj.verify_table_data_set('#wall1 #ITableData1', Test_Case_ID+'_'+summation[i]+'_Ds.xlsx','Step 07.'+str(i)+'.2 : Verify expect to see the report to reflect '+summation[i])
        time.sleep(2)
        miscelaneous_obj.close_popup_dialog('1')
        time.sleep(3)
            
if __name__ == '__main__':
    unittest.main()         