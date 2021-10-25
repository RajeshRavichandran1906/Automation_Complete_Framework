'''
Created on AUG 28, 2017

@author: Pavithra

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10117&group_by=cases:section_id&group_id=169813&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2324201
TestCase Name = User Creation/Adding to groups : Create basic, advanced and developer users for domain
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import wf_mainpage,visualization_resultarea,security_center, wf_legacymainpage
from common.lib import utillity



class C2324201_TestClass(BaseTestCase):

    def test_C2324201(self):
        
        """
            TESTCASE VARIABLES
        """
        driver = self.driver#Driver reference object created
        driver.implicitly_wait(15) #Intializing common implicit wait for throughout the test 
        utillobj = utillity.UtillityMethods(self.driver)
        if utillobj.parseinitfile('nodeid') in ('wfinst01','wfinst02','wfinst03','wfinst05'):
            main_obj = wf_mainpage.Wf_Mainpage(self.driver)
        else:
            main_obj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        resobj =visualization_resultarea.Visualization_Resultarea(driver)
        securityobj =security_center.Security_Center(driver)
        
        """
            Step 01:Sign in as WF Administrator
              
        """
        utillobj.invoke_webfocu('mrid', 'mrpass')
        parent_css="#bipTreePanel tbody tr:nth-child(1)> td"
        resobj.wait_for_property(parent_css, 1, string_value='Domains', with_regular_exprestion=True)
          
        """
            Step 02:Click banner link Administration->Security Center
        """
        time.sleep(8)
        main_obj.select_or_verify_top_banner_links('Administration->Security Center')
        parent_css="#dlgSecurityManager"
        resobj.wait_for_property(parent_css, 1)
          
        """
            Step 03:Create three new users : domain basic user, domain advanced user and group admin user.
               
            Step 04:Assign domain basic user to P292/Basic Users group,
                    Assign domain advanced user to P292/Advanced Users group and
                    Assign domain group admin user to P292/GroupAdmins.    
        """
        securityobj.create_user('basicuser',group='P292/BasicUsers', btn='ok')
        time.sleep(5)
        securityobj.create_user('advanceduser',group='P292/AdvancedUsers', btn='ok')
        time.sleep(5)
        securityobj.create_user('groupadminuser',group='P292/GroupAdmins', btn='ok')
        """
            Step 05: Select WF Basic user and add to Retail_samples -->BasicUsers group and WFPMResponsiveDemo -->BasicUsers group.
        """
        #Retail_Samples
        securityobj.add_user_to_group('basicuser','Retail_Samples', 'BasicUsers', ['basicuser'],"Step 05.1:")
        #WFPMResponsiveDemo
        securityobj.add_user_to_group('basicuser','WFPMResponsiveDemo', 'BasicUsers', ['basicuser'], "Step 05.2:")
            
        """
            Step 06:Select Advanced user and add to Retail_samples -->AdvancedUsers group and WFPMResponsiveDemo -->AdvancedUsers group.
        """
        time.sleep(2)
        #Retail_Samples
        securityobj.add_user_to_group('advanceduser','Retail_Samples', 'AdvancedUsers',['advanceduser'], "Step 06.1:")
        #WFPMResponsiveDemo
        securityobj.add_user_to_group('advanceduser','WFPMResponsiveDemo', 'AdvancedUsers',['advanceduser'], "Step 06.2")
           
        """
            Step 07:Select Developer user and add to Retail_samples -->DeveloperUsers group and WFPMResponsiveDemo -->DeveloperUsers group.
        """
        #Retail_Samples 
        securityobj.verify_user_in_group('Retail_Samples', 'Developers',['autodevuser43'], "Step 07.1:",pgdn_times=7)
        #WFPMResponsiveDemo
        securityobj.verify_user_in_group('WFPMResponsiveDemo', 'Developers',['autodevuser43'], "Step 07.2:" ,pgdn_times=7)
        """
            Step 08:Select GroupAdmin user and add to Retail_samples -->GroupAdmins group and WFPMResponsiveDemo -->GroupAdmins group.
        """
        #Retail_Samples  
        securityobj.add_user_to_group('groupadminuser','Retail_Samples', 'GroupAdmins',['groupadminuser'], "Step 08.1:")
        #WFPMResponsiveDemo
        securityobj.add_user_to_group('groupadminuser','WFPMResponsiveDemo', 'GroupAdmins',['groupadminuser'], "Step 08.2:")
        """
            Step 09:Click on every sub group under 'P292'.
        """
        #BasicUsers
          
        securityobj.verify_user_in_group('P292', 'BasicUsers', ['basicuser'],"Step 09.1:")
        #AdvancedUsers
        securityobj.verify_user_in_group('P292', 'AdvancedUsers', ['advanceduser'],"Step 09.2:")
        #Developers
        securityobj.verify_user_in_group('P292', 'Developers', ['autodevuser43'],"Step 09.3:",pgdn_times=7)
        #GroupAdmins
        securityobj.verify_user_in_group('P292', 'GroupAdmins', ['groupadminuser'],"Step 09.4:")
        """
            Step 10:Close Security Center.
        """
        securityobj.close_security_center_dialog()
        time.sleep(5)
        """
            Step 11:Click Sign Out
        """
        utillobj.infoassist_api_logout()
        time.sleep(5)
        """
            Step 12:Sign back in as the same user, Open Security Center.
        """
        utillobj.invoke_webfocu('mrid', 'mrpass')
        parent_css="#bipTreePanel tbody tr:nth-child(1)> td"
        resobj.wait_for_property(parent_css, 1, string_value='Domains', with_regular_exprestion=True)
        time.sleep(8)
        main_obj.select_or_verify_top_banner_links('Administration->Security Center')
        parent_css="#dlgSecurityManager"
        resobj.wait_for_property(parent_css, 1)    
        css="#dlgSecurityManager"
        utillobj.verify_popup(css, "Step 12.1: Verify dialog box displayed",caption_css="[style*='inherit'] [class*='active'] [class*='caption'] [class*='bi-label']", 
                              caption_text="Security Center", popup_text_css="[style*='inherit'] [class*='active'] [id^='BiTabBar']", popup_text="Users & Groups\nRoles")  
        securityobj.verify_user_in_group('P292', 'BasicUsers', ['basicuser'],"Step 12.2:")
        time.sleep(5)
         
        """
            Step 13:Close the Security Center and Sign Out from WebFOCUS.
        """
        securityobj.close_security_center_dialog()
        time.sleep(5)
        utillobj.infoassist_api_logout()
        time.sleep(5) 
        
if __name__ == '__main__':
    unittest.main()
