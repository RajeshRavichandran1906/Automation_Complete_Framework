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
from common.pages import security_center, wf_legacymainpage
from common.lib import utillity


class C2324201_TestClass(BaseTestCase):

    def test_C2324201(self):
        
        """
            TESTCASE VARIABLES
        """
        workspace = "Workspaces"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        main_obj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        securityobj =security_center.Security_Center(driver)
        project_id = utillobj.parseinitfile('project_id')
        devuser = utillobj.parseinitfile('mrid03')
#         
        """ Step 1 : Sign in as WF Administrator
        """
        utillobj.invoke_legacyhomepage('mrid', 'mrpass')
         
         
        """ Step 2: Click banner link Administration ->Security Center
        """
        utillobj.synchronize_until_element_is_visible("#topBannerMenuBox #AdministrationMainLink", securityobj.home_page_long_timesleep)
        main_obj.select_or_verify_top_banner_links('Administration->Security Center')
        utillobj.synchronize_until_element_is_visible("#dlgSecurityManager #SecurityManagerDialog_btnNewUser", securityobj.home_page_long_timesleep)
         
        """ Step 3: Create three new users : domain basic user, domain advanced user and group admin user.
        """
        """ Step 4: Assign domain basic user to P292/Basic Users group,
                    Assign domain advanced user to P292/Advanced Users group and
                    Assign domain group admin user to P292/GroupAdmins.
        """
        securityobj.create_user('basicuser', group=project_id+'/BasicUsers', btn='ok')
        time.sleep(5)
        securityobj.create_user('advanceduser', group=project_id+'/AdvancedUsers', btn='ok')
        time.sleep(5)
        securityobj.create_user('groupadminuser', group=project_id+'/GroupAdmins', btn='ok')
         
        """ Step 5: Select WF Basic user and add to Retail_samples -->BasicUsers group and WFPMResponsiveDemo -->BasicUsers group.
                    Verify the user is added to both the groups.
        """
        #Retail_Samples
        securityobj.add_user_to_group('basicuser','Retail_Samples->BasicUsers', ['basicuser'],"Step 5:")
        #WFPMResponsiveDemo
        securityobj.add_user_to_group('basicuser','WFPMResponsiveDemo->BasicUsers', ['basicuser'], "Step 5.1:")
         
        """ Step 6: Select Advanced user and add to Retail_samples -->AdvancedUsers group and WFPMResponsiveDemo -->AdvancedUsers group.
                    Verify the user is added to both the groups.
        """
        time.sleep(2)
        #Retail_Samples
        securityobj.add_user_to_group('advanceduser','Retail_Samples->AdvancedUsers',['advanceduser'], "Step 6:")
        #WFPMResponsiveDemo
        securityobj.add_user_to_group('advanceduser','WFPMResponsiveDemo->AdvancedUsers',['advanceduser'], "Step 6.1")
         
        """ Step 7: Select Developer user and add to Retail_samples -->DeveloperUsers group and WFPMResponsiveDemo -->DeveloperUsers group.
                    Verify the user is added to both the groups.
        """
        time.sleep(2)
        #Retail_Samples
        securityobj.add_user_to_group(devuser,'Retail_Samples->Developers',[devuser], "Step 7:")
        #WFPMResponsiveDemo
        securityobj.add_user_to_group(devuser, 'WFPMResponsiveDemo->Developers',[devuser], "Step 7.2")
         
        """ Step 8: Select GroupAdmin user and add to Retail_samples -->GroupAdmins group and WFPMResponsiveDemo -->GroupAdmins group.
                    Verify the user is added to both the groups.
        """
        time.sleep(2)
        #Retail_Samples  
        securityobj.add_user_to_group('groupadminuser','Retail_Samples->GroupAdmins',['groupadminuser'], "Step 8.1:")
        #WFPMResponsiveDemo
        securityobj.add_user_to_group('groupadminuser','WFPMResponsiveDemo->GroupAdmins',['groupadminuser'], "Step 8.2:")
         
        """ Step 9: Click on every sub group under 'P292'.
                    Verify that the corresponding users were added
        """
        time.sleep(2)
        #BasicUsers
        securityobj.verify_user_in_group(project_id+'->BasicUsers', ['basicuser'],"Step 9.1:")
        #AdvancedUsers
        securityobj.verify_user_in_group(project_id+'->AdvancedUsers', ['advanceduser'],"Step 9.2:")
        #Developers
        securityobj.verify_user_in_group(project_id+'->Developers', [devuser],"Step 9.3:")
        #GroupAdmins
        securityobj.verify_user_in_group(project_id+'->GroupAdmins', ['groupadminuser'],"Step 9.4:")
         
        """ Step 10: Close Security Center.
                     Security Center closes
        """
        securityobj.close_security_center_dialog()
        time.sleep(2)
         
        """ Step 11: Click Sign Out
        """
        utillobj.infoassist_api_logout()
        time.sleep(1)
        
        """ Step 12: Sign back in as the same user, Open Security Center.
                     Verify there are no errors
        """
        utillobj.invoke_legacyhomepage('mrid', 'mrpass')
        utillobj.synchronize_until_element_is_visible("#topBannerMenuBox #AdministrationMainLink", securityobj.home_page_long_timesleep)
        main_obj.select_or_verify_top_banner_links('Administration->Security Center')
        utillobj.synchronize_until_element_is_visible("#dlgSecurityManager #SecurityManagerDialog_btnNewUser", securityobj.home_page_long_timesleep)
        parent_css="#dlgSecurityManager"
        utillobj.synchronize_with_number_of_element(parent_css, 1, securityobj.home_page_long_timesleep)
        css="#dlgSecurityManager"
        utillobj.verify_popup(css, "Step 12: Verify dialog box displayed",caption_css="[style*='inherit'] [class*='active'] [class*='caption'] [class*='bi-label']", 
                              caption_text="Security Center", popup_text_css="[style*='inherit'] [class*='active'] [id^='BiTabBar']", popup_text="Users & Groups\nRoles")  
        time.sleep(2)
        #P292/BasicUsers
        securityobj.verify_user_in_group(project_id+'->BasicUsers', ['basicuser'],"Step 12.1:")
        #P292/AdvancedUsers
        securityobj.verify_user_in_group(project_id+'->AdvancedUsers', ['advanceduser'],"Step 12.2:")
        #P292/Developers
        securityobj.verify_user_in_group(project_id+'->Developers', [devuser],"Step 12.3:")
        #P292/GroupAdmins
        securityobj.verify_user_in_group(project_id+'->GroupAdmins', ['groupadminuser'],"Step 12.4:")
        time.sleep(2)
        #Retail_Samples/BasicUsers
        securityobj.verify_user_in_group('Retail_Samples->BasicUsers', ['basicuser'],"Step 12.5:")
        #Retail_Samples/AdvancedUsers
        securityobj.verify_user_in_group('Retail_Samples->AdvancedUsers', ['advanceduser'],"Step 12.6:")
        #Retail_Samples/Developers
        securityobj.verify_user_in_group('Retail_Samples->Developers', [devuser],"Step 12.7:")
        #Retail_Samples/GroupAdmins
        securityobj.verify_user_in_group('Retail_Samples->GroupAdmins', ['groupadminuser'],"Step 12.8:")
        time.sleep(2)
        #WFPMResponsiveDemo/BasicUsers
        securityobj.verify_user_in_group('WFPMResponsiveDemo->BasicUsers', ['basicuser'],"Step 12.9:")
        #WFPMResponsiveDemo/AdvancedUsers
        securityobj.verify_user_in_group('WFPMResponsiveDemo->AdvancedUsers', ['advanceduser'],"Step 12.10:")
        #WFPMResponsiveDemo/Developers
        securityobj.verify_user_in_group('WFPMResponsiveDemo->Developers', [devuser],"Step 12.11:")
        #WFPMResponsiveDemo/GroupAdmins
        securityobj.verify_user_in_group('WFPMResponsiveDemo->GroupAdmins', ['groupadminuser'],"Step 12.12:")
        
        """ Step 13: Close the Security Center and Sign Out from WebFOCUS.
        """
        securityobj.close_security_center_dialog()
        time.sleep(5)
        utillobj.infoassist_api_logout()
        time.sleep(5) 
         
        
if __name__ == '__main__':
    unittest.main()
