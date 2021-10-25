'''
Created on Jan 24, 2018
TestSuite ID :http://172.19.2.180/testrail/index.php?/suites/view/10851&group_by=cases:section_id&group_order=asc&group_id=175061
TestCase Name : Create a multi-page Document and rename Pages
TestCase ID :http://172.19.2.180/testrail/index.php?/cases/view/2358902
@author: BM13368
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_resultarea, active_miscelaneous
from common.lib import utillity, core_utility

class C2358902_TestClass(BaseTestCase):

    def test_C2358902(self):
        
        """ TESTCASE VARIABLES """
        Test_Case_ID = "C2358902"
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        core_utillobj=core_utility.CoreUtillityMethods(self.driver)
        """
            Step 01:Create a new AHTML Document using the ggsales file.
        """
        utillobj.infoassist_api_login('document','ibisamp/ggsales','P116/S10851_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#iaCanvasCaptionLabel", 'Document', 75)
        format_type=self.driver.find_element_by_css_selector("#HomeFormatType").text
        expected_format_type='Active Report'
        utillobj.asequal(expected_format_type, format_type, "Step 01:00:Verify output format shows Active Report bydefault")
          
        """Insert a report with Category and Unit Sales."""
        ribbonobj.select_ribbon_item("Insert", "Report")
        utillobj.synchronize_with_number_of_element("#TableChart_1", 1, 20)
        metaobj.datatree_field_click("Category", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 2, 13)
        metaobj.datatree_field_click("Unit Sales", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 4, 13)
        ribbonobj.repositioning_document_component('.45', '1.04')
          
        coln_list=["Category", "Unit Sales"]
        resultobj.verify_report_titles_on_preview(2, 2, "TableChart_1", coln_list, "Step 01:01: Verify column titles")
#         ia_resultobj.create_report_data_set('TableChart_1 ', 1, 2, Test_Case_ID+"_Ds01.xlsx")
        ia_resultobj.verify_report_data_set('TableChart_1', 1, 2, Test_Case_ID+"_Ds01.xlsx", 'Step 01:02: Verify Preview report dataset')
          
        """Insert a Bar chart with Category and Unit Sales."""
        ribbonobj.select_ribbon_item("Insert", "Chart")
        utillobj.synchronize_with_number_of_element("#TableChart_2 svg g.risers >g>rect[class^='riser']", 25, 20)
        metaobj.datatree_field_click("Category", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_2 text[class^='xaxis'][class$='title']",'Category',20)
        metaobj.datatree_field_click("Unit Sales", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_2 text[class^='xaxis'][class$='title']", 1,20)
        ribbonobj.repositioning_document_component('5.20', '1.04')
          
        resultobj.verify_yaxis_title("TableChart_2", 'Unit Sales', "Step 01:03: Verify Y-axis Title")
        resultobj.verify_xaxis_title("TableChart_2", 'Category', "Step 01:04: Verify X-axis Title")
        resultobj.verify_number_of_riser("TableChart_2", 1, 1, 'Step 01:05: Verify the total number of risers displayed on live-preview Chart')
        expected_yval_list=['0', '100K', '200K', '300K', '400K', '500K', '600K']
        expected_xval_list=['Coffee']
        resultobj.verify_riser_chart_XY_labels("TableChart_2", expected_xval_list, expected_yval_list, 'Step 01:06: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_2", "riser!s0!g0!mbar", "bar_blue", "Step 01:07: Verify first bar color")
          
        """
            Step 02:In the upper right corner, click Page 1, then Page Options.
        """
        ia_resultobj.select_or_verify_document_page_menu('Page Options...')
        utillobj.synchronize_with_number_of_element("#pageOptionsDlg", 1, 15)
        page_option_elem=self.driver.find_element_by_css_selector("#pageOptionsDlg table tbody").text.strip()
        utillobj.asequal(page_option_elem, 'Page 1', "Step 02:01:Verify the list of option in the Page Options")
        page1_elem=self.driver.find_element_by_css_selector("#pageOptionsDlg #iaPageList table tbody tr td img")
        core_utillobj.left_click(page1_elem)
        time.sleep(1)
        option_ok_elem=self.driver.find_element_by_css_selector("#pageOptionsDlg #pageOptionsOkBtn")
        core_utillobj.left_click(option_ok_elem)

        """
            Step 03:Click Page 1, then click the change page name button in the upper right of the Page options menu.
            Change "page1" to "Multi-page-Doc 1"
        """
        ia_resultobj.select_or_verify_document_page_menu('Page Options...')
        time.sleep(0.50)
        page1_elem=self.driver.find_element_by_css_selector("#pageOptionsDlg #iaPageList table tbody tr td img")
        core_utillobj.left_click(page1_elem)
        time.sleep(2)
          
        click_on_edit_title_elem=self.driver.find_element_by_css_selector("#pageOptionsToolBar #renamePageBtn")
        core_utillobj.left_click(click_on_edit_title_elem)
        time.sleep(1)
        edit_textbox_elem=self.driver.find_element_by_css_selector("#iaPageList input")
        utillobj.set_text_field_using_actionchains(edit_textbox_elem, "Multi-page-Doc 1")
        time.sleep(2)
          
        """ Step 04 :Click OK to confirm the changed name."""
        option_ok_elem=self.driver.find_element_by_css_selector("#pageOptionsDlg #pageOptionsOkBtn")
        core_utillobj.left_click(option_ok_elem)
        utillobj.synchronize_with_visble_text("#iaPagesMenuBtn div[id^='BiLabel']", 'Multi-page-Doc 1', 20)
          
        """ Expect to see the following Document pane with the new page 1 name - Multi-page-Doc 1. """
#         page_name_title=self.driver.find_element_by_css_selector("#iaPagesMenuBtn div[id^='BiLabel']").text
#         print(page_name_title)
#         utillobj.asequal(page_name_title, 'Multi-page-Doc 1', "Step 04:01:Verify page name has been changed Multi-Page-Doc1")
#           
        """ Step 05:Click the new page name in the upper right and click new page """
        ia_resultobj.select_or_verify_document_page_menu('New Page',default_page_name='Multi-page-Doc 1')
        time.sleep(15)
          
        """Expect to see a new page 1 with a blank canvas."""
        oPage2=self.driver.find_element_by_xpath("//div[@id='iaPagesMenuBtn']//div[contains(text(), 'Page 1')]")
        utillobj.verify_object_visible('css', True, "Step 05:01: Verify Page changed to 'Page 1'", elem_obj=oPage2)
        oLengthClass=self.driver.find_elements_by_css_selector("#iaCanvasPanel #theCanvas>div")
        utillobj.asequal(len(oLengthClass), 1, "Step 05:02: Verify blank page displayed")
          
        """ 
            Step 06:On the new page add Category, Product and Unit Sales to the default bar chart.
        """
        canvas_elem=self.driver.find_element_by_css_selector("#theCanvas")
        utillobj.click_on_screen(canvas_elem, "middle", click_type=0)
        time.sleep(5)
        ribbonobj.select_ribbon_item("Insert", "Chart")
        metaobj.datatree_field_click("Category", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_3 text[class^='xaxis'][class$='title']",'Category',20)
        metaobj.datatree_field_click("Product", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_3 svg g.risers >g>rect[class^='riser']", 2, 20)
        metaobj.datatree_field_click("Unit Sales", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_3 text[class^='yaxis'][class$='title']", 1, 20)
        ribbonobj.repositioning_document_component('.45', '1.04')
          
        """Then insert a report and position to the right of the Bar Chart."""
        ribbonobj.select_ribbon_item("Insert", "Report")
          
        """Add Category, Product & Unit Sales to the report."""
        metaobj.datatree_field_click("Category", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_4 div[class^='x']", 2, 13)
        metaobj.datatree_field_click("Product", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_4 div[class^='x']", 5, 13)
        metaobj.datatree_field_click("Unit Sales", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_4 div[class^='x']", 8, 13)
        ribbonobj.repositioning_document_component('5.80', '1.04')
          
        """ Expect to see the new page 1 Document pane. """
        resultobj.verify_yaxis_title("TableChart_3", 'Unit Sales', "Step 06:01: Verify Y-axis Title")
        resultobj.verify_xaxis_title("TableChart_3", 'Category : Product', "Step 06:02: Verify X-axis Title")
        resultobj.verify_number_of_riser("TableChart_3", 1, 2, 'Step 06:03: Verify the total number of risers displayed on live-preview Chart')
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K','350K']
        expected_xval_list=['Coffee : Capuccino', 'Coffee : Espresso']
        resultobj.verify_riser_chart_XY_labels("TableChart_3", expected_xval_list, expected_yval_list, 'Step 06:04: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_3", "riser!s0!g0!mbar", "bar_blue", "Step 06:05: Verify first bar color")
          
        coln_list = ["Category", "Product", "Unit Sales"]
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_4", coln_list, "Step 06:06: Verify column titles")
#         ia_resultobj.create_report_data_set('TableChart_4', 2, 3, Test_Case_ID+"_Ds02.xlsx")
        ia_resultobj.verify_report_data_set('TableChart_4', 2, 3, Test_Case_ID+"_Ds02.xlsx", 'Step 06:07: Verify Preview report dataset')
          
        """
            Click the Page 1 box in the upper right.
            Select Page Options.
            Select Page 1.
            Click the Edit button to rename.
        """
        ia_resultobj.select_or_verify_document_page_menu('Page Options...')
        time.sleep(0.50)
        page1_elem=self.driver.find_element_by_css_selector("#pageOptionsDlg #iaPageList table tbody tr:nth-child(2)")
        core_utillobj.left_click(page1_elem)
        time.sleep(1)
          
        click_on_edit_title_elem=self.driver.find_element_by_css_selector("#pageOptionsToolBar #renamePageBtn")
        core_utillobj.left_click(click_on_edit_title_elem)
        edit_textbox_elem=self.driver.find_element_by_css_selector("#iaPageList input")
          
        """ Step 08:Change "page1" to Multi-page-Doc 2.Click ok"""
        utillobj.set_text_field_using_actionchains(edit_textbox_elem, "Multi-page-Doc 2")
        option_ok_elem=self.driver.find_element_by_css_selector("#pageOptionsDlg #pageOptionsOkBtn")
        core_utillobj.left_click(option_ok_elem)
        utillobj.synchronize_with_visble_text("#iaPagesMenuBtn div[id^='BiLabel']", 'Multi-page-Doc 2', 20)
          
        """Expect to see the following changed page name for Multi-page-Doc 2."""
        oPage2=self.driver.find_element_by_xpath("//div[@id='iaPagesMenuBtn']//div[contains(text(), 'Multi-page-Doc 2')]")
        utillobj.verify_object_visible('css', True, "Step 08:01: Verify Page changed to 'Page 1'", elem_obj=oPage2)
        oLengthClass=self.driver.find_elements_by_css_selector("#iaCanvasPanel #theCanvas>div")
        utillobj.asequal(len(oLengthClass), 3, "Step 08:02: Verify the page is displayed with report, chart displayed")
        
        """Step 09:Click the Run button."""
        ribbonobj.select_top_toolbar_item('toolbar_run')
        css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(css, 1, 30)
        utillobj.switch_to_frame(pause=1) 
       
        """ Verify chart in Page1 """
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", "Unit Sales", "Step 09:01: Verify -yAxis Title")
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", "Category", "Step 09:02: Verify -xAxis Title")
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M']
        expected_xval_list=['Coffee','Food','Gifts']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 09:03: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 3, 'Step 09:04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mbar!", "bar_blue", "Step 09:04: Verify  bar color")
        miscelanousobj.verify_chart_title('MAINTABLE_wbody1_ft', 'Unit Sales BY Category', 'Step 09:05: Verify Chart Title')
        miscelanousobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['More Options','Advanced Chart','Original Chart'],"Step 09:06: Verify Chart toolbar")
        miscelanousobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Aggregation'],"Step 09:07: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelanousobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Sum'],"Step 09:08: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
         
        """Verify report data"""
        miscelanousobj.verify_page_summary(0, '3of3records,Page1of1', "Step 09:10: Verify the Run Report Heading")
        column_list=['Category', 'Unit Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, "Step 09:11: Verify the Run Report column heading")
#         utillobj.create_data_set('ITableData0','I0r', Test_Case_ID +'_Ds03.xlsx')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID +'_Ds03.xlsx', "Step 09:12: Verify entire Data set in Run Report on Page 1") 
                
        """Step 10:Click the Multi-page-Doc 2 button at the top of the Document."""
        select_css = "#IBILAYOUTDIV0TABS .arDashboardBarButton[id^='iLay']"
        self.driver.find_element_by_css_selector(select_css).click()
        time.sleep(5)
         
        """ Verify chart in Page2 """
        resultobj.verify_yaxis_title("MAINTABLE_wbody2", "Unit Sales", "Step 10:01: Verify -yAxis Title")
        resultobj.verify_xaxis_title("MAINTABLE_wbody2", "Category : Product", "Step 10:02: Verify -xAxis Title")
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        expected_xval_list=['Coffee : Ca...', 'Coffee : Es...', 'Coffee : Latte', 'Food : Biscotti', 'Food : Croi...', 'Food : Scone', 'Gifts : Coffe...', 'Gifts : Coffe...', 'Gifts : Mug', 'Gifts : Ther...']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody2", expected_xval_list, expected_yval_list, "Step 10:03: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody2", 1, 10, 'Step 08:21: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody2", "riser!s0!g2!mbar!", "bar_blue", "Step 10:04: Verify  bar color")
        miscelanousobj.verify_chart_title('MAINTABLE_wbody2_ft', 'Unit Sales BY Category, Product', 'Step 10:05: Verify Chart Title')
        miscelanousobj.verify_arChartToolbar('MAINTABLE_wmenu2', ['More Options','Advanced Chart','Original Chart'],"Step 10:06: Verify Chart toolbar")
        miscelanousobj.verify_arChartToolbar('MAINTABLE_wmenu2', ['Aggregation'],"Step 10:07: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelanousobj.verify_arChartToolbar('MAINTABLE_wmenu2', ['Sum'],"Step 10:08: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        
        """ Verify created report """
        miscelanousobj.verify_page_summary(3, '10of10records,Page1of1', "Step 10:10: Verify the Run Report Heading")
        column_list=['Category', 'Product','Unit Sales']
        miscelanousobj.verify_column_heading('ITableData3', column_list, "Step 10:11: Verify the Run Report column heading")
#         utillobj.create_data_set('ITableData3','I3r', Test_Case_ID +'_Ds04.xlsx')
        utillobj.verify_data_set('ITableData3','I3r',Test_Case_ID +'_Ds04.xlsx', "Step 10:12: Verify entire Data set in Run Report on Page 1") 
        time.sleep(2)
        
if __name__ == "__main__":
    unittest.main()    
        