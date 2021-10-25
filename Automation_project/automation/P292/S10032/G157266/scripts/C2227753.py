'''
Created on Feb 05, 2018

@author: Praveen Ramkumar/Updated by : Bhagavathi

Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227753
TestCase Name = Report Other: Verify that comments under Context menu may be added, expanded and deleted.
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, ia_run ,active_pivot_comment
from common.lib import utillity
from common.wftools import active_report

class C2227753_TestClass(BaseTestCase):

    def test_C2227753(self):
        
        """
            TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        pivot=active_pivot_comment.Active_Pivot_Comment(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        fex_name="AHTML_001.fex"
        
        def move_away_from_table():
            table=self.driver.find_element_by_id('TCOL_0_C_0')
            utillobj.default_click(table, 0)
            time.sleep(2)
        
        """
            Step 01 : Sign in to WebFOCUS as a Basic user http://machine:port/{alias}
            Step 02 :Expand folder P292_S10032_G157266Execute the following URL:
            http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10032_G157266%252FAHTML_OFF&BIP_item=AHTML_001.fex
        """
        
        active_reportobj.run_active_report_using_api(fex_name, column_css="#ITableData0 #TCOL_0_C_0 span", synchronize_visible_element_text="COUNTRY")
        
        """
            Step 03 : Verify the report is generated
        """        
        miscelanousobj.verify_page_summary('0','5of5records,Page1of1','Step 03.1 : Verify page summary')
#         iarun.create_table_data_set('#ITableData0', 'AHTML_001.xlsx')
        iarun.verify_table_data_set('#ITableData0', 'AHTML_001.xlsx', 'Step 03.2 : Verify the report is generated', desired_no_of_rows=5)
        
        """
            Step 04:Right click on report body under Country column for ENGLAND
                    Verify Context menu pop up is opened. That shows these sub menus:
                    - Commnets
                    - Highlight Value
                    - Highlight Row
                    - Unhighlight All
                    - Filter Cell
            Step 05:Click Comments option Add Comment pop up opened.
        """
        expected_value=['Comments','Highlight Value','Highlight Row','Unhighlight All','Filter Cell']
        miscelanousobj.verify_field_menu_items('ITableData0', 0, 0, expected_value, 'Step 04.1: Verify the report is generated')
        miscelanousobj.select_field_menu_items('ITableData0', 0, 0, 'Comments')
        move_away_from_table()
        
        """
            Step 06 : Enter 'Sample Comment for this test.' into the Comment Text Box and click Add comment.
            Left click on England and select the Comments option again.
            Verify the presence of a 'cloud-like' symbol and that England is highlighted.
            Verify on opening up comments, day, date and time along with comment is displayed.
            Verify on mouse over, comment details are displayed and the row data for England is highlighted.
        """
        
        pivot.create_comment("wall1","Sample Comment for this test.")
        css="table[id='ITableData0'] tr[id*='r0.'] td[id$='C0'] > div > span img"
        utillobj.verify_object_visible(css, True, 'Step 06.1:verify cloud-like symbol')
        miscelanousobj.select_field_menu_items('ITableData0', 0, 0, 'Comments')
        pivot.verify_comment("wall1",  '1', 'Sample Comment for this test.', 'Step 06.2: Expect to see the text entered in step 5')
        pivot.close_comment_dialog()
        miscelanousobj.verify_comment_tooltip('ITableData0', 0, 0,['Sample Comment for this test'],"Step 6.3: Verify tooltip comment")
        
        """
            Step 07 :From the dropdown for Country, click the Comments option, then select Expand.
            Expect to see the following report, now with the comment inserted after the England row of data.
        """
        
        miscelanousobj.select_menu_items('ITableData0', 0, 'Comments', 'Expand')
#         iarun.create_table_data_set('#ITableData0', 'AHTML_002.xlsx')
        iarun.verify_table_data_set('#ITableData0', 'AHTML_002.xlsx', 'Step 07.1 : Verify the report is generated',starting_rownum=2, desired_no_of_rows=5)
        
        """
            Step 08:From the dropdown for Country, click the Comments option, then select Expand to remove the Comments as a row.
            Click the Comments and select Hide Indicator.
            Expect to see the Comments removed as a row of data under England.Also expect to see the comment 'cloud-like' indicator removed.
        """
        miscelanousobj.select_menu_items('ITableData0', 0, 'Comments', 'Expand')
        miscelanousobj.select_menu_items('ITableData0', 0, 'Comments', 'Hide Indicator')
        
#         iarun.create_table_data_set('#ITableData0', 'AHTML_003.xlsx')
        iarun.verify_table_data_set('#ITableData0', 'AHTML_003.xlsx', 'Step 08.1 : Verify the report is generated', desired_no_of_rows=5)
        css="table[id='ITableData0'] tr[id*='r0.'] td[id$='C0'] > div > span img"
        utillobj.verify_object_visible(css, False, 'Step 06.1:verify cloud-like symbol')
        
        """
            Step 09:Dismiss the window and logout.http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
if __name__=='__main__' :
    unittest.main()
        