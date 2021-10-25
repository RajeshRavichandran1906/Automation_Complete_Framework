from ._common_ import Common

class _base_(Common):
    
    def __init__(self):
        
        super(_base_, self).__init__()
        self._IBIRS_service_ = 'pwa'
    
class pwaCreate(_base_):
    
    def __init__(self, IBIRS_path, IBIRS_createEmpty='false', IBIRS_args='__null'):
        super(pwaCreate, self).__init__()
        self._IBIRS_action_ = 'pwaCreate'
        params={
            'IBIRS_path' : IBIRS_path,
            'IBIRS_createEmpty' : IBIRS_createEmpty,  
            'IBIRS_args' : IBIRS_args,
            'IBIRS_action' : self._IBIRS_action_,
            'IBIRS_service' : self._IBIRS_service_  
        }
        self._get_(self._base_url_, params=params)

class pwaCommit(_base_):
    
    def __init__(self, IBIRS_path, IBIRS_closePWA='true', IBIRS_args='__null'):
        super(pwaCommit, self).__init__()
        self._IBIRS_action_ = 'pwaCommit'
        params={
            'IBIRS_path' : IBIRS_path,
            'IBIRS_closePWA' : IBIRS_closePWA,  
            'IBIRS_args' : IBIRS_args,
            'IBIRS_action' : self._IBIRS_action_,
            'IBIRS_service' : self._IBIRS_service_  
        }
        self._get_(self._base_url_, params=params)

class pwaDelete(_base_):
    
    def __init__(self, IBIRS_path, IBIRS_removePwaData='true', IBIRS_args='__null'):
        super(pwaDelete, self).__init__()
        self._IBIRS_action_ = 'pwaDelete'
        params={
            'IBIRS_path' : IBIRS_path,
            'IBIRS_removePwaData' : IBIRS_removePwaData,  
            'IBIRS_args' : IBIRS_args,
            'IBIRS_action' : self._IBIRS_action_,
            'IBIRS_service' : self._IBIRS_service_  
        }
        self._get_(self._base_url_, params=params)
         
class pwaList(_base_):
    
    def __init__(self, IBIRS_args='__null'):
        super(pwaList, self).__init__()
        self._IBIRS_action_ = 'pwaList'
        params={
            'IBIRS_args' : IBIRS_args,
            'IBIRS_action' : self._IBIRS_action_,
            'IBIRS_service' : self._IBIRS_service_  
        }
        self._get_(self._base_url_, params=params)
        
    class XmlNode:
        
        rootObject = "rootObject"
        rootObject_item = rootObject + "/item"
        pwa_git_connection = rootObject + "/item[@pwaIbfsRoot='{0}']/binding"