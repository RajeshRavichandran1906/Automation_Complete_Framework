'''
Created on 19-Dec-2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2270316
TestCase Name = API > BIP > Launch IA to edit an existing report (fex)
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea,wf_legacymainpage,vfour_miscelaneous,vfour_portal_ribbon,vfour_portal_canvas, vfour_portal_run, ia_resultarea
from common.lib import utillity

class C2270316_TestClass(BaseTestCase):

    def test_C2270316(self):
        
        """   
                TESTCASE VARIABLES 
        """
        Test_Case_ID = 'C2270316'
        utillobj = utillity.UtillityMethods(self.driver)
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
        utillobj.invoke_webfocu('mrid', 'mrpass')
        resultobj.wait_for_property("#topBannerMenuBox [id^='SignonBannerPanelToolsMenuBtn']", 1, expire_time=20, string_value="Tools")
        node=utillobj.parseinitfile('nodeid')
        port=utillobj.parseinitfile('httpport')
        context=utillobj.parseinitfile('wfcontext')
        folder=utillobj.parseinitfile('suite_id')
        project_id=utillobj.parseinitfile('project_id')
         
        """
            Step 02 : Right-click Domains folder (ex:S10032) > New > URL
        """
        homepage.select_repository_menu(project_id+'->'+folder,'New->URL')
         
        """
            Step 03 : Type Title: Launch IA to edit an existing report
            Step 04 : Type URL (with test environment) using API:
            http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2241552.fex&tool=Report > OK
        """
        setup_url = 'http://' + node + ':' + port + context + '/ia?item=IBFS:/WFC/Repository/'+project_id+'/'+folder+'/C2241552.fex&tool=Report'
        homepage.create_url(setup_url, url_title='Launch IA to edit an existing report', ok_btn=True)
        print(setup_url)
         
        """
            Step 05 : Create New > Collaborative Portal
            Step 06 : Type Title: C2270316
        """
        homepage.create_portal(project_id+'->'+folder,Test_Case_ID)
        run_loop = True
        count_time=0
        while run_loop:
            if count_time == 25:
                run_loop = False
            if len(self.driver.window_handles) > 1:
                run_loop = False
            count_time += 1
        utillobj.switch_to_window(1)
        parent_css = "#applicationButtonBox img[src*='bip_button']"
        resultobj.wait_for_property(parent_css, 1, expire_time=50)
        vfour_mis.verify_page_template("Step 6: Verify when Portal Designer loads you are on the Layout tab", page_template="1 Column")
         
        """
            Step 07 : Select 'One Column' > Create
        """
        vfour_mis.select_page_template(page_template="1 Column",btn_name="Create")
        time.sleep(3)
         
        """
            Step 08 : Select Insert tab > WebFOCUS Resources
        """
        vfour_ribbon.invoke_and_verify_wf_resource_tree()
        time.sleep(2)
         
        """
            Step 09 : Expand the folder "S10032" > Drag "Launch IA to edit an existing report" into Portal
        """
        item_path=project_id+'->'+folder+'->Launch IA to edit an existing report'
        vfour_canvas.dragdrop_repository_item_to_canvas(item_path,'column',1)
        time.sleep(2)
        vfour_canvas.verify_panel_caption('Launch IA to edit an existing report', "Step 9: Verify Launch IA to edit an existing report.")
        ''' Verification check points.    '''
        utillobj.switch_to_frame(pause=2,frame_css="[class*='iframe'][name='Panel_1_1']",frame_height_value=0)
        parent_css="#TableChart_1 div[class^='x']"
        resultobj.wait_for_property(parent_css, 18, expire_time=50)
        time.sleep(15)
        ia_resultobj.verify_across_report_data_set('TableChart_1', 1,2,8,2,'C2241552_DataSet_01.xlsx', 'Step 9.1 : Verify Report Dataset.')
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)
         
        """ Step 10: Select BIP > Exit > Yes to save prompt > OK
        """
        vfour_ribbon.bip_save_and_exit(btn_name='Yes')
        utillobj.switch_to_window(0, pause=5)
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value="Domains", with_regular_exprestion=True)
        time.sleep(1)
        
        """ Step 11: Right click on saved portal "C2270316" > Run
                     Verify IA is launched,
        """
        homepage.select_repository_menu(project_id+'->'+folder+'->'+Test_Case_ID, 'Run')
        parent_css="div[id^='BipNavigatorTop'] div[id^='BipNavigatorButton'][class*='checked']"
        resultobj.wait_for_property(parent_css, 1, expire_time=50)
        time.sleep(2)
        vfour_canvas.verify_panel_caption('Launch IA to edit an existing report', "Step 11: Verify Launch IA to edit an existing report.")
        ''' Verification check points.    '''
        utillobj.switch_to_frame(pause=2,frame_css="[class*='iframe'][name='Panel_1_1']",frame_height_value=0)
        parent_css="#TableChart_1 div[class^='x']"
        resultobj.wait_for_property(parent_css, 18, expire_time=50)
        time.sleep(15)
        ia_resultobj.verify_across_report_data_set('TableChart_1', 1,2,8,2,'C2241552_DataSet_01.xlsx', 'Step 11.1 : Verify Report Dataset.')
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)
        vfour_run.select_or_verify_portal_menu_bar_item(select='Close')
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value="Domains", with_regular_exprestion=True)
        
        """ Step 12: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()        
        