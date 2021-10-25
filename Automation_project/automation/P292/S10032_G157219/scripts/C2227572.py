'''
Created on Dec 6, 2017

@author: BM13368
TestCase ID : http://172.19.2.180/testrail/index.php?/cases/view/2227572
TestCase Name : Verify adding styling to report  
'''
import unittest, time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run, ia_styling
from common.lib.basetestcase import BaseTestCase

class C2227572_TestClass(BaseTestCase):

    def test_C2227572(self):
        
        """    TESTCASE VARIABLES    """
        Test_Case_ID = 'C2227572'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        vis_ribbon_obj=visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultarea_obj=ia_resultarea.IA_Resultarea(self.driver)
        ia_stylingobj = ia_styling.IA_Style(self.driver)
        ia_run_obj=ia_run.IA_Run(self.driver)
        """
            Step 01:Launch IA Report mode:
            http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','ibisamp/car','P292/S10032_infoassist_3', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        """
            Step 02:Double click "COUNTRY", "CAR", "DEALER_COST".
        """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("CAR", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('DEALER_COST', 2, 1)
        time.sleep(4)
        """ 
            Step 03:Verify the following report is displayed.
        """
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 03:00: Verify Preview column titles")
#         ia_resultarea_obj.create_report_data_set('TableChart_1', 10, 3, Test_Case_ID+"_Ds01.xlsx")
        ia_resultarea_obj.verify_report_data_set('TableChart_1', 10, 3, Test_Case_ID+"_Ds01.xlsx", 'Step 03:01: Verify report dataset')
        """
            Step 04:Select "Home" > "Report" icon (If not expanded)
            Step 05:Click "Style" icon.
        """
        vis_ribbon_obj.select_ribbon_item('Home', 'style')     
           
        """ 
            Step 06:Change Font Size = 12, Italic, Font Color = RED, Background color = YELLOW.
            Step 07:Click "OK".
        """
        ia_stylingobj.set_report_style(font_size='12', italic=True, text_color='red', background_color='yellow', btn_apply=True, btn_ok=True)    
           
        """ 
            Step 08:Verify the style applied to the report on "Live Preview".
        """
        ia_resultarea_obj.verify_report_data_set('TableChart_1', 10, 3, Test_Case_ID+"_Ds01.xlsx", 'Step 08:01: Verify report dataset')
        ia_resultarea_obj.verify_report_cell_property("TableChart_1", 15, bg_cell_no=17, bg_color='yellow', font_color='red', text_value='ALFA ROMEO', font_size='12pt', italic=True, msg='Step 08:02: ')
        ia_resultarea_obj.verify_report_cell_property("TableChart_1", 4, bg_cell_no=4, bg_color='yellow', font_color='red', text_value='ENGLAND', font_size='12pt', italic=True, msg='Step 08:03: ')
        ia_resultarea_obj.verify_report_cell_property("TableChart_1", 12, bg_cell_no=14, bg_color='yellow', font_color='red', text_value='PEUGEOT', font_size='12pt', italic=True, msg='Step 08:04: ')
        ia_resultarea_obj.verify_report_cell_property("TableChart_1", 27, bg_cell_no=33, bg_color='yellow', font_color='red', text_value="BMW", font_size='12pt', italic=True, msg='Step 08:05: ')
        
        """ 
            Step 09:Click "Run".
        """
        vis_ribbon_obj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)       
        """
            Step 10:Verify the report is displayed.
        """
#         ia_run_obj.create_table_data_set("table[summary='Summary']", Test_Case_ID+"_run_Ds01.xlsx")
        ia_run_obj.verify_table_data_set("table[summary='Summary']", Test_Case_ID+"_run_Ds01.xlsx" , 'Step 10:01: Verify report dataset')
        ia_run_obj.verify_table_cell_property("table[summary='Summary']", 1, 2, bg_color='yellow', font_color='red', text_value='CAR', font_size='12pt', italic=True, msg='Step 10:02: ')
        ia_run_obj.verify_table_cell_property("table[summary='Summary']", 5, 3, bg_color='yellow', font_color='red', text_value='4,631', font_size='12pt', italic=True, msg='Step 10:03: ')
        ia_run_obj.verify_table_cell_property("table[summary='Summary']", 7, 2, bg_color='yellow', font_color='red', text_value='MASERATI', font_size='12pt', italic=True, msg='Step 10:04: ')
        """ 
            Step 11:Click "IA" > "Save".
            Step 12:Enter Title = "C2227572".
            Step 13:Click "Save".
        """
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        vis_ribbon_obj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)    
        
        """ 
            Step 14:Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        """ 
            Step 15:Reopen saved FEX:
            http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2227572.fex&tool=Report
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10032_infoassist_3',mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        """ 
            Step 16:Verify successful restore
        """
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 16:00: Verify Preview column titles")
        ia_resultarea_obj.verify_report_data_set('TableChart_1', 10, 3, Test_Case_ID+"_Ds01.xlsx", 'Step 16:01: Verify report dataset')
        ia_resultarea_obj.verify_report_cell_property("TableChart_1", 15, bg_cell_no=17, bg_color='yellow', font_color='red', text_value='ALFA ROMEO', font_size='12pt', italic=True, msg='Step 16:02: ')
        ia_resultarea_obj.verify_report_cell_property("TableChart_1", 4, bg_cell_no=4, bg_color='yellow', font_color='red', text_value='ENGLAND', font_size='12pt', italic=True, msg='Step 16:03: ')
        ia_resultarea_obj.verify_report_cell_property("TableChart_1", 12, bg_cell_no=14, bg_color='yellow', font_color='red', text_value='PEUGEOT', font_size='12pt', italic=True, msg='Step 16:04: ')
        ia_resultarea_obj.verify_report_cell_property("TableChart_1", 27, bg_cell_no=33, bg_color='yellow', font_color='red', text_value="BMW", font_size='12pt', italic=True, msg='Step 16:05: ')
        """
            Step 17:Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()

if __name__ == "__main__":
    unittest.main()