'''
Created on Jan 16, 2018

@author: Robert

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251622
TestCase Name = Verify that Dashboard prompt's horizontal/vertical positions can be rearranged on canvas and runtime (by accessing Size and Position dialog box)
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_resultarea, active_miscelaneous
from common.lib import utillity

class C2251622_TestClass(BaseTestCase):

    def test_C2251622(self):
        
        """ TESTCASE VARIABLES """
        Test_Case_ID = 'C2251622'
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        miscobj=active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """    1. Launch IA to develop a Document.    """
        """    1.1. Select 'GGSales' as master file, and change output format as Active report    """
        
        utillobj.infoassist_api_login('document','ibisamp/ggsales','P116/S10071', 'mrid', 'mrpass')
        resultobj.wait_for_property("#iaCanvasCaptionLabel", 1, expire_time=60, string_value='Document') 
        
        """    1.2. Select Category, Product,Unit Sales to get a report    """
        metaobj.datatree_field_click("Category", 2, 1)
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 2, expire_time=25)    
        metaobj.datatree_field_click("Product", 2, 1)
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 5, expire_time=25)
        metaobj.datatree_field_click("Unit Sales", 2, 1)
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 8, expire_time=25)    
          
        ribbonobj.repositioning_document_component('0.5', '0.75')
        
        """    1.2a Verify the following "Report" in Canvas    """
        coln_list=["Category", "Product", "Unit Sales"]
        
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 1.2a: Verify column titles")
        #ia_resultobj.create_report_data_set('TableChart_1 ', 18, 5, 'C2251621_Ds01.xlsx')
        ia_resultobj.verify_report_data_set('TableChart_1', 2, 3, 'C2251622_Ds01.xlsx', 'Step 1.2b: Verify Preview report dataset')
        
        """    2. Now, select Drop down button from 'Insert' tab. Place it on the left side of the report.    """
        
        
        ribbonobj.select_ribbon_item("Insert", "Drop_down")
        utillobj.synchronize_with_number_of_element("#Prompt_1", 1, 25)
        ribbonobj.repositioning_document_component('3', '1')
        
        """    3. Right click on Drop down button and select properties.    """
        resultobj.choose_right_click_menu_item_for_prompt('#Prompt_1', 'Properties')
        utillobj.synchronize_with_number_of_element("#adpPropertiesDlg [class*='active'] [class*='window'][class*='caption']", 1, 25)
        
        """    4. Assign 'Unit Sales' under Field. Make sure Condition is set to Equal to and Include All is checked.    """
        utillobj.select_combobox_item('comboSourceFields', 'Unit Sales')
        
        '''to add code to verify condition is set to equal to'''
        eqval=self.driver.find_element_by_css_selector("#comboConditions div[class$='combo-box-label']").text
        utillobj.asequal('Equal to',eqval,'Step 4. Verify condition set to Equal to')
        
        utillobj.verify_object_visible("[id='adpPropertiesDlg'] #checkShowAll input[checked]", True, 'Step 04: Verify Include All checkbox is enabled')
        
        ok_Btn=driver.find_element_by_css_selector('#btnADPOK img')
        utillobj.default_left_click(object_locator=ok_Btn)
        time.sleep(5)
        
        '''    5. Right-click the component and click Size and Position    '''
        combo_box=driver.find_element_by_id("Prompt_1")
        utillobj.default_click(combo_box, click_option=0)
        time.sleep(2)
        utillobj.default_click(combo_box, click_option=1)
        time.sleep(2)
        
        '''    6. Click Position tab.    '''
        '''    6.1. Set the horizontal position to 2.04 and vertical position to 2.04. Click Apply.    '''
        ribbonobj.repositioning_document_component('2.04', '2.04')
        
        '''    7. Click Ok. Re arrange report on the right side so they do not overlap each other.    '''
        '''    7.1. Verify that ADP is moved per new horizontal/vertical position.    '''
        report1=driver.find_element_by_id("TableChart_1")
        utillobj.default_click(report1, click_option=0)
        time.sleep(2)
        utillobj.default_click(report1, click_option=1)
        time.sleep(2)
        ribbonobj.repositioning_document_component('7', '1')
        
        table_left=report1.value_of_css_property('left')
        table_left=int(table_left[:-2])
        print ('table_left', table_left)
        
        combo_left=combo_box.value_of_css_property('left')
        combo_left=int(combo_left[:-2])
        print ('combo_left', combo_left)
        
        if table_left> 500 and combo_left < 200:
            status=True
        else:
            status=False
        
        utillobj.asequal(True,status,'Step 7.1. Verify ADP is moved as per new position')
        
        '''    8. Run the dashboard.    '''
        '''    8.1. Verify that document should display as per the vertical and horizontal position.    '''
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.synchronize_with_number_of_element("[id^='ReportIframe']", 1, 60)
        utillobj.switch_to_frame()
        
        '''Verifying the data in the ouput'''
        miscobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 8.1a: Verify the Report Heading')
        column_list=["Category", "Product", "Unit Sales"]
        miscobj.verify_column_heading('ITableData0', column_list, 'Step 8.1b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', 'C2227529_Ds02.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2251622_Ds02.xlsx', 'Step 8.1c: Verify data.')
        val11=['[All]', '186534', '189217', '190081', '190695', '308986', '333414', '360570', '421377', '630054', '878063']
        p1=driver.find_elements_by_css_selector("#combobox_dPROMPT_1 option")
        prompt1=[el.text.strip() for el in p1]
        print ('prompt1',prompt1)
        utillobj.asequal(prompt1, val11, "Step 8.1d Verify prompt 1 Combobox")
        
        
        report1=driver.find_element_by_id("MAINTABLE_0")
        combo_box=driver.find_element_by_css_selector("div[id^='LOBJPrompt']")
        
        run_table_left=report1.value_of_css_property('left')
        run_table_left=int(run_table_left[:-2])
        
        run_combo_left=combo_box.value_of_css_property('left')
        run_combo_left=int(run_combo_left[:-2])
        
        if run_table_left> 500 and run_combo_left < 220:
            status=True
        else:
            status=False
        
        utillobj.asequal(True,status,'Step 8.1. Verify ADP is moved as per new position')
        
        utillobj.switch_to_default_content(pause=3)
        
        ''' Saving the report    '''
        ribbonobj.select_tool_menu_item('menu_save')
        
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        
        
if __name__ == '__main__':
    unittest.main()