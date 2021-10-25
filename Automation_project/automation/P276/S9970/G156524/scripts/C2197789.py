'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2197789
TestCase Name = Restore Auto Drill enabled fex shows Define field _FOC_NULL in Data pane
'''
import unittest
from common.lib import utillity  
from common.wftools import report
from common.lib.basetestcase import BaseTestCase

class C2197789_TestClass(BaseTestCase):
    
    def test_C2197789(self):
        
        Test_ID="C2197789"
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        Test_Case_ID = Test_ID+"_"+browser_type
        report_obj=report.Report(self.driver)
        
        """    
            Step 01 : Launch the IA report API with wf_retail_lite    
        """
        report_obj.invoke_ia_tool_using_api_login("report", "ibisamp/carolap")
        report_obj.wait_for_visible_text("#queryTreeColumn", "Sum", report_obj.home_page_long_timesleep)
        
        """    
            Step 02 : Add COUNTRY to By in the query panel    
        """
        element_css= "#queryTreeColumn"
        report_obj.double_click_on_datetree_item("COUNTRY->COUNTRY->COUNTRY", 3)
        report_obj.wait_for_visible_text(element_css, "COUNTRY")
        
        """    
            Step 03 : Click Format tab > Autodrill button
        """
        report_obj.select_ia_ribbon_item("Format", "auto_drill")
        report_obj.wait_for_number_of_element("[id='FormatAutoDrill'][class*='checked ']", 1)
        
        """    
            Step 04 : Click IA > Save As> Type C2197789 > click Save   
        """
        report_obj.save_as_from_application_menu_item(Test_Case_ID)
        report_obj.api_logout()
      
        """    
            Step 05 : Open the just saved C2197789 in IA+ editor    
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_visble_text("#queryTreeColumn table>tbody>tr:nth-child(4)>td", 'COUNTRY', expire_time=8)
        
        """
            Step 05.1 : Ensure that FOCNULL does not appear in the field list
        """
        actual_list=[]
        expected_list=['Measures', 'SEATS', 'DEALER_COST', 'RETAIL_COST', 'SALES', 'WIDTH', 'HEIGHT', 'WEIGHT', 'WHEELBASE', 'FUEL_CAP', 'BHP', 'RPM', 'MPG', 'ACCEL', 'Dimensions', 'WARRANTY', 'STANDARD', 'COUNTRY', 'BODYTYPE']
        datatree_items = self.driver.find_elements_by_css_selector("[id^=QbMetaDataTree] table>tbody>tr")
        actual_list.extend([i.text for i in datatree_items if i!=None])
        actual_list=' '.join(actual_list).split()
        utillobj.asequal(expected_list, actual_list, "Step 05.01 : Ensure that FOCNULL does not appear in the field list")
           
        """   
            Step  06 : Close the browser window    
        """
        utillobj.infoassist_api_logout()
        
if __name__ == '__main__':
    unittest.main()
