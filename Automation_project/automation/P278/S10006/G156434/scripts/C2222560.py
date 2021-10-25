'''
Created on Nov'22, 2016
@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2222560
'''
import unittest
import time
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon, visualization_run, ia_ribbon, ia_resultarea, ia_run, ia_styling
from common.lib import utillity
from common.locators.visualization_ribbon_locators import VisualizationRibbonLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.locators.loginpage_locators import LoginPageLocators

class C2222560_TestClass(BaseTestCase):

    def test_C2222560(self):
        
        """    TESTCASE VARIABLES    """
        Test_Case_ID = 'C2222560'
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
        ia_resultobj.verify_report_data_set("TableChart_1", 10, 4, "C2222560_Ds01.xlsx", "Step 02a: verify the preview report data")
        
        """    Step 03 : Click Style in the Report section    """
        ribbonobj.select_ribbon_item("Home", "Style")

        """    Step 04. Click Font Color > Select Magenta    """
        ia_styobj.set_report_style(text_color='magenta')
            
        """    Step 05. Click Bold    """
        bold_css=self.driver.find_element_by_css_selector("#Bold").get_attribute("class")
        if 'checked' not in bold_css:
            driver.find_element_by_css_selector("#Bold img").click()
        time.sleep(4)
        
        """    Step 06. Click Apply and Click OK        """
        driver.find_element_by_css_selector("#styleApplyBtn img").click()
        time.sleep(3)
        driver.find_element_by_css_selector("#styleOKBtn img").click()
        time.sleep(4)
        coln_list = ['COUNTRY', 'CAR' ,'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 06: Verify column titles")
        ia_resultobj.verify_report_data_set("TableChart_1", 10, 4, "C2222560_Ds01.xlsx", "Step 06a: verify the preview report data")
        ia_resultobj.verify_report_cell_property("TableChart_1", 1, bold=True, font_color='magenta',text='COUNTRY', msg="Step 06b:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 3, bold=True, font_color='magenta',text='DEALER_COST', msg="Step 06c:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 8, bold=True, font_color='magenta',text='22,369', msg="Step 06d:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 13, bold=True, font_color='magenta',text='4,292', msg="Step 06e:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 19, bold=True, font_color='magenta',text='ITALY', msg="Step 06f:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 24, bold=True, font_color='magenta',text='25,000', msg="Step 06g:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 28, bold=True, font_color='magenta',text='2,626', msg="Step 06h:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 33, bold=True, font_color='magenta',text='W GERMANY', msg="Step 06i:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 39, bold=True, font_color='magenta',text='58,762', msg="Step 06j:")
        
        """    Step 07. Click Run and verify output    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)     
        utillobj.switch_to_frame(pause=2)
        time.sleep(3)
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2222560_Ds02.xlsx", "Step 07: verify data set")
        iarun.verify_table_cell_property("table[summary='Summary']", 1, 3, bold=True, font_color='magenta', text_value='DEALER_COST', msg='Step 07a')
        iarun.verify_table_cell_property("table[summary='Summary']", 2, 2, bold=True, font_color='magenta', text_value='JAGUAR', msg='Step 07b')
        iarun.verify_table_cell_property("table[summary='Summary']", 4, 3, bold=True, font_color='magenta', text_value='4,292', msg='Step 07c')
        iarun.verify_table_cell_property("table[summary='Summary']", 5, 1, bold=True, font_color='magenta', text_value='FRANCE', msg='Step 07d')
        iarun.verify_table_cell_property("table[summary='Summary']", 5, 4, bold=True, font_color='magenta', text_value='5,610', msg='Step 07e')
        iarun.verify_table_cell_property("table[summary='Summary']", 6, 1, bold=True, font_color='magenta', text_value='ITALY', msg='Step 07f')
        iarun.verify_table_cell_property("table[summary='Summary']", 7, 2, bold=True, font_color='magenta', text_value='MASERATI', msg='Step 07g')
        iarun.verify_table_cell_property("table[summary='Summary']", 7, 4, bold=True, font_color='magenta', text_value='31,500', msg='Step 07h')
        iarun.verify_table_cell_property("table[summary='Summary']", 8, 2, bold=True, font_color='magenta', text_value='DATSUN', msg='Step 07i')
        iarun.verify_table_cell_property("table[summary='Summary']", 9, 3, bold=True, font_color='magenta', text_value='2,886', msg='Step 07j')
        iarun.verify_table_cell_property("table[summary='Summary']", 10, 1, bold=True, font_color='magenta', text_value='W GERMANY', msg='Step 07k')
        iarun.verify_table_cell_property("table[summary='Summary']", 11, 2, bold=True, font_color='magenta', text_value='BMW', msg='Step 07l')
        
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        
        """    Step 08. Click Save in the toolbar > Save As C2222560 > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as("se_"+Test_Case_ID)
        time.sleep(5)
        
        """    Step 09. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    Step 10. Open saved fex:- http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2222560.fex&tool=Report    """
        utillobj.infoassist_api_edit("se_"+Test_Case_ID, 'report', 'S10006',mrid='mrid', mrpass='mrpass')
        time.sleep(10)
        
        """    Step 11. Verify Preview    """
        coln_list = ['COUNTRY', 'CAR' ,'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 06: Verify column titles")
        time.sleep(4)
        ia_resultobj.verify_report_data_set("TableChart_1", 10, 4, "C2222560_Ds01.xlsx", "Step 11a: verify the preview report data")
        ia_resultobj.verify_report_cell_property("TableChart_1", 1, bold=True, font_color='magenta',text='COUNTRY', msg="Step 11b:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 3, bold=True, font_color='magenta',text='DEALER_COST', msg="Step 11c:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 8, bold=True, font_color='magenta',text='22,369', msg="Step 11d:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 13, bold=True, font_color='magenta',text='4,292', msg="Step 11e:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 19, bold=True, font_color='magenta',text='ITALY', msg="Step 11f:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 24, bold=True, font_color='magenta',text='25,000', msg="Step 11g:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 28, bold=True, font_color='magenta',text='2,626', msg="Step 11h:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 33, bold=True, font_color='magenta',text='W GERMANY', msg="Step 11i:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 39, bold=True, font_color='magenta',text='58,762', msg="Step 11j:")

        """    Step 12. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()