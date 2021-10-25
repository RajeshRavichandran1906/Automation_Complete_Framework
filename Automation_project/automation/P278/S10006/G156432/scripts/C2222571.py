'''
Created on 23-Dec-2016

@author: Aftab

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2222571
TestCase Name = Verify Styling with Traffic Lights
'''
import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run, ia_styling
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2222571_TestClass(BaseTestCase):

    def test_C2222571(self):
        
        Test_Case_ID = "C2222571"
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        ia_stylingobj = ia_styling.IA_Style(self.driver)
        
        
        """ 1. Launch IA Report mode:
               http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10006
        """
        utillobj.infoassist_api_login('report','ibisamp/car','P278/S10006', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        
        """ 2. Select "COUNTRY","CAR","DEALER_COST","RETAIL_COST".    """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("CAR", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('DEALER_COST', 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('RETAIL_COST', 2, 1)
        time.sleep(8)
        
        
        """ 3. Select DEALER_COST in the Query window                 """
        metaobj.querytree_field_click('DEALER_COST', 1)
        
        
        """ 4. Click Traffic Lights in the Display section            """
        ribbonobj.select_ribbon_item('Field', 'trafficlights')
        
        
        """ 5. Click down arrow next to 0 > click get value > All > Select 6000        """
        time.sleep(2)
        ia_stylingobj.traffic_light_create_new(1, filter_type='Constant', getvalue_params='All', value='6,000 (6000)')
        
        
        """ 6. Click Style in the Traffic light window            """
        """ 7. Select Font COMIC SANS ME                          """
        time.sleep(2)
        ia_stylingobj.traffic_light_toolbar_select('Style', 1, font_name='COMIC SANS MS')
        time.sleep(2)
        
        
        """ 8. Click Apply > Click OK                             """
        ia_stylingobj.traffic_light_close_dialog('Apply')
        time.sleep(2)
        ia_stylingobj.traffic_light_close_dialog('Ok')
        time.sleep(2)
        ia_resultobj.verify_report_cell_property("TableChart_1", 7, text_value='18,621', msg='Step 8.1:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 35, text_value='5,063', msg='Step 8.2:')
        
        
        """ 9. Select RETAIL_COST in the Query window            """
        metaobj.querytree_field_click('RETAIL_COST', 1)
        
        
        """ 10. Click Traffic Lights in the Display section      """
        ribbonobj.select_ribbon_item('Field', 'trafficlights')
        
        
        """ 11. Click down arrow next to 0 > click get value > All > Select 5970        """
        time.sleep(2)
        ia_stylingobj.traffic_light_create_new(1, filter_type='Constant', getvalue_params='All', value='5,970 (5970)')
        
        
        """ 12. Click Style in the Traffic light window        """
        """ 13. Select Font COMIC SANS ME                     """
        time.sleep(2)
        ia_stylingobj.traffic_light_toolbar_select('Style', 1, font_name='COMIC SANS MS')
        
        
        """ 14. Click Apply > Click OK                        """
        ia_stylingobj.traffic_light_close_dialog('Apply')
        time.sleep(2)
        ia_stylingobj.traffic_light_close_dialog('Ok')
        time.sleep(2)
        ia_resultobj.verify_report_cell_property("TableChart_1", 10, text_value='14,940', msg='Step 14.1:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 38, text_value='49,500', msg='Step 14.2:')
        
        
        """ 15. Click Header and Footer in the Report Section    """
        """ 16. In Report Header > type Report Header > set Font to Comic Sans MS > Font color to Blue > Background color to Yellow    """
        time.sleep(2)
        ia_stylingobj.create_header_footer('ribbon','Report Header', 'Report Header', font_name='COMIC SANS MS', text_color='blue',background_color='yellow')
        
        
        """ 17. In Report Footer > type Report Footer > set Font to Comic Sans MS > Font color to Blue > Background color to Yellow    """
        """ 18. Click Apply > Click OK            """
        time.sleep(2)
        ia_stylingobj.create_header_footer('frame', 'Report Footer', 'Report Footer', font_name='COMIC SANS MS', text_color='blue',background_color='yellow', btn_apply=True, btn_ok=True)
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 1, cell_no=1, bg_color='yellow', msg='Step 18: ')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 1, font_color='blue', text_value='Report Header', font_name='Comic Sans MS', msg='Step 18.1:')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 2, cell_no=2, bg_color='yellow', msg='Step 18.2: ')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 2, font_color='blue', text_value='Report Footer', font_name='Comic Sans MS', msg='Step 18.3:')
        
        
        """ 19. Click Style in the Report section        """
        ribbonobj.select_ribbon_item('Home', 'style')
        
        """ 20. Click Font Color > Select Magenta        """
        """ 21. Click Background Color > Select Cyan     """
        """ 22. Click Apply and click ok                 """
        ia_stylingobj.set_report_style(bold=True, text_color='magenta', background_color='cyan', btn_apply=True, btn_ok=True)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 22.1: Verify Canvas column titles After Apply Style")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, Test_Case_ID+"_Ds01.xlsx", 'Step 22.2: Verify report dataset After Apply Style')
        ia_resultobj.verify_report_cell_property("TableChart_1", 5, bg_cell_no=5,bg_color='cyan', font_color='magenta', text_value='ENGLAND', msg='Step 22.3:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 37, bg_cell_no=42,bg_color='cyan', font_color='magenta', text_value='BMW', msg='Step 22.4:')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 1, cell_no=1, bg_color='yellow', msg='Step 22.5: ')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 1, font_color='blue', text_value='Report Header', font_name='Comic Sans MS', msg='Step 22.6:')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 2, cell_no=46, bg_color='yellow', msg='Step 22.7: ')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 2, font_color='blue', text_value='Report Footer', font_name='Comic Sans MS', msg='Step 22.8:')
        
        
        """ 23. Click Run and verify output              """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        ia_runobj.verify_table_data_set("table[summary='Summary']", Test_Case_ID+"_run_Ds01.xlsx" , 'Step 23: Verify report dataset')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 3, 3, bg_color='cyan', font_color='magenta', text_value='DEALER_COST', msg='Step 23.1:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 8, 2, bg_color='cyan', font_color='magenta', text_value='ALFA ROMEO', msg='Step 23.2:')
        ia_runobj.verify_header_footer_stying(1, bg_color='yellow', font_color='blue', text_value='Report Header', font_name='comic sans ms', font_size='14pt', 
                                             msg='Step 23.3: IA-6269 -  Header&Footer: Unable to change font size for the text after changing font style')
        ia_runobj.verify_header_footer_stying(2, bg_color='yellow', font_color='blue', text_value='Report Footer', font_name='comic sans ms', font_size='10pt', 
                                             msg='Step 23.4: IA-6269 -  Header&Footer: Unable to change font size for the text after changing font style')
        
        
        """ 24. Click Save in the toolbar > Save As C2222571 > click Save        """
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        
        
        """ 25. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp        """
        time.sleep(2)
        utillobj.infoassist_api_logout()
        
        
        """ 26. Reopen saved FEX:
                http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2222571.fex&tool=Report
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10006', mrid='mrid', mrpass='mrpass')
        
        """ 27. Verify Preview                    """
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 27.1: Verify Preview column titles")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, Test_Case_ID+"_Ds01.xlsx", 'Step 27.2: Verify report dataset')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 1, cell_no=1, bg_color='yellow', msg='Step 27.3: ')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 1, font_color='blue', text_value='Report Header', font_name='Comic Sans MS', msg='Step 27.4:')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 2, cell_no=46, bg_color='yellow', msg='Step 27.5: ')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 2, font_color='blue', text_value='Report Footer', font_name='Comic Sans MS', msg='Step 27.6:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 5,bg_cell_no=5, bg_color='cyan', font_color='magenta', text_value='ENGLAND', msg='Step 27.7:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 37,bg_cell_no=42, bg_color='cyan', font_color='magenta', text_value='BMW', msg='Step 27.8:')
        
        
        """ 28. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp         """
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()