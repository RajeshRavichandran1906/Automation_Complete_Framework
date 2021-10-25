from common.lib.webfocus.get_data_frame import GetDataFrame
from common.pages import paris_home_page
from common.wftools.login import Login

class ParisHomePage :
    
    def __init__(self, driver):
        
        self.driver = driver
    
    def invoke_with_login(self, mrid, mrpass):
        
        Login(self.driver).invoke_paris_home_page(mrid, mrpass)
        
    @property
    def Banner(self):
        
        return paris_home_page.Banner(self.driver)
    
    @property
    def Home(self):
        
        return paris_home_page.Home(self.driver)
    
    @property
    def SearchResuls(self):
        
        return paris_home_page.Home.__viewall__(self.driver)
    
    @property
    def MyWorkspace(self):
        
        return paris_home_page.MyWorkspace(self.driver)
    
    @property
    def SharedWithMe(self):
        
        return paris_home_page.SharedWithMe(self.driver)

    @property
    def Workspaces(self):
        
        return paris_home_page.Workspaces(self.driver)

    @property
    def ContextMenu(self):
        
        return paris_home_page.ContextMenu(self.driver)
    
    @property
    def ModalDailogs(self):
        
        return paris_home_page.ModalDialogs(self.driver)
    
    @property
    def NotifyPopup(self):
        
        return paris_home_page.NotifyPopup(self.driver)
    
    @property
    def RunWindow(self):
        
        return paris_home_page.RunWindow(self.driver)
    
    @property
    def GetDataFrame(self):
        
        return GetDataFrame(self.driver)