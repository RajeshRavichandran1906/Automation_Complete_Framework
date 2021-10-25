import sys, re, os
from testrail import testrail as tr
import xml.etree.ElementTree as ET
from configparser import ConfigParser
   
runid=sys.argv[1]
if bool(re.match('C\d+','C2292420')):
    testid=sys.argv[2].lstrip('C') 
else:
    sys.exit()
res_xml_file=sys.argv[3]
pkgname=sys.argv[4]
browser=sys.argv[5]
release=sys.argv[6]
if release.startswith('branch'):
    release=release.lstrip('branch')
confid=sys.argv[7]
product=sys.argv[8]
testtool=3


def getFieldsDictionary( fields_str ) :
    theDictionary = {}
    for item in fields_str.split('\n'):
            pair = item.split(',')
            if len(pair) > 1:
                if bool(re.match('.*:.*', pair[1])):
                    reobj=re.match('(.*):.*', pair[1])
                    theDictionary.update({reobj.group(1): pair[0].strip()})
                else:
                    theDictionary.update({re.sub(' ','', pair[1]): pair[0].strip()})
    return theDictionary
current_file_path=os.path.abspath(os.path.dirname(__file__))
conf_file=os.path.join(current_file_path,'config.ini')
conf_pair = {}
parser = ConfigParser()
parser.read(conf_file)

section='testrail'
client = tr.APIClient(parser[section]['tr_link'])
client.user = parser[section]['tr_uid']
client.password = parser[section]['tr_pwd']
 
tree = ET.parse(res_xml_file)
root = tree.getroot()
test_summaries=[x.attrib for x in root.iter('Summary')]
status=5 if test_summaries[-1]['failed'] != '0' or test_summaries[-1]['warnings'] != '0' else 1


section='browser'
browser=browser+parser[section][browser]

# if result_fields[i]['name'] == 'release':
#         release_key = getFieldsDictionary(result_fields[i]['configs'][0]['options']['items']).get(release)

result_fields=client.send_get('get_result_fields')
for i in range(len(result_fields)):
    if result_fields[i]['name'] == 'release':
        release_key = getFieldsDictionary(result_fields[i]['configs'][0]['options']['items']).get(release.lower())
        if release_key == None:
            release_key = getFieldsDictionary(result_fields[i]['configs'][0]['options']['items']).get(release.upper())
    if result_fields[i]['name'] == 'prodid':  
        product_key = getFieldsDictionary(result_fields[i]['configs'][0]['options']['items']).get(product)
    if result_fields[i]['name'] == 'configurations':
        configuration_key = getFieldsDictionary(result_fields[i]['configs'][0]['options']['items']).get(confid)
    if result_fields[i]['name'] == 'browsers':
        browser_key = getFieldsDictionary(result_fields[i]['configs'][0]['options']['items']).get(browser)

if release_key is None:
    raise KeyError('The requested release ' + release + ' is not currently a valid release choice in TestRail.')
if product_key is None:
    raise KeyError('The requested product ' + product + ' is not currently a valid product choice in TestRail.')
if configuration_key is None:
    raise KeyError('The requested configuration ' + confid + ' is not currently a valid configuration choice in TestRail.')
if browser_key is None:
    raise KeyError('The requested browser [' + browser + '] is not currently a valid browser choice in TestRail.')

cmd='add_result_for_case/'+runid+'/'+testid

resp=''
try:
    resp=client.send_post(cmd,{ 'status_id':status,'custom_pkgname':pkgname,'custom_browsers':browser_key,
        'custom_configurations':configuration_key,'custom_run_mode':testtool,'custom_release':release_key,
        'custom_prodid':product_key,'custom_atm_issues':1})
except:
    print("Unable to Update Result to Test Rail.")