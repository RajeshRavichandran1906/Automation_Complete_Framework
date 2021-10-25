'''
Created on Nov 24, 2017

@author: Robert
TestCase Name : Verify Excel output formats
TestCase ID : http://172.19.2.180/testrail/index.php?/cases/view/2235578
'''
import unittest, time
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_ribbon 
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase

class C2235578_TestClass(BaseTestCase):

    def test_C2235578(self):
        
        Test_Case_ID = "C2235578"
        driver=self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        
        """    1. Launch IA Report mode:  """
        utillobj.infoassist_api_login('report','ibisamp/CAR','P292/S10032_infoassist_4', 'mrid', 'mrpass')
#         utillobj.infoassist_api_edit('C2235578', 'report', 'P292/S10032_infoassist_4', mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
         
        """    2. Double click "COUNTRY", "CAR", "DEALER_COST".    """
         
        metaobj.datatree_field_click('COUNTRY', 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('CAR', 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('DEALER_COST', 2, 1)
        time.sleep(4)
         
        """    "3. Select "IA" > Save as "C2235578" > Click "Save".    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
         
        """    "4. Click "HTML" dropdown > Verify the following formats are available.    """
         
        list1=['HTML', 'Active Report', 'PDF', 'Excel (xlsx)', 'PowerPoint (pptx)']
        ia_ribbobj.select_or_verify_output_type(launch_point="Home", expected_output_list1=list1, msg1='Step 4. Verify the formats')
         
        """    "5. Click arrow in the "Excel (xlsx)" menu to access sub menu > Verify Excel output formats    """
        """    "6. Select "Excel"    """
        """    "7. Click "Run".    """
         
        list2=['Excel (xlsx)', 'Excel', 'Excel Formula (xlsx)', 'Excel Formula']
        ia_ribbobj.select_or_verify_output_type(launch_point="Home",item_select_path='Excel (xlsx)',  expected_output_list2=list2)
         
        ribbonobj.select_top_toolbar_item('toolbar_run')
        
        
        """    "8. Verify the "Excel" formatted report (xls) is downloaded.    """
        """    "9. Close Excel application    """

        ''' code to download and verify excel'''
        utillobj.save_file_from_browser('C2235578_Ds01_actual.xls')
        utillobj.verify_excel_sheet('C2235578_Ds01.xls', 'C2235578_Ds01_actual.xls', 'C2235578', 'Step 8. Verify the Excel xls file that is downloaded')
        
        
        """    10. Click "Excel" dropdown > Select "Excel > Excel Formula" format.    """
        """    11. Click "Run".    """
        
        ia_ribbobj.select_or_verify_output_type(launch_point="Home",item_select_path='Excel (xlsx)->Excel Formula')
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        
        
        
        """    12. Verify the "Excel Formula" formatted report (xls) is downloaded."""
        """    13. Close Excel application    """
        
        ''' code to download and verify excel'''
        
        utillobj.save_file_from_browser('C2235578_Ds02_actual.xls')
        
        '''Verifying Excel formula using xlrd throws error need to use/try openpyxl'''
        #utillobj.verify_excel_sheet('C2235578_Ds02.xls', 'C2235578_Ds02_actual.xls', 'C2235578', 'Step 12. Verify the Excel Formula xls file that is downloaded')
        
        
        """    14. Click "Save"    """
        """    15. Logout:    """
        
        
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        
        """    16. Reopen saved FEX:    """
        """    17. Verify output format is set to "Excel Formula"    """
        
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10032_infosassist_4', mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(8)
        
        def_output_css="div[id='HomeFormatType'] div[id^='BiLabel']"
        
        ele1=self.driver.find_element_by_css_selector(def_output_css)
        
        utillobj.asequal(ele1.text.strip(), 'Excel Formula', 'Step 17. Verify Output format is set to "Excel Formula')
        
        """      18. Click "Excel Formula" dropdown > Select "Excel Formula > Excel Formula (xlsx)" format.    """
        ia_ribbobj.select_or_verify_output_type(launch_point="Home",item_select_path='Excel Formula->Excel Formula (xlsx)')
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        
        
        """    19. Verify the "Excel Formula (xlsx)" formatted report (xlsx) is downloaded.    """
        """    20. Close Excel application    """
        
        ''' code to download and verify excel'''
        utillobj.save_file_from_browser('C2235578_Ds03_actual.xlsx')
        
        '''Verifying Excel formula using xlrd throws error need to use/try openpyxl'''
        #utillobj.verify_excel_sheet('C2235578_Ds03.xlsx', 'C2235578_Ds03_actual.xlsx', 'C2235578', 'Step 19. Verify the Excel Formula xlsx file that is downloaded')
        
        """    21. Click "Excel Formula (xlsx)" dropdown > Select "Excel Formula (xlsx) > Excel (xlsx)" format.    """
        """    22. Click "Run".    """
        ia_ribbobj.select_or_verify_output_type(launch_point="Home",item_select_path='Excel Formula (xlsx)->Excel (xlsx)')
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        
        
        """    23. Verify the "Excel (xlsx)" formatted report (xlsx) is downloaded.    """
        """    24. Close Excel application    """
        
        ''' code to download and verify excel'''
        utillobj.save_file_from_browser('C2235578_Ds04_actual.xlsx')
        utillobj.verify_excel_sheet('C2235578_Ds04.xlsx', 'C2235578_Ds04_actual.xlsx', 'C2235578', 'Step 23. Verify the Excel xlsx file that is downloaded')
        
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        
        
        """    25. Logout:    """
        """    26. Reopen saved FEX:    """
        """    27. Verify output format is set to "Excel (xlsx)"    """
        """    28. Logout:    """
        utillobj.infoassist_api_logout()
        
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10032_infosassist_4', mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        
        def_output_css="div[id='HomeFormatType'] div[id^='BiLabel']"
        
        ele1=self.driver.find_element_by_css_selector(def_output_css)
        
        utillobj.asequal(ele1.text.strip(), 'Excel (xlsx)', 'Step 27. Verify Output format is set to "Excel (xlsx)')
        
        utillobj.infoassist_api_logout()
        
            

if __name__ == "__main__":
    unittest.main()