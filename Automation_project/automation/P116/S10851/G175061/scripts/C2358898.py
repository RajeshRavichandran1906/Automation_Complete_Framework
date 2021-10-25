'''
Created on Jan 18, 2018

@author: Robert

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/C2358898
TestCase Name = Navigating the Page Menu via Move Page Down option.
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, ia_resultarea, visualization_ribbon, active_miscelaneous, ia_run
from common.lib import utillity

class C2358898_TestClass(BaseTestCase):

    def test_C2358898(self):
        """ TESTCASE VARIABLES """
        Test_Case_ID = 'C2358898'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        miscobj=active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_runobj=ia_run.IA_Run(self.driver)
        
        """    1. Create a new Document using GGSALES master file and add a text box with the text inside "Global Filter for Multi-page Charts    """
#         utillobj.infoassist_api_edit('C2358898', 'document', 'P116/S10851_1', mrid='mrid', mrpass='mrpass')
        utillobj.infoassist_api_login('document','ibisamp/ggsales','P116/S10851_1', 'mrid', 'mrpass')
        utillobj.wait_for_page_loads(20)
        resultobj.wait_for_property("#iaCanvasCaptionLabel", 1, expire_time=35, string_value='Document')
        ribbonobj.select_ribbon_item("Insert", "text_box")
        time.sleep(5)
        ribbonobj.resizing_document_component('0.3', '3')
        time.sleep(5)
        ribbonobj.repositioning_document_component('4', '0.5')
        utillobj.synchronize_with_number_of_element("#Text_1", 1, 25)    
        ia_resultobj.enter_text_in_Textbox('Text_1', "Global Filter for Multi-page Charts")
           
        """    2.1. Insert -> Chart then add category, product, unit sales and dollar sales fields    """
        ribbonobj.select_ribbon_item("Insert", "Chart")
        time.sleep(5)
        resultobj.wait_for_property("#TableChart_1", 1, expire_time=20)
        metaobj.datatree_field_click("Category", 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click("Product", 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click("Unit Sales", 2, 1)
        time.sleep(5)  
        metaobj.datatree_field_click("Dollar Sales", 2, 1)
        time.sleep(5)
        ribbonobj.repositioning_document_component('1', '2')
        
        """    2.2. Expect to see the following chart with text box control inside the canvas    """
        utillobj.synchronize_with_number_of_element("#Text_1", 1, 25) 
        ia_resultobj.verify_text_in_Textbox('#Text_1', "Global Filter for Multi-page Charts", 'Step 2.2. Verify Textbox message')
        resultobj.verify_number_of_riser("TableChart_1", 1, 4, 'Step 2.2a: Verify the total number of risers displayed on Preview Chart')
        expected_xval_list=['Coffee : Capuccino', 'Coffee : Espresso']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        resultobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 2.2b: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 2.2c: Verify bar color")
        xaxis_value="Category : Product"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 2.2d(i): Verify X-Axis Title")
        leg_list=['Unit Sales','Dollar Sales']
        resultobj.verify_riser_legends("TableChart_1",leg_list , 'Step 2.2e Verify legends in the chart')
           
        """    3. To add another page select Insert tab, in the Pages group Page 2, is inserted after the current page, and appears on the canvas    """
        self.driver.find_element_by_css_selector("#iaPagesMenuBtn div[class$='tool-bar-menu-button-drop-down-arrow']").click()
        list1=['Page 1', 'New Page', 'Page Options...']
        utillobj.select_or_verify_bipop_menu('Page 1',verify='true',expected_popup_list=list1,msg='Step 3. Verify the items in page group')
        self.driver.find_element_by_css_selector("#iaCanvasCaptionLabel").click()
        time.sleep(4)
        ia_resultobj.select_or_verify_document_page_menu('New Page')
        time.sleep(10)
           
        """    4. Insert -> Chart then add category, product, budget units and budget dollars    """
        ribbonobj.select_ribbon_item("Insert", "Chart")
        time.sleep(5)
        resultobj.wait_for_property("#TableChart_2", 1, expire_time=20)
        metaobj.datatree_field_click("Category", 2, 1)
        time.sleep(5)   
        metaobj.datatree_field_click("Product", 2, 1)
        time.sleep(5)  
        metaobj.datatree_field_click("Budget Units", 2, 1)
        time.sleep(5)   
        metaobj.datatree_field_click("Budget Dollars", 2, 1)
        time.sleep(5)
        ribbonobj.repositioning_document_component('1', '2')
           
        """    4.1. Expect to see the following chart in the canvas    """
        resultobj.verify_number_of_riser("TableChart_2", 1, 4, 'Step 4.1a: Verify the total number of risers displayed on Preview Chart')
        expected_xval_list=['Coffee : Capuccino', 'Coffee : Espresso']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        resultobj.verify_riser_chart_XY_labels('TableChart_2', expected_xval_list, expected_yval_list, 'Step 4.1b: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("TableChart_2", "riser!s0!g0!mbar!", "bar_blue1", "Step 4.1c: Verify bar color")
        xaxis_value="Category : Product"
        resultobj.verify_xaxis_title("TableChart_2", xaxis_value, "Step 4.1d(i): Verify X-Axis Title")
        leg_list=['Budget Units','Budget Dollars']
        resultobj.verify_riser_legends("TableChart_2",leg_list , 'Step 4.1e Verify legends in the chart')
         
        """    5. Click the Page Options dialog box from the upper right corner, initially set at Page 1.    """
        """    5.1. Expect to see the following Page Option menu appear in the upper right of the canvas.    """
        list1=['Page 1', 'Page 2', 'New Page', 'Page Options...']
        ia_resultobj.select_or_verify_document_page_menu('Page 1',default_page_name='Page 2', verify=True, expected_popup_list=list1, msg='Step 5. Verify the default page')
        time.sleep(4)
         
        """    6. Click the last row, labeled 'Page Options'.    """
        ia_resultobj.select_or_verify_document_page_menu('Page Options...')
         
        """    6.1. Expect to see the following Page Options listing, containing Page 1 & Page 2.    """
        explist=['Page 1', 'Page 2']
        ia_runobj.verify_active_dashboard_prompts('listbox', '#iaPageList', explist, 'Step 6.1 Verify the page options list', default_selected_check=None)
        utillobj.switch_to_default_content(pause=3)
         
        """    7. Click the Page 2 row.    """
        sel_list=['Page 2']
        ia_runobj.select_active_dashboard_prompts('listbox', '#iaPageList', sel_list, scroll_down_times=0)
         
        """    7.1. Expect to see the Page Option icons appear, including the up-arrow icon.    """
        movedown_btn="#moveDownBtn[class$='button-disabled']"
        moveup_btn="#moveUpBtn[class$='button button ']"
        delete_btn="#deletePageBtn[class$='button button ']"
        dup_btn="#duplicatePageBtn[class$='button button ']"
        rename_btn="#renamePageBtn[class$='button button ']"
        utillobj.verify_object_visible(movedown_btn, True, 'Step 7.1a. Verify Down button is disabled')
        utillobj.verify_object_visible(moveup_btn, True, 'Step 7.1b. Verify Up button is enabled')
        utillobj.verify_object_visible(delete_btn, True, 'Step 7.1c. Verify Delete button is enabled')
        utillobj.verify_object_visible(dup_btn, True, 'Step 7.1d. Verify Duplicate button is enabled')
        utillobj.verify_object_visible(rename_btn, True, 'Step 7.1e. Verify Rename button is enabled')
        time.sleep(5)
         
        """    8. Click the Move Up arrow.    """
        """    8.1. Expect to see the order of the pages reverse, with Page 2 first, then Page 1.    """
        moveup_ele=self.driver.find_element_by_css_selector(moveup_btn)
        utillobj.click_on_screen(moveup_ele, coordinate_type='middle', click_type=2)
        time.sleep(5)
        explist=['Page 2', 'Page 1']
        ia_runobj.verify_active_dashboard_prompts('listbox', '#iaPageList', explist, 'Step 8.1 Verify the page options new order list', default_selected_check=None)
         
        """    9. Click the OK button to save the change, then click run to test the Dashboard Page display order.    """
        self.driver.find_element_by_css_selector("#pageOptionsOkBtn").click()
        time.sleep(10)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        utillobj.switch_to_frame()
        
        """    9.1. Expect to see the order of the Pages next to Layouts in the top reversed, with Page 2, then Page 1.    """
        pg_layouts_css="table[id='iLayTB$'] tbody td div[id^='iLay']"
        exp_list=['Page 2', 'Page 1']
        iter_values=[val for val in (val.text.strip() for val in self.driver.find_elements_by_css_selector(pg_layouts_css))  if val != '']
        utillobj.as_List_equal(exp_list,iter_values,'Step 9.1 Verify Pages next to layouts in reverse order')
        
        """    9.2. Also expect to see the Page 2 report showing Budget Dollars.    """
        msg="Step 9.2"
        miscobj.verify_arChartToolbar("MAINTABLE_0",['More Options','Advanced Chart','Original Chart'],"Step 09a: Verify Chart toolbar")
        x_val_list=['Coffee : Ca...', 'Coffee : Es...', 'Coffee : Latte', 'Food : Biscotti', 'Food : Croi...', 'Food : Scone', 'Gifts : Coff...', 'Gifts : Coff...', 'Gifts : Mug', 'Gifts : The...']
        y_val_list=['0', '3M', '6M', '9M', '12M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_0', x_val_list, y_val_list, msg + ".b")
        xaxis_value="Category : Product"
        resultobj.verify_xaxis_title("MAINTABLE_0", xaxis_value, "Step 9.2d(i): Verify X-Axis Title")
        utillobj.verify_chart_color("MAINTABLE_0", "riser!s0!g2!mbar!", "bar_blue1", "Step 9.2e: Verify bar color")
        leg_list=['Budget Units','Budget Dollars']
        resultobj.verify_riser_legends("MAINTABLE_0",leg_list , 'Step 9.2f Verify legends in the chart')
        
        """    10. Click the Page 1 icon at the top of the Chart.    """
        self.driver.find_element_by_css_selector("table[id^='iLayTB'] tbody tr td:nth-child(3)").click()
        
        """    10.1. Do not save the changes made to the Page order.    """
        """    10.2. Expect to see the Page 1 report showing Dollar Sales.    """
        time.sleep(10)
        msg="Step 10.2"
        miscobj.verify_arChartToolbar("MAINTABLE_1",['More Options','Advanced Chart','Original Chart'],"Step 10.2a: Verify Chart toolbar")
        x_val_list=['Coffee : Ca...', 'Coffee : Es...', 'Coffee : Latte', 'Food : Biscotti', 'Food : Croi...', 'Food : Scone', 'Gifts : Coff...', 'Gifts : Coff...', 'Gifts : Mug', 'Gifts : The...']
        y_val_list=['0', '2M', '4M', '6M', '8M', '10M', '12M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_1', x_val_list, y_val_list, msg + ".b")
        xaxis_value="Category : Product"
        resultobj.verify_xaxis_title("MAINTABLE_1", xaxis_value, "Step 10.2d(i): Verify X-Axis Title")
        utillobj.verify_chart_color("MAINTABLE_1", "riser!s0!g2!mbar!", "bar_blue1", "Step 10.2e: Verify bar color")
        leg_list=['Unit Sales', 'Dollar Sales']
        resultobj.verify_riser_legends("MAINTABLE_1",leg_list , 'Step 10.2f Verify legends in the chart')
        utillobj.switch_to_default_content(pause=3)
        
        """    3.1. Save and close IA, and Run the report.    """
        ribbonobj.select_tool_menu_item('menu_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        
if __name__ == '__main__':
    unittest.main()