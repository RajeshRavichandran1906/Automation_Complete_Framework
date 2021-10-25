'''
Created on Sep 11, 2017

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324245
TestCase Name = Run Mode : Run_the_Portal
'''

import unittest, time
from common.lib import utillity
from selenium.webdriver.common.by import By
from common.pages import visualization_resultarea, vfour_portal_canvas
from common.lib.basetestcase import BaseTestCase

class C2324245_TestClass(BaseTestCase):

    def test_C2324245(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        """
        TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        vfour_portal_canvas_obj=vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        
        """    1. Go to http://machine:port/alias/portal/S10032/BIP_xxx_Portal123_V4    """
        """    2. On the WF sign in page, sign in as Domain Basic user    """
        utillobj.invoke_bip_portal('BIP_V4_Portal/BIP_xxx_Portal123_V4','mrid01', 'mrpass01')
        time.sleep(15)
        driver.implicitly_wait(1)
        elem1=(By.CSS_SELECTOR, "[class*='banner-top'] > div[class*='menu-bar-item'][style*='inherit']")
        resultobj._validate_page(elem1)
        driver.maximize_window()
        time.sleep(3) 
             
        """    3. Add another page (1 Column) and drag the Retail samples domain on there.    """
        vfour_portal_canvas_obj.add_page('1 Column')
        time.sleep(5)
        vfour_portal_canvas_obj.verify_page_in_navigation_bar('1 Column', 'Step 3: Verify page - 1 Column added')
        time.sleep(5)
        vfour_portal_canvas_obj.dragdrop_repository_item_to_canvas('Retail Samples', 'column', 1)
        time.sleep(2)
        
        """verify Panel 1"""
        panel_obj=vfour_portal_canvas_obj.get_panel_obj('Panel 1')
        utillobj.verify_object_visible('dummy', True, 'Step 03a: Verify Retail Samples Folder visible in Panel 1', elem_obj=panel_obj)
        status=False
        Retail_elem=panel_obj.find_elements_by_css_selector("div[id^='BidFolderBlockTree'] table>tbody>tr")
        for elem in Retail_elem:
            if elem.text.strip() == "Portal":
                status=True
                break
        utillobj.verify_object_visible(elem, status, 'Step 03b: Verify Retail Samples Folder listed in Panel 5', elem_obj=elem)
        
        """    3. Sign Out from WebFOCUS    """
if __name__ == '__main__':
    unittest.main()        