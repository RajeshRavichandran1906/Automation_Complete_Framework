"""----------------------------------------------------
Author Name  : Prabhakaran
Automated on : 05 May 2020
----------------------------------------------------"""

from common.webservices.git import gitPush
from common.webservices import BaseTestCase

class C9945707_TestClass(BaseTestCase):
    
    def test_C9945707(self):
        
        """
        TEST CASE VARIABLS
        """
        IBIRS_path = self.get_config_file_key_value('IBIRS_path')
        trackingRefUpdate = [{'_jt': 'IBFSGitTrackingRefUpdate', 'localName': 'refs/remotes/origin/Branch_Val_API', 'remoteName': 'refs/heads/Branch_Val_API', 'result': 'FORCED'}]
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS and Run gitPush with IBIRS_path=IBFS:/WFC/Repository/P459_S33046_Val_API
        """
        self.Log.Message(STEP_01)
        self.signOn('devuser1', 'devpass1')
        git_push = gitPush(IBIRS_path)
         
        STEP_01_EXPECTED = """
            STEP 01 Expected : Verify returncode="10000" [<trackingRefUpdate _jt="IBFSGitTrackingRefUpdate" localName="refs/remotes/origin/Branch_Val_API" remoteName="refs/heads/Branch_Val_API" result="FORCED">]
        """
        self.Log.Message(STEP_01_EXPECTED)
        git_push.verify_returncode('01.01')
        git_push.XMLAssertions.assertAttributesListIn(git_push.XmlNode.IBFSGitPushResult_trackingRefUpdate, trackingRefUpdate, '01.02')