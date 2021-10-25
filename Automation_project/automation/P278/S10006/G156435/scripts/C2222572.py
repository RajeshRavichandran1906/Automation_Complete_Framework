'''
Created on Nov'22, 2016
@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2222572
TestCase Name = Verify Banded applied then Styling Report
'''
import unittest
import time
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run, ia_styling
from common.lib import utillity
from common.locators.visualization_ribbon_locators import VisualizationRibbonLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.locators.loginpage_locators import LoginPageLocators

class C2222572_TestClass(BaseTestCase):

    def test_C2222572(self):
        
        """    TESTCASE VARIABLES    """
        Test_Case_ID = 'C2222572'
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        iastyobj=ia_styling.IA_Style(self.driver)
        
        """    Step 01: Launch the IA API with CAR master file    """
        utillobj.infoassist_api_login('report','ibisamp/car','P278/S10006', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)

        """    Step 02 : Select "COUNTRY","CAR","DEALER_COST","RETAIL_COST".        """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("CAR", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("DEALER_COST", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("RETAIL_COST", 2, 1)
        time.sleep(4)
        coln_list = ['COUNTRY', 'CAR' ,'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 02a: Verify column titles")
        ia_resultobj.verify_report_data_set("TableChart_1", 10, 4, "C2222572_Ds01.xlsx", "Step 02a: verify the preview report data")
        time.sleep(4)
        
        """    "Step 03. Select Banded > Select Yellow    """
        """    "Step 04. Click OK    """
        ribbonobj.select_ribbon_item("Home", "Banded")
        iastyobj.set_color("yellow")
        
        """    Step 05 : Click Style in the Report section    """
        ribbonobj.select_ribbon_item("Home", "Style")

        """    Step 06. Click Font Color > Select Magenta    """
        """    Step 07. Click Background Color > Select Cyan    """
        """    Step 08. Click Apply and Click OK        """
        iastyobj.set_report_style(bold=True, text_color='magenta', background_color='cyan', btn_apply=True, btn_ok=True)
        time.sleep(4)
        coln_list = ['COUNTRY', 'CAR' ,'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 08: Verify column titles")
        ia_resultobj.verify_report_cell_property("TableChart_1", 1, bg_cell_no=1,bg_color='cyan', font_color='magenta',text_value='COUNTRY', msg="Step 08b:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 3, bg_cell_no=3,bg_color='cyan', font_color='magenta',text_value='DEALER_COST', msg="Step 08c:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 8, bg_cell_no=8,bg_color='cyan', font_color='magenta',text_value='22,369', msg="Step 08d:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 9, bg_cell_no=10,bg_color='yellow', font_color='magenta',text_value='JENSEN', msg="Step 08e:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 13, bg_cell_no=15,bg_color='cyan', font_color='magenta',text_value='4,292', msg="Step 08f:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 18, bg_cell_no=19,bg_color='yellow', font_color='magenta',text_value='5,610', msg="Step 08g:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 19, bg_cell_no=21,bg_color='cyan', font_color='magenta',text_value='ITALY', msg="Step 08h:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 23, bg_cell_no=26,bg_color='yellow', font_color='magenta',text_value='MASERATI', msg="Step 08i:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 28, bg_cell_no=31,bg_color='cyan', font_color='magenta',text_value='2,626', msg="Step 08j:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 32, bg_cell_no=36,bg_color='yellow', font_color='magenta',text_value='3,339', msg="Step 08k:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 33, bg_cell_no=37,bg_color='cyan', font_color='magenta',text_value='W GERMANY', msg="Step 08l:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 37, bg_cell_no=42,bg_color='yellow', font_color='magenta',text_value='BMW', msg="Step 08m:")
        
    
        """    Step 09. Click Run and verify output    """
        time.sleep(5)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(2)     
        utillobj.switch_to_frame(pause=2)
        time.sleep(3)
        #iarun.create_table_data_set("table[summary= 'Summary']", "C2222572_Ds02.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2222572_Ds02.xlsx", "Step 09: verify data set")
        iarun.verify_table_cell_property("table[summary='Summary']", 1, 3, bg_color='cyan', font_color='magenta', text_value='DEALER_COST', msg='Step 09a')
        iarun.verify_table_cell_property("table[summary='Summary']", 2, 2, bg_color='cyan', font_color='magenta', text_value='JAGUAR', msg='Step 09b')
        iarun.verify_table_cell_property("table[summary='Summary']", 4, 3, bg_color='cyan', font_color='magenta', text_value='4,292', msg='Step 09c')
        iarun.verify_table_cell_property("table[summary='Summary']", 5, 1, bg_color='yellow', font_color='magenta', text_value='FRANCE', msg='Step 09d')
        iarun.verify_table_cell_property("table[summary='Summary']", 5, 4, bg_color='yellow', font_color='magenta', text_value='5,610', msg='Step 09e')
        iarun.verify_table_cell_property("table[summary='Summary']", 6, 1, bg_color='cyan', font_color='magenta', text_value='ITALY', msg='Step 09f')
        iarun.verify_table_cell_property("table[summary='Summary']", 7, 2, bg_color='yellow', font_color='magenta', text_value='MASERATI', msg='Step 09g')
        iarun.verify_table_cell_property("table[summary='Summary']", 7, 4, bg_color='yellow', font_color='magenta', text_value='31,500', msg='Step 09h')
        iarun.verify_table_cell_property("table[summary='Summary']", 8, 2, bg_color='cyan', font_color='magenta', text_value='DATSUN', msg='Step 09i')
        iarun.verify_table_cell_property("table[summary='Summary']", 9, 3, bg_color='yellow', font_color='magenta', text_value='2,886', msg='Step 09j')
        iarun.verify_table_cell_property("table[summary='Summary']", 10, 1, bg_color='cyan', font_color='magenta', text_value='W GERMANY', msg='Step 09k')
        iarun.verify_table_cell_property("table[summary='Summary']", 11, 2, bg_color='yellow', font_color='magenta', text_value='BMW', msg='Step 09l')    
        
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        
        """    Step 10. Click Save in the toolbar > Save As C2222560 > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as("se_"+Test_Case_ID)
        time.sleep(5)
        
        """    Step 11. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    Step 12. Open saved fex:- http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2222560.fex&tool=Report    """

        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        utillobj.infoassist_api_edit("se_"+Test_Case_ID, 'report', 'S10006', mrid='mrid', mrpass='mrpass')
        time.sleep(10)
        
        """    Step 13. Verify Preview    """
        parent_css="#TableChart_1 [id^='ActivePreviewItem']"
        resultobj.wait_for_property(parent_css, 8)
        coln_list = ['COUNTRY', 'CAR' ,'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 13: Verify column titles")
        time.sleep(4)
        ia_resultobj.verify_report_data_set("TableChart_1", 10, 4, "C2222560_Ds01.xlsx", "Step 13a: verify the preview report data")
        ia_resultobj.verify_report_cell_property("TableChart_1", 1, bg_cell_no=1,bg_color='cyan', font_color='magenta',text_value='COUNTRY', msg="Step 13b:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 3, bg_cell_no=3,bg_color='cyan', font_color='magenta',text_value='DEALER_COST', msg="Step 13c:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 8, bg_cell_no=8,bg_color='cyan', font_color='magenta',text_value='22,369', msg="Step 13d:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 9, bg_cell_no=10,bg_color='yellow', font_color='magenta',text_value='JENSEN', msg="Step 13e:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 13, bg_cell_no=15,bg_color='cyan', font_color='magenta',text_value='4,292', msg="Step 13f:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 18, bg_cell_no=19,bg_color='yellow', font_color='magenta',text_value='5,610', msg="Step 13g:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 19, bg_cell_no=21,bg_color='cyan', font_color='magenta',text_value='ITALY', msg="Step 13h:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 23, bg_cell_no=26,bg_color='yellow', font_color='magenta',text_value='MASERATI', msg="Step 13i:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 28, bg_cell_no=31,bg_color='cyan', font_color='magenta',text_value='2,626', msg="Step 13j:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 32, bg_cell_no=36,bg_color='yellow', font_color='magenta',text_value='3,339', msg="Step 13k:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 33, bg_cell_no=37,bg_color='cyan', font_color='magenta',text_value='W GERMANY', msg="Step 13l:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 37, bg_cell_no=42,bg_color='yellow', font_color='magenta',text_value='BMW', msg="Step 13m:")
        
        """    Step 14. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()