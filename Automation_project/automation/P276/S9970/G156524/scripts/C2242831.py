'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2242831
TestCase Name = Autodrill menu wrong when parameter is used in query bucket
'''
import unittest, time
from common.pages import  visualization_ribbon, ia_run, visualization_metadata, metadata
from common.wftools import report
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase

class C2242831_TestClass(BaseTestCase):
    
    def test_C2242831(self):
        
        """
        Test case variable
        """
        Test_ID="C2242831"

        """
        Class & Objects
        """
        report_ = report.Report(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        meta=metadata.MetaData(self.driver)
        
        browser_type=utillobj.parseinitfile('browser')
        Test_Case_ID = Test_ID+"_"+browser_type
        
        """    
            Step 01 : Launch the IA report API with wf_retail_lite    
        """
        utillobj.infoassist_api_login('report','baseapp/wf_retail_lite','P276/S9970', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#queryTreeColumn", 'Sum', expire_time=40)
        time.sleep(8)
        
        """    
            Step 02 : Place Revenue in Sum    
        """
        #metaobj.datatree_field_click("Revenue", 2, 1)
#       metaobj.drag_drop_data_tree_items_to_query_tree('Revenue',1,'Sum',0)
        report_.drag_field_from_data_tree_to_query_pane('Revenue', 1, 'Sum')
        utillobj.synchronize_with_visble_text("#queryTreeColumn", 'Revenue', expire_time=10)
        meta.collapse_data_field_section('Measure Groups')
        time.sleep(2)
        
        """    
            Step 03 : Right click on By in the Query panel    
        """
        metaobj.querytree_field_click("By", 1, 1, "New Parameter")
        utillobj.synchronize_with_visble_text("#queryTreeColumn", 'Parameter1', expire_time=10)
        
        """    
            Step 04 : Drag both Product,Category and Store,Country under Parameter1 on the query panel    
        """
        #metaobj.drag_drop_data_tree_items_to_query_tree('Product,Category', 1, 'Parameter1',0)
        report_.drag_field_from_data_tree_to_query_pane('Product,Category', 1, 'Parameter1', 1)
        utillobj.synchronize_with_visble_text("#queryTreeColumn", 'Product,Category', expire_time=10)
        meta.collapse_data_field_section('Product')
        time.sleep(2)
        #metaobj.drag_drop_data_tree_items_to_query_tree('Store,Country', 1, 'Product,Category',0)
        report_.drag_field_from_data_tree_to_query_pane('Store,Country', 1, 'Product,Category', 1)
        utillobj.synchronize_with_visble_text("#queryTreeColumn", 'Store,Country', expire_time=10)
        
        """    
            Step 05 : Click Format tab > Autodrill button   
        """
        ribbonobj.select_ribbon_item("Format", "Auto_Drill")
        time.sleep(4)
        
        """    
            Step  6 : Click RUN     
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        
        utillobj.switch_to_frame(pause=2)
        time.sleep(3) 
        
        """    
            Step 07 : Accept the default of Product Category on the Auto Prompt screen and select the Run button    
        """
        iarun.select_amper_menu('Run')
        time.sleep(20)
        utillobj.switch_to_default_content(pause=2)
        time.sleep(2)
        utillobj.switch_to_frame(pause=2)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[name="wfOutput"]')
        time.sleep(4)
        utillobj.switch_to_frame(1, frame_css='iframe[src]', frame_height_value=0)
        #WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[src]')))
        #iarun.create_table_data_set("[summary= 'Summary']", Test_ID+"_Ds01.xlsx")
        #iarun.verify_table_data_set("[summary= 'Summary']", Test_ID+"_Ds01.xlsx", "Step 07a: Verify dataset")
        time.sleep(3)
        
        """    
            Step 08 : Click on Stereo Systems hyperlink. You should only see Drill down to Product Subcategory    
        """
        expected_tooltip_list = ['Drill down to Product Subcategory']
        iarun.verify_autolink_tooltip_values("table[summary='Summary']",6,1, expected_tooltip_list, "Step 08a: Only 'Drill down to Product Subcategory' is in the list of options")
        time.sleep(5)
        utillobj.switch_to_default_content(1)
        time.sleep(2)
        
        """   
            Step 09 : Click IA > Save As> Type C2242831 > click Save    
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    
            Step 10 : Logout of the IA API using the following URL.   
        """
        
if __name__ == '__main__':
    unittest.main()