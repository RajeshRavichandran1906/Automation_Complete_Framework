'''
Created on Jan 18, 2018

@author: Robert

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251685
TestCase Name = LAY: Active Report control values FILTER BETWEEN not working-94071
'''
from common.pages import visualization_metadata, visualization_resultarea, active_filter_selection, visualization_ribbon, ia_resultarea, active_miscelaneous, ia_run
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity,core_utility
import unittest,time

class C2251685_TestClass(BaseTestCase):

    def test_C2251685(self):
        
        """ TESTCASE VARIABLES """
        core_utils = core_utility.CoreUtillityMethods(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        ia_runobj=ia_run.IA_Run(self.driver)
        miscobj=active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        
        """    1. Open IA and create a new Document from the folder.    """
        """    1.1. Select CAR as master file.    """
        """    1.2. Select Country ,Car, Seats, Sales as fields.    """
        
        
        
        utillobj.infoassist_api_login('document','ibisamp/car','P116/S10071', 'mrid', 'mrpass')
        resultobj.wait_for_property("#iaCanvasCaptionLabel", 1, expire_time=60, string_value='Document') 
        
        """    1.2. Select Category, Product,Unit Sales to get a report    """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 6, expire_time=10)    
        metaobj.datatree_field_click("CAR", 2, 1)
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 17, expire_time=10)
        metaobj.datatree_field_click("SEATS", 2, 1)
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 28, expire_time=10)    
        metaobj.datatree_field_click("SALES", 2, 1)
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 39, expire_time=10)
        
        
        #ribbonobj.repositioning_document_component('1', '2')
        
        """    1.2a Verify the following "Report" in Canvas    """
        coln_list=["COUNTRY", "CAR", "SEATS", "SALES"]
        
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 01.01: Verify column titles")
        #ia_resultobj.create_report_data_set('TableChart_1 ', 10, 4, 'C2251685_Ds01.xlsx')
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, 'C2251685_Ds01.xlsx', 'Step 01.02: Verify Preview report dataset')
        time.sleep(3)
        
        """    "2. Click on Sales - filter - BETWEEN - choose any range, the correct.    """
        """    "2.1. Verify output is generated.    """
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 25)
        utillobj.switch_to_frame(pause=3)
        
        resultobj.wait_for_property("#ITableData0 tbody tr[id='I0r0.0']",1,20)
        miscobj.select_menu_items('ITableData0', 3, 'Filter', 'Between')
        filter_icon = self.driver.find_elements_by_css_selector('#wall1 img')
        core_utils.left_click(filter_icon[4])
        utillobj.synchronize_with_number_of_element('#dt0_ftp1_1_0_x__0 table>tbody', 1, 25)
        value = self.driver.find_elements_by_css_selector('#dt0_ftp1_1_0_x__0 table>tbody>tr')
        core_utils.left_click(value[1])
        core_utils.left_click(filter_icon[5])
        utillobj.synchronize_with_number_of_element('#dt0_ftp1_2_0_x__0 table>tbody', 1, 25)
        value = self.driver.find_elements_by_css_selector('#dt0_ftp1_2_0_x__0 table>tbody>tr')
        core_utils.left_click(value[5])
#         filterselectionobj.create_filter(1,'Between',value1='7800',value2='43000')
        
        time.sleep(4)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(4)
        
        miscobj.verify_page_summary('0','5of10records,Page1of1', 'Step 02.01: Verify the page summary')
        #utillobj.create_data_set('ITableData0','I0r','C2251685_Ds02.xlsx')
        utillobj.verify_data_set('ITableData0','I0r','C2251685_Ds02.xlsx', 'Step 02.02: Verify that report for between filter')
        time.sleep(4)

        """        3. Now from Insert tab click on Check box to insert.    """
        
        utillobj.switch_to_default_content(pause=3)
        ribbonobj.select_ribbon_item("Insert", "checkbox")
        
        utillobj.verify_object_visible("#Prompt_1", True, 'Step 03.01: Verify checkbox is present')
        ribbonobj.repositioning_document_component('5', '1')
        
        time.sleep(8)
        
        
        """    "4. Right click on the checkbox and click on Seats on the field option.    """
        
        resultobj.choose_right_click_menu_item_for_prompt('#Prompt_1', 'Properties')
        
        source_dict={'select_field':'SEATS'}
        resultobj.customize_active_dashboard_properties(source=source_dict)
        
        utillobj.wait_for_object_not_visible("#adpPropertiesDlg", 30, 'Step 04.01: Wait for Object not visible')
        
        """    "5. Execute the report, after which click on the any two checkbox values to be filtered from report.    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.synchronize_with_number_of_element(path_css, 1, 25)
        
        utillobj.switch_to_frame(pause=3)
        ia_runobj.select_active_dashboard_prompts('checkbox',"#checkbox_dPROMPT_1", ['2', '4'])
        
#         pg_css="#MAINTABLE_wbody0 table[class='arGridBar'] table>tbody"
        #utillobj.synchronize_with_visble_text(pg_css,"5of10records,Page1of1",30)
        time.sleep(10)
        
        #utillobj.create_data_set('ITableData0','I0r','C2251685_Ds03.xlsx')
        utillobj.verify_data_set('ITableData0','I0r','C2251685_Ds03.xlsx', 'Step 05.01: Verify that report for between filter')
        time.sleep(4)
        
        
        utillobj.switch_to_default_content(pause=3)
        
        
if __name__ == '__main__':
    unittest.main()