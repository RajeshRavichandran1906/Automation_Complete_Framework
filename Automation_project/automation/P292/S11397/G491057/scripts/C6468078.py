'''
Created on September 06, 2018

@author: AA14564

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/11397&group_by=cases:section_id&group_id=491057&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6468078
TestCase Name = Verify Add to Mobile Favorites is removed from the context menu menu on all items in the repository.
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators

class C6468078_TestClass(BaseTestCase):

    def test_C6468078(self):
        
        """
        TESTCASE Objects & VARIABLES
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        content_css=wf_mainpage_locators.WfMainPageLocators.CONTENT_CSS
        long_wait = 190
        folders_css="[data-ibxp-text*='Folders']"
        project_id = utillobj.parseinitfile('project_id')
        suite_id = utillobj.parseinitfile('suite_id')
        suite_path="{0}_{1}".format(str(project_id), str(suite_id))
        parent_group_id = "G491033"
        parent_group_id_path = "{0}->{1}".format(suite_path, parent_group_id)
        report_path = "{0}->Reports".format(parent_group_id_path)
        report_item = 'Margin by Product Category'
        report_shortcut_item = 'Margin by Product Category - Shortcut'
        portal_item = "Retail Samples"
        portal_filter_item= "Retail Sales Filter Panel"
        portal_sales_data_item = "Retail Sales Data"
        chart_item = "Arc - Sales by Region"
        visualization_item = "Analytical Dashboard"
        mobile_item = "Store Sales by Region"

        
        """ Step 1: Sign into WebFOCUS Home Page as Developer User.
        """
        wftools_login_obj.invoke_home_page('mriddev', 'mrpassdev')
        utillobj.synchronize_with_visble_text(content_css, "Content", 60)
        
        """ Step 2: From domain, Expand 'P292_S11397' > 'G491033' > click on Reports in tree.
        """
        wfmain_obj.click_repository_folder(report_path)
        
        """ Step 3: Right click on 'Margin by Product Category'.
                    Verify Mobile Favorites option is removed and Add to Favorites option is displayed.
        """
        wfmain_obj.verify_repository_folder_item_context_menu(report_item, ['Mobile Favorites'], msg="Step 3:", comparision_type='asnotin')
        wfmain_obj.verify_repository_folder_item_context_menu(report_item, ['Add to Favorites'], folder_path='Reports', msg="Step 3.1:", comparision_type='asin')
        
        """ Step 4: Right click on 'Margin by Product Category - Shortcut'.
                    Verify Mobile Favorites option is removed and Add to Favorites option is displayed.
        """
        wfmain_obj.verify_repository_folder_item_context_menu(report_shortcut_item, ['Mobile Favorites'], folder_path='Reports', msg="Step 4:", comparision_type='asnotin')
        wfmain_obj.verify_repository_folder_item_context_menu(report_shortcut_item, ['Add to Favorites'], folder_path='Reports', msg="Step 4.1:", comparision_type='asin')
        
        
        """ Step 5: Click on Portal in tree and right click on 'Retail Samples' portal.
                    Verify Mobile Favorites option is removed and Add to Favorites option is displayed.
        """
        wfmain_obj.verify_repository_folder_item_context_menu(portal_item, ['Mobile Favorites'], folder_path='Portal', msg="Step 5:", comparision_type='asnotin')
        wfmain_obj.verify_repository_folder_item_context_menu(portal_item, ['Add to Favorites'], folder_path='Portal', msg="Step 5.1:", comparision_type='asin')
        
        """ Step 6: Right click on 'Retail Sales Filter Panel' html file.
                    Verify Mobile Favorites option is removed and Add to Favorites option is displayed.
        """
        wfmain_obj.verify_repository_folder_item_context_menu(portal_filter_item, ['Mobile Favorites'], folder_path='Portal', msg="Step 6:", comparision_type='asnotin')
        wfmain_obj.verify_repository_folder_item_context_menu(portal_filter_item, ['Add to Favorites'], folder_path='Portal', msg="Step 6.1:", comparision_type='asin')
        
        """ Step 7: Right click on 'Retail Sales Data' reporting object.
                    Verify Mobile Favorites option is removed and Add to Favorites option is displayed.
        """
        wfmain_obj.verify_repository_folder_item_context_menu(portal_sales_data_item, ['Mobile Favorites'], folder_path='Portal', msg="Step 7:", comparision_type='asnotin')
        wfmain_obj.verify_repository_folder_item_context_menu(portal_sales_data_item, ['Add to Favorites'], folder_path='Portal', msg="Step 7.1:", comparision_type='asin')
        
        """ Step 8: Click on Charts folder and right click on 'Arc-Sales by Region'.
                    Verify Mobile Favorites option is removed and Add to Favorites option is displayed.
        """
        utillobj.wait_for_page_loads(10)
        wfmain_obj.verify_repository_folder_item_context_menu(chart_item, ['Mobile Favorites'], folder_path='Charts', msg="Step 8:", comparision_type='asnotin')
        wfmain_obj.verify_repository_folder_item_context_menu(chart_item, ['Add to Favorites'], folder_path='Charts', msg="Step 8.1:", comparision_type='asin')
        
        """ Step 9: Click on Visualizations folder and right click on 'Analytical Dashboard'.
                    Verify Mobile Favorites option is removed and Add to Favorites option is displayed.
        """
        wfmain_obj.verify_repository_folder_item_context_menu(visualization_item, ['Mobile Favorites'], folder_path='Visualizations', msg="Step 9:", comparision_type='asnotin')
        wfmain_obj.verify_repository_folder_item_context_menu(visualization_item, ['Add to Favorites'], folder_path='Visualizations', msg="Step 9.1:", comparision_type='asin')
        
        """ Step 10: Expand Mobile > click on Tablet-Oriented Content (Demo1) and right click on 'Store Sales by Region'.
                     Verify Mobile Favorites option is removed and Add to Favorites option is displayed.
        """
        utillobj.wait_for_page_loads(10)
        wfmain_obj.verify_repository_folder_item_context_menu(mobile_item, ['Mobile Favorites'], folder_path='Mobile->Tablet-Oriented Content (Demo1)', msg="Step 10:", comparision_type='asnotin')
        wfmain_obj.verify_repository_folder_item_context_menu(mobile_item, ['Add to Favorites'], folder_path='Mobile->Tablet-Oriented Content (Demo1)', msg="Step 10.1:", comparision_type='asin')
        
        """ Step 11: Revert back the Home Page by its default state (Click content from side bar and click on Domain from navigation bar)
        """
        wfmain_obj.collapse_repository_folder('Domains')
        
        """ Step 12: In the banner link, click on the top right username > Click Sign Out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()        