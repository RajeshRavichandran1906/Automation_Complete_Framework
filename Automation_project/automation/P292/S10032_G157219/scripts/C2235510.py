'''
Created on Nov 28, 2017

@author: Pavithra 

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2235510
TestCase Name = Verify Chart to Report Conversion
'''
import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea
from common.lib.basetestcase import BaseTestCase

class C2235510_TestClass(BaseTestCase):

    def test_C2235510(self):
        
        Test_Case_ID = "C2235510"
        driver = self.driver
        driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        
        """        
            Step 01:Launch IA Chart mode:
                    http://machine:port/ibi_apps/ia?tool=Chart&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('chart','baseapp/wf_retail_lite','P292/S10032_infoassist_3', 'mrid', 'mrpass')
        parent_css="#pfjTableChart_1 g.chartPanel"
        resobj.wait_for_property(parent_css, 1,expire_time=20)
        time.sleep(5)
        
        """
            Step 02:Double-click "Product,Category", "Cost of Goods", and "Revenue" 
        """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        parent_css="#queryTreeWindow tr:nth-child(8) td"
        resobj.wait_for_property(parent_css, 1, string_value='Product,Category', with_regular_exprestion=True,expire_time=50)
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        parent_css="#queryTreeWindow tr:nth-child(7) td"
        resobj.wait_for_property(parent_css, 1, string_value='CostofGoods', with_regular_exprestion=True,expire_time=50)
        metaobj.datatree_field_click("Revenue", 2, 1)
        parent_css="#queryTreeWindow tr:nth-child(8) td"
        resobj.wait_for_property(parent_css, 1, string_value='Revenue', with_regular_exprestion=True,expire_time=50)
        time.sleep(5)
        resobj.verify_xaxis_title("TableChart_1", 'Product Category', "Step 02.1: Verify X-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 02.2: Verify XY Label')
        expected_label_list=['Cost of Goods', 'Revenue']
        resobj.verify_riser_legends('TableChart_1', expected_label_list, 'Step : 02.3 Verify Legends ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s1!g0!mbar!', 'bar_green', 'Step 02.4: Verify Color')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar!', 'bar_blue1', 'Step 02.5: Verify Color')
        resobj.verify_number_of_riser("TableChart_1", 1, 14, 'Step 02.6: Verify the total number of risers displayed on preview')
        time.sleep(5)
         
        """
            Step 03:Click "Report" in the Home Tab ribbon
        """
        ribbonobj.select_ribbon_item('Home', 'Report')
        parent_css="#queryTreeWindow tr:nth-child(2) td"
        resobj.wait_for_property(parent_css, 1, string_value='Sum', with_regular_exprestion=True,expire_time=50)
        time.sleep(2)
 
        """
            Step 04:Verify Chart is converted to Report
        """
        ia_resultobj.verify_across_report_data_set('TableChart_1',2,3,7,3,Test_Case_ID+'_DataSet_01.xlsx','Step 04 : Verify report')
 
        """
            Step 05:Select View Tab > Click "Switch Report" button
            
            Step 06:Verify Chart1 and Report1 (only) are displayed in the list
            
            Step 07:Select the "Chart1" fex from the Switch Report menu
        """
        ribbonobj.select_ribbon_item('View', 'switch_report', verify=True,expected_popup_list=['Chart1', 'Report1'],msg="Step 06:Verify witch Report button option",opt='Chart1')
        time.sleep(2)


        """
            Step 08:Verify Chart is displayed
        """
        parent_css="#TableChart_1 text.xaxisOrdinal-title"
        resobj.wait_for_property(parent_css, 1,string_value='ProductCategory', with_regular_exprestion=True,expire_time=50)
        time.sleep(5)
        resobj.verify_xaxis_title("TableChart_1", 'Product Category', "Step 08.1: Verify X-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 08.2: Verify XY Label')
        expected_label_list=['Cost of Goods', 'Revenue']
        resobj.verify_riser_legends('TableChart_1', expected_label_list, 'Step 08.3: Verify Legends ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s1!g0!mbar!', 'bar_green', 'Step 08.4: Verify Color')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar!', 'bar_blue1', 'Step 08.5: Verify Color')
        resobj.verify_number_of_riser("TableChart_1", 1, 14, 'Step 08.6: Verify the total number of risers displayed on preview')
        time.sleep(5) 

        """
            Step 09:Click "IA" menu > Close > Click "No"
        """
        ribbonobj.select_tool_menu_item('menu_close')
        time.sleep(8)
        btn_No=driver.find_element_by_id('btnNo')
        utillobj.default_left_click(object_locator=btn_No)

        """
            Step 10:Click "Save" > Save Report1 as "C2235510" > Click "Save" 
        """
        time.sleep(6)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
 
        """
            Step 11:Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
 
        """
            Step 12:Reopen saved FEX:
                    http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2235510.fex&tool=Report
        """
        time.sleep(5)
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S10032_infoassist_3',mrid='mrid', mrpass='mrpass')
        parent_css="#queryTreeWindow tr:nth-child(2) td"
        resobj.wait_for_property(parent_css, 1, string_value='Sum', with_regular_exprestion=True,expire_time=50)
        """
            Step 13:Verify successful restore
        """
        time.sleep(5)
        ia_resultobj.verify_across_report_data_set('TableChart_1',2,3,7,3,Test_Case_ID+'_DataSet_01.xlsx','Step 13 : Verify report')
        """
            Step 14:Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(2)
 
if __name__ == '__main__':
    unittest.main() 

        