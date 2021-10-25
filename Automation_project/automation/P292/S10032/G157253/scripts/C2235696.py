'''
Created on Nov 27, 2017

@author: BM13368
TestCase ID : http://172.19.2.180/testrail/index.php?/cases/view/2235696
TestCase Name : Verify Preview context menus
'''
import unittest, time
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_ribbon, ia_run 
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class C2235696_TestClass(BaseTestCase):

    def test_C2235696(self):
        
        Test_Case_ID = "C2235696"
        driver=self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        ia_run_obj=ia_run.IA_Run(self.driver)
        """
            Step 01:Launch IA Report mode:
            http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','ibisamp/car','P292/S10032_infoassist_4', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        """
            Step 02:Double-click CAR and SALES
        """
        metaobj.datatree_field_click('CAR', 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('SALES', 2, 1)
        time.sleep(6)
         
        """ 
            Step 03:Drag COUNTRY into "Across" container in the Query pane
        """
        metaobj.drag_drop_data_tree_items_to_query_tree('COUNTRY',1,'Across',0)
        time.sleep(6)
         
        """
            Verify preview
        """
        ia_resultobj.verify_across_report_data_set('TableChart_1', 2, 6, 10, 6, Test_Case_ID+"_Ds01.xlsx","Step 03; Verify report dataset")
        time.sleep(6)
        
        """ 
            Step 04:Right-click across field COUNTRY on Preview > Verify menu
        """
        ia_resultobj.select_field_on_canvas('TableChart_1', -1, click_type=1)
        time.sleep(1)
        a=['Filter Values...', 'Sort', 'Break', 'Visibility', 'Create Group...', 'Change Title...', 'Drill Down', 'Delete']
        utillobj.select_or_verify_bipop_menu(verify='true', expected_popup_list=a, msg='Step 04:01: Verify live-preview field right click menu')
        time.sleep(1)
        
        """ 
            Step 05:Select Sort -> Sort -> Sort -> Descending
        """ 
        utillobj.select_or_verify_bipop_menu('Sort')
        time.sleep(0.5)
        utillobj.select_or_verify_bipop_menu('Sort')
        time.sleep(0.5)
        utillobj.select_or_verify_bipop_menu('Descending')
        time.sleep(8)  
        
        """ 
            Step 06:Verify Preview
        """   
        ia_resultobj.verify_across_report_data_set('TableChart_1', 2, 6, 10, 6, Test_Case_ID+"_Ds02.xlsx","Step 06; Verify report dataset") 
        time.sleep(6)
        
        """ 
            Step 07:Right-click CAR column on Preview > Verify menu
        """
        ia_resultobj.select_field_on_canvas('TableChart_1', 0, click_type=1)
        time.sleep(1)
        a=['Filter Values...', 'Sort', 'Break', 'Visibility', 'Create Group...', 'Change Title...', 'Drill Down', 'More', 'Delete']
        utillobj.select_or_verify_bipop_menu('Change Title...', verify='true', expected_popup_list=a, msg='Step 07:01: Verify CAR field right click menu') 
         
        """ 
            Step 08:Select "Change Title..." > Verify dialog
        """   
        btn_css = "div[id^='BiDialog'] [class*='window-active']"
        utillobj.verify_object_visible(btn_css, True, "Step 08:01: Verify Dialog is visible")
        edit_title_obj=self.driver.find_element_by_css_selector(btn_css)
        actual_value=edit_title_obj.find_element_by_css_selector("input").get_attribute('value')
        utillobj.asequal(actual_value, 'CAR', "Step 08:02: Verify Edit Title text value appears.")  
        """ 
            Step 09:Type "Car:" > Click OK
        """  
        text_field = edit_title_obj.find_element_by_css_selector("input")
        utillobj.set_text_field_using_actionchains(text_field, 'Car:')
        utillobj.click_dialog_button(btn_css,"OK")
        time.sleep(5)   
        """ 
            Step 10:Verify Preview
        """
        ia_resultobj.verify_across_report_data_set('TableChart_1', 2, 6, 10, 6, Test_Case_ID+"_Ds03.xlsx","Step 10; Verify report dataset")
        """ 
            Step 11:Right-click on any SALES values > Verify menu
            Step 12:Select "Drill Down" > Verify dialog
        """
        ia_resultobj.select_field_on_canvas('TableChart_1', 1, click_type=1)
        time.sleep(1)
        a=['Filter Values...', 'Sort', 'Visibility', 'Change Title...', 'Edit Format', 'Drill Down', 'More', 'Delete']
        utillobj.select_or_verify_bipop_menu('Drill Down', verify='true', expected_popup_list=a, msg='Step 12:01: Right-click on any SALES values > Verify menu')
        ia_ribbobj.create_drilldown_report("report", verify_default_drilldown_type=True)    
            
        """ 
            Step 13:Select "Web Page" radio button
            Step 14:In the URL input box, type > http://informationbuilders.com
            Step 15:Click OK
        """ 
        ia_ribbobj.create_drilldown_report("webpage", url_value="http://informationbuilders.com", click_ok='yes')    
             
        """ 
            Step 16:Verify Preview
        """
        ia_resultobj.verify_across_report_data_set('TableChart_1', 2, 6, 10, 6, Test_Case_ID+"_Ds04.xlsx","Step 16; Verify report dataset")
        ia_resultobj.verify_autolink("TableChart_1","30200",50,"Step 16:01: Verify Report preview with hyperlinks", link_color='cerulean_blue_2')
        time.sleep(3)
        """ 
            Step 17:Click "Save" > save as "C2235696" > Click "Save"
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        """     
            Step 18:Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """  
        utillobj.infoassist_api_logout()   
        """
            Step 19:Reopen saved FEX:
            http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2235696.fex&tool=Report
        """ 
        Test_Case_ID='C2235696'
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10032_infoassist_4', mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)   
        """ 
            Step 20:Verify Preview
        """
        ia_resultobj.verify_across_report_data_set('TableChart_1', 2, 6, 10, 6, Test_Case_ID+"_Ds04.xlsx","Step 20; Verify report dataset")
        ia_resultobj.verify_autolink("TableChart_1","30200",50,"Step 20:01: Verify Report preview with hyperlinks", link_color='cerulean_blue_2')
        time.sleep(3)
        """ 
            Step 21:Click Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5) 
        WebDriverWait(driver, 100).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "[id^='ReportIframe']"))) 
        """ 
            Step 22:Click on value 30200 > Verify site is displayed in a new window
            www.informationbuilders.com
        """
        ia_run_obj.verify_table_data_set("table[summary='Summary']", Test_Case_ID+"_Ds04.xlsx", " Step 22:01: Verify runtime report")
        ia_run_obj.select_and_verify_drilldown_report_field("table[summary='Summary']", 3, 4, expected_drill_down_tooltip='Drill Down 1', underline=True, msg="Step 22:02:")
        time.sleep(8)
        utillobj.switch_to_window(1)
        time.sleep(10)
        drill=("https://www.ibi.com/" in driver.current_url)
        utillobj.asequal(True, drill, "Step 22:03: Verify Information Builder page is displayed")
        time.sleep(3)       
        self.driver.close()
        time.sleep(3)
        utillobj.switch_to_window(0)
        time.sleep(3)
        
        """
            Step 23:Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
        
if __name__ == "__main__":
    unittest.main()