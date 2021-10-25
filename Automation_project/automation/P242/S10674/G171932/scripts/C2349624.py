'''
Created on 06 June, 2018

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10674&group_by=cases:section_id&group_id=171932&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2349624
TestCase Name = Verify same tab remains selected in Properties dialog after selecting another item
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import wf_mainpage
from common.wftools import login
from common.lib import utillity


class C2349624_TestClass(BaseTestCase):

    def test_C2349624(self):
        """
        TESTCASE VARIABLES
        """
        wf_login = login.Login(self.driver)
        wf_mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        project_id = utillobj.parseinitfile('project_id')
        proj_id = str(project_id)
        home_page_css=".explore-box .ibfs-tree .home-tree-node .ibx-label-text"
        proj_sub_folder="{0}->Blogs".format(proj_id)
        proj_sub_folder_item="Blog1"
        property_dialog_css='.properties-page.propPage'
        property_dialog_title_css=".properties-page-titlebar .ibx-label-text"
        
        """ Step 1: Login to WebFOCUS as a Developer
        """
        wf_login.invoke_home_page('mrid', 'mrpass')
        utillobj.synchronize_with_visble_text(home_page_css, 'Domains', 290)
        
        """ Step 2: From the new Home Page click on Content from side bar
        """
        wf_mainobj.select_left_panel('Content')
        
        """ Step 3: Right click on P242_S10674_G171304/Blogs sub folder and select Properties from the context menu.
        """
        wf_mainobj.select_repository_folder_context_menu(proj_sub_folder, 'Properties')
        utillobj.synchronize_with_number_of_element(property_dialog_css, 1, 190)
        
        """ Step 4: Click Advanced tab.
        """
        wf_mainobj.edit_property_dialog_value('Advanced', 'tab_value', 'Advanced')
        
        """ Step 5: Click Blog1
                    Verify Advanced tab remains selected.
        """
        wf_mainobj.select_repository_folder_item_context_menu(proj_sub_folder_item, click_option='left_click')
        utillobj.synchronize_with_visble_text(property_dialog_title_css, 'Blog1', 190)
        wf_mainobj.verify_selected_tab_in_property_dialog('Advanced', "Step 3: Verify Advanced tab remains selected.")
        
        """ Step 6: Close properties dialog.
        """
        wf_mainobj.close_property_dialog() 
        
        """ Step 7: Sign out.
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()