'''
Created on September 11, 2018
@author: Varun

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227617
'''
import unittest, time
from selenium.webdriver.common.by import By
from common.lib import utillity,core_utility
from common.lib.basetestcase import BaseTestCase
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon

class C6707459_TestClass(BaseTestCase):
    
    def test_C6707459(self):
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C6707459'
        
        """
            TESTCASE OBJECTS
        """
        utillobj = utillity.UtillityMethods(self.driver)
        core_utils = core_utility.CoreUtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
    
        """
        Step01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
             
        """
        Step02: Click "Change" in the Home Tab > Select "Bubble" chart type
        """
        ribbonobj.change_chart_type('bubble_chart')
        time.sleep(5)
               
        """
        Step03: Double-click "Gross Profit"
        Step04: Double-click "Product,Category"
        Step05: Drag and drop "Sale,Quarter" (from Sales_Related > Trasaction Date, Simple) to the Rows bucket
        """
        metaobj.datatree_field_click("Gross Profit", 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(5)
        metaobj.drag_drop_data_tree_items_to_query_tree('Sale,Quarter', 1, 'Rows', 0)
        time.sleep(8)
         
        """
        Step06: Verify Preview
        """
        parent_css="#MAINTABLE_wbody1 text[class*='rowLabel']"
        resultobj.wait_for_property(parent_css, 4)
        metaobj.verify_query_pane_field('Rows', 'Sale,Quarter', 1, "Step 06.00: Verify Rows")
            
        time.sleep(5)
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Gross Profit', "Step 06.01: Verify Y-Axis Title")
        expected_label=['1','2','3','4']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows', 'Sale Quarter', expected_label, "Step 06.02: Verify row header and labels")
        expected_xval_list=[]
        expected_yval_list=['0', '7M', '14M', '21M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 06.03:Verify XY labels")
        resultobj.verify_number_of_circle('MAINTABLE_wbody1', 28, 29, 'Step 06.04: Verify number of Circle displayed')
            
        time.sleep(5)
        bar=['Sale Quarter:1', 'Gross Profit:$20,953,693.47', 'Product Category:Stereo Systems', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g4!mmarker!r0!c0", bar, "Step 06.05: Verify bar value")
          
        """
        Step07:Hover over any point from Quarter 1 > Verify menu with "Drill up to Sale Year" and "Drill down to" sub menu "Sale Month" and "Product Subcategory"
        Step08: Select "Drill up to Sale Year"
        """
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g4!mmarker!r0!c0",'Drill up to Sale Year')
             
        """
        Step09:Verify Preview
        """
        parent_css="#MAINTABLE_wbody1 text[class*='rowLabel']"
        resultobj.wait_for_property(parent_css, 6)
        metaobj.verify_query_pane_field('Rows', 'Sale,Year', 1, "Step 09.00: Verify Rows")
        time.sleep(5)
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Gross Profit', "Step 09.01: Verify Y-Axis Title")
        expected_label=['2011', '2012', '2013', '2014', '2015', '2016']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows', 'Sale Year', expected_label, "Step 09.02: Verify column header and labels")
        expected_xval_list=[]
        expected_yval_list=['0','10M', '20M','30M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 09.03:Verify XY labels")
        resultobj.verify_number_of_circle('MAINTABLE_wbody1', 42, 43, 'Step 09.04: Verify number of Circle displayed')
           
        time.sleep(5)
        bar = ['Sale Year:2011', 'Gross Profit:$1,589,557.67', 'Product Category:Televisions', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g5!mmarker!r0!c0", bar, "Step 09.05: Verify bar value")
         
        """
        Step10: Click Run
        """
        time.sleep(5)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        core_utils.switch_to_new_window()

        """
        Step11: Hover over "Stereo Systems" for Year 2014 > select "Drill down to" > "Sale Quarter"
        """
        parent_css="#MAINTABLE_wbody1 text[class*='rowLabel']"
        resultobj.wait_for_property(parent_css, 6)

        time.sleep(5)
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Gross Profit', "Step 11.00: Verify Y-Axis Title")
        expected_label=['2011', '2012', '2013', '2014', '2015', '2016']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows', 'Sale Year', expected_label, "Step 11.01: Verify row header and labels")
        expected_xval_list=[]
        expected_yval_list=['0','10M','20M','30M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 11.02:Verify XY labels")
        resultobj.verify_number_of_circle('MAINTABLE_wbody1', 42, 43, 'Step 11.03: Verify number of Circle displayed')
         
        time.sleep(5)
        bar=['Sale Year:2014', 'Gross Profit:$10,776,019.32', 'Product Category:Stereo Systems', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g4!mmarker!r3!c0", bar, "Step 11.04: Verify bar value")
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g4!mmarker!r3!c0",'Drill down to->Sale Quarter',verify_menu1=['Sale Quarter', 'Product Subcategory'],msg="Step 11.05: Verify Drill down to menu")
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g4!mmarker!r3!c0",'Drill down to->Sale Quarter')
         
        """
        Step12: Verify output
        """         
        parent_css="#MAINTABLE_wbody1 text[class*='rowLabel']"
        resultobj.wait_for_property(parent_css, 4)
          
        time.sleep(5)
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Gross Profit', "Step 12.00: Verify Y-Axis Title")
        expected_label=['1', '2', '3', '4']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows', 'Sale Quarter', expected_label, "Step 12.01: Verify column header and labels")
        expected_xval_list=[]
        expected_yval_list=['0', '0.9M', '1.8M', '2.6M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 12.02:Verify XY labels")
        resultobj.verify_number_of_circle('MAINTABLE_wbody1', 4, 5, 'Step 12.03: Verify number of Circle displayed')
         
        time.sleep(5)
        bar=['Sale Quarter:1', 'Gross Profit:$2,539,408.57', 'Product Category:Stereo Systems', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill up to Sale Year', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mmarker!r0!c0", bar, "Step 12.04: Verify bar value")

        """
        Step13: Click Save in the toolbar
        Step14: Save as "C2158150" > Click Save
        """
        core_utils.switch_to_previous_window()
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
          
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
          
        """
        Step15: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2) 
          
        """
        Step16: Reopen fex using IA API:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158150.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_3',mrid='mrid',mrpass='mrpass')
           
        """
        Step17: Verify canvas
        """
        parent_css="#MAINTABLE_wbody1 text[class*='rowLabel']"
        resultobj.wait_for_property(parent_css, 6)
        metaobj.verify_query_pane_field('Rows', 'Sale,Year', 1, "Step 17.00: Verify Rows")
        time.sleep(5)
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Gross Profit', "Step 17.01: Verify Y-Axis Title")
        expected_label=['2011', '2012', '2013', '2014', '2015', '2016']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows', 'Sale Year', expected_label, "Step 17.02: Verify column header and labels")
        expected_xval_list=[]
        expected_yval_list=['0','10M', '20M', '30M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 17.03:Verify XY labels")
        resultobj.verify_number_of_circle('MAINTABLE_wbody1', 42, 43, 'Step 17.04: Verify number of Circle displayed')
           
        time.sleep(5)
        bar = ['Sale Year:2011', 'Gross Profit:$1,589,557.67', 'Product Category:Televisions', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g5!mmarker!r0!c0", bar, "Step 17.05: Verify bar value")
                       
if __name__ == '__main__':
    unittest.main()