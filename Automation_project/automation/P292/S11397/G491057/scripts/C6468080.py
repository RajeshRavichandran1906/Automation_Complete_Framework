'''
Created on September 11, 2018

@author: AA14564

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/11397&group_by=cases:section_id&group_id=491057&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6468080
TestCase Name = Verify Projected tags are shown as placeholder text
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.pages import wf_mainpage as wfmain_page
from common.lib import utillity
from common.locators import wf_mainpage_locators

class C6468080_TestClass(BaseTestCase):

    def test_C6468080(self):
        
        """
        TESTCASE Objects & VARIABLES
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        page_mainpageobj = wfmain_page.Wf_Mainpage(driver)
        content_css=wf_mainpage_locators.WfMainPageLocators.CONTENT_CSS
        long_wait = 190
        medium_wait = 145
        crumb_box_css = ".crumb-box .ibx-label-text"
        files_box_css = ".content-box.ibx-widget .files-box .ibx-label-text"
        folders_css="[data-ibxp-text*='Folders']"
        property_dialog_css='.properties-page.propPage'
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
        
        """ Step 2: Click on Favorites from the side bar.
                    Verify 'Margin by Product Category' , 'Quantity Sols By Stores' and 'Sales Metrics YTD' are shown and 
                    also Local tag is showing since few or more items have different tags.
        """
        wfmain_obj.select_favorites_from_sidebar()
        utillobj.synchronize_with_visble_text(crumb_box_css, "Favorites", medium_wait)
        wfmain_obj.verify_items_in_grid_view([report_item, report_store_item, report_sales_item], 'asin', "Step 2: Verify '{0}','{1}', '{2}' is added in Favorites view".format(report_item, report_store_item, report_sales_item))
        wfmain_obj.verify_favorites_tags(['Mobile Faves', 'Test_tag'], '2.1')
        
        """ Step 3: Right click on 'Margin by Product Category' > Properties > Advanced tab.
                    Verify tags appear as placeholder text.
        """
        wfmain_obj.right_click_folder_item_and_select_menu(report_item, context_menu_item_path='Properties')
        utillobj.synchronize_with_number_of_element(property_dialog_css, 1, 190)
        wfmain_obj.select_property_tab_value('Advanced')
        time.sleep(3)
        verify_property_dialog_placeholder('Tags', 'FAVES', '3')
        wfmain_obj.close_property_dialog()
        time.sleep(3)
        """ Step 4: Revert back the Home Page by its default state (Click content from side bar and click on Domain from navigation bar)
        """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_visble_text(files_box_css, "Folders", 45)
        wfmain_obj.select_option_from_crumb_box('Domains')
        
        """ Step 5: In the banner link, click on the top right username > Click Sign Out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()        