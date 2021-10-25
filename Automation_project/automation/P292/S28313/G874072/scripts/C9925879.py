'''
Created on Aug 27, 2019

@author: Niranjan
Test case link: http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/9925879
Test case name: Context Menu:Verify Homepage Context menu for Domain/Folders as Developer.
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.pages.wf_mainpage import Wf_Mainpage
from common.lib import utillity
from common.lib import core_utility

class C9925879_TestClass(BaseTestCase):

    def test_C9925879(self):
        
        """
        TESTCASE VARIABLES
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        core_utils = core_utility.CoreUtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        main_page = Wf_Mainpage(driver)
        
        """ COMMON VARIABLES """
        project_id = core_utils.parseinitfile('project_id')
        suite_id = core_utils.parseinitfile('suite_id')
        folder_path = project_id+'_'+suite_id
        
        '''
        Step 1 : Sign into WebFOCUS Home Page as Developer User.
        '''
        wftools_login_obj.invoke_home_page('mrid', 'mrpass')
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_visble_text('.toolbar', "Workspaces", wfmain_obj.home_page_long_timesleep)
        
        '''
        Step 2 : Under Domain Tree >> Right-click on P292_S10660 domain.
        Verify Context Menu,
        
        Expand/Collapse.
        Paste (Grayed out).
        Refresh.
        Security (Rules on this resource/Effective Policy).
        Properties.
        '''
        wfmain_obj.verify_repository_folder_context_menu(folder_path,['Collapse', 'Paste Ctrl+V', 'Refresh', 'Security', 'Properties'], msg ="step 02:01")
        paste_element = utillobj.validate_and_get_webdriver_object('[data-ibx-type="ibxMenuItem"][action="paste"]',"Paste_element")
        paste_grey_out_value =utillobj.get_element_css_propery(paste_element,'opacity')
        utillobj.asequal(paste_grey_out_value,'0.5',"step 02.02 : Paste (Grayed out).")
        main_page.verify_context_submenu_item('Security', ['Rules on this resource...', 'Effective policy...'], msg = 'step 02.03')
        
        '''
        Step 3 : Under Domain Tree >> Right-click on My Content folder underneath 'P292_S10660' domain.
        Verify Context Menu,
        
        Expand/Collapse.
        Paste (Grayed out).
        Delete.
        Refresh.
        Security (Rules on this resource/Effective Policy).
        Share/Unshare.
        Share with.
        Properties.
        '''
        wfmain_obj.verify_repository_folder_context_menu(folder_path+'->My Content',['Collapse', 'Paste Ctrl+V', 'Delete DEL', 'Refresh', 'Security', 'Share', 'Share with...', 'Properties'], msg ="step 03:01")
        paste_element = utillobj.validate_and_get_webdriver_object('[data-ibx-type="ibxMenuItem"][action="paste"]',"Paste_element")
        paste_grey_out_value =utillobj.get_element_css_propery(paste_element,'opacity')
        utillobj.asequal(paste_grey_out_value,'0.5',"step 03.02 : Paste (Grayed out).")
        main_page.verify_context_submenu_item('Security', ['Rules on this resource...', 'Effective policy...'], msg = 'step 03.03')
        
        '''
        Step 4 : Under Domain Tree >> Right-click on Hidden Content folder underneath 'P292_S10660' domain.
        Verify Context Menu,
        
        Expand/Collapse.
        Duplicate.
        Cut.
        Copy.
        Paste (Grayed out).
        Delete.
        Refresh.
        Unpublish/Publish.
        Show/Hide.
        Security (Rules on this resource/Effective Policy/Owner).
        Properties.
        '''
        wfmain_obj.verify_repository_folder_context_menu(folder_path+'->Hidden Content',['Collapse', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Paste Ctrl+V', 'Delete DEL', 'Refresh', 'Unpublish', 'Show', 'Security', 'Properties'],msg ="step 04:01")
        paste_element = utillobj.validate_and_get_webdriver_object('[data-ibx-type="ibxMenuItem"][action="paste"]',"Paste_element")
        paste_grey_out_value =utillobj.get_element_css_propery(paste_element,'opacity')
        utillobj.asequal(paste_grey_out_value,'0.5',"step 04.02 : Paste (Grayed out).")
        main_page.verify_context_submenu_item('Security', ['Rules on this resource...', 'Effective policy...', 'Owner...'], msg = 'step 04.03')
        
        '''
        Step 5 : Under Domain Tree >> Right-click on G671733 folder underneath 'P292_S10660' domain.
        Verify Context Menu,
        
        Expand/Collapse.
        Duplicate.
        Cut.
        Copy.
        Paste (Grayed out).
        Delete.
        Refresh.
        Unpublish/Publish.
        Hide/Show.
        Security (Rules on this resource/Effective Policy/Owner).
        Properties.
        '''
        wfmain_obj.verify_repository_folder_context_menu(folder_path+'->G671733',['Collapse', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Paste Ctrl+V', 'Delete DEL', 'Refresh', 'Unpublish', 'Hide', 'Security', 'Properties'],msg="step 05:01")
        paste_element = utillobj.validate_and_get_webdriver_object('[data-ibx-type="ibxMenuItem"][action="paste"]',"Paste_element")
        paste_grey_out_value =utillobj.get_element_css_propery(paste_element,'opacity')
        utillobj.asequal(paste_grey_out_value,'0.5',"step 05.02 : Paste (Grayed out).")
        main_page.verify_context_submenu_item('Security', ['Rules on this resource...', 'Effective policy...', 'Owner...'], msg = 'step 05.03')
        
        '''
        Step 6 : In the banner link, click on the top right username > Sign Out.
        '''
        wfmain_obj.signout_from_username_dropdown_menu()
                
if __name__ == '__main__':
    unittest.main()