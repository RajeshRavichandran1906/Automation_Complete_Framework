'''
Created on Jan 18, 2018

@author: Robert

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10851
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/C2358899
TestCase Name = Navigating the Page Menu via Move Page Up option.
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, ia_resultarea, visualization_ribbon, active_miscelaneous
from common.lib import utillity

class C2358899_TestClass(BaseTestCase):

    def test_C2358899(self):
        """ TESTCASE VARIABLES """
        Test_Case_ID = 'C2358899'
        utillobj = utillity.UtillityMethods(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        miscobj=active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """    1. Upload the attached Multi_Page.fex to IA Document and Edit using IA Tool.    """
        
        utillobj.infoassist_api_edit('Multi_Page', 'document', 'P116/S10851_2', mrid='mrid', mrpass='mrpass')
        
        resultobj.wait_for_property("#Text_1", 1, expire_time=60)
        time.sleep(10)
        
        """    1.1 Expect to see the following IA preview panel.    """  
        ia_resultobj.verify_text_in_Textbox('#Text_1', "Global Filter for Multi-page Charts", 'Step 1.1a. Verify Textbox message')
          
        resultobj.verify_number_of_riser("TableChart_1", 1, 4, 'Step 1.1b: Verify the total number of risers displayed on Preview Chart')
        expected_xval_list=['Coffee : Capuccino', 'Coffee : Espresso']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        resultobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 1.1c: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 1.1d: Verify bar color")
        xaxis_value="Category : Product"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 1.1e(i): Verify X-Axis Title")
        leg_list=['Unit Sales','Dollar Sales']
        resultobj.verify_riser_legends("TableChart_1",leg_list , 'Step 1.1f Verify legends in the chart')
          
        
        """    2. Click the Page Options dialog box from the upper right corner, initially set at Page 1.    """
        """    2.1. Expect to see the following Page Option menu appear in the upper right of the canvas.    """
        
        list1=['Page 1', 'Page 2', 'New Page', 'Page Options...']
        ia_resultobj.select_or_verify_document_page_menu('Page 1',default_page_name='Page 1', verify=True, expected_popup_list=list1, msg='Step 2. Verify the default page')
        time.sleep(4)
        """    3. Click the last row, labeled 'Page Options'.    """
        """    3.1. Expect to see the following Page Options listing, containing Page 1 & Page 2.    """
        
         
        ia_resultobj.select_or_verify_document_page_menu('Page Options...')
        
        ia_resultobj.verify_document_page_options(page_list=['Page 1','Page 2'],msg="Step03: Verify Page option listings")
        
        """    4. Click the Page 1 row.    """
        
        ia_resultobj.select_page_in_document_page_options('Page 1',click_type='left')
        
        
        """    4.1. Expect to see the Page Option icons appear, including the down-arrow icon.    """
        movedown_btn="#moveDownBtn[class$='button button ']"
        moveup_btn="#moveUpBtn[class$='button-disabled']"
        delete_btn="#deletePageBtn[class$='button button ']"
        dup_btn="#duplicatePageBtn[class$='button button ']"
        rename_btn="#renamePageBtn[class$='button button ']"
         
        utillobj.verify_object_visible(movedown_btn, True, 'Step 4.1a. Verify Down button is enabled')
        utillobj.verify_object_visible(moveup_btn, True, 'Step 4.1b. Verify Up button is disabled')
        utillobj.verify_object_visible(delete_btn, True, 'Step 4.1c. Verify Delete button is enabled')
        utillobj.verify_object_visible(dup_btn, True, 'Step 4.1d. Verify Duplicate button is enabled')
        utillobj.verify_object_visible(rename_btn, True, 'Step 4.1e. Verify Rename button is enabled')
        
        time.sleep(5)
        
        """    5. Click the Move Down arrow.    """
        """    5.1. Expect to see the order of the pages reverse, with Page 2 first, then Page 1.    """
        
        ia_resultobj.select_actions_in_document_page_options('movedown')
        
        ia_resultobj.verify_document_page_options(page_list=['Page 2','Page 1'],msg="Step5.1: Verify Page option listing reversed",close_dialog_btn_name='ok')
        
        """    6. Click the OK button to save the change, then click run to test the Dashboard Page display order.    """
        utillobj.wait_for_object_not_visible("#pageOptionsDlg", 30, 'Step 6. Wait for Page options dialog to close')
        

        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=5)
        """    6.1. Expect to see the order of the Pages next to Layouts in the top reversed, with Page 2, then Page 1.    """
        pg_layouts_css="table[id='iLayTB$'] tbody td div[id^='iLay']"
        utillobj.synchronize_with_number_of_element(pg_layouts_css, 2, 30, pause_time=1)
        
        pg_layouts_css="table[id='iLayTB$'] tbody td div[id^='iLay']"
        exp_list=['Page 2', 'Page 1']
        
        iter_values=[val for val in (val.text.strip() for val in self.driver.find_elements_by_css_selector(pg_layouts_css))  if val != '']
        
        utillobj.as_List_equal(exp_list,iter_values,'Step 6.1 Verify Pages next to layouts in reverse order')
        
        """    6.2. Also expect to see the Page 2 report showing Budget Dollars.    """
        
        msg="Step 6.2"
        miscobj.verify_arChartToolbar("MAINTABLE_0",['More Options','Advanced Chart','Original Chart'],"Step 06a: Verify Chart toolbar")
        x_val_list=['Coffee : Ca...', 'Coffee : Es...', 'Coffee : Latte', 'Food : Biscotti', 'Food : Croi...', 'Food : Scone', 'Gifts : Coff...', 'Gifts : Coff...', 'Gifts : Mug', 'Gifts : The...']
        y_val_list=['0', '3M', '6M', '9M', '12M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_0', x_val_list, y_val_list, msg + ".b")
        xaxis_value="Category : Product"
        resultobj.verify_xaxis_title("MAINTABLE_0", xaxis_value, "Step 6.2d(i): Verify X-Axis Title")
        utillobj.verify_chart_color("MAINTABLE_0", "riser!s0!g2!mbar!", "bar_blue1", "Step 6.2e: Verify bar color")
        
        leg_list=['Budget Units','Budget Dollars']
        resultobj.verify_riser_legends("MAINTABLE_0",leg_list , 'Step 6.2f Verify legends in the chart')
        
        
        """    7. Click the Page 1 icon at the top of the Chart.    """
        
        
        self.driver.find_element_by_css_selector("table[id^='iLayTB'] tbody tr td:nth-child(3)").click()
        
        """    7.1. Do not save the changes made to the Page order.    """
        """    7.2. Expect to see the Page 1 report showing Dollar Sales.    """
        time.sleep(10)
        msg="Step 7.2"
        miscobj.verify_arChartToolbar("MAINTABLE_1",['More Options','Advanced Chart','Original Chart'],"Step 7.2a: Verify Chart toolbar")
        x_val_list=['Coffee : Ca...', 'Coffee : Es...', 'Coffee : Latte', 'Food : Biscotti', 'Food : Croi...', 'Food : Scone', 'Gifts : Coff...', 'Gifts : Coff...', 'Gifts : Mug', 'Gifts : The...']
        y_val_list=['0', '2M', '4M', '6M', '8M', '10M', '12M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_1', x_val_list, y_val_list, msg + ".b")
        xaxis_value="Category : Product"
        resultobj.verify_xaxis_title("MAINTABLE_1", xaxis_value, "Step 7.2d(i): Verify X-Axis Title")
        utillobj.verify_chart_color("MAINTABLE_1", "riser!s0!g2!mbar!", "bar_blue1", "Step 7.2e: Verify bar color")
        
        leg_list=['Unit Sales', 'Dollar Sales']
        resultobj.verify_riser_legends("MAINTABLE_1",leg_list , 'Step 7.2f Verify legends in the chart')
        
        utillobj.switch_to_default_content(pause=3)
        
        
if __name__ == '__main__':
    unittest.main()