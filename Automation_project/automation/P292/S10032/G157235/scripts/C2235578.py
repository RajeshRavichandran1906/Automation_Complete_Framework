'''
Created on Nov 24, 2017

@author: Robert
TestCase Name : Verify Excel output formats
TestCase ID : http://172.19.2.180/testrail/index.php?/cases/view/2235578
'''
import unittest, time
from common.pages import visualization_metadata, visualization_ribbon, ia_ribbon 
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase

class C2235578_TestClass(BaseTestCase):

    def test_C2235578(self):
        
        Test_Case_ID = "C2235578"
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        
        """    
        1. Launch IA Report mode:  
        """
        utillobj.infoassist_api_login('report','ibisamp/car','P292/S10032_infoassist_4', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 20)
         
        """    
        2. Double click "COUNTRY", "CAR", "DEALER_COST".    
        """
        metaobj.datatree_field_click('COUNTRY', 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('CAR', 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('DEALER_COST', 2, 1)
        time.sleep(4)
         
        """    
        3. Select "IA" > Save as "C2235578" > Click "Save".    
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
         
        """    
        4. Click "HTML" dropdown > Verify the following formats are available.    
        """
        list1=['HTML', 'Active Report', 'PDF', 'Excel (xlsx)', 'PowerPoint (pptx)']
        ia_ribbobj.select_or_verify_output_type(launch_point="Home", expected_output_list=list1, msg='Step 4. Verify the formats')
          
        """    
        5. Click arrow in the "Excel (xlsx)" menu to access sub menu > Verify Excel output formats
        6. Select "Excel" 
        7. Click "Run".    
        """
        list2=['Excel (xlsx)', 'Excel', 'Excel Formula (xlsx)', 'Excel Formula', 'Excel (csv)']
        ia_ribbobj.select_or_verify_output_type(launch_point="Home",item_select_path='Excel (xlsx)->Excel',  expected_output_list2=list2, msg2='Step 5. Verify Excel output formats')
        ribbonobj.select_top_toolbar_item('toolbar_run')
        
        """
        8. Verify the "Excel" formatted report (xls) is downloaded.
        9. Close Excel application    
        """
        time.sleep(8)
        utillobj.save_file_from_browser('C2235578_actual_1', custom_cr_re="Untitled")
        utillobj.verify_xml_xls('C2235578_actual_1.xls', 'C2235578_base_1.xls', 'Step 8. Verify the "Excel" formatted report (xls) is downloaded.')
        time.sleep(2)
        utillobj.switch_to_main_window()
        
        """    
        10. Click "Excel" dropdown > Select "Excel > Excel Formula" format.
        11. Click "Run".    
        """
        time.sleep(4)
        utillobj.synchronize_with_number_of_element('#applicationButton img', 1, 20)
        ia_ribbobj.select_or_verify_output_type(launch_point="Home",item_select_path='Excel->Excel Formula')
        ribbonobj.select_top_toolbar_item('toolbar_run')
        
        """    
        12. Verify the "Excel Formula" formatted report (xls) is downloaded.
        13. Close Excel application    
        """
        utillobj.save_file_from_browser('C2235578_actual_2', custom_cr_re="Untitled")
        utillobj.verify_xml_xls('C2235578_actual_2.xls', 'C2235578_base_2.xls', 'Step 12. Verify the "Excel Formula" formatted report (xls) is downloaded.')
        time.sleep(2)
        utillobj.switch_to_main_window()
        
        """    
        14. Click "Save"
        15. Logout:    
        """
        time.sleep(4)
        utillobj.synchronize_with_number_of_element('#applicationButton img', 1, 20)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """    
        16. Reopen saved FEX:
        17. Verify output format is set to "Excel Formula"    
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10032_infosassist_4', mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 20)
        utillobj.verify_element_text("#HomeFormatType>div[id^='BiLabel']",'Excel Formula','Step 17. Verify output format is set to "Excel Formula"')
        
        """
        18. Click "Excel Formula" dropdown > Select "Excel Formula > Excel Formula (xlsx)" format.    
        """
        ia_ribbobj.select_or_verify_output_type(launch_point="Home",item_select_path='Excel Formula->Excel Formula (xlsx)')
        ribbonobj.select_top_toolbar_item('toolbar_run')
        
        """    
        19. Verify the "Excel Formula (xlsx)" formatted report (xlsx) is downloaded.
        20. Close Excel application    
        """
        utillobj.save_file_from_browser('C2235578_actual_3', custom_cr_re="Untitled")
        utillobj.verify_xml_xls('C2235578_actual_3.xlsx', 'C2235578_base_3.xlsx', 'Step 19. Verify the "Excel Formula (xlsx)" formatted report (xlsx) is downloaded.')
        time.sleep(2)
        utillobj.switch_to_main_window()
            
        """    
        21. Click "Excel Formula (xlsx)" dropdown > Select "Excel Formula (xlsx) > Excel (xlsx)" format.
        22. Click "Run".    
        """
        time.sleep(4)
        utillobj.synchronize_with_number_of_element('#applicationButton img', 1, 20)
        ia_ribbobj.select_or_verify_output_type(launch_point="Home",item_select_path='Excel Formula (xlsx)->Excel (xlsx)')
        ribbonobj.select_top_toolbar_item('toolbar_run')
        
        """    
        23. Verify the "Excel (xlsx)" formatted report (xlsx) is downloaded.
        24. Close Excel application    
        """
        utillobj.save_file_from_browser('C2235578_actual_4', custom_cr_re="Untitled")
        utillobj.verify_xml_xls('C2235578_actual_4.xlsx', 'C2235578_base_4.xlsx', 'Step 23. Verify the "Excel (xlsx)" formatted report (xlsx) is downloaded.')
        time.sleep(2)
        utillobj.switch_to_main_window()
            
        """    
        25. Click "Save"  
        """
        time.sleep(4)
        utillobj.synchronize_with_number_of_element('#applicationButton img', 1, 20)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        
        """    
        26. Logout:    
        """
        utillobj.infoassist_api_logout()
        
        """    
        27. Reopen saved FEX:
        28. Verify output format is set to "Excel (xlsx)"    
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10032_infosassist_4', mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 20)
        utillobj.verify_element_text("#HomeFormatType>div[id^='BiLabel']",'Excel (xlsx)','Step 27. Verify Output format is set to "Excel (xlsx)')
        
        """    
        29. Logout:    
        """
        time.sleep(3)   

if __name__ == "__main__":
    unittest.main()