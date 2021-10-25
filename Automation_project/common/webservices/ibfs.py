from ._common_ import Common

class _base_(Common):
    
    def __init__(self):
        
        super(_base_, self).__init__()
        self._IBIRS_service_ = 'ibfs'
        
class signOn(_base_):
    
    def __init__(self, user_name, password):
        super(signOn, self).__init__()
        self._IBIRS_action_ = 'signOn'
        params={
            'IBIRS_action' : self._IBIRS_action_,
            'IBIRS_service' : self._IBIRS_service_,
            'IBIRS_userName' : user_name,
            'IBIRS_password' : password
        }
        self._post_(self._base_url_, params=params)
        
    def _get_properties_key_value_(self, key):
        """
        Description : Return the properties key value.
        :Usage - _get_properties_key_value_('IBI_CSRF_Token_Value')
        """
        xpath = "properties/entry[@key='{}']".format(key)
        keys = self._xml_parser_.root.findall(xpath)
        if keys != []:
            return keys[0].attrib['value']
        erro_msg = "[{0}] key not found in [properties entry] tag".format(key)
        raise KeyError(erro_msg)
    
class signOff(_base_):
    
    def __init__(self):
        super(signOff, self).__init__()
        self._IBIRS_action_ = 'signOff'
        params={
            'IBIRS_action' : self._IBIRS_action_,
            'IBIRS_service' : self._IBIRS_action_  
        }
        self._get_(self._base_url_, params=params)

class put(_base_):
    
    def __init__(self, IBIRS_path, IBIRS_object, IBIRS_private='__null', IBIRS_replace='true', IBIRS_args='__null'):
        super(put, self).__init__()
        self._IBIRS_action_ = 'put'
        params={
            'IBIRS_path' : IBIRS_path,
            'IBIRS_object' : IBIRS_object,
            'IBIRS_private' : IBIRS_private,
            'IBIRS_replace' : IBIRS_replace,
            'IBIRS_args' : IBIRS_args,
            'IBIRS_action' : self._IBIRS_action_,
            'IBIRS_service' : self._IBIRS_service_,
            'IBIWF_SES_AUTH_TOKEN' : self._IBIWF_SES_AUTH_TOKEN
        }
        self._post_(self._base_url_, params=params)