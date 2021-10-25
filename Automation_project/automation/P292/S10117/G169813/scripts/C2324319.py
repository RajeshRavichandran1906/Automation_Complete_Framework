'''
Created on 27-Dec-2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324319
TestCase Name = Properties Testing : Properties_Open_automatically
'''
import unittest, time
from common.lib import utillity
from common.pages import visualization_resultarea, wf_legacymainpage, vfour_portal_run, vfour_portal_ribbon, vfour_miscelaneous
from common.lib.basetestcase import BaseTestCase
from selenium.common.exceptions import NoSuchElementException

class C2324319_TestClass(BaseTestCase):

    def test_C2324319(self):
        """
        TESTCASE VARIABLES
        """
        workspace = "Workspaces"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        portal_run = vfour_portal_run.Vfour_Portal_Run(self.driver)
        portal_ribbon = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        portal_misobj = vfour_miscelaneous.Vfour_Miscelaneous(self.driver)
        project_id=utillobj.parseinitfile('project_id')
        suite_id=utillobj.parseinitfile('suite_id')
        root_path = project_id+'->'+suite_id
        BIP_Portal_Path = root_path+'->BIP_V4_Portal'
        
        """ Step 1: Sign into WebFOCUS home page as Developer User
        Navigate URL to http://environment name:port/alias/legacyhome
        """
        utillobj.invoke_legacyhomepage('mrid03', 'mrpass03')
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value=workspace, with_regular_exprestion=True)
        time.sleep(1)
        
        """ Step 2: Expand P292 domain, right Click on S10117 folder and choose Properties
        """
        wf_mainpageobj.select_repository_menu(root_path, 'Properties')
        time.sleep(1)
        
        """ Step 3: Click the Automatically Open check box
                    Then click OK button
                    Verify that the domain is now expanded
        """
        wf_mainpageobj.edit_properties_dialog('Main Properties', 'checkbox', 'Automatically Open', checkbox_input='check', msg='Step 2')
        time.sleep(1)
        wf_mainpageobj.edit_properties_dialog('Main Properties', 'button', 'OK')
        time.sleep(5)
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value=workspace, with_regular_exprestion=True)
        domain_tree_text = driver.find_elements_by_css_selector(parent_css)
        actual_domain_tree_text = [elem for elem in [elem.text.strip() for elem in domain_tree_text] if elem != '']
        utillobj.asin('BIP_V4_Portal', actual_domain_tree_text, "Step 3: Verify that the domain is now expanded.")
        ''' Verify Image expand icon visible    '''
        domain_tree_elem = driver.find_elements_by_css_selector(parent_css)
        actual_domain_expand_image_icon = domain_tree_elem[[elem.text.strip() for elem in domain_tree_elem].index('S10117')]
        status=False
        try:
            if bool(actual_domain_expand_image_icon.find_element_by_css_selector("td>img[src*='triangle_expanded']").is_displayed()):
                status=True
        except NoSuchElementException:
                status=False
        utillobj.asequal(True, status, "Step 3.1: Verify that the domain is now expanded.")
        
        """ Step 4: Sign Out and Sign in as WF Developer
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        utillobj.invoke_legacyhomepage('mrid03', 'mrpass03')
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value=workspace, with_regular_exprestion=True)
        time.sleep(3)
        
        """ Step 5: Run lock column portal which has a tree block
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->lock column portal', 'Run')
        time.sleep(2)
        utillobj.wait_for_page_loads(10)
        parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 20)
#         resultobj.wait_for_property(parent_css, 1, expire_time=50)
        
        """ Step 6: Press F8 to bring up the resource tree
                    Verify that the folder is expanded.
                    Verify that the tree block has that folder expanded as well
        """
        portal_ribbon.invoke_and_verify_wf_resource_tree(launch_point='keybord')
        time.sleep(2)
        portal_misobj.expand_resource_tree(project_id+'->S10117')
        parent_css = "#bipResourcesPanel #treeView table>tbody>tr"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value=workspace, with_regular_exprestion=True)
        domain_tree_text = driver.find_elements_by_css_selector(parent_css)
        actual_domain_tree_text = [elem for elem in [elem.text.strip() for elem in domain_tree_text] if elem != '']
        utillobj.asin('BIP_V4_Portal', actual_domain_tree_text, "Step 6: Verify that the domain is now expanded.")
        ''' Verify Image expand icon visible    '''
        domain_tree_elem = driver.find_elements_by_css_selector(parent_css)
        actual_domain_expand_image_icon = domain_tree_elem[[elem.text.strip() for elem in domain_tree_elem].index('S10117')]
        status=False
        try:
            if bool(actual_domain_expand_image_icon.find_element_by_css_selector("td>img[src*='triangle_expanded']").is_displayed()):
                status=True
        except NoSuchElementException:
                status=False
        utillobj.asequal(True, status, "Step 6.1: Verify that the domain is now expanded.")
        
        
        """ Step 7: Click Close
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        
        """ Step 8: In the banner link, click on the top right username > Click Sign Out.
        """
        time.sleep(2)
        
if __name__ == '__main__':
    unittest.main()