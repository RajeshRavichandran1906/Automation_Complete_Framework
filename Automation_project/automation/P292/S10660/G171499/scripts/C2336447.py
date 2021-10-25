'''
Created on July 25, 2019

@author: AA14564
Testcase Name : Testing URL for PD
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2336447
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
from common.wftools.login import Login
from common.wftools.page_designer import Design

class C2336447_TestClass(BaseTestCase):

    def test_C2336447(self):
        
        """ TESTCASE OBJECT'S  """
        utillobj = utillity.UtillityMethods(self.driver)
        login = Login(self.driver)
        pd_design = Design(self.driver)
        
        """ TESTCASE VARIABLES  """
        SETUP_URL = login.create_setup_url().replace("home8206", "")
        URL_PATH = "{0}designer?item=IBFS:/WFC/Repository/Retail_Samples&tool=pagedesigner&startlocation=IBFS:/WFC/Repository/Retail_Samples".format(SETUP_URL)
        POP_TOP_CSS = '.pop-top'
        NODE_PANEL_CSS = ".ibfs-tree-node .tnode-children"
        PAGE_CANVAS = "div.pd-page-canvas"
        
        """ Step 1: Open a browser session.
        """
        """ Step 2: Create new page designer using API link:
                    http://{machine name}:{port}/context-root/designer?item=IBFS:/WFC/Repository/Retail_Samples&tool=pagedesigner&startlocation=IBFS:/WFC/Repository/Retail_Samples
                    Verify that this brings up the Sign In page.
        """
        self.driver.get(URL_PATH)
        
        """ Step 3: Login as domain developer.
                    It should bring up the page designer.
        """
        login.login_page('mriddev', 'mrpassdev')
        
        """ Step 4: Select Blank template.
        """
        utillobj.synchronize_with_visble_text(POP_TOP_CSS, 'Blank', pd_design.home_page_long_timesleep)
        pd_design.select_page_designer_template('Blank')
        utillobj.synchronize_with_visble_text(NODE_PANEL_CSS, 'Portal', pd_design.home_page_long_timesleep)
        
        """ Step 5: Navigate to Portal > Test Widgets folder.
        """
        """ Step 6: Drag and drop Blue, Gray and Green into the page canvas.
                    Verify able to add contents into the page designer.
        """
        pd_design.drag_content_item_to_blank_canvas('Blue', 1, content_folder_path='Portal->Test Widgets')
        pd_design.drag_content_item_to_blank_canvas('Gray', 4)
        pd_design.drag_content_item_to_blank_canvas('Green', 7)
        utillobj.synchronize_with_visble_text(PAGE_CANVAS, 'Green', pd_design.home_page_long_timesleep)
        pd_design.verify_containers_title(['Blue', 'Gray', 'Green'], 'Step 6: Verify able to add contents into the page designer.')
        
        """ Step 8: Sign out WF. 
        """
        
if __name__=='__main__' :
    unittest.main()
    