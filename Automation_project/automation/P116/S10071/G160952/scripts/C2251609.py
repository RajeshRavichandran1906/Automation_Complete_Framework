'''
Created on Jan 24, 2018
@author: Niranjan 
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea,visualization_ribbon,visualization_metadata,active_miscelaneous,ia_run, ia_resultarea
from common.lib import utillity

class C2251609_TestClass(BaseTestCase):

    def test_C2251609(self):
        """
        TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        vis_ribbon_obj=visualization_ribbon.Visualization_Ribbon(self.driver)
        miscelaneousobj=active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        TestCase_ID = 'C2251609'
        
        """        
        Step 01 : Launch IA Report mode:
        http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/ggorder&item=IBFS%3A%2FWFC%2FRepository%2FS10071
        """
        utillobj.infoassist_api_login('document','ibisamp/ggorder','P116/S10071_1', 'mrid', 'mrpass')
        result_obj.wait_for_property("#iaCanvasCaptionLabel", 1, expire_time=60, string_value='Document')
        """
        Step 02 : Select Category, Product,Unit Sales to get a report        
        """ 
        time.sleep(2)
        metaobj.datatree_field_click("Order,Date", 2, 1)
        parent_css='#queryTreeWindow tr:nth-child(4) td'
        result_obj.wait_for_property(parent_css, 1, expire_time=15)
        metaobj.datatree_field_click("Product,Code", 2, 1)
        parent_css='#queryTreeWindow tr:nth-child(5) td'
        result_obj.wait_for_property(parent_css, 1, expire_time=15)
        metaobj.datatree_field_click("Product", 2, 1)
        parent_css='#queryTreeWindow tr:nth-child(3) td'
        result_obj.wait_for_property(parent_css, 1, expire_time=15)
        metaobj.datatree_field_click("Order,Number", 2, 1)
        parent_css='#queryTreeWindow tr:nth-child(3) td'
        result_obj.wait_for_property(parent_css, 1, expire_time=15)
        
        """
        Step 03 : Select DropDown from Insert tab
        Drag the prompt right to the report     
        """
        vis_ribbon_obj.select_ribbon_item('Insert', 'drop_down')
        time.sleep(3)
        ia_resultobj.drag_drop_document_component("#Prompt_1", "#TableChart_1", 180, 0)
#         vis_ribbon_obj.repositioning_document_component('5', '1')
        """
        Step 04 : Select List box from Insert tab
        Drag the prompt right to the report     
        """
        vis_ribbon_obj.select_ribbon_item('Insert', 'list')
        time.sleep(3)
        utillobj.synchronize_with_number_of_element("#Prompt_2", 1, 35)
        ia_resultobj.drag_drop_document_component('#Prompt_2', '#Prompt_1', 60, 0)
        """
        Step 05 : Select Radio button from Insert tab
        Drag the prompt right to the report      
        """
        vis_ribbon_obj.select_ribbon_item('Insert', 'radio_button')
        time.sleep(3)
        utillobj.synchronize_with_number_of_element("#Prompt_3", 1, 35)
        ia_resultobj.drag_drop_document_component('#Prompt_3', '#Prompt_2', 70, 0)
        time.sleep(3)
        
        """
        Step 06 : Right click on Drop down button select properties
        In Active Dashboard Properties ssign UNIT SALES in 'Field'. Make sure Include All is checked already and Condition is Equal to.
        Click Ok.
        """
        canvas_css=self.driver.find_element_by_css_selector("#theCanvas")
        utillobj.click_on_screen(canvas_css, coordinate_type='left', click_type=0)
        time.sleep(1)
        result_obj.choose_right_click_menu_item_for_prompt('#Prompt_1', 'Properties')
        time.sleep(5)
        source={'select_field':'Order,Number', 'verify_condition':'Equal to', 'verify_includeall':True}
        result_obj.customize_active_dashboard_properties(source=source, msg="06: Verify the Active Dashboard Prompts")
        time.sleep(3)
        """
        Step 07 : Right click on List box and select properties
        Assign Order,Date in property of list box. Make sure Condition is set as Equal to and Include All is checked.
        Select 'OK'      
        """
        result_obj.choose_right_click_menu_item_for_prompt('#Prompt_2', 'Properties')
        time.sleep(5)
        source={'select_field':'Order,Date', 'verify_condition':'Equal to', 'verify_includeall':True}
        result_obj.customize_active_dashboard_properties(source=source, msg="07: Verify the Active Dashboard Prompts")
        """
        Step 08 : Right click on Radio button and select properties
        Assign Product,Code in property of radio button. Make sure Condition is set as Equal to and Include All is checked.
        Select 'OK'    
        """
        result_obj.choose_right_click_menu_item_for_prompt('#Prompt_3', 'Properties')
        time.sleep(5)
        source={'select_field':'Product,Code', 'verify_condition':'Equal to','verify_includeall':True}
        result_obj.customize_active_dashboard_properties(source=source, msg="08: Verify the Active Dashboard Prompts")
        """
        Step 09 : Run the Document
        """
        vis_ribbon_obj.select_tool_menu_item('menu_run')
        utillobj.synchronize_with_number_of_element("[id^='ReportIframe']", 1, 60)
        utillobj.switch_to_frame()
        miscelaneousobj.verify_page_summary(0, '241of241records,Page1of5', 'Step 9.1 : Verify the Report Heading')
        column_list=['Order Date', 'Product Code', 'Product', 'Order Number']
        miscelaneousobj.verify_column_heading('ITableData0', column_list, 'Step 9.2 : Verify the column heading')
#         utillobj.create_data_set('ITableData0', 'I0r', TestCase_ID+'_Ds01.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', TestCase_ID+'_Ds01.xlsx', 'Step 9.3 : Verify table data after Run.')
        """
        Step 10 : Choose "2136" value from drop-down and notice that report is filtered according to selection
        Verify 1 of 241 record is returned.     
        """
        select_css="#combobox_dPROMPT_1 select"
        utillobj.select_dropdown(select_css, 'visible_text', '2136')
        miscelaneousobj.verify_page_summary(0, '1of241records,Page1of1', 'Step 10.1 : Verify the Report Heading')
#         utillobj.create_data_set('ITableData0', 'I0r', TestCase_ID+'_Ds02.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', TestCase_ID+'_Ds02.xlsx', 'Step 10.2 : Verify table data after Run.')
        """
        Step 11 : Choose "06/01/96" value from List box and notice that report is filtered according to selection
        Verify 10 of 241 records are returned. All rows Order Date are 06/01/96.      
        """
        ia_runobj.select_active_dashboard_prompts('listbox', '#list_dPROMPT_2', ['06/01/96'])
        miscelaneousobj.verify_page_summary(0, '10of241records,Page1of1', 'Step 11.1 : Verify the Report Heading')
#         utillobj.create_data_set('ITableData0', 'I0r', TestCase_ID+'_Ds03.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', TestCase_ID+'_Ds03.xlsx', 'Step 11.2 : Verify table data after Run.')
        """
        Step 12 : Choose "B144" value from radio button and notice that report is filtered according to selection
        Verify24 of 241 records are returned. All rows show Product Code as B144.   
        """
        ia_runobj.select_active_dashboard_prompts('radio', '#PROMPT_3_cs', ['B144'])
        miscelaneousobj.verify_page_summary(0, '24of241records,Page1of1', 'Step 12.1 : Verify the Report Heading')
#         utillobj.create_data_set('ITableData0', 'I0r', TestCase_ID+'_Ds04.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', TestCase_ID+'_Ds04.xlsx', 'Step 12.2 : Verify table data after Run.')
           
if __name__ == '__main__':
    unittest.main()
        
        
        
        
