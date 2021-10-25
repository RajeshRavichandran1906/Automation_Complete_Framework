"""----------------------------------------------------
Author Name  : Prabhakaran
Automated on : 23 April 2020
----------------------------------------------------"""

from common.webservices.git import gitStatus
from common.webservices import BaseTestCase

class C9945263_TestClass(BaseTestCase):
    
    def test_C9945263(self):
        
        """
        TEST CASE VARIABLS
        """
        IBIRS_path = self.get_config_file_key_value('IBIRS_path')
        expected_item_attrib = [{'_jt': 'IBFSScmStatusObjectPair', 'path': 'IBFS:/WFC/Repository/P459_S33046_Val_API/scm_vis1.fex'}, {'_jt': 'IBFSScmStatusObjectPair', 'path': 'IBFS:/WFC/Repository/P459_S33046_Val_API'}, {'_jt': 'IBFSScmStatusObjectPair', 'path': 'IBFS:/WFC/Repository/P459_S33046_Val_API/Hidden_Content'}]
        expected_status_attrib = [{'_jt': 'IBFSScmStatusObject', 'contentStatus': 'UNTRACKED', 'metadatsStatus': 'UNTRACKED', 'status': 'UNTRACKED'}, {'_jt': 'IBFSScmStatusObject', 'metadatsStatus': 'UNTRACKED', 'status': 'UNTRACKED'}, {'_jt': 'IBFSScmStatusObject', 'contentStatus': 'UNTRACKED_FOLDER', 'metadatsStatus': 'UNTRACKED', 'status': 'UNTRACKED|UNTRACKED_FOLDER'}]
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS and Run gitBranch with Run gitStatus with IBFS_gitStatusParams=IBFS:/WFC/Repository/P459_S33046_Val_API
        """
        self.Log.Message(STEP_01)
        self.signOn('devuser1', 'devpass1')
        git_status = gitStatus(IBIRS_gitStatusParams=IBIRS_path)
        
        STEP_01_EXPECTED = """
            STEP 01 Expected : Verify returncode="10000" and <item>, <status> tags values.
        """
        self.Log.Message(STEP_01_EXPECTED)
        file_xpath = git_status.XmlNode.rootObject_item_staus.format(expected_item_attrib[0]['path'])
        folder_xpath = git_status.XmlNode.rootObject_item_staus.format(expected_item_attrib[1]['path'])
        hidden_content_xpath = git_status.XmlNode.rootObject_item_staus.format(expected_item_attrib[2]['path'])
        git_status.verify_returncode('01.01')
        git_status.XMLAssertions.assertAttributesListIn(git_status.XmlNode.rootObject_item, expected_item_attrib, '01.02', ['index'])
        git_status.XMLAssertions.assertAttributesEqual(file_xpath, expected_status_attrib[0], '01.03')
        git_status.XMLAssertions.assertAttributesEqual(folder_xpath, expected_status_attrib[1], '01.04')
        git_status.XMLAssertions.assertAttributesEqual(hidden_content_xpath, expected_status_attrib[2], '01.05')