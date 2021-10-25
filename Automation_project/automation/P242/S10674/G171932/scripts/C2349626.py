'''
Created on 04 June, 2018

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10674&group_by=cases:section_id&group_id=171932&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2349626
TestCase Name = Verify General tab is selected after signing out
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import wf_mainpage
from common.wftools import login
from common.lib import utillity


class C2349626_TestClass(BaseTestCase):

    def test_C2349626(self):
        """
        TESTCASE VARIABLES
        """
        wf_login = login.Login(self.driver)
        wf_mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        project_id = utillobj.parseinitfile('project_id')
        proj_id = str(project_id)
        home_page_css=".explore-box .ibfs-tree .home-tree-node .ibx-label-text"
        proj_sub_folder="{0}->Charts".format(proj_id)
        property_dialog_css='.properties-page.propPage'
        
        """ Step 1: Login to WebFOCUS as a Developer
        """
        wf_login.invoke_home_page('mrid', 'mrpass')
        utillobj.synchronize_with_visble_text(home_page_css, 'Domains', 290)
        
        """ Step 2: From the new Home Page click on Content page from side bar.
        """
        wf_mainobj.select_left_panel('Content')
        
        """ Step 3: Right click on P242_S10674_G171304/Charts sub folder and select properties from the menu.
                    Verify General tab selected.
        """
        wf_mainobj.select_repository_folder_context_menu(proj_sub_folder, 'Properties')
        utillobj.synchronize_with_number_of_element(property_dialog_css, 1, 190)
        wf_mainobj.verify_selected_tab_in_property_dialog('General', "Step 3: Verify General tab selected.")
        
        """ Step 4: Click on cancel button.
                    Verify properties dialog is closed.
        """
        wf_mainobj.select_property_dialog_save_cancel_button('Cancel')
        utillobj.synchronize_until_element_disappear(property_dialog_css, 9)
        utillobj.verify_element_visiblty(element_css=property_dialog_css, visible=False, msg="Step 4: Verify properties dialog is closed.")
        
        """ Step 5: Sign out.
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()