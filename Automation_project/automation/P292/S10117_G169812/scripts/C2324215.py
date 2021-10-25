'''
Created on 28-Aug-2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324215
TestCase Name = Defaults : Check_defaults_portal_page
'''
import unittest, time
from common.lib import utillity
from common.pages import visualization_resultarea, vfour_miscelaneous, wf_mainpage, vfour_portal_canvas, vfour_portal_ribbon, wf_legacymainpage
from common.pages import vfour_portal_properties
from common.lib.basetestcase import BaseTestCase

class C2324215_TestClass(BaseTestCase):

    def test_C2324215(self):
        """
        TESTCASE VARIABLES
        """
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        vfour_misobj = vfour_miscelaneous.Vfour_Miscelaneous(self.driver)
        if utillobj.parseinitfile('nodeid') in ('wfinst01','wfinst02','wfinst03','wfinst06'):
            wf_mainpageobj = wf_mainpage.Wf_Mainpage(self.driver)
        else:
            wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        portal_properties = vfour_portal_properties.Vfour_Portal_Properties(self.driver)
        portal_canvas = vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        portal_ribbon = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        
        """ Step 1: Sign in as WF Developer
        """
        utillobj.invoke_webfocu('mrid03', 'mrpass03')
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value="Domains", with_regular_exprestion=True)
          
          
        """ Step 2: Right Click on the 'BIP_xxx_Portal123_V4' portal under P292 domain->S10117 folder and choose Edit
        """
        wf_mainpageobj.select_repository_menu('P292->S10117->BIP_V4_Portal->BIP_xxx_Portal123_V4', 'Edit')
        run_loop = True
        count_time=0
        while run_loop:
            if count_time == 25:
                run_loop = False
            if len(driver.window_handles) > 1:
                run_loop = False
            count_time += 1
        utillobj.switch_to_window(1)
        parent_css = "#applicationButtonBox img[src*='bip_button']"
        resultobj.wait_for_property(parent_css, 1, expire_time=50)
          
          
        """ Step 3: Click Cancel on the page template dialog
        """
        vfour_misobj.select_page_template(btn_name="Cancel")
        time.sleep(3)
          
        """ Step 4: Check the Portal title
                    Verify that this reads the correct portal
        """
        portal_properties.verify_input_control('pageview', 'Portal Title', 'textbox', "Step 4: Verify that this reads the correct portal", textbox_value="BIP_xxx_Portal123_V4")
           
        """ Step 5: Verify that the Published Icon is Checked.
        """
        portal_properties.verify_input_control('pageview', 'Published', 'checkbox', "Step 5: Verify that the Published Icon is Checked", checkbox_input='check')
           
        """ Step 6: Check Dynamic Report Styling
                    Verify that its not checked
        """
        portal_properties.verify_input_control('pageview', 'Dynamic Report Styling', 'checkbox', "Step 6: Verify that the Dynamic Report Styling is not Checked", checkbox_input='uncheck')
         
        """ Step 7: Check Width
                    Verify that its set to 100%
        """
        portal_properties.verify_input_control('pageview', 'Width %', 'textbox', "Step 7: Verify that the Width is set to 100.", textbox_value='100')
        portal_properties.verify_input_control('pageview', 'Width unit %', 'combobox', "Step 7.1: Verify that the Width is set to %.", combobox_value='%')
           
        """ Step 8: Check Alignment
                    Verify that its set to center
        """
        portal_properties.verify_input_control('pageview', 'Alignment %', 'textbox', "Step 8: Verify that the Alignment is set to center.", textbox_value='Center')
           
        """ Step 9: Check Page Height Mode
                    Verify that its set to Fill
        """
        portal_properties.verify_input_control('pageview', 'Page Height Mode', 'combobox', "Step 9: Verify that the Alignment is set to center.", combobox_value='Fill')
           
        """ Step 10: Check Show live content
                     Verify that its checked
        """
        portal_properties.verify_input_control('pageview', 'Show live content', 'checkbox', "Step 10: Verify that the Show live content is checked.", checkbox_input='check')
           
           
        """ Step 11: Check Broadcast height for embedding
                     Verify that its not checked
        """
        portal_properties.verify_input_control('pageview', 'Broadcast height for embedding', 'checkbox', "Step 11: Verify that the Broadcast height for embedding is not checked.", checkbox_input='uncheck')
           
        """ Step 12: Check the box for Broadcast height for embedding
                     Verify
        """
        portal_properties.edit_input_control('pageview', 'Broadcast height for embedding', 'checkbox', checkbox_input='check', msg='Step 12')
        time.sleep(1)
        portal_properties.verify_input_control('pageview', 'Broadcast height for embedding', 'textbox', "Step 12.1: Verify that the Broadcast height for embedding text value '*'.", textbox_value='*')
           
           
        """ Step 13: Uncheck the Broadcast height for embedding box.
                     Verify that the Target origin box disappears
        """
        portal_properties.edit_input_control('pageview', 'Broadcast height for embedding', 'checkbox', checkbox_input='uncheck', msg='Step 13')
        time.sleep(1)
        try:
            portal_properties.get_vbox_object("[id^='idProperties']:not([style*='hidden'])", 'Target Origin')
            status_ = False
        except ValueError:
            status_ = True
        utillobj.asequal(status_, True, "Step 13.1: Verify that the Target origin box disappears.")
           
        """ Step 14: Check the Default Page drop down
                     Verify that the dropdown says None
        """
        portal_properties.verify_input_control('pageview', 'Default Page', 'combobox', "Step 14: Verify that the Default Page drop down is displayed 'None'.", combobox_value='None')
           
        """ Step 15: Click on the new page icon as by default no Page 1 is auto created.
                     If you see Page templates not found then Enter Page 1 then click Create.
                     If you see templates then choose Single area, enter Page 1 then click Create.
        """
        portal_canvas.add_page('Single Area', Page_title="Page 1")
        time.sleep(2)
          
        """ Step 16: Click on Page 1
                     Verify that the Page Title says Page 1
        """
        portal_canvas.select_page_in_navigation_bar('Page 1')
  
        """ Step 17: Checking default value for Lock Page
                     Verify that its checked
        """
        portal_properties.verify_input_control('page', 'Lock Page', 'checkbox', "Step 17: Verify that the Lock page is checked.", checkbox_input='check')
           
        """ Step 18: Checking default value for Refresh on Click
                     Verify that its not checked
        """
        portal_properties.verify_input_control('page', 'Refresh on Click', 'checkbox', "Step 18: Verify that the Refresh on Click is Unchecked.", checkbox_input='uncheck')
           
        """ Step 19: Checking default value for Show in Navigation
                     Verify that its checked
        """
        portal_properties.verify_input_control('page', 'Show in Navigation', 'checkbox', "Step 19: Verify that the Show in Navigation is Checked.", checkbox_input='check')
           
           
        """ Step 20: Check Prevent Layout Change
                     Verify that this is checked and grayed out.
                     this will tested more in depth later on in Check Layout change
        """
        portal_properties.verify_input_control('page', 'Prevent Layout Change', 'checkbox', "Step 20: Verify that the Prevent Layout Change is checked.", checkbox_input='check')
        portal_properties.verify_input_control_enable_or_disable('page', 'Prevent Layout Change', 'checkbox', "Step 20.1: Verify that the Prevent Layout Change is Disabled.", enable_status='disabled', enable_value=True, color_name='silver')
           
        """ Step 21: In V4 mode we will have Relative Path checkbox
                     Verify that the relative checkbox is not checked.
        """
        portal_properties.verify_input_control('page', 'Relative Path', 'checkbox', "Step 21: Verify that the Relative Path is Unchecked.", checkbox_input='uncheck')
         
           
        """ Step 22: Check Show Refresh
                     Verify that the show refresh checkbox is checked.
        """
        portal_properties.verify_input_control('page', 'Show Refresh', 'checkbox', "Step 22: Verify that the Show Refresh is checked.", checkbox_input='check')
           
        """ Step 23: Checking default value for Margins
                     Verify that its checked
        """
        portal_properties.verify_input_control('page', 'Same for All', 'checkbox', "Step 23: Verify that the Margins Same for All is checked.", checkbox_input='check')
           
            
        """ Step 24: In 82xx, check Comments is set to none
        """
        portal_properties.verify_input_control('page', 'Comments', 'combobox', "Step 24: Verify that the Comments is displayed 'None'.", combobox_value='None')
        """ Step 25: Click Container Defaults
                     HEAD/8200 image
        """
        portal_properties.edit_input_control('page', 'Container Defaults', 'button')
           
        """ Step 26: Verification  of Container Defaults dialogs.
        """
        textbox_option = {'Width':'400', 'Height':'400'}
        checkbox_option = {'Hide Title Bar':'uncheck', 'Show Menu Icons':'check', 'Move':'check', 'Resize':'check', 'Minimize':'check', 'Maximize':'check',
                   'Refresh':'check', 'Hide':'uncheck', 'Delete':'check', 'Show Comments':'uncheck'}
        button_option = ['Reset to Default', 'OK', 'Cancel']
        count = 1
        for text in textbox_option:
            portal_properties.manage_container_defaults_popup('textbox', text, textbox_value=textbox_option[text], msg="Step 26."+str(count)+": Verify Container Defaults dialogs "+text+" value "+textbox_option[text]+".")
            count += 1
        for box in checkbox_option:
            portal_properties.manage_container_defaults_popup('checkbox', box, checkbox_input=checkbox_option[box], msg="Step 26."+str(count)+": Verify Container Defaults dialogs "+box+" value "+checkbox_option[box]+".")
            count += 1
        for button in button_option:
            portal_properties.manage_container_defaults_popup('button', button, msg="Step 26."+str(count)+": Verify Container Defaults dialogs "+button+" is Displayed.")
            count += 1
        portal_properties.manage_container_defaults_popup('button', 'Cancel', verification=False)
           
        """ Step 27: Select "BIP_xxx_Portal123_V4" under breadcrumbs and repeat the steps from 4 to 14.
        """
        time.sleep(5)
        portal_properties.select_breadcrumb_panel('BIP_xxx_Portal123_V4')
         
        """ Step 28: Check the Portal title
            Verify that this reads the correct portal
        """
        portal_properties.verify_input_control('pageview', 'Portal Title', 'textbox', "Step 28: Verify that this reads the correct portal", textbox_value="BIP_xxx_Portal123_V4")
          
        """ Step 29: Verify that the Published Icon is Checked.
        """
        portal_properties.verify_input_control('pageview', 'Published', 'checkbox', "Step 29: Verify that the Published Icon is Checked", checkbox_input='check')
          
        """ Step 30: Check Dynamic Report Styling
                    Verify that its not checked
        """
        portal_properties.verify_input_control('pageview', 'Dynamic Report Styling', 'checkbox', "Step 30: Verify that the Dynamic Report Styling is not Checked", checkbox_input='uncheck')
        
        """ Step 31: Check Width
                    Verify that its set to 100%
        """
        portal_properties.verify_input_control('pageview', 'Width %', 'textbox', "Step 31: Verify that the Width is set to 100.", textbox_value='100')
        portal_properties.verify_input_control('pageview', 'Width unit %', 'combobox', "Step 31.1: Verify that the Width is set to %.", combobox_value='%')
          
        """ Step 32: Check Alignment
                    Verify that its set to center
        """
        portal_properties.verify_input_control('pageview', 'Alignment %', 'textbox', "Step 32: Verify that the Alignment is set to center.", textbox_value='Center')
          
        """ Step 33: Check Page Height Mode
                    Verify that its set to Fill
        """
        portal_properties.verify_input_control('pageview', 'Page Height Mode', 'combobox', "Step 33: Verify that the Alignment is set to center.", combobox_value='Fill')
          
        """ Step 34: Check Show live content
                     Verify that its checked
        """
        portal_properties.verify_input_control('pageview', 'Show live content', 'checkbox', "Step 34: Verify that the Show live content is checked.", checkbox_input='check')
          
          
        """ Step 35: Check Broadcast height for embedding
                     Verify that its not checked
        """
        portal_properties.verify_input_control('pageview', 'Broadcast height for embedding', 'checkbox', "Step 35: Verify that the Broadcast height for embedding is not checked.", checkbox_input='uncheck')
          
        """ Step 36: Check the box for Broadcast height for embedding
                     Verify
        """
        portal_properties.edit_input_control('pageview', 'Broadcast height for embedding', 'checkbox', checkbox_input='check', msg='Step 36')
        time.sleep(1)
        portal_properties.verify_input_control('pageview', 'Broadcast height for embedding', 'textbox', "Step 36.1: Verify that the Broadcast height for embedding text value '*'.", textbox_value='*')
          
          
        """ Step 37: Uncheck the Broadcast height for embedding box.
                     Verify that the Target origin box disappears
        """
        portal_properties.edit_input_control('pageview', 'Broadcast height for embedding', 'checkbox', checkbox_input='uncheck', msg='Step 37')
        time.sleep(1)
        try:
            portal_properties.get_vbox_object("[id^='idProperties']:not([style*='hidden'])", 'Target Origin')
            status_ = False
        except ValueError:
            status_ = True
        utillobj.asequal(status_, True, "Step 37.1: Verify that the Target origin box disappears.")
          
        """ Step 38: Check the Default Page drop down
                     Verify that the dropdown says None
        """
        portal_properties.verify_input_control('pageview', 'Default Page', 'combobox', "Step 38: Verify that the Default Page drop down is displayed 'None'.", combobox_value='None')
         
        """ Step 39: Select "BIP_xxx_Portal123_V4 > Pages > Page 1" under breadcrumbs and repeat the steps from 16 to 25
        """
        time.sleep(2)
        portal_properties.select_breadcrumb_panel('BIP_xxx_Portal123_V4', next='Pages')
        time.sleep(3)
        portal_properties.select_breadcrumb_panel('Pages', next='Page 1')
        
        """ Step 40: Click on Page 1
             Verify that the Page Title says Page 1
        "" Step 41: Checking default value for Lock Page
                     Verify that its checked
        """
        portal_properties.verify_input_control('page', 'Lock Page', 'checkbox', "Step 41: Verify that the Lock page is checked.", checkbox_input='check')
         
        """ Step 42: Checking default value for Refresh on Click
                     Verify that its not checked
        """
        portal_properties.verify_input_control('page', 'Refresh on Click', 'checkbox', "Step 42: Verify that the Refresh on Click is Unchecked.", checkbox_input='uncheck')
         
        """ Step 43: Checking default value for Show in Navigation
                     Verify that its checked
        """
        portal_properties.verify_input_control('page', 'Show in Navigation', 'checkbox', "Step 43: Verify that the Show in Navigation is Checked.", checkbox_input='check')
         
         
        """ Step 44: Check Prevent Layout Change
                     Verify that this is checked and grayed out.
                     this will tested more in depth later on in Check Layout change
        """
        portal_properties.verify_input_control('page', 'Prevent Layout Change', 'checkbox', "Step 44: Verify that the Prevent Layout Change is checked.", checkbox_input='check')
        portal_properties.verify_input_control_enable_or_disable('page', 'Prevent Layout Change', 'checkbox', "Step 44.1: Verify that the Prevent Layout Change is Disabled.", enable_status='disabled', enable_value=True, color_name='silver')
         
        """ Step 45: In V4 mode we will have Relative Path checkbox
                     Verify that the relative checkbox is not checked.
        """
        portal_properties.verify_input_control('page', 'Relative Path', 'checkbox', "Step 45: Verify that the Relative Path is Unchecked.", checkbox_input='uncheck')
         
         
        """ Step 46: Check Show Refresh
                     Verify that the show refresh checkbox is checked.
        """
        portal_properties.verify_input_control('page', 'Show Refresh', 'checkbox', "Step 46: Verify that the Show Refresh is checked.", checkbox_input='check')
         
        """ Step 47: Checking default value for Margins
                     Verify that its checked
        """
        portal_properties.verify_input_control('page', 'Same for All', 'checkbox', "Step 47: Verify that the Margins Same for All is checked.", checkbox_input='check')
         
          
        """ Step 48: In 82xx, check Comments is set to none
        """
        portal_properties.verify_input_control('page', 'Comments', 'combobox', "Step 48: Verify that the Comments is displayed 'None'.", combobox_value='None')
        
        """ Step 49: Click Container Defaults
                     HEAD/8200 image
        """
        portal_properties.edit_input_control('page', 'Container Defaults', 'button')
         
        """ Step 50: Verification  of Container Defaults dialogs.
        """
        textbox_option = {'Width':'400', 'Height':'400'}
        checkbox_option = {'Hide Title Bar':'uncheck', 'Show Menu Icons':'check', 'Move':'check', 'Resize':'check', 'Minimize':'check', 'Maximize':'check',
                   'Refresh':'check', 'Hide':'uncheck', 'Delete':'check', 'Show Comments':'uncheck'}
        button_option = ['Reset to Default', 'OK', 'Cancel']
        count = 1
        for text in textbox_option:
            portal_properties.manage_container_defaults_popup('textbox', text, textbox_value=textbox_option[text], msg="Step 50."+str(count)+": Verify Container Defaults dialogs "+text+" value "+textbox_option[text]+".")
            count += 1
        for box in checkbox_option:
            portal_properties.manage_container_defaults_popup('checkbox', box, checkbox_input=checkbox_option[box], msg="Step 50."+str(count)+": Verify Container Defaults dialogs "+box+" value "+checkbox_option[box]+".")
            count += 1
        for button in button_option:
            portal_properties.manage_container_defaults_popup('button', button, msg="Step 50."+str(count)+": Verify Container Defaults dialogs "+button+" is Displayed.")
            count += 1
        portal_properties.manage_container_defaults_popup('button', 'Cancel', verification=False)
         
        
        """ Step 51: Save and exit portal
        """
        portal_ribbon.select_tool_menu_item('menu_Save')
        time.sleep(3)
        portal_ribbon.select_tool_menu_item('menu_Exit')
        
        """ Step 52: Sign Out from WebFOCUS
        """
        time.sleep(5)
        
        

if __name__ == '__main__':
    unittest.main()