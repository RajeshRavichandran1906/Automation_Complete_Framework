'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2197837
TestCase Name = Auto Drill errors when DBA restriction is applied to a dimension field
'''
import unittest, time
from common.pages import visualization_resultarea, visualization_ribbon, ia_run, visualization_metadata
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2197837_TestClass(BaseTestCase):
    
    def test_C2197837(self):
        
        Test_ID="C2197837"
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        Test_Case_ID = Test_ID+"_"+browser_type
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        
        """    
            Step 01 : Launch the IA report API with cardba
            http://hostname:port/ibi_apps/ia?tool=report&master=ibisamp/cardba&item=IBFS%3A%2FWFC%2FRepository%2FS9970%2
        """
        utillobj.infoassist_api_login('report','ibisamp/cardba','P276/S9970', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)   
        time.sleep(15)
        
        """    
            Step 02 : Place DEALER_COST in SUM and CAR in BY.  
        """
        #metaobj.datatree_field_click("DEALER_COST", 2, 1)
        metaobj.drag_drop_data_tree_items_to_query_tree('DEALER_COST',1,'BY',0)
        time.sleep(5)
        #metaobj.datatree_field_click("CAR", 2, 1)
        metaobj.drag_drop_data_tree_items_to_query_tree('CAR',1,'BY',0)
        time.sleep(5)
        metaobj.verify_query_pane_field("Sum", "DEALER_COST", 1, "Step 02a: Verify DEALER_COST added in Sum")
        metaobj.verify_query_pane_field("By", "CAR", 1, "Step 02b: Verify CAR added in BY")
        
        """    
            Step 03 : Click Run to see this run without Auto Drill    
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        utillobj.switch_to_frame(pause=2)
        time.sleep(3)
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", "Step 3a: Verify report data set")
        iarun.verify_table_cell_property("table[summary= 'Summary']", 3, 1, text='AUDI', font_color = 'gray8', msg='Step 3b')
        iarun.verify_table_cell_property("table[summary= 'Summary']", 7, 1, text='JENSEN', font_color = 'gray8', msg='Step 3c')
        iarun.verify_table_cell_property("table[summary= 'Summary']", 11, 1, text='TRIUMPH', font_color = 'gray8', msg='Step 3d')
        time.sleep(4)
        utillobj.switch_to_default_content()
        time.sleep(4)
        
        """   
            Step  04 : Click Format tab > Autodrill button   
        """
        ribbonobj.select_ribbon_item("Format", "Auto_Drill")
        time.sleep(15)
        
        """    
            Step 05 : Click Run.   
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        utillobj.switch_to_frame(pause=2)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", "Step 5a: Verify report data set")
        iarun.verify_table_cell_property("table[summary= 'Summary']", 3, 1, text='AUDI', font_color = 'cerulean_blue_2', msg='Step 5b')
        iarun.verify_table_cell_property("table[summary= 'Summary']", 7, 1, text='JENSEN', font_color = 'cerulean_blue_2', msg='Step 5c')
        iarun.verify_table_cell_property("table[summary= 'Summary']", 11, 1, text='TRIUMPH', font_color = 'cerulean_blue_2', msg='Step 5d')
        time.sleep(4)
        utillobj.switch_to_default_content()
        time.sleep(4)
        
        """    
            Step 06 : Click "Save" in the toolbar > Type C2197837 > Click "Save" in the Save As dialog   
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    
            Step 07 : Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    
        """
        
if __name__ == '__main__':
    unittest.main()
    
