'''
Created on Feb 28, 2018

@author: BM13368
TestCase Name : Report-Other: Verify Table of Contents functionality in Active Reports via InfoAssist
TestCase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2227756
'''
import unittest, time, pyautogui
from common.lib import utillity
from common.pages import visualization_metadata, visualization_ribbon, ia_resultarea, ia_run
from common.lib.basetestcase import BaseTestCase
from common.wftools import report


class C2227756_TestClass(BaseTestCase):

    def test_C2227756(self):
        
        Test_Case_ID = "C2227756"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        report_obj= report.Report(self.driver)
        
        """
            Step 01:Sign in to WebFOCUS as a basic user
            http://machine:port/{alias}
            sign in screen will display
            Step 02:Navigate to folder: P292_S10032_G157266
            Execute the following URL:
            http://machine:port/{alias}/ia?tool=report&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FP292_S10032_G157266%2F
            Change the Output type to Active Report.
            Expect to see the following Active Report development canvas.
        """
        report_obj.invoke_report_using_api("new_retail/wf_retail_lite", mrid='autodevuser01')
        utillobj.synchronize_with_number_of_element("#singleReportCaptionLabel img[src*='preview']", 1, 200)
        
        """ 
            Step 03:Select the Gross Profit field from the Sales group in the data tree, as the Measure.
            Select the Product, Category field from the Product group in the data tree, as the Dimension.
            Expect to see the following Live Preview screen.
        """ 
        metaobj.datatree_field_click("Gross Profit", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 2, 60)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 18, 60)
        
#         ia_resultobj.create_across_report_data_set("TableChart_1", 2, 2, 7, 2, Test_Case_ID+"_Ds01.xlsx")
        ia_resultobj.verify_across_report_data_set("TableChart_1", 2, 2, 7, 2, Test_Case_ID+"_Ds01.xlsx", "Step 02:01: Verify report dataset")
       
        """
            Step 04:Click the Format tab at the top and select Table of Contents.
            Click the View Code tab at the top.
            Expect to see the Table of Contents tab highlighted.
            Also expect to see the following line in the View Code panel:
            ON TABLE SET COMPOUND 'BYTOC 1 '
        """
        ribbonobj.select_ribbon_item('Format', 'table_of_contents')
        web_element=self.driver.find_element_by_css_selector("#FormatReportToc")
        utillobj.verify_checked_class_property(web_element, "Step 04: TOC is selected")
        
        """ 
            Step 05:Close the View Code panel and click Run.
            Expect to see the following Active Report with Table of Contents.
            The default report should display the first Category - Accessories.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        iframe=driver.find_element_by_css_selector("iframe[id^='ReportIframe-']")
        x_fr=iframe.location['x']
        y_fr=iframe.location['y']
        utillobj.switch_to_frame(pause=2)
        
#         ia_runobj.create_table_data_set("table[id='IBI_Page0'][summary= 'Summary']", Test_Case_ID+"run_Ds01.xlsx")
        ia_runobj.verify_table_data_set("table[id='IBI_Page0'][summary= 'Summary']", Test_Case_ID+"run_Ds01.xlsx", "Step 05:01: Verify report data in runtime")
        
        toc_btn=driver.find_element_by_css_selector("#divtocDHTMLDummy > img").is_displayed()
        utillobj.asequal(toc_btn, True, "Step 05:02: Verify TOC is displayed at runtime")
        
        """ 
            Step 06:Double click the TOC icon, then move it away from the report
            Step 07:Test the Table of Contents by clicking 'Stereo Systems'.
            Expect to see the following filtered Active Report, with 
            Stereo Systems data shown.
        """
        
        toc_btn=driver.find_element_by_css_selector("#divtocDHTMLDummy > img")
        utillobj.click_on_screen(toc_btn, 'middle', 2)
        
        """    
            Step 08:Click the [All] tab in the Table of Contents.
            Expect to see the following Active Report with all 7 Categories.
        """
        toc_items=['Table of Contents', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'View Entire Report (On/Off)', 'Remove Table of Contents']
        ia_runobj.verify_toc_item(toc_items, "Step 08:01: Verify TOC list of fields")
        
        toc_tree=driver.find_element_by_css_selector("#divtocDHTML #move")
        x_toc=toc_tree.location['x']
        y_toc=toc_tree.location['y']
        w_toc=toc_tree.size['width']
        pyautogui.moveTo(x_toc + x_fr + (w_toc/2), y_toc + y_fr + 75)
        time.sleep(2)
        pyautogui.dragTo(x_fr+300,y_fr+150)
        time.sleep(2)
        
        """ 
            Step 09:From the Data area, add Product, Subcategory to the Active Report.
            Expect to see the Live Preview show the Product, Subcategory field added to the canvas.
        """
        utillobj.switch_to_default_content(pause=1)
        metaobj.datatree_field_click("Product,Subcategory", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 55, 60)
        
        """ 
            Step 10:Click Run.
            Expect to see the following Active Report with 3 records for 
            Product, Subcategory within Product, Category.
            Accessories group is again the default.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.synchronize_with_number_of_element("iframe[id^='ReportIframe-']", 1, 120)
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_number_of_element("#divtocDHTMLDummy > img", 1, 35)
        
        """    
            Step 11:Double click the TOC icon, then move it away from the report
            Click the plus(+) symbol next to the Stereo System line in the 
            Table of Contents
            Expect to see the Table of Contents expand to display all 
            Product, Subcategories for Stereo Systems.
            The Active Report still shows Accessories.
        """
        toc_btn=driver.find_element_by_css_selector("#divtocDHTMLDummy > img")
        utillobj.click_on_screen(toc_btn, 'middle', 2)
        ia_runobj.create_table_data_set("table[id='IBI_Page0'][summary= 'Summary']", Test_Case_ID+"run_Ds02.xlsx")
        ia_runobj.verify_table_data_set("table[id='IBI_Page0'][summary= 'Summary']", Test_Case_ID+"run_Ds02.xlsx", "Step 11:01: Verify report data in runtime")
        
        """    
            Step 12:Click the Stereo Systems text in the Table of Contents to filter the Active Report.
            Expect to see the following 5 line report for all Subcategories within Category Stereo Systems.
            Product Category should now display as Stereo Systems.
        """
        ia_runobj.expand_toc('Stereo Systems')
        item_list=['Table of Contents', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Boom Box', 'Home Theater Systems', 'Receivers','Speaker Kits','iPod Docking Station', 'Televisions', 'Video Production', 'View Entire Report (On/Off)', 'Remove Table of Contents']
        ia_runobj.verify_toc_item(item_list, "Step 12:01:Verify item list in toc table after exapnding stereo systems")
        
        """    
            Step 13:Close the report, and window
        """
        

if __name__ == "__main__":
    unittest.main()