"""----------------------------------------------------
Author Name  : Prabhakaran
Automated on : 22 April 2020
----------------------------------------------------"""

from common.webservices.git import gitConnectionSettings
from common.webservices import BaseTestCase
from common.webservices.pwa import pwaList

class C9945223_TestClass(BaseTestCase):
    
    def test_C9945223(self):
        
        """
        TEST CASE VARIABLS
        """
        IBIRS_path = self.get_config_file_key_value('IBIRS_path')
        IBFS_userName = self.get_config_file_key_value('git_userid')
        IBFS_password = self.get_config_file_key_value('git_pass')
        IBIRS_gitEmail = self.get_config_file_key_value('git_email')
        IBIRS_gitRepository = self.get_config_file_key_value('git_repro_url')  
        git_encrypted_pass = self.get_config_file_key_value('git_encrypted_pass')
        user_name = self.get_config_file_key_value('devuser1')
        pwa_item     =  [{'_jt': 'IBFSPwaWfcGenGitProps', 'pwaBindingFolder': 'git', 'pwaFolderRelToUser': 'WFC/Repository/P459_S33046_Val_API', 'pwaIbfsRoot': 'IBFS:/WFC/Repository/P459_S33046_Val_API', 'userWorkingFolder': user_name}]
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS and Run gitConnectionSettings.
        """
        self.Log.Message(STEP_01)
        self.signOn('devuser1', 'devpass1')
        git_connection = gitConnectionSettings(IBIRS_path, IBFS_userName, IBFS_password, IBIRS_gitEmail, IBIRS_gitRepository)
        
        STEP_01_EXPECTED = """
            STEP 01 Expected : Verify returncode="10000" and [entry key="IBIRS_path" value="IBFS:/WFC/Repository/P459_S33046_Val_API"]
        """
        self.Log.Message(STEP_01_EXPECTED)
        git_connection.verify_returncode('01.01')
        git_connection.verify_ibfsparams_key_value('IBIRS_path', [IBIRS_path], '01.02')
        
        STEP_02 = """
            STEP 02 : Run pwaList using API
        """
        self.Log.Message(STEP_02)
        pwa_list = pwaList()
        
        STEP_02_EXPECTED = """
            STEP 02 Expected : Verify returncode="10000" and [pwaFolderRelToUser="WFC\Repository\P459_S33046_Val_API".
            connectionUrl="https://github.com/scmdev1/QA_Val_API", scmUser="scmdev1", scmPassword ="[AES128I]<encrypted_value>"]
        """
        self.Log.Message(STEP_02_EXPECTED)
        git_connection_props = [{'connectionUrl' : IBIRS_gitRepository, 'scmUser' : IBFS_userName, 'scmPassword' : git_encrypted_pass}]
        pwa_git_con_xpath = pwa_list.XmlNode.pwa_git_connection.format(IBIRS_path)
        pwa_list.verify_returncode('02.01')
        pwa_list.XMLAssertions.assertAttributesListIn(pwaList.XmlNode.rootObject_item, pwa_item, '02.02', ignore_keys=['index'])
        pwa_list.XMLAssertions.assertAttributesListEqual(pwa_git_con_xpath, git_connection_props, '02.03', match_case=True)