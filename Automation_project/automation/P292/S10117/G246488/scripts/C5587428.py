'''
@TC ID: http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5587428
@Author: Jesmin A.
'''
import unittest
import os
from common.lib.basetestcase import BaseTestCase
from common.lib import html_dom_utility , core_utility
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class C5587428_TestClass(BaseTestCase):
   
    
    def test_C5587428(self):
        driver=self.driver
        htmlObject= html_dom_utility.Html_Dom_Utility(driver)
        coreUtilObject=core_utility.CoreUtillityMethods(driver)        
        
        ''''local variables'''
        RS_PATH= "/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/"            
        server = coreUtilObject.parseinitfile('clientid')
        node = coreUtilObject.parseinitfile('httpport')
        context = coreUtilObject.parseinitfile('wfcontext')
        userId = coreUtilObject.parseinitfile('mrid')
        wf_url=server+":"+node+context           
        domain_folder= coreUtilObject.parseinitfile('project_id')
        #subfolder_GA= coreUtilObject.parseinitfile('suite_id') 
        #subfolder_SP= coreUtilObject.parseinitfile('suite_id2') 
        approot = coreUtilObject.parseinitfile('approot')
        os.chdir(approot)
        release = coreUtilObject.parseinitfile('release')
        GA=eval(release)[0]
        print("Release: "+GA)
        SP=eval(release)[1]
        print("Release: "+SP)
        
        fileName_GA="US_CITY_ST_ABB_USA_MED_AGE2014-8201mGA"
        fileName_SP="US_CITY_ST_ABB_USA_MED_AGE2014-8201mSP"  
        html_file_GA=os.path.join(os.getcwd(),fileName_GA+".html" )         
        html_file_SP=os.path.join(os.getcwd(),fileName_SP+".html")
        fex_url_GA=wf_url+RS_PATH+domain_folder+"/"+GA+"&BIP_item="+fileName_GA+".fex"
        html_url_GA=wf_url+RS_PATH+domain_folder+"/"+SP+"&BIP_item="+fileName_GA+".htm"
        
        classTag='class'
        divTag="div"
        
        poly1_css= "layerId_1_layer"
        zoom_css="div[id$=_zoom_slider]"
        scale_css="div[class^=scalebar_bottom-right]"
        layer_css="div[class^=TableOfContentsButton]"
        legend_title="legend-title"
        legend_lable="legend-labels!s"
        sizeLegend_title="sizeLegend-title"
        sizeLegend_labels="sizeLegend-labels!s0!"
        riser="riser!s0!g"
        scalebar="esriScalebarLabel esriScalebarLineLabel esriScalebarSecondNumber"
        '''================== test scripts========================'''
        htmlObject.wf_login(wf_url,userId) 
        
        'read 8201MGA html'
        get_html_GA= htmlObject.get_html_dom(html_url_GA) 
        htmlObject.save_html_dom(get_html_GA, html_file_GA)
        read_html_GA = htmlObject.read_html_dom(html_file_GA)
 
        'read SP html'
        ''' Open Fex from GA; Run it ; save the fex as HTML file named xyz_SP.'''
        get_html_page_SP= htmlObject.get_html_dom(fex_url_GA)    
        htmlObject.save_html_dom(get_html_page_SP, html_file_SP) 
        read_html_SP = htmlObject.read_html_dom(html_file_SP)
        
        ''' Verify file in approot '''    
        try:
            os.path.isfile(html_file_GA)
        except FileNotFoundError as e:
            print(str(e))
            
        try:
            os.path.isfile(html_file_SP)
        except FileNotFoundError as e:
            print(str(e))
          
        '''verify legends Title'''         
        legend_title_GA = htmlObject.get_html_text_attributes(read_html_GA,classTag, legend_title)
        legend_title_SP = htmlObject.get_html_text_attributes(read_html_SP,classTag, legend_title)         
        self.assertEqual(legend_title_GA,legend_title_SP,msg="Expected legend does not match!")
        print("Legend Title 8201M_GA = {}.".format(legend_title_GA))
        print("Legend Title 8201M_SP = {}.".format(legend_title_SP))
            
        '''verify legend texts'''
        legend_GA = htmlObject.get_html_text_attributes(read_html_GA,classTag, legend_lable)
        legend_SP = htmlObject.get_html_text_attributes(read_html_SP,classTag, legend_lable)         
        self.assertEqual(legend_GA,legend_SP,msg="Expected legend does not match!")
        print("Legend text 8201M_GA = {}.".format(legend_GA))
        print("Legend text 8201M_SP = {}.".format(legend_SP))
          
        '''Verify Budget Unit & Size '''    
        legend_scale_GA=htmlObject.get_html_text_attributes(read_html_GA,classTag,sizeLegend_title) 
        legend_scale_SP=htmlObject.get_html_text_attributes(read_html_SP,classTag,sizeLegend_title)
        self.assertEqual(legend_scale_GA,legend_scale_SP,msg="Expected Budget Unit legend do not match!") 
        print("Size Legend title 8201M_GA = {}.".format(legend_scale_GA))        
        print("Size Legend title 8201M_SP = {}.".format(legend_scale_SP))
        
        legend_scale_GA=htmlObject.get_html_text_attributes(read_html_GA,classTag,sizeLegend_labels) 
        legend_scale_SP=htmlObject.get_html_text_attributes(read_html_SP,classTag,sizeLegend_labels)
        self.assertEqual(legend_scale_GA,legend_scale_SP,msg="Expected Budget Unit value do not match!") 
        print("Size Legend Value 8201M_GA = {}.".format(legend_scale_GA))        
        print("Size Legend Value 8201M_SP = {}.".format(legend_scale_SP))
                
        '''verify polygon color'''
        get_map_polygon_color_82018mGA=htmlObject.get_key_value(read_html_GA,"circle",riser)
        get_map_polygon_color_82018mSP=htmlObject.get_key_value(read_html_SP,"circle",riser)
        self.assertEqual(get_map_polygon_color_82018mGA,get_map_polygon_color_82018mSP,msg="Expected colors for map polygons do not match!")   
        print("Legend color GA = {0} & SP = {1}.".format(get_map_polygon_color_82018mGA,get_map_polygon_color_82018mSP))        

        '''Verify layers'''
        tagList=htmlObject.get_tag_list(read_html_GA, divTag, classTag, "toc-text")
        layer_list_GA=htmlObject.strip_text(tagList,"USA",startswith='startswith')
        tagList=htmlObject.get_tag_list(read_html_SP, divTag, classTag, "toc-text")
        layer_list_SP=htmlObject.strip_text(tagList,"USA",startswith='startswith')
        self.assertEqual(layer_list_GA,layer_list_SP,msg="Expected layers do not match!")
        print("Layers 8201M_GA = {}.".format(layer_list_GA))
        print("Layers 8201M_SP = {}.".format(layer_list_SP))
           
        '''Verify scalebar '''
        tagList=htmlObject.get_tag_list(read_html_GA, divTag, classTag, scalebar)
        scaleBar_GA=[]
        for i in tagList:
            x=i.text.strip(' \n')   
            scaleBar_GA.append(x)
        print("Scalebar 8201M_GA = {}.".format(scaleBar_GA))
        tagList=htmlObject.get_tag_list(read_html_SP, divTag, classTag, scalebar)
        scaleBar_SP=[]
        for i in tagList:
            x=i.text.strip(' \n')   
            scaleBar_SP.append(x)
        print("Scalebar 8201M_SP = {}.".format(scaleBar_SP))
        self.assertEqual(scaleBar_GA,scaleBar_SP,msg="scale units do not match!")
        
        #====  This section tested GUI elements that needs to be tested live ==== 
                
        '''Run 8201MGA html to gather UI locations'''
        print(">>>>>>>>> Open 8201MGA WF: ' {0}'\n".format(html_url_GA))
        driver.get(html_url_GA)
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID,poly1_css)))

        zoom=driver.find_element_by_css_selector(zoom_css)
        zoomSlider_location_GA=coreUtilObject.get_web_element_coordinate(zoom)
        
        scale=driver.find_element_by_css_selector(scale_css)
        scale_location_GA=coreUtilObject.get_web_element_coordinate(scale)
        
        layer=driver.find_element_by_css_selector(layer_css)
        layer_location_GA=coreUtilObject.get_web_element_coordinate(layer)
         
        
        '''Run 8201MSP html'''
        print(">>>>>>>>> Open  8201MSP WF and gather gather UI locations :' {0}'\n".format(fex_url_GA))
        driver.get(fex_url_GA)
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID,poly1_css)))

        zoom=driver.find_element_by_css_selector(zoom_css)
        zoomSlider_location_SP=coreUtilObject.get_web_element_coordinate(zoom)
        
        scale=driver.find_element_by_css_selector(scale_css)
        scale_location_SP=coreUtilObject.get_web_element_coordinate(scale)
     
        layer=driver.find_element_by_css_selector(layer_css)
        layer_location_SP=coreUtilObject.get_web_element_coordinate(layer) 
        
        '''                  Verify the contents between 8201MGA VS. 8201MSP                   '''
        
        print("Zoom slider location 8201M_GA = {}.".format(zoomSlider_location_GA))
        print("Zoom slider location 8201M_SP = {}.".format(zoomSlider_location_SP))
        self.assertEqual(zoomSlider_location_GA,zoomSlider_location_SP,msg="Zoom UI locations do not match!")
        
        print("Scale UI location 8201M_GA = {}.".format(scale_location_GA))        
        print("Scale UI location 8201M_SP = {}.".format(scale_location_SP))
        self.assertEqual(scale_location_GA,scale_location_SP,msg="Scale locations do not match!")
         
        print("Layers UI location 8201M_GA = {}.".format(layer_location_GA))
        print("Layers UI location 8201M_SP = {}.".format(layer_location_SP))
        self.assertEqual(layer_location_GA,layer_location_SP,msg="Layer UI locations do not match!")
   
        
if __name__ == '__main__':
    unittest.main()