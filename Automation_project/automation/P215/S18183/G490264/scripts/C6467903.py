'''
Created on 14-Aug-2018
@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/18183
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/6467903
TestCase Name = Verify United Way infographic after updating template with latest Easel.ly version, format PNG
'''

import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.wftools import infographics
from common.lib import utillity
import uiautomation as Automation

class C6467903_TestClass(BaseTestCase):
    def test_C6467903(self):
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
        EXPECTD_QRY_LIST=["Number here (wf_retail_lite)", "Sum", "Sale Unit(s)", "Coordinated", "9of10 (wf_retail_lite)", "Invested (wf_retail_lite)", "IB chart (wf_retail_lite)", "Left (wf_retail_lite)", "Right (wf_retail_lite)", "Center (wf_retail_lite)"]
        BRWSR='Chrome'
        
        """    1. Sign in to WebFOCUS as a Developer user - http://machine:port/{alias}/    """
        infographicObj.signin_to_WF_with_user(USER, PASSWRD, HOMEPAGECSS)
               
        """    2. Repository folder: P413_S18040 > InfoGraphics 
        Execute the following URL:
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_LAUNCH&BIP_folder=IBFS%253A%252FWFC%252FReposiory%252FP413_S18040%252FSummit%252F&BIP_item=united_way.fex    """
        infographicObj.run_infographic_using_api_url(PROJ_FLDR, PROJ_SUBFLDR, 'united_way', RUNIMGCSS, 10, USER)
        
        """    3. Verify the entire Infographic image    """
        utillobj.verify_picture_using_sikuli('ig_united_way_run_'+BRWSR.lower()+'.png', "Step 03(a): Verify entire infographic image")
        
        """    4. Close the output window    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        infographicObj.signin_to_WF_with_user(USER, PASSWRD, HOMEPAGECSS)
        
        """    5. Repository folder: P413_S18040 > InfoGraphics
        Execute the following URL:
        http://machine.ibi.com:8080/ibi_apps/ia?item=IBFS:/WFC/Repository/P413_S18040/Summit/united_way.fex    """
        infographicObj.restore_infographic_using_api_url(PROJ_FLDR, PROJ_SUBFLDR, 'united_way', EDITCSS, 1, USER)        
        
        """    6. Verify all components in the Query pane    """
        infographicObj.verify_all_fields_in_query_pane(EXPECTD_QRY_LIST, "step 06: Verify the Query_Pane")
        
        """    7. Verify the entire Live Preview Canvas    """
        Automation.MoveTo(1000,500)
        oScroll_times=4 if BROWSER == 'Chrome' else 1
        utillobj.mouse_scroll('down', oScroll_times, option='uiautomation')
        utillobj.verify_picture_using_sikuli('ig_united_way_livepreview_'+BRWSR.lower()+'.png', "Step 06(a): Verify Edit canvas Infographic live preview canvas")
        
        """    8. Click on "Save" button in the toolbar > Click OK    """
        infographicObj.select_item_in_top_toolbar('save')
        infographicObj.click_bibutton_in_dialog("div[id^='BiDialog'] div[class=bi-button-label]", "OK")
        
        """    9. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    10. Repository folder: P413_S18040 > InfoGraphics
        Execute the following URL: (with updated IA syntax)
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_LAUNCH&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP413_S18040%252FSummit%252F&BIP_item=united_way.fex    """
        infographicObj.signin_to_WF_with_user(USER, PASSWRD, HOMEPAGECSS)
        infographicObj.run_infographic_using_api_url(PROJ_FLDR, PROJ_SUBFLDR, 'united_way', RUNIMGCSS, 10, USER)
        
        """    11. Verify the entire Infographic image    """
        utillobj.verify_picture_using_sikuli('ig_united_way_run_'+BRWSR.lower()+'.png', "Step 11(a): Verify entire infographic image")
        
        """    12. Close the output window    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    13. Repository folder: P413_S18040 > InfoGraphics
        Execute the following URL: (Verifying restore)
        http://machine.ibi.com:8080/ibi_apps/ia?item=IBFS:/WFC/Repository/P413_S18040/InfoGraphics/united_way.fex    """
        infographicObj.signin_to_WF_with_user(USER, PASSWRD, HOMEPAGECSS)
        infographicObj.restore_infographic_using_api_url(PROJ_FLDR, PROJ_SUBFLDR, 'united_way', EDITCSS, 1, USER) 
        
        """    14. Verify the entire Live Preview Canvas    """
        Automation.MoveTo(1000,500)
        oScroll_times=4 if BROWSER == 'Chrome' else 1
        utillobj.mouse_scroll('down', oScroll_times, option='uiautomation')
        utillobj.verify_picture_using_sikuli('ig_united_way_livepreview_'+BRWSR.lower()+'.png', "Step 14(a): Verify Edit canvas Infographic live preview canvas")
        
        """    15. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()
