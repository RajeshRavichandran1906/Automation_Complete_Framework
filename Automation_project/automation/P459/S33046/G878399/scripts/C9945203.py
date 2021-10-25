"""----------------------------------------------------
Author Name  : Prabhakaran
Automated on : 21 April 2020
----------------------------------------------------"""

from common.webservices import BaseTestCase
from common.webservices import pwa

class C9945203_TestClass(BaseTestCase):
    
    def test_C9945203(self):
        
        """
        TEST CASE VARIABLS
        """
        username_key = 'devuser1'
        password_key = 'devpass1'
        repository   =  self.get_config_file_key_value('IBIRS_path')
        user_name    =  self.get_config_file_key_value(username_key)
        pwa_item     =  [{'_jt': 'IBFSPwaWfcGenGitProps', 'pwaBindingFolder': 'git', 'pwaFolderRelToUser': 'WFC/Repository/P459_S33046_Val_API', 'pwaIbfsRoot': 'IBFS:/WFC/Repository/P459_S33046_Val_API', 'userWorkingFolder': user_name}]
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS and create run pwaCreate using API.
        """
        self.Log.Message(STEP_01)
        self.signOn(username_key, password_key)
        pwa.pwaDelete(repository) # Deleting pwa before creating.
        pwaCreate = pwa.pwaCreate(repository)
        
        STEP_01_EXPECTED = """
            STEP 01 Expected : Verify returncode="10000" and <entry key="IBIRS_path" value="IBFS:/WFC/Repository/P459_S33046_Val_API"/>
        """
        self.Log.Message(STEP_01_EXPECTED)
        pwaCreate.verify_returncode('01.01')
        pwaCreate.verify_ibfsparams_key_value('IBIRS_path', [repository], '01.02')
        
        STEP_02 = """
            STEP 02 : Run pwaList using API
        """
        self.Log.Message(STEP_02)
        pwaList = pwa.pwaList()
        
        STEP_02_EXPECTED = """
            STEP 02 Expected : Verify returncode="10000" and pwaList item
        """
        self.Log.Message(STEP_02_EXPECTED)
        pwaList.verify_returncode('02.01')
        pwaList.XMLAssertions.assertAttributesListIn(pwaList.XmlNode.rootObject_item, pwa_item, '02.02', ignore_keys=['index'])