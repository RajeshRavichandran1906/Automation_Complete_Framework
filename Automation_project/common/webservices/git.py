from ._common_ import Common

class _base_(Common):
    
    def __init__(self):
        
        super(_base_, self).__init__()
        self._IBIRS_service_='git'
       
class gitAdd(_base_):
    
    def __init__(self, IBIRS_gitAddOptions='__null', IBIRS_gitAddParams='__null', IBIRS_args='__null'):
        super(gitAdd , self).__init__()
        self._IBIRS_action_ = 'gitAdd'
        params={
            'IBIRS_gitAddOptions' : IBIRS_gitAddOptions, 
            'IBIRS_gitAddParams' : IBIRS_gitAddParams, 
            'IBIRS_args' : IBIRS_args,
            'IBIRS_service' : self._IBIRS_service_,
            'IBIRS_action' : self._IBIRS_action_,
        }
        self._get_(self._base_url_, params=params)
        
class gitBranch(_base_):
    
    def __init__(self, IBIRS_path, IBIRS_gitBranchOptions='__null', IBIRS_gitBranchParams='__null', IBIRS_args='__null'):
        super(gitBranch, self).__init__()
        self._IBIRS_action_ = 'gitBranch'
        params={
            'IBIRS_path' : IBIRS_path,
            'IBIRS_gitBranchOptions' : IBIRS_gitBranchOptions,  
            'IBIRS_gitBranchParams' : IBIRS_gitBranchParams,
            'IBIRS_args' : IBIRS_args,
            'IBIRS_service' : self._IBIRS_service_,
            'IBIRS_action' : self._IBIRS_action_,
        }
        self._get_(self._base_url_, params=params)
    
    def verify_IBFSGitRef_name(self, expected_names, step_num):
        """
        Description : Verify the IBFSGitRef names
        :Usage - verify_IBFSGitRef_name(['refs/heads/master'], '03.01')
        """
        xpath = "rootObject[@_jt='IBFSGitBranchResult']/listResults/item[@_jt='IBFSGitRef']"
        nodes = self._xml_parser_.root.findall(xpath)
        actual_names = [node.attrib['name'] for node in nodes if 'name' in node.attrib]
        msg = 'STEP {0} : Verify IBFSGitRef name'.format(step_num)
        self._assertions_.assertEqual(expected_names, actual_names, msg)
        
class gitCheckout(_base_):
    
    def __init__(self, IBIRS_path, IBIRS_gitCheckoutOptions='__null', IBIRS_gitCheckoutParams='__null', IBIRS_args='__null'):
        super(gitCheckout, self).__init__()
        self._IBIRS_action_ = 'gitCheckout'
        params={
            'IBIRS_path' : IBIRS_path,
            'IBIRS_gitCheckoutOptions' : IBIRS_gitCheckoutOptions,  
            'IBIRS_gitCheckoutParams' : IBIRS_gitCheckoutParams,
            'IBIRS_args' : IBIRS_args,
            'IBIRS_service' : self._IBIRS_service_,
            'IBIRS_action' : self._IBIRS_action_,
        }
        self._get_(self._base_url_, params=params)
    
    class XmlNode:
        
        rootObject = "rootObject"
        
class gitClone(_base_):
    
    def __init__(self):
        super(gitClone, self).__init__()

class gitCommit(_base_):
    
    def __init__(self, IBIRS_gitCommitOptions='__null', IBIRS_gitCommitParams='__null', IBIRS_args='__null'):
        super(gitCommit, self).__init__()
        self._IBIRS_action_ = 'gitCommit'
        params={
            'IBIRS_gitCommitOptions' : IBIRS_gitCommitOptions,
            'IBIRS_gitCommitParams' : IBIRS_gitCommitParams,  
            'IBIRS_args' : IBIRS_args,
            'IBIRS_action' : self._IBIRS_action_,
            'IBIRS_service' : self._IBIRS_service_, 
        }
        self._get_(self._base_url_, params=params)
    
    class XmlNode:
        
        rootObject = "rootObject"
        IBFSGitRevCommit_item = rootObject + "/item[@commitTime]"
        IBFSGitRevCommit_parent_item = rootObject + "/item[@commitTime]/parents/item[@commitTime]"
        
class gitConnectToProject(_base_):
    
    def __init__(self):
        super(gitConnectToProject, self).__init__()

class gitConnectionSettings(_base_):
    
    def __init__(self, IBIRS_path, IBIRS_userName, IBIRS_password, IBIRS_gitEmail, IBIRS_gitRepository, IBIRS_args='__null'):
        super(gitConnectionSettings, self).__init__()
        self._IBIRS_action_ = 'gitConnectionSettings'
        params={
            'IBIRS_path' : IBIRS_path,
            'IBIRS_userName' : IBIRS_userName,  
            'IBIRS_password' : IBIRS_password,
            'IBIRS_gitEmail' : IBIRS_gitEmail,
            'IBIRS_gitRepository' : IBIRS_gitRepository,
            'IBIRS_args' : IBIRS_args,
            'IBIRS_action' : self._IBIRS_action_,
            'IBIRS_service' : self._IBIRS_service_, 
            'IBIWF_SES_AUTH_TOKEN' : self._IBIWF_SES_AUTH_TOKEN
        }
        self._post_(self._base_url_, params=params)
      
class gitFetch(_base_):
    
    def __init__(self, IBIRS_path, IBIRS_gitFetchOptions='__null', IBIRS_gitFetchParams='__null', IBIRS_args='__null'):
        super(gitFetch, self).__init__()
        self._IBIRS_action_ = 'gitFetch'
        params={
            'IBIRS_path' : IBIRS_path,
            'IBIRS_gitFetchOptions' : IBIRS_gitFetchOptions, 
            'IBIRS_gitFetchParams' : IBIRS_gitFetchParams,
            'IBIRS_args' : IBIRS_args,
            'IBIRS_service' : self._IBIRS_service_,
            'IBIRS_action' : self._IBIRS_action_,
        }
        self._get_(self._base_url_, params=params)
    
    class XmlNode:
        
        trackingRefUpdates_item = "rootObject/trackingRefUpdates/item"
        
class gitInfo(_base_):
    
    def __init__(self):
        super(gitInfo, self).__init__()

class gitInit(_base_):
    
    def __init__(self, IBIRS_path, IBIRS_gitInitOptions='__null', IBIRS_args='__null'):
        super(gitInit, self).__init__()
        self._IBIRS_action_ = 'gitInit'
        params={
            'IBIRS_path' : IBIRS_path,
            'IBIRS_gitInitOptions' : IBIRS_gitInitOptions,  
            'IBIRS_args' : IBIRS_args,
            'IBIRS_service' : self._IBIRS_service_,
            'IBIRS_action' : self._IBIRS_action_,
        }
        self._get_(self._base_url_, params=params)

class gitLog(_base_):
    
    def __init__(self, IBIRS_gitLogOptions='__null', IBIRS_gitLogParams='__null', IBIRS_args='__null'):
        super(gitLog, self).__init__()
        self._IBIRS_action_ = 'gitLog'
        params={
            'IBIRS_gitLogOptions' : IBIRS_gitLogOptions,
            'IBIRS_gitLogParams' : IBIRS_gitLogParams,  
            'IBIRS_args' : IBIRS_args,
            'IBIRS_service' : self._IBIRS_service_,
            'IBIRS_action' : self._IBIRS_action_,
        }
        self._get_(self._base_url_, params=params)
    
    class XmlNode:
        
        item_IBFSGitRevCommit = ".//item[@_jt='IBFSGitRevCommit']"
        item_authorIdent = item_IBFSGitRevCommit + """[@fullMessage="{0}"]/authorIdent"""
        
class gitMerge(_base_):
    
    def __init__(self):
        super(gitMerge, self).__init__()

class gitOpenProject(_base_):
    
    def __init__(self):
        super(gitOpenProject, self).__init__()
        
class gitPull(_base_):
    
    def __init__(self, IBIRS_path, IBIRS_gitPullOptions='__null', IBIRS_gitPullParams='__null', IBIRS_args='__null'):
        super(gitPull, self).__init__()
        self._IBIRS_action_ = 'gitPull'
        params={
            'IBIRS_path' : IBIRS_path,
            'IBIRS_gitPullOptions' : IBIRS_gitPullOptions, 
            'IBIRS_gitPullParams' : IBIRS_gitPullParams, 
            'IBIRS_args' : IBIRS_args,
            'IBIRS_service' : self._IBIRS_service_,
            'IBIRS_action' : self._IBIRS_action_,
        }
        self._get_(self._base_url_, params=params)
    
    class XmlNode:
        
        mergeStatus = "rootObject/mergeResult/mergeStatus"

class gitPush(_base_):
    
    def __init__(self, IBIRS_path, IBIRS_gitPushOptions='__null', IBIRS_gitPushParams='__null', IBIRS_args='__null'):
        super(gitPush, self).__init__()
        self._IBIRS_action_ = 'gitPush'
        params={
            'IBIRS_path' : IBIRS_path,
            'IBIRS_gitPushOptions' : IBIRS_gitPushOptions, 
            'IBIRS_gitPushParams' : IBIRS_gitPushParams, 
            'IBIRS_args' : IBIRS_args,
            'IBIRS_service' : self._IBIRS_service_,
            'IBIRS_action' : self._IBIRS_action_,
        }
        self._get_(self._base_url_, params=params)
    
    class XmlNode:
        
        IBFSGitPushResult_trackingRefUpdate = "rootObject/item/remoteUpdates/item/trackingRefUpdate"
        
class gitRemote(_base_):
    
    def __init__(self, IBIRS_path, IBIRS_gitRemoteOptions='__null', IBIRS_gitRemoteParams='__null', IBIRS_args='__null'):
        super(gitRemote, self).__init__()
        self._IBIRS_action_ = 'gitRemote'
        params={
            'IBIRS_path' : IBIRS_path,
            'IBIRS_gitRemoteOptions' : IBIRS_gitRemoteOptions, 
            'IBIRS_gitRemoteParams' : IBIRS_gitRemoteParams, 
            'IBIRS_args' : IBIRS_args,
            'IBIRS_service' : self._IBIRS_service_,
            'IBIRS_action' : self._IBIRS_action_,
        }
        self._get_(self._base_url_, params=params)
    
    class XmlNode:
        
        addResult = "rootObject/addResult"
        addResult_URIs_item = addResult + "/URIs/item"
        
class gitReset(_base_):
    
    def __init__(self):
        super(gitReset, self).__init__()

class gitRevisionContent(_base_):
    
    def __init__(self, IBIRS_path, IBIRS_gitRevisionContentOptions='__null', IBIRS_gitRevisionContentParams='__null', IBIRS_args='__null'):
        super(gitRevisionContent, self).__init__()
        self._IBIRS_action_ = 'gitRevisionContent'
        params={
            'IBIRS_path' : IBIRS_path,
            'IBIRS_gitRevisionContentOptions' : IBIRS_gitRevisionContentOptions, 
            'IBIRS_gitRevisionContentParams' : IBIRS_gitRevisionContentParams, 
            'IBIRS_args' : IBIRS_args,
            'IBIRS_service' : self._IBIRS_service_,
            'IBIRS_action' : self._IBIRS_action_,
        }
        self._get_(self._base_url_, params=params)
    
    class XmlNode:
        
        rootObject = "rootObject"
        
class gitStatus(_base_):
    
    def __init__(self, IBIRS_gitStatusOptions='__null', IBIRS_gitStatusParams='__null', IBIRS_args='__null'):
        super(gitStatus, self).__init__()
        self._IBIRS_action_ = 'gitStatus'
        params={
            'IBIRS_gitStatusOptions' : IBIRS_gitStatusOptions, 
            'IBIRS_gitStatusParams' : IBIRS_gitStatusParams, 
            'IBIRS_args' : IBIRS_args,
            'IBIRS_service' : self._IBIRS_service_,
            'IBIRS_action' : self._IBIRS_action_,
        }
        self._get_(self._base_url_, params=params)
    
    class XmlNode:
        
        rootObject_item = "rootObject/item"
        rootObject_item_staus = rootObject_item + "[@path='{0}']/status"