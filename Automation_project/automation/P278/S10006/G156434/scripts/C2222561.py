'''
Created on Nov'22, 2016
@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2222561
TestCase Name = Verify Underline
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

class C2222561_TestClass(BaseTestCase):

    def test_C2222561(self):
        
        """    TESTCASE VARIABLES    """
        Test_Case_ID = 'C2222561'
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver) 
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        ia_styobj = ia_styling.IA_Style(self.driver)
        
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
        time.sleep(4)
        ia_resultobj.verify_report_data_set("TableChart_1", 10, 4, "C2222562_Ds01.xlsx", "Step 02a: verify the preview report data")
        
        """    Step 03 : Click Style in the Report section    """
        ribbonobj.select_ribbon_item("Home", "Style")

        """    Step 04. Verify the Bold is selected by default and Click Underline    """
        """    Step 05. Click Apply and Click OK        """
        ia_styobj.set_report_style(bold=True, underline=True, btn_apply=True, btn_ok=True)
        time.sleep(4)
        coln_list = ['COUNTRY', 'CAR' ,'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 05a: Verify column titles")
        ia_resultobj.verify_report_cell_property("TableChart_1", 1, underline=True, text='COUNTRY', msg="Step 05b:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 3, underline=True, text='DEALER_COST', msg="Step 05c:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 8, underline=True, text='22,369', msg="Step 05d:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 13, underline=True, text='4,292', msg="Step 05e:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 19, underline=True, text='ITALY', msg="Step 05f:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 24, underline=True, text='25,000', msg="Step 05g:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 28, underline=True, text='2,626', msg="Step 05h:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 33, underline=True, text='W GERMANY', msg="Step 05i:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 39, underline=True, text='58,762', msg="Step 05j:")        
        
        """    Step 06. Click Run and verify output    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)
        utillobj.switch_to_frame(pause=2)
        time.sleep(3)
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2222562_run_Ds01.xlsx", "Step 06: verify data set")
        iarun.verify_table_cell_property("table[summary='Summary']", 1, 3, underline=True, text_value='DEALER_COST', msg='Step 06a')
        iarun.verify_table_cell_property("table[summary='Summary']", 2, 2, underline=True, text_value='JAGUAR', msg='Step 06b')
        iarun.verify_table_cell_property("table[summary='Summary']", 4, 3, underline=True, text_value='4,292', msg='Step 06c')
        iarun.verify_table_cell_property("table[summary='Summary']", 5, 1, underline=True, text_value='FRANCE', msg='Step 06d')
        iarun.verify_table_cell_property("table[summary='Summary']", 5, 4, underline=True, text_value='5,610', msg='Step 06e')
        iarun.verify_table_cell_property("table[summary='Summary']", 6, 1, underline=True, text_value='ITALY', msg='Step 06f')
        iarun.verify_table_cell_property("table[summary='Summary']", 7, 2, underline=True, text_value='MASERATI', msg='Step 06g')
        iarun.verify_table_cell_property("table[summary='Summary']", 7, 4, underline=True, text_value='31,500', msg='Step 06h')
        iarun.verify_table_cell_property("table[summary='Summary']", 8, 2, underline=True, text_value='DATSUN', msg='Step 06i')
        iarun.verify_table_cell_property("table[summary='Summary']", 9, 3, underline=True, text_value='2,886', msg='Step 06j')
        iarun.verify_table_cell_property("table[summary='Summary']", 10, 1, underline=True, text_value='W GERMANY', msg='Step 06k')
        iarun.verify_table_cell_property("table[summary='Summary']", 11, 2, underline=True, text_value='BMW', msg='Step 06l')
        
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        
        """    Step 07. Click Save in the toolbar > Save As C2222561 > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    Step 08. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    Step 09. Open saved fex:- http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2222561.fex&tool=Report    """
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10006',mrid='mrid', mrpass='mrpass')
        time.sleep(10)
        
        """    Step 10. Verify Preview    """
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR' ,'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 10a: Verify column titles")
        ia_resultobj.verify_report_data_set("TableChart_1", 10, 4, "C2222562_Ds01.xlsx", "Step 10b: verify the preview report data")
        ia_resultobj.verify_report_cell_property("TableChart_1", 1, underline=True, text='COUNTRY', msg="Step 10c:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 3, underline=True, text='DEALER_COST', msg="Step 10d:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 8, underline=True, text='22,369', msg="Step 10e:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 13, underline=True, text='4,292', msg="Step 10f:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 19, underline=True, text='ITALY', msg="Step 10g:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 24, underline=True, text='25,000', msg="Step 10h:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 28, underline=True, text='2,626', msg="Step 10i:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 33, underline=True, text='W GERMANY', msg="Step 10j:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 39, underline=True, text='58,762', msg="Step 10k:")
        

        """    Step 11. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
#         utillobj.infoassist_api_logout()
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()