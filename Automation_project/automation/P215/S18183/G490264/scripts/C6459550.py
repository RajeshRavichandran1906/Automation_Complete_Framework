'''
Created on 02-Aug-2018

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/18183
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/6459550
TestCase Name = Basic User: Verify Summit Demo Infographic, runtime
'''
import unittest,time, keyboard
from common.lib.basetestcase import BaseTestCase
from common.wftools import infographics
from common.lib import utillity
from common.lib.global_variables import Global_variables

class C6459550_TestClass(BaseTestCase):

    def test_C6459550(self):
        infographicObj=infographics.InfoGraphics(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        g_var = Global_variables()
        USER='mrid_bas'
        PASSWRD='mr_pass'
        PROJECT_ID = utillobj.parseinitfile('project_id')
        SUITE_ID = utillobj.parseinitfile('suite_id')
        PROJ_FLDR="{0}_{1}".format(PROJECT_ID,SUITE_ID)
        PROJ_SUBFLDR='Summit'
        HOMEPAGECSS="div.main-box"
        RUNIMGCSS='body>img'
        PAGES=['Peter', 'Marina', 'Stefan', 'Boris', 'Siebe', 'Majase', 'Christian', 'Peter', 'Thomas','Klaus']
        BRWSR='Chrome'   
        
        """    1. Sign in to WebFOCUS as a Basic user - http://machine:port/{alias}/    """
        infographicObj.signin_to_WF_with_user(USER, PASSWRD, HOMEPAGECSS)
        
        """    2. Repository folder: P413_S18040 > Summit, Execute the following URL:
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_LAUNCH&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP413_S18040%252FSummit%252F&BIP_item=summit_demo.fex    """
        infographicObj.run_infographic_using_api_url(PROJ_FLDR, PROJ_SUBFLDR, 'summit_demo', RUNIMGCSS, 10, USER)
        utillobj.wait_for_page_loads(20)
                
        """    3. Verify the 10 Infographic images displayed for the following participants:     
                  Peter   Marina  Stefan  Boris   Siebe   Majase  Christian   Peter   Thomas  Klaus    """
        '''Francesca 7/11/18 Note to Automation team: Step 3
            Verify the entire infographic image #1 for participant Peter
            Verify the entire infographic image #10 for participant Klaus
            Verify just the name for participants 2 - 9    '''
        oPages_obj = utillobj.validate_and_get_webdriver_objects(RUNIMGCSS, 'page body image')
        infographicObj.scrolled_into_view(oPages_obj[0])
        utillobj.verify_picture_using_sikuli('page1_top_'+BRWSR.lower()+'.png', "Step 3a.1a: Verify participants - "+PAGES[0]+" top chart")
        keyboard.send('page down')
        time.sleep(3)
        if g_var.browser_name == 'chrome':
            for i in range(1, 4):
                keyboard.send('down')
                time.sleep(3)
        utillobj.verify_picture_using_sikuli('page1_bottom_'+BRWSR.lower()+'.png', "Step 3a.1b: Verify participants - "+PAGES[0]+" bottom chart")
        for i in range(2,10):
            infographicObj.scrolled_into_view(oPages_obj[i-1])
            time.sleep(2)
            utillobj.verify_picture_using_sikuli('page'+str(i)+'_'+PAGES[i-1].lower()+'_'+BRWSR.lower()+'.png', "Step 3b."+str(i)+": Verify participants - "+PAGES[i-2]+" name")
            time.sleep(1)
        infographicObj.scrolled_into_view(oPages_obj[9])
        utillobj.verify_picture_using_sikuli('page10_top_'+BRWSR.lower()+'.png', "Step 3c.10a: Verify participants - "+PAGES[9]+" top chart")
        keyboard.send('page down')
        time.sleep(1)
        keyboard.send('page down')
        time.sleep(1)
        utillobj.verify_picture_using_sikuli('page10_bottom_'+BRWSR.lower()+'.png', "Step 3c.10b: Verify participants - "+PAGES[9]+" bottom chart")
        time.sleep(1)
        
        """    4. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        
if __name__ == '__main__':
    unittest.main()
