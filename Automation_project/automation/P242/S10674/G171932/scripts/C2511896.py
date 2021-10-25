'''
Created on 02 July, 2018

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10674&group_by=cases:section_id&group_id=171932&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2511896
TestCase Name = Open Properties,double click Domains,script error
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import wf_mainpage
from common.wftools import login
from common.lib import utillity, core_utility
from selenium.common.exceptions import NoSuchElementException


class C2511896_TestClass(BaseTestCase):

    def test_C2511896(self):
        """
        TESTCASE VARIABLES
        """
        wf_login = login.Login(self.driver)
        wf_mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        core_utilobj=core_utility.CoreUtillityMethods(self.driver)
        home_page_css=".explore-box .ibfs-tree .home-tree-node .ibx-label-text"
        proj_sub_folder="Retail Samples->Reports"
        proj_sub_folder_item='Sales Metrics YTD'
        property_dialog_css='.properties-page.propPage'
        property_dialog_title_css=".propPage .properties-page-titlebar .ibx-label-text"
        breadcrumb_css=".right-main-panel .toolbar [data-ibx-type='breadCrumbTrail'] [data-ibx-type='ibxButtonSimple']"
        
        
        """ Step 1: Login to WebFOCUS as a Developer
        """
        wf_login.invoke_home_page('mrid', 'mrpass')
        utillobj.synchronize_with_visble_text(home_page_css, 'Domains', 290)
        
        """ Step 2: From the new Home Page click on Content from side bar.
        """
        wf_mainobj.select_left_panel('Content')
        
        """ Step 3: Open Retail Samples/Reports
        """
        """ Step 4: Right click Sales Metrics YTD and select Properties
        """
        wf_mainobj.select_repository_folder_item_context_menu(proj_sub_folder_item, context_menu_item_path='Properties', folder_path=proj_sub_folder)
        utillobj.synchronize_with_number_of_element(property_dialog_css, 1, 190)
        
        """ Step 5: Click Retail Samples in tree
                    Verify script error does not occur
        """
        wf_mainobj.expand_repository_folders('Retail Samples')
        utillobj.synchronize_with_visble_text(property_dialog_title_css, 'Retail Samples', 19)
        property_dialog_title_text = self.driver.find_element_by_css_selector(property_dialog_title_css).text.strip()
        utillobj.asequal('Retail Samples', property_dialog_title_text, "Step 5: Verify script error does not occur.")
        
        """ Step 6: Click Retail Samples in breadcrumb trail
                    Verify script error does not occur
        """
        try:
            breadcrumb_elems=self.driver.find_elements_by_css_selector(breadcrumb_css)
            breadcrumb_retail_samples_elem=[elem for elem in breadcrumb_elems if elem.text.strip()=='Retail Samples']
        except NoSuchElementException:
            raise AttributeError("Breadcrumb trail is not exist.")
        except IndexError:
            raise IndexError("Step 6: Retail Samples is not exist in breadcrumb trail.")
        core_utilobj.left_click(breadcrumb_retail_samples_elem[0])
        property_dialog_title_text = self.driver.find_element_by_css_selector(property_dialog_title_css).text.strip()
        utillobj.asequal('Retail Samples', property_dialog_title_text, "Step 6: Verify script error does not occur.")
        
        """ Step 7: Close Properties panel
        """
        wf_mainobj.close_property_dialog()
        
        """ Step 8: Sign out
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()