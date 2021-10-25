from unittest import TestCase
from .log import Log

class Assertions:
    
    failures = []
    
    @staticmethod
    def assertEqual(expected, actual, msg):
        
        try:
            TestCase().assertEqual(expected, actual)
            log_msg = msg + ' : PASSED'
            print(log_msg)
            Log().Verification(log_msg)
        except AssertionError:
            log_msg = msg + ' : FAILED : ' + 'Expected : {0} != Actual : {1}'.format(expected, actual)
            Assertions.failures.append(log_msg)
            print(log_msg)
            Log().VerificationFailure(log_msg)
    
    @staticmethod
    def assertListEqual(expected, actual, msg):
        
        try:
            TestCase().assertListEqual(expected, actual)
            log_msg = msg + ' : PASSED'
            print(log_msg)
            Log().Verification(log_msg)
        except AssertionError as error_msg:
            log_msg = msg + ' : FAILED : ' + str(error_msg)
            Assertions.failures.append(log_msg)
            print(log_msg)
            Log().VerificationFailure(log_msg)

class XMLAssertions:
    
    def __init__(self, xml_root_object, xml_refence_name):
        
        self._xml_root_ = xml_root_object
        self._name_ = xml_refence_name
        
    def assertAttributesEqual(self, node_xpath, expected_attrib, step_num, ignore_keys=[], match_case=False):
        """
        Description : Check whether actual attributes and expected attributes equal.
        Condition : Expected {key : value} == Actual {key : value}
        :param - ignore_keys : Unwanted attribute key name to remove from actual attribute. 
        :param - match_case : Unwanted attribute key name to remove from actual attribute. 
        """
        node_object = self.__find_xml_node_by_xpath_(node_xpath)[0]
        match_case_key = expected_attrib.keys() if match_case else []
        actual_attributes = self._get_xml_node_attributes_([node_object], ignore_keys, match_case_key)[0]
        msg = 'STEP {0} : Verify [{1}] node attributes'.format(step_num, node_xpath)
        Assertions.assertEqual(expected_attrib, actual_attributes, msg)
        
    def assertAttributesNotEqual(self):
        """
        Description : Check whether actual attributes and expected attributes not equal.
        Condition : Expected {key : value} != Actual {key : value}
        :param - ignore_keys : Unwanted attribute key name to remove from actual attribute. 
        """
    
    def assertAttributesIn(self, node_xpath, expected_attrib, step_num):
        """
        Description : Check whether actual attributes contains expected attributes.
        Condition : Expected {key2 : value} in Actual {key1 : value, key2 : value}
        :param - ignore_keys : Unwanted attribute key name to remove from actual attribute. 
        """
        node_object = self.__find_xml_node_by_xpath_(node_xpath)[0]
        actual_attributes = self._get_xml_node_attributes_([node_object])[0]
        msg = 'STEP {0} : Verify [{1}] node contains {2} attributes'.format(step_num, node_xpath, expected_attrib)
        try:
            TestCase().assertDictContainsSubset(expected_attrib, actual_attributes)
            log_msg = msg + ' : PASSED'
            print(log_msg)
            Log().Verification(log_msg)
        except AssertionError as error_msg:
            log_msg = msg + ' : FAILED : ' + str(error_msg)
            Assertions.failures.append(log_msg)
            print(log_msg)
            Log().VerificationFailure(log_msg)
            
    def assertAttributesNotIn(self):
        """
        Description : Check whether actual attributes not contains expected attributes.
        Condition : Expected {key2 : value} not in Actual {key1 : value, key2 : value}
        :param - ignore_keys : Unwanted attribute key name to remove from actual attribute. 
        """
    
    def assertAttributesListEqual(self, node_xpath, expected_attribs, step_num, ignore_keys=[], match_case=False):
        """
        Description : Check whether actual attributes list and expected attributes equal.
        Condition : Expected [{key1 : value}, {key2 : value}] == Actual [{key1 : value}, {key2 : value}]
        :param - ignore_keys : Unwanted attribute key name to remove from actual attribute. 
        """
        node_objects = self.__find_xml_node_by_xpath_(node_xpath)
        match_case_key = list(expected_attribs[0].keys()) if match_case else []
        actual_attribs = self._get_xml_node_attributes_(node_objects, ignore_keys, match_case_key)
        msg = 'STEP {0} : Verify [{1}] node attributes list'.format(step_num, node_xpath)
        Assertions.assertListEqual(expected_attribs, actual_attribs, msg)
        
    def assertAttributesListNotEqual(self):
        """
        Description : Check whether actual attributes list and expected attributes not equal.
        Condition : Expected [{key1 : value}, {key2 : value}] != Actual [{key1 : value}, {key2 : value}]
        :param - ignore_keys : Unwanted attribute key name to remove from actual attribute. 
        """
    
    def assertAttributesListIn(self, node_xpath, expected_attribs, step_num, ignore_keys=[], match_case=False):
        """
        Description : Check whether expected attributes list in actual attributes list.
        Condition : Expected [{key1 : value}, {key4 : value}] in Actual [{key1 : value}, {key2 : value}, {key3 : value}, {key4 : value}]
        :param - ignore_keys : Unwanted attribute key name to remove from actual attribute. 
        """
        node_objects = self.__find_xml_node_by_xpath_(node_xpath)
        match_case_key = list(expected_attribs[0].keys()) if match_case else []
        actual_attribs = self._get_xml_node_attributes_(node_objects, ignore_keys, match_case_key)
        missing_attrib = None
        temp_actual_attribs = actual_attribs.copy() 
        for expected_attrib in expected_attribs:
            if expected_attrib in temp_actual_attribs:
                temp_actual_attribs.pop(temp_actual_attribs.index(expected_attrib))
            else:
                missing_attrib = expected_attrib
        msg = 'STEP {0} : Verify {1} attributes in [{2}] node'.format(step_num, expected_attribs, node_xpath)
        if missing_attrib == None:
            log_msg = msg + ' : PASSED'
            print(log_msg)
            Log().Verification(log_msg)
        else:
            log_msg = msg + ' : FAILED : {0} not found in {1}'.format(missing_attrib, actual_attribs)
            Assertions.failures.append(log_msg)
            print(log_msg)
            Log().VerificationFailure(log_msg)
        
    def assertAttributesListNotIn(self, node_xpath, expected_attribs, step_num):
        """
        Description : Check whether expected attributes list not in actual attributes list.
        Condition : Expected [{key1 : value}, {key4 : value}] not in Actual [{key1 : value}, {key2 : value}, {key3 : value}, {key4 : value}]
        :param - ignore_keys : Unwanted attribute key name to remove from actual attribute. 
        """
        node_objects = self.__find_xml_node_by_xpath_(node_xpath)
        actual_attribs = self._get_xml_node_attributes_(node_objects)
        match_attrib = set()
        for expected_attrib in expected_attribs:
            for actual_attrib in actual_attribs:
                match_attrib = set(expected_attrib.items()).intersection(actual_attrib.items())
                if len(match_attrib) >0 :
                    break
        msg = 'STEP {0} : Verify {1} attributes not in [{2}] node'.format(step_num, expected_attribs, node_xpath)
        if len(match_attrib) == 0:
            log_msg = msg + ' : PASSED'
            print(log_msg)
            Log().Verification(log_msg)
        else:
            log_msg = msg + ' : FAILED : {0} found in {1}'.format(match_attrib, actual_attribs)
            Assertions.failures.append(log_msg)
            print(log_msg)
            Log().VerificationFailure(log_msg)
            
    def __find_xml_node_by_xpath_(self, node_xpath):
        
        node_objects = self._xml_root_.findall(node_xpath)
        if node_objects == []:
            error_msg = "[{0}] node xpath not exists in [{1}] xml".format(node_xpath, self._name_)
            raise Exception(error_msg)
        return node_objects
    
    def _get_xml_node_attributes_(self, node_objects, ignore_keys=[], match_case_keys=[]):
        """
        Description : Return the xml node attributes as list
        :param : ignore_keys - Unwanted key name to remove from node attributes.
        :param : match_case_keys - Remove all keys from node attributes except match case keys
        :Node : Can't pass ignore_keys and match_case_keys at same time. We can pass either ignore_keys or match_case_keys
        :Usage1 : get_xml_node_attributes(node_objects, ignore_keys=['index'])
        :Usage2 : get_xml_node_attributes(node_objects, match_case_keys=['index'])
        """
        if isinstance(ignore_keys, list) and isinstance(match_case_keys, list):
            if ignore_keys !=[] and match_case_keys !=[]:
                raise BlockingIOError("Can't pass ignore_keys and match_case_keys at same time.")
            node_attributes = [node.attrib.copy() for node in node_objects]
            (ignore_keys != []) and [attribute.pop(key) for attribute in node_attributes for key in ignore_keys if key in attribute]
            (match_case_keys != []) and [attribute.pop(key) for attribute in node_attributes for key in list(attribute.keys()) if key not in match_case_keys]
            return node_attributes
        else:
            raise TypeError("ignore_keys and match_case_keys should be list")