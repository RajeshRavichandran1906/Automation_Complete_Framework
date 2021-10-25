'''
Created on November 15, 2018

@author: Prabhakaran

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5852254
TestCase Name = Visualization Edit options
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.wftools.visualization import Visualization
from common.pages.wf_legacymainpage import Wf_Legacymainpage 
from common.pages.visualization_resultarea import Visualization_Resultarea 

class C5852254_TestClass(BaseTestCase):

    def test_C5852254(self):
        
        """
        CLASS OBJECT
        """
        visual = Visualization(self.driver)
        legacy_homepage = Wf_Legacymainpage(self.driver)
        visual_result = Visualization_Resultarea(self.driver)
        utility = UtillityMethods(self.driver)
        
        """
        COMMON VARIABLES
        """
        LONG_WAIT_TIME = 180
        MEDIUM_WAIT_TIME = 90
        SHORT_WAIT_TIME = 60
        TESTCASE_ID = 'C5852254'
        DATASET_NAME = TESTCASE_ID + '.xlsx'
        
        """
            STEP 01 : Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10863&tool=idis&master=baseapp/wf_retail_lite
        """
        utility.invoke_infoassist_api_login('idis','baseapp/wf_retail_lite','P292_S10863/G432726', 'mrid', 'mrpass')
        visual.wait_for_visible_text("#pfjTableChart_1 text[class='title']", "Drop Measures or Sorts into the Query Pane", LONG_WAIT_TIME)
        
        """
            STEP 02 : Select "Home" > "Visual" > "Insert" (dropdown) > "Grid"
        """
        visual.select_ribbon_item('Home', 'insert->Grid')
        visual.wait_for_visible_text("#pfjTableChart_2 text[class='title']", "Drag fields here to create grid", MEDIUM_WAIT_TIME)
        
        """
            STEP 03 : Double click "Product,Category"
        """
        visual.double_click_on_datetree_item('Product,Category', 1)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_fmg text", "Product Category", SHORT_WAIT_TIME)
        
        """
            STEP 04 : Highlight "Product,Category" (in Query pane) > Right mouse click > "Delete"
        """
        visual.right_click_on_field_under_query_tree('Product,Category', 1, 'Delete')
        visual.wait_for_visible_text("#pfjTableChart_2 text[class='title']", "Drag fields here to create grid", SHORT_WAIT_TIME)
        
        """
            STEP 05 : Drag "Product,Category" to Rows
        """
        visual.drag_field_from_data_tree_to_query_pane('Product,Category', 1, 'Rows')
        visual.wait_for_visible_text("#MAINTABLE_wbody1_fmg text", "Product Category", SHORT_WAIT_TIME)
        
        """
            STEP 06 : Double click "Revenue"
        """
        visual.double_click_on_datetree_item('Revenue', 1)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_fmg .colHeaderScroll text", "Revenue", SHORT_WAIT_TIME)
        
        """
            STEP 07 : Drag "Gross Profit" to "Measure" under "Revenue"
        """
        visual.drag_field_from_data_tree_to_query_pane('Gross Profit', 1, 'Revenue')
        visual.wait_for_visible_text("#MAINTABLE_wbody1_fmg .colHeaderScroll path + text", "Gross Profit", SHORT_WAIT_TIME)
        
        """
            STEP 08 : Verify the following is displayed
        """
        visual.verify_field_listed_under_querytree('Rows', 'Product,Category', 1, 'Step 08.01')
        visual.verify_field_listed_under_querytree('Measure', 'Revenue', 1, 'Step 08.02')
        visual.verify_field_listed_under_querytree('Measure', 'Gross Profit', 2, 'Step 08.03')
        visual_result.verify_grid_column_heading('MAINTABLE_wbody1', ['Product Category', 'Revenue', 'Gross Profit'], 'Step 08.04 : Verify grid table column headings')
        row_lables = self.driver.find_elements_by_css_selector("#MAINTABLE_wbody1 .rowLabels text")
        actual_row_labels = [label.text.strip() for label in row_lables]
        utility.asequal(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], actual_row_labels, 'Step 08.05 : Verify grid table row labels')
        #visual_result.create_grid_data_set('MAINTABLE_wbody1',7, DATASET_NAME)
        visual_result.verify_grid_data_set('MAINTABLE_wbody1',7, DATASET_NAME, 'Step 08.04 : Verify grid data values')
        visual.verify_number_of_risers("#pfjTableChart_1 .groupPanel .risers rect", 4, 3, 'Step 08.05 : Verify number of default risers')
        
        """
            STEP 09 : Click "IA" > "Save" > "C5852254" > "Save"
        """
        visual.save_as_visualization_from_menubar(TESTCASE_ID)
        
        """
            STEP 10 : Logout: http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual.logout_visualization_using_api()
        
        """
            STEP 11 : Log on to WF: http://machine:port/ibi_apps/
        """
        utility.invoke_legacyhomepage('mrid', 'mrpass')
        visual.wait_for_visible_text("[id^='BiToolBar'] .bi-label", " Resources", LONG_WAIT_TIME)
        
        """
            STEP 12 : Highlight "C5852254" > Right mouse click > Verify Edit options
            Note : Execute this step from legacy home page.
        """
        legacy_homepage.expand_repository_tree('P292_S10863->G432726->'+TESTCASE_ID)
        legacy_homepage.right_click_repository_tree(TESTCASE_ID)
        utility.select_bipopup_list_item('Edit With...')
        utility.verify_bipopup_list_item(['InfoAssist', 'Text Editor'], 'Step 12.01 : Verify InfoAssist and Text Editor are displayed')
        
        """
            STEP 13 : Select Edit With... > InfoAssist
        """
        utility.select_bipopup_list_item('InfoAssist')
        visual.switch_to_new_window()
        visual.wait_for_visible_text("#MAINTABLE_wbody1_fmg .colHeaderScroll path + text", "Gross Profit", LONG_WAIT_TIME)
        
        """
            STEP 14 : Verify the following is displayed.
        """
        visual.verify_field_listed_under_querytree('Rows', 'Product,Category', 1, 'Step 14.01')
        visual.verify_field_listed_under_querytree('Measure', 'Revenue', 1, 'Step 14.02')
        visual.verify_field_listed_under_querytree('Measure', 'Gross Profit', 2, 'Step 14.03')
        visual_result.verify_grid_column_heading('MAINTABLE_wbody1', ['Product Category', 'Revenue', 'Gross Profit'], 'Step 14.04 : Verify grid table column headings')
        row_lables = self.driver.find_elements_by_css_selector("#MAINTABLE_wbody1 .rowLabels text")
        actual_row_labels = [label.text.strip() for label in row_lables]
        utility.asequal(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], actual_row_labels, 'Step 14.05 : Verify grid table row labels')
        #visual_result.create_grid_data_set('MAINTABLE_wbody1',7, DATASET_NAME)
        visual_result.verify_grid_data_set('MAINTABLE_wbody1',7, DATASET_NAME, 'Step 14.06 : Verify grid data values')
        visual.verify_number_of_risers("#pfjTableChart_1 .groupPanel .risers rect", 4, 3, 'Step 14.07 : Verify number of default risers')
        
        """
            STEP 15 : Logout:http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual.switch_to_previous_window()
        visual.logout_visualization_using_api
        
if __name__ == "__main__":
    unittest.main()