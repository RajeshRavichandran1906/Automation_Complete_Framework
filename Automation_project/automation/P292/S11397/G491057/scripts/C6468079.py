'''
Created on September 10, 2018

@author: AA14564

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/11397&group_by=cases:section_id&group_id=491057&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6468079
TestCase Name = Verify Tags are propageted from Favorite's target item
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.pages import wf_mainpage as wfmain_page
from common.lib import utillity
from common.locators import wf_mainpage_locators

class C6468079_TestClass(BaseTestCase):

    def test_C6468079(self):
        
        """
        TESTCASE Objects & VARIABLES
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        page_mainpageobj = wfmain_page.Wf_Mainpage(driver)
        content_css=wf_mainpage_locators.WfMainPageLocators.CONTENT_CSS
        medium_wait = 145
        crumb_box_css = ".crumb-box .ibx-label-text"
        files_box_css = ".content-box.ibx-widget .files-box .ibx-label-text"
#         property_dialog_css='.properties-page.propPage'
        project_id = utillobj.parseinitfile('project_id')
        suite_id = utillobj.parseinitfile('suite_id')
        suite_path="{0}_{1}".format(str(project_id), str(suite_id))
        parent_group_id = "G491033"
        parent_group_id_path = "{0}->{1}".format(suite_path, parent_group_id)
        report_path = "{0}->Reports".format(parent_group_id_path)
        report_item = 'Margin by Product Category'
        report_store_item = 'Quantity Sold By Stores'
        report_sales_item= 'Sales Metrics YTD'
        
        def verify_property_dialog_placeholder(property_name, expected_value, step_number):
            property_elem = page_mainpageobj.get_property_dialog_rows_object('Advanced', property_name, step_number)
            actual_value = property_elem.find_element_by_css_selector("input").get_attribute('placeholder')
            msg = "Step {0}: Verify {1} property placeholder value.".format(step_number, property_name)
            utillobj.asequal(expected_value, actual_value, msg)
            
        
        """ Step 1: Sign into WebFOCUS Home Page as Developer User.
        """
        wftools_login_obj.invoke_home_page('mriddev', 'mrpassdev')
        utillobj.synchronize_with_visble_text(content_css, "Content", 60)
        wfmain_obj.select_content_from_sidebar()
        utillobj.wait_for_page_loads(10)
        """ Step 2: From domain, Expand 'P292_S11397' > 'G491033' > click on Reports in tree.
        """
        wfmain_obj.click_repository_folder(report_path)
         
        """ Step 3: Right click on 'Margin by Product Category' > Properties > Advanced tab.
        """
        wfmain_obj.right_click_folder_item_and_select_menu(report_item, context_menu_item_path='Properties')
#         utillobj.synchronize_with_number_of_element(property_dialog_css, 1, 190)
        utillobj.synchronize_with_visble_text('div .properties-tab-pane', 'Advanced', wfmain_obj.home_page_long_timesleep)
        wfmain_obj.select_property_tab_value('Advanced')
         
        """ Step 4: Click on Tags text box and enter 'FAVES' > Click Save and Close.
        """
        wfmain_obj.edit_property_dialog_value('Tags', 'text_value', 'FAVES', tab_name='Advanced')
        wfmain_obj.select_property_dialog_save_cancel_button('Save')
        wfmain_obj.close_property_dialog()
         
        """ Step 5: Click on 'Quantity Sold By Stores' > Properties > Advanced tab.
        """
        wfmain_obj.right_click_folder_item_and_select_menu(report_store_item, context_menu_item_path='Properties')
#         utillobj.synchronize_with_number_of_element(property_dialog_css, 1, 190)
        utillobj.synchronize_with_visble_text('div .properties-tab-pane', 'Advanced', wfmain_obj.home_page_long_timesleep)
        wfmain_obj.select_property_tab_value('Advanced')
         
        """ Step 6: Click on Tags text box and enter 'FAVES' > Click Save and Close.
        """
        wfmain_obj.edit_property_dialog_value('Tags', 'text_value', 'FAVES', tab_name='Advanced')
        wfmain_obj.select_property_dialog_save_cancel_button('Save')
        wfmain_obj.close_property_dialog()
         
        """ Step 7: Right click on 'Margin by Product Category' > Click on Add to Favorites.
                    Right click on'Quantity Sold By Stores' > Click on Add to Favorites.
        """
        time.sleep(5)
        wfmain_obj.right_click_folder_item_and_select_menu(report_item, context_menu_item_path='Add to Favorites')
        time.sleep(3)
        wfmain_obj.right_click_folder_item_and_select_menu(report_store_item, context_menu_item_path='Add to Favorites')
         
        """ Step 8: Click Favorites view from the side bar.
                    Verify 'Margin by Product Category' and 'Quantity Sold By Stores' are added.
        """
        wfmain_obj.select_favorites_from_sidebar()
        utillobj.synchronize_with_visble_text(crumb_box_css, "Favorites", medium_wait)
        utillobj.synchronize_with_visble_text('div .content-box', report_store_item, medium_wait)
        wfmain_obj.verify_items_in_grid_view([report_item, report_store_item], 'asin', "Step 08.01 : Verify '{0}','{1}' is added in Favorites view".format(report_item, report_store_item))
          
        """ Step 9: Right click on 'Margin by Product Category' > Properties > Advanced tab.
                    Verify Tags shows 'FAVES'.
        """
        wfmain_obj.right_click_folder_item_and_select_menu(report_item, context_menu_item_path='Properties')
#         utillobj.synchronize_with_number_of_element(property_dialog_css, 1, 190)
        utillobj.synchronize_with_visble_text('div .properties-tab-pane', 'Advanced', wfmain_obj.home_page_long_timesleep)
        wfmain_obj.select_property_tab_value('Advanced')
        time.sleep(3)
        verify_property_dialog_placeholder('Tags', 'FAVES', '09.01 ')
         
        """ Step 10: Click Close.
        """
        wfmain_obj.close_property_dialog()
         
        """ Step 11: Right click on 'Quantity Sold By Stores' > Properties > Advanced tab.
                     Verify Tags shows 'FAVES'.
        """
        wfmain_obj.right_click_folder_item_and_select_menu(report_store_item, context_menu_item_path='Properties')
        utillobj.synchronize_with_visble_text('div .properties-tab-pane', 'Advanced', wfmain_obj.home_page_long_timesleep)
        wfmain_obj.select_property_tab_value('Advanced')
        time.sleep(3)
        verify_property_dialog_placeholder('Tags', 'FAVES', '11.01 ')
         
        """ Step 12: Click Close.
        """
        wfmain_obj.close_property_dialog()
         
        """ Step 13: Click on Content View from the side bar.
        """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_visble_text(files_box_css, "Folders", 45)
         
        """ Step 14: From domain, Expand 'P292_S11397' > 'G491033' > click on Reports in tree.
        """
        wfmain_obj.click_repository_folder(report_path)
         
        """ Step 15: Right click on 'Sales Metrics YTD' > Properties > Advanced tab.
        """
        wfmain_obj.right_click_folder_item_and_select_menu(report_sales_item, context_menu_item_path='Properties')
        utillobj.synchronize_with_visble_text('div .properties-tab-pane', 'Advanced', wfmain_obj.home_page_long_timesleep)
        wfmain_obj.select_property_tab_value('Advanced')
         
        """ Step 16: Click on Tags text box and enter 'Test_tag' > Click Save and Close.
        """
        wfmain_obj.edit_property_dialog_value('Tags', 'text_value', 'Test_tag', tab_name='Advanced')
        wfmain_obj.select_property_dialog_save_cancel_button('Save')
        wfmain_obj.close_property_dialog()
         
        """ Step 17: Right click on 'Sales Metrics YTD' > Add to Favorites.
        """
        wfmain_obj.right_click_folder_item_and_select_menu(report_sales_item, context_menu_item_path='Add to Favorites')
        
        """ Step 18: Click on Favorites from the side bar.
                     Verify 'Margin by Product Category' , 'Quantity Sold By Stores' and 'Sales Metrics YTD' are shown and 
                     also Local tag is showing since few or more items have different tags.
        """
        wfmain_obj.select_favorites_from_sidebar()
        utillobj.synchronize_with_visble_text(crumb_box_css, "Favorites", medium_wait)
        utillobj.synchronize_with_visble_text('div .content-box', report_store_item, medium_wait)
        wfmain_obj.verify_items_in_grid_view([report_item, report_store_item, report_sales_item], 'asin', "Step 18.01: Verify '{0}','{1}', '{2}' is added in Favorites view".format(report_item, report_store_item, report_sales_item))
        wfmain_obj.verify_favorites_tags(['Mobile Faves', 'Test_tag'], '18.02 ')
        
        """ Step 19: Revert back the Home Page by its default state (Click content from side bar and click on Domain from navigation bar)
        """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_visble_text(files_box_css, "Folders", 45)
        wfmain_obj.select_option_from_crumb_box('Domains')
        
        """ Step 20: In the banner link, click on the top right username > Click Sign Out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()        