'''
Created on 07 June, 2018

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10674&group_by=cases:section_id&group_id=171932&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2350198
TestCase Name = Verify page properties
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import wf_mainpage
from common.wftools import login
from common.lib import utillity, core_utility, javascript
from selenium.common.exceptions import NoSuchElementException


class C2350198_TestClass(BaseTestCase):

    def test_C2350198(self):
        """
        TESTCASE VARIABLES
        """
        wf_login = login.Login(self.driver)
        wf_mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        core_utilobj=core_utility.CoreUtillityMethods(self.driver)
        j_scrip=javascript.JavaScript(self.driver)
        project_id = utillobj.parseinitfile('project_id')
        admin_user_name = utillobj.parseinitfile('mrid01')
        proj_id = str(project_id)
        home_page_css=".explore-box .ibfs-tree .home-tree-node .ibx-label-text"
        proj_sub_folder="{0}->Page Designer".format(proj_id)
        proj_sub_folder_item="Page 1"
        property_dialog_css='.properties-page.propPage'
        edit_button_css=".properties-general-folder [data-ibx-type='ibxButton']"
        name_box_css=".properties-general-folder [data-ibx-type*='ibxText'].ibx-widget-disabled input"
        radio_button_css=".properties-advanced-pane-tab [data-ibx-type='ibxRadioButtonSimple']"
        advanced_tab_checkbox_css=".properties-advanced-pane-tab [role='checkbox']"
        advanced_tab_css = ".tpg-selected .properties-advanced-item-fex"
        
        """ Step 1: Login to WebFOCUS as a Developer
        """
        wf_login.invoke_home_page('mrid', 'mrpass')
        utillobj.synchronize_with_visble_text(home_page_css, 'Domains', 290)
        
        """ Step 2: From the new Home Page click on Content page from side bar.
        """
        wf_mainobj.select_left_panel('Content')
        
        """ Step 3: Right click on P242_S10674_G171304/Page Designer/Page1 and select properties from the menu.
                    Verify only General and Advanced tabs appear.
        """
        wf_mainobj.select_repository_folder_item_context_menu(proj_sub_folder_item, context_menu_item_path='Properties', folder_path=proj_sub_folder)
        utillobj.synchronize_with_number_of_element(property_dialog_css, 1, 190)
        expected_value_list=['General', 'Advanced']
        wf_mainobj.verify_property_dialog_value('General', 'tab_value', "Step 3: Verify only General and Advanced tabs appear.", property_value=expected_value_list)
        
        """ Step 4: Explore General tab.
                    Verify View All, Title, Summary, Publish and Show are enabled. Verify dates appear. No owner and save button is disabled.
                    Verify Name is enabled by clicking on Edit button next to Name box.
        """
        wf_mainobj.verify_property_dialog_enable_disable('Language', 'text', False, "Step 4: Verify View All - is enabled.")
        wf_mainobj.verify_property_dialog_enable_disable('Title', 'text_value', False, "Step 4.1: Verify Title - is enabled.")
        wf_mainobj.verify_property_dialog_enable_disable('Summary', 'text_area', False, "Step 4.2: Verify Summary - is enabled.")
        wf_mainobj.verify_property_dialog_enable_disable('Publish', 'radiobutton_value', False, "Step 4.3: Verify Publish - is enabled.")
        wf_mainobj.verify_property_dialog_value('Publish', 'radiobutton_value', "Step 4.4: Verify Publish - is enabled.", property_value='Yes')
        wf_mainobj.verify_property_dialog_enable_disable('Show', 'radiobutton_value', False, "Step 4.5: Verify Show - is enabled.")
        wf_mainobj.verify_property_dialog_value('Show', 'radiobutton_value', "Step 4.6: Verify Show - is enabled.", property_value='Yes')
        created_date=wf_mainobj.get_property_created_modified_accessed_time('Created', '4.7')
        wf_mainobj.verify_created_modified_accessed_time_formate(created_date, admin_user_name, "Step 4.7.1: Verify Created dates appear.")
        modified_date=wf_mainobj.get_property_created_modified_accessed_time('Modified', '4.8')
        wf_mainobj.verify_created_modified_accessed_time_formate(modified_date, admin_user_name, "Step 4.8.1: Verify Modified dates appear.")
        accessed_date=wf_mainobj.get_property_created_modified_accessed_time('Accessed', '4.9')
        wf_mainobj.verify_created_modified_accessed_time_formate(accessed_date, admin_user_name, "Step 4.9.1: Verify Accessed dates appear.")
        wf_mainobj.verify_property_dialog_value('Owner', 'text', "Step 4.10: Verify owner appears as : '-'", property_value='-')
        wf_mainobj.verify_property_dialog_save_cancel_button_enable_disable('Save', 'disable', "Step 4.11: Verify Button - Save is disabled.")
        name_row_obj=wf_mainobj.get_property_dialog_rows_object('Name', '4.12')
        edit_button_elem=name_row_obj.find_element_by_css_selector(edit_button_css)
        core_utilobj.left_click(edit_button_elem)
        try:
            name_row_obj.find_element_by_css_selector(name_box_css)
            status=False
        except NoSuchElementException:
            status=True
        utillobj.asequal(status, True, "Step 4.13: Verify Name is enabled by clicking on Edit button next to Name box.")
        
        """ Step 5: Click on Advanced tab.
                    Verify Thumbnail (Default is selected - page designer thumbnail, Embedded, Link radio buttons), Tags, Sort Order enabled. 
                    Load in iframe is disabled. No checkboxes for advanced properties appears.
        """
        wf_mainobj.edit_property_dialog_value('Advanced', 'tab_value', 'Advanced')
        thumbnail_row_obj=wf_mainobj.get_property_dialog_rows_object('Thumbnail', '5')
        radio_optoins_elems=thumbnail_row_obj.find_elements_by_css_selector(radio_button_css)
        actual_thumbnail_radiobutton_options=[elem.text.strip() for elem in radio_optoins_elems]
        expected_thumbnail_radiobutton_options=['Default', 'Embedded', 'Link']
        utillobj.as_List_equal(expected_thumbnail_radiobutton_options, actual_thumbnail_radiobutton_options, "Step 5.1: Verify Thumbnail (Default, Embedded, Link radio buttons).")
        default_radiobutoon_obj=radio_optoins_elems[expected_thumbnail_radiobutton_options.index('Default')].find_element_by_css_selector("[class^='ibx-radio-button']")
        if 'ibx-radio-button-simple-marker-check' in j_scrip.get_element_all_attributes(default_radiobutoon_obj)['class']:
            default_radiobutoon_status='checked'
        else:
            default_radiobutoon_status='unchecked'
        utillobj.asequal('checked', default_radiobutoon_status, "Step 5.2: Verify Thumbnail Default is selected.")
        properties_advanced_item_elem=self.driver.find_element_by_css_selector(advanced_tab_css)
        utillobj.verify_regional_picture_using_sikuli('page1.png', "Step 5.1.1: Verify Default is selected - page designer.", parent_element=properties_advanced_item_elem)
        wf_mainobj.verify_property_dialog_enable_disable('Tags', 'text_value', False, "Step 5.3: Verify Tags - is enabled.", tab_name='Advanced')
        wf_mainobj.verify_property_dialog_enable_disable('Sort order', 'text_value', False, "Step 5.4: Verify Sort Order - is enabled.", tab_name='Advanced')
        wf_mainobj.verify_property_dialog_enable_disable('Load in iframe', 'radiobutton_value', 'Yes', "Step 5.5: Verify Load in iframe - is disabled.", tab_name='Advanced')
        try:
            checkbox_value=self.driver.find_element_by_css_selector(advanced_tab_checkbox_css).text
            status=True if checkbox_value is '' else False
        except NoSuchElementException:
            status=True
        utillobj.asequal(True, status, "Step 5.6: Verify no checkboxes for advanced properties appears.")
        
        """ Step 6: Close Properties dialog.
        """
        wf_mainobj.close_property_dialog() 
        
        """ Step 7: Sign out.
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()