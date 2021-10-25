'''
Created on Nov 24, 2017

@author: BM13368
TestCase Name : Verify Filter Pane context menu
TestCase ID : http://172.19.2.180/testrail/index.php?/cases/view/2227524
'''
import unittest, time
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_ribbon 
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase

class C2227524_TestClass(BaseTestCase):

    def test_C2227524(self):
        
        Test_Case_ID = "C2227524"
        driver=self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        """
            Step 01 : Launch IA Report mode:
            http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','ibisamp/CAR','P292/S10032_infoassist_4', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        """
            Step 02 : Double-click CAR and SALES
        """
        metaobj.datatree_field_click('CAR', 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('SALES', 2, 1)
        time.sleep(4)
        """
            Step 03 :Drag COUNTRY into the Filter pane
        """
        metaobj.datatree_field_click('COUNTRY', 1, 1, 'Filter')
        parent_css="#dlgWhere"
        resultobj.wait_for_property(parent_css, 1)
        """
            Step 04 : Verify dialog
        """
        status=driver.find_element_by_css_selector("#dlgWhere").is_displayed()
        utillobj.asequal(status, True, "Step 04:01: Verify Filter Dialog")
        
        """
            Step 05 : Click the "Constant" dropdown menu
            Step 06 :Select "Parameter"
            Step 07:Click OK > OK
        """
        ia_ribbobj.create_parameter_filter_condition('Simple', 'dummy', True)
        
        """ 
            Step 08:Verify Filter pane
        """
        metaobj.verify_filter_pane_field('COUNTRY Equal to Simple Parameter (Name: COUNTRY)', 1, "Step 08:01 Verify the filter pane")
        """ 
            Step 09:Right-click filter in the Filter pane > Verify menu
            Step 10:Select "Edit"
        """
        parent_css=driver.find_element_by_css_selector("#qbFilterBox div>table>tbody>tr>td>img[src*='apply']")
        utillobj.click_on_screen(parent_css, 'middle', 1)
        time.sleep(1)
        a=['Edit','Delete','Exclude']
        utillobj.select_or_verify_bipop_menu('Edit', verify='true', expected_popup_list=a, msg='Step 09:01, Step 10:01: Verify menu displayed')
        
        """ 
            Step 11:Verify dialog in Edit mode
        """
        status=self.driver.find_element_by_css_selector("#dlgWhere span[class*='selected lead']").is_displayed()
        utillobj.asequal(status, True, "Step 11:01: Verify dialog in Edit Mode")
        
        """ 
            Step 12:Click Cancel > Cancel
        """
        parent_elem=driver.find_element_by_css_selector("#dlgWhere_btnCancel img")
        utillobj.click_on_screen(parent_elem, 'middle', 0)
        """ 
            Step 13:Right-click filter in the Filter pane > Select "Exclude"
        """
        parent_css=driver.find_element_by_css_selector("#qbFilterBox div>table>tbody>tr>td>img[src*='apply']")
        utillobj.click_on_screen(parent_css, 'left', 1)
        time.sleep(1)
        utillobj.select_or_verify_bipop_menu('Exclude')
        """ 
            Step 14:Verify Filter pane
        """
        status=driver.find_element_by_css_selector("#qbFilterBox div>table>tbody>tr>td>img[src*='remove']").is_displayed()
        utillobj.asequal(status, True, "Step 14:01: Verify pane filter icon is shown as exclude icon")
        
        """ 
            Step 15:Click "Save" > save as "C2227524" > Click "Save"
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        """ 
            Step 16:Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        """ 
            Step 17:Reopen saved FEX:
            http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2227524.fex&tool=Report
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10032_infoassist_4', mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        """ 
            Step 18:Verify Filter pane and successful restore
        """
        status=driver.find_element_by_css_selector("#qbFilterBox div>table>tbody>tr>td>img[src*='remove']").is_displayed()
        utillobj.asequal(status, True, "Step 14:01: Verify pane filter icon is shown as exclude icon")
        """ 
            Step 19 :Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
    

if __name__ == "__main__":
    unittest.main()