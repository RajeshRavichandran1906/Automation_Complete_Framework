'''
Created on Dec 22, 2016

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/6940
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2036178
Verify Horizontal Percent Area is working properly
'''

import unittest
from common.lib import utillity
from common.pages import visualization_resultarea, visualization_ribbon,ia_ribbon
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2036178_TestClass(BaseTestCase):

    def test_C2036178(self):
        
        Test_Case_ID = "C2036178"
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        
        """
        Step 01: Launch the IA API with chart in edit mode (edit domain, port and alias portions of URL, do not use link as is):
        http://domain.ibi.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS6940Chart_Type_PDF_Charts_Part_1_Test_Suite_%2FC2036178.fex&tool=chart
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S6940',mrid='mrid',mrpass='mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """
        Step02: Select "Format" > "Chart Types" > "Other".
        Step03: Select "Area" > "Horizontal Percent Area" > "OK".
        """
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbobj.select_other_chart_type('area', 'area_percent_horizontal', 10, ok_btn_click=True)
        
        """
        Step04: Verify the following chart is displayed.
        """
        browser=utillobj.parseinitfile('browser')
        utillobj.verify_picture_using_sikuli(Test_Case_ID + "_step4_"+ browser +".png" , "Step4 verification")
        
        """
        Step05: Click "Run".
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        
        """
        Step06: Verify the following chart is displayed.
        """
        utillobj.verify_picture_using_sikuli(Test_Case_ID + "_step6_"+ browser +".png" , "Step6 verification")
        
        """
        Step07: Click "IA" > "Save"
        Step08: Close the IA window.
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID+"_"+browser)
        utillobj.infoassist_api_logout()
        
        """
        Step09: Launch the IA API with chart in edit mode (edit domain, port and alias portions of URL, do not use link as is):
        """
        
        utillobj.infoassist_api_edit(Test_Case_ID+"_"+browser, 'chart', 'S6940',mrid='mrid',mrpass='mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """
        Step10: Verify the following chart is displayed. 
        """
        utillobj.verify_picture_using_sikuli(Test_Case_ID + "_step4_"+ browser +".png" , "Step10 verification")
        
        """
        Step11: Close IA.
        """

if __name__ == '__main__':
    unittest.main()

