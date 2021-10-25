'''
Created on 08-May-2018

@author: AAkhan(AA14564)

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324342
TestCase Name = Cleanup : Delete_Portal_and_signout
'''
import unittest, time
from common.lib import utillity, javascript
from common.pages import wf_legacymainpage, vfour_miscelaneous
from common.lib.basetestcase import BaseTestCase

class C2324342_TestClass(BaseTestCase):

    def test_C2324342(self):
        """
        TESTCASE VARIABLES
        """
        workspace = "Workspaces"
        utillobj = utillity.UtillityMethods(self.driver)
        wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        portal_misobj = vfour_miscelaneous.Vfour_Miscelaneous(self.driver)
        javascript_obj = javascript.JavaScript(self.driver)
        welcome_page_parent_css = "#PortalResourcevBOX table tr td"
        delete_dialog_css="[id*='BiDialog'] [class*='active']"
        projid=utillobj.parseinitfile('project_id')
        repositry_tree_rows_css="#bipTreePanel #treeView table>tbody>tr"
        
        """ Step 1: Sign into WebFOCUS home page as Administrator Navigate URL to http://environment_name:port/alias/legacyhome
        """
        utillobj.invoke_legacyhomepage('mrid', 'mrpass')
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, workspace, 50)
        
        """ Step 2: Right click on the 'P292_S10117_G169813' domain and choose Delete
        """
        wf_mainpageobj.select_repository_menu(projid, 'Delete')
        utillobj.synchronize_with_number_of_element(delete_dialog_css, 1, 90)
        
        """ Step 3: Click Yes in the popup
        """
        utillobj.click_dialog_button(delete_dialog_css, 'Yes')
        utillobj.synchronize_with_visble_text(delete_dialog_css+" [class*='caption'] .bi-label", 'Select an Option', 90)
        
        """ Step 4: Click OK on the popup
                    Verify that the domain is gone with all its content.
        """
        utillobj.click_dialog_button(delete_dialog_css, 'OK')
        portal_misobj.synchronize_until_element_disappear(delete_dialog_css, 0, 190)
        repository_items = self.driver.find_elements_by_css_selector(repositry_tree_rows_css)
        resource_tree_list = javascript_obj.get_elements_text(repository_items)
        utillobj.as_notin(projid, resource_tree_list, "Step 4: Verify that the domain is gone with all its content.")
        
        """ Step 5: Sign Out from WebFOCUS
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()