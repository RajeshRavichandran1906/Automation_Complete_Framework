'''
Created on May 10, 2019

@author: vpriya
Testcase Name : Chart with 1 image and 1 pictogram
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8792536
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import designer_chart
from common.lib import utillity 

class C8792536_TestClass(BaseTestCase):
    
    def test_C8792536(self):
        
        
        def verify_pictogram_image_location(elem,expected_list_loc,custom_msg):
            picto_gram_elem=utill_obj.validate_and_get_webdriver_object(elem,"pictogram_elem or image_elem")
            picto_gram_loc=utill_obj.get_object_screen_coordinate(picto_gram_elem)
            actual_list_loc=list(picto_gram_loc.values())
            utill_obj.asequal(actual_list_loc,expected_list_loc,custom_msg)
            
        expected_d_values=['M247.51404,152.40266139.05781,71.800946c0.80268,-12.4518451.32473,-40.2562660.85468,-45.417599-3.94034,-43.266462-31.23018,-24.6301193-31.48335,-5.320367-0.0693,5.281361-1.01502,32.598388-1.10471,50.836622L0.2842717,154.375620,180.19575l110.50058,-50.482393.99332,80.29163-32.042567,22.93816-0.203845,16.8969342.271772,-11.595660.008,0.139542.71311,10.91879-0.50929,-16.88213-32.45374,-22.399032.61132,-80.35205111.35995,48.50611-0.73494,-25.77295z']
        run_parent_css="#jschart_HOLD_0"
        
        """
        Testcase case objects
        """
        designer_chart_obj=designer_chart.Designer_Chart(self.driver)
        utill_obj=utillity.UtillityMethods(self.driver)
        
        """
        Step 1:Run C8792536.fex with API call
        domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_LAUNCH&BIP_folder=IBFS:/WFC/Repository/P292_S29835/G730863/&BIP_item=C8792536.fex
        """
        designer_chart_obj.run_designer_chart_using_api("C8792536")
        designer_chart_obj.verify_x_axis_title_in_preview(["CAR"], parent_css=run_parent_css,msg="Step:01:01")
        designer_chart_obj.verify_y_axis_title_in_preview(["RETAIL_COST"], parent_css=run_parent_css,msg="Step:01:02")
        designer_chart_obj.verify_x_axis_label_in_preview(['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH'], parent_css=run_parent_css,msg="Step 01:03")
        designer_chart_obj.verify_y_axis_label_in_preview(['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K'], parent_css=run_parent_css,msg="Step:01:04")
        utill_obj.verify_picture_using_sikuli("C8792536_step01.05.png", "Step 01.05 : verify the pictogram")
        utill_obj.verify_picture_using_sikuli("C8792536_step01.06.png", "Step 01.06 : verify the pictogram")
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview("rect[class='annotation!s0!']", "bar_blue", parent_css=run_parent_css,msg="Step 01:06 verify the pictogram border colour")
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview("path[class='placeholderannotation!s0!']", "red", parent_css=run_parent_css,msg="Step 01:07 verify the pictogram path colour")
        picto_gram_elem=utill_obj.validate_and_get_webdriver_object("[class='chartAnnotationsGroup'] rect +path","pictogram_elem or image_elem")
        d_values=utill_obj.get_attribute_value(picto_gram_elem,"d")
        path_d_list=list(d_values.values())
        actual_d_value=[x.replace(' ', '') for x in path_d_list]
        utill_obj.asequal(actual_d_value,expected_d_values,"Step 01:08 verify the path values for pictogram")
        
        """
        Step 2:Logout using API (without saving)
        http://machine:port/alias/service/wf_security_logout.jsp
        """
       
if __name__ == '__main__':
    unittest.main()