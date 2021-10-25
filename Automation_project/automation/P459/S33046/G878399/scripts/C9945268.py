"""----------------------------------------------------
Author Name  : Prabhakaran
Automated on : 13 May 2020
----------------------------------------------------"""

from common.webservices.git import gitPull
from common.webservices import BaseTestCase

class C9945268_TestClass(BaseTestCase):
    
    def test_C9945268(self):
        
        """
        TEST CASE VARIABLS
        """
        IBIRS_path = self.get_config_file_key_value('IBIRS_path')
        expected_attrib = {'_jt': 'IBFSGitMergeStatus', 'status': 'Merged', 'successful': 'true'}
        
        STEP_01 = """
            STEP 01 : Run gitPull with IBIRS_path=IBFS:/WFC/Repository/P459_S33046_Val_API
        """
        self.Log.Message(STEP_01)
        self.signOn('devuser1', 'devpass1')
        git_pull = gitPull(IBIRS_path) 
        
        STEP_01_EXPECTED = """
            STEP 01 Expected : Verify following returncode="10000" and <mergeStatus _jt="IBFSGitMergeStatus" status="Merged" successful="true"/>
        """
        self.Log.Message(STEP_01_EXPECTED)
        git_pull.verify_returncode('01.01')
        git_pull.XMLAssertions.assertAttributesEqual(git_pull.XmlNode.mergeStatus, expected_attrib, '01.02')