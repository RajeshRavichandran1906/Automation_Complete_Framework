"""----------------------------------------------------
Author Name  : Prabhakaran
Automated on : 23 April 2020
----------------------------------------------------"""

from common.webservices.git import gitFetch
from common.webservices import BaseTestCase

class C9945267_TestClass(BaseTestCase):
    
    def test_C9945267(self):
        
        """
        TEST CASE VARIABLS
        """
        IBIRS_path = self.get_config_file_key_value('IBIRS_path')
        trackingRefUpdates_items_attrib = [{'localName': 'refs/remotes/origin/Branch_Val_API', 'remoteName': 'refs/heads/Branch_Val_API', 'result': 'NEW'}, {'localName': 'refs/remotes/origin/master', 'remoteName': 'refs/heads/master', 'result': 'NEW'}]
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS and Run gitFetch with IBIRS_path=IBFS:/WFC/Repository/P459_S33046_Val_API
        """
        self.Log.Message(STEP_01)
        self.signOn('devuser1', 'devpass1')
        git_fetch = gitFetch(IBIRS_path) 
        
        STEP_01_EXPECTED = """
            STEP 01 Expected : Verify returncode="10000" and [localName="refs/remotes/origin/Branch_Val_API" remoteName="refs/heads/Branch_Val_API" result="NEW"]
            and [localName="refs/remotes/origin/master" remoteName="refs/heads/master" result="NEW"]
        """
        self.Log.Message(STEP_01_EXPECTED)
        git_fetch.verify_returncode('01.01')
        git_fetch.XMLAssertions.assertAttributesListIn(git_fetch.XmlNode.trackingRefUpdates_item, trackingRefUpdates_items_attrib, '01.02', match_case=True)