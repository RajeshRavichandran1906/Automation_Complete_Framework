'''
Created on Apr 15, 2019

@author: ml12793

@description: create HTML test result page 
'''

import re
import xml.etree.ElementTree as ET
from datetime import datetime

class Case_Result(object):
    
    @staticmethod
    def parse_xml(folder):
        case = re.search('C[0-9]+', folder).group(0)
        tree = ET.parse('./' + folder + '/' + case + '.xml')
        root = tree.getroot()
        for system_out in root.iter('system-out'):
            system_out_text = system_out.text
        lst = system_out_text.split('\n')
        steps = [s for s in lst if 'Step' in s]       
        try:
            for error in root.iter('error'):
                error_text = error.text
            if 'Step' in error_text and '- FAILED.' in error_text:
                error_step = error_text[error_text.index('Step'):error_text.index('- FAILED.')+len('- FAILED.')]
            else:
                error_step = 'Unexpected failure...'
            steps.append(error_step)
        except:
            pass
        return steps
    
    @staticmethod
    def generate_html(folder):
        case = re.search('C[0-9]+', folder).group(0)
        steps = Case_Result.parse_xml(folder)

        html = open('./' + folder + '/' + case + '.html', 'w')
        html_start = """
                    <!DOCTYPE html>
                    <html>
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <style>
                    * {
                    box-sizing: border-box;
                    }
                    p{
                        color: green;
                    }
                    .pErr{
                        color: red;
                    }
                    img{
                    width: 100%;
                    }
                    #time{
                        color: black;
                    }
                    </style>
                    <body>
                    """
        html_end = """
                    </body>
                    </html>
                   """
        html.write(html_start)
        html.write('<h1>' + case + '</h1>')
        
        for step in steps:
            if 'Step' in step:
                try:
                    try:
                        step_number=re.search(r'\d+.\d+', step).group()
                    except AttributeError:
                        step_number=re.search(r'\d+', step).group()
                except AttributeError:
                    step_number=re.search(r'[x|X]', step).group()
                if '- PASSED.' in step:
                    p = '<p id="' + step_number + '">' + step + '</p>'
                    img = '<img src = "' + case + '_' + step_number + '.png"/>'
                else:
                    p = '<p class="pErr">' + step + '</p>'
                    img = '<img src = "test_' + case + '_' + step_number + '.png"/>'
            else:
                p = '<p class="pErr">Unexpected failure occurs before reaching next verification point...</p>'
                img = '<img src = "test_' + case + '_' + step_number + '.png"/>'
            html.write(p)
            html.write(img)
        html.write('<p id="time">' + str(datetime.now().strftime('%m/%d/%Y %H:%M:%S')) + '<p>')    
        html.write(html_end)
        html.close()
