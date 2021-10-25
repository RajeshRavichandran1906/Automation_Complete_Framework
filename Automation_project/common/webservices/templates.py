from ._common_ import Common

class _base_(Common):
    
    def __init__(self):
        
        super(_base_, self).__init__()
        self._IBIRS_service_ = 'templates'
        
class create(_base_):
    
    def __init__(self, IBIRS_fileName):
        super().__init__()
        self._IBIRS_action_ = 'create'
        params={
            'IBIRS_service' : self._IBIRS_service_,
            'IBIRS_action' : self._IBIRS_action_,
            'IBIRS_fileName' : IBIRS_fileName,
            'IBIWF_SES_AUTH_TOKEN' : self._IBIWF_SES_AUTH_TOKEN
        }
        self._post_(self._base_url_, data=params)

class run(_base_):
    
    def __init__(self, IBIRS_fileName, IBIRS_vars, IBIRS_args='__null'):
        super().__init__()    
        self._IBIRS_action_ = 'run'
        params={
            'IBIRS_service' : self._IBIRS_service_,
            'IBIRS_action' : self._IBIRS_action_,
            'IBIRS_fileName' : IBIRS_fileName,
            'IBIRS_vars' : IBIRS_vars,
            'IBIRS_args' : IBIRS_args,
            'IBIWF_SES_AUTH_TOKEN' : self._IBIWF_SES_AUTH_TOKEN
        }    
        self._post_(self._base_url_, params=params)