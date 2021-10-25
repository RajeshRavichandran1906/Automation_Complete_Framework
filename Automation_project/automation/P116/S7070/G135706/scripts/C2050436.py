'''
Created on Aug 10, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7070&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050436
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_pivot_comment
from common.lib import utillity
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class C2050436_TestClass(BaseTestCase):

    def test_C2050436(self):
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        pivot_commentobj = active_pivot_comment.Active_Pivot_Comment(self.driver)

        """
        1. Execute the AHTML_report.fex
        """
        utillobj.active_run_fex_api_login("AHTML_Report.fex", "S7070", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', 'Step 01.1: Execute the AHTML_report.fex and Verify the Report Heading')
        column_list=['Category', 'Product', 'Product ID', 'State', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Execute the AHTML_report.fex and Verify the column heading')
        """
        Step 02: From any dropdown for State, select Sort descending
        """
        miscelanousobj.select_menu_items('ITableData0', 3, 'Sort Descending')
        
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2050436_Ds01.xlsx','Step 02: Expect to the report sorted in Descending State order')
        
        """
        Step 03: Left click on the last row of the WA State group.
        """
        
        values = ['Comments', 'Highlight Value', 'Highlight Row', 'Unhighlight All', 'Filter Cell']
        miscelanousobj.verify_field_menu_items('ITableData0', 106, 3,values,'Step 03: Expect to see Active row options')
        
        """
        Step 04: Click on the Comment option. 
        """
        miscelanousobj.select_field_menu_items('ITableData0', 106, 3, 'Comments',original_rownum=9)
        
        try:
            comment_field=self.driver.find_element(By.XPATH,"//span[contains(text(),'Add Comment')]").is_displayed()
            utillity.UtillityMethods.asequal(self,True,comment_field,'Step 04: Expect to see the Comment text window appear')
        except NoSuchElementException:
            print("Step 04: Expect to see the Comment text window appear - Failed")
        
        """
        Step 05: Add comment as "Comment on last WA State row." in the editor.
        Click the Add Comment button.
        """

        pivot_commentobj.create_comment('wall1','Comment on last WA State row.')
            
        """
        Step 06: Back I the report, select Sort Ascending for the Unit Sales field.
        """
        
        miscelanousobj.select_menu_items('ITableData0', 4, 'Sort Ascending')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2050436_Ds02.xlsx','Step 06: Expect to see the report sorted in Ascending Unit Sales order')
        miscelanousobj.verify_comment_field('ITableData0', 106, 3, 'WA', 'Step 06: Verify commented field')
        
        """
        Step 07: Verify the Comment text by left-clicking on the highlighted row and selecting Comments again.
        """
        miscelanousobj.select_field_menu_items('ITableData0', 106, 3, 'Comments',original_rownum=17)
        utillobj.synchronize_until_element_is_visible('#wall1',miscelanousobj.home_page_long_timesleep)
        pivot_commentobj.verify_comment('wall1', '1', 'Comment on last WA State row.', 'Step 07: Expect to see the text entered in step 5')
        
        
if __name__ == '__main__':
    unittest.main()
    
    
    
    
    
    
    
    