from common.pages.vfive_portal_page import Vfive_portal_page as v5_portal_page
from common.lib.base import BasePage

class Portal(BasePage):
    
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(Portal, self).__init__(driver)
    
    
    ''''''''''''''''''''''''''''''''' New V5 portal Creation '''''''''''''''''''''''''''''''''''''''''''''
    def create_vfive_portal(self, portal_name, folder_path, navigation_type, expire_time=90):
        '''
        This will create new V5 portal.
        @param folder_path: 'P116->S10902'
        :Usage create_vfive_portal('P116->S10902')
        '''
        v5_portal_page.create_vfive_portal(self, portal_name, folder_path, navigation_type, expire_time=expire_time)
    
    def close_vfive_portal_create_dialog(self, button_name):
        v5_portal_page.close_vfive_portal_create_dialog(self, button_name)
        
        
    '''''''''''''''''''''''''''''''''' Verify New V5 portal dialog '''''''''''''''''''''''''''''''''''''''
    def verify_vfive_portal_create_dialog(self, button_name):
        v5_portal_page.verify_vfive_portal_create_dialog(self, button_name)
    
    ''''''''''''''''''''''''''''''''' V5 portal run window '''''''''''''''''''''''''''''''''''''''
    def run_vfive_portal(self, portal_path):
        v5_portal_page.run_vfive_portal(self, portal_path)
        
    def close_vfive_portal_run_window(self):
        v5_portal_page.close_vfive_portal_run_window(self)

class Portal_canvas(BasePage):
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(Portal_canvas, self).__init__(driver)

class Portal_banner(BasePage):
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(Portal_banner, self).__init__(driver)

class Portal_left_side_bar(BasePage):
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(Portal_left_side_bar, self).__init__(driver)
    
    
    
