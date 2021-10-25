'''
Created on Dec 06, 2017

@author: PM14587
Testcase Name : Verify Excel Formula request
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2227584
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon,ia_ribbon
from common.lib import utillity

class C2227584_TestClass(BaseTestCase):

    def test_C2227584(self):
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID = 'C2227584'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaribbon=ia_ribbon.IA_Ribbon(self.driver)
         
        """
            Step 01 : Launch IA Report mode: http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','baseapp/CAR','P292/S10032_infoassist_4', 'mrid', 'mrpass')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(2)", 1,60,string_value='Sum')
        time.sleep(3)
        
        """
            Step 02 :Double click "CAR", "SEATS", "SALES".
        """
        metaobj.datatree_field_click('CAR',2,1)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(4)", 1,20,string_value='CAR')
              
        metaobj.datatree_field_click('SEATS',2,1)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(3)", 1,20,string_value='SEATS')
             
        metaobj.datatree_field_click('SALES',2,1)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(4)", 1,20,string_value='SALES')
        time.sleep(2)
        
        """
            Step 03 : Select "Home" tab > Click "HTML" dropdown
            Step 04 : Select "Excel(xlsx)" > "Excel Formula(xlsx)"
        """
        iaribbon.select_or_verify_output_type(launch_point='Home',item_select_path='Excel (xlsx)->Excel Formula (xlsx)')
        time.sleep(2)
         
        """
            Step 05 : Click "Run".
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        
        """
            Step 06 : Verify excel file is downloaded in a new window.
            Step 07 : Click on downloaded file.
            Step 08 : Verify it displays the data in Excel.
        """
        browser=utillobj.parseinitfile('browser') 
        if browser=='Chrome' :
            utillobj.save_window(Test_Case_ID+'_Actual_DataSet_01')
            time.sleep(5)
            utillobj.create_excel(Test_Case_ID+'_Actual_DataSet_01.xls',Test_Case_ID+'_Actual_DataSet_01.xlsx', pyautogui_save=True)
        else :
            utillobj.saveas_excel_sheet(Test_Case_ID+'_Actual_DataSet_01_.xlsx')
        time.sleep(4)
        utillobj.verify_excel_sheet(Test_Case_ID+'_Base_DataSet_01.xlsx', Test_Case_ID+'_Actual_DataSet_01.xlsx', 'Report1', 'Step 08 : Verify it displays the data in Excel')
        time.sleep(4)
        a = self.driver.window_handles
        print('before_switch:', a)
        if len(a) == 2:
            utillobj.switch_to_main_window()
            b = self.driver.window_handles
            print('after_switch:', b)
        
        """
            Step 09 : Dismiss Excel.
            Step 10 : Click "IA" > "Save".
            Step 11 : Enter Title = "C2227584".
            Step 12 : Click "Save".
        """
        time.sleep(4)
        utillobj.synchronize_with_number_of_element('#applicationButton img', 1, 20)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        
        """
            Step 13 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
        """
            Step 14 : Reopen saved FEX: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2227584.fex&tool=Report
        """
        utillobj.infoassist_api_edit(Test_Case_ID,'report','P292/S10032_infoassist_4',mrid='mrid', mrpass='mrpass')
        resultobj.wait_for_property("#HomeFormatType>div[id^='BiLabel']", 1,80,string_value='Excel Formula (xlsx)')
        time.sleep(3)
        
        """
            Step 15 : Verify "Excel Formula(xlsx)" is the selected format
        """
        utillobj.verify_element_text("#HomeFormatType>div[id^='BiLabel']",'Excel Formula (xlsx)','Step 15 : Verify "Excel Formula(xlsx)" is the selected format"')
        
        """
            Step 16 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(5)
        
if __name__=='__main__' :
    unittest.main()