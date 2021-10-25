"""----------------------------------------------------
Author Name  : Prabhakaran
Automated on : 27 April 2020
----------------------------------------------------"""

from common.webservices.git import gitStatus, gitAdd
from common.webservices import BaseTestCase

class C9945264_TestClass(BaseTestCase):
    
    def test_C9945264(self):
        
        """
        TEST CASE VARIABLS
        """
        IBIRS_path = self.get_config_file_key_value('IBIRS_path')
        add_file = IBIRS_path + "/scm_vis1.fex"
        expected_item_attrib = [{'_jt': 'IBFSScmStatusObjectPair', 'path': 'IBFS:/WFC/Repository/P459_S33046_Val_API/scm_vis1.fex'}]
        expected_status_attrib = {'_jt': 'IBFSScmStatusObject', 'contentStatus': 'ADDED', 'metadatsStatus': 'ADDED', 'status': 'ADDED'}
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS and Run gitAdd with IBFS_gitAddParams=IBFS:/WFC/Repository/P459_S33046_Val_API/scm_vis1.fex
        """
        self.Log.Message(STEP_01)
        self.signOn('devuser1', 'devpass1')
        git_add = gitAdd(IBIRS_gitAddParams=add_file)
        
        STEP_01_EXPECTED = """
            STEP 01 Expected : Verify returncode="10000" IBIRS_gitAddParams value
        """
        self.Log.Message(STEP_01_EXPECTED)
        git_add.verify_returncode('01.01')
        git_add.verify_ibfsparams_key_value('IBIRS_gitAddParams', [add_file], '01.02')
        
        STEP_02 = """
            STEP 02 : Run gitStatus with IBFS_gitStatusParams=IBFS:/WFC/Repository/P459_S33046_Val_API
        """
        self.Log.Message(STEP_02)
        git_status = gitStatus(IBIRS_gitStatusParams=IBIRS_path)
        
        STEP_02_EXPECTED = """
            STEP 02 Expected : Verify returncode="10000" and <item>, <status> tags values.
        """
        self.Log.Message(STEP_02_EXPECTED)
        file_xpath = git_status.XmlNode.rootObject_item_staus.format(expected_item_attrib[0]['path'])
        git_status.verify_returncode('02.01')
        git_status.XMLAssertions.assertAttributesListIn(git_status.XmlNode.rootObject_item, expected_item_attrib, '02.02', ['index'])
        git_status.XMLAssertions.assertAttributesEqual(file_xpath, expected_status_attrib, '01.03')