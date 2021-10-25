'''
Created on May 2, 2018

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10863
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5824307
TestCase Name = Verify Global Preferences default values
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import wf_administration_console,wf_mainpage
from common.lib import utillity

class C5824307_TestClass(BaseTestCase):

    def test_C5824307(self):
        
        """   
        TESTCASE VARIABLES 
        """
        utillobj = utillity.UtillityMethods(self.driver)
        Wf_admincons=wf_administration_console.Wf_Administration_Console(self.driver)
        mainpageobj = wf_mainpage.Wf_Mainpage(self.driver)
        
        """
            Step 01 :Logon to WF:http://machine:port/ibi_apps/
            Step 02 :Select "Administration" > "Administration Console".
        """
        utillobj.invoke_webfocu('mrid01', 'mrpass01')
        time.sleep(4)
        folders_css=".menu-btn div[class*='down']"
        utillobj.synchronize_with_number_of_element(folders_css, 1, 90)
        time.sleep(4)
        mainpageobj.select_username_dropdown_menu(navigate_path='Administration->Administration Console')
        time.sleep(4)
        utillobj.switch_to_window(1)
        
        """
            Step 03 :Select "InfoAssist Properties".
        """
        Wf_admincons.select_admin_console_tree("#console_tree_Configuration_Settings .bi-tree-view-body-content", "InfoAssist Properties")
                
        """
            Step 04 :Verify the following default settings for "Home Tab". Verify "Allow User Override" is enabled.
        """
        Wf_admincons.verify_bihbox("#idInfoassistPropertiesPage", "Use Live Preview Mode", 'checkbox','checked', "Step 04.1 : Verify Allow User Override is enabled.",2)
        
        """
            Step 05 :Verify the following default settings for "Format Tab".
        """
        item_checked=['Allow User Override','Excel 2000 Format','Excel 2000 Formula','Excel 2007 Format','Excel 2007 Formula','Excel csv','HTML Format','InfoMini Run Immediate','Other Chart Types','Pages on Demand','PDF Format','PowerPoint 2007 Format','Stack Measures']
        for i in range(len(item_checked)):
            Wf_admincons.verify_bihbox("#idInfoassistPropertiesPage", item_checked[i], 'checkbox', 'checked',"Step 05."+str(i)+" : Verify default settings for Format Tab checked")
         
        item_Unchecked=['Active PDF Format','Additional HTML Formats for Chart','Additional PDF Formats for Chart','Excel Pivot','PowerPoint 2000 Format','User Selection']
        for i in range(len(item_Unchecked)):
            Wf_admincons.verify_bihbox("#idInfoassistPropertiesPage", item_Unchecked[i], 'checkbox', 'unchecked',"Step 05.1."+str(i)+" : Verify default settings for Format Tab unchecked")
          
        """
            Step 06 :Verify the following default settings for "View Tab".
        """
        Wf_admincons.verify_bihbox("#idInfoassistPropertiesPage", "Display View Tab", 'checkbox','checked', "Step 06.1 : Verify the following default settings for View Tab")
        Wf_admincons.verify_bihbox("#idInfoassistPropertiesPage", "Data Panel", 'combobox','Logical', "Step 06.2 : Verify the following default settings for View Tab")
        Wf_admincons.verify_bihbox("#idInfoassistPropertiesPage", "Query Panel", 'combobox','Tree', "Step 06.3 : Verify the following default settings for View Tab")
        Wf_admincons.verify_bihbox("#idInfoassistPropertiesPage", "Query Panel", 'checkbox','checked', "Step 06.4 : Verify the following default settings for View Tab")
        
        """
            Step 07 :Verify the following default settings for "Tool Options Dialog Defaults".
        """
        utillobj.mouse_scroll('down',20)
        row=['Report Output Format','Chart Output Format','Document Output Format','Page Orientation','Page Size','Data Preview Method','Record Limit','Output Target']
        result=['HTML','HTML5','Active Report','Landscape','Letter','Live','500','Single tab']
        for i in range(len(row)):
            Wf_admincons.verify_bihbox("#idInfoassistPropertiesPage>div>div>div:nth-child(13)", row[i], 'combobox', result[i],"Step 07."+str(i)+" : Verify the following default settings for Tool Options Dialog Defaults")
        
        item_Unchecked=['Page Orientation','Page Size','Data Preview Method','Record Limit','Output Target','InfoAssist+/Portal Stylesheet','Visualization StyleSheet','Encode HTML']
        for i in range(len(item_Unchecked)):
            Wf_admincons.verify_bihbox("#idInfoassistPropertiesPage", item_Unchecked[i], 'checkbox', 'checked',"Step 07a."+str(i)+" : Verify the following default settings for Tool Options Dialog Defaults")
        Wf_admincons.verify_bihbox("#idInfoassistPropertiesPage", "Enable Pages On Demand", 'checkbox','unchecked', "Step 07a.2 : Verify the following default settings for Tool Options Dialog Defaults") 
        Wf_admincons.verify_bihbox("#idInfoassistPropertiesPage", "Rows retrieved from cache", 'textbox','100', "Step 07a.3 : Verify the following default settings for Tool Options Dialog Defaults")
        
        """
            Step 08 :Verify the following default settings for "File Options".
        """
        utillobj.mouse_scroll('down',10)
        item_checked=['Binary','FOCUS','Comma Delimited with Titles','Plain Text','Tab Delimited','Tab Delimited with Titles','Database Table','Hyperstage','SQL script','XML','JSON']
        for i in range(len(item_checked)):    
            Wf_admincons.verify_bihbox("#idInfoassistPropertiesPage", item_checked[i], 'checkbox', 'checked',"Step 08."+str(i)+" : Verify the following default settings for Tool Options Dialog Defaults")
        
        """
            Step 09 :Verify the following default settings for "Chart Types"
        """
        utillobj.mouse_scroll('down',20)
        Wf_admincons.verify_bihbox("#idInfoassistPropertiesPage", "Leaflet Maps", 'checkbox','checked', "Step 09.2 : Verify the following default settings for Chart Types")
        
        """
            Step 10 :Verify the following default settings for "Auto Drill"
        """
        item_checked=['Breadcrumbs','Restore Original','Drill Up','Drill Down']
        for i in range(len(item_checked)):
            Wf_admincons.verify_bihbox("#idInfoassistPropertiesPage", item_checked[i], 'checkbox', 'checked',"Step 10."+str(i)+" : Verify the following default settings for Auto Drill")
        Wf_admincons.verify_bihbox("#idInfoassistPropertiesPage", "Single Click Navigate", 'checkbox','unchecked', "Step 10.4 : Verify the following default settings for Chart Types")
        
        """
            Step 11 :Verify the following default settings for "Miscellaneous".
        """
        
        utillobj.mouse_scroll('down',10)
        item_checked=['Use two-part file name','Expand Data Source Tree','Join Tool','Layout Tab','Series Tab']
        for i in range(len(item_checked)):
            Wf_admincons.verify_bihbox("#idInfoassistPropertiesPage", item_checked[i], 'checkbox', 'checked',"Step 11."+str(i)+" : Verify the following default settings for Miscellaneous")
        
        """
            Step 12 :Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        self.driver.close()
        time.sleep(2)
        utillobj.switch_to_window(0)
        utillobj.infoassist_api_logout()
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()
        
