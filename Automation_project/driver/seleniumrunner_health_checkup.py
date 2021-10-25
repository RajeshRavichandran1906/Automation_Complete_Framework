import requests
import time
import xml.etree.ElementTree as ET
from requests.exceptions import ConnectionError

class Health_Check(object):
    rspath="/rs/ibfs"
    returncode='10000'
    user_id = 'admin'
    user_pass = 'admin'
    sleepTime=60
    
    def __init__(self, host_name, port_number):
        self.setup_url = 'http://'+host_name+':'+port_number+'/ibi_apps'
    
    def verify_returncode(self, test_name, url, params):
        r = requests.get(url = url, params = params) 
        xmlFile=str(r.text)
        root = ET.fromstring(xmlFile)
        key=root.attrib
        if 'returncode' in key and 'returndesc' in key:
            if key["returncode"] != Health_Check.returncode :
                userMessage=" Signon request status : returncode = {0} and returndesc = {1}".format(key["returncode"], key["returndesc"]) 
                e=ConnectionError(userMessage)
                raise(e)  
            else:
                print(" {0} : returncode = {1} , returndesc = {2}".format(test_name, key["returncode"], key["returndesc"]))
        return(r)
        
    
    def test_sign_on(self):
        url = self.setup_url + Health_Check.rspath
        params= {'IBIRS_action':'signOn','IBIRS_userName':Health_Check.user_id,'IBIRS_password':Health_Check.user_pass}
        test_name='Signon request status'
        r = requests.get(url = url, params = params)
        self.verify_returncode(test_name, url, params)  
        
    def test_ia_report_creation(self):
        url = self.setup_url + Health_Check.rspath
        create_report_url='ibfs/WFC/Repository/Public/report.fex?IBIRS_action=put&IBIRS_object=<rootObject _jt="IBFSMRObject" description="IAreportdefault" extension="fex" type="FexFile"> <properties size="1"> <entry key="tool" value="infoAssist,report,IAFull" /> </properties> <content _jt="IBFSByteContent" charset="Cp1252">LSpEbyBub3QgZGVsZXRlIG9yIG1vZGlmeSB0aGUgY29tbWVudHMgYmVsb3cKKi1JTlRFUk5BTF9DT01NRU5UIExJTkUjMCRQRDk0Yld3Z2RtVnljMmx2YmowaU1TNHdJaUJsYm1OdlpHbHVaejBpVlZSR0xUZ2lJSE4wWVc1a1lXeHZibVU5SW01dklqOCtEUW84SVMwdE1TNHdMUzArRFFvOFVtOXZkQ0IyWlhKemFXOXVQU0l4TGpBaVBnMEtJQ0FnSUR4UFltcGxZM1FnYjJKcVpXTjBTV1E5SWxSaFlteGxYekVpUGcwS0lDQWdJQ0FnSUNBOFVISnZjR1Z5ZEhrZ2JtRnRaVDBpVEdsdWEyVmtVMjl5ZEhNaUlIUjVjR1U5SW1waGRtRXViR0Z1Wnk1VGRISnBibWNpTHo0TkNpQWdJQ0E4TDA5aWFtVmpkRDROQ2lBZ0lDQThUMkpxWldOMElHOWlhbVZqZEVsa1BTSkhURTlDUVV3aVBnMEtJQ0FnSUNBZ0lDQThVSEp2Y0dWeWRIa2dibUZ0WlQwaVUyRnRjR3hsUkdGMFlTSWdkSGx3WlQwaWFtRjJZUzVzWVc1bkxrSnZiMnhsWVc0aVBtWmhiSE5sUEM5UWNtOXdaWEowZVQ0TkNpQWdJQ0FnSUNBZ1BGQnliM0JsY25SNUlHNWhiV1U5SWtkc2IySmhiRkpsWTI5eVpFeHBiV2wwSWlCMGVYQmxQU0pxWVhaaExteGhibWN1VTNSeWFXNW5JajQxTURBOEwxQnliM0JsY25SNVBnMEtJQ0FnSUNBZ0lDQThVSEp2Y0dWeWRIa2dibUZ0WlQwaVIyeHZZbUZzVW5WdVVtVmpiM0prVEdsdGFYUWlJSFI1Y0dVOUltcGhkbUV1YkdGdVp5NVRkSEpwYm1jaVBqQThMMUJ5YjNCbGNuUjVQZzBLSUNBZ0lDQWdJQ0E4VUhKdmNHVnlkSGtnYm1GdFpUMGlabWxsYkdSRWFYTndiR0Y1VFc5a1pTSWdkSGx3WlQwaWFtRjJZUzVzWVc1bkxsTjBjbWx1WnlJK2JHRmlaV3c4TDFCeWIzQmxjblI1UGcwS0lDQWdJQ0FnSUNBOFVISnZjR1Z5ZEhrZ2JtRnRaVDBpY0hKbFptbDRSR2x6Y0d4aGVVMXZaR1VpSUhSNWNHVTlJbXBoZG1FdWJHRnVaeTVUZEhKcGJtY2lMejROQ2lBZ0lDQWdJQ0FnUEZCeWIzQmxjblI1SUc1aGJXVTlJa0ZqZEdsMlpWOVRkSGxzWlY5VmMyVnlYM1I1Y0dVaUlIUjVjR1U5SW1waGRtRXViR0Z1Wnk1VGRISnBibWNpUG5CdmQyVnlQQzlRY205d1pYSjBlVDROQ2lBZ0lDQWdJQ0FnUEZCeWIzQmxjblI1SUc1aGJXVTlJa3hwYm10bFpGTnZjblJ6SWlCMGVYQmxQU0pxWVhaaExteGhibWN1VTNSeWFXNW5JajV1YjNRZ2FXNXBkR2xoYkdsNlpXUThMMUJ5YjNCbGNuUjVQZzBLSUNBZ0lDQWdJQ0E4VUhKdmNHVnlkSGtnYm1GdFpUMGlSMnh2WW1Gc1ZtRnNkV1Z6VUdGbmFXNW5JaUIwZVhCbFBTSnFZWFpoTG14aGJtY3VVM1J5YVc1bklqNDBQQzlRY205d1pYSjBlVDROQ2lBZ0lDQWdJQ0FnUEZCeWIzQmxjblI1SUc1aGJXVTlJa1p2WTJWNFpXTlFjbVZtWlhKbGJtTmxjeUlnZEhsd1pUMGlUV0Z3SWo0TkNpQWdJQ0FnSUNBZ0lDQWdJRHhGYm5SeWVTQnJaWGs5SW1ScGMzQnNZWGxGWkdsMFRXOWtaVWx1Wm05TmFXNXBVSEpsWm1WeVpXNWpaU0lnZEhsd1pUMGlhbUYyWVM1c1lXNW5MbE4wY21sdVp5SStabUZzYzJVOEwwVnVkSEo1UGcwS0lDQWdJQ0FnSUNBZ0lDQWdQRVZ1ZEhKNUlHdGxlVDBpWkdsemNHeGhlVVp2Y20xaGRGUmhZa2x1Wm05TmFXNXBVSEpsWm1WeVpXNWpaU0lnZEhsd1pUMGlhbUYyWVM1c1lXNW5MbE4wY21sdVp5SStkSEoxWlR3dlJXNTBjbmsrRFFvZ0lDQWdJQ0FnSUNBZ0lDQThSVzUwY25rZ2EyVjVQU0prYVhOd2JHRjVTRzl0WlZSaFlrbHVabTlOYVc1cFVISmxabVZ5Wlc1alpTSWdkSGx3WlQwaWFtRjJZUzVzWVc1bkxsTjBjbWx1WnlJK1ptRnNjMlU4TDBWdWRISjVQZzBLSUNBZ0lDQWdJQ0FnSUNBZ1BFVnVkSEo1SUd0bGVUMGlaR2x6Y0d4aGVWRjFhV05yUVdOalpYTnpWRzl2YkdKaGNsTmhkbVZKYm1adlRXbHVhVkJ5WldabGNtVnVZMlVpSUhSNWNHVTlJbXBoZG1FdWJHRnVaeTVUZEhKcGJtY2lQblJ5ZFdVOEwwVnVkSEo1UGcwS0lDQWdJQ0FnSUNBZ0lDQWdQRVZ1ZEhKNUlHdGxlVDBpYldWMFlXUmhkR0ZmZG1sbGQzTWlJSFI1Y0dVOUltcGhkbUV1YkdGdVp5NVRkSEpwYm1jaVBrMWxkR0ZFWVhSaFZISmxaUzVXU1VWWFgwUkpUVk04TDBWdWRISjVQZzBLSUNBZ0lDQWdJQ0FnSUNBZ1BFVnVkSEo1SUd0bGVUMGlaR2x6Y0d4aGVWSmxjMjkxY21ObGMwWnBaV3hrVkdGaVNXNW1iMDFwYm1sUWNtVm1aWEpsYm1ObElpQjBlWEJsUFNKcVlYWmhMbXhoYm1jdVUzUnlhVzVuSWo1bVlXeHpaVHd2Ulc1MGNuaytEUW9nSUNBZ0lDQWdJQ0FnSUNBOFJXNTBjbmtnYTJWNVBTSmthWE53YkdGNVNXNXpaWEowVkdGaVNXNW1iMDFwYm1sUWNtVm1aWEpsYm1ObElpQjBlWEJsUFNKcVlYWmhMbXhoYm1jdVUzUnlhVzVuSWo1bVlXeHpaVHd2Ulc1MGNuaytEUW9nSUNBZ0lDQWdJQ0FnSUNBOFJXNTBjbmtnYTJWNVBTSmthWE53YkdGNVUyeHBZMlZ5YzFSaFlrVmthWFJKYm1adlRXbHVhVkJ5WldabGNtVnVZMlVpSUhSNWNHVTlJbXBoZG1FdWJHRnVaeTVUZEhKcGJtY2lQbVpoYkhObFBDOUZiblJ5ZVQ0TkNpQWdJQ0FnSUNBZ0lDQWdJRHhGYm5SeWVTQnJaWGs5SW1ScGMzQnNZWGxUWlhKcFpYTlVZV0pKYm1adlRXbHVhVkJ5WldabGNtVnVZMlVpSUhSNWNHVTlJbXBoZG1FdWJHRnVaeTVUZEhKcGJtY2lQbVpoYkhObFBDOUZiblJ5ZVQ0TkNpQWdJQ0FnSUNBZ0lDQWdJRHhGYm5SeWVTQnJaWGs5SW1sdVptOUJjM05wYzNSTmIyUmxRV3hzYjNkbFpFbHVabTlOYVc1cFVISmxabVZ5Wlc1alpTSWdkSGx3WlQwaWFtRjJZUzVzWVc1bkxsTjBjbWx1WnlJK1ptRnNjMlU4TDBWdWRISjVQZzBLSUNBZ0lDQWdJQ0FnSUNBZ1BFVnVkSEo1SUd0bGVUMGlaR1ZtWVhWc2RGOXdjbVYyYVdWM1gzQmhaMlZzYVcxcGRGOXNZWGx2ZFhRaUlIUjVjR1U5SW1waGRtRXViR0Z1Wnk1VGRISnBibWNpUGpFOEwwVnVkSEo1UGcwS0lDQWdJQ0FnSUNBZ0lDQWdQRVZ1ZEhKNUlHdGxlVDBpWlhoalpXeGZabTl5YldGMFgzWnBjMmxpYkdVaUlIUjVjR1U5SW1waGRtRXViR0Z1Wnk1VGRISnBibWNpUG5SeWRXVThMMFZ1ZEhKNVBnMEtJQ0FnSUNBZ0lDQWdJQ0FnUEVWdWRISjVJR3RsZVQwaVpHVm1ZWFZzZEY5d2NtVjJhV1YzWDNCaFoyVnNhVzFwZENJZ2RIbHdaVDBpYW1GMllTNXNZVzVuTGxOMGNtbHVaeUkrTlR3dlJXNTBjbmsrRFFvZ0lDQWdJQ0FnSUNBZ0lDQThSVzUwY25rZ2EyVjVQU0prWldaaGRXeDBYMk52YlhCdmMyVmZabTl5YldGMElpQjBlWEJsUFNKcVlYWmhMbXhoYm1jdVUzUnlhVzVuSWo1UVJFWThMMFZ1ZEhKNVBnMEtJQ0FnSUNBZ0lDQWdJQ0FnUEVWdWRISjVJR3RsZVQwaVpHbHpjR3hoZVVsdWRHVnlZV04wYVhabFRXOWtaVWx1Wm05TmFXNXBVSEpsWm1WeVpXNWpaU0lnZEhsd1pUMGlhbUYyWVM1c1lXNW5MbE4wY21sdVp5SStkSEoxWlR3dlJXNTBjbmsrRFFvZ0lDQWdJQ0FnSUNBZ0lDQThSVzUwY25rZ2EyVjVQU0p5ZFc1UGJsTjBZWEowZFhCSmJtWnZUV2x1YVZCeVpXWmxjbVZ1WTJVaUlIUjVjR1U5SW1waGRtRXViR0Z1Wnk1VGRISnBibWNpUG5SeWRXVThMMFZ1ZEhKNVBnMEtJQ0FnSUNBZ0lDQWdJQ0FnUEVWdWRISjVJR3RsZVQwaVpHbHpjR3hoZVVSaGRHRlVZV0pKYm1adlRXbHVhVkJ5WldabGNtVnVZMlVpSUhSNWNHVTlJbXBoZG1FdWJHRnVaeTVUZEhKcGJtY2lQbVpoYkhObFBDOUZiblJ5ZVQ0TkNpQWdJQ0FnSUNBZ0lDQWdJRHhGYm5SeWVTQnJaWGs5SW1Wa2FYUnZjbFI1Y0dWZmRtbHphV0pzWlNJZ2RIbHdaVDBpYW1GMllTNXNZVzVuTGxOMGNtbHVaeUkrZEhKMVpUd3ZSVzUwY25rK0RRb2dJQ0FnSUNBZ0lDQWdJQ0E4Ulc1MGNua2dhMlY1UFNKMGFHVnRaWE5mWTI5dWRISnZiRjkyYVhOcFlteGxJaUIwZVhCbFBTSnFZWFpoTG14aGJtY3VVM1J5YVc1bklqNTBjblZsUEM5RmJuUnllVDROQ2lBZ0lDQWdJQ0FnSUNBZ0lEeEZiblJ5ZVNCclpYazlJbVJwYzNCc1lYbFRiR2xqWlhKelZHRmlTVzUwWlhKaFkzUnBkbVZKYm1adlRXbHVhVkJ5WldabGNtVnVZMlVpSUhSNWNHVTlJbXBoZG1FdWJHRnVaeTVUZEhKcGJtY2lQblJ5ZFdVOEwwVnVkSEo1UGcwS0lDQWdJQ0FnSUNBZ0lDQWdQRVZ1ZEhKNUlHdGxlVDBpWkdsemNHeGhlVXhoZVc5MWRGUmgKKi1JTlRFUk5BTF9DT01NRU5UIExJTkUjMSRZa2x1Wm05TmFXNXBVSEpsWm1WeVpXNWpaU0lnZEhsd1pUMGlhbUYyWVM1c1lXNW5MbE4wY21sdVp5SStabUZzYzJVOEwwVnVkSEo1UGcwS0lDQWdJQ0FnSUNBOEwxQnliM0JsY25SNVBnMEtJQ0FnSUNBZ0lDQThVSEp2Y0dWeWRIa2dibUZ0WlQwaVkyRnpZMkZrWlU1aGJXVnpJaUIwZVhCbFBTSk5ZWEFpTHo0TkNpQWdJQ0FnSUNBZ1BGQnliM0JsY25SNUlHNWhiV1U5SWsxaGMzUmxjbDlHYVd4bGN5SWdkSGx3WlQwaVUyVjBJajROQ2lBZ0lDQWdJQ0FnSUNBZ0lEeEZiblJ5ZVNCMGVYQmxQU0pxWVhaaExteGhibWN1VTNSeWFXNW5JajVEUVZJOEwwVnVkSEo1UGcwS0lDQWdJQ0FnSUNBOEwxQnliM0JsY25SNVBnMEtJQ0FnSUNBZ0lDQThVSEp2Y0dWeWRIa2dibUZ0WlQwaWJXVjBZV1JoZEdGV2FXVjNRWE1pSUhSNWNHVTlJazFoY0NJK0RRb2dJQ0FnSUNBZ0lDQWdJQ0E4Ulc1MGNua2dhMlY1UFNKRFFWSWlJSFI1Y0dVOUltcGhkbUV1YkdGdVp5NVRkSEpwYm1jaVBrMWxkR0ZFWVhSaFZISmxaUzVXU1VWWFgwUkpUVk04TDBWdWRISjVQZzBLSUNBZ0lDQWdJQ0E4TDFCeWIzQmxjblI1UGcwS0lDQWdJQ0FnSUNBOFVISnZjR1Z5ZEhrZ2JtRnRaVDBpWlc1aFlteGxVSEpsZG1sbGR5SWdkSGx3WlQwaWFtRjJZUzVzWVc1bkxrSnZiMnhsWVc0aVBuUnlkV1U4TDFCeWIzQmxjblI1UGcwS0lDQWdJRHd2VDJKcVpXTjBQZzBLUEM5U2IyOTBQZzBLCi0qRG8gbm90IGRlbGV0ZSBvciBtb2RpZnkgdGhlIGNvbW1lbnRzIGFib3ZlCkVOR0lORSBJTlQgQ0FDSEUgU0VUIE9OCgoKLURFRkFVTFRIICZXRl9TVU1NQVJZPSdTdW1tYXJ5JzsKLURFRkFVTFRIICZXRl9USVRMRT0nV2ViRk9DVVMgUmVwb3J0JzsKVEFCTEUgRklMRSBDQVIKU1VNIENBUi5CT0RZLkRFQUxFUl9DT1NUCkNBUi5CT0RZLlJFVEFJTF9DT1NUCkJZIENBUi5DT01QLkNBUgpPTiBUQUJMRSBQQ0hPTEQgRk9STUFUIEhUTUwKT04gVEFCTEUgTk9UT1RBTApPTiBUQUJMRSBTRVQgUEFHRS1OVU0gTk9MRUFECk9OIFRBQkxFIFNFVCBTUVVFRVpFIE9OCk9OIFRBQkxFIFNFVCBFTVBUWVJFUE9SVCBPTgpPTiBUQUJMRSBTRVQgSFRNTENTUyBPTgpPTiBUQUJMRSBTRVQgSFRNTEVOQ09ERSBPTgpPTiBUQUJMRSBTRVQgQ0FDSEVMSU5FUyAxMDAKT04gVEFCTEUgU0VUIFNUWUxFICoKSU5DTFVERT1JQkZTOi9GSUxFL0lCSV9IVE1MX0RJUi9qYXZhYXNzaXN0L2ludGwvRU4vRU5JQURlZmF1bHRfY29tYmluZS5zdHksJApUWVBFPVJFUE9SVCwgVElUTEVURVhUPSZXRl9USVRMRS5RVU9URURTVFJJTkcsIFNVTU1BUlk9JldGX1NVTU1BUlkuUVVPVEVEU1RSSU5HLCAkCkVORFNUWUxFCkVORAoKLVJVTgo=</content> </rootObject>'
        ia_report_creation_url=url+''
        
    def test_ia_report_run(self):
        ia_report_run=''
        
    def test_sign_off(self):
        sign_on_url=''
        
    def check_wf_client_exception(self):        
        no_reponse_yet=True   
        loop=5   
        count=0
        while no_reponse_yet and count < loop:             
            try:
                r=requests.get(url = self.setup_url) 
                no_reponse_yet=False
                status_code=r.status_code
                break
            except:
                time.sleep(Health_Check.sleepTime)
                count=count+1
                print("Iteration {0} Waiting for WF to come up!".format(count))

        if no_reponse_yet == True:
            msg="End WF wait:{0} sleep iterations completed:{1} \nWarning: No connection could be made to {2}. WF failed to return".format(count,loop,self.setup_url)
            raise ConnectionError(msg)
        return(status_code)
    
    def validate_setup(self):
        status_code=self.check_wf_client_exception()
        if status_code:
            self.test_sign_on()

if __name__ == '__main__':
    check_obj=Health_Check('unxrh7', '202641')
    check_obj.validate_setup()