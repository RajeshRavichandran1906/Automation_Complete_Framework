'''
Created on 02-Feb-2017

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227536
TestCase Name = Verify Document default page Size and Orientation and change page Size
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_ribbon, visualization_resultarea
from common.lib import utillity
from selenium.webdriver import ActionChains

class C2227536_TestClass(BaseTestCase):

    def test_C2227536(self):
        Test_Case_ID = 'C2227536'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """ 1. Launch IA Document mode:- http://machine:port/ibi_apps/ia?tool=Document&master=baseapp/wf_reatil_lite&item=IBFS%3A%2FWFC%2FRepository%2FS10032 """
        utillobj.infoassist_api_login('document','baseapp/wf_retail_lite','P292/S10032_1', 'mrid', 'mrpass')
        resultobj.wait_for_property("#iaCanvasCaptionLabel", 1, expire_time=20, string_value='Document')
        time.sleep(5)
        
        """ 2. Double click "Product,Category" """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(5)
        coln_list = ["ProductCategory"]
        resultobj.verify_report_titles_on_preview(1, 2, "TableChart_1", coln_list, "Step 02.01: Verify column titles")
        
        """ 3. Select the Layout Tab > Click "Orientation" button in the Ribbon """
        ribbonobj.select_ribbon_item("Layout", "Orientation")
        
        """ 4. Verify Page Orientation is set to "Landscape" by default """
        utillobj.select_or_verify_bipop_menu(expected_ticked_list=['Landscape'], msg='Step 04.01: Landscape - ')
        
        """ 5. Click the "Size" button > Verify default Page Size is "Letter" """
        ribbonobj.select_ribbon_item("Layout", "Size")
        utillobj.select_or_verify_bipop_menu(expected_ticked_list=['Letter'], msg='Step 05.01: Letter - ')
        
        """ 6. Select size "Large Size (34x44 Inches)" """
        utillobj.select_or_verify_bipop_menu("Large Size (34x44 Inches)")
        
        """ 7. Verify selected page is set > scroll all the way to the right and bottom of page to view dimensions """
        source_elem = self.driver.find_element_by_css_selector("#resultArea #canvasFrame")
        canvas_width=source_elem.size['width']
        canvas_heigth=source_elem.size['height']
        action1 = ActionChains(self.driver)
        ''' to move Vertical slider to the bottom and Horizontal slider to the right'''
        j=0
        while j<6:
            action1.move_to_element_with_offset(source_elem, canvas_width-8, canvas_heigth-40).click().perform()
            action1.move_to_element_with_offset(source_elem, canvas_width-40, canvas_heigth-8).click().perform()
            j=j+1
        time.sleep(5)
#         utillobj.take_screenshot(source_elem,Test_Case_ID+'_Actual_Step07_'+browser, image_type='actual')
        
        """ 8. Click "Save" > save as "C2227536" > Click Save """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """ 9. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """ 10. Reopen saved FEX:http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2227536.fex&tool=Document """

        utillobj.infoassist_api_edit(Test_Case_ID, 'document', 'S10032_1', mrid='mrid', mrpass='mrpass')
        resultobj.wait_for_property("#iaCanvasCaptionLabel", 1, expire_time=20, string_value='Document')
        time.sleep(2)
        
        """ 11. Select the Layout Tab > Click "Page" button > Verify selection is "Large Size (34x44 Inches)" """
        ribbonobj.select_ribbon_item("Layout", "Orientation")
        utillobj.select_or_verify_bipop_menu(expected_ticked_list=['Landscape'], msg='Step 11.01: Landscape - ')
        ribbonobj.select_ribbon_item("Layout", "Size")
        utillobj.select_or_verify_bipop_menu(expected_ticked_list=['Large Size (34x44 Inches)'], msg='Step 11.02: Large Size (34x44 Inches) - ')
        
        """ 12. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp """
        time.sleep(2)
        
if __name__ == '__main__':
    unittest.main()