'''
Created on 16-Aug-2018
@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/18183
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/6667875
TestCase Name = Verify United Way infographic after updating template with latest Easel.ly version, format PNG
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.wftools import infographics
from common.lib import utillity
import uiautomation as Automation

class C6667875_TestClass(BaseTestCase):
    def test_C6667875(self):
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
        RUNIMGCSS='body>embed'
        EDITCSS='#easelly-frame'
        EXPECTD_QRY_LIST=["Number here (wf_retail_lite)", "Sum", "Sale Unit(s)", "Coordinated", "9of10 (wf_retail_lite)", "Invested (wf_retail_lite)", "IB chart (wf_retail_lite)", "Left (wf_retail_lite)", "Right (wf_retail_lite)", "Center (wf_retail_lite)"]
        BRWSR='Chrome'
        
        """    1. Sign in to WebFOCUS as a Developer user- http://machine:port/{alias}/    """
        infographicObj.signin_to_WF_with_user(USER, PASSWRD, HOMEPAGECSS)
        
        """    2. Repository folder: P413_S18040 > Summit, Execute the following URL:
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_LAUNCH&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP413_S18040%252FSummit%252F&BIP_item=united_way_pdf.fex    """
        infographicObj.run_infographic_using_api_url(PROJ_FLDR, PROJ_SUBFLDR, 'united_way_pdf', RUNIMGCSS, 10, USER)
        
        """    3. Verify the entire Infographic image    """
        if BROWSER == 'Chrome':
            utillobj.verify_picture_using_sikuli('edit_ig_united_way_pdf_run_'+BRWSR.lower()+'_top.png', "Step 03(a): Verify United way infographic top chart")
            utillobj.verify_picture_using_sikuli('edit_ig_united_way_pdf_run_'+BRWSR.lower()+'_bottom.png', "Step 03(b): Verify United way infographic bottom chart")
        else:
            utillobj.verify_picture_using_sikuli('ig_united_way_pdf_run_'+BROWSER.lower()+'.png', "Step 03(a): Verify United way infographic pdf chart")
        
        """    4. Close the output window    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    5. Repository folder: P413_S18040 > Summit, Execute the following URL:
        http://machine.ibi.com:8080/ibi_apps/ia?item=IBFS:/WFC/Repository/P413_S18040/Summit/united_way_pdf.fex    """
        infographicObj.signin_to_WF_with_user(USER, PASSWRD, HOMEPAGECSS)
        infographicObj.restore_infographic_using_api_url(PROJ_FLDR, PROJ_SUBFLDR, 'united_way_pdf', EDITCSS, 1, USER)
        
        """    6. Verify output format is set to "PDF"    """
        utillobj.verify_element_visiblty(element_css="#HomeInfoGraphicPDFButton[class*='checked']", msg="Step 06(a):Verify output format remains set to 'PDF'")
        
        """    7. Verify all components in the Query pane    """
        infographicObj.verify_all_fields_in_query_pane(EXPECTD_QRY_LIST, "step 07: Verify the Query_Pane")
        
        """    8. Verify the entire Live Preview Canvas    """
        Automation.MoveTo(1000,500)
        oScroll_times=4 if BROWSER == 'Chrome' else 1
        utillobj.mouse_scroll('down', oScroll_times, option='uiautomation')
        utillobj.verify_picture_using_sikuli('ig_united_way_pdf_livepreview_'+BRWSR.lower()+'.png', "Step 08(a): Verify Edit canvas Infographic live preview canvas")
        
        """    9. Click on "Save" button in the toolbar > Click OK    """
        infographicObj.select_item_in_top_toolbar('save')
        infographicObj.click_bibutton_in_dialog("div[id^='BiDialog'] div[class=bi-button-label]", "OK")
        
        """    10. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    11. Repository folder: P413_S18040 > Summit, Execute the following URL:
        http://machine.ibi.com:8080/ibi_apps/ia?item=IBFS:/WFC/Repository/P413_S18040/Summit/united_way_pdf.fex    """
        infographicObj.signin_to_WF_with_user(USER, PASSWRD, HOMEPAGECSS)
        infographicObj.restore_infographic_using_api_url(PROJ_FLDR, PROJ_SUBFLDR, 'united_way_pdf', EDITCSS, 1, USER)
        
        """    12. Verify output format remains set to "PDF"    """
        utillobj.verify_element_visiblty(element_css="#HomeInfoGraphicPDFButton[class*='checked']", msg="Step 12(a):Verify output format remains set to 'PDF'")
        
        """    13. Verify all components in the Query panel    """
        infographicObj.verify_all_fields_in_query_pane(EXPECTD_QRY_LIST, "step 13: Verify the Query_Pane")
        
        """    14. Verify the entire Live Preview Canvas    """
        Automation.MoveTo(1000,500)
        oScroll_times=4 if BROWSER == 'Chrome' else 1
        utillobj.mouse_scroll('down', oScroll_times, option='uiautomation')
        utillobj.verify_picture_using_sikuli('ig_united_way_pdf_livepreview_'+BRWSR.lower()+'.png', "Step 14(a): Verify Edit canvas Infographic live preview canvas")
        
        """    15. Click on "Run" button in the toolbar    """
        infographicObj.run_chart_from_toptoolbar()
        utillobj.switch_to_frame(pause=1)
        utillobj.synchronize_with_number_of_element(RUNIMGCSS, 1, 100)
        
        """    16. Verify the entire Infographic image    """
        if BROWSER == 'Chrome':
            utillobj.verify_picture_using_sikuli('edit_ig_united_way_pdf_run_'+BRWSR.lower()+'_top.png', "Step 16(a): Verify United way infographic top chart")
            Automation.MoveTo(1000,500)
            utillobj.mouse_scroll('down', 10, option='uiautomation')
            utillobj.verify_picture_using_sikuli('edit_ig_united_way_pdf_run_'+BRWSR.lower()+'_bottom.png', "Step 16(b): Verify United way infographic bottom chart")
        else:
            utillobj.verify_picture_using_sikuli('edit_ig_united_way_pdf_run_'+BROWSER.lower()+'.png', "Step 16(a): Verify United way infographic pdf chart")
        time.sleep(2)
        utillobj.switch_to_default_content(pause=1)
        
        """    17. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()
