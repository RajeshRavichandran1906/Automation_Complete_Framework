'''
Created on JUL 26, 2017

@author: Pavithra

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2204971
 TestCase Name = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2204971
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea,active_miscelaneous,ia_resultarea,active_chart_rollup,ia_run
from common.lib import utillity

class C2204971_TestClass(BaseTestCase):

    def test_C2204971(self):
        
        Test_Case_ID="C2204971"
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
            miscelaneous_obj.verify_chart_title('wbody1_ft','P9.2M Unit Price by DATETIME HYYMDSA','Step '+step_num+'.1 : Verify chart title')
            expected_xval_list=['2002/12/31 11:59:59PM','2007/08/08 12:13:14PM','2011/03/30 10:23:24PM','2013/10/04 1:02:03AM']
            expected_yval_list=yaxis_list
            resobj.verify_riser_chart_XY_labels('wbody1_f', expected_xval_list, expected_yval_list,'Step '+step_num+'.2 :')
            resobj.verify_riser_legends('wbody1_f',['P9.2M Unit Price'],'Step '+step_num+'.3 : Verify chart legend label')
            resobj.verify_number_of_riser('wbody1_f',1,4,'Step '+step_num+'.4 : Verify number of chart risers')
            utillobj.verify_chart_color('wbody1_f','riser!s0!g3!mbar!','cerulean_blue_1','Step '+step_num+'.5 : Verify chart riser color')
            miscelaneous_obj.verify_active_chart_tooltip('wbody1_f','riser!s0!g3!mbar',tooltip_value,'Step '+step_num+'.6 : Verify chart tooltip value')
            time.sleep(5)
            ele=driver.find_element_by_css_selector("#wall1")
            utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step_'+step_num, image_type='actual',x=1, y=1, w=-1, h=-1)
            
        def verify_pie_charts(expected_datalabel,tooltip_value,step_num):
            time.sleep(4)
            miscelaneous_obj.verify_chart_title('wbody1_ft','P9.2M Unit Price by DATETIME HYYMDSA','Step '+step_num+'.1 : Verify chart title')
            resobj.verify_data_labels('wbody1_f', expected_datalabel, 'Step '+step_num+'.2 :', custom_css=".chartPanel text[class^='dataLabels']")
            resobj.verify_riser_legends('wbody1_f',['2002/12/31 11:59:59PM','2007/08/08 12:13:14PM','2011/03/30 10:23:24PM','2013/10/04 1:02:03AM'],'Step '+step_num+'.3 : Verify chart legend label')
            resobj.verify_riser_pie_labels_and_legends('wbody1_f', ['P9.2M Unit Price'], "Step 03.4:",custom_css="text[class*='pieLabel']",same_group=True)
            ia_resultobj.verify_number_of_chart_segment('wbody1_f',4,'Step '+step_num+'.4 : Verify number of chart risers')
            utillobj.verify_chart_color('wbody1_f','riser!s3!g0!mwedge!','milky_carrot','Step '+step_num+'.5 : Verify chart riser color')
            miscelaneous_obj.verify_active_chart_tooltip('wbody1_f','riser!s3!g0!mwedge!',tooltip_value,'Step '+step_num+'.6 : Verify chart tooltip value')
            time.sleep(5)
            ele=driver.find_element_by_css_selector("#wall1")
            utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step_'+step_num, image_type='actual',x=1, y=1, w=-1, h=-1)
        
        def verify_line_charts(yaxis_list,tooltip_value,step_num):
            time.sleep(4)
            miscelaneous_obj.verify_chart_title('wbody1_ft','P9.2M Unit Price by DATETIME HYYMDSA','Step '+step_num+'.1 : Verify chart title')
            expected_xval_list=['2002/12/31 11:59:59PM','2007/08/08 12:13:14PM','2011/03/30 10:23:24PM','2013/10/04 1:02:03AM']
            expected_yval_list=yaxis_list
            resobj.verify_riser_chart_XY_labels('wbody1_f', expected_xval_list, expected_yval_list,'Step '+step_num+'.2 :')
            resobj.verify_riser_legends('wbody1_f',['P9.2M Unit Price'],'Step '+step_num+'.3 : Verify chart legend label')
            ia_resultobj.verify_number_of_chart_segment('wbody1_f',5,'Step '+step_num+'.4 : Verify number of chart risers')
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
#         ia_runobj.verify_table_data_set("table[id='ITableData0']", Test_Case_ID+'_Ds01.xlsx',"Step 01.2: AR-RP-141CA.fex data verification")
        column_list=['Order Number INTEGER', 'ALPHA Store Code', 'Date YYMD', 'Date MDYY', 'Date DMYY', 'D10.2 Unit Price', 'P9.2M Unit Price', 'DATETIME HYYMDSA']
        miscelaneous_obj.verify_column_heading('ITableData0', column_list, 'Step 01.2 : Verify the column heading')
        time.sleep(2)
         
        """
            Step 02 : Select P9.2M Unit Price, ROLLUP, then Datetime HYYMDSA as the rollup column.
        """
        miscelaneous_obj.select_menu_items('ITableData0',6,'Rollup','DATETIME HYYMDSA')
        parent_css="#wall1 span[id='wtitle1']"
        utillobj.synchronize_with_visble_text(parent_css, 'P9.2MUnitPricebyDATETIMEHYYMDSA', 30)
        
        miscelaneous_obj.verify_popup_title('wall1','P9.2M Unit Price by DATETIME HYYMDSA','Step 02.1 : Verify popup title')
        
        """
            Step 02.1 :Expect to see a 4 line report with one row for each unique Datetime HYYMDSA value.
                         Use these Summed values to verify the data on the Pie, Bar & Line graphs.
        """
        miscelaneous_obj.verify_page_summary(1,'4of4records,Page1of1','Step 02.3 : Verify page summary')
#         ia_runobj.create_table_data_set("#wall1 #ITableData1", Test_Case_ID+"_Ds02.xlsx")
        ia_runobj.verify_table_data_set('#wall1 #ITableData1', Test_Case_ID+'_Ds02.xlsx','Step 02.4 : Verify 4 line report with one row for each unique Datetime HYYMDSA value')
        miscelaneous_obj.verify_arChartToolbar('wall1', ['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Rollup', 'Advanced Chart', 'Original Chart'],"Step 02.5 : Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('wall1', ['Aggregation'],"Step 02.6 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('wall1', ['Sum'],"Step 02.7 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)  
        utillobj.verify_object_visible("#wall1 .arChartMenuBar div[onclick*='toggleFiltLink']", True, 'Step 03.10 Verify chart rollup lock icon')        
        """
            Step 03 :Switch from the ROLLUP report to a BAR Chart by selecting the second option from the tool bar.
                     Then select the last icon and change SUM to AVG, MIN, MAX, COUNT & DISTINCT. Switch back to SUM for the next step.
                     Expect to see a 4 BAR chart of summed values of P9.2M by Datetime HYYMDSA, one for each unique Datetime value. 
                     Expect to see the graph reflect the AVG, MIN, MAX & COUNT changes.
                     Three BARs represent very small values and will not be visible.
        """       
        rollupobj.click_chart_menu_bar_items('wall1',1)
        yaxis_list={'Sum':['0','100K','200K','300K','400K','500K','600K'],'Avg':['0','100','200','300','400','500','600'],'Min':['0','10','20','30','40','50','60','70'],
                   'Max':['0','300','600','900','1200'],'Count':['0','200','400','600','800','1000','1200'],'Distinct':['0','100','200','300','400','500','600','700']}
           
        bar_tooltip={'Sum':['P9.2M Unit Price: 559K', 'X: 2013/10/04 1:02:03AM'],'Avg':['P9.2M Unit Price: 567.5', 'X: 2013/10/04 1:02:03AM'],'Min':['P9.2M Unit Price: 39', 'X: 2013/10/04 1:02:03AM'],
                   'Max':['P9.2M Unit Price: 1,139', 'X: 2013/10/04 1:02:03AM'],'Count':['P9.2M Unit Price: 985', 'X: 2013/10/04 1:02:03AM'],'Distinct':['P9.2M Unit Price: 664', 'X: 2013/10/04 1:02:03AM']}
        for i in range(len(summation)) :
            print("\n**********"+summation[i]+" Function for bar chart**********\n")
            rollupobj.select_aggregate_function('wall1', 1,summation[i])
            verify_bar_chart(yaxis_list[summation[i]],bar_tooltip[summation[i]],'3.'+str(i))
            
        """
            Step 04 :Switch from the BAR Chart to a PIE Chart by selecting the third option in the tool bar. Check the other Summation options as stated in Step 2.
                     Expect to see a 4 slice PIE chart. Use the values from the Rollup Report to verify the values on the bars. 
                     Verify the other Summation options. 
                     Three PIE slices represent very small values and are nearly zero.
        """
        rollupobj.click_chart_menu_bar_items('wall1',2)
        expected_datalabel={'Sum':['0%','0%','0%','100%'],'Avg':['10%','12%','4%','74%'],'Min':['38%','21%','16%','25%'],'Max':['6%','11%','3%','80%'],
                            'Count':['1%','1%','1%','99%'],'Distinct':['1%','1%','1%','98%']}
           
        pie_tooltip={'Sum':['2013/10/04 1:02:03AM', 'P9.2M Unit Price: 559K', '99.8% of 560K'],'Avg':['2013/10/04 1:02:03AM', 'P9.2M Unit Price: 567.5', '74.1% of 765.7'],'Min':['2013/10/04 1:02:03AM', 'P9.2M Unit Price: 39', '25.3% of 154'],
                   'Max':['2013/10/04 1:02:03AM', 'P9.2M Unit Price: 1,139', '80.3% of 1,418'],'Count':['2013/10/04 1:02:03AM', 'P9.2M Unit Price: 985', '98.5% of 1,000'],'Distinct':['2013/10/04 1:02:03AM', 'P9.2M Unit Price: 664', '97.8% of 679']}
        for i in range(len(summation)) :
            print("\n**********"+summation[i]+" Function for Pie chart**********\n")
            rollupobj.select_aggregate_function('wall1', 1,summation[i])
            verify_pie_charts(expected_datalabel[summation[i]],pie_tooltip[summation[i]],'4.'+str(i))
            
        """
        Step 05: Switch from the PIE Chart to a Line Graph by selecting the fourth option from the tool bar. Check the other Summation options as stated in Step 2.
                 
        """
        rollupobj.click_chart_menu_bar_items('wall1',3)
        yaxis_list={'Sum':['0','100K','200K','300K','400K','500K','600K'],'Avg':['0','100','200','300','400','500','600'],'Min':['0','10','20','30','40','50','60','70'],
                   'Max':['0','300','600','900','1200'],'Count':['0','200','400','600','800','1000','1200'],'Distinct':['0','100','200','300','400','500','600','700']}
        
        line_tooltip={'Sum':['P9.2M Unit Price: 559K', 'X: 2013/10/04 1:02:03AM'],'Avg':['P9.2M Unit Price: 567.5', 'X: 2013/10/04 1:02:03AM'],'Min':['P9.2M Unit Price: 39', 'X: 2013/10/04 1:02:03AM'],
                   'Max':['P9.2M Unit Price: 1,139', 'X: 2013/10/04 1:02:03AM'],'Count':['P9.2M Unit Price: 985', 'X: 2013/10/04 1:02:03AM'],'Distinct':['P9.2M Unit Price: 664', 'X: 2013/10/04 1:02:03AM']}
        for i in range(len(summation)) :
            print("\n**********"+summation[i]+" Function for Line chart**********\n")
            rollupobj.select_aggregate_function('wall1', 1,summation[i])
            verify_line_charts(yaxis_list[summation[i]],line_tooltip[summation[i]],'5.'+str(i))
        """
            Step 06: Switch from the LINE Graph to a Scatter Diagram by selecting the fifth option from the tool bar.
        """
        rollupobj.select_aggregate_function('wall1', 1,"Sum")
        print("\n**********Function for Scatter chart**********\n")
        rollupobj.click_chart_menu_bar_items('wall1',4)
        time.sleep(4)
        miscelaneous_obj.verify_chart_title('wbody1_ft','P9.2M Unit Price by DATETIME HYYMDSA','Step 06.1 : Verify chart title')
        expected_xval_list=['2002/12/31...','2007/08/08...','2011/03/30...','2013/10/04...']
        expected_yval_list=['0','100K','200K','300K','400K','500K','600K']
        resobj.verify_riser_chart_XY_labels('wbody1_f', expected_xval_list, expected_yval_list,'Step 06.2 :')
        resobj.verify_riser_legends('wbody1_f',['P9.2M Unit Price'],'Step 06.3 : Verify chart legend label')
        ia_resultobj.verify_number_of_chart_segment('wbody1_f',4,'Step 06.4 : Verify number of chart risers')
        utillobj.verify_chart_color('wbody1_f','riser!s0!g3!mmarker!','cerulean_blue_1','Step 06.5 : Verify chart riser color',attribute_type='stroke')
        
        ele=driver.find_element_by_css_selector("#wall1")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step_6', image_type='actual',x=1, y=1, w=-1, h=-1)
        total_summation=len(driver.find_elements_by_css_selector("#dt0_SUM_1_0 [id^='t0_SUM_1_0']"))
        utillobj.asequal(0,total_summation,'Step 06.1 : Verify No summation options are available for scatter diagram')
        
        """
            Step 07:Switch from the Scatter diagram back to the Rollup Report by using the first icon and select RESTORE ORIGINAL. Select the last icon, labeled SUM. Click Avg, then Min, Max, Count & Distinct.
        """
        rollupobj.select_chartmenubar_option('wall1',1,'Restore Original',0,custom_css='cpop')
        time.sleep(2)
        for i in range(len(summation)) :
            print("\n**********"+summation[i]+" Function for Report**********\n")
            rollupobj.select_aggregate_function('wall1', 1,summation[i])
            time.sleep(2)
            miscelaneous_obj.verify_page_summary(1,'4of4records,Page1of1','Step 07.'+str(i)+'.1 : Verify page summary')
#             ia_runobj.create_table_data_set("#wall1 #ITableData1", Test_Case_ID+'_'+summation[i]+'_Ds.xlsx')
            ia_runobj.verify_table_data_set('#wall1 #ITableData1', Test_Case_ID+'_'+summation[i]+'_Ds.xlsx','Step 07.'+str(i)+'.2 : Verify expect to see the report to reflect '+summation[i])
        time.sleep(2)
        miscelaneous_obj.close_popup_dialog('1')
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()    
            
            