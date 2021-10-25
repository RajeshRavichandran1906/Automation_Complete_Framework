'''
Created on Dec 5, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2298488
TestCase Name = Verify Join and Define field created in Reporting Object
'''

import unittest, time
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, wf_reporting_object, ia_ribbon, define_compute

class C2298488_TestClass(BaseTestCase):

    def test_C2298488(self):
        
        """ Test case variable """
        Test_Case_ID = "C2298488"
        
        """ Test case Objects """
        driver = self.driver
        ia_ribbonobj= ia_ribbon.IA_Ribbon(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        calculate_obj=define_compute.Define_Compute(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        wfreportobj = wf_reporting_object.Wf_Reporting_Object(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        
        """
        Step 01 : Launch Reporting Object with car:http://machine:port/ibi_apps/ia?tool=reportingobject&master=ibisamp/empdata&item=IBFS%3A%2FWFC%2FRepository%2FS10032%2F
        """
        utillobj.infoassist_api_login('reportingobject', 'ibisamp/empdata', 'P292/S10032_infoassist_4', 'mrid', 'mrpass')
        parent_css="#applicationButton img"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(6)
         
        """    
        Step 02: Click on Join > new > Add New > TRAINING.MAS
        """
        wfreportobj.select_ro_tree_item("Joins")
        time.sleep(2)
        wfreportobj.select_ro_tree_item("Joins", click_type = 0)
        time.sleep(5)
        new_btn = driver.find_element_by_css_selector("#HomeNew img")
        utillobj.click_on_screen(new_btn, 'middle', click_type=0)
        time.sleep(3)
        elem='#dlgJoin_btnOK img'
        resultobj.wait_for_property(elem, 1)
        ia_ribbonobj.create_join("ibisamp","training", new_join=False)
        time.sleep(3)
        join_btn=driver.find_element_by_css_selector("#dlgJoin_btnOK img")
        utillobj.default_left_click(object_locator=join_btn)
        time.sleep(5)
        
        """
        step03: Click on Define > new > add Expenses / 2 to the Define tool (Define_1) 
        """
        wfreportobj.select_ro_tree_item("Defines")
        time.sleep(2)
        wfreportobj.select_ro_tree_item("Defines", click_type = 0)
        time.sleep(5)
        new_btn = driver.find_element_by_css_selector("#HomeNew img")
        utillobj.click_on_screen(new_btn, 'middle', click_type=0)
        time.sleep(3)
        elem='#fldCreatorOkBtn'
        resultobj.wait_for_property(elem, 1)
        calculate_obj.enter_define_compute_parameter("Define_1", "D12.2", "EXPENSES", 1)
        time.sleep(5)
        calculate_obj.select_calculation_btns("div->two")
        
        """
        step04: Click OK 
        """
        calculate_obj.close_define_compute_dialog("ok")
        time.sleep(5)
        
        """    
        Step05: Click Report > Open
        """
        wfreportobj.select_ro_tree_item("Report")
        time.sleep(2)
        wfreportobj.select_ro_tree_item("Report", click_type = 0)
        time.sleep(5)
        open_btn = driver.find_element_by_css_selector("#HomeOpen img")
        utillobj.click_on_screen(open_btn, 'middle', click_type=0)
        time.sleep(3)
        utillobj.switch_to_window(1)
        time.sleep(8)
        
        """
        step06: Verify that Expenses (a joined field) and Define_1 are available   
        """
        parent_css="[id^=QbMetaDataTree]"
        resultobj.wait_for_property(parent_css, 1, expire_time=15)
        time.sleep(2)
        metaobj.verify_data_pane_field('Measures/Properties',"EXPENSES",2,"Step 06.01")
        metaobj.verify_data_pane_field('Measures/Properties',"Define_1",3,"Step 06.02")
        
        """    
        Step 07: Save and Exit Report
        """
        ribbonobj.select_tool_menu_item('save')
        time.sleep(5)
        utillobj.click_dialog_button("div[id^='BiDialog']", "OK")
        time.sleep(3)
        ribbonobj.select_tool_menu_item('menu_exit')
        time.sleep(5)
        utillobj.switch_to_window(0)
        time.sleep(5)
        parent_css="#applicationButton img"
        resultobj.wait_for_property(parent_css, 1)
        
        """    
        Step 08: Save Reporting Object as "C2298488"
        """
        time.sleep(2)
        wfreportobj.select_ro_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """
        Step 09: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
        Step 10: Reopen saved RO: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2298488.fex&tool=reportingobject
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'reportingobject', 'S10032_infoassist_4',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
        
        """    
        Step 11: Right-click 'Report' > Open
        """
        parent_css="#applicationButton img"
        resultobj.wait_for_property(parent_css, 1)
        wfreportobj.select_ro_tree_item("Report")
        time.sleep(2)
        wfreportobj.select_ro_tree_item("Report",1,'Open')
        time.sleep(5)
        utillobj.switch_to_window(1)
        time.sleep(8)
        
        """
        step 12: Verify Data panel  
        """
        parent_css="[id^=QbMetaDataTree]"
        resultobj.wait_for_property(parent_css, 1, expire_time=15)
        time.sleep(2)
        metaobj.verify_data_pane_field('Measures/Properties',"EXPENSES",2,"Step 12.01")
        metaobj.verify_data_pane_field('Measures/Properties',"Define_1",3,"Step 12.02")
        
        """
        step 13: Exit Report  
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(5)
        utillobj.switch_to_window(0)
        time.sleep(8)
        parent_css="#applicationButton img"
        resultobj.wait_for_property(parent_css, 1)
        
        """
        Step 14: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()