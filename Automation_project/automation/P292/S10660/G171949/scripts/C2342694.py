'''
Created on July 25, 2019

@author: AA14564
Testcase Name : Testing URL for PD
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2336447
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
from common.wftools.wf_mainpage import Wf_Mainpage
from common.wftools.login import Login
from common.wftools.report import Report
from common.pages.ia_miscelaneous import IA_Miscelaneous

class C2342694_TestClass(BaseTestCase):

    def test_C2342694(self):
        
        """ TESTCASE OBJECT'S  """
        utillobj = utillity.UtillityMethods(self.driver)
        login = Login(self.driver)
        report = Report(self.driver)
        wf_mainpage_obj = Wf_Mainpage(self.driver)
        IA_Miscelaneous_obj = IA_Miscelaneous(self.driver)
          
        """ TESTCASE VARIABLES  """
          
        folder_path_content  = "P292_S10660/~autodevuser40"
          
        Step1 = """
        Step 1:Invoke WF Home Page as Developer user.
        """
        Step2 = """
        Step 2:Create a new report using car.mas file under P292_S10660/MyContent using the below URL,
        http://host:port/alias/ia?item=IBFS%3A%2FWFC%2FRepository%2FP292_S10660%2F~autodevuser40&tool=report&master=car
        IA tool opens.
        """
         
        IA_Miscelaneous_obj.invoke_ia_tool_using_api_(master ='car',mrid='mriddev',mrpass='mrpassdev',folder_path=folder_path_content)
        utillobj.synchronize_with_visble_text("#queryViewPane",'COUNTRY',120)
        utillobj.capture_screenshot("01.01",Step1)
        utillobj.capture_screenshot("02.01",Step2)
         
        Step3 = """Step 3:Add the following fields,
       'COUNTRY', 'CAR' , 'MODEL' columns from Dimensions and 'Seats' from Measures       
        Verify,
        """
        report.double_click_on_datetree_item("COUNTRY")
        utillobj.synchronize_with_visble_text("#singleReportLayout",'COUNTRY',120)
        report.double_click_on_datetree_item("CAR")
        utillobj.synchronize_with_visble_text("#singleReportLayout",'CAR',120)
        report.double_click_on_datetree_item("MODEL")
        utillobj.synchronize_with_visble_text("#singleReportLayout",'MODEL',120)
        report.double_click_on_datetree_item("SEATS")
        utillobj.synchronize_with_visble_text("#singleReportLayout",'SEATS',120)
        utillobj.capture_screenshot("03.01",Step3,expected_image_verify=True)
         
        Step4 ="""
        Step 4:Save the report as "Test_report".
        """
         
        report.save_as_from_application_menu_item("Test_report")
        utillobj.capture_screenshot("04.01",Step4)
  
        Step5 = """
        Step 5:Run the report within IA.
        """
        report.run_report_from_toptoolbar()
        utillobj.capture_screenshot("05.01",Step5)
         
        Step6 = """
        Step 6:Click IA button on the top left >> Click Exit.
        """
        report.api_logout()
        utillobj.capture_screenshot("06.01",Step6)
         
        Step7 ="""
        Step 7:Using the below URL run the report 'Test_report.fex' under P292_S10660/MyContent
        http://host:port/alias/rs/ibfs/WFC/Repository/P292_S10660/~autodevuser40/Test_report.fex?IBIRS_action=run
        Verify report ran successfully,
        """
        IA_Miscelaneous_obj.run_fex_using_api(folder_path_content, fex_name='Test_report', mrid='mriddev',mrpass='mrpassdev')
        #report.create_table_data_set("table[summary='Summary']","c2342694.xlsx")
        report.verify_html_report_dataset("c2342694.xlsx", msg="Step7")
        utillobj.capture_screenshot("07.01",Step7,expected_image_verify=True)
         
        step8 ="""
        Step 8:Right click on the 'Test_report.fex' >> Select Share option from context menu.
         Verify Share icon is present for 'Test_report.fex'.
        """
        report.api_logout()
        login.invoke_home_page('mriddev', 'mrpassdev')
        wf_mainpage_obj.expand_repository_folder('P292_S10660->My Content')
        utillobj.synchronize_with_visble_text('.content-box','Test_report',120)
        wf_mainpage_obj.right_click_folder_item_and_select_menu('Test_report','Share')
        time.sleep(2)
        utillobj.capture_screenshot("08.01",step8,expected_image_verify=True)
        
        Step9 = """
        Step 9:In the banner link, click on the top right username > Sign Out.
        """
        wf_mainpage_obj.signout_from_username_dropdown_menu()
        utillobj.capture_screenshot("09.01",Step9)
 
        step10 ="""
        Step 10:Invoke WF Home Page as Advanced user.
        """
        login.invoke_home_page('mridadv', 'mrpassadv')
        utillobj.capture_screenshot("10.01",step10)

        step11 ="""
        Step 11:Under Domain tree, Navigate to P292_S10660/Shared Content/autodevuser40.
        Verify shared item is available,
        """
        wf_mainpage_obj.expand_repository_folder('P292_S10660->Shared Content->autodevuser40')
        wf_mainpage_obj.verify_items_in_grid_view(['Test_report'], "asin", msg="Step:11")
        utillobj.capture_screenshot("11.01",step11,expected_image_verify=True)
        
        """
        Step 12:In the banner link, click on the top right username > Sign Out.
        """

 
if __name__=='__main__' :
    unittest.main()
    