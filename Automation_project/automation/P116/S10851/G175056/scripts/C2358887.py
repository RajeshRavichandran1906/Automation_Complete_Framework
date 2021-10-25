'''
Created on Jan 24, 2018.
@author: Nasir.
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.pages import ia_resultarea, ia_run
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.lib import utillity


class C2358887_TestClass(BaseTestCase):

    def test_C2358887(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(driver)
        miscobj = active_miscelaneous.Active_Miscelaneous(driver)
        metaobj = visualization_metadata.Visualization_Metadata(driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(driver)  
        ribbonobj = visualization_ribbon.Visualization_Ribbon(driver)
        ia_runobj = ia_run.IA_Run(driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(driver)
        Test_Case_ID = 'C2227529'
        
        """
        Step 1. Launch IA to develop a new report.
        Select 'GGSales' as master file, and change output format as Active report.
        Select Category, Product ID, Unit Sales and Dollar Sales to get a report
        """
        utillobj.infoassist_api_login('report','ibisamp/ggsales','P116/S10851_1', 'mrid', 'mrpass')
        sync_text='Drag and drop fields onto thecanvas or into the query paneto begin building your report.'
        utillobj.synchronize_with_visble_text("#TableChart_1 [align='justify']", sync_text, 60)
        metaobj.datatree_field_click("Category", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 2, 30)
        metaobj.datatree_field_click("Product ID", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 5, 30)
        metaobj.datatree_field_click("Unit Sales", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 8, 30)
        metaobj.datatree_field_click("Dollar Sales", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 11, 30)
        coln_list = ["Category", "Product ID", "Unit Sales", "Dollar Sales"]
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1 ", coln_list, "Step 1a: Verify column titles")
        
        """    2. Save the report (Note: Report should be save as AHTML.001)    """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        resultobj.wait_for_property("#IbfsOpenFileDialog7_cbFileName input", 1, expire_time=10)
        time.sleep(1)
        utillobj.ibfs_save_as('AHTML_001')
        time.sleep(3)
        utillobj.infoassist_api_logout()
        
        """    3. Launch IA to develop a document    """
        """    4. Select 'GGSales' as master file, and change output format as Active report.    """
        utillobj.infoassist_api_login('document','ibisamp/ggsales','P116/S10851_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#iaCanvasCaptionLabel", 'Document', 60) 
        time.sleep(5) 
        active_format_btn_css="#HomeFormatType img[src*='active_reports_32']"
        utillobj.verify_element_visiblty(element_css=active_format_btn_css, msg='Step 1.0: Verify if the active report output fromat is selected by default.')
        output_type = self.driver.find_element_by_css_selector("#HomeFormatType").text.strip()
        utillobj.asequal('Active Report', output_type, "Step 4a: Verify output format as Active report.")
        
        """    5. Select Category, Product and Unit Sales to get a report.    """
        metaobj.datatree_field_click("Category", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 2, 30)
        metaobj.datatree_field_click("Product ID", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 5, 30)
        metaobj.datatree_field_click("Unit Sales", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 8, 30)
        ribbonobj.repositioning_document_component('0.5', '0.75')
        
        """    6. Choose 'Chart' from 'Insert' tab, then add PRODUCT ID and Dollar Sales to get a graph    """
        ribbonobj.select_ribbon_item("Insert", "Chart")
        time.sleep(15)
        metaobj.datatree_field_click("Product ID", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_2 svg g text[class*='xaxisOrdinal-title']", "Product ID", 10)
        metaobj.datatree_field_click("Dollar Sales", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_2 svg g text[class*='yaxis-title']", "Dollar Sales", 10)
        ribbonobj.repositioning_document_component('5', '2.75')
        
        """    7. Select 'Existing Report' from 'insert' tab, choose the saved AHTML report AHTML.001    """
        ribbonobj.select_ribbon_item("Insert", "Existing_Report")
        time.sleep(5)
        oFolder=utillobj.parseinitfile('suite_id')
        utillobj.select_masterfile_in_open_dialog(oFolder, "AHTML_001")
        ribbonobj.repositioning_document_component('0.5', '4.5')
        
        """    8. Choose 'Text box' from 'Insert' tab, and type "Chart, Report and Images are tested in this case"    """
        ribbonobj.select_ribbon_item("Insert", "Text_Box")
        time.sleep(1)
        ribbonobj.resizing_document_component('0.25', '5')
        ribbonobj.repositioning_document_component('5', '0.75')
        ia_resultobj.enter_text_in_Textbox('Text_1', "Report and Images are tested in this case")
        
        """    9. Choose 'Image' from 'Insert' tab, and choose a image(ex-SMPLOGO1), and give OK    """
        """    10. Now arrange the chart, report, text and Image, So it wont collide each other.    """
        ribbonobj.select_ribbon_item("Insert", "Image")
        resultobj.wait_for_property("#IbfsOpenFileDialog7_cbFileName input", 1, expire_time=10)
        apps_css="#paneIbfsExplorer_exTree > div.bi-tree-view-body-content table tr"
        x=[el.text.strip() for el in driver.find_elements_by_css_selector(apps_css)]
        apps=driver.find_elements_by_css_selector(apps_css)
        apps[x.index('Domains')].find_element_by_css_selector("img[src*='triangle']").click()
        time.sleep(1)
        utillobj.expand_domain_folders_in_open_dialog('EDASERVE->baseapp')
        utillobj.select_item_from_ibfs_explorer_list('smplogo1.gif')
        time.sleep(1)
        ribbonobj.repositioning_document_component('5', '1.5')
        
        """    10. Now arrange the chart, report, text and Image, So it wont collide each other.    """
        coln_list = ['Category', 'Product ID', 'Unit Sales']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 10a: Verify column titles")
        coln_list = ["Category", "Product ID", "Unit Sales", "Dollar Sales"]
        resultobj.verify_report_titles_on_preview(4, 4, "IncludeTable_1", coln_list, "Step 10b: Verify column titles")
        msg="Step 10c: Text box is shown with 'Report and Images are tested in this case'."
        ia_resultobj.verify_text_in_Textbox('#Text_1', 'Report and Images are tested in this case', msg)
        msg="Step 10d: Image box is shown with smplogo1.png."
        oImg=driver.find_element_by_id("PageItemImage_1").find_element_by_css_selector("img[src*='PageItemImage_1']").is_displayed()
        utillobj.asequal(True, oImg, msg)
        
        resultobj.verify_number_of_riser("TableChart_2", 1, 2, 'Step 10e: Verify the total number of risers displayed on Preview Chart')
        expected_xval_list=['C141', 'C144']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        resultobj.verify_riser_chart_XY_labels('TableChart_2', expected_xval_list, expected_yval_list, 'Step 10f: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("TableChart_2", "riser!s0!g0!mbar!", "bar_blue1", "Step 10g: Verify bar color")
        xaxis_value="Product ID"
        yaxis_value="Dollar Sales"
        resultobj.verify_xaxis_title("TableChart_2", xaxis_value, "Step 10h(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_2", yaxis_value, "Step 10h(ii): Verify Y-Axis Title")       
        
        """    11. Save and run the report.    """
        ribbonobj.select_tool_menu_item('menu_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        utillobj.switch_to_frame()
        time.sleep(2)
        # Report 1
        miscobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 11r.a: Verify the Report Heading')
        coln_list = ['Category', 'Product ID', 'Unit Sales']
        miscobj.verify_column_heading('ITableData0', coln_list, 'Step 11r.b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', 'C2358887_Ds01.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2358887_Ds01.xlsx', 'Step 11r.c: Verify data.')
        # Chart 2
        miscobj.verify_arChartToolbar("MAINTABLE_1",['More Options','Advanced Chart','Original Chart'],"Step 11g.a: Verify Chart toolbar")
        x_val_list=['C141', 'C142', 'C144', 'F101', 'F102', 'F103', 'G100', 'G104', 'G110', 'G121']
        y_val_list=['0', '2M', '4M', '6M', '8M', '10M', '12M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_1', x_val_list, y_val_list, "Step 11g.b")
        expected_tooltip=['Product ID:  C141', 'Dollar Sales:  3906243', 'Filter Chart', 'Exclude from Chart']
        miscobj.verify_active_chart_tooltip('MAINTABLE_1', 'riser!s0!g0!mbar', expected_tooltip, "Step 11g.c: verify the chart tooltip")
        xaxis_value="Product ID"
        yaxis_value="Dollar Sales"
        resultobj.verify_xaxis_title("MAINTABLE_1", xaxis_value, "Step 11g.d(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_1", yaxis_value, "Step 11g.d(ii): Verify Y-Axis Title")
        utillobj.verify_chart_color("MAINTABLE_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 11g.e: Verify bar color")
        miscobj.verify_chart_title("MAINTABLE_wbody1_ft","Dollar Sales BY Product ID", "Step 11g.f : Verify chart title ")
        # Include Report 1
        miscobj.verify_page_summary(2, '10of10records,Page1of1', 'Step 11i.a: Verify the Report Heading')
        coln_list = ['Category', 'Product ID', 'Unit Sales', 'Dollar Sales']
        miscobj.verify_column_heading('ITableData2', coln_list, 'Step 11i.b: Verify the column heading')
        #utillobj.create_data_set('ITableData2', 'I2r', 'C2358887_Ds02.xlsx')
        utillobj.verify_data_set('ITableData2', 'I2r', 'C2358887_Ds02.xlsx', 'Step 11i.c: Verify data.')
        # Text Box
        msg="Step 11.txt: verify Text box is shown with 'Report and Images are tested in this case'."
        ia_runobj.verify_document_objects("[id^='LOBJText']", 'textbox', msg, expected_value_list=['Report and Images are tested in this case'])
        # Image
        msg="Step 11.img: Verify Image is shown with smplogo1.png."
        ia_runobj.verify_document_objects("[id^='LOBJPageItemImage']", 'image', msg, expected_image_name='C2358887_2.png')
        utillobj.switch_to_default_content()
        
        """    Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
if __name__ == '__main__':
    unittest.main()
        