from common.pages.basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common import alert
from selenium.common.exceptions import NoAlertPresentException

class API(BasePage):
    
    def __init__(self):
        
        super().__init__()
        self._base_url = self._utils.get_setup_url().replace("home8206", "")
        self._workspace_folder = self._core_utils.parseinitfile("workspace_folder") 
        
    def invoke_new_visualization(self, credential_keys=None, workspace_folder=None, master_file=None):
        """
        Description: Invoke designer tool to create new file.
        :Parameters
            credential_keys:tuple = config.init file key values of user id and password. exp: credential_keys=("mrid", "mrpass")
            workspace_folder:str = Workspace folder path of WebFOCUS. workspace_folder is None if already workspace folder defined in config.init file. 
            master_file:str = Path of master file. master_file if None if invoke designer tool without master file. exp: "ibisamp/car"
        :Usages
            invoke_new_visualization(credential_keys=('mrid', 'mrpass'), master_file='ibisamp/car')
            invoke_new_visualization(credential_keys=('mrid', 'mrpass'), workspace_folder="P292_S123456/G12345)
            invoke_new_visualization(credential_keys=('mrid', 'mrpass'))
        """
        folder = workspace_folder if workspace_folder else self._workspace_folder
        master_file = "&master={}".format(master_file) if master_file else ""
        api_url = "{0}designer?tool=framework{1}&item=IBFS:/WFC/Repository/{2}".format(self._base_url, master_file, folder)
        self._driver.get(api_url)
        credential_keys and self._utils.login_wf(credential_keys[0], credential_keys[1], add_home_path=False)
        if master_file:
            self._webelement.wait_for_element_text((By.CSS_SELECTOR, "div.base-canvas"), "Drop measures", 90)
        else:
            self._webelement.wait_for_element_text((By.CSS_SELECTOR, "div.select-data-source.pop-top"), "Title", 90)
        self._utils.wait_for_page_loads(30, pause_time=2)
    
    def invoke_assemble_visualizations(self, credential_keys=None, workspace_folder=None):
        """
        Description: Invoke assemble visualizations 
        :Parameters
            credential_keys:tuple = config.init file key values of user id and password. exp: credential_keys=("mrid", "mrpass")
            workspace_folder:str = Workspace folder path of WebFOCUS. workspace_folder is None if already workspace folder defined in config.init file. 
        :Usages
            invoke_new_visualization(credential_keys=('mrid', 'mrpass'))
            invoke_new_visualization(credential_keys=('mrid', 'mrpass'), workspace_folder="P292_S123456/G12345)
            invoke_new_visualization()
        """
        folder = workspace_folder if workspace_folder else self._workspace_folder
        api_url = "{0}designer?tool=framework&item=IBFS:/WFC/Repository/{1}&startUpConditions=eyJtb2RlIjoiYXNzZW1ibGUifQ%3D%3D".format(self._base_url, folder)
        self._driver.get(api_url)
        credential_keys and self._utils.login_wf(credential_keys[0], credential_keys[1], add_home_path=False)
        self._webelement.wait_for_element_text((By.CSS_SELECTOR, "div.df-template-picker.pop-top"), "Choose Template", 80)
        self._utils.wait_for_page_loads(30, pause_time=1)
        
    def logout(self):
        """
        Description: Logout the current WebFOCUS session
        """
        logout_url = self._base_url + "service/wf_security_logout.jsp"
        self._driver.get(logout_url)
        try:
            alert.Alert(self._driver).accept()
        except NoAlertPresentException:
            pass
        
    def edit_fex(self, fex_name, credential_keys=None, workspace_folder=None):
        """
        Description: Open saved fex file to edit using API
        """
        self.__edit_file(fex_name.lower(), ".fex", credential_keys, workspace_folder)
                
    def edit_page(self, page_name, credential_keys=None, workspace_folder=None):
        """
        Description: Open saved page  file to edit using API
        """
        self.__edit_file(page_name.lower(), "", credential_keys, workspace_folder)
        
    def edit_fex_in_texteditor(self, file_name, credential_keys=None, workspace_folder=None):
        """
        Description: Open saved fex file to edit using API
        """
        self.__edit_texteditor_file(file_name, ".fex", credential_keys, workspace_folder)
    
    def run_fex(self, fex_name, credential_keys=None, workspace_folder=None):
        """
        Description: Run saved fex file using API
        """
        self.__run_file(fex_name.lower(), ".fex", credential_keys, workspace_folder)
        
    def run_page(self, page_name, credential_keys=None, workspace_folder=None):
        """
        Description: Run saved page file using API
        """
        self.__run_file(page_name.lower(), "", credential_keys, workspace_folder)
        
    def __edit_file(self, file_name, file_extendion, credential_keys=None, workspace_folder=None):
        """
        Description: Edit the designer fex or page
        """
        folder = workspace_folder if workspace_folder else self._workspace_folder
        file = file_name + file_extendion
        api_url = "{0}designer?&item=IBFS:/WFC/Repository/{1}/{2}".format(self._base_url, folder, file)
        self._driver.get(api_url)
        credential_keys and self._utils.login_wf(credential_keys[0], credential_keys[1], add_home_path=False)
        self._webelement.wait_for_element_text((By.CSS_SELECTOR, "div.top-bar"), file_name, 80)
        self._utils.wait_for_page_loads(30, pause_time=2)
        
    def __run_file(self, file_name, file_extension, credential_keys=None, workspace_folder=None):
        """
        Description: run the designer fex or page
        """
        folder = workspace_folder if workspace_folder else self._workspace_folder
        file = file_name + file_extension
        api_url = "{0}run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/{1}&BIP_item={2}".format(self._base_url, folder, file)
        self._driver.get(api_url)
        credential_keys and self._utils.login_wf(credential_keys[0], credential_keys[1], add_home_path=False)
        self._utils.wait_for_page_loads(30, pause_time=2)
        
    def __edit_texteditor_file(self, file_name, file_extension, credential_keys=None, workspace_folder=None):
        """
        Description: Edit fex in texteditor 
        """
        folder = workspace_folder if workspace_folder else self._workspace_folder
        file = file_name + file_extension
        api_url = "{0}TED?rootFolderPath=IBFS:/WFC/Repository&folderPath=IBFS:/WFC/Repository/{1}/&itemName={2}".format(self._base_url,folder, file)
        self._driver.get(api_url)
        credential_keys and self._utils.login_wf(credential_keys[0], credential_keys[1], add_home_path=False)
        self._webelement.wait_for_element_text((By.CSS_SELECTOR, "div.te-tab-pane"), file_name, 80)
        self._utils.wait_for_page_loads(30, pause_time=2)
        
        