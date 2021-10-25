'''
Created on Dec 01, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227579
TestCase Name = Verify Query panel Views 2x2, 1x4
'''

import unittest, time
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase

class C2227579_TestClass(BaseTestCase):

    def test_C2227579(self):
        
        Test_Case_ID = "C2227579"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """
        Step 01 : Launch IA Report mode: http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','ibisamp/CAR','P292/S10032_infoassist_4', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(2)
         
        """    
        Step 02: Double click "COUNTRY", "CAR", "DEALER_COST", "RETAIL_COST".
        """
         
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        resultobj.wait_for_property("#TableChart_1  div[class^='x']", 6, expire_time=10) 
        time.sleep(3)
            
        metaobj.datatree_field_click("CAR", 2, 1)
        resultobj.wait_for_property("#TableChart_1  div[class^='x']", 17, expire_time=10) 
        time.sleep(3)
         
        metaobj.datatree_field_click("DEALER_COST", 2, 1)
        resultobj.wait_for_property("#TableChart_1  div[class^='x']", 28, expire_time=10)
        time.sleep(3)
          
        metaobj.datatree_field_click("RETAIL_COST", 2, 1)
        resultobj.wait_for_property("#TableChart_1  div[class^='x']", 39, expire_time=10) 
        time.sleep(3)
        
        """
        Step 03: Verify Preview
        """
        coln_list = ["COUNTRY", "CAR", "DEALER_COST", "RETAIL_COST"]
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 03: Verify report titles")
        
        """    
        Step 04: Select "View" > "Areas 2x2" (Query Panel group).
        """
        ribbonobj.select_ribbon_item("View", "area22")
        time.sleep(1)
        
        """    
        Step 05: Verify Query panel area is changed to 2x2 grid.
        """
        listitem = ['filterBox', 'acrossBoxColumn', 'byBoxColumn', 'measureBoxColumn']
        x=driver.find_elements_by_css_selector("#resultAreaQueryGrid [class='bi-component group-box']")
        list1 = [el.get_attribute("id") for el in x]
        print(list1)
        utillobj.as_List_equal(list1,listitem,"Step 05a: Verify Query panel area is changed to 2x2 grid.")
        
        x=driver.find_elements_by_css_selector("#resultAreaQueryGrid [class='bi-component group-box']")
        
        a=x[0].location['x']
        print(a)
        b=x[2].location['x']
        print(b)
        utillobj.asequal(a,b,"Step 05b: Verify Query panel area is changed to 2x2 grid.")
        
        a=x[1].location['x']
        print(a)
        b=x[3].location['x']
        print(b)
        utillobj.asequal(a,b,"Step 05c: Verify Query panel area is changed to 2x2 grid.")
        
        a=x[0].location['y']
        print(a)
        b=x[1].location['y']
        print(b)
        utillobj.asequal(a,b,"Step 05d: Verify Query panel area is changed to 2x2 grid.")
        
        a=x[2].location['y']
        print(a)
        b=x[3].location['y']
        print(b)
        utillobj.asequal(a,b,"Step 05e: Verify Query panel area is changed to 2x2 grid.")
        
        a=x[1].location['x']
        print(a)
        b=(x[0].location['x'] + x[0].size['width'])
        print(b)
        utillobj.asequal(a,b,"Step 05f: Verify Query panel area is changed to 2x2 grid.")
        
        a=x[3].location['x']
        print(a)
        b=(x[2].location['x'] + x[2].size['width'])
        print(b)
        utillobj.asequal(a,b,"Step 05g: Verify Query panel area is changed to 2x2 grid.")
        
        a=x[0].location['y']
        print(a)
        b=x[1].location['y']
        print(b)
        utillobj.asequal(a,b,"Step 05h: Verify Query panel area is changed to 2x2 grid.")
        
        a=x[2].location['y']
        print(a)
        b=x[3].location['y']
        print(b)
        utillobj.asequal(a,b,"Step 05i: Verify Query panel area is changed to 2x2 grid.")
        
        a=x[2].location['y'] 
        print(a)
        b=x[0].location['y']
        print(b)
        c=a>b
        utillobj.asequal(c,True,"Step 05j: Verify Query panel area is changed to 2x2 grid.")
        
        a=x[2].location['y']
        print(a)
        b=x[0].location['y'] + x[0].size['height']
        print(b)
        utillobj.asequal(a,b,"Step 05k: Verify Query panel area is changed to 2x2 grid.")
        
        """    
        Step 06: Click "Areas 1x4".
        """
        ribbonobj.select_ribbon_item("View", "area14")
        time.sleep(1)
        
        """    
        Step 07: Verify Query panel area is changed to 1x4 grid.
        """
        listitem = ['filterBox', 'acrossBoxColumn', 'byBoxColumn', 'measureBoxColumn']
        x=driver.find_elements_by_css_selector("#resultAreaQueryGrid [class='bi-component group-box']")
        list1 = [el.get_attribute("id") for el in x]
        print(list1)
        utillobj.as_List_equal(list1,listitem,"Step 07a: Verify Query panel area is changed to 1x4 grid.")
        
        a=x[0].location['y']
        b=x[1].location['y']
        c=a<b
        utillobj.asequal(c,True,"Step 07b: Verify Query panel area is changed to 1x4 grid.")
        
        a=x[1].location['y']
        b=x[2].location['y']
        c=a<b
        utillobj.asequal(c,True,"Step 07c: Verify Query panel area is changed to 1x4 grid.")
        
        a=x[2].location['y'] 
        b=x[3].location['y']
        c=a<b
        utillobj.asequal(c,True,"Step 07d: Verify Query panel area is changed to 1x4 grid.")
        
        a=x[0].location['y'] + x[0].size['height']
        b=x[1].location['y']
        utillobj.asequal(a,b,"Step 07e: Verify Query panel area is changed to 1x4 grid.")
        
        """    
        Step 08: Click "Tree"
        """
        ribbonobj.select_ribbon_item("View", "tree")
        time.sleep(1)
        
        """    
        Step 09: Verify default Tree view is restored
        """
        listitem = ['queryBoxColumn', 'filterBox']
        x=driver.find_elements_by_css_selector("#resultAreaQueryGrid [class='bi-component group-box']")
        list1 = [el.get_attribute("id") for el in x]
        print(list1)
        utillobj.as_List_equal(list1,listitem,"Step 09a: Verify Query panel area is changed to 2x2 grid.")
        
        a=x[0].location['y']
        b=x[1].location['y']
        c=a<b
        utillobj.asequal(c,True,"Step 09b: Verify default Tree view is restored")
        time.sleep(3)
        
        """    
        Step 10: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == "__main__":
        unittest.main()       