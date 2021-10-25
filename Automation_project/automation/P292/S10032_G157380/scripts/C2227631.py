'''
Created on May 12, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227631
TestCase Name = Query Variable Filter with & cannot be used
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase

class C2227631_TestClass(BaseTestCase):

    def test_C2227631(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227631'
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_2', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """
        Step 02: Expand "Query Variables" in the Query Pane 
        Step 03: Drag and drop "Product Filter" variable into the Filter pane 
        """
        time.sleep(5)
        metaobj.datatree_field_click("Product Filter", 1, 1,"Filter")
        time.sleep(2)
        
        """
        Step04: Verify warning message is displayed
        Step05: Click OK
        """  
        parent_css="div[id^='BiDialog']"
        resultobj.wait_for_property(parent_css, 1)      
        obj=driver.find_element_by_css_selector("[id*='BiOptionPane'] div[id*='BiLabel']").text.strip()
        utillobj.asequal(obj,"The field cannot be used to create a filter", "Step04: Verify message is displayed")
        time.sleep(2)
        utillobj.click_dialog_button("div[id^='BiDialog']", "OK")
        time.sleep(5)
        
        """
        Step06: Double click "Product Filter" 
        """ 
        metaobj.datatree_field_click("Product Filter", 2, 1)
        time.sleep(2)
        
        """
        Step07: Verify warning message is displayed
        Step08: Click OK
        """ 
        parent_css="div[id^='BiDialog']"
        resultobj.wait_for_property(parent_css, 1)
        obj=driver.find_element_by_css_selector("[id*='BiOptionPane'] div[id*='BiLabel']").text.strip()
        utillobj.asequal(obj,"The field cannot be used to create a filter", "Step07: Verify message is displayed")
        time.sleep(10)
        ele=driver.find_element_by_css_selector("div[id^='BiDialog']")
        utillobj.take_screenshot(ele,'C2227631_Base_step08', image_type='actual',x=1, y=1, w=-1, h=-1)
        utillobj.click_dialog_button("div[id^='BiDialog']", "OK")
        time.sleep(5)
        
        """
        Step 09: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()