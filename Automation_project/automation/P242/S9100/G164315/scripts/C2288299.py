'''-------------------------------------------------------------------------------------------
Reworked on January 14, 2019
@author: Pradheep

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288299
Test Case Title =  Folder Contextual Impact Analysis
-----------------------------------------------------------------------------------------------'''
from appstudio import settings
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.report import DataSourceWindow
from appstudio.tools.common.environments import Tree
import unittest

class C2288299_TestClass(BaseTestCase):
    
    def test_C2288299(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
        
        """ 
            COMMON VARIABLES
        """
        MRID = 'mradmin'
        WF_PUBLIC_FOLDER_PATH= 'Domains->Public'
        
        """
            STEP 01.01 : Right click Public under Domains and select Impact Analysis
        """
        Tree.right_click_on_webfocus_environment_item(WF_PUBLIC_FOLDER_PATH, mrid=MRID)
        Tree.select_context_menu('Impact Analysis')
        DataSourceWindow.verify_select_data_source_window_exist('01.01')
        
        """
            STEP 02.01 : Click Cancel button.
            STEP 02.01 Expected : Dialog closes
        """
        DataSourceWindow.click_on_cancel_button()
        DataSourceWindow.verify_select_data_source_window_not_exist('02.01')
        
        
if __name__=='__main__' :
    unittest.main()