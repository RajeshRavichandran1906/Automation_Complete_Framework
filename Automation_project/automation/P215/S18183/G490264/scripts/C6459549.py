'''
Created on 10-Aug-2018

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/18183
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/6459549
TestCase Name = Developer User: Verify Summit Demo Infographic, runtime, edit, save
'''
import unittest,time, keyboard
from common.lib.basetestcase import BaseTestCase
from common.wftools import infographics
from common.lib import utillity
import uiautomation as Automation

class C6459549_TestClass(BaseTestCase):

    def test_C6459549(self):
        driver=self.driver
        infographicObj=infographics.InfoGraphics(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        USER='mrid_dev'
        PASSWRD='mr_pass'
        PROJECT_ID = utillobj.parseinitfile('project_id')
        SUITE_ID = utillobj.parseinitfile('suite_id')
        BROWSER=utillobj.parseinitfile('browser')
        PROJ_FLDR="{0}_{1}".format(PROJECT_ID,SUITE_ID)
        PROJ_SUBFLDR='Summit'
        HOMEPAGECSS=".explore-box .ibfs-tree .home-tree-node .ibx-label-text"
        RUNIMGCSS='body>img'
        EDITCSS='#easelly-frame'
        PAGES=['Peter', 'Marina', 'Stefan', 'Boris', 'Siebe', 'Majase', 'Christian', 'Peter', 'Thomas','Klaus']
        EXPECTD_QRY_LIST=["Participant Count (summitparticipants)", "Sum", "IndustryCounts", "Coordinated", "PID", "Industry Table (summitparticipants)", "First Name (summitparticipants)", "Industry Chart (summitparticipants)", "FocalPoint Badge (summitparticipants)"]
        BRWSR='Chrome'
        
        """    1. Sign in to WebFOCUS as a Basic user - http://machine:port/{alias}/    """
        infographicObj.signin_to_WF_with_user(USER, PASSWRD, HOMEPAGECSS)
        
        """    2. Repository folder: P413_S18040 > Summit, Execute the following URL:
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_LAUNCH&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP413_S18040%252FSummit%252F&BIP_item=summit_demo.fex    """
        infographicObj.run_infographic_using_api_url(PROJ_FLDR, PROJ_SUBFLDR, 'summit_demo', RUNIMGCSS, 10, USER)
                
        """    3. Verify the 10 Infographic images displayed for the following participants:    
                    Peter   Marina  Stefan  Boris   Siebe   Majase  Christian   Peter   Thomas  Klaus    """
        '''Francesca 7/11/18 Note to Automation team: Step 3
            Verify the entire infographic image #1 for participant Peter
            Verify the entire infographic image #10 for participant Klaus
            Verify just the name for participants 2 - 9    '''
        PAGES_obj=driver.find_elements_by_css_selector(RUNIMGCSS)
        infographicObj.scrolled_into_view(PAGES_obj[0])
        utillobj.verify_picture_using_sikuli('page1_top_'+BRWSR.lower()+'.png', "Step 3a.1a: Verify participants - "+PAGES[0]+" top chart")
        # verification of bottom chart fails need to debug
        '''PAGES_obj[0].click()
        for i in range(11):
            keyboard.send('down')
            time.sleep(1)
        utillobj.verify_picture_using_sikuli('page1_bottom'+oBrowser.lower()+'.png', "Step 3a.1b: Verify participants - "+PAGES[0]+" bottom chart")'''
        for i in range(2,10):
            infographicObj.scrolled_into_view(PAGES_obj[i-1])
            time.sleep(2)
            utillobj.verify_picture_using_sikuli('page'+str(i)+'_'+PAGES[i-1].lower()+'_'+BRWSR.lower()+'.png', "Step 3b."+str(i)+": Verify participants - "+PAGES[i-2]+" name")
            time.sleep(1)
        infographicObj.scrolled_into_view(PAGES_obj[9])
        utillobj.verify_picture_using_sikuli('page10_top_'+BRWSR.lower()+'.png', "Step 3c.10a: Verify participants - "+PAGES[9]+" top chart")
        keyboard.send('page down')
        time.sleep(1)
        keyboard.send('page down')
        time.sleep(1)
        utillobj.verify_picture_using_sikuli('page10_bottom_'+BRWSR.lower()+'.png', "Step 3c.10b: Verify participants - "+PAGES[9]+" bottom chart")
        time.sleep(1)
         
        """    4. Repository folder: P413_S18040 > Summit
        Execute the following URL:- http://machine.ibi.com:8080/ibi_apps/ia?item=IBFS:/WFC/Repository/P413_S18040/Summit/summit_demo.fex    """
        infographicObj.restore_infographic_using_api_url(PROJ_FLDR, PROJ_SUBFLDR, 'summit_demo', EDITCSS, 1, USER)
        
        """    5. Verify the Query Pane    """
        infographicObj.verify_all_fields_in_query_pane(EXPECTD_QRY_LIST, "step 05: Verify the Query_Pane")
        
        """    6. Verify the entire Document Canvas (Live Preview)        """
        utillobj.verify_picture_using_sikuli('edit_ig_top_'+BRWSR.lower()+'.png', "Step 06.1: Verify Edit canvas Infographic top chart")
        Automation.MoveTo(1000,500)
        oScroll_times=25 if BROWSER == 'Chrome' else 10
        utillobj.mouse_scroll('down', oScroll_times, option='uiautomation')
        utillobj.verify_picture_using_sikuli('edit_ig_middle1_'+BRWSR.lower()+'.png', "Step 06.2: Verify Edit canvas Infographic middle 1 chart")
        oScroll_times=15 if BROWSER == 'Chrome' else 5
        utillobj.mouse_scroll('down', oScroll_times, option='uiautomation')
        utillobj.verify_picture_using_sikuli('edit_ig_middle2_'+BRWSR.lower()+'.png', "Step 06.3: Verify Edit canvas Infographic millde 2 chart")
        oScroll_times=25 if BROWSER == 'Chrome' else 8
        utillobj.mouse_scroll('down', oScroll_times, option='uiautomation')
        utillobj.verify_picture_using_sikuli('edit_ig_bottom_'+BRWSR.lower()+'.png', "Step 06.4: Verify Edit canvas Infographic bottom chart")
        
        """    7. Click on 'Run' button in the toolbar    """
        infographicObj.run_chart_from_toptoolbar()
        utillobj.switch_to_frame(pause=1)
        utillobj.synchronize_with_number_of_element(RUNIMGCSS, 10, 100)
        
        """    8. Verify the 10 Infographic images displayed for the 10 participants    """
        PAGES_obj=driver.find_elements_by_css_selector(RUNIMGCSS)
        infographicObj.scrolled_into_view(PAGES_obj[0])
        utillobj.verify_picture_using_sikuli('ig_page1_peter_'+BRWSR.lower()+'_top.png', "Step 8a.1a: Verify participants - "+PAGES[0]+" top chart")
        Automation.MoveTo(1000,500)
        utillobj.mouse_scroll('down', 5, option='uiautomation')
        utillobj.verify_picture_using_sikuli('ig_page1_peter_'+BRWSR.lower()+'_middle1.png', "Step 8a.1b: Verify participants - "+PAGES[0]+" middle_1 chart")
        utillobj.mouse_scroll('down', 4, option='uiautomation')
        utillobj.verify_picture_using_sikuli('ig_page1_peter_'+BRWSR.lower()+'_middle2.png', "Step 8a.1c: Verify participants - "+PAGES[0]+" middle_2 chart")
        utillobj.mouse_scroll('down', 4, option='uiautomation')
        utillobj.verify_picture_using_sikuli('ig_page1_peter_'+BRWSR.lower()+'_bottom.png', "Step 8a.1d: Verify participants - "+PAGES[0]+" bottom chart")
        for i in range(2,10):
            infographicObj.scrolled_into_view(PAGES_obj[i-1])
            time.sleep(2)
            utillobj.verify_picture_using_sikuli('page'+str(i)+'_'+PAGES[i-1].lower()+'_'+BRWSR.lower()+'.png', "Step 8b."+str(i)+": Verify participants - "+PAGES[i-2]+" name")
            time.sleep(1)
        infographicObj.scrolled_into_view(PAGES_obj[9])
        utillobj.verify_picture_using_sikuli('ig_page10_klaus_'+BRWSR.lower()+'_top.png', "Step 8c.1a: Verify participants - "+PAGES[9]+" top chart")
        Automation.MoveTo(1000,500)
        utillobj.mouse_scroll('down', 5, option='uiautomation')
        utillobj.verify_picture_using_sikuli('ig_page1_peter_'+BRWSR.lower()+'_middle1.png', "Step 8c.1b: Verify participants - "+PAGES[9]+" middle_1 chart")
        utillobj.mouse_scroll('down', 4, option='uiautomation')
        utillobj.verify_picture_using_sikuli('ig_page1_peter_'+BRWSR.lower()+'_middle2.png', "Step 8c.1c: Verify participants - "+PAGES[9]+" middle_2 chart")
        utillobj.mouse_scroll('down', 4, option='uiautomation')
        utillobj.verify_picture_using_sikuli('ig_page1_peter_'+BRWSR.lower()+'_bottom.png', "Step 8c.1d: Verify participants - "+PAGES[9]+" bottom chart")      
        time.sleep(2)
        utillobj.switch_to_default_content(pause=1)
        
        """    9. Click on 'Save' button in the toolbar > Click OK    """
        infographicObj.select_item_in_top_toolbar('save')
        infographicObj.click_bibutton_in_dialog("div[id^='BiDialog'] div[class=bi-button-label]", "OK")
        
        """    10. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """  
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    11. Repository folder: P413_S18040 > Summit
        Execute the following URL:- http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_LAUNCH&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP413_S18040%252FSummit%252F&BIP_item=summit_demo.fex    """
        infographicObj.signin_to_WF_with_user(USER, PASSWRD, HOMEPAGECSS)
        infographicObj.run_infographic_using_api_url(PROJ_FLDR, PROJ_SUBFLDR, 'summit_demo', RUNIMGCSS, 10, USER)
        
        """    12. Verify the 10 Infographic images displayed for the 10 participants    """
        PAGES_obj=driver.find_elements_by_css_selector(RUNIMGCSS)
        infographicObj.scrolled_into_view(PAGES_obj[0])
        utillobj.verify_picture_using_sikuli('page1_top_'+BRWSR.lower()+'.png', "Step 12a.1a: Verify participants - "+PAGES[0]+" top chart")
        # verification of bottom chart fails need to debug
        '''PAGES_obj[0].click()
        for i in range(11):
            keyboard.send('down')
            time.sleep(1)
        utillobj.verify_picture_using_sikuli('page1_bottom'+oBrowser.lower()+'.png', "Step 12a.1b: Verify participants - "+PAGES[0]+" bottom chart")'''
        for i in range(2,10):
            infographicObj.scrolled_into_view(PAGES_obj[i-1])
            time.sleep(2)
            utillobj.verify_picture_using_sikuli('page'+str(i)+'_'+PAGES[i-1].lower()+'_'+BRWSR.lower()+'.png', "Step 12b."+str(i)+": Verify participants - "+PAGES[i-2]+" name")
            time.sleep(1)
        infographicObj.scrolled_into_view(PAGES_obj[9])
        utillobj.verify_picture_using_sikuli('page10_top_'+BRWSR.lower()+'.png', "Step 12c.10a: Verify participants - "+PAGES[9]+" top chart")
        keyboard.send('page down')
        time.sleep(1)
        keyboard.send('page down')
        time.sleep(1)
        utillobj.verify_picture_using_sikuli('page10_bottom_'+BRWSR.lower()+'.png', "Step 12c.10b: Verify participants - "+PAGES[9]+" bottom chart")
        time.sleep(1)
       
        """    13. Repository folder: P413_S18040 > Summit
        Execute the following URL: http://machine.ibi.com:8080/ibi_apps/ia?item=IBFS:/WFC/Repository/P413_S18040/Summit/summit_demo.fex    """
        infographicObj.restore_infographic_using_api_url(PROJ_FLDR, PROJ_SUBFLDR, 'summit_demo', EDITCSS, 1, USER)
        
        """    14. Verify the Query Pane    """
        infographicObj.verify_all_fields_in_query_pane(EXPECTD_QRY_LIST, "step 14: Verify the Query_Pane")
        
        """    15. Verify the entire Document Canvas (Live Preview)        """
        utillobj.verify_picture_using_sikuli('edit_ig_top_'+BRWSR.lower()+'.png', "Step 15.1: Verify Edit canvas Infographic top chart")
        Automation.MoveTo(1000,500)
        oScroll_times=25 if BROWSER == 'Chrome' else 10
        utillobj.mouse_scroll('down', oScroll_times, option='uiautomation')
        utillobj.verify_picture_using_sikuli('edit_ig_middle1_'+BRWSR.lower()+'.png', "Step 15.2: Verify Edit canvas Infographic middle 1 chart")
        oScroll_times=15 if BROWSER == 'Chrome' else 5
        utillobj.mouse_scroll('down', oScroll_times, option='uiautomation')
        utillobj.verify_picture_using_sikuli('edit_ig_middle2_'+BRWSR.lower()+'.png', "Step 15.3: Verify Edit canvas Infographic millde 2 chart")
        oScroll_times=25 if BROWSER == 'Chrome' else 8
        utillobj.mouse_scroll('down', oScroll_times, option='uiautomation')
        utillobj.verify_picture_using_sikuli('edit_ig_bottom_'+BRWSR.lower()+'.png', "Step 15.4: Verify Edit canvas Infographic bottom chart")
        
        """    16. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()
