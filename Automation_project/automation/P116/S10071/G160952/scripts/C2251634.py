'''
Created on Jan 30, 2018

@author: BM13368
TestCase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2251634
TestCase Name: AHTML/APDF: TEXT prompt functionality is not working - specific to IE browser (164049)
'''
import unittest, pyautogui
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_resultarea, active_miscelaneous
from common.lib import utillity

class C2251634_TestClass(BaseTestCase):

    def test_C2251634(self):
        
        """ TESTCASE VARIABLES """
        Test_Case_ID = 'C2251634'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        miscobj=active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
            Step 01:Launch IA to develop a Document and select 'GGSales' as master file
            Select Product and Unit Sales fields to create one report
        """
        utillobj.infoassist_api_login('document','ibisamp/ggsales','P116/S10071_2', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#iaCanvasCaptionLabel", 'Document', 95)
        metaobj.datatree_field_click("Product", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 3, 60)
        metaobj.datatree_field_click("Unit Sales", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 6, 60)
         
        """
            Verify live preview report data
        """
        coln_list = ["Product", "Unit Sales"]
        resultobj.verify_report_titles_on_preview(2, 2, "TableChart_1 ", coln_list, "Step 02:01: Verify column titles")
#         ia_resultobj.create_report_data_set('TableChart_1', 2, 2, Test_Case_ID+"_Ds01.xlsx")
        ia_resultobj.verify_report_data_set('TableChart_1', 2, 2, Test_Case_ID+"_Ds01.xlsx", 'Step 02:02: Verify Preview report dataset')
         
        """
            Step 02:Now select Text from insert tab and drag it on the right of the report
        """
        ribbonobj.select_ribbon_item("Insert", "text")
        utillobj.synchronize_with_number_of_element("#Prompt_1", 1, 30)
        ribbonobj.repositioning_document_component('4.80', '1.04')
         
        """ 
            Step 03:Right click on Text box and select 'Properties'
        """
        resultobj.choose_right_click_menu_item_for_prompt('#Prompt_1','Properties')
        utillobj.synchronize_with_number_of_element("#adpPropertiesDlg [class*='active'] [class*='window'][class*='caption']", 1, 15) 
        """ 
            Step 04:Assign field as Unit Sales. Make sure Condition is set as Equal to, and Include All is checked. Click Ok.
        """
        source={'select_field':'Unit Sales','verify_condition':'Equal to', 'verify_includeall':True}
        resultobj.customize_active_dashboard_properties(source=source, msg="Step 04:01:", btn_type='ok')
        
        """ 
            Step 05:Run the Document.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.synchronize_with_number_of_element("[id^='ReportIframe']", 1, 45)
        utillobj.switch_to_frame(pause=1)
        
        """
            Step 06:Enter text as '190695' in text box and enter
            Verify TEXT prompt returns correct results for '190695' on IE browser. Test with FF and Chrome as well.
        """
        element=self.driver.find_element_by_css_selector("#PROMPT_1_cs input")
        exec("element.clear()")
        exec("element.send_keys('190695')")
        
        pyautogui.press('enter', pause=7)
        utillobj.synchronize_with_number_of_element("table[id='IWindowBody0'] .arGridBar table>tbody>tr>td>table>tbody>tr", 1,25)
        miscobj.verify_page_summary(0, '1of10records,Page1of1', 'Step 06:01: Verify the Report Heading')
        column_list=['Product', 'Unit Sales']
        miscobj.verify_column_heading('ITableData0', column_list, "Step 06:02: Verify the Run Report column heading")
#         utillobj.create_data_set('ITableData0','I0r', Test_Case_ID +'_Ds02.xlsx')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID +'_Ds02.xlsx', "Step 06:03: Verify entire Data set in Run Report on Page 1")
        utillobj.switch_to_default_content(pause=1)

if __name__ == "__main__":
    unittest.main()