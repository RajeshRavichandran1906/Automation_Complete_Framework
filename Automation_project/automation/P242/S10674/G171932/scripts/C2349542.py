'''
Created on May 25, 2018

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10674&group_by=cases:section_id&group_id=171932&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2349542
TestCase Name = Verify user's My Content folder properties
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import wf_mainpage
from common.wftools import login
from common.lib import utillity


class C2349542_TestClass(BaseTestCase):

    def test_C2349542(self):
        """
        TESTCASE VARIABLES
        """
        wf_login = login.Login(self.driver)
        wf_mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        project_id = utillobj.parseinitfile('project_id')
        proj_id = str(project_id)
        dev_user_name = utillobj.parseinitfile('mrid')
        home_page_css=".explore-box .ibfs-tree .home-tree-node .ibx-label-text"
        proj_sub_folder="My Content"
        
        """ Step 1: Login to WebFOCUS as a Developer
        """
        wf_login.invoke_home_page('mrid', 'mrpass')
        utillobj.synchronize_with_visble_text(home_page_css, 'Domains', 290)
        
        """ Step 2: From the new Home Page click on Content page from side bar.
        """
        wf_mainobj.select_left_panel('Content')
        
        """ Step 3: Click on 'P242_S10674_G171304' domain in tree.
        """
        wf_mainobj.expand_repository_folders(proj_id)
        
        """ Step 4: Right click on 'My Content' folder in Content area and select Properties from the context menu.
                    Verify only General and Advanced tabs appear.
        """
        wf_mainobj.select_content_area_folder_context_menu(proj_sub_folder, 'Properties')
        expected_value_list=['General', 'Advanced']
        wf_mainobj.verify_property_dialog_value('General', 'tab_value', "Step 4: Verify only General and Advanced tabs appear.", property_value=expected_value_list)
        
        """ Step 5: Explore General tab.
                    Verify only Summary is enabled.
                    Verify Title and Name are disabled.
                    Verify dates appear for Created, Modified and Accessed.
                    Verify owner is the domain developer.
                    Verify Save button is disabled.
        """
        wf_mainobj.verify_property_dialog_enable_disable('Summary', 'text_area', False, "Step 5.1: Verify Summary - is enabled.")
        wf_mainobj.verify_property_dialog_enable_disable('Title', 'text_value', proj_sub_folder, "Step 5.2: Verify Title - value:{0} is disabled.".format(proj_sub_folder))
        wf_mainobj.verify_property_dialog_enable_disable('Name', 'text_value', '~'+dev_user_name, "Step 5.3: Verify Name - value:{0} is disabled.".format('~'+dev_user_name))
        created_date=wf_mainobj.get_property_created_modified_accessed_time('Created', '5.4')
        wf_mainobj.verify_created_modified_accessed_time_formate(created_date, dev_user_name, "Step 5.4.1: Verify Created dates appear.")
        modified_date=wf_mainobj.get_property_created_modified_accessed_time('Modified', '5.5')
        wf_mainobj.verify_created_modified_accessed_time_formate(modified_date, dev_user_name, "Step 5.5.1: Verify Modified dates appear.")
        accessed_date=wf_mainobj.get_property_created_modified_accessed_time('Accessed', '5.6')
        wf_mainobj.verify_created_modified_accessed_time_formate(accessed_date, dev_user_name, "Step 5.5.1: Verify Accessed dates appear.")
        wf_mainobj.verify_property_dialog_value('Owner', 'text', "Step 5.8: Verify owner appears as : {0}".format(dev_user_name), property_value=dev_user_name)
        wf_mainobj.verify_property_dialog_save_cancel_button_enable_disable('Save', 'disable', "Step 5.9: Verify Button - Save is disabled.")
        
        """ Step 6: Click on Advanced tab.
                    Verify only Sort Order (-300) is enabled in Advanced tab as below:
        """
        wf_mainobj.edit_property_dialog_value('Advanced', 'tab_value', 'Advanced')
        wf_mainobj.verify_property_dialog_enable_disable('Sort order', 'text_value', False, "Step 6: Verify only Sort Order is enabled in Advanced tab.", tab_name='Advanced')
        wf_mainobj.verify_property_dialog_value('Sort order', 'text_value', "Step 6.1: Verify only Sort Order is (-300).", property_value='-300', tab_name='Advanced')
        
        """ Step 7: Close properties dialog.
        """
        wf_mainobj.close_property_dialog() 
        
        """ Step 8: Sign out.
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()