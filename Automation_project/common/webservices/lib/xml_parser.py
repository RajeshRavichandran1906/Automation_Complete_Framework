import xml.etree.ElementTree as ET

class XmlParser:
    
    def __init__(self, response_xml_value):
        
        self.root = ET.fromstring(response_xml_value)
    
    def get_ibfsrpc_attribute_value(self, attribute):
        """
        Description : Return the <ibfsrpc> tag attribute value.
        :Usage - get_ibfsrpc_attribute_value('returncode')
        """
        if attribute in self.root.attrib:
            return self.root.attrib[attribute]
        erro_msg = '[{0}] attribute not found in <ibfsrpc> tag.'.format(attribute)
        raise KeyError(erro_msg)
    
    def get_xml_tags_attrib(self, tags_obj, excluded_keys=[]):
        """
        Description : Return the tags attributes as list.
        :param - excluded_keys : dictionary key to remove from attributes,
        """
        actual_attribs = [tag.attrib for tag in tags_obj]
        [actual_attrib.pop(key) for actual_attrib in actual_attribs for key in excluded_keys if key in actual_attrib]
        return actual_attribs
    
    def get_xml_node_attributes(self, node_objects, ignore_keys=[], match_case_keys=[]):
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