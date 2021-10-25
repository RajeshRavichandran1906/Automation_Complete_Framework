'''
Created on Dec 14, 2017

@author: Pavithra 

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10660&group_by=cases:section_id&group_order=asc
TestCase ID : http://172.19.2.180/testrail/index.php?/cases/view/2270315
TestCase Name : API > BIP > Open an existing Reporting Object to report from
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, wf_legacymainpage,vfour_portal_canvas, vfour_portal_ribbon,vfour_miscelaneous,wf_reporting_object
from common.lib import utillity

class C2270315_TestClass(BaseTestCase):

    def test_C2270315(self):
        
        
        """
            TESTCASE VARIABLES
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(driver)
        wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(driver)
        portal_canvas = vfour_portal_canvas.Vfour_Portal_Canvas(driver)
        portal_ribbon = vfour_portal_ribbon.Vfour_Portal_Ribbon(driver)
        vfourmisobj = vfour_miscelaneous.Vfour_Miscelaneous(driver)
        wfreporting =wf_reporting_object.Wf_Reporting_Object(driver)
        """
            Step 01:Launch WebFOCUS using API,
            http://machine:port/ibi_apps
        """
        utillobj.invoke_webfocu('mrid', 'mrpass')
        parent_css = "#topBannerMenuBox [id^='SignonBannerPanelToolsMenuBtn']"
        result_obj.wait_for_property(parent_css, 1, expire_time=20, string_value="Tools", with_regular_exprestion=True)
        """
            Step 02:Right-click Domains folder (ex:S10032) > New > URL
        """
        wf_mainpageobj.select_repository_menu("P292->S10032_infoassist_5", "New->URL")
        
        """     
            Step 03:Type Title: Open an existing Reporting Object to report from
            
            Step 04:Type URL (with test environment) using API:
            http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2241559.fex&tool=reportingobject > OK
        """
        node = utillobj.parseinitfile('nodeid')
        port = utillobj.parseinitfile('httpport')
        context = utillobj.parseinitfile('wfcontext')
        setup_url = 'http://' + node + ':' + port + context + '/ia?item=IBFS%3A%2FWFC%2FRepository%2FP292%2FS10032_infoassist_5%2FC2241559.fex&tool=Report'
        wf_mainpageobj.create_url(setup_url, url_title='Open an existing Reporting Object to report from', ok_btn=True)
        
        """
            Step 05:Create New > Collaborative Portal
            
            Step 06:Type Title: C2270315
            Verify that Add Page dialog opens,
        """
        wf_mainpageobj.create_portal("P292->S10032_infoassist_5", "C2270315")
        utillobj.switch_to_window(1, pause=2)        
        parent_css ="#dlgTitleExplorer[style*='inherit'] [class*='active'] [class*='caption'] [class*='bi-label']"
        result_obj.wait_for_property(parent_css, 1, expire_time=20)
        parent_css= "#dlgTitleExplorer[style*='inherit'] [class*='active'] [class*='caption'] [class*='bi-label']"
        utillobj.verify_popup("#dlgTitleExplorer", "Step 03:02 : Verify that the Page Templates dialog showed.", caption_css=parent_css, caption_text='Add Page')
        """
            Step 07:Select 'One Column' > Create
        """
        vfourmisobj.select_page_template(page_template="1 Column", btn_name="Create")
        time.sleep(5)
        """     
            Step 08:Select Insert tab > WebFOCUS Resources
            Verify that WebFOCUS Resources added,
        """
        portal_ribbon.select_ribbon_item('Insert', 'Insert_WebFOCUSResources')
        time.sleep(5)
        """
            Step 09:Expand the folder "S10032" > Drag "Open an existing Reporting Object to report from" into Portal
            Verify the Portal,
        """
        portal_canvas.dragdrop_repository_item_to_canvas('P292->S10032_infoassist_5->Open an existing Reporting Object to report from', 'column', 1)
        time.sleep(8)
        portal_canvas.verify_column_panel_caption(1, 'Open an existing Reporting Object to report from', "Step 09.1: Verify first panel title")        
        utillobj.switch_to_frame(pause=2,frame_css="[class*='bi-iframe iframe '][name^='Panel']",frame_height_value=0)
        time.sleep(8)
        ro_tool_name=['Reporting Object', 'Preprocessing Other', 'Joins', 'Defines', 'Filters', 'Where Statements', 'Report', 'Chart', 'Postprocessing Other']
        wfreporting.verify_ro_tree_item(ro_tool_name,"Step 09.2: Verify the existing Reporting Object opens")
        
        """
            Step 10:Select BIP > Exit > Yes to save prompt > OK
        """
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
        portal_ribbon.select_tool_menu_item('menu_Exit')
        time.sleep(5)
        utillobj.verify_object_visible('#dlgSavepromptPortal', True, "Step 10: Verify save prompt appears")
        yes_btn=driver.find_element_by_css_selector("#dlgSavepromptPortal div[id*='yesDialogbtnAction']")
        utillobj.default_left_click(object_locator=yes_btn)
        ok_btn=driver.find_element_by_css_selector("#dlgPortalSaveDialog div[id*='BiButton'][ class^='bi-button button button-focus']")
        utillobj.default_left_click(object_locator=ok_btn)
        time.sleep(3)
        """     
            Step 11:Right click on saved portal "C2270315" > Run
            Verify IA is launched,
        """
        time.sleep(3)
        utillobj.switch_to_window(0)
        time.sleep(5)
        parent_css = "#topBannerMenuBox [id^='BiWelcomeBannerMenuButton']"
        result_obj.wait_for_property(parent_css, 1, expire_time=15)
        wf_mainpageobj.select_repository_menu('P292->S10032_infoassist_5->C2270315', 'Run')
        time.sleep(6)
        portal_canvas.verify_column_panel_caption(1, 'Open an existing Reporting Object to report from', "Step 11.1: Verify first panel title")        
        utillobj.switch_to_frame(pause=2,frame_css="[class*='bi-iframe iframe '][name^='Panel']",frame_height_value=0)
        time.sleep(8)
        ro_tool_name=['Reporting Object', 'Preprocessing Other', 'Joins', 'Defines', 'Filters', 'Where Statements', 'Report', 'Chart', 'Postprocessing Other']
        wfreporting.verify_ro_tree_item(ro_tool_name,"Step 11.2: Verify the existing Reporting Object opens") 
        
        """
            Step 12:Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(5)
        
if __name__ == "__main__":
    unittest.main()