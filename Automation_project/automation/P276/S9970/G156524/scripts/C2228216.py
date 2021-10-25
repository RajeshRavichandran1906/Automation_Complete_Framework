'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2228216
TestCase Name = Test drilling all the way down and up an ACROSS hierarchy path - AHTML
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, active_miscelaneous
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2228216_TestClass(BaseTestCase):
    def test_C2228216(self):
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        Test_ID="C2228216"
        Test_Case_ID = Test_ID+"_"+browser_type
        #driver = self.driver
        #driver.implicitly_wait(60)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """    1. Open IA_Shell for edit using the API
        http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FIA-Shell.fex&tool=Report    """
        utillobj.infoassist_api_edit("IA-Shell", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(15)
        
        """    2. Click Format tab > Autodrill button     """
        ribbonobj.select_ribbon_item("Format", "Auto_Drill")
        time.sleep(15)
        
        """    3. Click on HTML output format in status bar and select Active format    """
        ribbonobj.change_output_format_type('active_report', 'status_bar')
        time.sleep(15)
        
        """    4. Click RUN     """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        #iframe=driver.find_element_by_css_selector("iframe[id^='ReportIframe-']")
        #x_fr=iframe.location['x']
        #y_fr=iframe.location['y']
        utillobj.switch_to_frame(1)
        time.sleep(3)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        miscelanousobj.verify_page_summary(0, '28of28records,Page1of1', 'Step 04a: Verify the Report Records')
        column_list=['Store Business Region', 'Product Category', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 04b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds01.xlsx')
        #utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds01.xlsx', 'Step 04c: Verify the report data ')
        time.sleep(4)
        utillobj.switch_to_default_content(1)
        time.sleep(10)
        
        
        """    5. Click on 2016 in the ACROSS labels and Select "Drill down to Sale Year/Quarter "    """
        """    6. Click on 2016 Q4 and Select "Drill down to Sale Year/Month"    """
        """    7. Click on 2016/12 and Select "Drill down to Sale Day"    """
        """    8. Click on 2016/12/31 and select "Drillup to Sale Year/Month"    """
        """    9. Click on 2016/12 and select "Drillup to Sale Year/Quarter"    """       
        """    10. Click on 2016 Q4 and select "Drillup to Sale Year"    """
        
        self.fail(" ACT-618 exist for this case, once it is fixed, script will be updated")       
        
        """    11. Click IA > Save As> Type C2228216 > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    12. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2228216.fex&tool=report    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(14) 
        
        """    13. Click format tab and see Autodrill button is still selected    """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(10)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 112a: Active_Report - Verify Autodrill button is still selected")
        time.sleep(4)
        
        """    14. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()
    
