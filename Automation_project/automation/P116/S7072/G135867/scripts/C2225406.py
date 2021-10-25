'''
Created on Feb 7, 2017

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7072
Test Case =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2225406
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,wf_mainpage, active_pivot_comment
from common.lib import utillity
import unittest,time
from selenium.webdriver.common.by import By



class C2225406_TestClass(BaseTestCase):

    def test_C2225406(self):
        
        driver = self.driver #Driver reference object created'
        utillobj = utillity.UtillityMethods(self.driver)
        miscellaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_piv=active_pivot_comment.Active_Pivot_Comment(self.driver)
        
        """
        Step 01: Execute the AR-RP-001.fex
        """
        utillobj.active_run_fex_api_login("AR-RP-001.fex", "S7072", 'mrid', 'mrpass')
        time.sleep(15)
        miscellaneousobj.verify_page_summary(0, '107of107records,Page1of2', 'Step 01.a: Verify the Page Summary 107 of 107 records')
        column_list=['Category', 'Product', 'Product ID', 'State', 'Unit Sales', 'Dollar Sales']
        miscellaneousobj.verify_column_heading('ITableData0', column_list, 'Step 01.b: Verify the column heading')
        
        utillobj.verify_data_set('ITableData0', 'I0r', 'AR-RP-001.xlsx','Step 01.c: Verify data set')
        time.sleep(5)
        
        """
        Step02: Click on report cell
        Verify Context menu pop up is opened. That shows these sub menus: - Comments - Highlight Value - Highlight Row - Unhighlight All - Filter Cell
        """
        values= ['Comments', 'Highlight Value', 'Highlight Row', 'Unhighlight All', 'Filter Cell']
        miscellaneousobj.verify_field_menu_items('ITableData0', 0, 5,values,"Step02: Verify field menu items")
        time.sleep(5)
        
        """
        Step03: Click Comments option.
        """
        miscellaneousobj.select_field_menu_items('ITableData0', 0, 5, 'Comments')
        time.sleep(8)
        
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
        Step05: Click any column heading dropdown menu.
        Verify Comments option is available in the menu option with two sub menus: (default state) - Expand - Hide Indicator.
        """
        browser=utillobj.parseinitfile('browser')
        if browser=='IE':
            option=['Sort Ascending', 'Sort Descending', 'Filter', 'Calculate', 'Chart', 'Rollup', 'Pivot (Cross Tab)', 'Hide Column', 'Grid Tool', 'Chart/Rollup Tool', 'Pivot Tool', 'Show Records', 'Comments', 'Send as E-mail', 'Save Changes', 'Export', 'Print', 'Window', 'Restore Original']
        else:
            option=['Sort Ascending', 'Sort Descending', 'Filter', 'Calculate', 'Chart', 'Rollup', 'Pivot (Cross Tab)', 'Hide Column', 'Grid Tool', 'Chart/Rollup Tool', 'Pivot Tool', 'Show Records', 'Comments', 'Export', 'Print', 'Window', 'Restore Original']
        miscellaneousobj.verify_menu_items('ITableData0',3,None,option,'Step 05: Verify Filter menu')
        
        """
        Step06: Click Hide Indicator option.
        Verify report shows the complete comment.
        """
        time.sleep(4)
        miscellaneousobj.select_menu_items('ITableData0', 0, 'Comments','Hide Indicator')
        time.sleep(5)
        miscellaneousobj.verify_cell_property('ITableData0',0,5,'586298','Step 06: Verify cell color',bg_color='white')
        
        """
        Step07: Click Hide Indicator option again.
        Verify report hides the comment and shows the '[*]' sign.
        """
        time.sleep(4)
        miscellaneousobj.select_menu_items('ITableData0', 0, 'Comments','Hide Indicator')
        time.sleep(5)
        miscellaneousobj.verify_comment_field('ITableData0', 0, 5,'586298', 'Step07: Verify Comment is added'  )    
        miscellaneousobj.verify_comment_tooltip('ITableData0',0, 5,['comments added'], 'Step07: Verify Comment tooltip for 586298' ) 
         
        miscellaneousobj.verify_cell_property('ITableData0',0,5,'586298','Step07: Verify cell color',bg_color='comment')
          
if __name__ == '__main__':
    unittest.main()  
                       
        