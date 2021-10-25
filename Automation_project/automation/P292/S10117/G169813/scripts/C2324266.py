'''
Created on 15-Nov-2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324266
TestCase Name = Properties testing : Change title
'''
import unittest, time
from common.lib import utillity
from common.pages import visualization_resultarea, vfour_portal_canvas, vfour_portal_run, wf_legacymainpage
from common.lib.basetestcase import BaseTestCase

class C2324266_TestClass(BaseTestCase):

    def test_C2324266(self):
        """
        TESTCASE VARIABLES
        """
        workspace = "Workspaces"
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        portal_canvas = vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        portal_run = vfour_portal_run.Vfour_Portal_Run(self.driver)
        project_id=utillobj.parseinitfile('project_id')
        suite_id=utillobj.parseinitfile('suite_id')
        folder_path=project_id+'->'+suite_id
        BIP_Portal_Path = folder_path+'->BIP_V4_Portal'
        
        """ Step 1: Sign into WebFOCUS home page as Developer User
                    Navigate URL to http://environment_name:port/alias/legacyhome
        """
        utillobj.invoke_legacyhomepage('mrid03', 'mrpass03')
        parent_css = "#PortalResourcevBOX table tr td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, resultobj.home_page_long_timesleep)
        
        """ Step 2: Open P292->S10117 from Domains tree,
                    Right click on 'BIP_Responsive' portal and choose Change Title
        """
        wf_mainpageobj.change_repository_elem_title(BIP_Portal_Path+'->BIP_Responsive', 'Change Title', 'testing change title')
        utillobj.synchronize_with_visble_text('#PortalResourcevBOX table', 'testing change title', resultobj.home_page_long_timesleep)
         
        """ Step 3: Change the title to "testing change title"
                    Verify that the title has been changed.
        """
        wf_mainpageobj.verify_repositery_item(BIP_Portal_Path,'testing change title', msg='03.00')
         
        """ Step 4: Right Click on Accordion report and choose Change title
                    Enter title as "Accordion_change_title"
                    Verify that the title has been changed.
        """
        wf_mainpageobj.change_repository_elem_title(BIP_Portal_Path+'->Accordion report', 'Change Title', 'Accordion_change_title')
        utillobj.synchronize_with_visble_text('#PortalResourcevBOX table', 'Accordion_change_title', resultobj.home_page_long_timesleep)
        wf_mainpageobj.verify_repositery_item(BIP_Portal_Path,'testing change title', msg='04.00')
         
        """ Step 5: Right click on the IA_Chart1_1 and choose properties
                    Change the title there and click OK
                    Verify that the title has been changed.
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->IA_Chart1_1', 'Properties')
        time.sleep(2)
        wf_mainpageobj.edit_properties_dialog('Main Properties', 'textbox', 'Title', textbox_input='IA_Chart1_1_1')
        wf_mainpageobj.edit_properties_dialog('Main Properties', 'button', 'OK')
        time.sleep(2)
        wf_mainpageobj.verify_repositery_item(BIP_Portal_Path,'IA_Chart1_1_1', msg='05.00')
         
        """ Step 6: Run the V4 portal "testing change title" located under P292->S10117 .
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->testing change title', 'Run')
        utillobj.wait_for_page_loads(20)
        parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        resultobj.wait_for_property(parent_css, 1, expire_time=resultobj.home_page_long_timesleep)
         
        """ Step 7: Add a new one column page
        """
        portal_canvas.add_page('1 Column',Page_title='Page 5')
         
        """ Step 8: Right click on the page and choose change title
        """
        """ Step 9: Enter testing change page title as title
                    Verify that you get no errors
        """
        portal_canvas.manage_page_menu('Page 5', 'Change Title', change_title='testing change page title')
        portal_canvas.verify_page_in_navigation_bar('testing change page title', "Step 09.00: Verify that you get no errors and page title changed.")
         
        """ Step 10: Click Close
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        
        """ Step 11: Navigate URL to http://environment_name:port/alias/legacyhome
        """
        utillobj.navigate_to_legacyhomepage()
        
        """ Step 12: Open the portal hierarchy on the tree
                     Verify that the title change shows on the portal tree under the portal
        """
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=resultobj.home_page_medium_timesleep, string_value=workspace, with_regular_exprestion=True)
        wf_mainpageobj.verify_repositery_item(BIP_Portal_Path+'->BIP_Responsive Resources','testing change title', msg='12.00')
         
        """ Step 13: Rerun the portal
                     Verify that page is still there and the new title as well.
        """
        wf_mainpageobj.select_repository_menu(BIP_Portal_Path+'->testing change title', 'Run')
        parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        utillobj.wait_for_page_loads(20)
        resultobj.wait_for_property(parent_css, 1, expire_time=resultobj.home_page_long_timesleep)
        portal_canvas.verify_page_in_navigation_bar('testing change page title', "Step 13.00: Verify that page is still there and the new title as well.")
        
        """ Step 14: Right click on the page and choose delete
        """
        portal_canvas.manage_page_menu('testing change page title', 'Delete')
        
        """ Step 15: Click Close
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        
        """ Step 16: In the banner link, click on the top right username > Click Sign Out.
        """
        time.sleep(2)
                

if __name__ == '__main__':
    unittest.main()