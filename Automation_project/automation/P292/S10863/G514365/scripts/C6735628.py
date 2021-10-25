'''
Created on 19-Nov-2018

@author: Nasir

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6735628
TestCase Name = Verify optional (_FOC_NULL) prompting fields
'''
import unittest
from common.wftools import report
from common.pages import visualization_resultarea
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase

class C6735628_TestClass(BaseTestCase):

    def test_C6735628(self):
        
        """
            CLASS OBJECTS
        """
        
        driver = self.driver
        ia_report=report.Report(self.driver)
        resultobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        
        """
            TESTCASE VARIABLES
        """
        MASTER_FILE_NAME='baseapp/wf_retail_lite'
        Test_Case_ID = "C6735628"
        
        """
            CSS
        """
        filterdialog_css = "#dlgWhere [class*='active'] [class*='caption'] [class*='bi-label']"    
        coln_list = ['ProductCategory', 'Revenue']
        expected_text = 'Create a filtering condition'
        
        
        """    1. Create new IA report using WF_retail_lite
        http://machine:port/alias/ia?is508=false&item=IBFS%3A%2FWFC%2FRepository%2FP292_S10117%2FG456746&tool=report&master=baseapp/wf_retail_lite    """
        ia_report.invoke_ia_tool_using_new_api_login(master=MASTER_FILE_NAME)
                
        """    2. Double click "Product,Category" and "Revenue" fields.
        Verify the following report is displayed.    """
        ia_report.double_click_on_datetree_item("Dimensions->Product->Product->Product,Category", 1)
        ia_report.double_click_on_datetree_item("Measure Groups->Sales->Revenue", 1)
        resultobj.verify_report_titles_on_preview(2, 4, "TableChart_1", coln_list, "Step 02.1: Verify column titles")
        ia_report.verify_report_data_set_in_preview('TableChart_1', 5,2, Test_Case_ID+'_Ds01.xlsx',"Step 02.2: Verify report data set",no_of_cells=4)
        
        """    3. Drag "Product,Subcategory" field into the Filter pane.
        Verify Create a filtering condition window opens.    """
        ia_report.drag_and_drop_from_data_tree_to_filter("Product,Subcategory", 1)
        utillobj.synchronize_with_number_of_element(filterdialog_css, 1, ia_report.report_short_timesleep)
        utillobj.verify_object_visible(filterdialog_css, True, 'Step 03.1: Verify Create a filtering condition window appears.')
        utillobj.verify_element_text(filterdialog_css, expected_text, 'Step 03.2: Verify Create a filtering condition window title.')
        
        
        """    4. Select Parameter in Type dropdown.    """
        ia_report.open_filter_where_value_dialog()
        ia_report.select_filter_type('Parameter')
        
        """    5. Check Optional checkbox and click OK and OK.    """
        ia_report.select_filter_parameter_checkbox(ParamOptional=True)
        ia_report.close_filter_where_value_popup_dialog()
        ia_report.close_filter_dialog()
        
        """    6. Click Run in toolbar.
        Verify report run successfully.    """
        ia_report.select_ia_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_frame(pause=4)
        time.sleep(3)
        ia_report.verify_table_data_set("table[summary= 'Summary']", Test_Case_ID+'_Ds02.xlsx', "Step 6: verify Report data set")
        
        """    7. Logout WF using API:
        http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        driver.switch_to.default_content()
        time.sleep(2)
        utillobj.infoassist_api_logout()
         
if __name__ == '__main__':
    unittest.main()