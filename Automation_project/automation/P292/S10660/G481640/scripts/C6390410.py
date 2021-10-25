'''
Created on June 28, 2018

@author: Magesh 

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10660&group_by=cases:section_id&group_order=asc
TestCase ID : http://172.19.2.180/testrail/index.php?/cases/view/6390410
TestCase Name : API > BIP > Launch IA to edit an existing report (fex)
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea,wf_legacymainpage,vfour_miscelaneous,vfour_portal_ribbon,vfour_portal_canvas, vfour_portal_run, ia_resultarea
from common.lib import utillity, core_utility

class C6390410_TestClass(BaseTestCase):

    def test_C6390410(self):
        
        """   
                TESTCASE VARIABLES 
        """
        Test_Case_ID = 'C6390410'
        utillobj = utillity.UtillityMethods(self.driver)
        core_utilobj = core_utility.CoreUtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        vfour_mis=vfour_miscelaneous.Vfour_Miscelaneous(self.driver)
        vfour_ribbon=vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        vfour_canvas=vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        vfour_run=vfour_portal_run.Vfour_Portal_Run(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        homepage=wf_legacymainpage.Wf_Legacymainpage(self.driver)
        
        """
           Step 01 : Launch WebFOCUS using API, http://machine:port/ibi_apps
        """
        utillobj.invoke_legacyhomepage('mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#topBannerMenuBox [id^='SignonBannerPanelToolsMenuBtn']", 'Tools', resultobj.chart_long_timesleep)
        node=utillobj.parseinitfile('nodeid')
        port=utillobj.parseinitfile('httpport')
        context=utillobj.parseinitfile('wfcontext')
        folder=utillobj.parseinitfile('suite_id')
        project_id=utillobj.parseinitfile('project_id')
        br = utillobj.get_browser_height() # Some time browser height not update correctly in login page method. 
        utillity.UtillityMethods.browser_x = br['browser_width']
        utillity.UtillityMethods.browser_y = br['browser_height']
        
        """
            Step 02 : Right-click Domains folder (ex:"P292_S10032_G157398 (Folder Name is P292 - Remain as is due to HTML pages)" > S10032_infoassist_5 folder) > New > URL
        """
        homepage.select_repository_menu(project_id+'_S10032_G157398 (Folder Name is P292 - Remain as is due to HTML pages)->'+folder,'New->URL')
          
        """
            Step 03 : Type Title: Launch IA to edit an existing report
            Step 04 : Type URL (with test environment) using API:
            http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2241552_base.fex&tool=Report > OK
        """
        setup_url = 'http://' + node + ':' + port + context + '/ia?item=IBFS:/WFC/Repository/'+project_id+'/S10032_infoassist_5/C2241552_base.fex&tool=Report'
        homepage.create_url(setup_url, url_title='Launch IA to edit an existing report', ok_btn=True)
        utillobj.synchronize_until_element_disappear('#btnOK', resultobj.home_page_medium_timesleep)
         
        """
            Step 05 : Create New > Collaborative Portal
            Step 06 : Type Title: C6390410
        """
        homepage.create_portal(project_id+'_S10032_G157398 (Folder Name is P292 - Remain as is due to HTML pages)->'+folder,Test_Case_ID)
        core_utilobj.switch_to_new_window()
        parent_css = "#applicationButtonBox img[src*='bip_button']"
        utillobj.synchronize_until_element_is_visible(parent_css, resultobj.home_page_long_timesleep)
        vfour_mis.verify_page_template("Step 06.00: Verify when Portal Designer loads you are on the Layout tab", page_template="1 Column")
         
        """
            Step 07 : Select 'One Column' > Create
        """
        vfour_mis.select_page_template(page_template="1 Column", Page_title="1 Column", btn_name="Create")
        time.sleep(5)
         
        """
            Step 08 : Select Insert tab > WebFOCUS Resources
        """
        vfour_ribbon.select_ribbon_item('Insert', 'Insert_WebFOCUSResources')
        time.sleep(2)
         
        """
            Step 09 : Expand the folder ""P292_S10032_G157398 (Folder Name is P292 - Remain as is due to HTML pages)" > S10032_infoassist_5 folder" > Drag "Launch IA to edit an existing report" into Portal
        """
        item_path=project_id+'_S10032_G157398 (Folder Name is P292 - Remain as is due to HTML pages)->'+folder+'->Launch IA to edit an existing report'
        vfour_canvas.dragdrop_repository_item_to_canvas(item_path,'column',1)
        time.sleep(2)
        vfour_canvas.verify_panel_caption('Launch IA to edit an existing report', "Step 09.00: Verify Launch IA to edit an existing report.")
        ''' Verification check points.    '''
        utillobj.switch_to_frame(pause=2,frame_css="[class*='iframe'][name='Panel_1_1']",frame_height_value=0)
        parent_css="#TableChart_1 div[class^='x']"
        resultobj.wait_for_property(parent_css, 18, expire_time=90)
        time.sleep(15)
        ia_resultobj.verify_across_report_data_set('TableChart_1', 1,2,8,2,'C6390410_DataSet_01.xlsx', 'Step 09.01 : Verify Report Dataset.')
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)
         
        """ Step 10: Select BIP > Exit > Yes to save prompt > OK
        """
        vfour_ribbon.bip_save_and_exit(btn_name='Yes')
        core_utilobj.switch_to_previous_window(window_close=False)
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value="Workspaces", with_regular_exprestion=True)
        time.sleep(1)
        
        """ Step 11: Right click on saved portal "C6390410" > Run
                     Verify IA is launched,
        """
        homepage.select_repository_menu(project_id+'_S10032_G157398 (Folder Name is P292 - Remain as is due to HTML pages)->'+folder+'->'+Test_Case_ID, 'Run')
        parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        resultobj.wait_for_property(parent_css, 1, expire_time=190)
        time.sleep(2)
        vfour_canvas.verify_panel_caption('Launch IA to edit an existing report', "Step 11.00: Verify Launch IA to edit an existing report.")
        
        ''' Verification check points.    '''
        utillobj.switch_to_frame(pause=2,frame_css="[class*='iframe'][name='Panel_1_1']",frame_height_value=0)
        parent_css="#TableChart_1 div[class^='x']"
        resultobj.wait_for_property(parent_css, 18, expire_time=90)
        time.sleep(15)
        ia_resultobj.verify_across_report_data_set('TableChart_1', 1,2,8,2,'C6390410_DataSet_01.xlsx', 'Step 11.01: Verify Report Dataset.')
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)
        vfour_run.select_or_verify_portal_menu_bar_item(select='Close')
                
        """ Step 12: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()        
        