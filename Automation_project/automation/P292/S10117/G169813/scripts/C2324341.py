'''
Created on 08-May-2018

@author: AAkhan(AA14564)

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324341
TestCase Name = Cleanup : Delete_groups_users
'''
import unittest, time
from common.lib import utillity
from common.pages import wf_legacymainpage, security_center
from common.lib.basetestcase import BaseTestCase

class C2324341_TestClass(BaseTestCase):

    def test_C2324341(self):
        """
        TESTCASE VARIABLES
        """
        workspace = "Workspaces"
        utillobj = utillity.UtillityMethods(self.driver)
        wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        securityobj =security_center.Security_Center(self.driver)
        welcome_page_parent_css = "#PortalResourcevBOX table tr td"
        security_dialog_css="#dlgSecurityManager [class*='active']"
        basicuser=utillobj.parseinitfile('mrid01')
        advanceduser=utillobj.parseinitfile('mrid02')
        groupadminuser=utillobj.parseinitfile('mrid04')
        projid=utillobj.parseinitfile('project_id')
        
        """ Step 1: Sign into WebFOCUS home page as Administrator Navigate URL to http://environment_name:port/alias/legacyhome
        """
        utillobj.invoke_legacyhomepage('mrid', 'mrpass')
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, workspace, 50)
        
        """ Step 2: Invoke Security Center dialog and delete the created users.
        """
        wf_mainpageobj.select_or_verify_top_banner_links('Administration->Security Center')
        utillobj.synchronize_with_number_of_element(security_dialog_css, 1, 120)
        time.sleep(1)
        user_name=[basicuser, advanceduser, groupadminuser]
        securityobj.delete_user(user_name, Step_num_msg='2')
        
        """ Step 3: Delete the groups associated with the domain created.
        """
        securityobj.delete_group(projid, Step_num_msg='3')
        
        """ Step 4: Close the Security Center.
        """
        securityobj.close_security_center_dialog()
        
        """ Step 5: Sign Out from WebFOCUS
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()