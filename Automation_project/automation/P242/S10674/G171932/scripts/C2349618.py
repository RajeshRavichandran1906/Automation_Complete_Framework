'''
Created on 06 June, 2018

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10674&group_by=cases:section_id&group_id=171932&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2349624
TestCase Name = Verify domain subfolder properties
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import wf_mainpage
from common.wftools import login
from common.lib import utillity, core_utility
from selenium.common.exceptions import NoSuchElementException


class C2349618_TestClass(BaseTestCase):

    def test_C2349618(self):
        """
        TESTCASE VARIABLES
        """
        wf_login = login.Login(self.driver)
        wf_mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        core_utilobj=core_utility.CoreUtillityMethods(self.driver)
        project_id = utillobj.parseinitfile('project_id')
        proj_id = str(project_id)
        admin_user_name = utillobj.parseinitfile('mrid01')
        home_page_css=".explore-box .ibfs-tree .home-tree-node .ibx-label-text"
        proj_sub_folder="{0}->Alerts".format(proj_id)
        property_dialog_css='.properties-page.propPage'
        edit_button_css=".properties-general-folder [data-ibx-type='ibxButton']"
        name_box_css=".properties-general-folder [data-ibx-type*='ibxText'].ibx-widget-disabled input"
        
        """ Step 1: Login to WebFOCUS as a Developer
        """
        wf_login.invoke_home_page('mrid', 'mrpass')
        utillobj.synchronize_with_visble_text(home_page_css, 'Domains', 290)
        
        """ Step 2: From the new Home Page click on Content page from side bar.
        """
        wf_mainobj.select_left_panel('Content')
        
        """ Step 3: Right click P242_S10674_G171304/Alerts sub folder and select Properties from the menu.
                    Verify only General and Advanced tabs appear and View All, Title, Summary, Publish and Show are enabled as below.
                    Verify Name is enabled by clicking on Edit button next to Name box.
        """
        wf_mainobj.select_repository_folder_context_menu(proj_sub_folder, 'Properties')
        utillobj.synchronize_with_number_of_element(property_dialog_css, 1, 190)
        expected_value_list=['General', 'Advanced']
        wf_mainobj.verify_property_dialog_value('General', 'tab_value', "Step 3: Verify only General and Advanced tabs appear.", property_value=expected_value_list)
        wf_mainobj.verify_property_dialog_enable_disable('Language', 'text', False, "Step 3.1: Verify View All - is enabled.")
        wf_mainobj.verify_property_dialog_enable_disable('Title', 'text_value', False, "Step 3.2: Verify Title - is enabled.")
        wf_mainobj.verify_property_dialog_enable_disable('Summary', 'text_area', False, "Step 3.3: Verify Summary - is enabled.")
        wf_mainobj.verify_property_dialog_enable_disable('Publish', 'radiobutton_value', False, "Step 3.4: Verify Publish - is enabled.")
        wf_mainobj.verify_property_dialog_value('Publish', 'radiobutton_value', "Step 3.5: Verify Publish - is enabled.", property_value='Yes')
        wf_mainobj.verify_property_dialog_enable_disable('Show', 'radiobutton_value', False, "Step 3.6: Verify Show - is enabled.")
        wf_mainobj.verify_property_dialog_value('Show', 'radiobutton_value', "Step 3.7: Verify Show - is enabled.", property_value='Yes')
        name_row_obj=wf_mainobj.get_property_dialog_rows_object('Name', '3.8')
        edit_button_elem=name_row_obj.find_element_by_css_selector(edit_button_css)
        core_utilobj.left_click(edit_button_elem)
        try:
            name_row_obj.find_element_by_css_selector(name_box_css)
            status=False
        except NoSuchElementException:
            status=True
        utillobj.asequal(status, True, "Step 3.9: Verify Name is enabled by clicking on Edit button next to Name box.")
        
        """ Step 4: Explore General tab.
                    Verify dates appear and the owner.
                    Verify Save is disabled.
        """
        created_date=wf_mainobj.get_property_created_modified_accessed_time('Created', '5.2')
        wf_mainobj.verify_created_modified_accessed_time_formate(created_date, admin_user_name, "Step 5.2.1: Verify Created dates appear.")
        modified_date=wf_mainobj.get_property_created_modified_accessed_time('Modified', '5.3')
        wf_mainobj.verify_created_modified_accessed_time_formate(modified_date, admin_user_name, "Step 5.3.1: Verify Modified dates appear.")
        accessed_date=wf_mainobj.get_property_created_modified_accessed_time('Accessed', '5.4')
        wf_mainobj.verify_created_modified_accessed_time_formate(accessed_date, admin_user_name, "Step 5.3.1: Verify Accessed dates appear.")
        wf_mainobj.verify_property_dialog_value('Owner', 'text', "Step 4.1: Verify owner appears as : '-'", property_value='-')
        wf_mainobj.verify_property_dialog_save_cancel_button_enable_disable('Save', 'disable', "Step 4.2: Verify Button - Save is disabled.")
        
        """ Step 5: Click on Advanced tab.
                    Verify Sort Order appears as below and Automatically Open is enabled.
                    Verify Save is disabled.
        """
        wf_mainobj.edit_property_dialog_value('Advanced', 'tab_value', 'Advanced')
        wf_mainobj.verify_property_dialog_enable_disable('Sort order', 'text_value', False, "Step 5: Verify only Sort Order is enabled in Advanced tab.", tab_name='Advanced')
        wf_mainobj.verify_property_dialog_value('Sort order', 'text_value', "Step 5.1: Verify only Sort Order with no value.", property_value='', tab_name='Advanced')
        wf_mainobj.verify_property_dialog_enable_disable('Automatically open', 'check_box', False, 'Step 5.2: Verify Automatically Open is enabled', tab_name='Advanced')
        wf_mainobj.verify_property_dialog_save_cancel_button_enable_disable('Save', 'disable', "Step 5.3: Verify Button - Save is disabled.")
        
        """ Step 6: Close Properties panel,
        """
        wf_mainobj.close_property_dialog() 
        
        """ Step 7: Sign out
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()