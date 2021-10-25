"""----------------------------------------------------
Author Name  : Prabhakaran
Automated on : 29 May 2020
----------------------------------------------------"""

from common.webservices.pwa import pwaCommit, pwaList
from common.webservices import BaseTestCase

class C9945230_TestClass(BaseTestCase):
    
    def test_C9945230(self):
        
        """
        TEST CASE VARIABLS
        """
        IBIRS_path = self.get_config_file_key_value('IBIRS_path')
        
        STEP_01 = """
            STEP 01 : Run pwaCommit with parameters: IBFS_path =IBFS:/WFC/Repository/P459_S33046_Val_API, IBFS_closePWA = true
        """
        self.Log.Message(STEP_01)
        self.signOn('devuser1', 'devpass1')
        pwa_commit = pwaCommit(IBIRS_path)
        
        STEP_01_EXPECTED = """
            STEP 01 Expected : Verify returncode="10000" and IBFS_closePWA, IBFS_path values.
        """
        self.Log.Message(STEP_01_EXPECTED)
        pwa_commit.verify_returncode('01.01')
        pwa_commit.verify_ibfsparams_key_value('IBIRS_closePWA', ['true'], '01.02')
        pwa_commit.verify_ibfsparams_key_value('IBIRS_path', [IBIRS_path], '01.03')
        
        STEP_02 = """
            STEP 02 : Run pwaList
        """
        self.Log.Message(STEP_02)
        pwa_list = pwaList()
        
        STEP_02_EXPECTED = """
            STEP 02 Expected : Verify returncode="10000" and Removed domain is not listed in the response:
        """
        self.Log.Message(STEP_02_EXPECTED)
        pwa_list.verify_returncode('02.01')
        pwa_list.XMLAssertions.assertAttributesListNotIn(pwa_list.XmlNode.rootObject_item, [{'pwaIbfsRoot' : IBIRS_path}], '02.02')