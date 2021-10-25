'''
Created on May 2, 2018

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10863
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5824549
TestCase Name = Verify Global Preferences default values are correct after restoring default values
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea,wf_administration_console,ia_ribbon,visualization_metadata,visualization_ribbon
from common.lib import utillity

class C5824549_TestClass(BaseTestCase):

    def test_C5824549(self):
        
        """   
        TESTCASE VARIABLES 
        """
        TestCase_ID = "C5824549"
        driver=self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        Wf_admincons=wf_administration_console.Wf_Administration_Console(self.driver)
        iaribbon=ia_ribbon.IA_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """
        Step 01 : Logon to WF:http://machine:port/ibi_apps/
        Step 02 :Select "Administration" > "Administration Console".
        """
        utillobj.invoke_webfocu('mrid01', 'mrpass01')
        time.sleep(8)
        node = utillobj.parseinitfile('nodeid')
        port = utillobj.parseinitfile('httpport')
        context = utillobj.parseinitfile('wfcontext')
        admin_console_url = 'http://' + node + ':' + port + context + '/admin'
        driver.get(admin_console_url)
        time.sleep(8)

        """
        Step 03:Select "InfoAssist Properties".        
        """
        Wf_admincons.select_admin_console_tree("#console_tree_Configuration_Settings .bi-tree-view-body-content", "InfoAssist Properties")
         
        """
        Step 04:In the "Tool Options Dialog Defaults" section > "Chart Output Format" > Select "PDF".       
        """
        utillobj.mouse_scroll('down',15)        
        Wf_admincons.input_bihbox("#idInfoassistPropertiesPage","Chart Output Format",input_control='combobox',combobox_value='PDF')
        print("input")
         
        """
        Step 05:Scroll down, click "Save" > Click OK in the save confirmation message displayed        
        """
        Wf_admincons.save_cancel_restoredefaultvalues_button('down', 'Save', number_of_times=30)
        time.sleep(5)
          
        """
        Step 06:Select again "InfoAssist Properties".       
        """
        Wf_admincons.select_admin_console_tree("#console_tree_Configuration_Settings .bi-tree-view-body-content", "InfoAssist Properties")
          
        """
        Step 07:Scroll down and locate "Tool Options Dialog Defaults" > "Chart Output Format".
        Step 08:Verify "Chart Output Format" = "PDF".
        """
        utillobj.mouse_scroll('up',25)
        time.sleep(8)
        Wf_admincons.verify_bihbox("#idInfoassistPropertiesPage", "Chart Output Format",'combobox','PDF', "Step 08.1:Verify the following default settings for View Tab")
 
        """
        Step 09:Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp   
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
          
        """
        Step 10:Launch IA Chart mode:http://machine:port/ibi_apps/ia?tool=Chart&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10032  
        """
        utillobj.infoassist_api_login('Chart','ibisamp/car','P292/S10863_infoassist_1', 'mrid', 'mrpass')
        parent_css="div[align='justify']"
        resultobj.wait_for_property(parent_css, 1,expire_time=15)
        
        """
        Step 11:Verify Chart default format is "PDF" (located in the Home Tab)  
        """
        iaribbon.select_or_verify_output_type(launch_point='Home',item_select_path='PDF')
         
        """
        Step 12:Double click fields CAR, RETAIL_COST  
        """
        metadataobj.datatree_field_click('CAR', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(4) td"
        resultobj.wait_for_property(parent_css, 1, string_value='CAR', with_regular_exprestion=True)
        metadataobj.datatree_field_click('RETAIL_COST', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(3) td"
        resultobj.wait_for_property(parent_css, 1, string_value='RETAIL_COST', with_regular_exprestion=True)
         
        """
        Step 13:Click "Save" > save as "C5824549" > Click Save
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(TestCase_ID)
        time.sleep(8)
         
        """
        Step 14:Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
         
        """
        Step 15:Reopen saved FEX:http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2227499.fex&tool=Chart
                Reopen FEX:http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2223508.fex&tool=report
        """
        utillobj.infoassist_api_edit(TestCase_ID,'Chart','P292/S10863_infoassist_1',mrid='mrid',mrpass='mrpass')
        time.sleep(8)
         
        """
        Step 16:Verify Chart and default format (PDF)
        """
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,TestCase_ID + '_Actual_step16', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
         
        """
        Step 17:Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
        Step 18:Logon to WF:http://machine:port/ibi_apps/
        Step 19:Select "Administration" > "Administration Console".
        """
        utillobj.invoke_webfocu('mrid01', 'mrpass01')
        time.sleep(8)
        node = utillobj.parseinitfile('nodeid')
        port = utillobj.parseinitfile('httpport')
        context = utillobj.parseinitfile('wfcontext')
        admin_console_url = 'http://' + node + ':' + port + context + '/admin'
        driver.get(admin_console_url)
        time.sleep(8)
        
        """
        Step 20:Select "InfoAssist Properties".
        """
        Wf_admincons.select_admin_console_tree("#console_tree_Configuration_Settings .bi-tree-view-body-content", "InfoAssist Properties")
        utillobj.mouse_scroll('down',50)
        
        """
        Step 21:Scroll down, click "Restore Default Values".
        Step 22:Verify a message window displayed.
        Step 23: Click "OK" > OK
        """
        utillobj.click_dialog_button("#idInfoassistPropertiesPage div[id^='BiHBox']",'Restore Default Values')
        utillobj.click_dialog_button("#dlgInfoassistRestore [class*='active']", "OK")
        time.sleep(5)
        als = driver.switch_to.alert
        als.accept()
        
        """
        Step 23: Click "OK" > OK
        Step 24:Select again "InfoAssist Properties".
        """ 
        Wf_admincons.select_admin_console_tree("#console_tree_Configuration_Settings .bi-tree-view-body-content", "InfoAssist Properties")
        
        """
        Step 25:Scroll down and locate "Tool Options Dialog Defaults" > "Chart Output Format".
        Step 26:Verify default value (HTML5) is restored
        """ 
        Wf_admincons.verify_bihbox("#idInfoassistPropertiesPage", "Chart Output Format",'combobox','HTML5', "Step 26.1:Verify the following default settings for View Tab")
        
        """
        Step 27:Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """ 
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
if __name__ == '__main__':
    unittest.main()