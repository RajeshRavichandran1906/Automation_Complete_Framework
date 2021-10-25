'''
Created on Oct 30, 2018

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/6412883&group_by=cases:section_id&group_order=asc&group_id=483974
Testcase Name : Verify Rules for this Group for Group Admin 
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import utillity
from common.lib import core_utility
from common.wftools import security_center

class C6412883_TestClass(BaseTestCase):

    def testName(self):
        
        """
            CLASS OBJECTS 
        """
        wf_login = login.Login(self.driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(self.driver)
        utillobj=utillity.UtillityMethods(self.driver)
        core_utillobj=core_utility.CoreUtillityMethods(self.driver)
        security_centre_obj=security_center.Security_Center(self.driver)
        
        """ 
            VARIABLES
        """
        USERNAME='mrid'
        PASSWORD='mrpass'
        MEDIUM_WAIT=60
        
        """ 
            CSS 
        """
        RULES_FOR_THIS_GROUP_DIALOG="#resourceRulesDlg"
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        """
            Step 1:Sign to Webfocus using the below link.
            http://machine:port/ibi_apps
            Step 2:Verify the Retail Samples Domain is available under Repository
        """
        wf_login.invoke_home_page(USERNAME, PASSWORD)

        
        """ 
            Step 3:Click Administration > Security Center
            Verify the Retail Samples Group is available.
        """
        wfmain_obj.select_username_dropdown_menu(navigate_path='Administration->Security Center')
        core_utillobj.switch_to_new_window()
        
        """ 
            Step 4:Expand Retail Samples
            Verify the following Groups are available
        """
        security_centre_obj.expand_group_section_('Retail_Samples->GroupAdmins')
        
        security_centre_obj.get_group_name_from_the_parent_group('BasicUsers')
        security_centre_obj.get_group_name_from_the_parent_group('AdvancedUsers')
        security_centre_obj.get_group_name_from_the_parent_group('GroupAdmins')
        security_centre_obj.get_group_name_from_the_parent_group('Developers')
        
        """
            Step 5:Right click Group Admins > Security
            Verify the following Rules are available
            Step 6:Select Rules for this Group
        """
        security_centre_obj.right_click_on_group('Retail_Samples->GroupAdmins')
        security_centre_obj.select_group_context_menu('Security->Rules for this Group...')
        
#         utillobj.synchronize_with_number_of_element(RULES_FOR_THIS_GROUP_DIALOG, "Rules for this Group - GroupAdmins", MEDIUM_WAIT) 
            
        """ 
            Verify the following rules are displayed.
        """
        security_centre_obj.verify_caption_in_rules_for_this_group_dialog("Rules for this Group", "Step 07:Verify rules dialog")
        
         
        """ 
            Step 7:Close Security center
        """
        security_centre_obj.click_close_button_in_rules_for_this_resource_dialog()
          
        """    
            Step 8:Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp.
        """
    


if __name__ == "__main__":
    unittest.main()