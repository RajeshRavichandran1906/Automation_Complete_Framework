import time, re
import pyautogui, keyboard, unittest
from common.lib import utillity
from common.lib.base import BasePage

class Rest_Web_Services_Test_Page(BasePage):
    def testlicense(self, licence, sitecode):
        
        self.driver.find_element_by_css_selector("html > body input[name='license']").click()
        time.sleep(3)
        utillity.UtillityMethods.switch_to_frame(self, pause=2, frame_css='html body iframe', frame_height_value=0)
        time.sleep(5)
        self.driver.find_element_by_css_selector("form#testLicense input[name='IBFS_license']").send_keys(licence)
        time.sleep(1)
        self.driver.find_element_by_css_selector("form#testLicense input[name='IBFS_sitecode']").send_keys(sitecode)
        time.sleep(1)
        self.driver.find_element_by_css_selector("form#testLicense input[name='IBFS_action']").click()
        time.sleep(5)
        self.driver.switch_to_default_content()
        
    def verify_xml_page(self, value_of, expected_value_list, msg, from_viewsource=True, close_viewsource=False):
        new_win=self.driver.window_handles
        if from_viewsource==False:
            time.sleep(5)
            keyboard.send('ctrl+u')
            count=0
            while True:
                if count == 60:
                    break
                num_win=self.driver.window_handles
                if len(num_win)  == 3:
                    time.sleep(2)
                    utillity.UtillityMethods.switch_to_window_handle_test(self, 2, custom_windows=new_win)
                    break
                else:
                    time.sleep(1)
                    count += 1
            time.sleep(2)
            if count == 60:
                unittest.TestCase.fail(self, "IE crash failure")
        xmlobj=self.driver.find_element_by_css_selector("html body table")
        act=xmlobj.text.strip().split("><")
        temp_val = 0
        for act_line in act:
            if bool(re.match(".*"+value_of+".*", act_line)):
                temp_val = 1
                print(act_line)
                for expected_value in expected_value_list:
                    utillity.UtillityMethods.asin(self, expected_value, act_line, msg)
                break
        if temp_val == 0:
            utillity.UtillityMethods.asequal(self, True, False, "Step X: "+value_of+" not found in XML Page. ")
        if close_viewsource==True:
            self.driver.close()
            time.sleep(2)