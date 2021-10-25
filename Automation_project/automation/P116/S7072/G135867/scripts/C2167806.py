'''
Created on Sep 27, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7070&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2167806
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity

class C2167806_TestClass(BaseTestCase):

    def test_C2167806(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        """
        Step 01: Execute the attached repro - act-886-report.fex
        """
        utillobj.active_run_fex_api_login("act-886-report.fex", "S7072", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 01.1: Execute the act-886-report.fex and Verify the Report Heading')
        column_list=['COUNTRY','CAR','DEALER_COST']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Execute the act-886-report.fex and Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', 'act-886-report.xlsx', 'Step 01.3: Execute the act-886-report.fex and Verify the entire data')
        
        val = '[id="THEAD_0_4_0_0"] span'
        font_size = self.driver.find_elements_by_css_selector(val)
        value1 = font_size[0].value_of_css_property('font-size')
        value2 = font_size[1].value_of_css_property('font-size')
        
        new_val1=int(value1[:2])
        new_val2=int(value2[:2])

        
        if(new_val1==new_val2):
            utillobj.asequal(new_val1,18,'Step 01.4: Expect to see Country - ENGLAND with a large font for Heading' )
        else:
            self.fail('Step 01.4: Expect to see Country - ENGLAND with a large font for Heading - Failed')
            
        utillobj.infoassist_api_logout()
        
        """
        Step 02: Execute the attached repro - act-886-chart.fex
        """
        
        utillobj.active_run_fex_api_login("act-886-chart.fex", "S7072", 'mrid', 'mrpass')
        
        val_report = '[id="MAINTABLE_wbody0_f"] span'
        report_font_size = self.driver.find_elements_by_css_selector(val_report)
        value3 = report_font_size[0].value_of_css_property('font-size')
        value4 = report_font_size[1].value_of_css_property('font-size')
        
        new_val3=int(value3[:2])
        new_val4=int(value4[:2])
        
        if(new_val3==new_val4):
            utillobj.asequal(new_val3,16,'Step 02: Expect to see Country - ENGLAND with a large font for Heading' )
        else:
            self.fail('Step 02: Expect to see Country - ENGLAND with a large font for Heading - Failed')
            
        
if __name__ == "__main__":
    unittest.main()