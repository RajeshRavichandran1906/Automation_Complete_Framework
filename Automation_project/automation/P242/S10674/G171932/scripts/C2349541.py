'''
Created on May 25, 2018

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10674&group_by=cases:section_id&group_id=171932&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2349541
TestCase Name = Verify Properties panel for domain
'''

import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import wf_mainpage
from common.wftools import login
from common.lib import utillity


class C2349541_TestClass(BaseTestCase):

    def test_C2349541(self):
        """
        TESTCASE VARIABLES
        """
        wf_login = login.Login(self.driver)
        wf_mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        project_id = utillobj.parseinitfile('project_id')
        proj_id = str(project_id)
        home_page_css=".explore-box .ibfs-tree .home-tree-node .ibx-label-text"
        path_in_webfocus="IBFS:/WFC/Repository/{0}".format(proj_id)
        
        """ Step 1: Login to WebFOCUS as a Developer
        """
        wf_login.invoke_home_page('mrid', 'mrpass')
        utillobj.synchronize_with_visble_text(home_page_css, 'Domains', 290)
        
        """ Step 2: From the new Home Page click on Content page from side bar.
        """
        wf_mainobj.select_left_panel('Content')
        
        """ Step 3: Expand 'P242_S10674_G171304' domain in tree if not already expanded.
            Note - When a user signs on, the domain last accessed by the user will be expanded. 
            The first time a user signs on it will be closed unless Automatically Open is checked in Advanced tab in Properties.
        """
        wf_mainobj.expand_repository_folders(proj_id)
        
        """ Step 4: Right click on 'P242_S10674_G171304' domain in tree and select Properties.
                    Verify Properties is displayed on right side and the WebFOCUS Explorer folds its content to make room.
                    Verify only General tab appears and nothing is enabled 
                    (Note: You can type in Summary and Title in 8202m but Save is always disabled. This issue has been fixed in 8203.)
        """
        wf_mainobj.select_repository_folder_context_menu(proj_id, 'Properties')
        wf_mainobj.verify_property_dialog_location('4')
        wf_mainobj.verify_property_tab_value(['General'], "Step 4.1: Verify only General tab appears.")
        wf_mainobj.verify_property_dialog_enable_disable('Language', 'text', 'View All', "Step 4.2: Verify Language - View All is disabled.")
        wf_mainobj.verify_property_dialog_enable_disable('Name', 'text_value', proj_id, "Step 4.3: Verify Name - value:{0} is disabled.".format(project_id))
        wf_mainobj.verify_property_dialog_enable_disable('Path', 'text_value', path_in_webfocus, "Step 4.4: Verify Path - value:{0} is disabled and readonly.".format(project_id))
        wf_mainobj.verify_property_dialog_save_cancel_button_enable_disable('Save', 'disable', "Step 4.5: Verify Button - Save is disabled.")
        wf_mainobj.edit_property_dialog_value('Title', 'text_value', "Able_to_type_in_Title")
        wf_mainobj.verify_property_dialog_value('Title', 'text_value', "Step 4.6: Verify you can type Title input in 8202m.", property_value="Able_to_type_in_Title")
        wf_mainobj.verify_property_dialog_save_cancel_button_enable_disable('Save', 'disable', "Step 4.7: Verify Button - Save is disabled.")
        wf_mainobj.edit_property_dialog_value('Summary', 'text_area', "Able_to_type_in_Summary")
        wf_mainobj.verify_property_dialog_value('Summary', 'text_area', "Step 4.8: Verify you can type Summary text area in 8202m.", property_value="Able_to_type_in_Summary")
        wf_mainobj.verify_property_dialog_save_cancel_button_enable_disable('Save', 'disable', "Step 4.9: Verify Button - Save is disabled.")
        
        """ Step 5: Explore General tab.
                    Verify owner appears as follows:
                    Verify Publish and Show radio button appear and are disabled:
        """
        wf_mainobj.verify_property_dialog_value('Owner', 'text', "Step 5: Verify owner appears as follows: -", property_value="-")
        wf_mainobj.verify_property_dialog_enable_disable('Publish', 'radiobutton_value', 'Yes', "Step 5.1: Verify Publish - value:Yes and No is disabled.")
        wf_mainobj.verify_property_dialog_enable_disable('Show', 'radiobutton_value', 'Yes', "Step 5.2: Verify Show - value:Yes and No is disabled.")
        
        """ Step 6: Close properties dialog.
        """
        wf_mainobj.close_property_dialog()
        
        """ Step 7: Sign out.
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()