'''
Created on Aug 17, 2018

@author: qaauto
'''
import unittest,time, keyboard
from common.lib.basetestcase import BaseTestCase
from common.pages import infographic
from common.wftools import login
from common.lib import utillity
from common.pages import visualization_ribbon, visualization_metadata


class C6667711_TestClass(BaseTestCase):
    def test_C6667711(self):
        user_type='mrid_dev'
        wf_login = login.Login(self.driver)
        info_graphic=infographic.InfoGraphic(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj=visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        project_id = utillobj.parseinitfile('project_id')
        suite_id = utillobj.parseinitfile('suite_id')
        oBrowser=utillobj.parseinitfile('browser')
        print(oBrowser)
        proj_folder="{0}_{1}".format(project_id,suite_id)
        proj_sub_folder='InfoGraphics'
        home_page_css=".explore-box .ibfs-tree .home-tree-node .ibx-label-text"
        run_img_css='body > img'
        oBrowser='Chrome'   # for temp need to remove later
        
        """    1. Sign in to WebFOCUS as a Developer user
        http://machine:port/{alias}/    """
        wf_login.invoke_home_page(user_type, 'mrpass')
        utillobj.synchronize_with_visble_text(home_page_css, 'Domains', 200)
        
        """    2. Repository folder: P413_S18040 > InfoGraphics, Execute the following URL:
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_LAUNCH&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP413_S18040%252FInfoGraphics%252F&BIP_item=ig_alignment.fex    """
        info_graphic.run_infographic_using_api(proj_folder, proj_sub_folder, 'ig_alignment', user_type)
        utillobj.synchronize_with_number_of_element(run_img_css, 1, 100)
        
        """    3. Verify the entire Infographic image (alignment and text wrap)    """
        time.sleep(2)
        utillobj.verify_picture_using_sikuli('ig_alignment_runtime_'+oBrowser.lower()+'.png', "Step 03(a): Verify ig_alignment fex - alignment and text wrap in runtime")
        
        """    4. Close the output window    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        wf_login.invoke_home_page(user_type, 'mrpass')
        utillobj.synchronize_with_visble_text(home_page_css, 'Domains', 200)
        
        """    5. Repository folder: P413_S18040 > InfoGraphics, Execute the following URL:
        http://machine.ibi.com:8080/ibi_apps/ia?item=IBFS:/WFC/Repository/P413_S18040/InfoGraphics/ig_alignment.fex    """
        info_graphic.restore_infographic_using_api(proj_folder, proj_sub_folder, 'ig_alignment', user_type)
        utillobj.synchronize_with_number_of_element("#easelly-frame", 1, 100)
        
        """    6. Verify the entire Live Preview Canvas    """
        utillobj.verify_picture_using_sikuli('ig_alignment_preview_'+oBrowser.lower()+'.png', "Step 06(a): Verify Edit canvas Infographic live preview canvas")
        
        """    7. Right-click "Unit Sales" in the Query pane (component named "Left") > Delete    """
        metaobj.select_querytree_field('Unit Sales', 'right', 1, context_menu_path='Delete')
        
        """    8. Select Home Tab > Click on the "Header&Footer" button    """
        ribbonobj.select_ribbon_item('Home', 'header_footer_img')
        
        """    9. Highlight and delete the text displayed > Click OK    """
        textbox_obj=self.driver.find_element_by_css_selector("#subheaderDlg")
        utillobj.click_on_screen(textbox_obj, coordinate_type='middle', click_type=0)
        time.sleep(1)
        keyboard.send('home')
        time.sleep(1)
        count=0
        while count<27:
            keyboard.send('del')
            count+=1
        time.sleep(1)
        self.driver.find_element_by_css_selector("#subheaderDlg #okBtn").click()
        time.sleep(1)
        
        """    10. Drag "Unit Sales" into the Sum bucket (component named "Left")    """
        metaobj.drag_drop_data_tree_items_to_query_tree('Unit Sales',1, 'Sum',0)
        time.sleep(8)
        
        """    11. Select Home Tab > Click on the "Header&Footer" button    """
        ribbonobj.select_ribbon_item('Home', 'header_footer_img')
        
        """    12. Copy/paste the following text string: This text is left justified    """
        textbox_obj=self.driver.find_element_by_css_selector("#subheaderDlg")
        utillobj.click_on_screen(textbox_obj, coordinate_type='middle', click_type=0)
        time.sleep(1)
        keyboard.send('home')
        time.sleep(1)
        count=0
        while count<15:
            keyboard.send('del')
            count+=1
        time.sleep(1)
        keyboard.write("This text is left justified", delay=1)
        time.sleep(3)
        
        """    13. Click OK    """
        self.driver.find_element_by_css_selector("#subheaderDlg #okBtn").click()
        time.sleep(1)
        
        
        """    14. Verify text remains displayed in a single line in the Live Preview    """
        utillobj.verify_picture_using_sikuli('ig_alignment_preview_'+oBrowser.lower()+'.png', "Step 14(a): Verify Edit canvas Infographic live preview canvas")
        
        """    15. Click on "Save" button in the toolbar > Click OK    """
        ribbonobj.select_top_toolbar_item("toolbar_save")
        try:
            if self.driver.find_element_by_css_selector("div[id^='BiDialog'] img[src*='infomark']").is_displayed():
                btn_css="div[id^='BiDialog'] div[class=bi-button-label]"
                dialog_btns=self.driver.find_elements_by_css_selector(btn_css)
                btn_text_list=[el.text.strip() for el in dialog_btns]
                dialog_btns[btn_text_list.index('OK')].click()
        except:
            pass
        time.sleep(5)
        
        """    16. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    17. Repository folder: P413_S18040 > InfoGraphics Execute the following URL:
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_LAUNCH&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP413_S18040%252FInfoGraphics%252F&BIP_item=ig_alignment.fex    """
        wf_login.invoke_home_page(user_type, 'mrpass')
        utillobj.synchronize_with_visble_text(home_page_css, 'Domains', 200)
        info_graphic.run_infographic_using_api(proj_folder, proj_sub_folder, 'ig_alignment', user_type)
        utillobj.synchronize_with_number_of_element(run_img_css, 1, 100)
        
        """    18. Verify the entire Infographic image    """
        utillobj.verify_picture_using_sikuli('ig_alignment_runtime_'+oBrowser.lower()+'.png', "Step 18(a): Verify ig_alignment fex - alignment and text wrap in runtime")
        
        """    19. Close the output window    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        wf_login.invoke_home_page(user_type, 'mrpass')
        utillobj.synchronize_with_visble_text(home_page_css, 'Domains', 200)
        
        """    20. Repository folder: P413_S18040 > InfoGraphics, Execute the following URL:
        http://machine.ibi.com:8080/ibi_apps/ia?item=IBFS:/WFC/Repository/P413_S18040/InfoGraphics/ig_alignment.fex    """
        info_graphic.restore_infographic_using_api(proj_folder, proj_sub_folder, 'ig_alignment', user_type)
        utillobj.synchronize_with_number_of_element("#easelly-frame", 1, 100)
        
        """    21. Verify the entire Live Preview Canvas    """
        utillobj.verify_picture_using_sikuli('ig_alignment_preview_'+oBrowser.lower()+'.png', "Step 21(a): Verify Edit canvas Infographic live preview canvas")
        
        """    22. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """  
        utillobj.infoassist_api_logout()
        time.sleep(3)
          


if __name__ == "__main__":
    unittest.main()
