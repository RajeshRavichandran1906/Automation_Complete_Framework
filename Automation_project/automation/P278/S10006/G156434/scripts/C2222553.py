'''
Created on 30-NOV-2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2222553
TestCase Name = Verify Report with styling converted to Chart
'''
import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea,active_miscelaneous,ia_styling
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2222553_TestClass(BaseTestCase):

    def test_C2222553(self):
        
        Test_Case_ID = "C2222553"
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        active_misobj=active_miscelaneous.Active_Miscelaneous(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_styobj = ia_styling.IA_Style(self.driver)
        
        """
        Step 01: Launch IA Report mode
        http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10006
        """
        utillobj.infoassist_api_login('report','ibisamp/car','P278/S10006', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """
        Step 02. Select "COUNTRY","CAR","DEALER_COST","RETAIL_COST".      
        """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("CAR", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('DEALER_COST', 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('RETAIL_COST', 2, 1)
        
        """ 
        Step 03. Click Header and Footer in the Report Section   
        Step 04: In Page Header > type Page Header > set Font to Comic Sans MS > Font color to Blue > Background color to Yellow > Click Italic > Click Underline 
        Step 05: In Page Footer > type Page Footer > set Font to Comic Sans MS > Font color to Blue > Background color to Yellow > Click Italic > Click Underline
        Step 06: Click Apply > Click OK                              
        """
        ia_styobj.create_header_footer('ribbon','Page Header', 'Page Header', font_name='COMIC SANS MS', text_color='blue',background_color='yellow',italic=True,underline=True)
        time.sleep(2)
        ia_styobj.create_header_footer('frame', 'Page Footer', 'Page Footer', font_name='COMIC SANS MS', text_color='blue',background_color='yellow',italic=True,underline=True, btn_apply='btn_apply', btn_ok='btn_ok')
        
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 1, cell_no=1, bg_color='yellow', msg='Step 6: Page Header-IA-5846- Highlighted Header/Footer text background color is not applied')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 1, font_color='blue', text_value='Page Header', font_name='COMIC SANS MS', font_size='12pt', italic=True, underline=True, msg='Step 6.1:')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 2, cell_no=2, bg_color='yellow', msg='Step 6.2: Page Footer-IA-5846- Highlighted Header/Footer text background color is not applied')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 2, font_color='blue', text_value='Page Footer', font_name='COMIC SANS MS', font_size='10pt', italic=True, underline=True, msg='Step 6.3:')
        
        """
        Step 07: Click Dealer_Cost in the Query window
        """
        metaobj.querytree_field_click('DEALER_COST', 1, 0)
        
        """
        Step 08: Click Font Color > Select Magenta > Click OK
        """
        ribbonobj.select_ribbon_item('Field', 'fontcolour')
        time.sleep(2)
        ia_styobj.set_color('magenta')
        
        """
        Step 09: Click Retail_Cost in the Query window
        """
        metaobj.querytree_field_click('RETAIL_COST', 1, 0)
        
        """
        Step 10: Click Font Color > Select Cyan > Click OK
        """
        ribbonobj.select_ribbon_item('Field', 'fontcolour')
        ia_styobj.set_color('cyan')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 10.1: Verify Canvas column titles After Apply Style")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, "C2222564_Ds01.xlsx", 'Step 10.2: Verify report dataset After Apply Style')
        ia_resultobj.verify_report_cell_property("TableChart_1", 7,font_name='ARIAL',font_color='magenta', text_value='18,621', msg='Step 10.3: Verify cell property of DEALER_COST')
        ia_resultobj.verify_report_cell_property("TableChart_1", 8,font_name='ARIAL',font_color='cyan', text_value='22,369', msg='Step 10.4: Verify cell property of RETAIL_COST')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 1, cell_no=1, bg_color='yellow', msg='Step 10.5: Page Header-IA-5846- Highlighted Header/Footer text background color is not applied')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 1, font_color='blue', text_value='Page Header', font_name='COMIC SANS MS', font_size='12pt', italic=True, underline=True, msg='Step 10.6:')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 2, cell_no=2, bg_color='yellow', msg='Step 10.7: Page Footer-IA-5846- Highlighted Header/Footer text background color is not applied')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 2, font_color='blue', text_value='Page Footer', font_name='COMIC SANS MS', font_size='10pt', italic=True, underline=True, msg='Step 10.8:')
        
        
        """
        Step 11: Click Save in the toolbar > Save As C2222553 > click Save
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as("se_"+Test_Case_ID)
        time.sleep(5)
        
        """
        Step 12: Select Home Tab > Select Chart in Format Section
        """
        ribbonobj.select_ribbon_item('Home', 'chart')
        time.sleep(2)
        
        """
        Step 13: Verify Styling is converted over to the Chart
        """
        ia_resultobj.verify_chart_header_footer_property('TableChart_1', 1, bg_cell_no=1, bg_color='yellow', msg='Step 13: Page Header-IA-5846- Highlighted Header/Footer text background color is not applied')
        ia_resultobj.verify_chart_header_footer_property('TableChart_1', 1, font_color='blue', text_value='Page Header', font_name='COMIC SANS MS', font_size='12pt', italic=True, underline=True, msg='Step 13.1:')
        ia_resultobj.verify_chart_header_footer_property('TableChart_1', 2, bg_cell_no=2, bg_color='yellow', msg='Step 13.2: Page Footer-IA-5846- Highlighted Header/Footer text background color is not applied')
        ia_resultobj.verify_chart_header_footer_property('TableChart_1', 2, font_color='blue', text_value='Page Footer', font_name='COMIC SANS MS', font_size='10pt',italic=True, underline=True, msg='Step 13.3:')
        #Tooltip & Color
        time.sleep(5)
        utillobj.verify_chart_color('TableChart_1',"riser!s0!g0!mbar!",'magenta',"Step 13.4: Verify Chart color DEALER_COST- Known Product Failure CHART-881")
        time.sleep(5)
        utillobj.verify_chart_color('TableChart_1',"riser!s1!g0!mbar!",'cyan',"Step 13.5: Verify Chart color RETAIL_COST- Known Product Failure CHART-881")
        time.sleep(5)
        #Label
        x=['ENGLAND/JAGUAR', 'ITALY', 'JAPAN', 'W GERMANY']
        y=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        resultobj.verify_riser_chart_XY_labels('TableChart_1', x, y, "Step 13.6: Verify Chart XY labels")
        #Legends
        resultobj.verify_riser_legends('TableChart_1', ['DEALER_COST','RETAIL_COST'],"Step 13.7: Verify Chart Legend")
        #X axis Title    
        resultobj.verify_xaxis_title('TableChart_1', 'COUNTRY : CAR', 'Step 13.8: Verify xaxis Title')        
        
               
        
        """
        Step 14: Click Run and verify output
        """ 
        ribbonobj.select_tool_menu_item("toolbar_run")
        #screenshot
        time.sleep(15)
        element = self.driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(element, 'C2222553_Actual_Step14', image_type='actual')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)  
             
        #Tooltip & Color
        time.sleep(5)
        active_misobj.verify_active_chart_tooltip('jschart_HOLD_0',"riser!s0!g0!mbar!",['COUNTRY:  ENGLAND', 'CAR:  JAGUAR', 'DEALER_COST:  18,621'],"Step 14.1a: Verify Chart tooltip RETAIL_COST")
        utillobj.verify_chart_color('jschart_HOLD_0',"riser!s0!g0!mbar!",'magenta',"Step 14.1a: Verify Chart color DEALER_COST- Known Product Failure CHART-881")
        time.sleep(5)
        active_misobj.verify_active_chart_tooltip('jschart_HOLD_0',"riser!s1!g0!mbar!",['COUNTRY:  ENGLAND', 'CAR:  JAGUAR', 'RETAIL_COST:  22,369'],"Step 14.2a: Verify Chart tooltip RETAIL_COST")
        utillobj.verify_chart_color('jschart_HOLD_0',"riser!s1!g0!mbar!",'cyan',"Step 14.2a: Verify Chart color RETAIL_COST- Known Product Failure CHART-881")
        time.sleep(5)
        #Label
        x=['ENGLAND/JAGUAR', 'ITALY', 'JAPAN', 'W GERMANY']
        y=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', x, y, "Step 14.c Verify Chart XY labels")
        #Legends
        resultobj.verify_riser_legends('jschart_HOLD_0', ['DEALER_COST','RETAIL_COST'],"Step 14.d: Verify Chart Legend")
        #X axis Title    
        resultobj.verify_xaxis_title('jschart_HOLD_0', 'COUNTRY : CAR', 'Step 14.e: Verify xaxis Title')        
        
        """
        Step 15: Click Save in the toolbar > Save As C2222553_1 > click Save
        """
        time.sleep(2)
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)
        
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as("se_"+Test_Case_ID+ str("_1"))
        time.sleep(5)
        
        """    
        Step 19. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp   
        """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """
        Step 20. Reopen saved FEX: 
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2222553_1.fex&tool=Chart      
        """              
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        utillobj.infoassist_api_edit("se_"+Test_Case_ID + str("_1"), 'chart', 'S10006', mrid='mrid', mrpass='mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1 svg .title span")
        resultobj._validate_page(elem1)
        
        """
        Step 21: Verify Chart Preview
        """
        time.sleep(7)
        ia_resultobj.verify_chart_header_footer_property('TableChart_1', 1, bg_cell_no=1, bg_color='yellow', msg='Step 21: Page Header-IA-5846- Highlighted Header/Footer text background color is not applied')
        ia_resultobj.verify_chart_header_footer_property('TableChart_1', 1, font_color='blue', text_value='Page Header', font_name='COMIC SANS MS', font_size='12pt', italic=True, underline=True, msg='Step 21.1:')
        ia_resultobj.verify_chart_header_footer_property('TableChart_1', 2, bg_cell_no=2, bg_color='yellow', msg='Step 21.2: Page Footer-IA-5846- Highlighted Header/Footer text background color is not applied')
        ia_resultobj.verify_chart_header_footer_property('TableChart_1', 2, font_color='blue', text_value='Page Footer', font_name='COMIC SANS MS', font_size='10pt',italic=True, underline=True, msg='Step 21.3:')
        
        #screenshot
        time.sleep(15)
        element = self.driver.find_element_by_css_selector("#TableChart_1")
        utillobj.take_screenshot(element, 'C2222553_Actual_Step21', image_type='actual')
        #Tooltip & Color
        time.sleep(5)
        utillobj.verify_chart_color('TableChart_1',"riser!s0!g0!mbar!",'magenta',"Step 21a: Verify Chart color DEALER_COST- Known Product Failure CHART-881")
        time.sleep(5)
        utillobj.verify_chart_color('TableChart_1',"riser!s1!g0!mbar!",'cyan',"Step 21b: Verify Chart color RETAIL_COST- Known Product Failure CHART-881")
        time.sleep(5)
        #Label
        x=['ENGLAND/JAGUAR', 'ITALY', 'JAPAN', 'W GERMANY']
        y=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        resultobj.verify_riser_chart_XY_labels('TableChart_1', x, y, "Step 21c Verify Chart XY labels")
        #Legends
        resultobj.verify_riser_legends('TableChart_1', ['DEALER_COST','RETAIL_COST'],"Step 21c: Verify Chart Legend")
        #X axis Title    
        resultobj.verify_xaxis_title('TableChart_1', 'COUNTRY : CAR', 'Step 21d: Verify xaxis Title')        
        
        
if __name__ == '__main__':
    unittest.main()