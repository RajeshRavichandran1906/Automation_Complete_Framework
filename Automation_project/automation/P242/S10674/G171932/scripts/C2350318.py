'''
Created on 14 June, 2018

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10674&group_by=cases:section_id&group_id=171932&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2350318
TestCase Name = Verify editor report (html) properties
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import wf_mainpage
from common.wftools import login
from common.lib import utillity, core_utility, javascript
from selenium.common.exceptions import NoSuchElementException


class C2350318_TestClass(BaseTestCase):

    def test_C2350318(self):
        """
        TESTCASE VARIABLES
        """
        wf_login = login.Login(self.driver)
        wf_mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        core_utilobj=core_utility.CoreUtillityMethods(self.driver)
        j_scrip=javascript.JavaScript(self.driver)
        project_id = utillobj.parseinitfile('project_id')
        proj_id = str(project_id)
        home_page_css=".explore-box .ibfs-tree .home-tree-node .ibx-label-text"
        proj_sub_folder="{0}->Text Editor".format(proj_id)
        proj_sub_folder_item='html file'
        property_dialog_css='.properties-page.propPage'
        edit_button_css=".properties-general-folder [data-ibx-type='ibxButton']"
        name_box_css=".properties-general-folder [data-ibx-type*='ibxText'].ibx-widget-disabled input"
        radio_button_css=".properties-advanced-pane-tab [data-ibx-type='ibxRadioButtonSimple']"
        
        """ Step 1: Login to WebFOCUS as a Developer.
        """
        wf_login.invoke_home_page('mrid', 'mrpass')
        utillobj.synchronize_with_visble_text(home_page_css, 'Domains', 290)
        
        """ Step 2: From the new Home Page click on Content from side bar.
        """
        wf_mainobj.select_left_panel('Content')
        
        """ Step 3: Right click on P242_S10674_G171304/Text Editor/html file and select Properties.
                    Verify only General and Advanced tabs appear.
        """
        wf_mainobj.select_repository_folder_item_context_menu(proj_sub_folder_item, context_menu_item_path='Properties', folder_path=proj_sub_folder)
        utillobj.synchronize_with_number_of_element(property_dialog_css, 1, 190)
        expected_value_list=['General', 'Advanced']
        wf_mainobj.verify_property_dialog_value('General', 'tab_value', "Step 3: Verify only General, Advanced tabs appears.", property_value=expected_value_list)
        
        """ Step 4: Explore General tab.
                    Verify View All, Title, Summary, Publish and Show are enabled and Tool is editor. No owner. Save button is disabled.
                    Verify Name is enabled by clicking on Edit button next to Name box.
        """
        wf_mainobj.verify_property_dialog_enable_disable('Language', 'text', False, "Step 4: Verify View All - is enabled.")
        wf_mainobj.verify_property_dialog_enable_disable('Title', 'text_value', False, "Step 4.1: Verify Title - is enabled.")
        wf_mainobj.verify_property_dialog_enable_disable('Summary', 'text_area', False, "Step 4.2: Verify Summary - is enabled.")
        wf_mainobj.verify_property_dialog_enable_disable('Publish', 'radiobutton_value', False, "Step 4.3: Verify Publish - is enabled.")
        wf_mainobj.verify_property_dialog_value('Publish', 'radiobutton_value', "Step 4.4: Verify Publish - is enabled.", property_value='Yes')
        wf_mainobj.verify_property_dialog_enable_disable('Show', 'radiobutton_value', False, "Step 4.5: Verify Show - is enabled.")
        wf_mainobj.verify_property_dialog_value('Show', 'radiobutton_value', "Step 4.6: Verify Show - is enabled.", property_value='Yes')
        wf_mainobj.verify_property_dialog_value('Tool', 'text', "Step 4.7: Verify Tool is 'editor'", property_value='editor')
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
                    Verify Thumbnail (Default is selected - paper document, Embedded, Link radio buttons), 
                    Tags, Sort Order, Default Width, Default Height are enabled. Load in iframe is disabled.
        """
        wf_mainobj.edit_property_dialog_value('Advanced', 'tab_value', 'Advanced')
        thumbnail_row_obj=wf_mainobj.get_property_dialog_rows_object('Thumbnail', '5')
        radio_optoins_elems=thumbnail_row_obj.find_elements_by_css_selector(radio_button_css)
        actual_thumbnail_radiobutton_options=[elem.text.strip() for elem in radio_optoins_elems]
        expected_thumbnail_radiobutton_options=['Default', 'Embedded', 'Link']
        utillobj.as_List_equal(expected_thumbnail_radiobutton_options, actual_thumbnail_radiobutton_options, "Step 5: Verify Thumbnail (Default, Embedded, Link radio buttons).")
        default_radiobutoon_obj=radio_optoins_elems[expected_thumbnail_radiobutton_options.index('Default')].find_element_by_css_selector("[class^='ibx-radio-button']")
        if 'ibx-radio-button-simple-marker-check' in j_scrip.get_element_all_attributes(default_radiobutoon_obj)['class']:
            default_radiobutoon_status='checked'
        else:
            default_radiobutoon_status='unchecked'
        utillobj.asequal('checked', default_radiobutoon_status, "Step 5.1: Verify Thumbnail Default is selected.")
        wf_mainobj.verify_property_dialog_enable_disable('Tags', 'text_value', False, "Step 5.2: Verify Tags - is enabled.", tab_name='Advanced')
        wf_mainobj.verify_property_dialog_enable_disable('Sort order', 'text_value', False, "Step 5.3: Verify Sort Order - is enabled.", tab_name='Advanced')
        wf_mainobj.verify_property_dialog_enable_disable('Default width', 'text_value', False, "Step 5.4: Verify Default Width - is enabled.", tab_name='Advanced')
        wf_mainobj.verify_property_dialog_enable_disable('Default height', 'text_value', False, "Step 5.5: Verify Default Height - is enabled.", tab_name='Advanced')
        wf_mainobj.verify_property_dialog_enable_disable('Load in iframe', 'radiobutton_value', 'Yes', "Step 5.5: Verify Load in iframe - is disabled.", tab_name='Advanced')
        
        """ Step 6: Close Properties dialog.
        """
        wf_mainobj.close_property_dialog()
        
        """ Step 7: Sign out. 
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()