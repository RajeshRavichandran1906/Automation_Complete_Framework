'''
Created on 13 June, 2018

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10674&group_by=cases:section_id&group_id=171932&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2350273
TestCase Name = Verify report library properties
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import wf_mainpage
from common.wftools import login
from common.lib import utillity, core_utility, javascript
from selenium.common.exceptions import NoSuchElementException


class C2350273_TestClass(BaseTestCase):

    def test_C2350273(self):
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
        proj_sub_folder="{0}->Report Library".format(proj_id)
        proj_sub_folder_item='Report Library Reports'
        property_dialog_css='.properties-page.propPage'
        edit_button_css=".properties-general-folder [data-ibx-type='ibxButton']"
        name_box_css=".properties-general-folder [data-ibx-type*='ibxText'].ibx-widget-disabled input"
        radio_button_css=".properties-advanced-pane-tab [data-ibx-type='ibxRadioButtonSimple']"
        schedule_value_css=".caster-entry:not(.caster-detail-name)"
        
        """ Step 1: Login to WebFOCUS as a Developer
        """
        wf_login.invoke_home_page('mrid', 'mrpass')
        utillobj.synchronize_with_visble_text(home_page_css, 'Domains', 290)
        
        """ Step 2: From the new Home Page click on Content from side bar.
        """
        wf_mainobj.select_left_panel('Content')
        
        """ Step 3: Right click on P242_S10674_G171304/Report Library/Report Library Reports and select Properties from the menu.
                    Verify only General, Advanced and Library Details tabs appears.
        """
        wf_mainobj.select_repository_folder_item_context_menu(proj_sub_folder_item, context_menu_item_path='Properties', folder_path=proj_sub_folder)
        utillobj.synchronize_with_number_of_element(property_dialog_css, 1, 190)
        expected_value_list=['General', 'Advanced', 'Library Details']
        wf_mainobj.verify_property_dialog_value('General', 'tab_value', "Step 3: Verify only General, Advanced and Library Details tabs appears.", property_value=expected_value_list)
        
        """ Step 4: Explore General tab.
                    Verify View All, Title, Summary, Publish and Show are enabled. Verify dates appear. Tool is report library. No Owner. Save button is disabled.
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
        wf_mainobj.verify_property_dialog_value('Tool', 'text', "Step 4.10: Verify Tool as : 'reportlibrary'", property_value='reportlibrary')
        wf_mainobj.verify_property_dialog_value('Owner', 'text', "Step 4.11: Verify owner appears as : '-'", property_value='-')
        wf_mainobj.verify_property_dialog_save_cancel_button_enable_disable('Save', 'disable', "Step 4.12: Verify Button - Save is disabled.")
        name_row_obj=wf_mainobj.get_property_dialog_rows_object('Name', '4.13')
        edit_button_elem=name_row_obj.find_element_by_css_selector(edit_button_css)
        core_utilobj.left_click(edit_button_elem)
        try:
            name_row_obj.find_element_by_css_selector(name_box_css)
            status=False
        except NoSuchElementException:
            status=True
        utillobj.asequal(status, True, "Step 4.14: Verify Name is enabled by clicking on Edit button next to Name box.")
        
        """ Step 5: Click on Advanced tab.
                    Thumbnail (Default is selected - Report Library thumbnail, Embedded, Link radio buttons) and Sort Order enabled.
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
        wf_mainobj.verify_property_dialog_enable_disable('Sort order', 'text_value', False, "Step 5.3: Verify Sort Order - is enabled.", tab_name='Advanced')
        
        """ Step 6: Click on Library Details tab.
                    Verify library details properties appears as below.
        """
        wf_mainobj.edit_property_dialog_value('Library Details', 'tab_value', 'Library Details')
        access_list_title_value_obj=wf_mainobj.get_property_dialog_rows_object("Access List Title:", '6')
        access_list_title_value=access_list_title_value_obj.find_element_by_css_selector(schedule_value_css).text.strip()
        utillobj.asequal('N/A', access_list_title_value, "Step 6.1: Verify Access List Title is N/A.")
        burst_value_obj=wf_mainobj.get_property_dialog_rows_object("Burst Value:", '6.2')
        burst_value=burst_value_obj.find_element_by_css_selector(schedule_value_css).text.strip()
        utillobj.asequal('', burst_value, "Step 6.3: Verify Burst Value is  .")
        category_value_obj=wf_mainobj.get_property_dialog_rows_object("Category:", '6.4')
        category_value=category_value_obj.find_element_by_css_selector(schedule_value_css).text.strip()
        utillobj.asequal('', category_value, "Step 6.5: Verify Category is  .")
        expiration_interval_value_obj=wf_mainobj.get_property_dialog_rows_object("Expiration Interval:", '6.6')
        expiration_interval_value=expiration_interval_value_obj.find_element_by_css_selector(schedule_value_css).text.strip()
        utillobj.asequal('1', expiration_interval_value, "Step 6.7: Verify Expiration Interval is '1'.")
        expiration_type_value_obj=wf_mainobj.get_property_dialog_rows_object("Expiration Type:", '6.8')
        expiration_type_value=expiration_type_value_obj.find_element_by_css_selector(schedule_value_css).text.strip()
        utillobj.asequal('N', expiration_type_value, "Step 6.8: Verify Expiration Type is N")
        last_execution_value_obj=wf_mainobj.get_property_dialog_rows_object("Last Execution:", '6.9')
        last_execution_value=last_execution_value_obj.find_element_by_css_selector(schedule_value_css).text.strip()
        utillobj.asequal('Friday, May 11, 2018 4:43:04 PM EDT', last_execution_value, "Step 6.10: Verify Last Execution is 'Friday, May 11, 2018 4:43:04 PM EDT'.")
        last_version_value_obj=wf_mainobj.get_property_dialog_rows_object("Last Version:", '6.11')
        last_version_value=last_version_value_obj.find_element_by_css_selector(schedule_value_css).text.strip()
        utillobj.asequal('1', last_version_value, "Step 6.12: Verify Last Version is 1")
        schedule_id_value_obj=wf_mainobj.get_property_dialog_rows_object("Schedule Id:", '6.13')
        schedule_id_value=schedule_id_value_obj.find_element_by_css_selector(schedule_value_css).text.strip()
        utillobj.asequal('S3e52bed6sc6fbs453fsa76eseb84363a6099', schedule_id_value, "Step 6.14: Verify Schedule Id is 'S3e52bed6sc6fbs453fsa76eseb84363a6099'.")
        schedule_title_value_obj=wf_mainobj.get_property_dialog_rows_object("Schedule Title:", '6.15')
        schedule_title_value=schedule_title_value_obj.find_element_by_css_selector(schedule_value_css).text.strip()
        utillobj.asequal('N/A', schedule_title_value, "Step 6.16: Verify Schedule Title is N/A")
        task_id_value_obj=wf_mainobj.get_property_dialog_rows_object("Task Id:", '6.16')
        task_id_value=task_id_value_obj.find_element_by_css_selector(schedule_value_css).text.strip()
        utillobj.asequal('T8c24e2a6t3f47t4ef5taa17tb193b58a83a6', task_id_value, "Step 6.17: Verify Task Id is 'T8c24e2a6t3f47t4ef5taa17tb193b58a83a6'.")
        
        """ Step 7: Close Properties dialog.
        """
        wf_mainobj.close_property_dialog()
        
        """ Step 8: Sign out.
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()