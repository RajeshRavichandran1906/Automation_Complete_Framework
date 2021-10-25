
import unittest
from configparser import ConfigParser
import os, time
from common.lib.basetestcase import BaseTestCase
from common.lib import html_dom_utility, core_utility
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class C5587427_TestClass(BaseTestCase):
        
    def test_C5587427(self):
        driver=self.driver
        htmlObject= html_dom_utility.Html_Dom_Utility(driver)
        coreUtilObject=core_utility.CoreUtillityMethods(driver)

        ''''local variables'''
        RS_PATH = "/rs/ibfs/WFC/Repository/"
        server = coreUtilObject.parseinitfile('clientid')
        node = coreUtilObject.parseinitfile('httpport')
        context = coreUtilObject.parseinitfile('wfcontext')
        userId = coreUtilObject.parseinitfile('mrid')
        #upload_html= coreUtilObject.parseinitfile('upload_html')
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
        
        fileName_GA="FIPS_ST_REF_US_COUNTIES_TERRAIN8201mGA"
        fileName_SP="FIPS_ST_REF_US_COUNTIES_TERRAIN8201mSP"
        html_file_GA= os.path.join(os.getcwd(),fileName_GA+".html" )
        html_file_SP= os.path.join(os.getcwd(),fileName_SP+".html")
        fex_url_GA=wf_url+RS_PATH+domain_folder+"/"+GA+"/"+fileName_GA+".fex"
        html_url_GA=wf_url+RS_PATH+domain_folder+"/"+SP+"/"+fileName_GA+".htm"
        
        classTag='class'
        divTag="div"
        rectTag="rect"
        
        layer_locator= "layerId_1_layer"
        zoom_css="div[id$=_zoom_slider]"
        scale_css="div[class^=scalebar_bottom-right]"
        layer_css="div[class^=TableOfContentsButton]"
        
        colorScaleLegend_title= "colorScaleLegend-title"
        colorScaleaxis_labels="colorScaleaxis-labels!"
        legendColor="legendColor"
        scaleBar="esriScalebarLabel esriScalebarLineLabel esriScalebarSecondNumber"
        layer_name="USA"
        
        '''================== test scripts========================'''
        htmlObject.wf_login(wf_url,userId)

        'read 8201MGA html'
        get_html_GA= htmlObject.get_html_dom(html_url_GA)
        htmlObject.save_html_dom(get_html_GA, html_file_GA)
        read_html_GA = htmlObject.read_html_dom(html_file_GA)

        '''read 8201MSP html:  Open Fex from 8201mGA; Run it ; save the fex as HTML file named 8201m_SP.'''
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
        legend_title_GA = htmlObject.get_html_text_attributes(read_html_GA,classTag, colorScaleLegend_title)
        legend_title_SP = htmlObject.get_html_text_attributes(read_html_SP,classTag, colorScaleLegend_title)
        self.assertEqual(legend_title_GA,legend_title_SP,msg="Expected legend does not match!")
        print("Legend Title 8201M_GA = {}.".format(legend_title_GA))
        print("Legend Title 8201M_SP = {}.".format(legend_title_SP))

        '''verify legend texts'''
        legend_GA = htmlObject.get_html_text_attributes(read_html_GA,classTag, colorScaleaxis_labels)
        legend_SP = htmlObject.get_html_text_attributes(read_html_SP,classTag, colorScaleaxis_labels)
        self.assertEqual(legend_GA,legend_SP,msg="Expected legend does not match!")
        print("Legend 8201M_GA = {}.".format(legend_GA))
        print("Legend 8201M_SP = {}.".format(legend_SP))

        '''verify legend color scale '''
        legend_scale_GA=htmlObject.get_key_value(read_html_GA,rectTag,legendColor)
        legend_scale_SP=htmlObject.get_key_value(read_html_SP,rectTag,legendColor)
        self.assertEqual(legend_scale_GA,legend_scale_SP,msg="Expected color scales do not match!")
        print("Legend color scale 8201M_GA = {}.".format(legend_scale_GA))
        print("Legend color scale 8201M_SP = {}.".format(legend_scale_SP))

        '''verify polygon color'''
        get_map_polygon_color_82018mGA=htmlObject.get_key_value(read_html_GA,"path","riser!s0!g")
        get_map_polygon_color_82018mSP=htmlObject.get_key_value(read_html_GA,"path","riser!s0!g")
        self.assertEqual(get_map_polygon_color_82018mGA,get_map_polygon_color_82018mSP,msg="Expected colors for map polygons do not match!")
        print("Legend color GA = {0} & SP = {1}.".format(get_map_polygon_color_82018mGA,get_map_polygon_color_82018mSP))

        '''Verify layers'''
        tagList=htmlObject.get_tag_list(read_html_GA, divTag, classTag, "toc-text")
        layer_list_GA=htmlObject.strip_text(tagList,layer_name,startswith='startswith')
        tagList=htmlObject.get_tag_list(read_html_SP, divTag, classTag, "toc-text")
        layer_list_SP=htmlObject.strip_text(tagList,layer_name,startswith='startswith')
        self.assertEqual(layer_list_GA,layer_list_SP,msg="Expected layers do not match!")
        print("Layers 8201M_GA = {}.".format(layer_list_GA))
        print("Layers 8201M_SP = {}.".format(layer_list_SP))

        '''Verify scalebar '''
        tagList=htmlObject.get_tag_list(read_html_GA, divTag, classTag, scaleBar)
        scaleBar_GA=[]
        for i in tagList:
            x=i.text.strip(' \n')
            scaleBar_GA.append(x)
        print("Layers 8201M_GA = {}.".format(scaleBar_GA))
        tagList=htmlObject.get_tag_list(read_html_SP, divTag, classTag, scaleBar)
        scaleBar_SP=[]
        for i in tagList:
            x=i.text.strip(' \n')
            scaleBar_SP.append(x)
        print("Layers 8201M_SP= {}.".format(scaleBar_SP))
        self.assertEqual(scaleBar_GA,scaleBar_SP,msg="scale units do not match!")

        '''Run 8201MGA html'''
        print(">>> Opening 8201MGA to gather all UI location {0}.".format(html_url_GA))
        driver.get(html_url_GA)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, layer_locator)))

        zoom=driver.find_element_by_css_selector(zoom_css)
        zoomSlider_location_GA=coreUtilObject.get_web_element_coordinate(zoom)

        scale=driver.find_element_by_css_selector(scale_css)
        scale_location_GA=coreUtilObject.get_web_element_coordinate(scale)

        layer=driver.find_element_by_css_selector(layer_css)
        layer_location_GA=coreUtilObject.get_web_element_coordinate(layer)


        '''Run 8201MSP html'''
        print(">>> Opening 8201MSP to gather all UI location {0}.".format(fex_url_GA))
        driver.get(fex_url_GA)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, layer_locator)))

        zoom=driver.find_element_by_css_selector(zoom_css)
        zoomSlider_location_SP=coreUtilObject.get_web_element_coordinate(zoom)

        scale=driver.find_element_by_css_selector(scale_css)
        scale_location_SP=coreUtilObject.get_web_element_coordinate(scale)


        layer=driver.find_element_by_css_selector(layer_css)
        layer_location_SP=coreUtilObject.get_web_element_coordinate(layer)


        ''' >>>> Verify the contents between 8201MGA vs SP  <<<<'''
        print("Zoom slider location 8201M_GA = {}.".format(zoomSlider_location_GA))
        print("Zoom slider location 8201M_SP = {}.".format(zoomSlider_location_SP))
        self.assertEqual(zoomSlider_location_GA,zoomSlider_location_SP,msg="Zoom UI locations do not match!")

        print("Scale UI location 8201M_GA = {}.".format(scale_location_GA))
        print("Scale UI location 8201M_SP = {}.".format(scale_location_SP))
        self.assertEqual(scale_location_GA,scale_location_SP,msg="Scale locations do not match!")

        print("Layers UI 8201M_GA = {}.".format(layer_location_GA))
        print("Layers UI 8201M_SP = {}.".format(layer_location_SP))
        self.assertEqual(layer_location_GA,layer_location_SP,msg="Layer UI locations do not match!")


        

if __name__ == '__main__':
    unittest.main()