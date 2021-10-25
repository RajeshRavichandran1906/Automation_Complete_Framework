"""----------------------------------------------------
Author Name  : Prabhakaran
Automated on : 12 May 2020
----------------------------------------------------"""

from common.webservices.git import gitStatus
from common.webservices.pwa import pwaCommit
from common.webservices import BaseTestCase

class C9945269_TestClass(BaseTestCase):
    
    def test_C9945269(self):
        
        """
        TEST CASE VARIABLS
        """
        IBIRS_path = self.get_config_file_key_value('IBIRS_path')
        added_file = [{'path' : IBIRS_path + "/scm_vis1.fex"}]
        
        STEP_01 = """
            STEP 01 : Run gitStatus with IBFS_gitStatusParams=IBFS:/WFC/Repository/P459_S33046_Val_AP
        """
        self.Log.Message(STEP_01)
        self.signOn('devuser1', 'devpass1')
        git_status = gitStatus(IBIRS_gitStatusParams=IBIRS_path)
        
        STEP_01_EXPECTED = """
            STEP 01 Expected : Verify returncode="10000" and
            path='IBFS:/WFC/Repository/P459_S33046_Val_API/scm_vis1.fex not in response
        """
        self.Log.Message(STEP_01_EXPECTED)
        git_status.verify_returncode('01.01')
        git_status.XMLAssertions.assertAttributesListNotIn(git_status.XmlNode.rootObject_item, added_file, '01.02')
        
        STEP_02 = """
            STEP 02 : Run pwaCommit with IBIRS_path=IBFS:/WFC/Repository/P459_S33046_Val_API and IBFS_closePWA = false
        """
        self.Log.Message(STEP_02)
        pwa_commit = pwaCommit(IBIRS_path, 'false')
        
        STEP_02_EXPECTED = """
            STEP 02 Expected : Verify returncode="10000".
        """
        self.Log.Message(STEP_02_EXPECTED)
        pwa_commit.verify_returncode('02.01')