'''
Created on Oct 4, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7215
Test Case =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2203715
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,visualization_ribbon,visualization_metadata,ia_styling
from common.pages import ia_resultarea
from common.lib import utillity
import unittest,time
from selenium.common.exceptions import NoSuchElementException

class C2203715_TestClass(BaseTestCase):

    def test_C2203715(self):
        
#         driver = self.driver #Driver reference object created'
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultareaobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_stylingobj = ia_styling.IA_Style(self.driver)
        """
        Step 01: Execute the AR-RP-001.fex.
        """
        utillobj.infoassist_api_login('report', 'ibisamp/ggsales', 'P116/S7072', 'mrid', 'mrpass')
        element_css="div[id='HomeTab'] div[id='HomeFormatType']"
        utillobj.synchronize_with_number_of_element(element_css, 1, expire_time=30)
        
        """
        Step 02: On the Format tab, in the Output Types group, click Active Report.
        """
        ribbonobj.change_output_format_type('active_report')  
        
        """
        Step 03: Select data from the left pane (Dimensions and Measures) Category, Product ID, Product, State, Unit Sales, Dollar Sales.
        """
        metadataobj.datatree_field_click('Category', 2, 1)
        time.sleep(6)
        metadataobj.datatree_field_click('Product ID', 2, 1)
        time.sleep(6)
        metadataobj.datatree_field_click('Product', 2, 1)
        time.sleep(6)
        metadataobj.datatree_field_click('State', 2, 1)
        time.sleep(6)
        metadataobj.datatree_field_click('Unit Sales', 2, 1)
        time.sleep(6)
        metadataobj.datatree_field_click('Dollar Sales', 2, 1)        
        time.sleep(8)
        resultareaobj.verify_report_data_set('TableChart_1', 19, 6, 'C2203715_Ds01.xlsx','Step 03.1: Verify data is displayed in the Live Preview pane')

        """
        Step 04: Click Run command.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', "Step 04.1: Verify Page summary")
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2203715_Ds02.xlsx','Step 04.2: Verify dataset')
        utillobj.switch_to_default_content(pause=2)
        ribbonobj.select_tool_menu_item("menu_save")
        time.sleep(5)
        utillobj.ibfs_save_as("AR_RP_C2203713")
        time.sleep(6)
        
        """
        Step 05: Edit the AR-RP-001.fex via IA
        """
        utillobj.infoassist_api_edit("AR_RP_C2203713", 'Report', 'S7072')
        element_css="div[id='HomeTab'] div[id='HomeFormatType']"
        utillobj.synchronize_with_number_of_element(element_css, 1, expire_time=30)
             
        """
        Step 06: Highlight any column under report.
        """
        metadataobj.querytree_field_click('Category', 1)
        time.sleep(8)
        field = self.driver.find_element_by_xpath("//div[contains(text(),'Field - Category')]").is_displayed()
        utillobj.asequal(field,True,'Step 06.1: Verify that Field-Category menu is available in the menu bar')
        filter_menu = self.driver.find_elements_by_xpath("//div[contains(text(),'Filter')]/br/..")
        filter_1 = filter_menu[1].is_displayed()
        utillobj.asequal(filter_1,True,'step 06.2: Verify Filter menu is available in the menu bar')
        sort = self.driver.find_element_by_xpath('//div[@id="FieldSortUp"]/..').is_displayed()
        utillobj.asequal(sort,True,'Step 06.3: Verify Sort menu is available in the menu bar')
        field_break = self.driver.find_element_by_xpath('//div[@id="FieldPageBreak"]/..').is_displayed() 
        utillobj.asequal(field_break,True,'Step 06.4: Verify break menu is available in the menu bar')
        style = self.driver.find_element_by_css_selector('[id*="FieldStyleCluster"]').is_displayed()
        utillobj.asequal(style,True,'Step 06.5: Verify style menu is available in the menu bar')
        
        links = self.driver.find_element_by_css_selector('[id="FieldLinksCluster"]').is_displayed()
        utillobj.asequal(links,True,'Step 06.6: Verify links  menu is available in the menu bar')
        
        
        """
        Step 07: Click Sub Footer link.
        """
        ia_stylingobj.create_sub_header_footer('Sub_footer', 'GGSALES SUB FOOTING')
        time.sleep(6)
        '''
        self.driver.find_element_by_css_selector('[id="FieldSubFoot"]').click()
        time.sleep(2)
        footer_popup = self.driver.find_element_by_xpath("//div[contains(text(),'Sub Header & Sub Footer')]").text
        utillobj.asequal(footer_popup,'Sub Header & Sub Footer','Step 07.1: Verify Sub Header & Sub Footer pop up is opened')
        
        """
        Step 08: Enter text as "GGSALES SUB FOOTING".
        """
        time.sleep(8)
        actionChains = ActionChains(driver)
        actionChains.send_keys('GGSALES SUB FOOTING').perform()
        self.driver.find_element_by_css_selector('#subheaderDlg #okBtn').click()  
        '''
        ribbonobj.select_tool_menu_item('menu_run')
        time.sleep(3)
#         iframe=driver.find_element_by_css_selector("[id^=ReportIframe-]")
#         x_fr=iframe.location["x"]
#         y_fr=iframe.location["y"]
        utillobj.switch_to_frame(pause=2)
        
#         self.driver.switch_to_frame(self.driver.find_element_by_tag_name('iframe'))
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', "Step 08.1: Verify Page summary")
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2203715_Ds02.xlsx','Step 08.2: Verify dataset')
        footer = self.driver.find_element_by_css_selector('[id="THEAD_0_8_1_0"] div span').is_displayed()
        utillobj.asequal(footer,True,'Step 08.3: Verify that "GGSALES SUB FOOTING" is displayed under each category')
        
        """
        Step 09: Click any column heading and click Hide Subtitles.
        """
        miscelanousobj.select_menu_items('ITableData0', 0, 'Hide Subtitles')
        
        try:
            footer = self.driver.find_element_by_css_selector('[id="THEAD_0_8_1_0"] div span').is_displayed()
            self.fail('Subtitles is diaplaying')
        
        except NoSuchElementException:
            footer = False
            utillobj.asequal(footer,False,'Step 09: Veify that Sub Header/Sub Footer is not visible on a report.')
        
        """
        Step 10: Click any column heading and click Show Subtitles
        """
        miscelanousobj.select_menu_items('ITableData0', 0, 'Show Subtitles')
        footer = self.driver.find_element_by_css_selector('[id="THEAD_0_8_1_0"] div span').is_displayed()
        utillobj.asequal(footer,True,'Step 10: Veify that Sub Header/Sub Footer is again visible on a report')
        utillobj.switch_to_default_content(pause=2)
        self.driver.switch_to_default_content()
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(4)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()