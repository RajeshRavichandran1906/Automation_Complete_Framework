import os

class Log:
    
    __logs = ""
    
    def Message(self, msg):
        
        tag = '<div class="well text-primary"><b>{0}</b></div>'.format(msg)
        Log.__logs += tag
        
    def Verification(self, msg):
        
        tag = '<b><div class="text-success">{0}</div></b><br>'.format(msg)
        Log.__logs += tag
        
    def VerificationFailure(self, msg):
        
        tag = '<b><div class="text-danger">{0}</div></b><br>'.format(msg)
        Log.__logs += tag
        
    def IBIRSResponse(self, response, IBIRS_action):

        url = "<tr><td>API Url</td><td>{}</td></tr>".format(response.url)
        method = "<tr><td>Method</td><td>{}</td></tr>".format(response.request.method)
        action = "<tr><td>IBIRS Action</td><td>{}</td></tr>".format(IBIRS_action)
        textarea = "<div class='text-info'><b>Response Content : </b></div><br><textarea class = 'form-control' style='width:100%; height:150px; font-size:14px;' readonly value={}></textarea><br><br>".format(response.text)
        tags = "<table class='table table-bordered'>" + url + method + action + "</table>" + textarea
        Log.__logs += tags
        
    def _write_(self, case_id):
        file_dir = os.path.join(os.getcwd(), case_id)
        if os.path.exists(file_dir) != True:
            os.mkdir(case_id)
        file_path = os.path.join(file_dir, "index.html")
        css_link = '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">'
        base_html = "<html><head>" + css_link + "<title>{} Test Run Log</title><head><body>".format(case_id)
        footer_html = "</body></html>"
        full_html = base_html + Log.__logs + footer_html
        with open(file_path, 'w') as file:
            file.write(full_html)