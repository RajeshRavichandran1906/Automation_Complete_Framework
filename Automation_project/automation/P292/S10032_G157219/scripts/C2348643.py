'''
Created on Dec 07, 2017

@author: Praveen Ramkumar
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2348643
Testcase Name :Responsive Autoprompt- All values check box should be checked after running with the filter values
'''
import unittest, time
from common.pages import visualization_resultarea, ia_run,wf_legacymainpage
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase


class C2348643_TestClass(BaseTestCase):

    def test_C2348643(self):
        driver=self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ia_runobj=ia_run.IA_Run(self.driver)
        wf_mainobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        
        
        """
            Step 01: Upload the attached fex in the repository
        """
#        Fex uploaded in CVS
        utillobj.invoke_webfocu('mrid', 'mrpass')
        parent_css="#bipTreePanel tbody tr:nth-child(1)> td"
        resultobj.wait_for_property(parent_css, 1, string_value='Domains', with_regular_exprestion=True)
        
        """
            Step 02: Right click the attached fex and click the properties option Verify that Prompt for parameters options is checked
        """
        wf_mainobj.select_repository_folder_item_menu('P292->S10032_infoassist_5', "simple_optional", "Properties")
        wf_mainobj.verify_properties_dialog("checkbox", "Prompt for Parameters", msg='Step 02:Verify properity',tab_name='Main Properties',enable=True)
        time.sleep(1)
        
        """
            Step 03:Click ok in the properties dialog
        """
        wf_mainobj.verify_properties_dialog('button', 'OK', 'Step 3:')
        time.sleep(2)
        utillobj.infoassist_api_logout()
        
        """
            Step 04:Run the saved fex from BIP using API link
            http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10032&BIP_item=simple_optional.fex
        """
        utillobj.active_run_fex_api_login("simple_optional.fex",'S10032_infoassist_5', 'mrid', 'mrpass')
        
        """
            Step 05:In Autoprompt window verify that all check box is checked for country values
            Step 06:Click run with filter values in autoprompt window.
        """
        actual1=self.driver.find_element_by_css_selector("div[class='autop-amper-ctrl-container'] div[class^='autop-amper'][title='COUNTRY:']").text.strip().replace('\n',' ')
        expected_paramter1="COUNTRY: All"
        utillobj.asequal(actual1,expected_paramter1,'Step 06.1 : Verify default amper value for Paramater1')
        actual_2=self.driver.find_element_by_css_selector("div[class^='autop-amper'][title='COUNTRY:'] input[type='text']").get_attribute('value').strip()
        expected_paramter2="All Values"
        utillobj.asequal(actual_2,expected_paramter2,'Step 06.2 : Verify default amper value for Paramater1')
        ia_runobj.select_amper_menu('Run')
                
        """
            Step 07:Click the show filter panel icon the autoprompt window.Verify that All check box should be checked.
        """        
        css="#header [class*='autop-btn-show-prompts ui-btn-left ui-btn ui-icon-bars ui-btn-icon-notext ui-corner-all']"
        elem=driver.find_element_by_css_selector(css)
        utillobj.click_on_screen(elem, 'left', click_type=0)
        actual1=self.driver.find_element_by_css_selector("div[class='autop-amper-ctrl-container'] div[class^='autop-amper'][title='COUNTRY:']").text.strip().replace('\n',' ')
        expected_paramter1="COUNTRY: All"
        utillobj.asequal(actual1,expected_paramter1,'Step 07.1 : Verify default amper value for Paramater1')
        actual_2=self.driver.find_element_by_css_selector("div[class^='autop-amper'][title='COUNTRY:'] input[type='text']").get_attribute('value').strip()
        expected_paramter2="All Values"
        utillobj.asequal(actual_2,expected_paramter2,'Step 07.2 : Verify default amper value for Paramater1')
        time.sleep(5)
        
        """
            Step 08:Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        
if __name__ == '__main__':
    unittest.main()        