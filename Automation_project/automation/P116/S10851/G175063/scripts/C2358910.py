'''
Created on Jan 31, 2018
TestSuite ID : http://172.19.2.180/testrail/index.php?/suites/view/10071&group_by=cases:section_id&group_order=asc&group_id=160958
TestSuite Name: AR14 - Active Document 
TestCase Name: AHTML:CMPD:ARPASSWORD throw JS err unable to open Document(135630)
TestCase ID : http://172.19.2.180/testrail/index.php?/cases/view/2358910
@author: Robert
'''
import unittest,datetime
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_resultarea, active_miscelaneous, ia_ribbon
from common.lib import utillity, core_utility

class C2358910_TestClass(BaseTestCase):

    def test_C2358910(self):
        
        """ TESTCASE VARIABLES """
        Test_Case_ID = 'C2358910'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        ia_ribbonobj=ia_ribbon.IA_Ribbon(self.driver)
        miscobj=active_miscelaneous.Active_Miscelaneous(self.driver)
        core_utillobj=core_utility.CoreUtillityMethods(self.driver)
        """
            Step 1. Create a new Document with GGSALES master file.
            Step 1.1. Using Dashboard create a report with Category,Product ID,Unit Sales,Dollar Sales fields
            
        """
        utillobj.infoassist_api_login('document','ibisamp/ggsales','P116/S10851_2', 'mrid', 'mrpass')
#         utillobj.infoassist_api_edit('a', 'document', 'S10851_2',mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_visble_text("#iaCanvasCaptionLabel", 'Document', 75)
        metaobj.datatree_field_click("Category", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 2, 15)
        metaobj.datatree_field_click("Product ID", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 5, 15)
        metaobj.datatree_field_click("Unit Sales", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 8, 15)
        metaobj.datatree_field_click("Dollar Sales", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 11, 15)
        coln_list = ["Category", "Product ID", "Unit Sales", "Dollar Sales"]
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1 ", coln_list, "Step 01:01: Verify column titles")
#         ia_resultobj.create_report_data_set('TableChart_1', 2, 4, Test_Case_ID+"_Ds01.xlsx")
        ia_resultobj.verify_report_data_set('TableChart_1', 2, 4, Test_Case_ID+"_Ds01.xlsx", 'Step 01:02: Verify Preview report dataset')
          
        """        
            Step 2. From Insert tab click on chart with Category,Product and Unit Sales fields
        """
        ribbonobj.select_ribbon_item("Insert", "Chart")
        utillobj.synchronize_with_number_of_element('#TableChart_2',1, 25)
        ribbonobj.repositioning_document_component('4.80', '1.04')
        metaobj.datatree_field_click("Category", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_2 text[class^='xaxis'][class$='title']",'Category',20)
        metaobj.datatree_field_click("Product", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_2 text[class^='xaxis'][class$='title']",'Category : Product',20)
        metaobj.datatree_field_click("Unit Sales", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_2 text[class^='yaxis'][class$='title']", 1, 20)
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K','350K']
        expected_xval_list=['Coffee : Capuccino', 'Coffee : Espresso']
        
        resultobj.verify_yaxis_title("TableChart_2", 'Unit Sales', "Step 03:01: Verify Y-axis Title")
        resultobj.verify_xaxis_title("TableChart_2", 'Category : Product', "Step 03:02: Verify X-axis Title")
        resultobj.verify_number_of_riser("TableChart_2", 1, 2, 'Step 03:03: Verify the total number of risers displayed on live-preview Chart')
        
        resultobj.verify_riser_chart_XY_labels("TableChart_2", expected_xval_list, expected_yval_list, 'Step 03:04: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_2", "riser!s0!g0!mbar", "bar_blue1", "Step 03:05: Verify first bar color")
          
        """
            Step 3. Select Active Report option from Format->Features and click on the icon.
        """
        utillobj.synchronize_with_number_of_element("#FormatTab_tabButton", 1,30)
        ribbonobj.select_ribbon_item("Format", "active_report_options_chart")
        css="[id^='QbDialog'] #activeReportOptionsSplitPane"
        utillobj.synchronize_with_number_of_element(css, 1, 25)
        
        
        """
            Step 4. Select Advanced tab from Active report window and enter password as "New1" and enter the current date and click OK
        """
        ia_ribbonobj.set_password_active_report_options('textbox', 'password_field', 'New1')
        ia_ribbonobj.set_password_active_report_options('checkbox', 'password_expiration', 'nocheck')
        ia_ribbonobj.set_password_active_report_options('radiobutton', 'date_selection', 'check')
        now = datetime.datetime.now()
        yy=str(now.year)
        yy=str(yy[2:])
        mm=str('%02d' %now.month)
        dd=str('%02d' %now.day)        
        ia_ribbonobj.set_password_active_report_options('textbox', 'expire_date', str(yy+mm+dd))
        ia_ribbonobj.set_password_active_report_options('button', 'ok_button', 'click')
 
        """
            Step 5. Click Run and execute the Dashboard.
        """
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(css, 1, 45)
        utillobj.switch_to_frame(pause=1) 
        
        win_title_css="#wall1 span[id='wtitle1']"
        win_textbox="#wall1 #PromptTable1 input[type='password']"
        win_ok="#wall1 #PromptTable1 div[class='arPromptButton']"
        """
            Step 6. Enter Password on the prompt displayed.
        """
        utillobj.synchronize_with_visble_text(win_title_css, "Report is Password Protected", 20, pause_time=1)
        win_title=self.driver.find_element_by_css_selector(win_title_css).text
        pass_elem=self.driver.find_element_by_css_selector(win_textbox)
        btn_elem=self.driver.find_element_by_css_selector(win_ok)
        utillobj.asequal("Report is Password Protected", win_title,'Step 6. Verify the password prompt')
        utillobj.set_text_field_using_actionchains(pass_elem, 'New1')
        core_utillobj.left_click(btn_elem)
#         utillobj.click_on_screen(btn_elem, "middle", click_type=0, pause=1)
        
        """
            6.1. Verify Report and chart is displayed without any error.
        """
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody1 svg g.risers >g>rect[class^='riser']",10, 55)
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Unit Sales', "Step 03:06: Verify Y-axis Title")
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Category : Product', "Step 03:07: Verify X-axis Title")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 10, 'Step 03:08: Verify the total number of risers displayed on live-preview Chart')
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        expected_xval_list=['Coffee : Ca...', 'Coffee : Es...', 'Coffee : Latte', 'Food : Biscotti', 'Food : Croi...', 'Food : Scone', 'Gifts : Coff...', 'Gifts : Coff...', 'Gifts : Mug', 'Gifts : The...']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, 'Step 03:09: X and Y axis labels')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue1", "Step 03:10: Verify first bar color")
        
        miscobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['More Options','Advanced Chart','Original Chart'],"Step 03:12: Verify Chart toolbar")
        miscobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Aggregation'],"Step 03:13: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Sum'],"Step 03:14: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        miscobj.verify_chart_title("MAINTABLE_wbody1_ft","Unit Sales BY Category, Product", "Step 03:15: Verify chart title ")
        miscobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 03:16: Verify the Report Heading shows 10of10records')
        column_list=["Category", "Product ID", "Unit Sales", "Dollar Sales"]
        miscobj.verify_column_heading('ITableData0', column_list, 'Step 03:17: Verify the column heading')
        
#         utillobj.create_data_set('ITableData0','I0r', Test_Case_ID+"_Ds02.xlsx")
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds02.xlsx","Step 03:18: Verify report data")
        
        
if __name__ == "__main__":
    unittest.main()