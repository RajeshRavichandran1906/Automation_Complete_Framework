'''
Created on Jan 16, 2019

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5751528
TestCase_Name : Verify that reopening Document does not affect "Include ALL" option
'''
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.visualization import Visualization
from common.lib.basetestcase import BaseTestCase
from common.wftools import document
from common.wftools import report
from common.lib import utillity
import unittest, time

class C5751528_TestClass(BaseTestCase):

    def test_C5751528(self):
        
        """
        TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        coreutils= CoreUtillityMethods(self.driver)       
        report_obj = report.Report(self.driver)
        doc_obj=document.Document(self.driver)
        visual_obj=Visualization(self.driver)
        
        """
        COMMON VARIABLES
        """
        MEDIUM_WAIT_TIME = 60
        report_parent_css="TableChart_1"
        prompt_css="#Prompt_1"
        fex_name="AR-AD-09a"
        folder_name='P116/S10071_1'
        
        """
        Step 01: Sign in to WebFOCUS as a basic user
        http://machine:port/{alias}
        Step 02: Execute the following URL:
        http://machine:port/{alias}/ia?tool=document&master=ibisamp/ggsales&item=IBFS%3A%2FWFC%2FRepository%2FP116%2FS10071_1%2F
        """
        report_obj.invoke_ia_tool_using_api_login(tool='document', master='ibisamp/ggsales', report_css='#resultArea', no_of_element=1, wait_time=MEDIUM_WAIT_TIME)
          
        """
        Step 03: Add Category, Product,Unit Sales to get a report
        """
        report_obj.double_click_on_datetree_item('Category', 1)
        report_obj.wait_for_visible_text("#queryTreeColumn tr:nth-child(4)", 'Category', MEDIUM_WAIT_TIME)
          
        report_obj.double_click_on_datetree_item('Product', 1)
        report_obj.wait_for_visible_text("#queryTreeColumn tr:nth-child(5)", 'Product', MEDIUM_WAIT_TIME)
          
        report_obj.double_click_on_datetree_item('Unit Sales', 1)
        report_obj.wait_for_visible_text("#queryTreeColumn tr:nth-child(3)", 'Unit Sales', MEDIUM_WAIT_TIME)
          
        coln_list=['Category', 'Product', 'Unit Sales']
        report_obj.verify_column_title_on_preview(colnum=3, no_of_cells=3, table_id=report_parent_css, expected_list=coln_list, msg="Step 03.01: Verify column titles")
          
        """
        Step 04: Now, select Drop down button from 'Insert' tab
        """
        doc_obj.select_ia_ribbon_item('Insert', 'Drop_Down')
        report_obj.wait_for_number_of_element(prompt_css,  expected_number=1, time_out=MEDIUM_WAIT_TIME)
        doc_obj.repositioning_document_component_in_ia('5', '1')
        time.sleep(3)
          
        """    
        Step 05. Right click on Drop down button select properties    
        """
        doc_obj.choose_right_click_menu_item_for_prompt(prompt_css, item_name='Properties')
        time.sleep(5) 
          
        """    
        Step 06. In Active Dashboard Properties assign UNIT SALES in 'Field'. Make sure Include All is checked already and Condition is Equal to. 
        Step 07. Click Ok.  
        """
        ComboBox_1_source = {'select_field':'Unit Sales', 'verify_condition':'Equal to', 'verify_includeall':True}
        ComboBox_1_target = {'verify_target_name':['Report1']}
        doc_obj.customize_active_dashboard_properties(source=ComboBox_1_source, targets=ComboBox_1_target, msg="Step 06", btn_type='ok') 
        time.sleep(3)
          
        """    
        Step 08. Save and close the report as AHTML as AR-AD-09a.fex.   
        """
        report_obj.save_report_from_toptoolbar()
        report_obj.save_file_in_save_dialog(fex_name)
        doc_obj.api_logout()
         
        """    
        Step 09. Now open the report again in IA (Edit), and right click on dropdown, and select properties.    
        """
        visual_obj.edit_fex_using_api_url(folder_name=folder_name, tool='document', fex_name=fex_name, mrid='mrid', mrpass='mrpass')
        report_obj.wait_for_number_of_element("#TableChart_1 div[class^='x']", 8, time_out=MEDIUM_WAIT_TIME)
        coln_list=['Category', 'Product', 'Unit Sales']
        report_obj.verify_column_title_on_preview(colnum=3, no_of_cells=3, table_id=report_parent_css, expected_list=coln_list, msg="Step 09: Verify column titles")
        report_obj.wait_for_number_of_element(prompt_css,  expected_number=1, time_out=MEDIUM_WAIT_TIME)
        doc_obj.choose_right_click_menu_item_for_prompt(prompt_css, item_name='Properties')
        time.sleep(3) 
         
        """    
        Step 10. "Include All" should be checked on reopening the saved report
        """
        ComboBox_1_source = {'verify_field':'Unit Sales', 'verify_condition':'Equal to', 'verify_includeall':True}
        doc_obj.customize_active_dashboard_properties(source=ComboBox_1_source, msg="Step 10.", btn_type='ok') 
        doc_obj.api_logout()
         
        """    
        Step 11. Verify Include All gets generated in the syntax (ARFILTER_SHOWALL=ON)
        """
        utillobj.invoke_webfocu('mrid', 'mrpass')
        node = coreutils.parseinitfile('nodeid')
        port = coreutils.parseinitfile('httpport')
        context = coreutils.parseinitfile('wfcontext')
        setup_url = 'http://' + node + ':' + port + context + '/'+'TED?rootFolderPath=IBFS%253A%252FWFC%252FRepository&folderPath=IBFS%253A%252FWFC%252FRepository%252FP116%252FS10071_1%252F&itemName=AR-AD-09a.fex'
        self.driver.get(setup_url)
        text_editor_css = "[class*='text-editor'] .ace_text-layer"
        utillobj.synchronize_with_number_of_element(text_editor_css, 1, 60)
        text_editor_obj=utillobj.validate_and_get_webdriver_object(text_editor_css, "Text_editor source code")
        actual_value=text_editor_obj.text.strip()
        expected_value="ARFILTER_SHOWALL='ON'"
        utillobj.asin(expected_value, actual_value, "Step 11.01: Verify Include All gets generated in the syntax (ARFILTER_SHOWALL=ON)")
        
        """    
        Step 12. Dismiss the window
        """
        
if __name__ == "__main__":
    unittest.main()