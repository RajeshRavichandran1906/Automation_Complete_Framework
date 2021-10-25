'''
Created on April 13, 2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7072&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2225413
Description = AHTML Report comment with CRLF,JavaScript Err occur(Project 88839)
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_pivot_comment
from common.lib import utillity

class C2225413_TestClass(BaseTestCase):

    def test_C2225413(self):

        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_piv= active_pivot_comment.Active_Pivot_Comment(self.driver)
        
        """ Step 1: Execute the AR-RP-001.fex            """
        utillobj.active_run_fex_api_login("AR-RP-001.fex", "S7072", 'mrid', 'mrpass')
        element_css="#MAINTABLE_wbody0 span[title='Move to Bottom'] img"
        utillobj.synchronize_with_number_of_element(element_css, expected_number=1, expire_time=30)
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', 'Step 01.1: Verified the Page Summary')
        column_list=['Category', 'Product','Product ID','State','Unit Sales','Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Verified Column Heading')
        utillobj.verify_data_set('ITableData0','I0r','AR-RP-001.xlsx','Step 01.3: Data set verified')
          
        """ Step 2: Click on report cell
                    Verify Context menu pop up is opened. That shows these sub menus: - Comments - Highlight Value - Highlight Row - Unhighlight All - Filter Cell
        """
        values = ['Comments', 'Highlight Value', 'Highlight Row', 'Unhighlight All', 'Filter Cell']
        miscelanousobj.verify_field_menu_items('ITableData0', 5, 5, values, 'Step 2: Verify Context menu pop up is opened with appropraite sub menus')
         
        """ Step 3: Click Comments option.
                    Add Comment pop up opened.
                    Add two line one after another
        """
        miscelanousobj.select_field_menu_items('ITableData0', 5, 5,'Comments')
        active_piv.create_comment('wall1', 'first line', 'second line')
        
        """ Step 4: Enter a commnet and click Add comment.
                    Verify '[*]' sign is displayed for the comment Verify on mouse over day, date and time along with comment is displayed. 
                    Add multiple comments and see all are displayed correctly.
        """
        miscelanousobj.verify_comment_field('ITableData0', 5, 5,'208756', 'Step 04: Verify Comment is added'  )    
        miscelanousobj.verify_comment_tooltip('ITableData0',5, 5,['first line', 'second line'], 'Step 04.1: Verify Comment tooltip for 208756' ) 
        miscelanousobj.verify_cell_property('ITableData0',5,5,'208756','Step 04.2: Verify cell ', bg_color='comment')

if __name__=='__main__' :
    unittest.main()