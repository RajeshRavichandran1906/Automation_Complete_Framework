'''
Created on Jan 17, 2018

@author: Robert

Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251687
TestCase Name = AHTML: Combo Box incorrectly positioned to Filter Graph - 163906
'''
import unittest, time
import re
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, active_miscelaneous, ia_run
from common.lib import utillity

class C2251687_TestClass(BaseTestCase):

    def test_C2251687(self):
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2251687'
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        iarun = ia_run.IA_Run(self.driver)
        
        """    1. Execute the attached Document repro 163906_Old.    """
            
        utillobj.active_run_fex_api_login('163906_old.fex', 'S10071_3', 'mrid', 'mrpass')
             
        resultobj.wait_for_property("#MAINTABLE_wbody0_f",1,30)
         
        time.sleep(3)
         
        """    1.1. Expect to see the following Document, with the Combo Box positioned incorrectly at the first value, which reads 'Jun, 1939'. This was the old behavior.   """
             
        expected_xlabel_list=['CLASSIC/FLEMING V.']
        expected_ylabel_list=['0', '0.5', '1', '1.5', '2', '2.5', '3', '3.5']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0_f', expected_xlabel_list, expected_ylabel_list,'Step 1.1a : ')
        resultobj.verify_xaxis_title('MAINTABLE_wbody0_f','CATEGORY : Define_1 : DIRECTOR','Step 1.1b : Verify X-Axis title')
        resultobj.verify_yaxis_title('MAINTABLE_wbody0_f','COPIES','Step 1.1c : Verify Y-Axis title')
        resultobj.verify_number_of_riser('MAINTABLE_wbody0_f',1,1,'Step 1.1d : Verify number of chart risers')
          
        utillobj.verify_object_visible("#combobox_dsPROMPT_1", True, 'Step 01.1e: Verify Combobox1 present')
         
        utillobj.verify_dropdown_value('#combobox_dsPROMPT_1', expected_default_selected_value='Jun, 1939', default_selection_msg='Step 2.1. Verify Combobox positioned incorrectly at Jun 1939')
        
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        '''    2. Execute the attached Document repro 163906_New.    '''
        utillobj.active_run_fex_api_login('163906_new.fex', 'S10071_3', 'mrid', 'mrpass')
        resultobj.wait_for_property("#MAINTABLE_wbody0_f",1,30)
        
        """    2.1. Expect to see the following Document, with the Combo Box positioned at Jun, 1988, now correctly using the start value specified in the keyword ARFILTER_VALUE, for the ComboBox definition.    """
        """    2.2. Verify that the bars read 'ACTION/VERHOVEN P.' and 'FOREIGN, SCOLA E.' because the field used as the Filter has been suppressed by a NOPRINT phrase in the Fex.    """
        
        expected_xlabel_list=['ACTION/VERHOVEN P.', 'FOREIGN/SCOLA E.']
        expected_ylabel_list=['0', '0.5', '1', '1.5', '2', '2.5', '3', '3.5']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0_f', expected_xlabel_list, expected_ylabel_list,'Step 2.1a : ')
        resultobj.verify_xaxis_title('MAINTABLE_wbody0_f','CATEGORY : Define_1 : DIRECTOR','Step 2.1b : Verify X-Axis title')
        resultobj.verify_yaxis_title('MAINTABLE_wbody0_f','COPIES','Step 2.1c : Verify Y-Axis title')
        resultobj.verify_number_of_riser('MAINTABLE_wbody0_f',1,2,'Step 2.1d : Verify number of chart risers')
          
        utillobj.verify_object_visible("#combobox_dsPROMPT_1", True, 'Step 2.1e: Verify Combobox1 present')
         
        """    3. Click on the arrow in the Combo Box to verify that the displayed date is in the middle of the list and between the values May, 1988 and Jul, 1988.    """
        """    3.1. Expect to see the following expanded ComboBox list.    """
         
        
        list1 = ['Jun, 1939', 'May, 1940', 'Aug, 1941', 'Nov, 1941', 'Mar, 1942', 'Jul, 1942', 'Nov, 1950', 'Jul, 1951', 'Jul, 1954', 'Dec, 1954', 'Jan, 1955', 'Oct, 1955', 'Nov, 1958', 'Dec, 1958', 'Jan, 1959', 'Feb, 1959', 'May, 1960', 'Jan, 1962', 'Sep, 1963', 'Nov, 1972', 'Jul, 1973', 'Aug, 1975', 'Apr, 1976', 'Dec, 1976', 'Apr, 1978', 'May, 1978', 'Mar, 1980', 'Apr, 1980', 'May, 1980', 'Jul, 1981', 'Jul, 1982', 'Sep, 1982', 'Mar, 1983', 'Feb, 1984', 'Nov, 1984', 'Aug, 1985', 'Aug, 1986', 'Oct, 1986', 'Nov, 1986', 'Dec, 1986', 'Jan, 1987', 'Sep, 1987', 'Oct, 1987', 'Jan, 1988', 'Feb, 1988', 'Mar, 1988', 'Apr, 1988', 'May, 1988', 'Jun, 1988', 'Jul, 1988', 'Aug, 1988', 'Oct, 1988', 'Feb, 1989', 'Dec, 1989', 'Jan, 1990', 'Jun, 1990', 'Mar, 1991']
        #utillobj.verify_selected_dropdown_value("#combobox_dsPROMPT_1", "Jun, 1988", 'Step 2.1b. Verify Combobox positioned at Jun 1988', all_value_list=list1, all_value_list_msg='Step 2.1a. Verify all items in the list')
        utillobj.verify_dropdown_value("#combobox_dsPROMPT_1",list1, msg='Step 2.1a. Verify all items in the list', expected_default_selected_value="Jun, 1988", default_selection_msg='Step 2.1b. Verify Combobox positioned at Jun 1988')
    
if __name__=='__main__' :
    unittest.main()
        