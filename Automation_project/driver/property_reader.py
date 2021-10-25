from configparser import ConfigParser
from configparser import NoOptionError
import sys

if __name__ == "__main__":
    #parameters from the outside
    property_file=sys.argv[1]
    key=sys.argv[2]

    #java properties files don't have sections, fix that here
    section = 'DEFAULT'
    dummy_header = '[' + section + ']\n' 
    with open(property_file, 'r') as input_file:
        new_content = dummy_header + input_file.read()
    with open(property_file, 'w') as file:
        file.write(new_content)
    
    #get the value of interest
    parser = ConfigParser()
    parser.read(property_file) 
    default_value = "The requested key does not exist in the properties file [" + key + "]."
    end = ''
    try:
        value = parser.get(section, key)
    except NoOptionError:
        value = default_value
    print(value, end)