'''
Created on Dec'15, 2016
@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2222559
'''
import unittest
import time
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_resultarea, ia_styling
from common.lib import utillity

class C2222559_TestClass(BaseTestCase):

    def test_C2222559(self):
        
        """    TESTCASE VARIABLES    """
        Test_Case_ID = 'C2222559'
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        iastyobj=ia_styling.IA_Style(self.driver)
        
        """    
        Step 01: Launch the IA API with CAR master file    
        """
        utillobj.infoassist_api_login('report','ibisamp/car','P278/S10006', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)

        """    
        Step 02 : Select "COUNTRY","CAR","DEALER_COST","RETAIL_COST".        
        """
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
        
        """    
        Step 03 : Click Style in the Report section    
        """
        ribbonobj.select_ribbon_item("Home", "Style")

        """    
        Step 04. Click Font Color > Select Magenta
        Step 05. Click Background Color > Select Cyan 
        Step 06. Click Apply and Click OK  
        """
        elem=(By.CSS_SELECTOR, '#styleDlg')
        resultobj._validate_page(elem)
        time.sleep(12)
        iastyobj.set_report_style(bold=False, text_color='magenta', background_color='cyan', btn_apply=True, btn_ok=True)
        time.sleep(3)
        elem=(By.CSS_SELECTOR, '#TableChart_1')
        resultobj._validate_page(elem)
        
        """    
        Step 07. Select Banded > Select Yellow    
        Step 08. Verify Preview  
        """
        ribbonobj.select_ribbon_item("Home", "Banded")
        time.sleep(3)
        iastyobj.set_color("yellow")
        
        coln_list = ['COUNTRY', 'CAR' ,'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 08: Verify column titles")
        ia_resultobj.verify_report_cell_property("TableChart_1", 1, bg_cell_no=1,bg_color='cyan', font_color='magenta',text_value='COUNTRY', msg="Step 08b:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 3, bg_cell_no=3,bg_color='cyan', font_color='magenta',text_value='DEALER_COST', msg="Step 08c:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 8, bg_cell_no=8,bg_color='white', font_color='magenta',text_value='22,369', msg="Step 08d:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 9, bg_cell_no=10,bg_color='yellow', font_color='magenta',text_value='JENSEN', msg="Step 08e:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 13, bg_cell_no=15,bg_color='white', font_color='magenta',text_value='4,292', msg="Step 08f:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 18, bg_cell_no=19,bg_color='yellow', font_color='magenta',text_value='5,610', msg="Step 08g:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 19, bg_cell_no=21,bg_color='white', font_color='magenta',text_value='ITALY', msg="Step 08h:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 23, bg_cell_no=26,bg_color='yellow', font_color='magenta',text_value='MASERATI', msg="Step 08i:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 28, bg_cell_no=31,bg_color='white', font_color='magenta',text_value='2,626', msg="Step 08j:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 32, bg_cell_no=36,bg_color='yellow', font_color='magenta',text_value='3,339', msg="Step 08k:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 33, bg_cell_no=37,bg_color='white', font_color='magenta',text_value='W GERMANY', msg="Step 08l:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 37, bg_cell_no=42,bg_color='yellow', font_color='magenta',text_value='BMW', msg="Step 08m:")
       
        """    
        Step 09. Click Save in the toolbar > Save As C2222559 > click Save    
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as("se_"+Test_Case_ID)
        time.sleep(5)
        
        """    
        Step 10. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    
        """
        utillobj.infoassist_api_logout()
        time.sleep(3)
         
        """    
        Step 11. Open saved fex:- http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2222559.fex&tool=Report    
        """
        utillobj.infoassist_api_edit("se_"+Test_Case_ID, 'report', 'S10006', mrid='mrid', mrpass='mrpass')
        time.sleep(10)
         
        """    
        Step 12. Verify Preview    
        """
        elem=(By.CSS_SELECTOR, '#TableChart_1')
        resultobj._validate_page(elem)
        coln_list = ['COUNTRY', 'CAR' ,'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 12: Verify column titles")
        time.sleep(4)
        ia_resultobj.verify_report_data_set("TableChart_1", 10, 4, "C2222560_Ds01.xlsx", "Step 12a: verify the preview report data")
        ia_resultobj.verify_report_cell_property("TableChart_1", 1, bg_cell_no=1,bg_color='cyan', font_color='magenta',text_value='COUNTRY', msg="Step 12b:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 3, bg_cell_no=3,bg_color='cyan', font_color='magenta',text_value='DEALER_COST', msg="Step 12c:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 8, bg_cell_no=8,bg_color='white', font_color='magenta',text_value='22,369', msg="Step 12d:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 9, bg_cell_no=10,bg_color='yellow', font_color='magenta',text_value='JENSEN', msg="Step 12e:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 13, bg_cell_no=15,bg_color='white', font_color='magenta',text_value='4,292', msg="Step 12f:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 18, bg_cell_no=19,bg_color='yellow', font_color='magenta',text_value='5,610', msg="Step 12g:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 19, bg_cell_no=21,bg_color='white', font_color='magenta',text_value='ITALY', msg="Step 12h:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 23, bg_cell_no=26,bg_color='yellow', font_color='magenta',text_value='MASERATI', msg="Step 12i:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 28, bg_cell_no=31,bg_color='white', font_color='magenta',text_value='2,626', msg="Step 12j:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 32, bg_cell_no=36,bg_color='yellow', font_color='magenta',text_value='3,339', msg="Step 12k:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 33, bg_cell_no=37,bg_color='white', font_color='magenta',text_value='W GERMANY', msg="Step 12l:")
        ia_resultobj.verify_report_cell_property("TableChart_1", 37, bg_cell_no=42,bg_color='yellow', font_color='magenta',text_value='BMW', msg="Step 12m:")
 
        """    
        Step 13. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    
        """
        time.sleep(2)
        
        

if __name__ == '__main__':
    unittest.main()