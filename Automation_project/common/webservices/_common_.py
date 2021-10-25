import requests
from common.webservices.lib.log import Log
from common.webservices.lib.utils import Utils
from common.webservices.lib.xml_parser import XmlParser
from common.webservices.lib.assertions import Assertions
from common.webservices.lib.assertions import XMLAssertions

class Common:
    
    __session = requests.Session()
    _IBIWF_SES_AUTH_TOKEN = None
    
    def __init__(self):
        
        self._session_ = self.__session
        self._assertions_ = Assertions
        self.__log = Log()
        self._IBIRS_action_ = None
        self._base_url_ = Utils.get_webfocus_url() + "rs"
        
    @property
    def _xml_parser_(self): return XmlParser(self._response_.text)
    
    @property
    def XMLAssertions(self): return XMLAssertions(self._xml_parser_.root, self._IBIRS_action_)
    
    def verify_returncode(self, step_num, expected_returncode="10000"):
        """
        Description : Verify the api url return code
        :Usage - verify_returncode('01.01')
        """
        actual_returncode = self._xml_parser_.get_ibfsrpc_attribute_value('returncode')
        action_name = self._xml_parser_.get_ibfsrpc_attribute_value('name')
        msg = "STEP {0} : Verify [{1}] action returns [{2}]".format(step_num, action_name, expected_returncode)
        self._assertions_.assertEqual(expected_returncode, actual_returncode, msg)
    
    def verify_ibfsparams_key_value(self, key, expected_values, step_num):
        """
        Description : Verify the <ibfsparams> xml tag key values
        :Usage - verify_ibfsparams_key_values('IBIRS_path', ['IBFS:/WFC/Repository/P459_S33046_Val_API'], '04.01')
        """
        xpath = "ibfsparams/entry[@key='{}']".format(key)
        keys = self._xml_parser_.root.findall(xpath)
        actual_values = [key.attrib['value'] for key in keys]
        msg = "STEP {0} : Verify [{1}] key value in [ibfsparams] node".format(step_num, key)
        self._assertions_.assertEqual(expected_values, actual_values, msg)
    
    def _post_(self, url, data=None, json=None, **kwargs):
        
        self._response_ = self._session_.post(url, data=data, json=json, **kwargs)
        self.__log.IBIRSResponse(self._response_, self._IBIRS_action_)
    
    def _get_(self, url, params=None, **kwargs):
        
        self._response_ = self._session_.get(url, params=params, **kwargs)
        self.__log.IBIRSResponse(self._response_, self._IBIRS_action_)
    
    def _put_(self, url, data=None, **kwargs):
        
        self._response_ = self._session_.put(url, data=data, **kwargs)
        self.__log.IBIRSResponse(self._response_, self._IBIRS_action_)