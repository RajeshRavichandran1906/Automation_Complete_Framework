'''
Created on JUL 20, 2017

@author: Pavithra

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2204960
 TestCase Name = Chart Rollup using an Integer by a Numeric field.
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea,active_miscelaneous,ia_resultarea,active_chart_rollup,ia_run
from common.lib import utillity

class C2204960_TestClass(BaseTestCase):

    def test_C2204960(self):
        
        Test_Case_ID="C2204960"
        
        """            TESTCASE VARIABLES
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
            miscelaneous_obj.verify_chart_title('wbody1_ft','Order Number INTEGER by D10.2 Unit Price','Step '+step_num+'.1 : Verify chart title')
            expected_xval_list=['13','17','26','28','58','76','81','96','125','140']
            expected_yval_list=yaxis_list
            resobj.verify_riser_chart_XY_labels('wbody1_f', expected_xval_list, expected_yval_list,'Step '+step_num+'.2 :')
            resobj.verify_riser_legends('wbody1_f',['Order Number INTEGER'],'Step '+step_num+'.3 : Verify chart legend label')
            resobj.verify_number_of_riser('wbody1_f',1,10,'Step '+step_num+'.4 : Verify number of chart risers')
            utillobj.verify_chart_color('wbody1_f','riser!s0!g5!mbar','cerulean_blue_1','Step '+step_num+'.5 : Verify chart riser color')
            miscelaneous_obj.verify_active_chart_tooltip('wbody1_f','riser!s0!g6!mbar',tooltip_value,'Step '+step_num+'.6 : Verify chart tooltip value')
            time.sleep(5)
            ele=driver.find_element_by_css_selector("#wall1")
            utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step_'+step_num, image_type='actual',x=1, y=1, w=-1, h=-1)
            
        def verify_pie_charts(expected_datalabel,tooltip_value,step_num):
            time.sleep(4)
            miscelaneous_obj.verify_chart_title('wbody1_ft','Order Number INTEGER by D10.2 Unit Price','Step '+step_num+'.1 : Verify chart title')
            resobj.verify_data_labels('wbody1_f', expected_datalabel, 'Step '+step_num+'.2 :', custom_css=".chartPanel text[class^='dataLabels']")
            resobj.verify_riser_legends('wbody1_f',['13','17','26','28','58','76','81','96','125','140'],'Step '+step_num+'.3 : Verify chart legend label')
            resobj.verify_riser_pie_labels_and_legends('wbody1_f', ['Order Number INTEGER'], "Step 03.4:",custom_css="text[class*='pieLabel']",same_group=True)
            ia_resultobj.verify_number_of_chart_segment('wbody1_f',10,'Step '+step_num+'.4 : Verify number of chart risers')
            utillobj.verify_chart_color('wbody1_f','riser!s0!g0!mwedge','cerulean_blue_1','Step '+step_num+'.5 : Verify chart riser color')
            miscelaneous_obj.verify_active_chart_tooltip('wbody1_f','riser!s0!g0!mwedge!',tooltip_value,'Step '+step_num+'.6 : Verify chart tooltip value')
            time.sleep(5)
            ele=driver.find_element_by_css_selector("#wall1")
            utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step_'+step_num, image_type='actual',x=1, y=1, w=-1, h=-1)
        
        def verify_line_charts(yaxis_list,tooltip_value,step_num):
            time.sleep(4)
            miscelaneous_obj.verify_chart_title('wbody1_ft','Order Number INTEGER by D10.2 Unit Price','Step '+step_num+'.1 : Verify chart title')
            expected_xval_list=['13','17','26','28','58','76','81','96','125','140']
            expected_yval_list=yaxis_list
            resobj.verify_riser_chart_XY_labels('wbody1_f', expected_xval_list, expected_yval_list,'Step '+step_num+'.2 :')
            resobj.verify_riser_legends('wbody1_f',['Order Number INTEGER'],'Step '+step_num+'.3 : Verify chart legend label')
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
        parent_css="#MAINTABLE_wbody0 span[title='Move to Bottom'] img"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 65)
        
        miscelaneous_obj.verify_page_summary(0,'1000of1000records,Page1of18', 'Step 01.1: Verify Page summary')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID + "_Ds01.xlsx")
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID + "_Ds01.xlsx", "Step 01.2: AR-RP-141CA.fex data verification")
        miscelaneous_obj.verify_column_heading('ITableData0', ['OrderNumberINTEGER', 'ALPHAStoreCode', 'DateYYMD', 'DateMDYY', 'DateDMYY', 'D10.2UnitPrice', 'P9.2MUnitPrice', 'DATETIMEHYYMDSA'], 'Step 01.3 : Verify report column heading')
        time.sleep(2)
         
        """
            Step 02 : Select Order Number INTEGER, ROLLUP, then D10.2 Unit Price as the rollup column..
        """
        miscelaneous_obj.select_menu_items('ITableData0',0,'Rollup','D10.2 Unit Price')
        parent_css="#wall1 span[id='wtitle1']"
        resobj.wait_for_property(parent_css, 1,string_value='OrderNumberINTEGERbyD10.2UnitPrice',with_regular_exprestion=True)
        miscelaneous_obj.verify_popup_title('wall1','Order Number INTEGER by D10.2 Unit Price','Step 02.1 : Verify popup title')
         
        """
            Step 02.1 : Expect to see a 10 line report with one row for each unique D10.2 Unit Price value
        """
        miscelaneous_obj.verify_page_summary(1,'10of10records,Page1of1','Step 02.3 : Verify page summary')
#         ia_runobj.create_table_data_set("#wall1 #ITableData1", Test_Case_ID+"_Ds02.xlsx")
        ia_runobj.verify_table_data_set('#wall1 #ITableData1', Test_Case_ID+'_Ds02.xlsx','Step 02.4 : Verify expect to see a 12 line report with one row for each unique D10.2 Unit Price value')
        miscelaneous_obj.verify_arChartToolbar('wall1', ['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Rollup', 'Advanced Chart', 'Original Chart'],"Step 02.5 : Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('wall1', ['Aggregation'],"Step 02.6 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('wall1', ['Sum'],"Step 02.7 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)  
        utillobj.verify_object_visible("#wall1 .arChartMenuBar div[onclick*='toggleFiltLink']", True, 'Step 03.10 Verify chart rollup lock icon')        
        """
            Step 03 :Switch from the ROLLUP report to a BAR Chart by selecting the second option from the tool bar.
                    Then select the last icon and change SUM to AVG, MIN, MAX, COUNT & DISTINCT. Switch back to SUM for the next step.
        """
        rollupobj.click_chart_menu_bar_items('wall1',1)
        yaxis_list={'Sum':['0','20K','40K','60K','80K','100K','120K'],'Avg':['0','100','200','300','400','500','600'],'Min':['0','5','10','15','20','25','30','35','40'],
                   'Max':['0','200','400','600','800','1000','1200'],'Count':['0','40','80','120','160','200','240'],'Distinct':['0','40','80','120','160','200','240']}
           
        bar_tooltip={'Sum':['Order Number INTEGER: 109K', 'X: 81'],'Avg':['Order Number INTEGER: 499.3', 'X: 81'],'Min':['Order Number INTEGER: 3', 'X: 81'],
                   'Max':['Order Number INTEGER: 994', 'X: 81'],'Count':['Order Number INTEGER: 218', 'X: 81'],'Distinct':['Order Number INTEGER: 218', 'X: 81']}
        for i in range(len(summation)) :
            rollupobj.select_aggregate_function('wall1', 1,summation[i])
            verify_bar_chart(yaxis_list[summation[i]],bar_tooltip[summation[i]],'3.'+str(i))
           
        """
            Step 04 :Switch from the BAR Chart to a PIE Chart by selecting the third option in the tool bar. Check the other Summation options as stated in Step 2.
        """
        rollupobj.click_chart_menu_bar_items('wall1',2)
        expected_datalabel={'Sum':['8%','10%','13%','15%','8%','3%','22%','7%','7%','7%'],'Avg':['10%','10%','10%','10%','10%','10%','10%','10%','10%','10%'],'Min':['10%','12%','5%','13%','1%','32%','3%','7%','8%','9%'],
                   'Max':['10%','10%','10%','10%','10%','10%','10%','10%','10%','10%'],'Count':['8%','10%','13%','15%','8%','3%','22%','7%','7%','7%'],'Distinct':['8%','10%','13%','15%','8%','3%','22%','7%','7%','7%']}
           
        pie_tooltip={'Sum':['13','Order Number INTEGER: 42,216', '8.4% of 501K'],'Avg':['13','Order Number INTEGER: 502.6', '10.0% of 5,007'],'Min':['13','Order Number INTEGER: 11', '10.0% of 110'],
                   'Max':['13','Order Number INTEGER: 1,000', '10.1% of 9,929'],'Count':['13', 'Order Number INTEGER: 84', '8.4% of 1,000'],'Distinct':['13', 'Order Number INTEGER: 84', '8.4% of 1,000']}
        for i in range(len(summation)) :
            rollupobj.select_aggregate_function('wall1', 1,summation[i])
            verify_pie_charts(expected_datalabel[summation[i]],pie_tooltip[summation[i]],'4.'+str(i))
  
        """
            Step 05 :Switch from the PIE Chart to a Line Graph by selecting the fourth option from the tool bar. Then select the last icon and change SUM to AVG, MIN, MAX, COUNT & DISTINCT.
                    Check the other Summation options as stated in Step 2.
        """
        rollupobj.click_chart_menu_bar_items('wall1',3)
        yaxis_list={'Sum':['0','20K','40K','60K','80K','100K','120K'],'Avg':['0','100','200','300','400','500','600'],'Min':['0','5','10','15','20','25','30','35','40'],
                   'Max':['0','200','400','600','800','1000','1200'],'Count':['0','40','80','120','160','200','240'],'Distinct':['0','40','80','120','160','200','240']}
          
        line_tooltip={'Sum':['Order Number INTEGER: 109K', 'X: 81'],'Avg':['Order Number INTEGER: 499.3', 'X: 81'],'Min':['Order Number INTEGER: 3', 'X: 81'],
                   'Max':['Order Number INTEGER: 994', 'X: 81'],'Count':['Order Number INTEGER: 218', 'X: 81'],'Distinct':['Order Number INTEGER: 218', 'X: 81']}
        for i in range(len(summation)) :
            rollupobj.select_aggregate_function('wall1', 1,summation[i])
            verify_line_charts(yaxis_list[summation[i]],line_tooltip[summation[i]],'5.'+str(i))
        
        """
            Step 06: Switch from the Line Graph to a Scatter Diagram by selecting the fifth option from the tool bar.
                     Expect to see a multipoint scatter diagram. This will produce a detail diagram. No Summation options are available.
        """
        rollupobj.select_aggregate_function('wall1', 1,"Sum")
        rollupobj.click_chart_menu_bar_items('wall1',4)
        time.sleep(4)
        miscelaneous_obj.verify_chart_title('wbody1_ft','Order Number INTEGER by D10.2 Unit Price','Step 06.1 : Verify chart title')
        expected_xval_list=['0','40','80','120','160']
        expected_yval_list=['0','20K','40K','60K','80K','100K','120K']
        resobj.verify_riser_chart_XY_labels('wbody1_f', expected_xval_list, expected_yval_list,'Step 06.2 :')
        resobj.verify_riser_legends('wbody1_f',['Order Number INTEGER'],'Step 06.3 : Verify chart legend label')
        ia_resultobj.verify_number_of_chart_segment('wbody1_f',10,'Step 06.4 : Verify number of chart risers')
        utillobj.verify_chart_color('wbody1_f','riser!s0!g1!mmarker','cerulean_blue_1','Step 06.5 : Verify chart riser color',attribute_type='stroke')
        tooltip_value=['Order Number INTEGER', 'X: 81', 'Y: 109K']
        miscelaneous_obj.verify_active_chart_tooltip('wbody1_f','riser!s0!g6!mmarker!',tooltip_value,'Step 06.6 : Verify chart tooltip value')
        ele=driver.find_element_by_css_selector("#wall1")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step_6', image_type='actual',x=1, y=1, w=-1, h=-1)
        total_summation=len(driver.find_elements_by_css_selector("#dt0_SUM_1_0 [id^='t0_SUM_1_0']"))
        utillobj.asequal(0,total_summation,'Step 06.1 : Verify No summation options are available for scatter diagram')
        
        """
            Step 07:Switch from the Scatter diagram back to the Rollup Report by using the first icon and select RESTORE ORIGINAL. Select the last icon, labeled SUM. 
                    Click Avg, then Min, Max, Count & Distinct.
        """
        rollupobj.select_chartmenubar_option('wall1',1,'Restore Original',0,custom_css='cpop')
        time.sleep(2)
        for i in range(len(summation)) :
            rollupobj.select_aggregate_function('wall1', 1,summation[i])
            time.sleep(2)
            miscelaneous_obj.verify_page_summary(1,'10of10records,Page1of1','Step 07.'+str(i)+'.1 : Verify page summary')
#             ia_runobj.create_table_data_set("#wall1 #ITableData1", Test_Case_ID+'_'+summation[i]+'_Ds.xlsx')
            ia_runobj.verify_table_data_set('#wall1 #ITableData1', Test_Case_ID+'_'+summation[i]+'_Ds.xlsx','Step 07.'+str(i)+'.2 : Verify expect to see the report to reflect '+summation[i])
       
        
if __name__ == '__main__':
    unittest.main()     