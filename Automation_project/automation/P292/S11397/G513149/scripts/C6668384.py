"""--------------------------------------------------------------
Author Name : Prabhakaran.
Automated On : 26-September-2019
--------------------------------------------------------------"""

from common.wftools.page_designer import Design
from common.lib.basetestcase import BaseTestCase

class C6668384_TestClass(BaseTestCase):
    
    def test_C6668384(self):
        
        """
            CLASS OBJECTS
        """
        pd_design = Design(self.driver)
        
        """
            STEP 01 : Login WF as developer user.
            STEP 02 : Click on Content view from side bar.
            STEP 03 : Expand "P292_S11397" domain -> "G513149" folder.
            STEP 03 : Click on "Page" action tile from under Designer category.
            STEP 05 : Choose "Blank" template
        """
        pd_design.invoke_page_designer_and_select_template('Blank', from_designer_group=True)
        
        """
            STEP 06 : In Content tab open "Repository Widgets".
        """
        pd_design.expand_and_collapse_repository_widgets_tab('expand')
        
        """
            STEP 06 - Expected : Verify user cant see Folder option, only Explorer and Link Tile widgets appear as below.
        """
        pd_design.verify_repository_widgets_item(['Explorer', 'Link tile'], "Step 06.02 : Verify Explorer and Link Tile widgets appear")
        
        """
            STEP 07 : Click the Application menu and Select "Close".
            STEP 08 : Click "NO" button.
        """
        pd_design.close_page_designer_without_save_page()
        
        """
            STEP 09 : Logout WF
        """