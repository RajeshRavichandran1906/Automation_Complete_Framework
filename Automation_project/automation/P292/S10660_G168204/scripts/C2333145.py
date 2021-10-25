'''
Created on Nov 7, 2017

@author: BM13368
Testcase_Name :Create Datagrid Chart 
Testcase_ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2333145&group_by=cases:section_id&group_id=171044&group_order=asc
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_ribbon
from common.lib import utillity
from selenium.webdriver.common.by import By

class C2333145_TestClass(BaseTestCase):


    def test_C2333145(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2333145'
        
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        """
            Step 01 : Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660&tool=chart&master=wf_retail_lite
        """
        utillobj.infoassist_api_login('chart','new_retail/wf_retail_lite','P292/S10660_chart_2', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        """
            Step 02 : Select Format > Chart type > Other > HTML5 > Datagrid
        """
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbonobj.select_other_chart_type('html5', 'html5_DataGrid', 6, ok_btn_click=True)
        """
            Step 03 : Double click Product,Category
        """
        metadataobj.datatree_field_click('Product,Category', 2, 0)
        time.sleep(3)
        parent_css1="#TableChart_1 .colHeaderScroll text"
        resultobj.wait_for_property(parent_css1, 1)
        heading = ['Product Category']
        resultobj.verify_grid_column_heading('#TableChart_1',heading, 'Step 03: Verify first column title')
        row_val=['Accessories']
        resultobj.verify_grid_row_val('TableChart_1',row_val,'Step 04: verify grid 1st row value')
        """
            Verification : Product Category is added to Rows bucket and shows in preview as first column.
        """
        metadataobj.verify_query_pane_field('Rows', 'Product,Category', 1, "Step 03::01: Verify Product Category is visible underneath Rows bucket")
        """
            Step 04 : Double click Cost of Goods, Discount, Gross Profit and Revenue
        """
        metadataobj.datatree_field_click('Cost of Goods', 2, 0)
        time.sleep(3)
        metadataobj.datatree_field_click('Gross Profit', 2, 1)
        time.sleep(2)
        metadataobj.datatree_field_click('Discount', 2, 2)
        time.sleep(2)
        metadataobj.datatree_field_click('Revenue', 2, 3)
        time.sleep(2)
        """
            Verification : All measures are added to Measures bucket and show as additional columns in preview.
        """
        metadataobj.verify_query_pane_field('Measure', 'Cost of Goods', 1, "Step 04::01: Verify Cost of Goods is visible underneath Measure bucket")
        metadataobj.verify_query_pane_field('Cost of Goods', 'Gross Profit', 1, "Step 04::02: Verify Gross Profit is visible underneath Measure bucket")
        metadataobj.verify_query_pane_field('Gross Profit', 'Discount', 1, "Step 04::03: Verify Discount is visible underneath Measure bucket")
        metadataobj.verify_query_pane_field('Discount', 'Revenue', 1, "Step 04::03: Verify Discount is visible underneath Measure bucket")
        
        parent_css1="#TableChart_1 .colHeaderScroll text"
        resultobj.wait_for_property(parent_css1, 1)
        heading = ['Product Category', 'Cost of Goods', 'Gross Profit','Discount','Revenue']
        resultobj.verify_grid_column_heading('TableChart_1',heading, 'Step 04:04: Verify data-grid column title')
        row_val=['Accessories','$89,753,898.00','$39,854,440.53','$6,014,845.52','$129,608,338.53']
        resultobj.verify_grid_row_val('TableChart_1',row_val,'Step 04:05: verify grid 1st row values')
        
        """
            Step 05 : Click Auto Drill button in the Run With section of Format tab.
        """
        ribbonobj.select_ribbon_item('Format', 'Auto_Drill')
        
        """
            Step 06 : Run, hover over measure columns
            Verification : Each cell is a link (the cursor changes to pointing finger).
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        parent_css1="#jschartHOLD_0 .colHeaderScroll text"
        resultobj.wait_for_property(parent_css1, 1)
        expected_tooltip=['Customer Country ISO-3166 Code:AR', 'Cost of Goods:$3,798,511.00', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("jschartHOLD_0","riser!s0!g0!mcellFill!r1!c3!",expected_tooltip, "Step 06:01: verify the default tooltip values")
        
        """
            Step 07 : Click the cell of Accessories and Cost of Goods
        """
        resultobj.select_default_tooltip_menu("jschartHOLD_0", "riser!s0!g0!mcellFill!r1!c3!", "Drill down to Product Subcategory")
        """
            Verification : Chart for Accessories subcategories displays.
        """
        heading = ['Product Subcategory', 'Cost of Goods', 'Gross Profit','Discount','Revenue']
        resultobj.verify_grid_column_heading('jschartHOLD_0',heading, 'Step 07:01: Verify data-grid column title')
        row_val=['Charger','$2,052,711.00','$1,970,123.91','$187,485.88','$4,022,834.91']
        resultobj.verify_grid_row_val('jschartHOLD_0',row_val,'Step 07:02: verify grid 1st row values')
        
        """
            Step 08: Click Save in the toolbar > Save as "C2333145" > Click Save 
        """
        utillobj.switch_to_default_content(pause=1)
        time.sleep(1)
        obj1=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(obj1,Test_Case_ID + '_Actual_step06', image_type='actual',x=1, y=1, w=-1, h=-1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        utillobj.infoassist_api_logout()
        time.sleep(2)
        """
            Step 09 :Run the chart with API call
            http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/P292_S10660&BIP_item=C2333145.FEX
        """
        utillobj.active_run_fex_api_login(Test_Case_ID+".fex", "S10660_chart_2", 'mrid', 'mrpass')
        time.sleep(6)
        """
            Step 10: Close output window.
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
            Step 11: Restore the saved fex using API
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660%2FC2333145.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S10660_chart_2', mrid='mrid', mrpass='mrpass')
        parent_css1="#TableChart_1 .colHeaderScroll text"
        resultobj.wait_for_property(parent_css1, 1)
        heading = ['Product Category', 'Cost of Goods', 'Gross Profit','Discount','Revenue']
        resultobj.verify_grid_column_heading('TableChart_1',heading, 'Step 11:01: Verify data-grid column title')
        row_val=['Accessories','$89,753,898.00','$39,854,440.53','$6,014,845.52','$129,608,338.53']
        resultobj.verify_grid_row_val('TableChart_1',row_val,'Step 11:02: verify grid 1st row values')
        
        """
            Step 12: Logout using API
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        


if __name__ == "__main__":
    unittest.main()