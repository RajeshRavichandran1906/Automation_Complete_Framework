'''
Created on 20-Jan-2017

@author: Aftab

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2222797
TestCase Name = Verify Rank on Measure field, add TL condition on Rank column and on Virtual Sort
'''
import unittest
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run, ia_styling
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from common.lib import core_utility

class C2222797_TestClass(BaseTestCase):

    def test_C2222797(self):
        
        Test_Case_ID = "C2222797"
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_stylingobj = ia_styling.IA_Style(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        selection_list = ["COUNTRY","CAR","DEALER_COST"]
        
        """ 1. Launch IA Report mode:
               http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10006
        """
        utillobj.infoassist_api_login('report','ibisamp/car','P278/S10006', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """ 2. Double click COUNTRY, CAR, DEALER_COST            """
        for text in selection_list:
            metaobj.datatree_field_click(text, 2, 1)
            utillobj.synchronize_with_visble_text("#queryTreeColumn", text, metaobj.chart_medium_timesleep)
        
        """ 3. Click on DEALER_COST in query pane and click on Rank button from Field tab        """
        metaobj.querytree_field_click('DEALER_COST', 1, 1, 'Sort', 'Rank', 'On')
        
        """ 4. Now click on Virtual sort field 'DEALER_COST' in query pane under By                """
        metaobj.querytree_field_click('DEALER_COST', 2)
        
        """ 5. Click on Display button from Field tab (If display group not expanded in Field tab )        """
        """ 6. Display tab expands -> Click on Traffic Lights                                              """
        ribbonobj.select_ribbon_item('Field', 'trafficlights')
        
        """ 7. Select the value dropdown arrow and enter value = "6000" and click "Ok"                    """
        ia_stylingobj.traffic_light_create_new(1, filter_type='Constant', value_box_input='6000')
        
        """ 8. Now click on Style tab Make some changes Bold, Italic, Font size -12, color - Purple rgb(128,0,128), Background color - Yellow (rgb(255,255,0))        """
        ia_stylingobj.traffic_light_toolbar_select('Style', 1, bold=True, italic=True, font_size='12', text_color='purple', background_color='yellow')
        
        """ 9. Click "Ok" verify the preview reflected by the applied TL condition        """
        ia_stylingobj.traffic_light_close_dialog('Ok')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['RANK', 'DEALER_COST','COUNTRY', 'CAR', 'DEALER_COST']
        resultobj.verify_report_titles_on_preview(5, 5, "TableChart_1", coln_list, "Step 9: Verify Canvas column titles ")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 5, Test_Case_ID+"_Ds01.xlsx", 'Step 9.1: Verify Canvas report dataset ')
        ia_resultobj.verify_report_cell_property("TableChart_1", 7, font_size='9pt', font_color='gray8', text_value='2,626', msg='Step 9.2:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 32, bg_cell_no=1, bg_color='yellow', bold=True, italic=True, font_size='12pt', font_color='purple', text_value='14,940', msg='Step 9.3:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 42, bg_cell_no=3, bg_color='yellow', bold=True, italic=True, font_size='12pt', font_color='purple', text_value='18,621', msg='Step 9.4:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 52, bg_cell_no=5, bg_color='yellow', bold=True, italic=True, font_size='12pt', font_color='purple', text_value='49,500', msg='Step 9.5:')
        
        
        """ 10. Click on RANK field in canvas                """
        ia_resultobj.select_field_on_canvas("TableChart_1", 1)
        
        
        """ 11. Click on Field tab -> Display button (If not expanded), Open Traffic Lights        """
        ribbonobj.select_ribbon_item('Field', 'trafficlights')
        
        
        """ 12. Click on values dropdown menu                  """
        """ 13. Now click on the ""Get Values"" menu And Select "All" from the dropdown menu > 4,292 > OK    """   
        ia_stylingobj.traffic_light_create_new(1, filter_type='Constant', getvalue_params='All', value='4,292')
        
        
        """ 14. Now click on Style tab Make some changes Bold, Italic, Font size -12, color - BLUE rgb(0,0,255), Background color - Yellow (rgb(255,255,0))        """
        ia_stylingobj.traffic_light_toolbar_select('Style', 1, bold=True, italic=True, font_size='12', text_color='blue', background_color='yellow')
        
        """ 15. Click apply and "Ok", Verify the preview applied with TL condition        """
        ia_stylingobj.traffic_light_close_dialog('Ok')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['RANK', 'DEALER_COST','COUNTRY', 'CAR', 'DEALER_COST']
        resultobj.verify_report_titles_on_preview(5, 5, "TableChart_1", coln_list, "Step 15: Verify Canvas column titles ")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 5, Test_Case_ID+"_Ds01.xlsx", 'Step 15.1: Verify Canvas report dataset ')
        ia_resultobj.verify_report_cell_property("TableChart_1", 7, font_size='9pt', font_color='gray8', text_value='2,626', msg='Step 15.2:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 32, bg_cell_no=4, bg_color='yellow', bold=True, italic=True, font_size='12pt', font_color='purple', text_value='14,940', msg='Step 15.3:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 42, bg_cell_no=8, bg_color='yellow', bold=True, italic=True, font_size='12pt', font_color='purple', text_value='18,621', msg='Step 15.4:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 52, bg_cell_no=12, bg_color='yellow', bold=True, italic=True, font_size='12pt', font_color='purple', text_value='49,500', msg='Step 15.5:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 11, font_color='gray8', font_size='9pt', text_value='2', msg='Step 15.6:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 16, font_color='gray8', font_size='9pt', text_value='3', msg='Step 15.7:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 21, bg_cell_no=1, bg_color='yellow', bold=True, italic=True, font_size='12pt', font_color='blue', text_value='4', msg='Step 15.8:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 36, bg_cell_no=5, bg_color='yellow', bold=True, italic=True, font_size='12pt', font_color='blue', text_value='7', msg='Step 15.9:')
        
        
        """ 16. Click "Run"        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.synchronize_with_number_of_element('[id^=ReportIframe-]', 1, resultobj.chart_medium_timesleep)
        core_util_obj.switch_to_frame()
        
        """ 17. Verify that TL condition applied on Rank column and on Virtual Sort        """
        ia_runobj.verify_table_data_set("table[summary='Summary']", Test_Case_ID+"_run_Ds01.xlsx" , 'Step 16: Verify report dataset')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 3, 1, font_size='9pt', font_color='gray8', text_value='2', msg='Step 16.1:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 4, 1, font_size='9pt', font_color='gray8', text_value='3', msg='Step 16.2:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 5, 1, bg_color='yellow', font_size='12pt', font_color='blue', text_value='4', bold=True, italic=True, msg='Step 16.3:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 8, 1, bg_color='yellow', font_size='12pt', font_color='blue', text_value='7', bold=True, italic=True, msg='Step 16.4:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 6, 2, font_size='9pt', font_color='gray8', text_value='5,063', msg='Step 16.5:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 7, 2, bg_color='yellow', font_size='12pt', font_color='purple', text_value='14,940',bold=True, italic=True,  msg='Step 16.6:')
        
        """ 18. Click "IA" menu > "Save As" > "C2222797" > Click Save            """
        core_util_obj.switch_to_default_content()
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as("ia"+Test_Case_ID)
        
        """ 19. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp        """
        core_util_obj.switch_to_default_content()
        utillobj.infoassist_api_logout()
        
        """ 20. Reopen saved FEX:
                http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2222797.fex&tool=Report
        """
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        utillobj.infoassist_api_edit("ia"+Test_Case_ID, 'report', 'S10006', mrid='mrid', mrpass='mrpass')
        
        """ 21. Verify Preview                """
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['RANK', 'DEALER_COST','COUNTRY', 'CAR', 'DEALER_COST']
        resultobj.verify_report_titles_on_preview(5, 5, "TableChart_1", coln_list, "Step 21: Verify Canvas column titles ")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 5, Test_Case_ID+"_Ds01.xlsx", 'Step 21.1: Verify Canvas report dataset ')
        ia_resultobj.verify_report_cell_property("TableChart_1", 7, font_size='9pt', font_color='gray8', text_value='2,626', msg='Step 21.2:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 32, bg_cell_no=4, bg_color='yellow', bold=True, italic=True, font_size='12pt', font_color='purple', text_value='14,940', msg='Step 21.3:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 42, bg_cell_no=8, bg_color='yellow', bold=True, italic=True, font_size='12pt', font_color='purple', text_value='18,621', msg='Step 21.4:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 52, bg_cell_no=12, bg_color='yellow', bold=True, italic=True, font_size='12pt', font_color='purple', text_value='49,500', msg='Step 21.5:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 11, font_color='gray8', font_size='9pt', text_value='2', msg='Step 21.6:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 16, font_color='gray8', font_size='9pt', text_value='3', msg='Step 21.7:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 21, bg_cell_no=1, bg_color='yellow', bold=True, italic=True, font_size='12pt', font_color='blue', text_value='4', msg='Step 21.8:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 36, bg_cell_no=5, bg_color='yellow', bold=True, italic=True, font_size='12pt', font_color='blue', text_value='7', msg='Step 21.9:')
        
        """ 22. Logout:    http://machine:port/ibi_apps/service/wf_security_logout.jsp        """
        
if __name__ == '__main__':
    unittest.main()