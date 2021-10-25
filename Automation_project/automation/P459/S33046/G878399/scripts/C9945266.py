"""----------------------------------------------------
Author Name  : Prabhakaran
Automated on : 12 May 2020
----------------------------------------------------"""

from common.webservices.git import gitCheckout
from common.webservices import BaseTestCase

class C9945266_TestClass(BaseTestCase):
    
    def test_C9945266(self):
        
        """
        TEST CASE VARIABLS
        """
        IBIRS_path = self.get_config_file_key_value('IBIRS_path')
        rootObject_attrib = {'_jt': 'IBFSGitCheckoutResult', 'status': 'OK'}
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS and Run gitCheckout with [IBIRS_path=IBFS:/WFC/Repository/P459_S33046_Val_API, 
            IBFS_gitCheckoutOptions=--track, IBFS_gitCheckoutParams=origin/master]
        """
        self.Log.Message(STEP_01)
        self.signOn('devuser1', 'devpass1')
        git_checkout = gitCheckout(IBIRS_path, '--track', 'origin/master')
        
        STEP_01_EXPECTED = """
            STEP 01 Expected : Verify returncode="10000" <rootObject _jt="IBFSGitCheckoutResult" status="OK"> and
            <entry key="IBIRS_gitCheckoutParams" value="origin/master"/>
        """
        self.Log.Message(STEP_01_EXPECTED)
        git_checkout.verify_returncode('01.01')
        git_checkout.XMLAssertions.assertAttributesEqual(git_checkout.XmlNode.rootObject, rootObject_attrib, '01.02')
        git_checkout.verify_ibfsparams_key_value('IBIRS_gitCheckoutParams', ['origin/master'], '01.03')