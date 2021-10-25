import unittest
from ._common_ import Common
from common.webservices.lib.log import Log
from common.webservices.ibfs import signOn
from common.webservices.ibfs import signOff
from common.webservices.lib.utils import Utils
from common.webservices.lib.assertions import Assertions

class BaseTestCase(unittest.TestCase):
    
    def setUp(self):
        
        self.Log = Log()
        self.Assertions = Assertions
        
    def signOn(self, user_key, password_key):
        """
        Description : Sign into webfocus.
        :Usage - signOn('adminuser' 'adminpass')
        """
        user_name = Utils.get_config_file_key_value(user_key)
        password = Utils.get_config_file_key_value(password_key)
        response =  signOn(user_name, password)
        returncod = response._xml_parser_.get_ibfsrpc_attribute_value('returncode')
        if returncod != '10000':
            returndesc = response._xml_parser_.get_ibfsrpc_attribute_value('returndesc')
            raise Exception(returndesc)
        Common._IBIWF_SES_AUTH_TOKEN = response._get_properties_key_value_('IBI_CSRF_Token_Value')
        return response
    
    def signOff(self):
        """
        Description : SignOff webfocus.
        """
        return signOff()
    
    def get_config_file_key_value(self, key):
        """
        Desciption : Return the key value from config.init file
        :Usage - get_config_file_key_value('nodeif')
        """
        return Utils.get_config_file_key_value(key)
    
    def tearDown(self):
        signOff()
        self.Log._write_(self._testMethodName.replace('test_', '').strip())
        if Assertions.failures != []:
            failure_logs = "\n".join(Assertions.failures)
            raise AssertionError("\n" + failure_logs)
        