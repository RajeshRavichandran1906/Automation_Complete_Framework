'''
Created on Jan 24, 2018

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251738
Test_Case Name : AHTML:CMPD reports/charts;ARFILTER doesn`t filter all (136688)
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import ia_run, active_miscelaneous
from common.lib import utillity

class C2251738_TestClass(BaseTestCase):

    def test_C2251738(self):
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID='C2251738'
        utillobj = utillity.UtillityMethods(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        active=active_miscelaneous.Active_Miscelaneous(self.driver)
        
        def verify_chart(parent_css, chart_title,xaxis_label, yaxis_label, total_risers, step_num, verify_color=True):
            utillobj.verify_element_text(parent_css+ " div[style*='Arial']>div[style]", chart_title, 'Step ' + step_num + '.1 : Verify Chart title')
            actual_axis_labels=[xaxis.text.strip() for xaxis in self.driver.find_elements_by_css_selector(parent_css+ " .chartContainer div[style*='10pt']")]
            actual_yxis_labels=[yaxis.text.strip() for yaxis in self.driver.find_elements_by_css_selector(parent_css+ " .chartContainer div[style*='12pt']")]
            utillobj.asequal(xaxis_label, actual_axis_labels, 'Step ' + step_num + '.2 : Verify X-Axis labels')
            utillobj.asequal(actual_yxis_labels, yaxis_label, 'Step ' + step_num + '.3 : Verify y-Axis labels')
            actual_risers=len(self.driver.find_elements_by_css_selector(parent_css+ " div[style*='rect'][title]"))
            utillobj.asequal(actual_risers, total_risers, 'Step ' + step_num + '.4 : Verify number of chart risers')
            if verify_color :
                utillobj.verify_element_color_using_css_property(parent_css+ " div[style*='rect'][title]", 'Lochmara', 'Step ' + step_num + '.4 : Verify chart first riser color', 'background-color')
            active.verify_arChartToolbar('MAINTABLE_wmenu'+parent_css[-1], ['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation'], 'Step ' + step_num + '.5 : Verify chart tool bars', custom_css='[title]')
            active.verify_arChartToolbar('MAINTABLE_wmenu'+parent_css[-1], ['Sum'], 'Step ' + step_num + '.6 : Verify Aggregation type', text=True, custom_css="[id^='SUM'] td[class^='tabPagingTex']")
        
        def verify_report(index, filename, page_summary, step_num):
            #iarun.create_table_data_set('#ITableData'+str(index), Test_Case_ID+'_'+filename+'.xlsx')
            iarun.verify_table_data_set('#ITableData'+str(index), Test_Case_ID+'_'+filename+'.xlsx', 'Step ' + step_num + '.1 : Verify Report '+str(index+1)+' data')
            active.verify_page_summary(index, page_summary, 'Step ' + step_num + '.2 : Verify Report '+str(index+1)+' page summary')
            
        """
            Step 01 : Execute 136688.fex from repro
        """
        utillobj.active_run_fex_api_login('136688.fex', 'S10071_5', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#ITableData0 #TCOL_0_C_0>tt", 'COUNTRY', 60)
        
        """
            Step 01.1 : Verify output Chart
        """
        xaxis_label=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        verify_chart('#MAINTABLE_4', 'SALES by COUNTRY,', xaxis_label, ['0', '20 K', '40 K', '60 K', '80 K', '100 K'], 4, '1A')
        verify_chart('#MAINTABLE_5', 'RETAIL_COST by COUNTRY,', xaxis_label, ['0', '20 K', '40 K', '60 K', '80 K'], 5, '1B')
        verify_chart('#MAINTABLE_6', 'DEALER_COST by COUNTRY,', xaxis_label, ['0', '20 K', '40 K', '60 K'], 5, '1C')
        verify_chart('#MAINTABLE_7', 'SEATS by COUNTRY,', xaxis_label, ['0', '10', '20', '30', '40'], 5, '1D')
        
        """
            Step 01.2 : Verify output Report
        """
        for i in range(4) :
            verify_report(i, 'DataSet0'+str(i+1), '10of10records,Page1of1', '1E')
        utillobj.verify_dropdown_value("#combobox_dsCOMBOBOX_1", ['[All]','ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY'], 'Step 1F.1 : Verify dropdown box values', '[All]', 'Step 1F.2 : Verify [All] is selected as default in dropdown box')
        
        """
            Step 02  : Select France in the dropdown box
        """
        utillobj.select_dropdown("#combobox_dsCOMBOBOX_1", 'visible_text', 'FRANCE')
        time.sleep(2)
        
        """
            Step 03 : Verify all the report and chart get filtered based on country"France"
        """
        xaxis_label=['FRANCE']
        verify_chart('#MAINTABLE_4', 'SALES by COUNTRY,', xaxis_label, ['-1.00', '0', '1.00'], 0, '3A', verify_color=False)
        verify_chart('#MAINTABLE_5', 'RETAIL_COST by COUNTRY,', xaxis_label, ['5000', '5200', '5400', '5600', '5800', '6000', '6200'], 1, '3B')
        verify_chart('#MAINTABLE_6', 'DEALER_COST by COUNTRY,', xaxis_label, ['4000', '4200', '4400', '4600', '4800', '5000', '5200'], 1, '3C')
        verify_chart('#MAINTABLE_7', 'SEATS by COUNTRY,', xaxis_label, ['4.4', '4.6', '4.8', '5.0', '5.2', '5.4', '5.6'], 1, '3D')
        
        for i in range(4) :
            verify_report(i, 'DataSet0'+str(i+5), '1of10records,Page1of1', '3E')
            
if __name__ == '__main__':
    unittest.main()