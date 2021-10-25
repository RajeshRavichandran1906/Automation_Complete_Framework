'''
Created on 31-Jan-2018

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324329
TestCase Name = Properties Testing : Properties for page or/and portal object
'''
import unittest, time
from common.lib import utillity
from common.pages import visualization_resultarea, wf_legacymainpage
from common.lib.basetestcase import BaseTestCase

class C2324329_TestClass(BaseTestCase):

    def test_C2324329(self):
        """
        TESTCASE VARIABLES
        """
        workspace = "Workspaces"
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        project_id=utillobj.parseinitfile('project_id')
        suite_id=utillobj.parseinitfile('suite_id')
        root_path = project_id+'->'+suite_id
        BIP_Portal_Path = root_path+'->BIP_V4_Portal'
        
        def verify_property_window(page_name, page_name_with_ext, path, step_num):
            properties_textbox_dict = {'Title':str(page_name),'File Name':str(page_name_with_ext)}
            properties_textline_dict = {'Parent Folder':str(path), 'Full Path':str(path)+"/"+str(page_name_with_ext)}
            properties_checkbox_check_uncheck_dict = {"Do not show on User's List":'uncheck', 'Prompt for Parameters':'check', 'Run With OLAP':'uncheck', 'Enable Auto Linking':'uncheck', 'Allow user to Run':'uncheck', 
                                        'Automatically Open':'uncheck','Only Run as Deferred Report':'uncheck', 'Schedule Only':'uncheck', 'Auto Link Target':'uncheck', 'Only allow user to Run':'uncheck',
                                        'Auto Create My Content Folders':'uncheck','Use Title for Deferred Report Description':'uncheck', 'Restrict Schedule to Library Only':'uncheck', 'Enable Auto Drill':'uncheck'}
            properties_checkbox_enable_disable_dict = {"Do not show on User's List":'enable', 'Prompt for Parameters':'disable', 'Run With OLAP':'disable', 'Enable Auto Linking':'disable', 'Allow user to Run':'disable', 
                                        'Automatically Open':'disable','Only Run as Deferred Report':'disable', 'Schedule Only':'disable', 'Auto Link Target':'disable', 'Only allow user to Run':'disable',
                                        'Auto Create My Content Folders':'disable','Use Title for Deferred Report Description':'disable', 'Restrict Schedule to Library Only':'disable', 'Enable Auto Drill':'disable'}
            i=1
            for opt in properties_textbox_dict.keys():
                wf_mainpageobj.verify_properties_dialog('textbox', opt, 
                                                    "Step "+str(step_num)+"."+str(i)+": Verify "+str(page_name)+" Properties window for " +str(opt)+" textbox", value=properties_textbox_dict[opt])
                i+=1
            for opt in properties_textline_dict.keys():
                wf_mainpageobj.verify_properties_dialog('textline', opt, 
                                                    "Step "+str(step_num)+"."+str(i)+": Verify "+str(page_name)+" Properties window for " +str(opt)+" textline", expected_text_line=properties_textline_dict[opt])
                i+=1
            wf_mainpageobj.verify_properties_dialog('checkbox', properties_checkbox_check_uncheck_dict, 
                                                    "Step "+str(step_num)+"."+str(i)+": Verify "+str(page_name)+" Properties window for checkbox checked and unchecked", uncheck=True)
            i+=1
            wf_mainpageobj.verify_properties_dialog('checkbox', properties_checkbox_enable_disable_dict, 
                                                    "Step "+str(step_num)+"."+str(i)+": Verify "+str(page_name)+" Properties window for enable and disable checkbox.", disable=True)
        
            
        """ Step 1: Sign into WebFOCUS home page as Administrator
                    Navigate URL to http://environment_name:port/alias/legacyhome
        """
        utillobj.invoke_legacyhomepage('mrid03', 'mrpass03')
        parent_css = "#PortalResourcevBOX table tr td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, 190)
        time.sleep(1)
        
        """ Step 2: Right click on a page in the Custom folder in the global resources area.
        """
        """ Step 3: Choose Properties
        """
        wf_mainpageobj.select_menu('Global Resources->Page Templates->Custom->Global_Resources_page', 'Properties')
        time.sleep(1)
        path="IBFS:/WFC/Global/PageTemplates/Custom"
        verify_property_window('Global_Resources_page', 'Global_Resources_page.page', path, '1')
        wf_mainpageobj.verify_properties_dialog('button', 'OK', 'msg')
        time.sleep(19)
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value=workspace, with_regular_exprestion=True)
        """ Step 4: Right click on any portal object in the domains area
                    Verify that properties show
        """
        wf_mainpageobj.select_menu(BIP_Portal_Path+'->lock column portal', 'Properties')
        path="IBFS:/WFC/Repository/"+project_id+"/"+suite_id+"/BIP_V4_Portal"
        verify_property_window('lock column portal', 'lock_column_portal.prtl', path, '4')
        wf_mainpageobj.verify_properties_dialog('button', 'OK', 'msg')
        parent_css = "#PortalResourcevBOX table tr td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, 190)
        
        """ Step 5: Right click on any page object in the domains area
        """
        wf_mainpageobj.select_menu(BIP_Portal_Path+'->lock column portal Resources->two_column_page', 'Properties')
        path="IBFS:/WFC/Repository/"+project_id+"/"+suite_id+"/BIP_V4_Portal/lock_column_portal_Resources"
        verify_property_window('two_column_page', 'two_column_page.page', path, '5')
        wf_mainpageobj.verify_properties_dialog('button', 'OK', 'msg')
        
        """ Step 6: Sign Out from WebFOCUS 
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()