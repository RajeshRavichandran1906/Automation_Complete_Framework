'''
Created on Nov 15, 2017

@author: Niranjan

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227527
Test case Name =  Verify output formats HTML, Active Report, PDF
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_ribbon, ia_resultarea, ia_run, active_miscelaneous
from common.lib import utillity

class C2227527_TestClass(BaseTestCase):

    def test_C2227527(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227527'
        driver = self.driver 
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
        1 Launch IA Report mode:
        http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','ibisamp/car','P292/S10032_infoassist_4', 'mrid', 'mrpass')
        elem1="#TableChart_1"
        utillobj.synchronize_with_number_of_element(elem1, 1, 30)
        
        """
        2. Double click "COUNTRY", "CAR", "DEALER_COST".
        """
        metaobj.datatree_field_click('COUNTRY', 2, 1)
        parent_css="#queryTreeWindow table tr:nth-child(4) td"
        resultobj.wait_for_property(parent_css, 1,expire_time=15, string_value='COUNTRY', with_regular_exprestion=True)
        metaobj.datatree_field_click('CAR', 2, 1)
        parent_css="#queryTreeWindow table tr:nth-child(5) td"
        resultobj.wait_for_property(parent_css, 1,expire_time=15, string_value='CAR', with_regular_exprestion=True)
        metaobj.datatree_field_click('DEALER_COST', 2, 1)
        parent_css="#queryTreeWindow table tr:nth-child(3) td"
        resultobj.wait_for_property(parent_css, 1,expire_time=15, string_value='DEALER_COST', with_regular_exprestion=True)
        utillobj.synchronize_with_number_of_element("[id*='ActivePreviewItem']", 6, 20)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 3.1: Verify Canvas column titles")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 3, Test_Case_ID+"_Ds01.xlsx", 'Step 2.1: Verify report dataset', no_of_cells=4)
        
        """ 
        3. Select "IA" > Save as "C2227527" > Click "Save".
        """    
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(8)
        
        """ 
        4. Click "HTML" dropdown.
        5. Verify the following output formats are available and default selection is HTML
        """ 
        list1=['HTML', 'Active Report', 'PDF', 'Excel (xlsx)', 'PowerPoint (pptx)'] 
        ia_ribbonobj.select_or_verify_output_type(launch_point='Home', expected_output_list1=list1, msg1="Step 5. Verify output formats.", item_select_path='HTML')
        
        """
        6. Click "Run".
        7. Verify the HTML formatted report is generated.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        ia_runobj.verify_table_data_set("table[summary='Summary']", Test_Case_ID+"_Ds02.xlsx", 'Step 7: Verify HTML format report After Run') 
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2) 
          
        """
        8. Select "Active Report" format.
        """    
        ia_ribbonobj.select_or_verify_output_type(launch_point='Home', item_select_path='Active Report')
        
        """ 
        9. Click "Run".
        10. Verify the "Active Report" formatted report is generated.
        """  
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        active_misobj.verify_page_summary('0','10of10records,Page1of1', 'Step 10.1: Verify Page summary')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds03.xlsx',"Step 10.2: Verify 5active data set")
        utillobj.switch_to_default_content(pause=1)
        time.sleep(3)  
        
        """
        11. Select "PDF" format.
        """    
        ia_ribbonobj.select_or_verify_output_type(launch_point='Home', item_select_path='PDF')
        
        """ 
        12. Click "Run".
        13. Verify the "PDF" formatted report is generated.
        """  
        browser=utillobj.parseinitfile('browser')
        ribbonobj.select_top_toolbar_item('toolbar_run') 
        time.sleep(8) 
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step12'+'_'+browser, image_type='actual')  
        time.sleep(3)
        
        """
        14. Click "Save"
        """    
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """ 
        15. Logout:
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """    
        utillobj.infoassist_api_logout()
        
        """ 
        16. Reopen saved FEX:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2227527.fex&tool=Report
        """    
        uname="input[id='SignonUserName']"
        utillobj.synchronize_with_number_of_element(uname, 1, 20)
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10032_infoassist_4', mrid='mrid', mrpass='mrpass')
        elem1="#TableChart_1"
        utillobj.synchronize_with_number_of_element(elem1, 1, 20)
        
        """ 
        17. Verify output format is set to PDF
        """   
        elem1="#HomeFormatType img[src$='format_pdf_32.png']"
        utillobj.synchronize_with_number_of_element(elem1, 1, 20) 
        utillobj.verify_object_visible("#HomeFormatType img[src$='format_pdf_32.png']", True, 'Step 17: Verify output format is set to PDF.')
        
        """
        18. Logout:
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()
        