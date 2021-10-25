'''-------------------------------------------------------------------------------------------
Reworked on January 25, 2019
@author: Prabhakaran

Test Case Link   =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6778676
Test Case Title  =  "Text Editor" ribbon tab in focus when in Source view
-----------------------------------------------------------------------------------------------'''

from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common.ribbon import Ribbon
from appstudio.tools import report as Report
import unittest

class C6778676_TestClass(BaseTestCase):

    def test_C6778676(self):
       
        """
            STEP 01 : Right click on AS Framework and select New->Report Click on ibisamp->car.mas. Click OK
        """
        Report.Report.create_new_report_from_webfocus_environments_tree('ibisamp', 'car.mas')
        
        """
            STEP 02 : Click Source tab at the bottom of the Report Canvas
        """
        Report.Canvas.switch_to_source_view()

        """
            STEP 02 Expected : Ribbon bar should switch to Text Editor
        """
        Ribbon.verify_tab_is_selected(Ribbon.Locators.TextEditorTab.TEXTEDITOR, '02.01')
        
        """
            STEP 03 : Close Report3 tab
        """
        
if __name__=='__main__' :
    unittest.main()