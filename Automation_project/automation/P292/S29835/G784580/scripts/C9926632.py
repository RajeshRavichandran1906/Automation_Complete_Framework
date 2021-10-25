"""-------------------------------------------------------------------------------------------
Created on September 13, 2019
@author: Vishnu Priya
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.wftools import page_designer
from common.lib import utillity
from common.locators import wf_mainpage_locators

class C9926632_TestClass(BaseTestCase):

    def test_C9926632(self):
        
        """
            CLASS OBJECTS 
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        content_css=wf_mainpage_locators.WfMainPageLocators.CONTENT_CSS
        page_designer_obj=page_designer.Design(self.driver)
        wfmain_obj_run=wf_mainpage.Run(self.driver)
      
        """
            COMMON TEST CASE VARIABLES 
        """
            
        """ Step 1: Login WF as domain developer
        """
        wftools_login_obj.invoke_home_page('mrid', 'mrpass')
        utillobj.synchronize_with_visble_text(content_css, "Content", 60)
        
        """Step 2: Click on Content tree from side bar
        """
        wfmain_obj.select_content_from_sidebar()
        
        """
        Step 3:Expand 'P292_S29835' domain -> 'G874878' folder;
        Double click on 'Explorer Widget page'
        Verify that sidebar removed from the explorer widget.
        """
        wfmain_obj.expand_repository_folder("P292_S11397->G874878")
        page_designer_obj.run_page_designer_by_double_click("Explorer Widget page",folder_path='P292_S11397->G874878')
        wfmain_obj_run.switch_to_frame()
        page_designer_obj.switch_to_container_frame("Panel 1")
        utillobj.verify_object_visible(".left-main-panel",False,"Verify that sidebar removed from the explorer widget.")
        
        """
        Step 4:Close the 'Explorer widget page' run window..
        """
        page_designer_obj.switch_to_default_page()
        wfmain_obj_run.close()
        
        """
        Step 5:In the banner link, click on the top right username > Click Sign Out.
        """
        

if __name__ == '__main__':
    unittest.main()