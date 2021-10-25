'''
Created on 30-NOV-2016

@author: Aftab

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2222580
TestCase Name = Verify Justify not enabled / no code written
'''
import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_styling
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By


class C2222580_TestClass(BaseTestCase):

    def test_C2222580(self):
        
        Test_Case_ID = "C2222580"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_stylingobj = ia_styling.IA_Style(self.driver)
        
        """ 1. Launch IA Report mode:
               http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10006    """
        utillobj.infoassist_api_login('report','ibisamp/car','P278/S10006', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        
        """ 2. Select "COUNTRY","CAR","DEALER_COST","RETAIL_COST".        """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("CAR", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('DEALER_COST', 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('RETAIL_COST', 2, 1)
        
        """ 3. Click Style in the Report section            """
        ribbonobj.select_ribbon_item('Home', 'style')
        
        
        """ 4. Verify Justify options (Left/Center/Right) are not enabled        """
        """ 5. Click Cancel            """
        ia_stylingobj.verify_report_style_popup_property(left_btn=False, preview_left=True)
        ia_stylingobj.verify_report_style_popup_property(center_btn=False, preview_center=False)
        ia_stylingobj.verify_report_style_popup_property(right_btn=False, preview_right=False)
        ia_stylingobj.set_report_style(btn_cancel=True)
#         ia_stylingobj.set_report_style(left_justify=False, center_justify=False, right_justify=False, btn_cancel=True)
        
        """ 6. Click View Code in the toolbar            """
        ribbonobj.select_top_toolbar_item('toolbar_showfex')
        time.sleep(8)
        
        """ 7. Verify Style Justify syntax is not written        """
        e = driver.find_element_by_xpath("//iframe[starts-with(@id,'BiRich')]")
        time.sleep(3)
        driver.switch_to.frame(e)
        fex_code = driver.find_element_by_css_selector("body>div").text
        expected_code = 'Justify'
        vp_text = 'Style Justify syntax is not written..in the fexex code'
        bol=expected_code in fex_code
        utillity.UtillityMethods.asequal(self,False, bol, vp_text)
        driver.switch_to_default_content()
        time.sleep(2)
        driver.find_element_by_css_selector("#showFexOKBtn img").click()
        
        
        """ 8. Click Save in the toolbar > Save As C2222580 > click Save     """
        driver.switch_to.default_content()
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as("se_"+Test_Case_ID)
        
        
if __name__ == '__main__':
    unittest.main()