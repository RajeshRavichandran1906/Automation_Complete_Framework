import os, shutil
import glob
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from testrail import testrail as tr
import time
from selenium import webdriver
import uiautomation as automation

product=sys.argv[1]
release=sys.argv[2]
print(release)
confid=sys.argv[3]
pkgname=sys.argv[4]
project_id=sys.argv[5]
suite=sys.argv[6]
runid=sys.argv[7]
browser=sys.argv[8]

testtool='6'
root=os.getcwd()
new_suiteDir=root+'/qa2/sikuli'
print('new_suiteDir_path: ', new_suiteDir)
# The below script moves the sikuli folder from qa2 to qa
#shutil.move(new_suiteDir, root)

suiteDir=root+'/qa2/sikuli/'+suite
print(suiteDir)
#rename existing wfscom to new name
wfscom_path='C:/Users/qaauto/AppData/Roaming/Information Builders/'
filename='wfscom.xml'
new_filename='wfscom_old.xml'
print('existing_path: ', wfscom_path+filename)
print('new_path: ', suiteDir+'/'+filename)
try:
    if os.path.isfile(wfscom_path+new_filename):
        os.remove(wfscom_path+new_filename)
except:
    pass
try:
    if os.path.isfile(wfscom_path+filename):
        os.rename(wfscom_path+filename, wfscom_path+new_filename)
    else:  
        print("Could not find %s file." % filename)
except:
    pass
#moving the wfscom from suite location to its appstudio path location
try:
    if os.path.isfile(suiteDir+'/'+filename):
        shutil.move(suiteDir+'/'+filename, wfscom_path)
    else:
        print("Pass")
except:
    pass    
#aspath='D:/'+confid+'/ibi/AppStudio82/bin/Focshell.exe'
aspath='D:/'+confid+'/ibi/AppStudio82/bin/AppStudio.exe'
f=open(suiteDir + '/reports/aspath','w')
f.write('')
f.write(aspath)
f.close()
time.sleep(30)
os.system('start /min c:/Winium.Desktop.Driver.exe')
time.sleep(60)
if os.path.isfile(aspath):
    driver = webdriver.Remote(
    command_executor='http://localhost:9999',
    desired_capabilities={'debugConnectToRunningApp': 'false',
        'app': aspath
    })
    time.sleep(90)
    try:
        if driver.find_element_by_name('Cancel').is_displayed():
            driver.find_element_by_name('Cancel').click()
    except:pass
    time.sleep(15)
    help_dialog_object=driver.find_element_by_class_name('#32770')
    if help_dialog_object.find_element_by_name('Close').is_displayed():
        help_dialog_object.find_element_by_name('Close').click()
    time.sleep(2)
#     AS_MainWindow=automation.WindowControl(Name='App Studio')
#     AS_MainWindow.SetFocus()
#     if automation.ExpandCollapseState.Expanded!=AS_MainWindow.TreeItemControl(Name=suite).CurrentExpandCollapseState():
#         AS_MainWindow.TreeItemControl(Name=suite).DoubleClick(waitTime=4)
#         time.sleep(4)
#     if automation.ExpandCollapseState.Expanded!=AS_MainWindow.TreeItemControl(Name='Domains').CurrentExpandCollapseState():
#         AS_MainWindow.TreeItemControl(Name='Domains').DoubleClick(waitTime=4)
#         time.sleep(4)
else:
    print(aspath)
    exit()

client = tr.APIClient('http://lnxtestrail.ibi.com/testrail/')
client.user = 'bigscm@ibi.com'
client.password = 'Li47OFB.CFpL1diBiImX-iDa9PymKNq7v47dAz4nR'

rel = {'8105m': '2', '8106': '3', 'head': '4', '8200': '5', 'headcont': '6', '8106cont': '7', '8200m': '8', '8201': '9', '8201cont': '10',
       '8201m': '11', '8202': '14', '82xx': '20', '8203': '21', '8204': '25', '82xx_cdr':'999', 'head_git':'998'}
conf = {'bue1':'55','bue2':'56','wf1':'57','wf2':'82','wf3':'65','as1':'58','507':'31','500':'28','wf4':'66','wf5':'67','623':'78','as8':'80', '660':'87', '799':'154'}
prod={'wf':'1','as':'2','wq':'3','wx':'4','wb':'5'}
R = {'ie': '2', 'cr': '29', 'ff': '27','eg':'28', 'ff_current':'37', 'ie_current':'38', 'cr_current':'39'}

suitename=re.sub(r'_.*','',suite)
suiteid=re.sub(r'S','',suitename)
confid=conf[confid]
product=prod[product]
browser=R[browser]
release=rel[release]
print(release)

#ruunig tests
os.chdir(suiteDir)

result=client.send_get('get_cases/'+project_id+'&suite_id='+suiteid)
for i in range(len(result)):
    if result[i]['custom_automation_status'] == 4:
        testid=str(result[i]['id'])
        test='C'+testid
        #print('test no '+test+" started to run")
        runtest='true'
        defects=''
        status=''
        
        try:
            cmd='get_results_for_case/'+runid+'/'+testid+'&limit=1'
            if client.send_get(cmd):
                output=client.send_get(cmd)
                if output[0]['defects']:
                    defects=output[0]['defects']
                    status='6' 
                    runtest='false' 
        except :
            #print (test+' testrun causing error')
            continue
        if runtest == 'true':
            for file in glob.glob("*.sikuli"):
                if file[:-7] == test:
                    resp=subprocess.call('C:/Sikuli/runsikulix.cmd -r '+test)
                    if resp != 0:
                        continue
                    for name in glob.glob(suiteDir+'/reports/*'+test+'*.xml'):
                        tree = ET.parse(name)
                        root = tree.getroot()
                        fail=root.attrib.get('failures')
                        err=root.attrib.get('errors')
                        if fail != '0' or err != '0':
                            status='5'
                        else:
                            status='1'
                        break
        cmd='add_result_for_case/'+runid+'/'+testid
        resp=''
        try:
            print("test= ", test, "status= ", status)
            resp=client.send_post(cmd,{'status_id':status,'custom_pkgname':pkgname,'custom_browsers':browser,
                'custom_configurations':confid,'custom_run_mode':testtool,'custom_release':release,
                'custom_prodid':product,'custom_atm_issues':1,'defects':defects})
            print(resp)
        except:
            continue
            #print(sys.exc_info())
os.system("taskkill /f /im  Winium.Desktop.Driver.exe")