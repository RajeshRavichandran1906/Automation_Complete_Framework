'''
Created on Jan17, 2018
@author: KS13172

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2308059
TestCase Name = AHTML:Cache:Webpage error when filtering with DATEs (MtYY) (ACT-383)
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea,active_miscelaneous
from common.lib import utillity


class C2308059_TestClass(BaseTestCase):

    def test_C2308059(self):
        Test_Case_ID = 'C2308059'
        """
        Step 01: Execute the attached ACT-383_ON.fex
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        visul_result = visualization_resultarea.Visualization_Resultarea(self.driver)
        active_misobj=active_miscelaneous.Active_Miscelaneous(self.driver)
        utillobj.active_run_fex_api_login('ACT-383_ON.fex','S10071_1','mrid','mrpass')
        
        def verify_bar_chart(parent_id,tooltip,xaxis_labels,yaxis_labels,title,riser, step_num):
            visul_result.verify_xaxis_title(parent_id, 'CATEGORY : Define_1 : DIRECTOR', 'Step ' + step_num + '.1 : Verify X-Axis title')
            visul_result.verify_yaxis_title(parent_id, 'COPIES', 'Step ' + step_num + '.2 : Verify Y-Axis title')
            visul_result.verify_riser_chart_XY_labels(parent_id, xaxis_labels, yaxis_labels, 'Step ' + step_num + '.3 :Verify XY labels')
            visul_result.verify_number_of_riser(parent_id, 1, riser, 'Step ' + step_num + '.4 : Verify number of bar chart risers')
            utillobj.verify_chart_color(parent_id, 'riser!s0!g0!mbar!', 'cerulean_blue', 'Step ' + step_num + '.5 : Verify bar chart riser color')
            active_misobj.verify_chart_title('MAINTABLE_wbody0_ft',title,'Step ' + step_num + '.6 :Verify title')
            visul_result.verify_default_tooltip_values(parent_id,"riser!s0!g0!mbar!", tooltip,"Step"  + step_num + ".7: Verify Chart tooltip")
           
        """
        Step02: Verify chart is displayed with Date dropdown box without any webpage error.
        """        
        utillobj.synchronize_with_number_of_element("#MAINTABLE_0", 1, 3)
        xaxis=['ACTION','FOREIGN']
        yaxis=['0', '0.5', '1', '1.5', '2','2.5','3','3.5']
        title='COPIES BY CATEGORY, DIRECTOR' 
        tooltip=['COPIES, ACTION/VERHOVEN P.:3']
        verify_bar_chart('MAINTABLE_wbody0',tooltip,xaxis,yaxis ,title,2,'02.1')
        utillobj.verify_dropdown_value('#combobox_dsPROMPT_1',expected_default_selected_value='Jun, 1988', default_selection_msg="Step02.1.8: Verify Jun, 1988 is selected")
        utillobj.select_dropdown('#combobox_dsPROMPT_1', 'visible_text', 'Jan, 1987')
        utillobj.verify_dropdown_value('#combobox_dsPROMPT_1',expected_default_selected_value='Jan, 1987', default_selection_msg="Step02.1.9: Verify Jan, 1987 is selected")
        
        xaxis=['MYSTERY']
        yaxis=['0', '0.3', '0.6', '0.9', '1.2']
        title='COPIES BY CATEGORY, DIRECTOR' 
        tooltip=['COPIES, MYSTERY/LUMET S.:1']
        verify_bar_chart('MAINTABLE_wbody0',tooltip,xaxis,yaxis ,title,1,'02.2')
        
if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
