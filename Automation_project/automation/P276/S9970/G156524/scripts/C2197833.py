'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2197833
TestCase Name = Drilling down on ACROSS field create two breadcrumb lines
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, wf_legacymainpage
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2197833_TestClass(BaseTestCase):
    def test_C2197833(self):
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        Test_ID="C2197833"
        Test_Case_ID = Test_ID+"_"+browser_type
        driver = self.driver
        #driver.implicitly_wait(60)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        legacyobj=wf_legacymainpage.Wf_Legacymainpage(self.driver)
        
        """    1. Open IA_Shell for edit using the API
        http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FIA-Shell.fex&tool=Report    """
        utillobj.infoassist_api_edit("IA-Shell", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(15)
        
        """    2. Click on HTML output format in status bar and select Active format    """
        ribbonobj.change_output_format_type('pdf', 'status_bar')
        time.sleep(15)
        
        """    3. Click IA > Save As > Type C2197833a > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID + "_a")
        time.sleep(5)
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    4. Navigate to the welcome page to access resource tree...Enter credentials to login if needed    """
        node = utillobj.parseinitfile('nodeid')
        port = utillobj.parseinitfile('httpport')
        context = utillobj.parseinitfile('wfcontext')
        setup_url = 'http://' + node + ':' + port + context + '/'
        self.driver.get(setup_url)
        utillobj.login_wf('mrid','mrpass')
        time.sleep(6)
        
        """    5. Right click on C2197833 under S9970 folder from the BIP,and Select Properties from the context menu.    """
        project_id=utillobj.parseinitfile('project_id')
        folder = utillobj.parseinitfile('suite_id')
        legacyobj.select_repository_menu(project_id + "->" + folder + "->" + Test_Case_ID + "_a", "Properties")
        
        """    6. Check off the Enable Auto Drill check box > Click OK to close.    """
        driver.find_element_by_css_selector("#dlgProperties #flagList #enableAutoDrill").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#dlgProperties #btnOK").click()
        time.sleep(6)
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    7. Run from BIP using API, 
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%3A%2FWFC%2FRepository%2FS9970&BIP_item=C2197833.fex    """
        utillobj.active_run_fex_api_login(Test_Case_ID + "_a" + ".fex", "S9970", 'mrid', 'mrpass')
        time.sleep(25)
        """    Verify the Report should run and not display any Auto Drill links    """
        time.sleep(3) 
        utillobj.take_monitor_screenshot(Test_Case_ID+'_Actual_Step07', image_type='actual',left=1, top=80, right=1, bottom=120)    
        
        """    8. Close the output window    """
        
if __name__ == '__main__':
    unittest.main()
    
