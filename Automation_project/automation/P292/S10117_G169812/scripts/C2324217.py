'''
Created on 28-Aug-2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324217
TestCase Name = Portal Designer_Design Tree : Create_and_Delete_folder_from_F8_Resource_Tree
'''
import unittest, time, keyboard
from common.lib import utillity
from common.pages import visualization_resultarea, vfour_miscelaneous, wf_mainpage, wf_legacymainpage, vfour_portal_ribbon
from common.lib.basetestcase import BaseTestCase

class C2324217_TestClass(BaseTestCase):

    def test_C2324217(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        """
        TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        vfour_misobj = vfour_miscelaneous.Vfour_Miscelaneous(self.driver)
        if utillobj.parseinitfile('nodeid') in ('wfinst01','wfinst02','wfinst03','wfinst05'):
            wf_mainpageobj = wf_mainpage.Wf_Mainpage(self.driver)
        else:
            wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        portal_ribbon = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        
        """ Step 1: Sign in as WF Developer
            Step 2: Open 'P292_S10032' domain and edit 'BIP_xxx_Portal123_V4' portal
        """
        utillobj.invoke_webfocu('mrid03', 'mrpass03')
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value="Domains", with_regular_exprestion=True)
        wf_mainpageobj.select_repository_menu('P292->S10117->BIP_V4_Portal->BIP_xxx_Portal123_V4', 'Edit')
        run_loop = True
        count_time=0
        while run_loop:
            if count_time == 25:
                run_loop = False
            if len(driver.window_handles) > 1:
                run_loop = False
            count_time += 1
        utillobj.switch_to_window(1)
        parent_css = "#applicationButtonBox img[src*='bip_button']"
        resultobj.wait_for_property(parent_css, 1, expire_time=50)
        
        """ Step 3: Press F8 to invoke resource tree
        """
        keyboard.send('esc')
        time.sleep(2)
        keyboard.send('f8')
        time.sleep(5)
        """ Step 4: Right click on the 'P292_S10032' domain and choose New > Folder. 
                    Enter 'aaa_BIP' and click the OK button
        """
        vfour_misobj.create_resource_folder('P292->S10117->BIP_V4_Portal', 'aaa_BIP')
        time.sleep(2)
        vfour_misobj.select_resource_menu('Domains', 'Refresh')
        
        """ Step 5: Verify aaa_BIP folder appears under the domain
        """
        vfour_misobj.verify_resource_item('P292->S10117->BIP_V4_Portal->aaa_BIP', 'aaa_BIP', '5')
                
        """ Step 6: Right click on 'aaa_BIP' and delete
                    Click Yes
                    Verify the confirmation deletion window
                    Verify 'aaa_BIP' folder is deleted from Resource tree
        """
        vfour_misobj.select_resource_menu('Domains', 'Refresh')
        time.sleep(2)
        vfour_misobj.delete_resource_item('P292->S10117->BIP_V4_Portal->aaa_BIP')
        
        """ Step 6: Right mouse click to refresh the Repository and make sure the folder is gone.
                    Verify 'aaa_BIP' folder is deleted from Resource tree
        """
        time.sleep(2)
        vfour_misobj.select_resource_menu('Domains', 'Refresh')
        time.sleep(2)
        vfour_misobj.verify_resource_item('P292->S10117->BIP_V4_Portal', 'aaa_BIP', '6', item_exit=False)
        
        """ Step 7: Exit portal
                    Sign Out from WebFOCUS
        """
        portal_ribbon.bip_save_and_exit('Yes')
        utillobj.switch_to_window(0)
        time.sleep(5)
        

if __name__ == '__main__':
    unittest.main()
    