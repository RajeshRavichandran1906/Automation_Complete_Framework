from locust import HttpLocust, TaskSequence, seq_task
import random
import xml.etree.ElementTree as ET
import json
import re
import time

class designer_chart(TaskSequence):
    BAD_RESPONSE_CODE_MSG = "Unexpected response code: "
    BAD_CSRF_TOKEN_MSG = "CSRF token is null."
    BAD_MIDDLE_TIER_MSG = "Middle tier call contains error."
    BAD_CONTENT_MSG = "Request to content.vxl fails"
    BAD_RUNTIME_MSG = "Runtime output is not correct."

    CONTENT_URL = "/content.vxl"
    csrf_token = ""
    fdm_id = ""
    component_id = ""
    pagelayout_id = ""
    #tasks_executed = 0

    BAD_CSRF_TOKEN_REGEX = re.compile(".*CSRFTokenValue=\"null\".*")
    GOOD_MIDDLE_TIER_REGEX = re.compile(".*\"hasError\":false.*")
    GOOD_CONTENT_REGEX = re.compile(".*<status status=\"SUCCESS\" hasstatus=\"true\" ><warnings></warnings>.*")
    GOOD_RUNTIME_REGEX = re.compile(".*NUMBER OF RECORDS IN GRAPH=        7  PLOT POINTS=      7.*")

    @staticmethod
    def failure_capture_signon(call, response):
        with open("failure_signon.log", "a", encoding="utf-8") as f:
            f.write("******************" + call + "*******************\n")
            f.write(response.text)
            f.write("\n\n\n")

    @staticmethod
    def failure_capture(call, response, user):
        with open("failure_" + user + ".log", "a", encoding="utf-8") as f:
            f.write("******************" + call + "*******************\n")
            f.write(response.text)
            f.write("\n\n\n")

    def signon(self):
        random_wait = random.randint(0, 5)
        time.sleep(random_wait)
        signon_url = "/service/wf_security_check.jsp"
        with self.client.post(signon_url, 
                                {"IBIB_userid":"admin", 
                                 "type":"json", 
                                 "IBIB_password":"admin", 
                                 "IBIB_force_signon":"false",
                                 "webfocus-security-direct-response":"true",
                                 "IBIWF_rememberme":"false",
                                 "random":str(random.random())
                                }, 
                                catch_response=True) as response:
            response.locust_request_meta["name"] = "URL1: Signon"
            if response.status_code == 200 and self.BAD_CSRF_TOKEN_REGEX.search(response.text) is None:
                response.success()
                root = ET.fromstring(response.text)
                self.csrf_token = root[0].attrib.get("CSRFTokenValue")
            else:
                designer_chart.failure_capture_signon("URL1: Signon", response)
                response.failure("URL1: Signon request failed...") 

    def launch_designer_chart(self):
        launch_designer_chart_url = "/designer?&master=wfretail82/wf_retail&item=IBFS:/WFC/Repository/P329_S31911&tool=chart"
        with self.client.get(launch_designer_chart_url, catch_response=True) as response:
            response.locust_request_meta["name"] = "URL2: LaunchDesigner"
            if response.status_code == 200: #TODO add check for redirect to signon page
                response.success()      
            else:
                designer_chart.failure_capture("URL2: LaunchDesigner", response, self.csrf_token)
                response.failure("URL2: LaunchDesigner request failed...")

    def start_ia(self):            
        fdm_session_url = "/ia?item=IBFS:/WFC/Repository/P329_S31911&tool=chart&startUpViewName=insight/json&is508=false&master=wfretail82/wf_retail&insightDesigner=true"
        with self.client.get(fdm_session_url, catch_response=True) as response:
            response.locust_request_meta["name"] = "URL3: StartIA"
            if response.status_code == 200 and self.GOOD_MIDDLE_TIER_REGEX.search(response.text) is not None:
                response.success()
                response_dict = json.loads(response.text)
                self.fdm_id = response_dict["fdmId"]
                self.component_id = response_dict["componentId"]
                self.pagelayout_id = response_dict["pageLayoutId"]
            else:
                designer_chart.failure_capture("URL3: StartIA", response, self.csrf_token)
                response.failure("URL3: StartIA request fail...")     

    def choose_treemap(self):
        with self.client.post(self.CONTENT_URL,
                                    {"IBIWF_SES_AUTH_TOKEN":self.csrf_token,
                                     "dmSessionId":self.fdm_id,
                                     "configurationId":"xMultiConfigurations",
                                     "configurationIds":"xChartTypeUpdate;xQueryTrees;xPropertyInfoQuery",
                                     "id":"Treemap",
                                     "bucketAction":"show",
                                     "propertyListId_infoQuery":"bucket_component_update,tool_bar_state",
                                     "eventDescription":"ibx_change_chart_type_action",
                                     "componentId":self.component_id, 
                                     "pageLayoutId":self.pagelayout_id 
                                    }, 
                                    catch_response=True) as response:
            response.locust_request_meta["name"] = "URL4: Choose-TreeMap"
            if response.status_code == 200 and self.GOOD_CONTENT_REGEX.search(response.text) is not None: 
                response.success()      
            else:
                designer_chart.failure_capture("URL4: Choose-TreeMap", response, self.csrf_token)
                response.failure("URL4: Choose-TreeMap request failed...")

    def choose_treemap_draw_canvas(self):    
        with self.client.post(self.CONTENT_URL,
                                    {"IBIWF_SES_AUTH_TOKEN":self.csrf_token,
                                     "dmSessionId":self.fdm_id,
                                     "configurationId":"xMultiConfigurations",
                                     "configurationIds":"xComponentPreview",
                                     "action":"html",
                                     "componentId":self.component_id, 
                                     "pageLayoutId":self.pagelayout_id  
                                    },
                                    catch_response=True) as response:
            response.locust_request_meta["name"] = "URL5: DrawCanvas1"
            if response.status_code == 200 and self.GOOD_CONTENT_REGEX.search(response.text) is not None:
                response.success()
            else:
                designer_chart.failure_capture("URL5: DrawCanvas1", response, self.csrf_token)
                response.failure("URL5: DrawCanvas1 request failed...")

    def add_product_category_to_group_bucket(self):
        with self.client.post(self.CONTENT_URL,
                                    {"IBIWF_SES_AUTH_TOKEN":self.csrf_token,
                                     "dmSessionId":self.fdm_id,
                                     "configurationId":"xMultiConfigurations",
                                     "configurationIds":"xQueryTrees;xPropertyInfoQuery;xWhereQueryXml",
                                     "bucketAction":"add",
                                     "index":"-1",
                                     "dropTargetId":"WF_RETAIL.WF_RETAIL_PRODUCT.PRODUCT_CATEGORY",
                                     "targetId":"ddt_by",
                                     "initialTargetId":"",
                                     "prefix":"",
                                     "propertyListId_infoQuery":"bucket_component_update,tool_bar_state",
                                     "eventDescription":"ibx_add_field_action",
                                     "componentId":self.component_id, 
                                     "pageLayoutId":self.pagelayout_id  
                                    },
                                    catch_response=True) as response: 
            response.locust_request_meta["name"] = "URL6: Drop-Category"
            if response.status_code == 200 and self.GOOD_CONTENT_REGEX.search(response.text) is not None: 
                response.success()      
            else:
                designer_chart.failure_capture("URL6: Drop-Category", response, self.csrf_token)
                response.failure("URL6: Drop-Category request 1 failed...")    

    def add_product_category_to_group_bucket_draw_canvas(self):
        with self.client.post(self.CONTENT_URL,
                                    {"IBIWF_SES_AUTH_TOKEN":self.csrf_token,
                                     "dmSessionId":self.fdm_id,
                                     "configurationId":"xMultiConfigurations",
                                     "configurationIds":"xComponentPreview",
                                     "action":"html",
                                     "componentId":self.component_id, 
                                     "pageLayoutId":self.pagelayout_id  
                                    },
                                    catch_response=True) as response:
            response.locust_request_meta["name"] = "URL7: DrawCanvas2"
            if response.status_code == 200 and self.GOOD_CONTENT_REGEX.search(response.text) is not None:
                response.success()
            else:
                designer_chart.failure_capture("URL7: DrawCanvas2", response, self.csrf_token)
                response.failure("URL7: DrawCanvas2 request failed...")  

    def add_model_to_size_bucket(self):
        with self.client.post(self.CONTENT_URL,
                                    {"IBIWF_SES_AUTH_TOKEN":self.csrf_token,
                                     "dmSessionId":self.fdm_id,
                                     "configurationId":"xMultiConfigurations",
                                     "configurationIds":"xQueryTrees;xPropertyInfoQuery;xWhereQueryXml",
                                     "bucketAction":"add",
                                     "index":"-1",
                                     "dropTargetId":"WF_RETAIL.WF_RETAIL_PRODUCT.MODEL",
                                     "targetId":"ddt_verb",
                                     "initialTargetId":"",
                                     "prefix":"",
                                     "propertyListId_infoQuery":"bucket_component_update,tool_bar_state",
                                     "eventDescription":"ibx_add_field_action",
                                     "componentId":self.component_id, 
                                     "pageLayoutId":self.pagelayout_id 
                                    }, 
                                    catch_response=True) as response:
            response.locust_request_meta["name"] = "URL8: Drop-Model"
            if response.status_code == 200 and self.GOOD_CONTENT_REGEX.search(response.text) is not None: 
                response.success()      
            else:
                designer_chart.failure_capture("URL8: Drop-Model", response, self.csrf_token)
                response.failure("URL8: Drop-Model request failed...")    

    def add_model_to_size_bucket_draw_canvas(self):
        with self.client.post(self.CONTENT_URL,
                                    {"IBIWF_SES_AUTH_TOKEN":self.csrf_token,
                                     "dmSessionId":self.fdm_id,
                                     "configurationId":"xMultiConfigurations",
                                     "configurationIds":"xComponentPreview",
                                     "action":"html",
                                     "componentId":self.component_id, 
                                     "pageLayoutId":self.pagelayout_id  
                                    },
                                    catch_response=True) as response:
            response.locust_request_meta["name"] = "URL9: DrawCanvas3"
            if response.status_code == 200 and self.GOOD_CONTENT_REGEX.search(response.text) is not None:
                response.success()
            else:
                designer_chart.failure_capture("URL9: DrawCanvas3", response, self.csrf_token)
                response.failure("URL9: DrawCanvas3 request failed...")  

    def add_gross_profit_to_color_bucket(self):
        with self.client.post(self.CONTENT_URL,
                                    {"IBIWF_SES_AUTH_TOKEN":self.csrf_token,
                                     "dmSessionId":self.fdm_id,
                                     "configurationId":"xMultiConfigurations",
                                     "configurationIds":"xQueryTrees;xPropertyInfoQuery;xWhereQueryXml",
                                     "bucketAction":"add",
                                     "index":"0",
                                     "dropTargetId":"WF_RETAIL.WF_RETAIL_SALES.GROSS_PROFIT_US",
                                     "targetId":"treemap_color_bucket",
                                     "initialTargetId":"",
                                     "prefix":"",
                                     "propertyListId_infoQuery":"bucket_component_update,tool_bar_state",
                                     "eventDescription":"ibx_add_field_action",
                                     "componentId":self.component_id, 
                                     "pageLayoutId":self.pagelayout_id  
                                    },
                                    catch_response=True) as response:
            response.locust_request_meta["name"] = "URL10: Drop-Profit"
            if response.status_code == 200 and self.GOOD_CONTENT_REGEX.search(response.text) is not None: 
                response.success()      
            else:
                designer_chart.failure_capture("URL10: Drop-Profit", response, self.csrf_token)
                response.failure("URL10: Drop-Profit request failed...")  

    def add_gross_profit_to_color_bucket_draw_canvas(self):
        with self.client.post(self.CONTENT_URL,
                                    {"IBIWF_SES_AUTH_TOKEN":self.csrf_token,
                                     "dmSessionId":self.fdm_id,
                                     "configurationId":"xMultiConfigurations",
                                     "configurationIds":"xComponentPreview",
                                     "action":"html",
                                     "componentId":self.component_id, 
                                     "pageLayoutId":self.pagelayout_id  
                                    },
                                    catch_response=True) as response:
            response.locust_request_meta["name"] = "URL11: DrawCanvas4"
            if response.status_code == 200 and self.GOOD_CONTENT_REGEX.search(response.text) is not None:
                response.success()
            else:
                designer_chart.failure_capture("URL11: DrawCanvas4", response, self.csrf_token)
                response.failure("URL11: DrawCanvas4 request failed...")   

    def click_preview_button_to_run(self):
        preview_run_url = "/content.vxl?configurationId=xRunUOAFex&componentId=" + self.component_id + "&dmSessionId=" + self.fdm_id + "&mayRedirNewWindow=false&IBIMR_random=24695"
        with self.client.get(preview_run_url, catch_response=True) as response:
            response.locust_request_meta["name"] = "URL12: RunPreview"
            if response.status_code == 200 and self.GOOD_RUNTIME_REGEX.search(response.text) is not None:
                response.success()
            else:
                designer_chart.failure_capture("URL12: RunPreview", response, self.csrf_token)
                response.failure("URL12: RunPreview request failed...")  

    def save_fex(self):
        with self.client.post(self.CONTENT_URL,
                                    {"IBIWF_SES_AUTH_TOKEN":self.csrf_token,
                                     "dmSessionId":self.fdm_id,
                                     "configurationId":"xMultiConfigurations",
                                     "configurationIds":"xBrowseAction;xPropertyInfoQuery",
                                     "type":"saveas",
                                     "ibfsPath":"IBFS:/WFC/Repository/P329_S31911/G784783/c9335800_" + self.csrf_token + ".fex",
                                     "ibfsDescription":"C9335800_" + self.csrf_token,
                                     "overwrite":"false",
                                     "propertyListId_infoQuery":"tool_bar_state",
                                     "eventDescription":"ibx_file_saveas_event",
                                     "componentId":self.component_id, 
                                     "pageLayoutId":self.pagelayout_id  
                                    },
                                    catch_response=True) as response:
            response.locust_request_meta["name"] = "URL13: SaveFex"
            if response.status_code == 200 and self.GOOD_CONTENT_REGEX.search(response.text) is not None: 
                response.success()      
            else:
                designer_chart.failure_capture("URL13: SaveFex", response, self.csrf_token)
                response.failure("URL13: SaveFex request failed...")  

    def quit_cd(self):
        with self.client.post(self.CONTENT_URL,
                                    {"IBIWF_SES_AUTH_TOKEN":self.csrf_token,
                                     "dmSessionId":self.fdm_id,
                                     "configurationId":"xMultiConfigurations",
                                     "configurationIds":"xComponentPreview",
                                     "action":"html",
                                     "componentId":self.component_id, 
                                     "pageLayoutId":self.pagelayout_id  
                                    },
                                    catch_response=True) as response:
            response.locust_request_meta["name"] = "URL14: QuitCD"
            if response.status_code == 200 and self.GOOD_CONTENT_REGEX.search(response.text) is not None:
                response.success()
            else:
                designer_chart.failure_capture("URL14: QuitCD", response, self.csrf_token)
                response.failure("URL14: QuitCD request failed...")  

    def run_fex(self):
        run_url = "/run.bip?BIP_REQUEST_TYPE=BIP_LAUNCH&BIP_folder=IBFS:/WFC/Repository/P329_S31911/G784783/&BIP_item=c9335800_" + self.csrf_token + ".fex"
        with self.client.get(run_url, catch_response=True) as response:
            response.locust_request_meta["name"] = "URL15: BipRun"
            if response.status_code == 200 and self.GOOD_RUNTIME_REGEX.search(response.text) is not None:
                response.success()
            else:
                designer_chart.failure_capture("URL15: BipRun", response, self.csrf_token)
                response.failure("URL15: BipRun request failed...")    

    def logout(self):
        logout_url = "/service/wf_security_logout.jsp" 
        with self.client.post(logout_url, catch_response=True) as response:
            response.locust_request_meta["name"] = "URL16: Logout"
            if response.status_code == 200:
                response.success()
            else:
                designer_chart.failure_capture("URL16: Logout", response, self.csrf_token)
                response.failure("URL16: Logout request failed...") 

    def on_start(self):
        self.tasks_executed = 0

    def on_stop(self):
        funcs = {"1":self.signon,
                "2":self.launch_designer_chart,
                "3":self.start_ia,
                "4":self.choose_treemap,
                "5":self.choose_treemap_draw_canvas,
                "6":self.add_product_category_to_group_bucket,
                "7":self.add_product_category_to_group_bucket_draw_canvas,
                "8":self.add_model_to_size_bucket,
                "9":self.add_model_to_size_bucket_draw_canvas,
                "10":self.add_gross_profit_to_color_bucket,
                "11":self.add_gross_profit_to_color_bucket_draw_canvas,
                "12":self.click_preview_button_to_run,
                "13":self.save_fex,
                "14":self.quit_cd,
                "15":self.run_fex,
                "16":self.logout
        }
        if self.tasks_executed > 0:
            for i in range(self.tasks_executed + 1, len(funcs) + 1):
                funcs[str(i)]()
                random_wait = 2.5 + 5 * random.random()
                time.sleep(random_wait)
                #print("*******************************" + str(i))
        print("@@@@@@@@@@@@admin_" + self.csrf_token)

    @seq_task(1)
    def signon_task(self):
        self.signon()
        self.tasks_executed = 1

    @seq_task(2)
    def launch_designer_chart_task(self):
        self.launch_designer_chart()
        self.tasks_executed += 1

    @seq_task(3)
    def start_ia_task(self):
        self.start_ia()
        self.tasks_executed += 1

    @seq_task(4)
    def choose_treemap_task(self):
        self.choose_treemap()
        self.tasks_executed += 1

    @seq_task(5)
    def choose_treemap_draw_canvas_task(self):
        self.choose_treemap_draw_canvas()
        self.tasks_executed += 1

    @seq_task(6)
    def add_product_category_to_group_bucket_task(self):
        self.add_product_category_to_group_bucket()
        self.tasks_executed += 1

    @seq_task(7)
    def add_product_category_to_group_bucket_draw_canvas_task(self):
        self.add_product_category_to_group_bucket_draw_canvas()
        self.tasks_executed += 1

    @seq_task(8)
    def add_model_to_size_bucket_task(self):
        self.add_model_to_size_bucket()
        self.tasks_executed += 1

    @seq_task(9)
    def add_model_to_size_bucket_draw_canvas_task(self):
        self.add_model_to_size_bucket_draw_canvas()
        self.tasks_executed += 1

    @seq_task(10)
    def add_gross_profit_to_color_bucket_task(self):
        self.add_gross_profit_to_color_bucket()
        self.tasks_executed += 1

    @seq_task(11)
    def add_gross_profit_to_color_bucket_draw_canvas_task(self):
        self.add_gross_profit_to_color_bucket_draw_canvas()
        self.tasks_executed += 1

    @seq_task(12)
    def click_preview_button_to_run_task(self):
        self.click_preview_button_to_run()
        self.tasks_executed += 1

    @seq_task(13)
    def save_fex_task(self):
        self.save_fex()
        self.tasks_executed += 1

    @seq_task(14)
    def quit_cd_task(self):
        self.quit_cd()
        self.tasks_executed += 1

    @seq_task(15)
    def run_fex_task(self):
        self.run_fex() 
        self.tasks_executed += 1       

    @seq_task(16)
    def logout_task(self):
        self.logout()    
        self.tasks_executed += 1           

class wf_user(HttpLocust):
    task_set = designer_chart
    host = "http://bipgprf1:25000/ibi_apps"
    #host = "http://bigscm14:8080/ibi_apps8"
    #host = "http://bigcontinst01.ibi.com:25030/ibi_apps"
    min_wait = 2500
    max_wait = 7500
