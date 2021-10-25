'''
Created on 13 June, 2018

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10674&group_by=cases:section_id&group_id=171932&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2350289
TestCase Name = Verify secondary sub-folder properties
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import wf_mainpage
from common.wftools import login
from common.lib import utillity, core_utility
from selenium.common.exceptions import NoSuchElementException


class C2350289_TestClass(BaseTestCase):

    def test_C2350289(self):
        """
        TESTCASE VARIABLES
        """
        wf_login = login.Login(self.driver)
        wf_mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        core_utilobj=core_utility.CoreUtillityMethods(self.driver)
        project_id = utillobj.parseinitfile('project_id')
        proj_id = str(project_id)
        home_page_css=".explore-box .ibfs-tree .home-tree-node .ibx-label-text"
        proj_sub_folder="{0}->sub1->sub2".format(proj_id)
        property_dialog_css='.properties-page.propPage'
        edit_button_css=".properties-general-folder [data-ibx-type='ibxButton']"
        name_box_css=".properties-general-folder [data-ibx-type*='ibxText'].ibx-widget-disabled input"
        
        """ Step 1: Login to WebFOCUS as a Developer
        """
        wf_login.invoke_home_page('mrid', 'mrpass')
        utillobj.synchronize_with_visble_text(home_page_css, 'Domains', 290)
        
        """ Step 2: From the new Home Page click on Content from side bar.
        """
        wf_mainobj.select_left_panel('Content')
        
        """ Step 3: Right click on P242_S10674_G171304/sub1/sub2 and select Properties from the menu.
                    Verify only General and Advanced tabs appears.
        """
        wf_mainobj.select_repository_folder_context_menu(proj_sub_folder, 'Properties')
        utillobj.synchronize_with_number_of_element(property_dialog_css, 1, 190)
        expected_value_list=['General', 'Advanced']
        wf_mainobj.verify_property_dialog_value('General', 'tab_value', "Step 3: Verify only General tabs appears.", property_value=expected_value_list)
        
        """ Step 4: Explore General tab.
                    Verify View All, Title, Summary, Publish and Show are enabled. No Tool. No owner. Save button is disabled.
                    Verify Name is enabled by clicking on Edit button next to Name box.
        """
        wf_mainobj.verify_property_dialog_enable_disable('Language', 'text', False, "Step 4: Verify View All - is enabled.")
        wf_mainobj.verify_property_dialog_enable_disable('Title', 'text_value', False, "Step 4.1: Verify Title - is enabled.")
        wf_mainobj.verify_property_dialog_enable_disable('Summary', 'text_area', False, "Step 4.2: Verify Summary - is enabled.")
        wf_mainobj.verify_property_dialog_enable_disable('Publish', 'radiobutton_value', False, "Step 4.3: Verify Publish - is enabled.")
        wf_mainobj.verify_property_dialog_value('Publish', 'radiobutton_value', "Step 4.4: Verify Publish - is enabled.", property_value='Yes')
        wf_mainobj.verify_property_dialog_enable_disable('Show', 'radiobutton_value', False, "Step 4.5: Verify Show - is enabled.")
        wf_mainobj.verify_property_dialog_value('Show', 'radiobutton_value', "Step 4.6: Verify Show - is enabled.", property_value='Yes')
        try:
            wf_mainobj.get_property_dialog_rows_object('Tool', '4.7')
            tool_status=False
        except IndexError:
            tool_status=True
        utillobj.asequal(True, tool_status, "Step 4.7: Verify No Tool")
        wf_mainobj.verify_property_dialog_value('Owner', 'text', "Step 4.8: Verify owner appears as : '-'", property_value='-')
        wf_mainobj.verify_property_dialog_save_cancel_button_enable_disable('Save', 'disable', "Step 4.9: Verify Button - Save is disabled.")
        name_row_obj=wf_mainobj.get_property_dialog_rows_object('Name', '4.10')
        edit_button_elem=name_row_obj.find_element_by_css_selector(edit_button_css)
        core_utilobj.left_click(edit_button_elem)
        try:
            name_row_obj.find_element_by_css_selector(name_box_css)
            status=False
        except NoSuchElementException:
            status=True
        utillobj.asequal(status, True, "Step 4.11: Verify Name is enabled by clicking on Edit button next to Name box.")
        
        """ Step 5: Click on Advanced tab.
                    Verify Automatically create My Content folders disabled, Automatically Open unchecked and enabled, Sort Order is enabled.
        """
        wf_mainobj.edit_property_dialog_value('Advanced', 'tab_value', 'Advanced')
        wf_mainobj.verify_property_dialog_enable_disable('Automatically create My Content folders', 'check_box', 'Automatically create My Content folders', 'Step 5: Verify Automatically create My Content folders is disable.', tab_name='Advanced')
        wf_mainobj.verify_property_dialog_enable_disable('Automatically open', 'check_box', False, 'Step 5.1: Verify Automatically Open is enabled', tab_name='Advanced')
        automatically_open_obj=wf_mainobj.get_property_dialog_rows_object('Automatically open', '5.2')
        try:
            status=automatically_open_obj.find_element_by_css_selector(".ibx-check-box-simple-marker-uncheck").is_displayed()
        except NoSuchElementException:
            status=False
        utillobj.asequal(True, status, "Step 5.3: Verify Automatically Open is unchecked.")
        wf_mainobj.verify_property_dialog_enable_disable('Sort order', 'text_value', False, "Step 5.4: Verify Sort Order - is enabled.", tab_name='Advanced')
        
        """ Step 6: Close Properties dialog.
        """
        wf_mainobj.close_property_dialog()
        
        """ Step 7: Sign out.
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()