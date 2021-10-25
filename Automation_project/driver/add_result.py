import sys
from testrail import testrail as tr

runid=sys.argv[1]
testid=sys.argv[2]
status=sys.argv[3]
pkgname=sys.argv[4]
browser=sys.argv[5]
release=sys.argv[6]
confid=sys.argv[7]
testtool=sys.argv[8]
product=sys.argv[9]
print("Testing")
client = tr.APIClient('http://lnxtestrail.ibi.com/testrail/')
client.user = 'bigscm@ibi.com'
client.password = 'Li47OFB.CFpL1diBiImX-iDa9PymKNq7v47dAz4nR'


cmd='add_result_for_case/'+runid+'/'+testid
resp=''
try:
    resp=client.send_post(cmd,{ 'status_id':status,'custom_pkgname':pkgname,'custom_browsers':browser,
        'custom_configurations':confid,'custom_run_mode':testtool,'custom_release':release,
        'custom_prodid':product,'custom_atm_issues':1})
except:
    print("Unable to Update Result to Test Rail.")