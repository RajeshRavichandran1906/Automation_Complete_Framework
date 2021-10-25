'''
Created on Jan 8, 2019

@author: AA14564

Testsuite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/20311&group_by=cases:section_id&group_id=517177&group_order=asc
Testcase id=http://172.19.2.180/testrail/index.php?/cases/view/6733517
TestCase Name = Verify hide indicator option does not show comments
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.wftools.active_report import Active_Report
from common.lib.core_utility import CoreUtillityMethods
from common.lib.utillity import UtillityMethods

class C6733517_TestClass(BaseTestCase):

    def test_C6733517(self):
        
        """
            TESTCASE VARIABLES
        """
        active_rpt_obj = Active_Report(self.driver)
        core_utilobj = CoreUtillityMethods(self.driver)
        utilobj = UtillityMethods(self.driver)
        project_id = core_utilobj.parseinitfile('project_id')
        suite_id = core_utilobj.parseinitfile('suite_id')
        group_id = core_utilobj.parseinitfile('group_id')
        folder_path = '{0}_{1}/{2}'.format(project_id, suite_id, group_id)
        page_load_css = '#ITableData0 tr:nth-child(3) td:nth-child(5)'
        case_id = 'C6733516'
        
        """
        Step 1: Execute the AR-RP-001.fex
        """
        active_rpt_obj.run_active_report_using_api('AR-RP-001.fex', column_css=page_load_css, synchronize_visible_element_text='22482', repository_path=folder_path)
        active_rpt_obj.verify_page_summary(0, '107of107records,Page1of2', 'Step 1: Verify the Page Summary 107 of 107 records')
        active_rpt_obj.verify_active_report_dataset(case_id+'.xlsx', 'Step 1.1: Verify data set', table_css="#ITableData0")
        
        """
        Step 2: Click on report cell
                Verify Context menu pop up is opened. That shows these sub menus: 
                - Comments 
                - Highlight Value 
                - Highlight Row 
                - Unhighlight All 
                - Filter Cell
        """
        expected_value=['Comments','Highlight Value','Highlight Row','Unhighlight All','Filter Cell']
        active_rpt_obj.verify_field_menu_options(expected_value, 'Step 04.1: Verify the report is generated', rownum=19, colnum=5)
        
        """
        Step 3: Click Comments option.
                Add Comment pop up opened.
        """
        active_rpt_obj.select_option_from_field_menu('Comments', rownum=9, colnum=5)
        active_rpt_obj.verify_comment_window('Step 3: veirfy Add Comment pop up opened.')
        
        """
        Step 4: Enter a comment and click Add comment.
                Verify '[*]' sign is displayed for the comment Verify on mouse over day, date and time along with comment is displayed. Add multiple comments and see all are displayed correctly.
        """
        active_rpt_obj.enter_text_on_comment_dialog('comments added')
        active_rpt_obj.verify_comment_field('Step 4: Verify Comment is added', rownum=9, colnum=5)
        active_rpt_obj.verify_comment_tooltip(['comments added'], 'Step 4.1: Verify Comment tool-tip.', rownum=9, colnum=5)
        
        """
        Step 5: Click any column heading dropdown menu.
                Verify Comments option is available in the menu option with two sub menus: (default state) - Expand - Hide Indicator.
        """
        active_rpt_obj.verify_menu_items('ITableData0', 0, None, 'Comments', 'Step 5: Verify Comments option is available in the menu option.', all_items='no')
        active_rpt_obj.verify_menu_items('ITableData0', 5, 'Comments', 'Expand', 'Step 5.1: Verify Comments option Expand is available in the menu option.', all_items='no')
        active_rpt_obj.verify_menu_items('ITableData0', 5, 'Comments', 'Hide Indicator', 'Step 5.2: Verify Comments option Hide Indicator is available in the menu option.', all_items='no')
        
        """
        Step 6: Click Hide Indicator option.
                Verify report does not show '[*]' sign.
        """
        active_rpt_obj.select_menu_items('ITableData0', 4, 'Comments','Hide Indicator')
        time.sleep(2)
        try:
            active_rpt_obj.verify_comment_tooltip([''], 'Step 6: Verify Comment tool-tip.', rownum=9, colnum=5)
            utilobj.asequal('', 'comments added', "Step 6.1: Verify report show '[*]' sign.")
        except AttributeError:
            utilobj.asequal('', '', "Step 6.1: Verify report does not show '[*]' sign.")
        
        """
        Step 7: Click Hide Indicator option again.
                Verify report hides the comment and shows the '[*]' sign.
        """
        active_rpt_obj.select_menu_items('ITableData0', 4, 'Comments','Hide Indicator')
        time.sleep(2)
        active_rpt_obj.verify_comment_field('Step 7: Verify Comment is added', rownum=9, colnum=5)
        active_rpt_obj.verify_comment_tooltip(['comments added'], 'Step 7.1: Verify Comment tool-tip.', rownum=9, colnum=5)
        

if __name__ == '__main__':
    unittest.main()