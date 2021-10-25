'''
Created on 14 June, 2018

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10674&group_by=cases:section_id&group_id=171932&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2350272
TestCase Name = Verify Properties of V3 portal is not available
'''
import unittest,time, re
from common.lib.basetestcase import BaseTestCase
from common.pages import wf_mainpage
from common.wftools import login
from common.lib import utillity, core_utility, javascript


class C2350272_TestClass(BaseTestCase):

    def test_C2350272(self):
        """
        TESTCASE VARIABLES
        """
        wf_login = login.Login(self.driver)
        wf_mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        core_utilobj=core_utility.CoreUtillityMethods(self.driver)
        j_script=javascript.JavaScript(self.driver)
        dev_name = utillobj.parseinitfile('mrid')
        developer_user_name_css=".menu-btn .ibx-label-text"
        portal_name="V3 portal"
        folder_path='Portals'
        
        def get_domain_folder_item(item_name, folder_path):
            """
            local function
            """
            scroll_css="div[class*='files-box-files']"
            item_not_found_error="[{0}] file not found in [{1}] domain folder path"
            items_css="div[class*='files-box-files'] div[class*='file-item-shown']"
            items_label_css="{0} div.ibx-label-text".format(items_css)
            item_obj_list=self.driver.find_elements_by_css_selector(items_css)
            item_label_obj_list=self.driver.find_elements_by_css_selector(items_label_css)
            found_item_index=j_script.find_element_index_by_text(item_label_obj_list, item_name)
            scroll_obj=self.driver.find_element_by_css_selector(scroll_css)
            scroll_bottom_cord = core_utilobj.get_web_element_coordinate(scroll_obj, 'bottom_middle')
            core_utilobj.python_move_to_element(scroll_obj)
            time.sleep(1)
            scroll_y = scroll_bottom_cord['y']
            if found_item_index != None :
                item_obj=item_obj_list[found_item_index]
                while True :
                    item_bootm_cord = core_utilobj.get_web_element_coordinate(item_obj, 'bottom_middle')
                    item_bottom_y = item_bootm_cord['y']
                    if item_bottom_y > scroll_y:
                        utillobj.mouse_scroll('down', 1, option='uiautomation', pause=2)
                    else :
                        break
                return item_obj
            else:
                raise FileNotFoundError(item_not_found_error.format(item_name, folder_path))
        
        def verify_context_menu_item(expected_context_menu_item, msg):
            """
            local function
            """
            pop_up_css="div[class*='pop-top'][data-ibx-type='ibxMenu']"
            popup_menu_rows=pop_up_css+" div[data-ibx-type='ibxMenuItem'] div[class='ibx-label-text']"
            popup_items = self.driver.find_elements_by_css_selector(popup_menu_rows)
            actual_context_menu_item_list=[el.text.strip() for el in popup_items  if bool(re.match('\S+', el.text.strip()))]
            utillobj.as_notin(expected_context_menu_item, actual_context_menu_item_list, msg)
    
        """ Step 1: Login to WebFOCUS as a Developer
        """
        wf_login.invoke_home_page('mrid', 'mrpass')
        utillobj.synchronize_with_visble_text(developer_user_name_css, dev_name, 290)
        
        """ Step 2: From the new Home Page click on Portals page from side bar.
        """
        wf_mainobj.select_left_panel('Portals')
        
        """ Step 3: Right click on 'V3 Portal'
                    Verify properties doesn't appear in context menu.
        """
        portal_obj=get_domain_folder_item(portal_name, folder_path)
        core_utilobj.right_click(portal_obj)
        verify_context_menu_item('Properties', "Step 3: Verify properties doesn't appear in context menu.")
        
        """ Step 4: Sign out. 
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()