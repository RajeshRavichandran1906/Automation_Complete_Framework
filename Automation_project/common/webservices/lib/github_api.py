import requests
import json

class GitHubApi:
    
    def __init__(self, user_name='scmdev1', oauth_token='be596757291f784c951cf5b2e68cce8b6c3854c9'):
        """
        Description : This class will perform various github actions using API.
        Examples - create repository, delete repository, create repository branch and etc.
        :param - user_name : Github account user name
        :param - oauth_token : token value to access github. 
        Note : This class only for personal user api calls. 
        """
        self._user_name = user_name
        self._oauth_token = oauth_token
    
    def create_repository(self, name, description=None, private=False, auto_init=True):
        """
        Description : Create the new Github repository. 
        Return True if repository created successfully else raise RequestException
        :param - name : Name of the gihub repository
        :param - description : Description about the repository
        :param - private - If True then repository will create as private else public.
        """
        url = "https://api.github.com/user/repos?access_token={0}".format(self._oauth_token)
        data = {'name' : name, 'description' : description, 'private' : private, 'auto_init' : auto_init}
        response = requests.post(url, json.dumps(data))
        if response.status_code == 201 :
            return True
        error_msg = "Unable to create [{0}] repository. Please check log file for more info.".format(name)
        raise requests.exceptions.RequestException(error_msg)
    
    def delete_repository(self, name):
        """
        Description : Delete the existing Github repository. 
        Return True if repository deleted successfully else raise RequestException.
        :param - name : Name of the gihub repository.
        """
        url = "https://api.github.com/repos/{0}/{1}?access_token={2}".format(self._user_name, name, self._oauth_token)
        response = requests.delete(url)
        if response.status_code == 204 :
            return True
        elif response.status_code == 404:
            error_msg = "[{0}] Repository not found in Github".format(name)
        else :
            error_msg = "Unable to delete [{0}] repository. Please check log file for more info.".format(name)
        raise requests.exceptions.RequestException(error_msg)
    
    def create_branch(self, repo_name, branch_name):
        """
        Description : Create the new new branch for Github repository. 
        Return True if repository branch created successfully else raise RequestException
        :param - repo_name : Name of the gihub repository
        :param - branch_name : Name of the gihub repository branch
        """
        sha = self._get_repository_sha_value_(repo_name)
        data = {"ref" : 'refs/heads/{0}'.format(branch_name), "sha" : sha}
        url = "https://api.github.com/repos/{0}/{1}/git/refs?access_token={2}".format(self._user_name, repo_name ,self._oauth_token)
        response = requests.post(url, json.dumps(data))
        if response.status_code == 201 :
            return True
        error_msg = "Unable to create [{0}] branch for [{1}] repository. Please check log file for more info.".format(branch_name, repo_name)
        raise requests.exceptions.RequestException(error_msg)
    
    def create_pull_request(self, repro, title, head, base, **kwargs):
        """
        Description : Create the GitHub pull request using api. Return pull request number if success. 
        Reference Link : https://developer.github.com/v3/pulls/#create-a-pull-request
        """
        data = {'title' : title, 'head' : head, 'base' : base}
        data.update(kwargs)
        url = 'https://api.github.com/repos/{0}/{1}/pulls?access_token={2}'.format(self._user_name, repro, self._oauth_token)
        response = requests.post(url, data=json.dumps(data))
        if response.status_code == 201 :
            response_json = response.json()
            return response_json['number']
        error_msg = "Unable to create pull request repository. Please check log file for more info."
        raise requests.exceptions.RequestException(error_msg)
    
    def merge_pull_request(self, repro, pull_number):
        """
        Description : Merge the pull request. Return True if success
        Reference Link : https://developer.github.com/v3/pulls/#merge-a-pull-request-merge-button
        """
        url = 'https://api.github.com/repos/{0}/{1}/pulls/{2}/merge?access_token={3}'.format(self._user_name, repro, pull_number, self._oauth_token)
        response = requests.put(url)
        if response.status_code == 200 :
            return True
        error_msg = "Pull Request is not mergeable. Please check log file for more info."
        raise requests.exceptions.RequestException(error_msg)
    
    def _get_repository_sha_value_(self, repo_name):
        """
        Desciption : Return the repository reference value(sha value)
        :param - repo_name : Name of the gihub repository.
        """
        url = "https://api.github.com/repos/{0}/{1}/git/refs/heads?access_token={2}".format(self._user_name, repo_name, self._oauth_token)
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()[0]['object']['sha']
        error_msg = "Unable to get sha value for [{0}] repository. Please check log file for more info.".format(repo_name)
        raise requests.exceptions.RequestException(error_msg)
