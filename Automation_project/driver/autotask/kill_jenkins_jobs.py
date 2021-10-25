import argparse
from jenkins import Jenkins
import getpass

arg_parse = argparse.ArgumentParser()
arg_parse.add_argument("-servername", help="Name of the Jenkins name : jenkins or jenkins-prod", required=True, type=str)
arg_parse.add_argument("-username", default="guest", help="Jenkins user name")
arg_parse.add_argument("-password", default="guest", help="Jenkins password")
arg_parse.add_argument("-jobname", default="guest", help="Jenkins job name", required=True, type=str)
args = arg_parse.parse_args()

servername = args.servername.strip().lower()

class Jobs :
    
    def __init__(self, url, user_name, password, job_name):
        
        self._job_name = job_name
        self._server = self._connect_server(url, user_name, password)
        
    def _connect_server(self, url, user_name, password):
        """
        Return the server object
        """
        try :
            server = Jenkins(url, user_name, password)
            server.get_views()
            return server
        except Exception as msg :
            print("[ERROR] : Please check given user name and password")
            input("Please enter to exit")
            exit()
            
    def _get_running_job_number_by_name(self):
        """
        Return running jobs number by job name
        """
        print("[INFO] : Getting running jobs info...")
        job_list = self._server.get_running_builds()
        job_number_list = [job['number'] for job in job_list if job['name'].replace("%20", " ") == self._job_name]
        print("[INFO] : [{0}] Jobs are running".format(len(job_number_list)))
        return job_number_list
    
    def _get_queue_job_id_by_job_name(self):
        """
        Return the queue job id from specific job
        """
        
        print("[INFO] : Getting queue jobs info...")
        queue_jobs_list = self._server.get_queue_info()
        queue_jobs_id = [job['id'] for job in queue_jobs_list if job['task']['name'] == self._job_name]
        print("[INFO] : [{0}] Jobs are in queue".format(len(queue_jobs_id)))
        return queue_jobs_id
     
    def kill_running_jobs(self):
        """
        Kill the running jobs
        """
        print("\n--------------------- KILL {0} RUNNING JOBS ---------------------".format(self._job_name.upper()))
        job_number_list = self._get_running_job_number_by_name()
        for job_number in job_number_list :
            self._server.stop_build(self._job_name, job_number)
            print("[INFO] : [{0}] Job killed".format(job_number))
        print("\n")
    def kill_queue_jobs(self):
        """
        Kill the all queue jobs
        """
        print("\n--------------------- KILL {0} QUEUE JOBS ---------------------".format(self._job_name.upper()))
        queue_id_list = self._get_queue_job_id_by_job_name()
        for id_value in queue_id_list :
            self._server.cancel_queue(id_value)
            print("[INFO] : [{0}] Queue job killed".format(id_value))
        print("\n")

if servername == "jenkins":
    url = "http://jenkins.ibi.com:8080"
elif servername == "jenkins-prod":
    url = "http://jenkins-prod.ibi.com:8080"
else:
    raise ValueError("Invalid Jenkins server name. Available jenkins server : jenkins, jenkins-prod")
job = Jobs(url, args.username, args.password, args.jobname)
job.kill_queue_jobs()
job.kill_running_jobs()