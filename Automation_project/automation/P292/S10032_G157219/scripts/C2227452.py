'''
Created on Dec 06, 2017

@author: Praveen Ramkumar
Testcase ID :http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227452
Testcase Name :Verify Sorting on Dimension and Measure
'''
import unittest, time
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase


class C2227452_TestClass(BaseTestCase):

    def test_C2227452(self):
        
        TestCase_ID = "C2227452"
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)        
        
        """
            Step 01: Launch IA Report mode:http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        
        utillobj.infoassist_api_login('report','baseapp/wf_retail_lite','P292/S10032_infoassist_6', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        
        """
            Step 02:Drag "Product,Category" to the "Across" container in the Query pane
        """
        metaobj.drag_drop_data_tree_items_to_query_tree('Product,Category', 1, 'Across',0)
        parent_css='#queryTreeWindow tr:nth-child(5) td'
        resultobj.wait_for_property(parent_css, 1,string_value='Product,Category',expire_time=15)
        
        """
            Step 03:Select "Product,Category" in "Across" container > Click "Down" button in the Field Tab
        """
        
        metaobj.querytree_field_click("Product,Category",1,0)
        ribbonobj.select_ribbon_item('Field','down')
        time.sleep(3)
        
        """
            Step 04:Verify sorting is applied
        """
        
#         ia_resultobj.create_across_report_data_set('TableChart_1',1,1,2,7,TestCase_ID+'_DataSet_01.xlsx')
        ia_resultobj.verify_across_report_data_set('TableChart_1',1,1,2,7,TestCase_ID+'_DataSet_01.xlsx','Step 04:Verify sorting is applied')
        
    
        """
            Step 05:Drag "Product,Subcategory" to the "By" container in the Query pane
        """
        metaobj.drag_drop_data_tree_items_to_query_tree('Product,Subcategory', 1, 'By',0)
        parent_css='#queryTreeWindow tr:nth-child(4) td'
        resultobj.wait_for_property(parent_css, 1,string_value='Product,Subcategory',expire_time=15)
        
        """
            Step 06:Select "Product,Subcategory" in "By" container > Click "Down" button in the Field Tab
        """
        metaobj.querytree_field_click("Product,Subcategory",1,0)
        ribbonobj.select_ribbon_item('Field','down')
        time.sleep(3)
        
        """
            Step 07:Verify sorting is applied
        """
        
#         ia_resultobj.create_across_report_data_set('TableChart_1',3,1,21,7,TestCase_ID+'_DataSet_02.xlsx')
        ia_resultobj.verify_across_report_data_set('TableChart_1',3,1,21,7,TestCase_ID+'_DataSet_02.xlsx','Step 07:Verify sorting is applied')
        
        """
            Step 08:Drag "Cost of Goods" to the "Sum" container in the Query pane
        """
        
        metaobj.drag_drop_data_tree_items_to_query_tree('Cost of Goods', 1, 'Sum',0)
        parent_css='#queryTreeWindow tr:nth-child(4) td'
        resultobj.wait_for_property(parent_css, 1,string_value='Cost of Goods',expire_time=15)
        
        """
            Step 09:Select "Cost of Goods" in "Sum" container > Click "Down" button in the Field Tab
        """
        
        metaobj.querytree_field_click("Cost of Goods",1,0)
        ribbonobj.select_ribbon_item('Field','down')
        time.sleep(3)
        
        """
            Step 10:Verify sorting is applied and a "Cost of Goods" sort field appears in the Query pane, under By container
        """
        
#         ia_resultobj.create_across_report_data_set('TableChart_1',3,1,21,7,TestCase_ID+'_DataSet_03.xlsx')
        ia_resultobj.verify_across_report_data_set('TableChart_1',3,1,21,7,TestCase_ID+'_DataSet_03.xlsx','Step 10.1:Verify sorting is applied')
        metaobj.verify_query_pane_field('By','Cost of Goods',1,'Step 10.2: Verify Query pane and Preview ',color='Trolley_Grey',font_style='italic')
        """
            Step 11:Click "Save" > "C2227452" > Click "Save"
        """
        
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(TestCase_ID)
        time.sleep(8)
        
        """
            Step 12:Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp        
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
            Step 13:Reopen saved FEX:http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2227452.fex&tool=Report 
        """
        utillobj.infoassist_api_edit(TestCase_ID,'Report', 'P292/S10032_infoassist_6',mrid='mrid',mrpass='mrpass')
        time.sleep(8)
        
        """
            Step 14:Verify Query pane and Preview 
        """
        
#         ia_resultobj.create_across_report_data_set('TableChart_1',3,1,21,7,TestCase_ID+'_DataSet_04.xlsx')
        ia_resultobj.verify_across_report_data_set('TableChart_1',3,1,21,7,TestCase_ID+'_DataSet_04.xlsx','Step 14.1:Verify sorting is applied')
        metaobj.verify_query_pane_field('By','Cost of Goods',1,'Step 14.2: Verify Query pane and Preview ',color='Trolley_Grey',font_style='italic')
        metaobj.verify_query_pane_field('By','Product,Subcategory',2,"Step 14.3: Verify query pane")
        metaobj.verify_query_pane_field('Across','Product,Category',1,"Step 13.4: Verify query pane")
        
        """
            Step 15:Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
      
if __name__ == '__main__':
    unittest.main()     
        