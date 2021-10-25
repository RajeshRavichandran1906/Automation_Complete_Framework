'''
Created on Feb 7, 2017

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7072
Test Case =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2225407
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_pivot_comment
from common.lib import utillity
import unittest

class C2225407_TestClass(BaseTestCase):

    def test_C2225407(self):
        utillobj = utillity.UtillityMethods(self.driver)
        miscellaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_piv=active_pivot_comment.Active_Pivot_Comment(self.driver)
        
        """
        Step 01: Execute the AR-RP-001.fex
        """
        utillobj.active_run_fex_api_login("AR-RP-001.fex", "S7072", 'mrid', 'mrpass')
        miscellaneousobj.verify_page_summary(0, '107of107records,Page1of2', 'Step 01.a: Verify the Page Summary 107 of 107 records')
        column_list=['Category', 'Product', 'Product ID', 'State', 'Unit Sales', 'Dollar Sales']
        miscellaneousobj.verify_column_heading('ITableData0', column_list, 'Step 01.b: Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', 'AR-RP-001.xlsx','Step 01.c: Verify data set')
        
        """
        Step02: Click on report cell
        Verify Context menu pop up is opened. That shows these sub menus: - Comments - Highlight Value - Highlight Row - Unhighlight All - Filter Cell
        """
        values= ['Comments', 'Highlight Value', 'Highlight Row', 'Unhighlight All', 'Filter Cell']
        miscellaneousobj.verify_field_menu_items('ITableData0', 0, 5,values,"Step02: Verify field menu items")
        
        """
        Step03: Click Comments option.
        """
        miscellaneousobj.select_field_menu_items('ITableData0', 0, 5, 'Comments')
        
        """
        Step04: Enter a commnet and click Add comment.
        Verify '[*]' sign is displayed for the comment Verify on mouse over day, date and time along with comment is displayed. 
        """
        active_piv.create_comment('wall1', 'comments added')        
        """In the report, ENGLAND is highlighted, and a Comment Indicator appears next to it."""  
        miscellaneousobj.verify_comment_field('ITableData0', 0, 5,'586298', 'Step 04: Verify Comment is added'  )    
        miscellaneousobj.verify_comment_tooltip('ITableData0',0, 5,['comments added'], 'Step 07: Verify Comment tooltip for 586298' ) 
        miscellaneousobj.verify_cell_property('ITableData0',0,5,'586298','Step 05: Verify cell color',bg_color='comment')
        
        """
        Step05: Click Comments option
        """
        miscellaneousobj.select_field_menu_items('ITableData0', 0, 5, 'Comments')
        
        """
        Step06: Click comment option again and click delete button for the previous comment, click Close 'X'.
        Verify deleted comment is no longer visible under the box.
        """
        active_piv.delete_comment('wall1', '1')
        active_piv.close_comment_dialog()
        miscellaneousobj.verify_cell_property('ITableData0',0,5,'586298','Step 06: Verify cell color',bg_color='white')
        
if __name__ == '__main__':
    unittest.main()  
                       
        