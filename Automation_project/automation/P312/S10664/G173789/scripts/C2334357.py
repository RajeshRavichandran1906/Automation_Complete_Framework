'''
Created on Jan 02, 2018

@author: Robert

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2334357
Test_Case Name : Paperclipping on YMD date format 
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.visualization import Visualization
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.lib import utillity
from common.lib.core_utility import CoreUtillityMethods

class C2334357_TestClass(BaseTestCase):

    def test_C2334357(self):
        
        """   
            TESTCASE VARIABLES 
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metadata = visualization_metadata.Visualization_Metadata(self.driver)
        visual = Visualization(self.driver)
        coreutils = CoreUtillityMethods(self.driver)
        visul_result = visualization_resultarea.Visualization_Resultarea(self.driver)
        visul_ribbon=visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """
            STEP 01 : Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is)
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=empdata  
        """
        utillobj.infoassist_api_login('idis','ibisamp/empdata','P312/S10664_paperclipping_2', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 svg text", 'DropMeasuresorSortsintotheQueryPane', 200)
        
        """   
            STEP 02 : Double click "HIREDATE" and "SALARY" to add fields
        """
        metadata.datatree_field_click('HIREDATE', 2, 1)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", 'HIREDATE', 120)
        
        metadata.datatree_field_click('SALARY', 2, 1)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody1_f text[class='yaxis-title']", 'SALARY', 120)
        
        """
            STEP 03 : Lasso on first 6 riser in preview 
        """
        source_element=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 rect[class*='riser!s0!g0!mbar!']")
        target_element=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 rect[class*='riser!s0!g5!mbar!']")
        visual.create_lasso(source_element, target_element, source_element_location='bottom_left')
        
        """
            Step 4. Click "Group HIREDATE selection"    
        """
        visul_result.select_or_verify_lasso_filter(select="Group HIREDATE Selection", msg='Step 4. Click on the Group selection')
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", 'HIREDATE_1', 120)
        
        """
            Step 5. Verify preview updated with group    
        """ 
        xaxis_value="HIREDATE_1"
        yaxis_value="SALARY"
        parentcss="MAINTABLE_wbody1_f"
        visul_result.verify_xaxis_title(parentcss, xaxis_value, "Step 05:a(i) Verify X-Axis Title")
        visul_result.verify_yaxis_title(parentcss, yaxis_value, "Step 05:a(ii) Verify Y-Axis Title")
        expected_xval_list=['89/03/01 and 89/03/15 and 89/04/03...', '89/07/12', '90/01/08', '90/02/05', '90/02/07', '90/03/05', '90/03/14', '90/03/21', '90/03/30', '90/04/02', '90/04/03', '90/04/11', '90/05/01', '90/05/09', '90/05/14', '90/05/16', '90/06/04', '90/07/11', '90/07/18', '90/09/12', '90/10/10', '90/11/07', '90/12/05', '91/01/07', '91/01/09', '91/02/13', '91/03/07', '91/03/12', '91/03/13', '91/03/20', '91/05/08', '91/05/13']
        expected_yval_list=['0', '100K', '200K', '300K', '400K', '500K', '600K']
        visul_result.verify_riser_chart_XY_labels(parentcss, expected_xval_list, expected_yval_list, "Step 05:c(iii):Verify XY labels")
        visul_result.verify_number_of_riser('MAINTABLE_wbody1_f', 1, 32, 'Step 5d. Verify no of risers')
        
        """
            Step 6. Right click on "HIREDATE_1" > Edit group    
        """
        metadata.querytree_field_click('HIREDATE_1', 1, 1, 'Edit Group...')
        utillobj.synchronize_with_visble_text("#dynaGrpsValuesTree table>tbody>tr:first-child", '89/07/12', 80)
         
        """
            Step 7. Scroll down and verify group created
        """
        groupvalue_table = self.driver.find_element_by_id('dynaGrpsValuesTree')
        coreutils.python_move_to_element(groupvalue_table)
        utillobj.scroll_down_and_find_item_using_mouse("#dynaGrpsValuesTree table>tbody>tr>td", '89/05/10')
        
        actaul_group_values = [value.text.strip() for value in self.driver.find_elements_by_css_selector("#dynaGrpsValuesTree table>tbody>tr>td") if value.text.strip() != ''][-7:]
        expected_group_values = ['89/03/01 and 89/03/15 and 89/04/03 and 3 more', '89/03/01', '89/03/15', '89/04/03', '89/04/05', '89/04/19', '89/05/10']
        utillobj.asequal(actaul_group_values, expected_group_values, 'Step 07.1 : verify group created')
            
        """    
            STEP  08 : Click Cancel    
        """
        metadata.close_ia_group_dialog(close_button='cancel')
        utillobj.synchronize_until_element_disappear("#dynaGrpsValuesTree", 40)
        
        
        """    
            STEP 09 : Click on Grouped riser    
            STEP 10 : Verify tooltip values
        """
        riser1_ele=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class='riser!s0!g0!mbar!']")
        utillobj.click_on_screen(riser1_ele, coordinate_type='middle', click_type=0)
        expected_tooltip_list=['1 item selected', 'Filter Chart', 'Exclude from Chart', 'Edit group HIREDATE_1', 'Rename group HIREDATE_1', 'Rename 89/03/01 and 89/03/15...', 'Ungroup 89/03/01 and 89/03/15...', 'Ungroup All']
        visul_result.select_or_verify_lasso_filter(verify=expected_tooltip_list, msg='Step 10. Verify tooltip values')
        
        """
            STEP 11 : Click Run  
        """
        visul_ribbon.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_window(1, pause=3)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody1_f text[class='yaxis-title']", 'SALARY', 120)
        
        """
            STEP 12 : STEP 12 : Hover on Grouped riser and verify tooltip value
        """
        xaxis_value="HIREDATE_1"
        yaxis_value="SALARY"
        parentcss="MAINTABLE_wbody1_f"
        visul_result.verify_xaxis_title(parentcss, xaxis_value, "Step 12:a(i) Verify X-Axis Title")
        visul_result.verify_yaxis_title(parentcss, yaxis_value, "Step 12:a(ii) Verify Y-Axis Title")
        expected_xval_list=['89/03/01 and 89/03/15 and 89/04/03 and 3 more', '89/07/12', '90/01/08', '90/02/05', '90/02/07', '90/03/05', '90/03/14', '90/03/21', '90/03/30', '90/04/02', '90/04/03', '90/04/11', '90/05/01', '90/05/09', '90/05/14', '90/05/16', '90/06/04', '90/07/11', '90/07/18', '90/09/12', '90/10/10', '90/11/07', '90/12/05', '91/01/07', '91/01/09', '91/02/13', '91/03/07', '91/03/12', '91/03/13', '91/03/20', '91/05/08', '91/05/13']
        expected_yval_list=['0', '100K', '200K', '300K', '400K', '500K', '600K']
        visul_result.verify_riser_chart_XY_labels(parentcss, expected_xval_list, expected_yval_list, "Step 12:c(iii):Verify XY labels")
        visul_result.verify_number_of_riser('MAINTABLE_wbody1_f', 1, 32, 'Step 12d. Verify no of risers')
        expected_tooltip_list=['HIREDATE_1:89/03/01 and 89/03/15 and 89/04/03 and 3 more', 'SALARY:$541,600.00', 'Filter Chart', 'Exclude from Chart']
        visual.verify_tooltip('riser!s0!g0!mbar!', expected_tooltip_list, 'Step 12e. Verify tooltip values')
        
        """   
            STEP 13 : Dismiss run window   
            STEP 14 : Logout using API (without saving)  
        """
        self.driver.close()
        
if __name__ == '__main__':
    unittest.main()