'''
Created on DEC 05, 2017

@author: Pavithra 

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2227581
TestCase Name = Test Splash Screen and Switch Reports shortcut
'''
import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon,ia_resultarea,ia_styling,ia_run
from common.lib.basetestcase import BaseTestCase

class C2227581_TestClass(BaseTestCase):

    def test_C2227581(self):
        
        Test_Case_ID = "C2227581"
        driver = self.driver
        driver.implicitly_wait(35)
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)  
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)  
        ia_stylingobj = ia_styling.IA_Style(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        
        """        
            Step 01:Launch IA Report mode:
                    http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','ibisamp/CAR','P292/S10032_infoassist_6', 'mrid', 'mrpass')
        parent_css="div[align='justify']"
        resobj.wait_for_property(parent_css, 1,expire_time=20)
        time.sleep(2)
        
        """
            Step 02:Double click "COUNTRY", "CAR", "DEALER_COST", "RETAIL_COST".
        """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        parent_css="#queryTreeWindow tr:nth-child(4) td"
        resobj.wait_for_property(parent_css, 1, string_value='COUNTRY', with_regular_exprestion=True,expire_time=50)
        metaobj.datatree_field_click("CAR", 2, 1)
        parent_css="#queryTreeWindow tr:nth-child(5) td"
        resobj.wait_for_property(parent_css, 1, string_value='CAR', with_regular_exprestion=True,expire_time=50)
        metaobj.datatree_field_click('DEALER_COST', 2, 1)
        parent_css="#queryTreeWindow tr:nth-child(3) td"
        resobj.wait_for_property(parent_css, 1, string_value='DEALER_COST', with_regular_exprestion=True,expire_time=50)
        metaobj.datatree_field_click('RETAIL_COST', 2, 1)
        parent_css="#queryTreeWindow tr:nth-child(4) td"
        resobj.wait_for_property(parent_css, 1, string_value='RETAIL_COST', with_regular_exprestion=True,expire_time=50)
        time.sleep(5)
 
        """
            Step 03:Verify the following report is displayed.
        """
        coln_list = ["COUNTRY", "CAR", "DEALER_COST", "RETAIL_COST"]
        resobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 03: Verify report titles")
#         ia_resultobj.create_report_data_set('TableChart_1', 10, 4, Test_Case_ID+"_Ds01.xlsx")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, Test_Case_ID+"_Ds01.xlsx", 'Step 3.2: Verify report dataset in live preview', no_of_cells=4)
        """
            Step 04:Select "Home" > Style (in Report Group)
        """
        ribbonobj.select_ribbon_item('Home', 'style')

        """
            Step 05:Select Background color = Cyan, Font color = Red, Font size = 12, Justification = Center
            
            Step 06: Click "OK".
        """
        ia_stylingobj.set_report_style(font_size='12', center_justify=True, text_color='red', background_color='cyan', btn_apply=True, btn_ok=True)

        """
            Step 07:Verify "Live Preview" has been applied with the specified style.
        """
        coln_list =  ["COUNTRY", "CAR", "DEALER_COST", "RETAIL_COST"]
        resobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 07.1: Verify Canvas column titles")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, Test_Case_ID+"_Ds01.xlsx", 'Step 07.2: Verify report dataset in live preview', no_of_cells=5)
        ia_resultobj.verify_report_cell_property("TableChart_1", 2, bg_cell_no=2, bg_color='cyan', font_size='12pt', text_align='center', font_color='red', text_value='CAR', msg='Step 07.3: ')
        ia_resultobj.verify_report_cell_property("TableChart_1", 5, bg_cell_no=5, bg_color='cyan', font_size='12pt', text_align='center', font_color='red', text_value='ENGLAND', msg='Step 07.4: ')
        ia_resultobj.verify_report_cell_property("TableChart_1", 9 ,bg_cell_no=9, bg_color='cyan', font_size='12pt', text_align='center', font_color='red', text_value='JENSEN', msg='Step 07.5: ')
        
        """
            Step 08:Click "Run".
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        """
            Step 09:Verify the proper styling is applied to the report in Run mode.
        """
        ia_runobj.verify_table_data_set("table[summary='Summary']", Test_Case_ID+"_Ds02.xlsx", 'Step 09.1: Verify report dataset after run.')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 1, 2, bg_color='cyan', font_size='12pt', text_align='center', font_color='red', text_value='CAR', msg='Step 09.2: ')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 2, 1, bg_color='cyan', font_size='12pt', text_align='center', font_color='red', text_value='ENGLAND', msg='Step 09.3: ')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 5, 2, bg_color='cyan', font_size='12pt', text_align='center', font_color='red', text_value='PEUGEOT', msg='Step 09.4: ')
        
        """
            Step 10:Click "IA" > "Save".
        """ 
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        
        """
            Step 11:Enter Title = "C2227581".
            
            Step 12:Step 12:Click "Save".
        """
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)

        """
            Step 13:Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(5)
        
        """
            Step 14:Reopen saved FEX:
                    
                    http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2227581.fex&tool=Report
        """ 
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10032_infoassist_6',mrid='mrid', mrpass='mrpass')
        parent_css="#queryTreeWindow tr:nth-child(4) td"
        resobj.wait_for_property(parent_css, 1, string_value='RETAIL_COST', with_regular_exprestion=True,expire_time=50)
        """
            Step 15:Verify Preview
        """
        coln_list =  ["COUNTRY", "CAR", "DEALER_COST", "RETAIL_COST"]
        resobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 07.1: Verify Canvas column titles")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, Test_Case_ID+"_Ds01.xlsx", 'Step 07.2: Verify report dataset in live preview', no_of_cells=5)
        ia_resultobj.verify_report_cell_property("TableChart_1", 2, bg_cell_no=2, bg_color='cyan', font_size='12pt', text_align='center', font_color='red', text_value='CAR', msg='Step 15.3: ')
        ia_resultobj.verify_report_cell_property("TableChart_1", 5, bg_cell_no=5, bg_color='cyan', font_size='12pt', text_align='center', font_color='red', text_value='ENGLAND', msg='Step 15.4: ')
        ia_resultobj.verify_report_cell_property("TableChart_1", 9 ,bg_cell_no=9, bg_color='cyan', font_size='12pt', text_align='center', font_color='red', text_value='JENSEN', msg='Step 15.5: ')
        """
            Step 16:Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(2)        
          
if __name__ == '__main__':
    unittest.main() 
        
