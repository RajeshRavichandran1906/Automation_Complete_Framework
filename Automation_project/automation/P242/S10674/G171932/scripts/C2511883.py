'''
Created on 19 June, 2018

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10674&group_by=cases:section_id&group_id=171932&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2511883
TestCase Name = Times are partly cutoff in the properties dialog
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import wf_mainpage
from common.wftools import login
from common.lib import utillity


class C2511883_TestClass(BaseTestCase):

    def test_C2511883(self):
        """
        TESTCASE VARIABLES
        """
        wf_login = login.Login(self.driver)
        wf_mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        admin_user_name = utillobj.parseinitfile('mrid01')
        home_page_css=".explore-box .ibfs-tree .home-tree-node .ibx-label-text"
        proj_sub_folder="Retail Samples->Charts"
        proj_sub_folder_item='Arc - Sales by Region'
        property_dialog_css='.properties-page.propPage'
        
        """ Step 1: Login to WebFOCUS as a Developer.
        """
        wf_login.invoke_home_page('mrid', 'mrpass')
        utillobj.synchronize_with_visble_text(home_page_css, 'Domains', 290)
        
        """ Step 2: From the new Home Page click on Content from side bar.
        """
        wf_mainobj.select_left_panel('Content')
        
        """ Step 3: Open Retail Samples/Charts
        """
        """ Step 4: Right click Arc - Sales by Region and select Properties
                    Verify times are not cut off. For example they should appear like this:
        """
        wf_mainobj.select_repository_folder_item_context_menu(proj_sub_folder_item, context_menu_item_path='Properties', folder_path=proj_sub_folder)
        utillobj.synchronize_with_number_of_element(property_dialog_css, 1, 190)
        created_date=wf_mainobj.get_property_created_modified_accessed_time('Created', '4')
        wf_mainobj.verify_created_modified_accessed_time_formate(created_date, admin_user_name, "Step 4.1: Verify times are not cut off for Created dates.")
        modified_date=wf_mainobj.get_property_created_modified_accessed_time('Modified', '4.1.1')
        wf_mainobj.verify_created_modified_accessed_time_formate(modified_date, admin_user_name, "Step 4.2: Verify times are not cut off for Modified dates.")
        accessed_date=wf_mainobj.get_property_created_modified_accessed_time('Accessed', '4.2.1')
        wf_mainobj.verify_created_modified_accessed_time_formate(accessed_date, admin_user_name, "Step 4.3: Verify times are not cut off for Accessed dates.")
        
        """ Step 5: Close Properties panel
        """
        wf_mainobj.close_property_dialog()
        
        """ Step 6: Sign out.
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()