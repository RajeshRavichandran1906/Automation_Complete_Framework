#  A Python wrapper for WebFOCUS RESTful Web Services using
#  Requests: HTTP for Humans. See python-requests.org

#  Note: this software is for demonstration purposes only
#        and is not certified to be used in a production
#        environment.

#  filename:  wfrws.py
#     date:   2016-04-15
#   author:   Ira Kaplan, Information Builders
#    email:   ira_kaplan@ibi.com
# 

import requests
import xml.etree.ElementTree as ET
import xml.dom.minidom
import base64
#import StringIO
import re
import csv



'''
    Function and method naming conventions, prefixes

    sa - Security Administration
    mr - Managed Reporting
    rs - Reporting Server
    rc - Report Caster (future)
    ex - extended or helper functions not included with WebFOCUS RESTful Web Services


    New for lab in 2016. Add CSRF token to requests for:
    addUserToGroup
    copy
    delete
    listRulesForResource
    listRulesForRole
    listRulesForSubject
    move
    publish
    put  # any RESTful web service were IBIRS_action = 'put'
    removeUserFromGroup
    rename
    run # report
    unpublish

'''



class Request:
    ''' Pseudo Requests Request object for supporting ex_ or extended functions '''

    def __init__(self):
        self.headers = None
        self.body    = None
        

class ExRetval:
    ''' Pseudo Requests Response object for supporting ex_ or extended functions '''

    def __init__(self):
        self.text = '<?xml version="1.0" encoding="UTF-8"><extended message="Extended function for WebFOCUS 8 RESTful Web Services for Everyone"></extended>'
        self.url = 'http://www.InformationBuilders.com'
        self.content = '<?xml version="1.0" encoding="UTF-8"><extended message="Extended function for WebFOCUS 8 RESTful Web Services for Everyone"></extended>'
        
        self.request = Request()
        self.request.headers = 'This is a dummy header'
        self.request.body = 'This is a dummy body'
        



# -------------------------------[ Session ]----------------------------------
class Session(requests.Session):
    ''' Extend the features of Requests' Session object. '''

 
    # //////////////////////////// [ Helper functions ] //////////////////////////

    def xml_to_list(self, xml = None, node_spec = None):

        # structure of node_spec[ification] as a (dictionary)
        #   { 'tag' : 'item', '_jt' : 'IBFSUserObject', 'attributes' = ['name', 'email', 'description', 'handle'] }

        container = []

        for (event, node) in ET.iterparse(StringIO.StringIO(xml), ['start', 'end']):
            
            if event == 'start':
                if node.tag == node_spec['tag'] and ( not node.attrib.has_key('_jt') or  node.attrib['_jt'] == node_spec['_jt'] ):
                    for attribute in node_spec['attributes']:
                        container.append(node.attrib[attribute])

            if event == 'end':
                if node.tag == node_spec['tag'] and ( not node.attrib.has_key('_jt') or  node.attrib['_jt'] == node_spec['_jt'] ):
                    pass

        return container



    #----------------------------[ pretty_print_xml ]-----------------------------
    def pretty_print_xml(self, xml_string=None):
        '''Reformat xml string suitable for reading.'''

        # See: http://stackoverflow.com/questions/749796/pretty-printing-xml-in-python

        try:
            xml_parsed = xml.dom.minidom.parseString(xml_string)
        except:
            pretty_xml_as_string = '<Response not formatted as XML, cannot pretty print>'
        else:
            pretty_xml_as_string = xml_parsed.toprettyxml()

        return pretty_xml_as_string
        

   # ------------------------------[ sort_records ]------------------------------
    def sort_records(self, records, *sort_keys):
        '''Sort records represented as a list of dictionaries.'''

        # for nested sorts, start with the last sort key
        sort_keys = list(sort_keys)
        sort_keys.reverse()
        
        
        for sort_key in sort_keys:
            # Python sorts a list in place, no value returned
            records.sort(key=lambda record: record[sort_key].lower())

        return records



    # ------------------------------[ write_records_to_csv ]----------------------
    def write_records_to_csv(self, filename, fieldnames, records):
        '''Write list of dictionaries as csv file.

        See https://pymotw.com/2/csv/index.html
        '''

        with open(filename, 'wb') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames, restval='',
                                    extrasaction='ignore', dialect='excel',
                                    quoting=csv.QUOTE_ALL)
            writer.writeheader()
            writer.writerows(records)

    # ------------------------[ tabular_print_to_string ]---------------------
    def tabular_print_to_string(self, records, fieldnames):
        ''' Print records, a list of dictionaries, in columnar format.
            Columns are in order of fieldnames passed as a list.
        '''

        buffer = ''
        column_padding = 3
        underline_character = '-'
        
        column_widths = dict(zip(fieldnames, map(lambda fieldname: max([len(record[fieldname]) for record in records]) + column_padding, fieldnames)))

       # adjust column widths so no column is narrower than its title
        column_widths = { k : max(len(k) + column_padding, column_widths[k])  for k in column_widths.keys() }

        # print header row
        for fieldname in fieldnames:
            buffer += '%-*s' % (column_widths[fieldname], fieldname)
        buffer += '\n'

        # print underline row
        for fieldname in fieldnames:
            buffer += '%-*s' % (column_widths[fieldname], underline_character * (column_widths[fieldname] - 3)) 
        buffer += '\n'
        
        # print data records
        for record in records:
            for fieldname in fieldnames:
                buffer += '%-*s' % (column_widths[fieldname], record[fieldname]) 
            buffer += '\n'    

        return buffer







    # ////////////////////// [ Security Administration ] //////////////////////


    # ------------[ WebFOCUS Security Administration: list users ]-------------

    def sa_list_users(self):
        '''Listing Users.'''

        method = 'get'

        url = '%s://%s:%s/ibi_apps/rs/ibfs/SSYS/USERS?IBIRS_action=get' % (self.protocol,
                                                                           self.host,
                                                                           self.port)
         
        return self.request(method = method, url = url)

    def  mr_list_folders(self):
        '''Listing folders.'''

        method = 'get'

        url = '%s://%s:%s/ibi_apps/rs/ibfs/WFC/Repository?IBIRS_action=get' % (self.protocol,
                                                                           self.host,
                                                                           self.port)
         
        return self.request(method = method, url = url)




    # ------[ WebFOCUS Security Administration: list users to csv file ]-------

    def ex_sa_list_users_to_csv_file(self, csv_filename=r'D:\ibi\apps\wf_restful_lab\users.csv'):
        '''Write list of users to a csv file'''

        records = []

        retval = self.sa_list_users()
        tree = ET.fromstring(retval.content)

        for user in tree.iter('item'):
            attributes = user.attrib
            attributes['status'] = user.find('status').get('name')
            entries = [item.attrib  for item in user.findall('./properties/entry')]
            entries = {entry['key']: entry['value']  for entry in entries}
            attributes.update(entries)
            records.append(attributes)


        records = self.sort_records(records, 'name')

        fieldnames = ('name', 'description', 'email', 'fullPath',
                      'status', 'handle', 'index', 'length',
                      'parent', 'policy', 'rsPath', 'type',
                      'dummy', '_jt')
        
        self.write_records_to_csv(csv_filename, fieldnames, records) 

        retval = ExRetval()
        retval.text = self.tabular_print_to_string(records, fieldnames)
        return retval
        

        
    # ------[ WebFOCUS Security Administration: add users read from csv file ]-------
    def ex_sa_add_or_update_users_from_csv_file(self, csv_filename=r'D:\ibi\apps\wf_restful_lab\users.csv'):
        '''Add or update users read from a csv file.
        
           The column titles "name", "description", "email", and "status" must exist
           and must be in lowercase.  "password" is optional.  All other columns will
           be ignored.
        '''

        stream_in  = open(csv_filename, 'rb')

        # all fields must be quoted
        reader = csv.DictReader(stream_in, dialect='excel', quoting=csv.QUOTE_ALL, skipinitialspace=True)  

        # create a pseudo-response object to store each call's response
        response_values = ExRetval()

        for row in reader:            
            retval = self.sa_add_or_update_user(user = row['name'],
                                                replace_userid_properties = 'false',
                                                userid_title = row['description'], 
                                                email_address = row['email'],
                                                status = row['status'],
                                                password =  row['password'] if 'password' in row else ''
                                               )
            
            response_values.content += self.pretty_print_xml(retval.content)
            response_values.text    += self.pretty_print_xml(retval.text)
            
        return response_values
    


    # ------[ WebFOCUS Security Administration: delete users read from csv file ]-------
    def ex_sa_delete_users_read_from_csv_file(self, csv_filename=r'D:\ibi\apps\wf_restful_lab\users.csv'):
        '''Add or update users read from a csv file.
        
           The column title "name" must exist and must be in lowercase.
           All other columns will be ignored.
        '''

        stream_in  = open(csv_filename, 'rb')

        # all fields must be quoted
        reader = csv.DictReader(stream_in, dialect='excel', quoting=csv.QUOTE_ALL, skipinitialspace=True)  

        # create a pseudo-response object to store each call's response
        response_values = ExRetval()

        for row in reader:            
            retval = self.sa_delete_user(user=row['name'])
                                               
            response_values.content += self.pretty_print_xml(retval.content)
            response_values.text    += self.pretty_print_xml(retval.text)
            
        return response_values
    


    # ------[ WebFOCUS Security Administration: add groups read from csv file ]-------
    def ex_sa_add_or_update_groups_from_csv_file(self, replace_group_properties='false',
                                                 csv_filename=r'D:\ibi\apps\wf_restful_lab\groups.csv'):
        
        '''Add or update groups read from a csv file.
        
           The column titles "group_name" and "description" must exist and must be in lowercase.
           All other columns will be ignored.
        '''

        stream_in = open(csv_filename, 'rb')

        # all fields must be quoted
        reader = csv.DictReader(stream_in, dialect='excel', quoting=csv.QUOTE_ALL, skipinitialspace=True)  

        # create a pseudo-response object to store each call's response
        response_values = ExRetval()

        for row in reader:
            retval = self.sa_add_or_update_group(group_name=row['group_name'],
                                                 description=row['description'],
                                                 replace_group_properties=replace_group_properties)
            
            response_values.content += self.pretty_print_xml(retval.content)
            response_values.text    += self.pretty_print_xml(retval.text)
            
        return response_values
    


    # ------[ WebFOCUS Security Administration: add users read from csv file ]-------
    def ex_sa_add_users_to_groups_from_csv_file(self, csv_filename=r'D:\ibi\apps\wf_restful_lab\users_to_groups.csv'):
        '''Add users to groups read from a csv file.
        
           The column titles "user" and "group_name" must exist and must be in lowercase.
           All other columns will be ignored.

           Before using this function users and groups must have already been created.
        '''

        stream_in = open(csv_filename, 'rb')

        # all fields must be quoted
        reader = csv.DictReader(stream_in, dialect='excel', quoting=csv.QUOTE_ALL, skipinitialspace=True)  

        # create a pseudo-response object to store each call's response
        response_values = ExRetval()

        for row in reader:            
            retval = self.sa_add_user_to_group(user = row['user'],
                                               group_name = row['group_name'])
            
            response_values.content += self.pretty_print_xml(retval.content)
            response_values.text    += self.pretty_print_xml(retval.text)
            
        return response_values
    


    # -------------[ WebFOCUS Security Administration: list groups ]-----------

    def sa_list_groups(self, group_name = ''):
        '''Listing Groups. List groups in the level immediate below the parent
        group.'''
        
        method = 'get'

        url = '%s://%s:%s/ibi_apps/rs/ibfs/SSYS/GROUPS/%s?IBIRS_action=get' % (self.protocol,
                                                                               self.host,
                                                                               self.port,
                                                                               group_name)
        
        return self.request(method = method, url = url)


        
    #------------[ WebFOCUS Security Administration: list privileges]----------

    def sa_list_privileges(self):
        '''Listing Privileges.'''
        
        method = 'get' 

        params = {'IBIRS_action' : 'privileges'}
        
        url = '%s://%s:%s/ibi_apps/rs/ibfs' % (self.protocol, self.host, self.port)

        return self.request(method = method, url = url, params = params) 



    #------------[ WebFOCUS Security Administration: list roles]---------------

    def sa_list_roles(self):
        '''Listing Roles.'''
        
        method = 'get' 

        params = {'IBIRS_action' : 'get'}
        
        url = '%s://%s:%s/ibi_apps/rs/ibfs/SSYS/ROLES' % (self.protocol, self.host, self.port)

        return self.request(method = method, url = url, params = params) 



    # --------[WebFOCUS Security Administration: listing_all_groups ]----------

    def ex_sa_list_all_groups(self, group_name='/'):
        '''Listing Groups. List groups in all levels below the parent group.'''

        records = []
        
        def get_nested_groups(group_name=group_name):
            retval = self.sa_list_groups(group_name=group_name)
            tree = ET.fromstring(retval.content)
    
            for group in tree.iter('item'):
                attributes = group.attrib
                attributes['fullName'] = attributes['fullPath'].replace('IBFS:/SSYS/GROUPS/', '')
                records.append(attributes)
                get_nested_groups(group_name=attributes['fullName'])


        get_nested_groups(group_name=group_name)
        records = self.sort_records(records, 'fullName')

        fieldnames = ['fullName', 'name', 'description', 'rsPath', 'fullPath', 'dummy',
                      'container', 'handle', 'parent', 'index', 'length', 'policy',
                      'typeDescription', 'type', '_jt']
        
        retval = ExRetval()
        # retval.content = self.tabular_print_to_string(records, fieldnames)
        retval.text = self.tabular_print_to_string(records, fieldnames)
        return retval



    # ------[ WebFOCUS Security Administration: list users in group ]----------

    def sa_list_users_in_group(self, group_name = ''):
        '''Listing Users Within a Group.'''

        method = 'get'

        args = '''<object _jt="HashMap">
                    <entry>
                      <key _jt="string" value="TYPE"/>
                      <value _jt="string" value="USERS"/>
                    </entry>
                  </object>'''

        params = {'IBIRS_action'  : 'get',
                  'IBIRS_args'    :  args
                 }

        url = '%s://%s:%s/ibi_apps/rs/ibfs/SSYS/GROUPS/%s' % (self.protocol, 
                                                              self.host, 
                                                              self.port, 
                                                              group_name)
        
        return self.request(method = method, url = url, params = params)

    

    # ---------[ WebFOCUS Security Administration: list groups with users ]----
    
    def ex_sa_list_groups_with_users(self, group_name= '/', sort_by='group'):
        '''List groups, with users, in all levels below the parent group.
           Default sorting is by group. sort_by values are 'user' or 'group'.
        '''

        records = []
        
        def get_nested_groups(group_name=group_name):
            retval_groups = self.sa_list_groups(group_name=group_name)
            tree_groups = ET.fromstring(retval_groups.content)
    
            for group in tree_groups.iter('item'):
                group_full_name = group.attrib['fullPath'].replace('IBFS:/SSYS/GROUPS/', '')
                # skip the group EVERYONE
                if group_full_name == 'EVERYONE': continue
                
                # get users in group
                retval_users = self.sa_list_users_in_group(group_name = group_full_name)
                tree_users = ET.fromstring(retval_users.content)
                for user in tree_users.iter('item'):
                    user_name = user.attrib['name']
                    records.append({'group_name': group_full_name, 'user_name': user_name})
                    
                get_nested_groups(group_name=group_full_name)


        get_nested_groups(group_name=group_name)

        if sort_by.lower() == 'user':
            records = self.sort_records(records, 'user_name', 'group_name')
        elif sort_by.lower() == 'group':
            # sort by group, by user within group
            records = self.sort_records(records, 'group_name', 'user_name')
        else:
            # future development: raise an exception
            pass
        
        fieldnames = ['group_name', 'user_name' ]        
        retval = ExRetval()
        retval.text = self.tabular_print_to_string(records, fieldnames)
        return retval


    
    # -------[ WebFOCUS Security Administration: add or update user]-----------

    def sa_add_or_update_user(self, user = None,
                                    replace_userid_properties = 'false',
                                    userid_title = '', 
                                    email_address = '',
                                    password = '', 
                                    status = 'ACTIVE'):
        '''Adding and Updating a User.'''
        

        method = 'post' 

        object = '''<object _jt="IBFSUserObject"
                       description="%s"
                       email="%s"
                       password="%s"
                       type="User">
                       <status _jt="IBSSUserStatus" name="%s"/>
                    </object>''' % (userid_title, email_address, password, status)

        data = {'IBIRS_action'   :  'put',
                'IBIRS_object'   :  object,
                'IBIRS_replace'  :  replace_userid_properties
               }

        # add the CSRF token value to the body (data) of the request
        if self.IBIWF_SES_AUTH_TOKEN is not None:
            data['IBIWF_SES_AUTH_TOKEN'] = self.IBIWF_SES_AUTH_TOKEN


        url = '%s://%s:%s/ibi_apps/rs/ibfs/SSYS/USERS/%s' % (self.protocol, 
                                                             self.host, 
                                                             self.port, 
                                                             user)

        return self.request(method = method, url = url, data = data)



    
    # -------[ WebFOCUS Security Administration: change password]-----------

    def sa_change_password(self, user_name = '', password = ''):
        '''Change user's password.'''

        method = 'post' 

        data = {'IBIRS_action'   :  'changePassword',
                'IBIRS_userName' :  user_name,
                'IBIRS_password' :  password
               }

        # add the CSRF token value to the body (data) of the request
        if self.IBIWF_SES_AUTH_TOKEN is not None:
            data['IBIWF_SES_AUTH_TOKEN'] = self.IBIWF_SES_AUTH_TOKEN


        url = '%s://%s:%s/ibi_apps/rs/ibfs/SSYS/USERS/%s' % (self.protocol, 
                                                             self.host, 
                                                             self.port, 
                                                             user_name)

        return self.request(method = method, url = url, data = data)






    # ------------[ WebFOCUS Security Administration: delete user]-------------

    def sa_delete_user(self, user = None):
        '''Deleting a User.'''

        method = 'delete'

        data = {'IBIRS_action' : 'delete'}
        
        url = '%s://%s:%s/ibi_apps/rs/ibfs/SSYS/USERS/%s' % (self.protocol, 
                                                             self.host,
                                                             self.port, 
                                                             user)

        # add the CSRF token value to the body (data) of the request, if the token exists
        if self.IBIWF_SES_AUTH_TOKEN is not None:
            data['IBIWF_SES_AUTH_TOKEN'] = self.IBIWF_SES_AUTH_TOKEN

        return self.request(method = method, url = url, data = data)



    # --------[ WebFOCUS Security Administration: add or update group]---------
    
    def sa_add_or_update_group(self,
                               group_name = None,
                               description = '',
                               replace_group_properties = 'false'):          

        '''Adding and Updating a Group.'''
       
        method = 'post' 

        object = '''<object _jt="IBFSGroupObject"
                        container="true"
                        description="%s"
                        type="Group">
                    </object>''' % (description)

        data = {'IBIRS_action'   :  'put',
                'IBIRS_object'   :  object,
                'IBIRS_replace'  :  replace_group_properties
               }

        # add the CSRF token value to the body (data) of the request
        if self.IBIWF_SES_AUTH_TOKEN is not None:
            data['IBIWF_SES_AUTH_TOKEN'] = self.IBIWF_SES_AUTH_TOKEN


        url = '%s://%s:%s/ibi_apps/rs/ibfs/SSYS/GROUPS/%s' % (self.protocol, 
                                                              self.host, 
                                                              self.port, 
                                                              group_name)

        return self.request(method = method, url = url, data = data)



    # -----------[ WebFOCUS Security Administration: delete group]-------------

    def sa_delete_group(self, group_name = None):
        '''Deleting a Group.'''

        method = 'delete'
        
        data = {'IBIRS_action' : 'delete'}

        # add the CSRF token value to the body (data) of the request
        if self.IBIWF_SES_AUTH_TOKEN is not None:
            data['IBIWF_SES_AUTH_TOKEN'] = self.IBIWF_SES_AUTH_TOKEN
     
        url = '%s://%s:%s/ibi_apps/rs/ibfs/SSYS/GROUPS/%s' % (self.protocol, 
                                                              self.host, 
                                                              self.port, 
                                                              group_name)

        return self.request(method = method, url = url, data = data)



    # --------[ WebFOCUS Security Administration: add user to group ]----------

    def sa_add_user_to_group(self, user = None, group_name = None):
        '''Adding a User to a Group.'''
      
        method = 'post' 

        data = {'IBIRS_action'    :  'addUserToGroup',
                'IBIRS_groupPath' :  'SSYS/GROUPS/%s' % group_name,
               }

        # add the CSRF token value to the body (data) of the request, if the token exists
        if self.IBIWF_SES_AUTH_TOKEN is not None:
            data['IBIWF_SES_AUTH_TOKEN'] = self.IBIWF_SES_AUTH_TOKEN


        url = '%s://%s:%s/ibi_apps/rs/ibfs/SSYS/USERS/%s' % (self.protocol, 
                                                             self.host, 
                                                             self.port, 
                                                             user)

        return self.request(method = method, url = url, data = data) 
    


    #-----[ WebFOCUS Security Administration: remove user from group ]-------

    def sa_remove_user_from_group(self, user = None, group_name = None):
        '''Removing a User From a Group.'''
        
        method = 'post' 

        data = {'IBIRS_action'    :  'removeUserFromGroup',
                'IBIRS_groupPath' :  'SSYS/GROUPS/%s' % group_name,
               }

        # add the CSRF token value to the body (data) of the request, if the token exists
        if self.IBIWF_SES_AUTH_TOKEN is not None:
            data['IBIWF_SES_AUTH_TOKEN'] = self.IBIWF_SES_AUTH_TOKEN

        url = '%s://%s:%s/ibi_apps/rs/ibfs/SSYS/USERS/%s' % (self.protocol, 
                                                             self.host, 
                                                             self.port, 
                                                             user)

        return self.request(method = method, url = url, data = data) 




    #-------[ WebFOCUS Security Administration: list rules for subject ]-------

    def sa_list_rules_for_subject(self, type = 'group', groupuser = ''):
        '''Listing Rules for a Subject.'''

        types = {'group' : 'GROUPS', 'user' : 'USERS'}
        
        method = 'post' 

        data = {'IBIRS_action'  : 'listRulesForSubject'}
                                 
        # add the CSRF token value to the body (data) of the request, if the token exists
        if self.IBIWF_SES_AUTH_TOKEN is not None:
            data['IBIWF_SES_AUTH_TOKEN'] = self.IBIWF_SES_AUTH_TOKEN

        url = '%s://%s:%s/ibi_apps/rs/ibfs/SSYS/%s/%s' % (self.protocol, 
                                                          self.host, 
                                                          self.port, 
                                                          types[type], 
                                                          groupuser )

        return self.request(method = method, url = url, data = data) 




    #------[ WebFOCUS Security Administration: list rules for resource ]-------

    def sa_list_rules_for_resource(self, resource = ''):
        '''Listing Rules for a Resource'''
        
        method = 'post' 

        data = {'IBIRS_action': 'listRulesForResource'}

        # add the CSRF token value to the body (data) of the request, if the token exists
        if self.IBIWF_SES_AUTH_TOKEN is not None:
            data['IBIWF_SES_AUTH_TOKEN'] = self.IBIWF_SES_AUTH_TOKEN

                          
        url = '%s://%s:%s/ibi_apps/rs/ibfs/%s' % (self.protocol, 
                                                  self.host, 
                                                  self.port, 
                                                  resource)

        return self.request(method = method, url = url, data = data) 




    #-------[ WebFOCUS Security Administration: list rules for role ]----------

    def sa_list_rules_for_role(self, role = ''):
        '''Listing Rules for a Role.'''
        
        method = 'post' 

        data = {'IBIRS_action': 'listRulesForRole'}

        # add the CSRF token value to the body (data) of the request, if the token exists
        if self.IBIWF_SES_AUTH_TOKEN is not None:
            data['IBIWF_SES_AUTH_TOKEN'] = self.IBIWF_SES_AUTH_TOKEN

                                 
        url = '%s://%s:%s/ibi_apps/rs/ibfs/%s' % (self.protocol, 
                                                  self.host, 
                                                  self.port, 
                                                  role)

        return self.request(method = method, url = url, data = data) 



    #-------------[ WebFOCUS Security Administration: expand policy string] ------------

    def sa_expand_policy_string(self, policy_string= ''):
        '''Expand the base 64 policy string.'''

        method = 'post'
        
        data = {'IBIRS_action'       : 'expandPolicy',
                'IBIRS_base64Policy' :  policy_string}

        # add the CSRF token value to the body (data) of the request, if the token exists
        if self.IBIWF_SES_AUTH_TOKEN is not None:
            data['IBIWF_SES_AUTH_TOKEN'] = self.IBIWF_SES_AUTH_TOKEN

        url = '%s://%s:%s/ibi_apps/rs/utils' % (self.protocol,
                                                self.host,
                                                self.port)

        return self.request(method = method, url = url, data = data)
        





	


    # ///////////////////////// [ Managed Reporting ] /////////////////////////

    # -----------------[ persist_ibi_csrf_token_value ]-----------------------

    def persist_ibi_csrf_token_value(self, xml):
        '''Get the value of IBI_CSRF_Token_Value from the response to the sign-on request.'''

        tree = ET.fromstring(xml)
        token = tree.find('properties/entry[@key="IBI_CSRF_Token_Value"]')

        if token is not None:
            token_value = token.attrib['value']
            self.IBIWF_SES_AUTH_TOKEN = token_value
        
        

    # -------------[ WebFOCUS Managed Reporting: sign in ]---------------------
    
    def mr_signin(self, protocol='http', 
                        host = 'localhost', 
                        port = '8080', 
                        user = 'admin', 
                        password = 'admin'): 
        '''Authenticating WebFOCUS Sign-On Requests.'''

        self.protocol = protocol
        self.host = host
        self.port = port

        method = 'post'
        
        body = {'IBIRS_action'   : 'signOn',
                'IBIRS_userName' :  user,
                'IBIRS_password' :  password,
               }	

        url = '%s://%s:%s/ibi_apps/rs/ibfs' % (self.protocol, 
                                               self.host, 
                                               self.port)
        
        response = self.request(method = method, url = url, data = body)
        self.persist_ibi_csrf_token_value(response.content)
        return response



    # ----------------[ WebFOCUS Managed Reporting: sign off ]-----------------

    def mr_signoff(self): 
        '''Signing-Off From WebFOCUS.'''

        method = 'post'
        
        body = {'IBIRS_action' : 'signOff'}

        url = '%s://%s:%s/ibi_apps/rs/ibfs' % (self.protocol, 
                                               self.host, 
                                               self.port)

        return self.request(method = method, url = url, data = body)



##   In development.  IBIRS_clientPath and IBIRS_htmlPath needs fixing,
##   could not figure out correct values.
##   Add support for report parameters.

    #---------------[ WebFOCUS Managed Reporting: run report ] ----------------

    def mr_run_report(self, foldername = '', reportname = '', report_parms = ''):
        '''WebFOCUS Managed Reporting  - Running a Report

           Output format for reports run with mr_run_report should be
           html or xml.  For Excel or PDF output use mr_run_report_no_redirect.

           Optional report_parms are entered as parm_name=parm_value.
           multiple parameters are separated by &.

           Example
           -------
           COUNTRY=ENGLAND&CAR=JAGUAR
         '''       

        method = 'post'        

        data = {'IBIRS_action' : 'run'}

        # parse the report parameters and add them to the data dictionary
        if report_parms:
            report_parms_dict  = dict([item.split('=') for item in report_parms.split('&')])  
            data.update(report_parms_dict)
            
        # add the CSRF token value to the body (data) of the request, if the token exists
        if self.IBIWF_SES_AUTH_TOKEN is not None:
            data['IBIWF_SES_AUTH_TOKEN'] = self.IBIWF_SES_AUTH_TOKEN

        url = '%s://%s:%s/ibi_apps/rs/ibfs/WFC/Repository/%s/%s' % (self.protocol,
                                                                    self.host,
                                                                    self.port,
                                                                    foldername,
                                                                    reportname)
        
        return self.request(method = method, url = url, data = data) 

    def run_sch(self, foldername = '',schname = ''):

        method = 'post'        

        data = {'IBIRS_action' : 'run'}
            
        # add the CSRF token value to the body (data) of the request, if the token exists
        if self.IBIWF_SES_AUTH_TOKEN is not None:
            data['IBIWF_SES_AUTH_TOKEN'] = self.IBIWF_SES_AUTH_TOKEN

        url = '%s://%s:%s/ibi_apps/rs/ibfs/WFC/Repository/%s/%s' % (self.protocol,
                                                                    self.host,
                                                                    self.port,
                                                                    foldername,
                                                                    schname)
        
        return self.request(method = method, url = url, data = data) 
      
    def get_contents(self,foldername = ''):
          
            method = 'get'
            params = {'IBIRS_action' : 'get'}
            
            url = '%s://%s:%s/ibi_apps/rs/ibfs/WFC/Repository/%s' % (self.protocol,
                                                                     self.host,
                                                                     self.port,
                                                                     foldername)
           
         
            return self.request(method = method, url = url, params = params)


    def delete_rc_report_lib(self, foldername = '',libtitle = ''):

        method = 'post'        

        data = {'IBIRS_action' : 'delete'}
            
        # add the CSRF token value to the body (data) of the request, if the token exists
        if self.IBIWF_SES_AUTH_TOKEN is not None:
            data['IBIWF_SES_AUTH_TOKEN'] = self.IBIWF_SES_AUTH_TOKEN

        url = '%s://%s:%s/ibi_apps/rs/ibfs/WFC/Repository/%s/%s' % (self.protocol,
                                                                    self.host,
                                                                    self.port,
                                                                    foldername,
                                                                    libtitle)
        
        return self.request(method = method, url = url, data = data) 

    def sch_status(self, jobid = ''):

        method = 'get'        

        url = '%s://%s:%s/ibi_apps/services/ConsoleServiceREST/getJobStatus?jobId=%s' % (self.protocol,
                                                                                     self.host,
                                                                                     self.port,
                                                                                     jobid)
        return self.request(method = method, url = url) 

        
       

   #-------[ WebFOCUS Managed Reporting: run report, no redirection ] --------

    def mr_run_report_streaming(self, foldername = '', reportname = '', report_parms = ''):
        '''WebFOCUS Managed Reporting  - Running a Report with no Redirection

           Output format for reports run with mr_run_report_no_redirect should be
           Excel or PDF.  For html or xml output use mr_run_report.

           Optional report_parms are entered as parm_name=parm_value.
           multiple parameters are separated by &.

           Example
           -------
           COUNTRY=ENGLAND&CAR=JAGUAR
         '''       

        method = 'post'        

        data = {'IBIRS_action' : 'run'}

        # parse the report parameters and add them to the data dictionary
        if report_parms:
            report_parms_dict = dict([item.split('=') for item in report_parms.split('&')])  
            data.update(report_parms_dict)
            
        # add the CSRF token value to the body (data) of the request, if the token exists
        if self.IBIWF_SES_AUTH_TOKEN is not None:
            data['IBIWF_SES_AUTH_TOKEN'] = self.IBIWF_SES_AUTH_TOKEN
            
##        # Object (Optional)
##        # Is the XML object that is used to turn off redirection when retrieving
##        # report output for MIME types like EXCEL and PDF using the following format:
##        object = '''<rootObject _jt="HashMap">
##                        <entry>
##                            <key _jt="string" value="IBFS_contextVars"/>
##                            <value _jt="HashMap">
##                                <entry>
##                                    <key _jt="string" value="IBIWF_redirect"/>
##                                    <value _jt="string" value="LEN"/>
##                                </entry>
##                            </value>
##                        </entry>
##                    </rootObject>'''
##        
##        data['IBIRS_args'] = object
##        data['IBIRS_object'] = object

        url = '%s://%s:%s/ibi_apps/rs/ibfs/WFC/Repository/%s/%s' % (self.protocol,
                                                                    self.host,
                                                                    self.port,
                                                                    foldername,
                                                                    reportname)
        
        return self.request(method = method, url = url, data = data, stream = False) 


    
    #-------------[ WebFOCUS Managed Reporting: list report parameters] --------------------

    def mr_list_report_parameters(self, foldername = '', fexname = '' ):
        '''WebFOCUS Managed Reporting  - Listing the Parameters for a Report Within Managed Reporting.'''

        method = 'get' 

        url = '%s://%s:%s/ibi_apps/rs/ibfs/WFC/Repository/%s/%s?IBIRS_action=describeFex' % (self.protocol,
                                                                                             self.host,
                                                                                             self.port,
                                                                                             foldername,
                                                                                             fexname)
        return self.request(method = method, url = url) 



    #-------------[ WebFOCUS Managed Reporting: move item] --------------------

    def mr_move_item(self, foldername_source = '',
                           itemname_source = '',
                           foldername_destination = '',
                           itemname_destination = '',
                           replace = 'true'):
        
        '''WebFOCUS Managed Reporting  - Moving an Item.'''


        method = 'post' 
 
        data= {'IBIRS_action'      : 'move',
               'IBIRS_destination' : '/WFC/Repository/%s/%s' % (foldername_destination,
                                                                itemname_destination),
               'IBIRS_replace'     :  replace
              }

        # add the CSRF token value to the body (data) of the request, if the token exists
        if self.IBIWF_SES_AUTH_TOKEN is not None:
            data['IBIWF_SES_AUTH_TOKEN'] = self.IBIWF_SES_AUTH_TOKEN

        url = '%s://%s:%s/ibi_apps/rs/ibfs/WFC/Repository/%s/%s' % (self.protocol,
                                                                    self.host,
                                                                    self.port,
                                                                    foldername_source,
                                                                    itemname_source)
        
        return self.request(method = method, url = url, data = data) 



    #-------------[ WebFOCUS Managed Reporting: copy item] --------------------

    def mr_copy_item(self, foldername_source = '',
                           itemname_source = '',
                           foldername_destination = '',
                           itemname_destination = '',
                           replace = 'true'):
        
        '''WebFOCUS Managed Reporting  - Copying an Item.'''


        method = 'post' 

        data= {'IBIRS_action'      : 'copy',
               'IBIRS_destination' : '/WFC/Repository/%s/%s' % (foldername_destination,
                                                                itemname_destination),
               'IBIRS_replace'     :  replace
              }

        # add the CSRF token value to the body (data) of the request, if the token exists
        if self.IBIWF_SES_AUTH_TOKEN is not None:
            data['IBIWF_SES_AUTH_TOKEN'] = self.IBIWF_SES_AUTH_TOKEN

        url = '%s://%s:%s/ibi_apps/rs/ibfs/WFC/Repository/%s/%s' % (self.protocol,
                                                                    self.host,
                                                                    self.port,
                                                                    foldername_source,
                                                                    itemname_source)
        
        return self.request(method = method, url = url, data = data) 



    #---------[ WebFOCUS Managed Reporting: create or update folder ]----------

    # trouble with replace.  See manual re retrieving and updating properties
    
    def mr_create_or_update_folder(self, folder_name = '',
                                         folder_description = '',
                                         summary = '',
                                         # applist = '', not working correctly
                                         private = 'false',
                                         replace = 'true'):

        '''WebFOCUS Managed Reporting  - Creating and Updating a Folder.'''

        method = 'post' 


        applist = '' # removed applist from function parameters
        
        object = '''<object _jt="IBFSMRObject" container="true"
                        description="%s"
                        summary="%s"
                        appName="%s">

                        <properties size="3">
                             <entry key="autogenmyreports"/>
                             <entry key="GeneralAccessGroup=/SSYS/GROUPS/p3/BasicUsers"/> 
                             <entry key="Cascade"/>  
                        </properties>

                    </object>''' % (folder_description, summary, applist)


        data= {'IBIRS_action'      : 'put',
               'IBIRS_object'      :  object,
               'IBIRS_private'     :  private,
               'IBIRS_replace'     :  replace
              }
    def create_Domain(self,domain_name = '') :

        '''WebFOCUS Managed Reporting  - Creating and Updating a Folder.'''

        method = 'post' 

        object='''<object
_jt="HashMap"><entry><key _jt="string" value="name"/><value _jt="string"
value="%s"/></entry><entry><key _jt="string" value="desc"/><value
_jt="string" value="%s"/></entry></object>''' % (domain_name,domain_name)


        data= {'IBIRS_action'    : 'run',
               'IBIRS_vars'      :  object,
               'IBIRS_fileName'  : 'ibiEnterpriseDomain'
              
              }
       # add the CSRF token value to the body (data) of the request
        if self.IBIWF_SES_AUTH_TOKEN is not None:
            data['IBIWF_SES_AUTH_TOKEN'] = self.IBIWF_SES_AUTH_TOKEN



        url = '%s://%s:%s/ibi_apps/rs/templates' % (self.protocol,
                                                    self.host,
                                                    self.port )
        
        return self.request(method = method, url = url, data = data) 



    #--------[ WebFOCUS Managed Reporting: list folders and subfolders ]-------

    def ex_mr_list_folders_and_subfolders(self, folder_name=''):
        '''Extended List Folders and Subfolders. List folders in all levels below the
           parent folder.
           Code can be simplified. See ex_sa_list_all_groups() for example.
        '''

        folder_list = []

        def get_folders(folder_name = ''):
            method = 'get'
            params = {'IBIRS_action' : 'get'}
            
            url = '%s://%s:%s/ibi_apps/rs/ibfs/WFC/Repository/%s' % (self.protocol,
                                                                     self.host,
                                                                     self.port,
                                                                     folder_name)
           
            f = self.request(method = method, url = url, params = params)

            folder_names = []            
            tree = ET.fromstring(f.content)
            
            # can a list comprehension replace these lines?
            # should the folder name include the path to eliminate ambiguity?
            for folder in tree.findall(".//item[@_jt='IBFSMRObject']"):
                name = folder.attrib.get('name')
                if name: folder_names.append(name)
            
            return folder_names


        def count_subfolders(folder_name=''):
            '''Return count of folder's subfolders one level down only.'''
            return len(get_folders(folder_name = folder_name))

    
        def compare(x, y):
            if x.lower() == y.lower(): return 0
            if x.lower()  < y.lower(): return -1
            if x.lower()  > y.lower(): return 1
    

        def walk_folder_tree(folder_name, folder_list):
            folder_list.append(folder_name)
        
            for folder in get_folders(folder_name):
                path = folder_name + '/' + folder 
            
                if not count_subfolders(folder_name = path):  
                    folder_list.append(path)
                else:
                    walk_folder_tree(path, folder_list)
             
            return folder_list

        folder_list.sort(cmp=compare)   
        completed_folder_list = walk_folder_tree(folder_name, folder_list)

        completed_folder_list_as_text = ('\n').join(completed_folder_list)
        retval = ExRetval()
        retval.content = completed_folder_list_as_text
        return retval



    #--------[ WebFOCUS Managed Reporting: list folders and subfolders ]-------

    def mr_list_folders_and_subfolders(self, folder_name=''):
        '''List Folders and Subfolders. List folders one levels below the
           parent folder.'''

        method = 'get'
        params = {'IBIRS_action' : 'get'}
        
        url = '%s://%s:%s/ibi_apps/rs/ibfs/WFC/Repository/%s' % (self.protocol,
                                                                 self.host,
                                                                 self.port,
                                                                 folder_name)
       
        retval = self.request(method = method, url = url, params = params)
        return retval



    #-------------[ WebFOCUS Managed Reporting: publish item ]-----------------

    def mr_publish_item(self, folder_name='', item_name = None):
        
        '''Publishing an Item. Publish a folder or an item within a folder.
            Note: an item cannot be published if the parent folder is
            unpublished.'''

        method = 'post' 

        data= {'IBIRS_action' : 'publish'}

        # add the CSRF token value to the body (data) of the request, if the token exists
        if self.IBIWF_SES_AUTH_TOKEN is not None:
            data['IBIWF_SES_AUTH_TOKEN'] = self.IBIWF_SES_AUTH_TOKEN

        folder_and_item = '%s/%s' % (folder_name, item_name) if item_name else folder_name

        url = '%s://%s:%s/ibi_apps/rs/ibfs/WFC/Repository/%s' % (self.protocol,
                                                                 self.host,
                                                                 self.port,
                                                                 folder_and_item)
        
        return self.request(method = method, url = url, data = data) 

    

    #-------------[ WebFOCUS Managed Reporting: unpublish item ]---------------

    def mr_unpublish_item(self, folder_name='',
                                item_name = None,
                                user_name = 'rest_admin',
                                clear_shares = 'false'):
        
        '''Unpublishing an Item. Unpublish a folder or an item within a
        folder.'''

        method = 'post'

        # user_name
        # ---------
        # If the item is private, then the full path to the owner of the item.
        # For example, /SSYS/USERS/admin.
        #
        # clear_shares
        # ------------
        # If the item is private, specify one of the following:
        # true. Unshares the item.
        # false. Does not unshare the item.
    
        data= {'IBIRS_action'      : 'unpublish',
               'IBIRS_ownerPath'   : '/SSYS/USERS/%s' % user_name,
               'IBIRS_clearShares' :  clear_shares
              }

        # add the CSRF token value to the body (data) of the request, if the token exists
        if self.IBIWF_SES_AUTH_TOKEN is not None:
            data['IBIWF_SES_AUTH_TOKEN'] = self.IBIWF_SES_AUTH_TOKEN


        folder_and_item = '%s/%s' % (folder_name, item_name) if item_name else folder_name

        url = '%s://%s:%s/ibi_apps/rs/ibfs/WFC/Repository/%s' % (self.protocol,
                                                                 self.host,
                                                                 self.port,
                                                                 folder_and_item)
        
        return self.request(method = method, url = url, data = data) 



    #--------------[ WebFOCUS Managed Reporting: rename item ] ----------------

    def mr_rename_item(self, foldername = '',
                             itemname = '',
                             renamed_item=''):

        '''WebFOCUS Managed Reporting  - Renaming an Item.'''
        
        method = 'post' 

        data= {'IBIRS_action'     : 'rename',
               'IBIRS_newName'    :  renamed_item
              }

        # add the CSRF token value to the body (data) of the request, if the token exists
        if self.IBIWF_SES_AUTH_TOKEN is not None:
            data['IBIWF_SES_AUTH_TOKEN'] = self.IBIWF_SES_AUTH_TOKEN

        url = '%s://%s:%s/ibi_apps/rs/ibfs/WFC/Repository/%s/%s' % (self.protocol,
                                                                    self.host,
                                                                    self.port,
                                                                    foldername,
                                                                    itemname)
        
        return self.request(method = method, url = url, data = data) 



    #--------------[ WebFOCUS Managed Reporting: upload report ] --------------

    def mr_upload_report(self,
                         folder_name = None,
                         fex_name = None,
                         local_file_path = None):
                                                          
        '''WebFOCUS Managed Reporting.  Uploading a WebFOCUS Report.'''

        method = 'post'
      
        content = open(local_file_path, 'rb').read() 
        content_base64 = base64.b64encode(content)
        content_base64=re.sub(r'\\','',str(content_base64,'utf-8'))
        object = '''<rootObject _jt="IBFSFile"  type="IBFSFile">
                        <content _jt="IBFSByteContent" char_set="Cp1252">%s</content>
                    </rootObject>''' % (content_base64)

        data= {'IBIRS_action' : 'put',
               'IBIRS_object' :  object,
              }

        # add the CSRF token value to the body (data) of the request
        if self.IBIWF_SES_AUTH_TOKEN is not None:
            data['IBIWF_SES_AUTH_TOKEN'] = self.IBIWF_SES_AUTH_TOKEN

        url = '%s://%s:%s/ibi_apps/rs/ibfs/WFC/Repository/%s/%s' % (self.protocol,
                                                                    self.host,
                                                                    self.port,
                                                                    folder_name,
                                                                    fex_name)
        
        return self.request(method = method, url = url, data = data) 



    #--------------[ WebFOCUS Managed Reporting: Retrieving Content for a WebFOCUS Report and URL ] --------------
    def mr_get_report_or_url_content_decoded(self, folder_name = '', content_name = ''):
                                                          
        '''WebFOCUS Managed Reporting.  Retrieving Content for a WebFOCUS Report and URL.'''

        method = 'get'

        url = '%s://%s:%s/ibi_apps/rs/ibfs/WFC/Repository/%s/%s/?IBIRS_action=get' % (self.protocol,
                                                                                      self.host,
                                                                                      self.port,
                                                                                      folder_name,
                                                                                      content_name)
        retval = self.request(method = method, url = url)

        tree = ET.fromstring(retval.content)
        content_item = tree.find('rootObject/content')
        content_base64_encoded = content_item.text
        content_base64_decoded = base64.b64decode(content_base64_encoded)

        # pseudo object for handling requests that require post processing
        pseudo_retval = ExRetval()
        pseudo_retval.text = content_base64_decoded
        pseudo_retval.content = content_base64_decoded                              
        return pseudo_retval



    #--------------[ WebFOCUS Managed Reporting: Retrieving Content for a WebFOCUS Report and URL ] --------------
    def mr_get_report_or_url_content_raw(self, folder_name = '', content_name = ''):
                                                          
        '''WebFOCUS Managed Reporting.  Retrieving Content for a WebFOCUS Report and URL.'''

        method = 'get'

        url = '%s://%s:%s/ibi_apps/rs/ibfs/WFC/Repository/%s/%s/?IBIRS_action=get' % (self.protocol,
                                                                                      self.host,
                                                                                      self.port,
                                                                                      folder_name,
                                                                                      content_name)
        return self.request(method = method, url = url)




    # ///////////////////////// [ Reporting Server ] /////////////////////////


##   In development.  IBIRS_clientPath and IBIRS_htmlPath needs fixing,
##   could not figure out correct values.
##   Add support for report parameters.
    #---------------[ WebFOCUS Reporting Server: run report ] -----------------

    def rs_run_report(self, nodename = 'EDASERVE', appname = '', fexname = '' ):
        '''Running a Report Within an Application.'''
        
        method = 'post' 

        data = {'IBIRS_action'     : 'run',
##                'IBIRS_clientPath' : '',
##                'IBIRS_htmlPath'   : '%s://%s:%s/ibi_apps/ibi_html' % (self.protocol,
##                                                                          self.host,
##                                                                          self.port)
               }

        # add the CSRF token value to the body (data) of the request
        if self.IBIWF_SES_AUTH_TOKEN is not None:
            data['IBIWF_SES_AUTH_TOKEN'] = self.IBIWF_SES_AUTH_TOKEN

        url = '%s://%s:%s/ibi_apps/rs/ibfs/EDA/%s/%s/%s' % (self.protocol,
                                                            self.host,
                                                            self.port,
                                                            nodename,
                                                            appname,
                                                            fexname)

        return self.request(method = method, url = url, data = data) 



    #---------------[ WebFOCUS Reporting Server: run ad hoc fex ] -----------------

    def rs_run_ad_hoc_fex(self, nodename = 'EDASERVE', fex_content = '' ):
        '''Running a Report Within an Application.'''

        method = 'post' 

        data = {'IBIRS_action'     : 'runAdHocFex',
                'IBIRS_path'       : 'EDA',
                'IBIRS_nodeName'   : nodename,
                'IBIRS_fexContent' : fex_content
               }

        # add the CSRF token value to the body (data) of the request
        if self.IBIWF_SES_AUTH_TOKEN is not None:
            data['IBIWF_SES_AUTH_TOKEN'] = self.IBIWF_SES_AUTH_TOKEN

        url = '%s://%s:%s/ibi_apps/rs/ibfs/EDA' % (self.protocol,
                                                   self.host,
                                                   self.port)

        return self.request(method = method, url = url, data = data) 


    #-----------------[ WebFOCUS Reporting Server: list nodes ] ---------------

    def rs_list_nodes(self):
                                                          
        '''WebFOCUS Reporting Server. Listing WebFOCUS Reporting Server Nodes.'''

        method = 'get'    

        params= {'IBIRS_action' : 'get'}
    
        url = '%s://%s:%s/ibi_apps/rs/ibfs/EDA' % (self.protocol, self.host, self.port)
        
        return self.request(method = method, url = url, params = params) 



    #------------[ WebFOCUS Reporting Server: create application ] ------------

    def rs_create_application(self, node_name = 'EDASERVE', app_name = 'My_App'):
                                 
        '''WebFOCUS Reporting Server. Creating an Application.'''

        method = 'post' 

        object = '''<object _jt="IBFSFolder" container="true" type="IBFSFolder"></object>'''

        data = {'IBIRS_action' : 'put',
                'IBIRS_object' : object
                }

        # add the CSRF token value to the body (data) of the request
        if self.IBIWF_SES_AUTH_TOKEN is not None:
            data['IBIWF_SES_AUTH_TOKEN'] = self.IBIWF_SES_AUTH_TOKEN


        url = '%s://%s:%s/ibi_apps/rs/ibfs/EDA/%s/%s' % (self.protocol,
                                                         self.host, 
                                                         self.port,
                                                         node_name, 
                                                         app_name)

        return self.request(method = method, url = url, data = data)



    #------------[ WebFOCUS Reporting Server: list applications ] -------------

    def rs_list_applications(self, node_name = 'EDASERVE'):
        '''WebFOCUS Reporting Server. Listing Applications.'''
        
        method = 'get'

        params = {'IBIRS_action' : 'get'}
       
        url = '%s://%s:%s/ibi_apps/rs/ibfs/EDA/%s' % (self.protocol,
                                                      self.host, 
                                                      self.port, 
                                                      node_name)
        
        return self.request(method = method, url = url, params = params)



    #----------[ WebFOCUS Reporting Server: list application files ] ----------

    def rs_list_application_files(self, node_name = 'EDASERVE', app_name = ''):
        '''WebFOCUS Reporting Server. Listing Files Within an Application.'''
        
        method = 'get'

        params = {'IBIRS_action' : 'get'}
       
        url = '%s://%s:%s/ibi_apps/rs/ibfs/EDA/%s/%s' % (self.protocol,
                                                         self.host, 
                                                         self.port, 
                                                         node_name, 
                                                         app_name)
        
        return self.request(method = method, url = url, params = params)



# ///////////////////////////////// [ Main ]//////////////////////////////////

if __name__ == '__main__':

    session = Session()
    
    r = session.mr_signin( protocol='http',
                           host='localhost',
                           port= '8080', 
                           user='admin', 
                           password='admin')


    # test with a method
    # retval = session.ex_sa_list_groups_with_users()
    
