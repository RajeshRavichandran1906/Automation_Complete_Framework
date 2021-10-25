'''
Created on 15-Nov-2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324267
TestCase Name = Properties testing : Change Name
'''
import unittest, time
from common.lib import utillity
from common.pages import visualization_resultarea, vfour_portal_canvas, wf_legacymainpage, vfour_portal_run
from common.lib.basetestcase import BaseTestCase

class C2324267_TestClass(BaseTestCase):

    def test_C2324267(self):
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
        
        """
        Step 1: Sign into WebFOCUS home page as Developer User
        Navigate URL to http://environment_name:port/alias/legacyhome
        """
        utillobj.invoke_legacyhomepage('mrid03', 'mrpass03')
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=resultobj.home_page_long_timesleep, string_value=workspace, with_regular_exprestion=True)
        
        """ Step 2: Right Click on the Domains node and choose View By Name
        """
        wf_mainpageobj.select_menu(workspace, 'View->Display By Name')
        
        """ Step 3: Open P292 -> S10117 from domains tree,
                    Right click on 'Portal_within.prtl' and choose Change Name
        """
        """ Step 4: Change the title as "testing change name"
                    Verify that you get an error message stating that you have illegal characters
        """
        wf_mainpageobj.change_repository_elem_title(folder_path+'->BIP_V4_Portal->Portal_within.prtl', 'Change Name', 'testing change name')
        time.sleep(2)
        css = "[id*='BiDialog'] [class*='active']"
        cap_css = css + " [class*='caption']"
        cap_txt = 'Message'
        pop_css = css + " [id*='BiOptionPane']"
        pop_txt="'testing change name' contains invalid characters.\nOK"
        utillobj.verify_popup(css,'Step 04.00: Verify that you get an error message stating that you have illegal characters',caption_css=cap_css,caption_text=cap_txt,popup_text_css=pop_css,popup_text=pop_txt)
        utillobj.click_dialog_button(pop_css, 'OK')
        
        """ Step 5: Change the title as "testing_change_name"
                    Verify that the name has changed.
        """
        wf_mainpageobj.change_repository_elem_title(folder_path+'->BIP_V4_Portal->Portal_within.prtl', 'Change Name', 'testing_change_name')
        time.sleep(2)
        wf_mainpageobj.verify_repositery_item(folder_path+'->BIP_V4_Portal','testing_change_name.prtl', msg='05.00')
        
        """ Step 6: Run the portal and make sure all is well
                    Close the portal run
        """
        wf_mainpageobj.select_repository_menu(folder_path+'->BIP_V4_Portal->testing_change_name.prtl', 'Run')
        parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        resultobj.wait_for_property(parent_css, 1, expire_time=resultobj.home_page_long_timesleep)
        portal_canvas.select_page_in_navigation_bar('Page 1')
        time.sleep(2)
        portal_canvas.verify_page_in_navigation_bar('Page 1', "Step 06.00: Verify portal opened without any error.")
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        
        """ Step 7:Navigate URL to http://environment_name:port/alias/legacyhome """
        
        utillobj.navigate_to_legacyhomepage()
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=resultobj.home_page_long_timesleep, string_value=workspace, with_regular_exprestion=True)
        
        """ Step 8: Right Click on tagCloud chart and choose Change name
                    Enter title as tagCloud_change_name
                    Verify that the name has been changed.
        """
        wf_mainpageobj.change_repository_elem_title(folder_path+'->BIP_V4_Portal->tagCloud_chart.fex', 'Change Name', 'tagCloud_change_name')
        time.sleep(2)
        wf_mainpageobj.verify_repositery_item(folder_path+'->BIP_V4_Portal','tagCloud_change_name.fex', msg='08.00')
        
        """ Step 9: Right click on the IA_Chart1 and choose properties
                    Check the box for change name
                    Change the title there and click OK
                    Verify the change
        """
        time.sleep(2)
        wf_mainpageobj.select_menu(folder_path+'->BIP_V4_Portal->IA_Chart1_1.fex', 'Properties')
        time.sleep(2)
        wf_mainpageobj.edit_properties_dialog('Main Properties', 'textbox', 'File Name', textbox_input='IA_Chart1_1_1')
        wf_mainpageobj.edit_properties_dialog('Main Properties', 'button', 'OK')
        time.sleep(2)
        wf_mainpageobj.verify_repositery_item(folder_path+'->BIP_V4_Portal','IA_Chart1_1_1.fex', msg='09.00')
        time.sleep(1)
        
        """ Step 10: Right Click on the Content node and choose View by title
        """
        wf_mainpageobj.select_menu(workspace, 'View->Display By Title')
        
        """ Step 11: Sign Out from WebFOCUS
        """
        time.sleep(5)
                

if __name__ == '__main__':
    unittest.main()