from common.lib import utillity
from common.lib.base import BasePage
from common.locators.infoassist_locators import InfoassistLocators
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, StaleElementReferenceException
import time    
from common.locators.as_ribbon_locators import AsRibbonLocators    
import pyautogui    
import sys 
if sys.platform == 'linux':
    from pykeyboard import PyKeyboard
    pykeyboard = PyKeyboard()
else:
    from pynput.keyboard import Controller          

class IaMainPage(BasePage):
    """ Inherit attributes of the parent class = Baseclass """
    def __init__(self, driver):
        super(IaMainPage, self).__init__(driver)  



#Function 3: Returns the Title of main page page will be used to validate in Script
    def is_title_mathces(self):
        return "InfoAssist+" in self.driver.title

#Function 4: Click on the calculation and select detail or summary
    def calculation(self, types = 'Detail (Define)'):
        """
        :param type: type should be define or summary
        :return:
        @author = Gobinath
        """
        cal = self.driver.find_element(*InfoassistLocators.calculation)
        time.sleep(3)
        cal.click()
        option = self.driver.find_element_by_xpath("//td[contains(text(), '"+types+"')]")
        WebDriverWait(self.driver, 25).until(lambda driver: option.is_displayed())
        option.click()

#Function 5: Select the field format option in detail format window or summary format window
    def field_format(self, option = 'Date'):
        """
        :param option: Default param = Date , if you give another format it will override
               date_format :
        :return:
        @author = Gobinath
        """
        field = self.driver.find_element_by_xpath("//div[contains(text(), '"+option+"')]")
        WebDriverWait(self.driver, 25).until(lambda driver: field.is_displayed())
        field.click()

#Function 6: Select Visual by clicking on Change dropdown
    def choose_chart_type(self, option = 'stacked_bar'):
        """
        :param option: Default param stacked_bar and other params =tablegrid, chart_bar, chart_line, chart_area,
         stacked_area, chart_pie, chart_pie_ring, chart_scatter, x_y_plots_bubble, matrix_marker, treemap, gauge,
         choropleth, bubblemap, special_marked_mapped
         @author = Kiruthika/Gobi
        """
        WebDriverWait(self.driver, 70).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[id*=Chart_1]')))
        chart_type = self.driver.find_element(*InfoassistLocators.ChangeChartType)
        time.sleep(3)
        chart_type.click()
        time.sleep(3)
        change = self.driver.find_element_by_xpath("// img[contains( @ src, '"+option+"_32.png')]")
        change.click()

#Function 7: Add Fields using the search field and clicking ENTER to add
    def add_field_doubleclick(self, option):
        """
        :param option: Revenue or Product,Category
        @author = Kiruthika
        """
        time.sleep(5)
        send = self.driver.find_element(*InfoassistLocators.SearchField)
        send.send_keys(option)
        time.sleep(5)
        field_xpath = "//*[normalize-space(text())= '" + option + "']/img[2]"
        self.driver.find_element_by_xpath(field_xpath).send_keys(keys.Keys.TAB)
        selected = self.driver.find_element(*InfoassistLocators.Selected_Field)
        current_selected_field=selected.text
        for x in range(0, 10):
            if (current_selected_field != option):
                self.driver.find_element_by_xpath(field_xpath).send_keys(keys.Keys.ARROW_DOWN)
                newly_selected = self.driver.find_element(*InfoassistLocators.Selected_Field)
                current_selected_field = newly_selected.text
            else:
                self.driver.find_element_by_xpath(field_xpath).send_keys(keys.Keys.ENTER)
                WebDriverWait(self.driver, 60).until(lambda driver: self.driver.find_elements_by_css_selector("#MAINTABLE_wbody1_f > svg > g.chartPanel "))
                break
        send.clear()
        time.sleep(5)


# Function 8: Verify x and y axis labels of chart
    def verification_x_y_label(self,xaxis_value,yaxis_value,text):
        """
        :param xaxis_value: Product Category
        yaxis_value: Gross Profit
        eg: verification_x_y_label('Product Category','Gross Profit',"Step 10: Verify x,y label")
        @author = Kiruthika
        """
        xaxis = self.driver.find_element_by_xpath("//*[contains(@class,'xaxis')and contains(@class,'title')]")
        yaxis = self.driver.find_element_by_css_selector("g > text[class='yaxis-title']")
        utillity.UtillityMethods.asequal(self,xaxis.text, xaxis_value, text+": X Label")
            # assert(xaxis.text == xaxis_value)
        utillity.UtillityMethods.asequal(self,yaxis.text, yaxis_value, text+": Y Label")
            # assert(yaxis.text == yaxis_value)

#Function 9: Verify Titles in Grid

    def verification_grid_title(self, rowTitle, text):
       """
       :param Title: list = ['Sale Year', 'Sale Quarter', 'Revenue']
       eg: verification_grid_title(list,'Step 04: Verify field titles')
       @author = Sindhuja & Kiruthika
       """
       
       run_data = []
       for tr in self.driver.find_elements_by_css_selector('svg > g.chartPanel > g > g.rowTitle'):
           tds = tr.find_elements_by_tag_name('text')
           if tds:
               run_data.extend([td.text for td in tds])
       for tr in self.driver.find_elements_by_css_selector("svg > g.chartPanel > g > g.colHeaderScroll"):
           tds = tr.find_elements_by_tag_name('text')
           if tds:
               run_data.extend([td.text for td in tds])
       utillity.UtillityMethods.asequal(self,rowTitle, run_data, text)
         

# Function 10 : Click ia options < will click ia and select option based on the suggestion
    def click_ia(self, *args, **kwargs):
        """
        :param kwargs: file_name='Sample' (should be passed at the end)
        args: Save, Close, app_options, Run
                        Example for saving file, 
                        ia.click_ia('Save', 'click_save', file_name='Sample')
        :return:
        __author = gobinath thiyagarajan

        """
        self.driver.find_element(*InfoassistLocators.ia).click()
        app_menu = self.driver.find_element(*InfoassistLocators.app_menu)
        WebDriverWait(self.driver, 60).until(lambda driver: app_menu.is_displayed())
        if 'Save' in args:
            self.driver.find_element(*InfoassistLocators.save).click()
            open_window = self.driver.find_element(*InfoassistLocators.open_window)
            WebDriverWait(self.driver, 25).until(lambda driver: open_window.is_displayed())
            fileinput = self.driver.find_element(*InfoassistLocators.input_filename)
            if 'file_name' in kwargs:
                fileinput.send_keys(kwargs['file_name'])
                time.sleep(3)#after developer to see fex name typed
            if 'click_save' in args:
                sv = self.driver.find_element(*InfoassistLocators.save_fex)
                sv.click()
                try:
                    already_exists = self.driver.find_element_by_xpath("//div[contains(text(), 'already exists')]")
                    if already_exists.is_displayed():
                        self.driver.find_element_by_xpath("//div[contains(text(), 'already exists')]").send_keys(keys.Keys.TAB + keys.Keys.ENTER)
                except NoSuchElementException:
                    return False
                print(kwargs['file_name']+' saved successfully')
            if 'cancel' in args:
                cancel_save = self.driver.find_element(*InfoassistLocators.cancel)
                cancel_save.click()
        elif 'Save_As' in args:
            self.driver.find_element(*InfoassistLocators.save_as).click()
            self.driver.find_element(*InfoassistLocators.save).click()
            open_window = self.driver.find_element(*InfoassistLocators.open_window)
            WebDriverWait(self.driver, 25).until(lambda driver: open_window.is_displayed())
            fileinput = self.driver.find_element(*InfoassistLocators.input_filename)
            if 'file_name' in kwargs:
                fileinput.send_keys(kwargs['file_name'])
                time.sleep(3)#after developer to see fex name typed
            if 'click_save' in args:
                open_file = self.driver.find_element(*InfoassistLocators.save_fex)
                open_file.click()
                try:
                    yes = self.driver.find_element_by_xpath('//*div[.="Yes"]')
                    if yes.is_displayed():
                        yes.click()
                except NoSuchElementException:
                    return False
            if 'cancel' in args:
                cancel_save = self.driver.find_element(*InfoassistLocators.cancel)
                cancel_save.click()
        elif 'Open' in args:
            self.driver.find_element(*InfoassistLocators.open).click()
            self.driver.find_element(*InfoassistLocators.save).click()
            open_window = self.driver.find_element(*InfoassistLocators.open_window)
            WebDriverWait(self.driver, 25).until(lambda driver: open_window.is_displayed())
            fileinput = self.driver.find_element(*InfoassistLocators.input_filename)
            if 'file_name' in kwargs:
                fileinput.send_keys(kwargs['file_name'])
                time.sleep(3)#after developer to see fex name typed
            if 'open_file' in args:
                open_file = self.driver.find_element(*InfoassistLocators.save_fex)
                open_file.click()
            if 'cancel' in args:
                cancel_save = self.driver.find_element(*InfoassistLocators.cancel)
                cancel_save.click()
        elif 'New' in args:
            self.driver.find_element(*InfoassistLocators.new).click()
        elif 'Run' in args:
            self.driver.find_element(*InfoassistLocators.run).click()
        elif 'Close' in args:
            self.driver.find_element(*InfoassistLocators.close).click()
        elif 'app_options' in args:
            self.driver.find_element(*InfoassistLocators.app_option).click()

       
# Function 11: Verify Filter Pane
    def verification_filter_pane(self, filter_Pane, text):
        """
            :param filter_Pane: filter pane fields (eg: Product,Category or Revenue)
            eg: ia.verification_filter_pane("Product,Category","Step10: Verify Filter Pane")
            @author = Sindhuja
            """ 
        filterPane=self.driver.find_element(*InfoassistLocators.filterPane)
        filterValues = filterPane.text
        utillity.UtillityMethods.asin(self, filter_Pane, filterValues, text)
            # assert filter_Pane in filterValues

# Function 12: Verify Filter Prompt title and values
    def verification_filter_prompt_preview(self,prompt_num,prompt_values, text):
        """
            :param prompt_num: indicates filter prompt number (1 -> first filter prompt, 2-> second filter prompt)
            eg: ia.verification_filter_prompt_preview("1", "Product,Category", "Step 10: Verify Filter prompt in preview")
            prompt_values: indicates filter prompt title and filter values
            @author = Sindhuja
            """
        promptNum=self.driver.find_element_by_xpath("//div[contains(@id,'ar_Prompt_"+prompt_num+"')]")
        filterPrompt=promptNum.text
        utillity.UtillityMethods.asin(self, prompt_values,filterPrompt, text )
        # assert prompt_values in filterPrompt, "Not present"

		
#Function 13: Add Fields using the search field and right click ans select first menu and second menu
    def add_field_right_click_menu_submenu(self, option, first_menu, *args,**kwargs):
        """
        :param option: Revenue or Product,Category 
        first_menu: Sum or Filter or Add To Query
        second_menu: Rows or Columns or Vertical Axis or Horizontal Axis or Size or Color or Color By or Tooltip
        args = 'verify' or 'Grid'
		eg: ia.add_field_right_click_menu_submenu('Sale,Year','Add To Query',second_menu='Rows',format='YYMDy')
		eg: ia.add_field_right_click_menu_submenu('Sale,Year','Add To Query','Grid',second_menu='Rows',format='YYMDy') if Grid
        @author = Kiruthika & Sindhuja
        """
        action = ActionChains(self.driver)
        send =self.driver.find_element(*InfoassistLocators.SearchField)
        WebDriverWait(self.driver, 10).until(lambda driver: send.is_displayed())
        send.send_keys(option)
        if send.get_attribute("value") != option:
            send.send_keys(option)
        elif send.get_attribute("value") == '':
            time.sleep(8)
        field_xpath = "//*[normalize-space(text())= '" + option + "']/img[2]"
        self.driver.find_element_by_xpath(field_xpath).send_keys(keys.Keys.TAB)
        selected = self.driver.find_element(*InfoassistLocators.Selected_Field_text)
        selected_image = self.driver.find_element(*InfoassistLocators.Selected_Field_image)
        current_selected_field=selected.text
        for x in range(0, 10):
            if (current_selected_field != option):
                self.driver.find_element_by_xpath(field_xpath).send_keys(keys.Keys.ARROW_DOWN)
                newly_selected = self.driver.find_element(*InfoassistLocators.Selected_Field_text)
                current_selected_field = newly_selected.text
            elif(current_selected_field == option):
                if 'format' in kwargs:
                    field_xpath = self.driver.find_element_by_xpath("//*[normalize-space(text())= '" + option + "']/img[2]")
                    action = ActionChains(self.driver)
                    action.move_to_element(field_xpath).perform()
                    time.sleep(2)
                    tooltip = self.driver.find_element_by_xpath(
                        "//*[normalize-space(text())='" + option + "']/../../tr[*]/td[normalize-space(text())='Format:']/../../..")
                    new = tooltip.text
                    # print("initial tooltip", new)
                    for j in range(0, 10):
                        if kwargs['format'] not in new:
                            field_xpath = self.driver.find_element_by_xpath("//*[normalize-space(text())= '" + option + "']/img[2]")
                            field_xpath.send_keys(keys.Keys.ARROW_DOWN)
                            selected_field = self.driver.find_element_by_xpath("//*[contains(@class,'selected')]/td")
                            # print("selected", selected_field.text)
                            for i in range(0, 7):
                                if selected_field.text != option:
                                    field_xpath = self.driver.find_element_by_xpath(
                                        "//*[normalize-space(text())= '" + selected_field.text + "']/img[2]")
                                    field_xpath.send_keys(keys.Keys.ARROW_DOWN)
                                    selected_field = self.driver.find_element_by_xpath("//*[contains(@class,'selected')]/td")
                                    # print("selected", selected_field.text)
                                elif selected_field.text == option:
                                    time.sleep(7)
                                    elements = self.driver.find_elements_by_xpath(
                                        "//*[normalize-space(text())= '" + option + "']/img[2]")
                                    # print("elements", len(elements))
                                    a = len(elements) - 1
                                    try:
                                        elements[a].click()
                                    except ElementNotVisibleException:
                                        print("except")
                                    elements = self.driver.find_elements_by_xpath(
                                        "//*[normalize-space(text())= '" + option + "']/img[2]")
                                    elements[len(elements) - 1].click()
                                    time.sleep(2)
                                    elements2 = self.driver.find_elements_by_xpath(
                                        "//*[normalize-space(text())='" + option + "']/../../tr[*]/td[normalize-space(text())='Format:']/../../..")
                                    # print("text", elements2[len(elements2) - 1].text)
                                    new = elements2[len(elements2) - 1].text
                                    break
                    elements = self.driver.find_elements_by_xpath(
                        "//*[normalize-space(text())= '" + option + "']/img[2]")
                    # field_xpath=elements[len(elements) - 1]
                    field_xpath = "//*[normalize-space(text())= '" + option + "']/img[2]"
                self.driver.find_element_by_xpath(field_xpath).send_keys(keys.Keys.SHIFT + keys.Keys.F10)
                self.driver.find_element_by_xpath(field_xpath).send_keys(keys.Keys.ARROW_DOWN)
                ele_first_menu = self.driver.find_element(*InfoassistLocators.Initial_RC_Menu)
                first_menu_xpath = "//div[contains(@style,'inherit')]/div/table/tbody/tr[*]/td[contains(text(),'"+first_menu+"')]"
                WebDriverWait(self.driver, 10).until(lambda driver: ele_first_menu.is_displayed())
                current_selected_first_menu = ele_first_menu.text
                for y in range(0, 3):
                    if (current_selected_first_menu != first_menu):
                            self.driver.find_element_by_xpath(field_xpath).send_keys(keys.Keys.ARROW_DOWN)
                            newly_selected_first_menu = self.driver.find_element(*InfoassistLocators.Selected_RC_Menu)
                            current_selected_first_menu = newly_selected_first_menu.text
                if(current_selected_first_menu == first_menu):
                    new = self.driver.find_element_by_xpath(
                        "//div[contains(@style,'inherit')]/div/table/tbody/tr[*]/td[contains(text(),'" + first_menu + "')]/../td/img")
                    new.send_keys(keys.Keys.ENTER)
                    time.sleep(3)
                    if (first_menu == "Add To Query"):
                        self.driver.find_element_by_xpath(first_menu_xpath).send_keys(keys.Keys.ARROW_DOWN)
                        if 'Grid' in args:
                            ele_second_menu1 = self.driver.find_element(*InfoassistLocators.Initial_RC_Submenu_Grid_img)
                            WebDriverWait(self.driver, 10).until(lambda driver: ele_second_menu1.is_displayed())
                            current_selected_second_menu = ele_second_menu1.text
                        else:
                            ele_second_menu = self.driver.find_element(*InfoassistLocators.Initial_RC_Submenu_img)
                            WebDriverWait(self.driver, 10).until(lambda driver: ele_second_menu.is_displayed())
                            current_selected_second_menu = ele_second_menu.text
                        if 'second_menu' in kwargs:
                            if 'verify' in args:
                                menu = kwargs['second_menu']
                                verify_option = self.driver.find_element_by_xpath(InfoassistLocators.common_xpath.format(menu))
                                try:
                                    if verify_option.is_displayed():
                                        print(''+menu+ 'is displayed')
                                except NoSuchElementException:
                                    print(''+menu+' is not displayed ')
                            else:
                                for z in range(0, 9):
                                    if (current_selected_second_menu != kwargs['second_menu']):
                                        new.send_keys(keys.Keys.ARROW_DOWN)
                                        newly_selected_second_menu = self.driver.find_element(*InfoassistLocators.Selected_RC_Submenu)
                                        current_selected_second_menu = newly_selected_second_menu.text
                                if (current_selected_second_menu == kwargs['second_menu']):
                                        new_second = self.driver.find_element(*InfoassistLocators.Selected_RC_Submenu)
                                        new_second.send_keys(keys.Keys.ENTER)
                                        send.clear()
                                        time.sleep(3)
                        break
                    send.clear()
                    time.sleep(2)
                    break

#Function 14: Verify chart values
    def chart_values_validation(self, type, s, g, value01, value02, text, **kwargs):
        """
        :param
        type : bar or bubble, s : numbers, g : numbers, **kwargs : value05 = "Product Subcategory" text: Step 10: chart value verify
        :param condition='notin'
        eg: chart_values_validation("bar", "18", "0", "Product Category", "Camcorder", "Step 10: chart value verify",value03="Revenue",
        value04="$41,970,570.97", value05='Product Subcategory:', value06='Handheld', condition='notin')
        @author :   Kiruthika
        """
        action = ActionChains(self.driver)
        if type == 'bar':
            var = 'mbar'
            WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "g > text[class='yaxis-title']")))
            move_element = self.driver.find_element_by_css_selector("g > text[class='yaxis-title']")
            action.move_to_element(move_element).perform()
        if type == 'bubble':
            var = 'mmarker'
        bar_riser = self.driver.find_element_by_xpath("//*[contains(@class,'riser!s"+str(s)+"!g"+str(g)+"!"+var+"')]")
        WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(@class,'riser!s"+str(s)+"!g"+str(g)+"!"+var+"')]")))
        time.sleep(5)
        action.move_to_element(bar_riser).perform()
        time.sleep(2)
        table1_value = self.driver.find_element(*InfoassistLocators.tooltip1_name).text
        table2_value = self.driver.find_element(*InfoassistLocators.tooltip1_value).text
        table = [table1_value, table2_value]
        value = [value01, value02]
        y=2
        if 'value03' in kwargs:
            table3_value = self.driver.find_element(*InfoassistLocators.tooltip2_name).text
            table.extend([table3_value])
            value.extend([kwargs['value03']])
        if 'value04' in kwargs:
            table4_value = self.driver.find_element(*InfoassistLocators.tooltip2_value).text
            table.extend([table4_value])
            value.extend([kwargs['value04']])
            y = 4
        if 'value05' in kwargs :
            table5_value = self.driver.find_element(*InfoassistLocators.tooltip3_name).text
            table.extend([table5_value])
            value.extend([kwargs['value05']])
        if 'value06' in kwargs:
            table6_value = self.driver.find_element(*InfoassistLocators.tooltip3_value).text
            table.extend([table6_value])
            value.extend([kwargs['value06']])
            y = 6

        for i in range(0,len(value)):
            if 'condition' in kwargs:
                for j in range(1,y,1):
                    utillity.UtillityMethods.as_notin(self,value[j], table[j], text + '-' + value[j] + ' present in ' + table[j])
            else:
                utillity.UtillityMethods.asin(self,value[i], table[i], text+ '-'+value[i]+ ' not in '+table[i])
        time.sleep(4)


#Function 15: Hover over the bar chart and click filter, hover over any riser

    def default_tooltip_menu(self, a,b, option,*args,**kwargs):
        """
        :param a: 1 or 2..  b: 1 or 2...
        :param option: Filter chart
        Usage: ia.default_tooltip_menu('2','10','Sales Branch','bar',Drill='Drill Down')
        ia.default_tooltip_menu("0","1","Filter Chart","bubble")
        ia.default_tooltip_menu("0","1","Drill Down","bar")
        :param args: @author: Sindhuja,Kiruthika& Gobinath Date: 13 May
        :return:
        """
        action = ActionChains(self.driver)
        if 'bar' in args:
            bar_riser = self.driver.find_element_by_css_selector(" rect.riser\\21 s"+str(a)+"\\21 g"+str(b)+"\\21 mbar")
            action.move_to_element(bar_riser).perform()
            time.sleep(3)
        if 'bubble' in args:
            bubble = self.driver.find_element_by_css_selector("circle.riser\\21 s"+str(a)+"\\21 g"+str(b)+"\\21 mmarker")
            action.move_to_element(bubble).perform()
            time.sleep(1)
        if 'Drill' in kwargs:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, InfoassistLocators.drill.format(option))))
            option_to = self.driver.find_element_by_xpath(InfoassistLocators.drill.format(option))
            option_to.click()
            submenu = self.driver.find_element_by_xpath(InfoassistLocators.multi_drill.format(option, kwargs['Drill']))
            submenu.click()
        else:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, InfoassistLocators.filter.format(option))))
            option_to = self.driver.find_element_by_xpath(InfoassistLocators.filter.format(option))
            option_to.click()

# Function 16: Click Filter button and change filter operator values

    def filter_operator_values(self, *args, **kwargs):
        """
        :param args: clickOperatorDropdown or notEqualto or equalto or sortDropdown or sortOption or uncheck
                            ShowPrompt or clickOK or pass all this values in arguments
        :param kwargs: filter prompt values (eg: checkvalues = "Camcorder" or "Accessories")
            (always call this ata the end of the argument)
        :return:
          __author = Sindhuja
        """

        if 'clickOperatorDropdown' in args:
            self.driver.find_element(*InfoassistLocators.operatorDropdown).click()
        if 'notEqualto' in args:
            self.driver.find_element(*InfoassistLocators.changeOperator_notequal).click()
        if 'equalto' in args:
            self.driver.find_element(*InfoassistLocators.changeOperator_equal).click()
        if 'checkvalues' in kwargs:
            value= kwargs['checkvalues']
            check = self.driver.find_element_by_xpath("//div[starts-with(@id, 'CheckBoxItem')]/div[contains(text(),'"+value+"')]")
            action = ActionChains(self.driver)
            action.move_to_element(check).perform()
            check.click()
        if 'sortDropdown' in args:
            self.driver.find_element(*InfoassistLocators.sortDropdown).click()
        if 'sortOption' in args:
            self.driver.find_element(*InfoassistLocators.sortOption).click()#by default sort is "ascending"
        if 'uncheckShowPrompt' in args:
            self.driver.find_element(*InfoassistLocators.uncheckShowPrompt).click()
        if 'clickOK' in args:
            self.driver.find_element(*InfoassistLocators.clickOK).click()
        if 'search' in args:
            searchBox=self.driver.find_element(*InfoassistLocators.searchBox)
            value = kwargs['search']
            searchBox.send_keys(value)


#Function 17: Verify Chart type

    def verification_chart_type(self,chart_type, text):
        """
            :param chart_type: Grid1 or Bar1...
            eg: verification_chart_type(Grid1, "Step 10: Verify Chart Type")
            @author = Sindhuja
            """

        chartType= self.driver.find_element_by_xpath("//div[contains(@id,'BoxLayoutMiniWindow')]/div/div[contains(text(),'"+chart_type+"')]")
        utillity.UtillityMethods.asequal(self, chartType.text, chart_type, text)
       
# Function 18: Click Filter button for Range window and changing filter values
    def filter_operator_range_values(self,*args,**kwargs):
        """
            :param **kwargs = filter prompt values (ex: 2011, Camcorder)
            *args = any of the condition values (ex: notEqualto, equalto)
            eg: ia.filter_operator_range_values('uncheckShowPrompt',From='21')
            @author = Kiruthika
            """
        if 'clickOperatorDropdown' in args:
            self.driver.find_element(*InfoassistLocators.range_operatorDropdown).click()
        if 'notEqualto' in args:
             self.driver.find_element(*InfoassistLocators.changeOperator_notequal).click()
        if 'equalto' in args:
            self.driver.find_element(*InfoassistLocators.changeOperator_equal).click()
        if 'GTequalto' in args:
            self.driver.find_element(*InfoassistLocators.changeOperator_GT_orequalto).click()
        if 'LTequalto' in args:
            self.driver.find_element(*InfoassistLocators.changeOperator_LT_orequalto).click()
        if 'To' in kwargs:
            to = self.driver.find_element_by_xpath("//div[contains(@id, 'avfToValue')]/input")
            to.clear()
            value = kwargs['To']
            to.send_keys(value)
        if 'Range' in args:
            self.driver.find_element(*InfoassistLocators.changeOperator_Range).click()
        if 'checkvalues' in kwargs:
             value= kwargs['checkvalues']
             check = self.driver.find_element_by_xpath("//div[starts-with(@id, 'CheckBoxItem')]/div[contains(text(),'"+value+"')]")
             action = ActionChains(self.driver)
             action.move_to_element(check).perform()
             check.click()
        if 'From' in kwargs:
            ran = self.driver.find_element_by_xpath("//div[contains(@id, 'avfFromValue')]/input")
            ran.clear()
            value = kwargs['From']
            ran.send_keys(value)
        if 'sortDropdown' in args:
             self.driver.find_element(*InfoassistLocators.sortDropdown).click()
        if 'sortOption' in args:
             self.driver.find_element(*InfoassistLocators.sortOption).click()#by default sort is "ascending"
        if 'sortAsc' in args:
            self.driver.find_element(*InfoassistLocators.sort_Asc).click()
        if 'uncheckShowPrompt' in args:
             self.driver.find_element(*InfoassistLocators.uncheckShowPrompt).click()#default  Show Prompt is checked
        if 'clickOK' in args:
            self.driver.find_element_by_id("avFilterOkBtn").click()
        if 'Starting_Date' in kwargs:
            start = self.driver.find_element(*InfoassistLocators.Starting_Date)
            start.click()
            start.clear()
            start.send_keys(kwargs['Starting_Date'])
        if 'Ending_Date' in kwargs:
            end = self.driver.find_element(*InfoassistLocators.Ending_Date)
            end.click()
            end.clear()
            end.send_keys(kwargs['Ending_Date'])
		
# Function 19: Verify Filter Prompt title and values in runtime
    def verification_filter_prompt_runtime(self,promptNum,values, text):
        """
            :param promptNum = filter prompt number (11 -> represents first filter, 22 -> second filter , 33 -> third filter)
            eg: (ia.verification_filter_prompt_runtime("11","Product,Category", "Step 10: Verify Quer Pane"))
            values = Product,Category or Accessories or [All] (filter prompt title and values)
            @author = Sindhuja
            """
        filterPrompt=self.driver.find_element_by_xpath("//div[@id='LOBJPrompt_"+promptNum+"']")
        runtimeFilterPrompt=filterPrompt.text
        utillity.UtillityMethods.asin(self, values, runtimeFilterPrompt, text)
         
		
# Function 20: Verify Query Pane
    def verification_query_pane(self,values , text):
        """
            :param values = Product,Category or Model.. (ia.verification_query_pane("Model", "Step 10: Verify Quer Pane"))
            @author = Sindhuja
            """
        queryPane = self.driver.find_element(*InfoassistLocators.query_pane)
        queryPaneValues=queryPane.text
        utillity.UtillityMethods.asin(self, values, queryPaneValues, text)
        # assert values in queryPaneValues, "Not present"

# Function 21: Verify Filter Pane checkbox checked values
    def verification_filter_pane_checkbox(self, value, text):
        """
            :param value: filter pane checked values (eg: ia.verification_filter_pane_checkbox(['EMEA', 'North America'], "Step10: Verify Filter Pane Checkbox")
            @author = Kiruthika Date : 12May
        """
        total = []
        total.extend(value)
        for i in range(0,len(total)):
            equal = self.driver.find_element_by_xpath("//input[@value='"+total[i]+"']")
            utillity.UtillityMethods.asequal(self, equal.get_attribute("checked"), 'true', text)
            # assert equal.get_attribute("checked") == 'true', "The value "+total[i]+" is not checked in filter pane"

# Function 22: Verify Color label (legend label)
    def verification_color_label(self, value, text):
        """
            :param value: Color label value (legend) (eg: ia.verification_color_label('Product Subcategory', "Step06: Verify Color Legend")
            @author = Kiruthika Date : 12May
        """
        color_text = self.driver.find_element_by_xpath("//*[@class='legend-title']").text
        utillity.UtillityMethods.asequal(self, value, color_text, text)
        # assert value == color_text, "Color legend not matched"

# Function 23: Insert Chart or Grid or Text
    def insert(self, option):
        """
            :param option: chart_bar or tablegrid or text (eg: ia.verification_color_label('Product Subcategory')
            @author = Kiruthika Date : 13May
            """
        time.sleep(2)
        drop_down = self.driver.find_element_by_xpath("//*[@id='HomeInsertVis']/div/div[contains(@class,'drop-down-arrow')]")
        drop_down.click()
        time.sleep(1)
        change = self.driver.find_element_by_xpath("// img[contains( @ src, '"+option+"_16.png')]")
        change.click()
        

# Function 24 : Verification of Grid, Rows and Measure separately

    def grid_values_verify(self, **kwargs):
        """
        Keyword 1:
        Grid Values verification for first three values and last three values based on the given data this function
        verify, if keyword arg given as rows = ['Computer', 'Camcorder', 'State'] function will automatically count the
        list of values verify each values present in rows with run_time list
        Keyword 2:
        keyword argument measure needs to given to get the measure field text and verify the data correct as per given list
        Keyword 3:
        if  Keyword 2 given as golast and if more value present in grid , it will have scroll bar and needs to be
        scrolled to view last few values present in grid table
        sample verify rows and go to last grid value :
        data01 = ['Cam', 'Computers', 'Ram']
        ia.grid_value_verify(rows=data01, go_last='600')
        600 value is y axis value to drag - caller needs to give this value

        Full usage :
        data01 = ['2011', '1', '1', 'EMEA', 'Europe', 'Czech Republic', 'Denmark', 'Accessories', 'Camcorder',
                   'Computers', 'Media Player', 'Stereo Systems']
        data02 = ['$168.00', '$31,185.71', '$25,575.20', '$7,382.95', '$72,997.86']
        data03 = ['SA-Span' , 'Argentina']
        data04 = ['$2,186.77', '$1,1603.95', '$490.00', '$1,073.94']
        ia.grid_value_verify(rows=data01, measure=data02, go_last='670',rows_last=data03, measure_last= data04 )
        :param kwargs:
        :return:
        Future implementation get all visible table values create run time csv table and compare with two csv files
        __author = Gobinath Thiyagarajan
        """
        if 'rows' in kwargs:
            runtime_list = []
            for tr in self.driver.find_elements(*InfoassistLocators.rows):
                tds = tr.find_elements_by_tag_name('text')
                if tds:
                    runtime_list.append([td.text for td in tds])

            for x in range(0, len(kwargs['rows'])):
                assert kwargs['rows'][x] in runtime_list[0]

        if 'measure' in kwargs:
            runtime_measure_list = []
            for tr in self.driver.find_elements(*InfoassistLocators.measure_grid):
                tds = tr.find_elements_by_tag_name('text')
                if tds:
                    runtime_measure_list.append([td.text for td in tds])

            for x in range(0, len(kwargs['measure'])):
                assert kwargs['measure'][x] in runtime_measure_list[0]
        if 'go_last' in kwargs:
            actions = ActionChains(self.driver)
            source = self.driver.find_element(*InfoassistLocators.slider_grid)
            actions.drag_and_drop_by_offset(source, 0, kwargs['go_last']).perform()
            if 'rows_last' in kwargs:
                runtime_list02 = []
                for tr in self.driver.find_elements(*InfoassistLocators.rows):
                    tds = tr.find_elements_by_tag_name('text')
                    if tds:
                        runtime_list02.append([td.text for td in tds])

                for x in range(0, len(kwargs['rows_last'])):
                    assert kwargs['rows_last'][x] in runtime_list02[0]

            if 'measure_last' in kwargs:
                runtime_last = []
                for tr in self.driver.find_elements(*InfoassistLocators.rows):
                    tds = tr.find_elements_by_tag_name('text')
                    if tds:
                        runtime_last.append([td.text for td in tds])

                for x in range(0, len(kwargs['rows'])):
                    assert kwargs['rows'][x] in runtime_last[0]

    def verification_row_values_after_filter(self,filter_values,text):        
        row_lables = self.driver.find_element_by_xpath(".//*[contains(@class,'rowLabels')]")
        row_values = row_lables.text
        utillity.UtillityMethods.asin(self,filter_values,row_lables.text,text)
        
#Function 25 : Function to click prompt options (Equals/ Not Equals/ Dropdown/ List...)
    def change_prompt_options(self,prompt_num,selectMenu):
        """

        :param prompt_num: 1,2,3,...(filter prompt number) (ia.change_prompt_options("1","Dropdown (Single Select)"))
        selectMenu: Equals, Not Equals,Dropdown (Single Select), List (Single Select)..
        author: Sindhuja & Gobinath Date: 23 May
        """
        promptNum = self.driver.find_element_by_xpath("//div[contains(@id,'ar_Prompt_"+prompt_num+"')]")
        action = ActionChains(self.driver)
        action.move_to_element(promptNum).perform()
        move_prompt=self.driver.find_element_by_xpath("//div[contains(@id,'ar_Prompt_"+prompt_num+"')]/div/div/table/tbody/tr/td/div/span")
        action.move_to_element(move_prompt).perform()
        time.sleep(1)        
        self.driver.find_element(*InfoassistLocators.prompt_dropdown).click()
        option = self.driver.find_element_by_xpath(InfoassistLocators.prompt_option_dropdown.format(selectMenu))
        option.click()

# Function 26 : Verify Grid row values based on the tooltip of measure(implemented for single measure in Grid) - measure tooltip value will be converted to integer and check values

    def verification_grid_row_value(self, row, a, text, **kwargs):
        """
        :param row: 0
        :param a: ["Sale Year:  2011","Product Category:  Accessories","Revenue:  5039297.570000065"]
        :param kwargs: go_last='670'
        :param text: "Step10: verify"
        eg: a = ["Sale Year:  2011","Product Category:  Accessories","Revenue:  5039297.570000065"]
         ia.verification_grid_row_value('0', a, "Step 10: Verify 1st Row Value")
         ia.verification_grid_row_value('41', a, "Step 10: Verify last Row Value", go_last='670')
        :return:
        @author = Kiruthika Date : 27May2016
        """

        if 'go_last' in kwargs :
                actions = ActionChains(self.driver)
                source = self.driver.find_element(*InfoassistLocators.slider_grid)
                actions.drag_and_drop_by_offset(source, 0, kwargs['go_last']).perform()
        if row:
            grid_row = self.driver.find_element_by_xpath("//*[contains(@class,'row"+str(row)+"')]")
            action = ActionChains(self.driver)
            action.move_to_element(grid_row).perform()
            time.sleep(1)
            row1_tbody = self.driver.find_element_by_xpath(
            ".//*[@id='tdgchart-tooltip']/div/ul/li[1]/table/tbody")
            WebDriverWait(self.driver, 200).until(
                EC.presence_of_element_located((By.XPATH, ".//*[@id='tdgchart-tooltip']/div/ul/li[1]/table/tbody")))
            action.move_to_element(row1_tbody).perform()
            tooltip = row1_tbody.text
            for i in range(0, len(a)):
                utillity.UtillityMethods.asin(self, a[i], tooltip, text + '-' + a[i] + ' not in tooltip menu')
            action.move_to_element(self.driver.find_element_by_css_selector("svg > g.chartPanel > g > g.rowTitle"))
            time.sleep(5)


#Function 27 : Click run menu icon and options
    def clickRunMenuOption(self,*args):
        """

        :param args: click icon,grid, reset, remove filter (ia.clickRunMenuOption("click icon","grid"))
        :author: Sindhuja Date: 24 May
        """
        if 'click icon' in args:
            self.driver.find_element(*InfoassistLocators.run_menu_icon).click()
        if 'grid' in args:
            self.driver.find_element(*InfoassistLocators.grid_icon).click()
        if 'reset' in args:
            self.driver.find_element(*InfoassistLocators.reset_icon).click()
        if 'remove filter' in args:
            self.driver.find_element(*InfoassistLocators.removeFilter_icon).click()

#Function 28: Verify grid icon values
    def verifyRunMenuOption_gridValues(self,rowNum,rowValue,text):
        """

        :param rowNum: 1,2,3,.. (ia.verifyRunMenuOption_gridValues("1","Product Category Revenue"))
        :param rowValue: Product Category Revenue/ Accessories $129,608,338.53
        :author : Sindhuja Date : 25 May
        """
        selectRow = self.driver.find_element_by_css_selector("tbody > tr:nth-child(1) > td > table > tbody > tr:nth-child("+rowNum+")")
        value = selectRow.text
        assert rowValue in value
        utillity.UtillityMethods.asin(self, rowValue, value, text + '-' + value + 'not in run menu grid')

		
#Function 29 : Perform default lasso on united states for bubble map and select the default lasso option menu
    """
    Perform lasso and select lasso menu selection
	__author = gobinath thiyagarajan
    """

    def lasso_tooltip_menu_xy_bubble_map(self, riser, x, y, menu):
        """
        :param riser:
        :param x:
        :param y:
        :param menu:
        :return:
         ia.lasso('5', '250', '250', 'Filter Chart')
		 For bubble map 

        """
        action = ActionChains(self.driver)
        pan = self.driver.find_element(*InfoassistLocators.pan)
        pan.click()
        time.sleep(5)
        riser1 = str(riser)
        source = self.driver.find_element_by_css_selector(InfoassistLocators.lasso.format(riser1))
        action.drag_and_drop_by_offset(source, x, y).perform()
        time.sleep(4)
        option = self.driver.find_element_by_xpath(InfoassistLocators.lasso_options.format(menu))
        option.click()			

#Function 30a : Click options displayed after lasso 

    def lasso_tooltip_menu(self, menu):
        """
        :param menu:Filter Chart or Exclude from Chart
        eg: ia.lasso_tooltip_menu('Filter Chart')
        @author = Kiruthika Date : 6Jun2016

        """
        action = ActionChains(self.driver)
        time.sleep(1)
        for y in range(1, 4):
            option_to = self.driver.find_element_by_xpath(
                "//*[starts-with(@id,'ibi$tt$')]/span[" + str(y) + "]")
            option_to_value = option_to.text
            if option_to_value in menu:
                try:
                    self.driver.find_element_by_xpath("//*[starts-with(@id,'ibi$tt$')]/span[" + str(y) + "]").click()
                except ElementNotVisibleException:
                    print("click done after exception")
        time.sleep(2)


#Function 30b : Perform default lasso from the given values

    def lasso(self, riser1, riser2, *args,**kwargs):
        """
        :param riser1 eg: s0!g0 [riser\\21 s0\\21 g0 (Starting point of riser, pass the s snd g value from locator)]
        :param riser2 eg:s0!g2 [riser\\21 s0\\21 g0 (Ending point of riser, pass the s snd g value from locator)]
        :param type="line or type="bubble" or type="heatmap"
        eg: ia.lasso(s0!g0,s0!g2, type="bubble")
        eg: ia.lasso('s0!g0!mmarker!r0!c0','s0!g2!mmarker!r0!c0', rowcolumn,type="scatter")
        @author = Kiruthika Date : 8Jun2016

        """
        action = ActionChains(self.driver)
        mbar = 'mmarker'
        if 'type' in kwargs:
            if kwargs['type'] == 'line':
                riser = 'marker'
            if kwargs['type'] == 'bubble' or kwargs['type']=='scatter':
                riser = 'riser'
            if kwargs['type'] == 'heatmap':
                riser='riser'
                mbar='mbar'
        if 'type' not in kwargs:
            WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 
                 "g > text[class='yaxis-title']")))
            move_element = self.driver.find_element_by_css_selector("g > text[class='yaxis-title']")
            action.move_to_element(move_element).perform()
            riser = 'riser'
            mbar = 'mbar'
        if 'rowcolumn' in args:
            WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH,InfoassistLocators.lasso_chart_xpath_rowcolumn.format(riser,riser1))))
            src = self.driver.find_element_by_xpath(InfoassistLocators.lasso_chart_xpath_rowcolumn.format(riser,riser1))
            dest = self.driver.find_element_by_xpath(InfoassistLocators.lasso_chart_xpath_rowcolumn.format(riser,riser2))
        else:
            WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH,InfoassistLocators.lasso_chart_xpath.format(riser,riser1,mbar))))
            src = self.driver.find_element_by_xpath(InfoassistLocators.lasso_chart_xpath.format(riser,riser1,mbar))
            dest = self.driver.find_element_by_xpath(InfoassistLocators.lasso_chart_xpath.format(riser,riser2,mbar))
        action.drag_and_drop(src,dest).perform()

#Function 30c : Perform default lasso from the given values

    def lasso_by_offset(self, riser1,dropx,dropy, *args,**kwargs):
        """
        :param riser1 eg: s0!g0 [riser\\21 s0\\21 g0 (Starting point of riser, pass the s snd g value from locator)]
        :param dropx = -200, dropy = -10
        eg: ia.lasso(s0!g1,-200,10 type="bubble")
        eg: ia.lasso('s0!g0!mmarker!r0!c0', 10,-20,rowcolumn,type="scatter")
        @author = Kiruthika Date : 8Jun2016

        """
        action = ActionChains(self.driver)
        mbar = 'mmarker'
        if 'type' in kwargs:
            if kwargs['type'] == 'line':
                riser = 'marker'
            if kwargs['type'] == 'bubble' or kwargs['type']=='scatter':
                riser = 'riser'
            if kwargs['type'] == 'heatmap':
                riser='riser'
                mbar='mbar'
        if 'type' not in kwargs:
            WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "g > text[class='yaxis-title']")))
            move_element = self.driver.find_element_by_css_selector("g > text[class='yaxis-title']")
            action.move_to_element(move_element).perform()
            riser = 'riser'
            mbar = 'mbar'
        if 'rowcolumn' in args:
            WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH,InfoassistLocators.lasso_chart_xpath_rowcolumn.format(riser,riser1))))
            src = self.driver.find_element_by_xpath(InfoassistLocators.lasso_chart_xpath_rowcolumn.format(riser,riser1))
        else:
            WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH,InfoassistLocators.lasso_chart_xpath.format(riser,riser1,mbar))))
            src = self.driver.find_element_by_xpath(InfoassistLocators.lasso_chart_xpath.format(riser,riser1,mbar))
        action.drag_and_drop_by_offset(src,dropx,dropy).perform()



#Function 31: Verify labels in HeatMap
    def verification_heatmap_labels(self,value1,text):
        """
        
        :param a = ["Product Subcategory","Sale Month"]
        ia.verification_heatmap_labels(a,"Step 05: Verify label values")
        :author: Sindhuja Date: May 31 
        """
        xaxis = self.driver.find_elements_by_css_selector("g > text[class='xaxisOrdinal-title']")
        for x in range(0, 2):
            utillity.UtillityMethods.asequal(self, xaxis[x].text, value1[x], text + ": X Label")
	 
#Function 32: Change filter prompt values
    def change_filter_prompt_checkBoxValue(self,prompt_num,prompt_value_num,*args):
        """

        :param prompt_num: 1, 2, 3 (1 -> indicates first filter prompt number in "runtime")
               prompt_num: 0, 1, 2 (0 -> indicates first filter prompt number in "preview") 
        :param prompt_value_num: 0 or 1 or 2.. (0 -> incidates first prompt value checkbox, 1 -> incidates second prompt value checkbox in "preview"and "runtime")
        :author: Sindhuja Date: June 01
        """

        if 'preview' in args:
            previewPrompt = self.driver.find_element_by_xpath("//input[@id='checkboxLOBJC20"+prompt_num+"_"+prompt_value_num+"']")
            previewPrompt.click()
        if 'runtime' in args:
            runtimePrompt = self.driver.find_element_by_xpath("//input[contains(@id,'checkboxPROMPT_"+prompt_num+"_"+prompt_value_num+"')]")
            runtimePrompt.click()

#Function 33: Verify Query added to Filter pane is editable
    def verification_filterpane_editable(self,title,text):
        """
        :param: title: eg: PRODUCT_SUBCATEG and PRODUCT_CATEGORY
        ia.verification_filterpane_editable("PRODUCT_SUBCATEG and PRODUCT_CATEGORY",'Edit not in Right Click Menu of filter')
        :author: Kiruthika Date: June 1
        """
        edit = self.driver.find_element_by_xpath("//*[@id='qbFilterBox']/div[*]/table/tbody/tr[*]/td[contains(text(),'"+title+"')]/img")
        try:
            edit.click()
        except ElementNotVisibleException:
            edit = self.driver.find_element_by_xpath(
                "//*[@id='qbFilterBox']/div[*]/table/tbody/tr[*]/td[contains(text(),'" + title + "')]/img")
            edit.click()
        edit.send_keys(keys.Keys.SHIFT + keys.Keys.F10)
        time.sleep(2)
        edit.send_keys(keys.Keys.ARROW_DOWN)
        menu = self.driver.find_elements_by_xpath("//td[contains(text(),'Delete')]/..")
        menu_text=menu[len(menu)-1].text
        utillity.UtillityMethods.as_notin(self, 'Edit',menu_text, text)
		
#Function 34 ; Right click Filter pane select given option from it
    def filter_pane_right_click_options(self, title, option):
        """
        param title: eg: PRODUCT_SUBCATEG and PRODUCT_CATEGORY
        :param option:  'Edit', 'Delete'
        :author: Gobinath T 
		usage obj.filter_pane_right_click_options('Product,Category', 'Edit...')
        """
        filter_field = self.driver.find_element_by_xpath("//*[@id='qbFilterBox']/div[*]/table/tbody/tr[*]/td[contains(text(),'"+title+"')]/img")
        try:
            filter_field.click()
        except ElementNotVisibleException:
            filter_field = self.driver.find_element_by_xpath(
                "//*[@id='qbFilterBox']/div[*]/table/tbody/tr[*]/td[contains(text(),'" + title + "')]/img")
            filter_field.click()
        filter_field.send_keys(keys.Keys.SHIFT + keys.Keys.F10)
        time.sleep(2)
        filter_field.send_keys(keys.Keys.ARROW_DOWN)
        menu = self.driver.find_elements_by_xpath(InfoassistLocators.filter_pane_right_click_menus.format(option))
        menu_text=menu[len(menu)-1]
        try:
            menu_text.click()
        except ElementNotVisibleException:
            print('%s clicked'%option)		
			
#Function 35 : Verify tooltip values

    def verification_tooltip_values(self, riser1,a, text,*args,**kwargs):
        """
        :param
        riser1 : s0!g0,  a=["Quantity Sold:  25,666","Revenue:  $6,858,809.70","Model:  GLXYT10716"]
        kwargs : type='bubble' or 'line' (default is bar)
        ia.verification_tooltip_values('s0!g22',a,"Step 07: Hover any bubble ", type='bubble')
        ia.verification_tooltip_values('s0!g22',a,"Step 07: Hover any bar ", condition='notin')
        ia.verification_tooltip_values('s0!g22!mmarker!r0!c0',["Quantity Sold:  25,666"],"Step 07: verify tooltip",'rowcolumn', type='scatter')
        @author : Sindhuja & Kiruthika  Date: June 06
        """
        action = ActionChains(self.driver)
        action1 = ActionChains(self.driver)
        mbar = 'mmarker'
        if 'type' in kwargs:
            if kwargs['type'] == 'line':
                riser = 'marker'
            if kwargs['type'] == 'bubble' or kwargs['type'] == 'scatter':
                riser = 'riser'
            if kwargs['type'] == 'heatmap':
                riser = 'riser'
                mbar = 'mbar'

        if 'type' not in kwargs:
            WebDriverWait(self.driver, 100).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//*[contains(@class,'xaxis')and contains(@class,'title')]")))
            move_element = self.driver.find_element_by_xpath("//*[contains(@class,'xaxis')and contains(@class,'title')]")
            action.move_to_element(move_element).perform()
            riser = 'riser'
            mbar = 'mbar'
        if 'rowcolumn' in args:
            WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH,InfoassistLocators.lasso_chart_xpath_rowcolumn.format(riser,riser1))))
            bar_riser = self.driver.find_element_by_xpath(InfoassistLocators.lasso_chart_xpath_rowcolumn.format(riser,riser1))
        else:    
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, InfoassistLocators.lasso_chart_xpath.format(riser, riser1, mbar))))
            bar_riser = self.driver.find_element_by_xpath(InfoassistLocators.lasso_chart_xpath.format(riser, riser1, mbar))
        # time.sleep(5)
        action1.move_to_element(bar_riser).perform()
        time.sleep(2)
        row1_tbody = self.driver.find_element_by_css_selector(
            "#tdgchart-tooltip > div > ul > li:nth-child(1) > table > tbody")
        try:
            tooltip = row1_tbody.text
            for i in range(0, len(a)):
                if 'condition' in kwargs:
                    for j in range(1, len(a), 1):
                        utillity.UtillityMethods.as_notin(self, a[j], tooltip, text + '-' + a[j] + ' present in tooltip menu')
                else:
                    utillity.UtillityMethods.asin(self, a[i], tooltip, text + '-' + a[i] + ' not in tooltip menu')
            time.sleep(4)
        except StaleElementReferenceException:
            print("excepted")


#Function 36 : Click field item in query pane 
    def click_querypane_field(self, field):	
        """
        :param field: eg: "Product,Category"
        :author: Gobinath T 
        Usage : ia.click_querypane_field('Product,Category')
        """
        querpane=self.driver.find_element_by_xpath(InfoassistLocators.field_querypane.format(field))
        try:
            querpane.click()
        except ElementNotVisibleException:
            print('Element now moved to option')
        q=self.driver.find_element_by_xpath(InfoassistLocators.field_querypane.format(field))
        q.click()
        print('%s field clicked'%field)
			
# Function 37: Verify filter dialog after edit
    def verify_filterPane_edit_values(self,text,*args,**kwargs):
        """
        :param args: "operator", "checkbox", "sort"
        kwargs: "value", "checkedValues", "sortValue"
        Usage: values= ["Camcorder","Computers","Media Player","Stereo Systems","Televisions","Video Production"]
        ia.verify_filterPane_edit_values("checkbox",checkedValues=values)
        :author: Sindhuja Date : June 6
        """
        if "operator"in args:
            operatorValue=self.driver.find_element_by_id("avAlphaOperatorComboBox")
            value1=operatorValue.text
            utillity.UtillityMethods.asin(self, value1, kwargs['value'], text)


        if "checkbox" in args:
            checkbox=[]
            action = ActionChains(self.driver)
            action.move_to_element(self.driver.find_element_by_xpath("//div[@id='avValueGrid']"))
            values = self.driver.find_elements_by_xpath("//div[starts-with(@id,'BiCheckBox')]/input[@checked='true']/..")
            for result in values:
                checkbox.append(result.text)
            utillity.UtillityMethods.asequal(self,checkbox, kwargs['checkedValues'],text)
            
        if "sort" in args:
            sortValue = self.driver.find_element_by_id("avfSortValuesComboBox")
            value2=sortValue.text
            utillity.UtillityMethods.asin(self, value2, kwargs['sortValue'], text)
			
#Function 38: Change Line Chart marker None to circle or square to identify the tooltip marker
    def change_lineChart_marker(self,marker):
        """
        :param marker : 'Circle'
        eg: ia.change_lineChart_marker('Circle')
        @ author :Kiruthika 6June2016
        """
        self.driver.find_element_by_id("SeriesTab_tabButton").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='SeriesChartMarker']/div[2]").click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, (InfoassistLocators.marker_options.format(marker)))))
        self.driver.find_element_by_xpath(InfoassistLocators.marker_options.format(marker)).click()		

#Function 39 : verification of bar chart x and y label values- verify with order
    def verification_y_axis_legend_labels(self, label_values, text):
        """
        :param label_values: label_values = ['SALES', 'RETAIL_COST']
        :param text: step number detail
        :return:
        @author = Gobinath Thiyagarajan
        """
        get_values = self.driver.find_elements(*InfoassistLocators.legend_clip)
        runtime_values = []
        for tr in get_values:
            tds = tr.find_elements_by_tag_name('text')
            if tds:
                runtime_values.append([td.text for td in tds])
        utillity.UtillityMethods.asin(self,label_values, runtime_values, text)
        
#Function 40: Verify query pane labels and its fields
    def verification_querypane_label_and_fields(self,label,field,text,**kwargs):
        """
        :param label: 'Horizontal axis'
        :param: field: 'Product,Category'
        eg: ia.verification_querypane_label_and_fields('Horizontal axis','Product,Category',"Step10: Verify Query Pane 'Horizantal axis' has 'Product Category'")
        @author: Kiruthika 6Jun2016
        """
        a=self.driver.find_element(*InfoassistLocators.querycolumn).text
        if 'all' in kwargs:
            val = kwargs['all']
            value1='\n'.join(val)
            utillity.UtillityMethods.asin(self,value1, a,text+' %s not in %s'%(value1,a))
        else:    
            utillity.UtillityMethods.asin(self,''+label+'\n'+field+'', a, text+' %s doesnot have %s'%(label,field))

#Function 41: Verify Filter Prompt checkbox values
    def verification_filter_prompt_checkbox_values(self,field,value,text,**kwargs):
        """
        :param field: 'Product,Category' value: 'Accessories'
        eg: ia.verification_filter_prompt_checkbox_values('Product,Category','Accessories',"Step 10: Verify Filter Prompt Accessories checked", condition='notin')
        @author: Kiruthika 7Jun2016
        """
        a = self.driver.find_elements_by_xpath(InfoassistLocators.filter_prompt_checked.format(field))
        checkbox = []
        for i in range(0,len(a)):
            checkbox.append(a[i].get_attribute("value"))
        if 'condition' in kwargs:
            utillity.UtillityMethods.as_notin(self, value, checkbox, text+' %s is checked '%value)
        else:
            utillity.UtillityMethods.asin(self, value, checkbox, text + ' %s not checked ' % value) 
#Function 42: Verify grid column value
    def verification_grid_column_value(self,Values,row_num,text):
        """
        
        :param Values: $243,497,.42,$77,581.42,$165,916.00
        :param row_num: 0,1,2 (indicates row number)
        :Usgae: a=["$243,497,.42","$77,581.42","$165,916.00"]
        ia.verification_grid_column_value(a, "0","Step 04:verify column values")
        :author: Sindhuja Date: June 7
        """
        grid_row = self.driver.find_element_by_xpath("//*[contains(@class,'row"+row_num+"')]")        
        column=[]
        action=ActionChains(self.driver)
        action.move_to_element(grid_row).perform()
        values=grid_row.find_elements_by_tag_name('text')
        for result in values:
            column.append(result.text)
        utillity.UtillityMethods.asequal(self,column,Values,text)
		
#Function 43: verify bubble map legend Values
    def verifcation_bubble_map_legend(self,chart_num,legend_values,text):
        """

        :param chart_num: 1, 2, 3..(indicates chart number)
        :param legend_values: Customer Country
        :Usage: legend_values=['Customer Country']
        ia.verifcation_bubble_map_legend("2",legend_values, "Step 08: Verify label value")
        :author: Sindhuja Date: June 8
        """
        get_values = self.driver.find_elements_by_css_selector("#MAINTABLE_wbody"+chart_num+"_f > div > svg > g.legend > g > g")
        runtime_values = []

        for tr in get_values:
            tds = tr.find_elements_by_tag_name('text')
            if tds:
                runtime_values.extend([td.text for td in tds])
                print(runtime_values)
        utillity.UtillityMethods.asequal(self,runtime_values,legend_values,text)

#Function 44: Verify number of risers displayed in a chart
    def verify_number_of_riser(self,number,text):
        """
        :param: number: 2
        :param: text: "Step 10: Verify number of risers displayed"
        eg: ia.verify_number_of_riser("5","Step 10: Verify number of risers displayed")
        @author: Kiruthika 8Jun2016
        """
        a=self.driver.find_elements(*InfoassistLocators.no_of_risers)
        utillity.UtillityMethods.asequal(self,len(a),int(number),text + ' No. of Riser not equal to %s ' % number)		
		
#Function 45: Drag and Drop Visualization to required position
    def drag_and_drop_visualization(self,source_chart,target_chart, position):
        """

        :param source_chart: BubbleMap1
        :param target_chart: Grid1
        :param position: left_most,left,top_most,top,centre,bottom,bottom_most,right,right_most
        :Usage: ia.drag_and_drop_visualization("BubbleMap1","Grid1","bottom")
        :author: Sindhuja Date: June 9
        """
        action = ActionChains(self.driver)
        Source= self.driver.find_element_by_xpath(InfoassistLocators.chart_type.format(source_chart))
        Target= self.driver.find_element_by_xpath(InfoassistLocators.chart_type.format(target_chart))
        action.click_and_hold(Source)
        action.move_to_element(Target)
        if position=="left_most":
            action.release(self.driver.find_element(*InfoassistLocators.Left_most))
        if position=="left":
            action.release(self.driver.find_element(*InfoassistLocators.Left))
        if position=="top_most":
            action.release(self.driver.find_element(*InfoassistLocators.Top_most))
        if position=="top":
            action.release(self.driver.find_element(*InfoassistLocators.Top))
        if position=="centre":
            action.release(self.driver.find_element(*InfoassistLocators.Centre))
        if position=="bottom":
            action.release(self.driver.find_element(*InfoassistLocators.Bottom))
        if position=="bottom_most":
            action.release(self.driver.find_element(*InfoassistLocators.Bottom_most))
        if position=="right":
            action.release(self.driver.find_element(*InfoassistLocators.Right))
        if position=="right_most":
            action.release(self.driver.find_element(*InfoassistLocators.Right_most))
        action.perform()

# Function 46: Verify Color legend values 
    def verification_color_legend_values(self, value, text):
        """
        :param value: Color label value (legend)
        eg: ia.verification_color_legend_values(["Canada","Central","Eastern","Southern","Western"], "Step06: Verify Color Legend values"
        @author = Kiruthika 9June2016
        """
        color_text = self.driver.find_element(*InfoassistLocators.color_legend).text
        value1=''.join(value)
        utillity.UtillityMethods.asin(value1, color_text, text+' not in %s'%color_text)

#Function 47: Verify element not displayed
    def verify_riser_not_displayed(self,riser1,text,*args,**kwargs):
        """
       :param
        riser1 : s0!g0
        kwargs : type='bubble' or 'scatter' or'line' (default is bar)
        ia.verify_riser_not_displayed('s0!g22',"Step 07: verify any bubble ", type='bubble')
        ia.verify_riser_not_displayed('s0!g22',"Step 07: verify any bar ")
        ia.verify_riser_not_displayed('s0!g22!mmarker!r0!c0',"Step 07: verify any scatter value",'rowcolumn', type='scatter')
        @author : Kiruthika  9June2016
        """
        action = ActionChains(self.driver)
        mbar = 'mmarker'
        if 'type' in kwargs:
            if kwargs['type'] == 'line':
                riser = 'marker'
            if kwargs['type'] == 'bubble' or kwargs['type'] == 'scatter':
                riser = 'riser'
            if kwargs['type'] == 'heatmap':
                riser = 'riser'
                mbar = 'mbar'

        if 'type' not in kwargs:
            WebDriverWait(self.driver, 100).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "g > text[class='yaxis-title']")))
            move_element = self.driver.find_element_by_css_selector("g > text[class='yaxis-title']")
            action.move_to_element(move_element).perform()
            riser = 'riser'
            mbar = 'mbar'
        if 'rowcolumn' in args:
            try:
                bar_riser = self.driver.find_element_by_xpath(InfoassistLocators.lasso_chart_xpath_rowcolumn.format(riser, riser1))
            except NoSuchElementException:
                utillity.UtillityMethods.asequal(self,'False', 'False', text + 'Element found in Chart')
        else:
            try:
                bar_riser = self.driver.find_element_by_xpath(InfoassistLocators.lasso_chart_xpath.format(riser, riser1, mbar))
            except NoSuchElementException:
                utillity.UtillityMethods.asequal(self,'True', 'True', text + 'Element Not found in Chart')

#Function 48: Verify number of risers displayed in a chart
        
    def verify_slider_range_filter_prompts(self, promptNum, range_val, text):
        """
        :param promptNum: Prompt Number needs to be passed in 
        :param range: range ['0', '1']
        :param text:
        :return:
        __author = Gobinath Thiyagarajan
        """
        prompt = self.driver.find_elements_by_xpath(InfoassistLocators.prompts.format(promptNum))
        get_min_max = []
        for tr in prompt:   
            ranges = tr.find_elements_by_tag_name('span')
            if ranges:
                get_min_max.extend([td.text for td in ranges]) 
        utillity.UtillityMethods.asequal(self, get_min_max, range_val ,text)
        return get_min_max      
         
#Function 49 : Adjust filter prompt to start from/near some value or end to near or some value ,     
        
    def move_slider_measure(self,promptNum, **kwargs):
        """
        
        :param self: 
        :param promptNum: prompt number should be given in this format '1'
        :param kwargs: r1 = 15 , or r2 = 120 r1 moves front left to right , r2 moves end point right to left value given should be integer
         function only applicable for measure field 
        :return: 
        """ 
        
        prompt = self.driver.find_element_by_xpath(InfoassistLocators.prompts.format(promptNum))
        sliders = prompt.find_elements_by_tag_name('span')
        start_val =sliders[0].text
        end_val = sliders[1].text
        s = prompt.find_element_by_css_selector("div[id^='slider_']").find_elements_by_tag_name('a')
        if 'r1' in kwargs:
            s[0].click()
            range_end = kwargs['r1']- int(start_val) 
            page_downval = kwargs['r1']-10
            for x in range(1, 25):
                s[0].send_keys(keys.Keys.PAGE_UP)
                time.sleep(1)
                if int(sliders[0].text) in range(page_downval, kwargs['r1']):
                   start_val = sliders[0].text 
                   break     
            s2 = kwargs['r1'] - int(start_val)
            for y in range(1,s2+1):
                s[0].send_keys(keys.Keys.ARROW_RIGHT)                     
            print('moved to value %s'%(sliders[0].text))
        if 'r2' in kwargs:
            s[1].click()
            range_end = int(end_val)-kwargs['r2']  
            page_downval = kwargs['r2']+ 15
            for x in range(1, 25):
                s[1].send_keys(keys.Keys.PAGE_DOWN)
                time.sleep(1)
                if int(sliders[1].text) in range(kwargs['r2'],page_downval):
                   end_val = sliders[1].text 
                   break     
            s2 = int(end_val)- kwargs['r2'] 
            for y in range(1,s2+1):
                s[1].send_keys(keys.Keys.ARROW_LEFT)                     
            print('moved to value %s'%(sliders[1].text))  
            
            
    def move_slider_dimension_sale_month(self,promptNum, **kwargs):
        """
        
        :param self: 
        :param promptNum: prompt number should be given in this format '1'
        :param kwargs: r1 = 2 , or r2 = 6 r1 moves front left to right , r2 moves end point right to left value given should be integer
         function only applicable for measure field 
        :Usage:ia.move_slider_dimension_sale_month("1",r1=2,r2=6)
        :author: Gobinath 
        """ 
        
        prompt = self.driver.find_element_by_xpath(InfoassistLocators.prompts.format(promptNum))
        sliders = prompt.find_elements_by_tag_name('span')
        start_val =sliders[0].text
        end_val = sliders[1].text
        s = prompt.find_element_by_css_selector("div[id^='slider_']").find_elements_by_tag_name('a')
        if 'r1' in kwargs:
            s[0].click()
            s2 = kwargs['r1'] - int(start_val)
            for y in range(1,s2+1):
                s[0].send_keys(keys.Keys.ARROW_RIGHT)                     
            print('moved to value %s'%(sliders[0].text))
        if 'r2' in kwargs:
            s[1].click()   
            s2 = int(end_val)- kwargs['r2'] 
            for y in range(1,s2+1):
                s[1].send_keys(keys.Keys.ARROW_LEFT)                     
            print('moved to value %s'%(sliders[1].text))  

# Function 50: Verify x  labels of chart
    def verification_x_label(self,text, **kwargs):
        """
        :param xaxis_value: Product Category
        yaxis_value: Gross Profit
        eg: verification_x_y_label('Product Category','Gross Profit',"Step 10: Verify x,y label")
        @author = Gobinath Thiyagarajan/Kiruthika 
        """
        if 'x'in kwargs:
            xaxis = self.driver.find_element_by_xpath("//*[contains(@class,'xaxis')and contains(@class,'title')]")
            print(xaxis.text)
            utillity.UtillityMethods.asequal(self, xaxis.text, kwargs['x'], text+": X Label")
#Function 51 : Filter Prompt select dropdown Values
    def filter_prompt_select_drop_down(self,prompt_num,values):
        """

        :param prompt_num: 1,2 (indicates filter prompt number)
        :param values: United States
        :Usgae: ia.filter_prompt_select_drop_down("2", "Brazil")
        :author: Sindhuja Date: June 10
        """
        promptNum = self.driver.find_element_by_xpath("//div[contains(@id,'ar_Prompt_"+prompt_num+"')]")
        action = ActionChains(self.driver)
        action.move_to_element(promptNum).perform()
        select = Select(self.driver.find_element_by_xpath("//select[contains(@id,'combobox')]"))
        select.select_by_visible_text(values)
        			
# Function 52: Click Swap in Home Tab
    def swap(self):
        """
        eg: ia.swap()
        @author = Kiruthika 10June2016
        """
        swap = self.driver.find_element_by_xpath("//img[contains(@src, 'swap_32.png')]")
        swap.click()

    def choose_contextmenu(self, obj, item):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(
            (By.XPATH, "//div[starts-with(@id, 'BiPopup')][@class = 'bi-menu']//td[contains(text(), '" + item + "')]")))
        element = self.driver.find_elements_by_xpath("//div[starts-with(@id, 'BiPopup')][@class = 'bi-menu']//td[contains(text(), '" + item + "')]")
        x=len(element) - 1
        element[x].click()

    def datatree_field_click(self, field_name, type=0, position=1,**kwargs):
        """
        :Usage: ia.datatree_field_click('Sale,Year', type=1, position=2,opt1='Query', opt2='Vertical')
        :param: type =0 : left click, type =1 : right click
        :param: option: Position =1 : 1st selection, Position =2 is 2nd Selection
        __author = Niranjan 
        16Jun2016
        """
        
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.ID, "metaDataSearchTxtFld")))
        element = self.driver.find_element_by_id("iaMetaDataBrowser").find_element_by_id("metaDataSearchTxtFld")
        element.click()
        element.send_keys(field_name)
        if position == 1:
            xpath="//div[starts-with(@id, 'QbMetaDataTree')]//tr[contians(@class,'selected')]/td[.='" + field_name + "']/img[2]"
        else:
            xpath="//div[starts-with(@id, 'QbMetaDataTree')]//tr[(@class='')]/td[.='" + field_name + "']//img[2]"
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element1 = self.driver.find_element_by_xpath(xpath)
        try:
            element1.click()
        except ElementNotVisibleException:
            pass
        element2 = self.driver.find_element_by_xpath(xpath)
        element2.click()
        if type != 0:
            self.action.context_click(element2).perform()
            for key in kwargs:
                self.choose_contextmenu(element2, kwargs[key])
        element.clear()
        
#Function 54: Chart Minimize or Maximize or Close or Menu
    def preview_menu(self,chart_title,option):
        """
        :param: chart_title: 'Grid1'
        :param: option: 'maximize' or 'menu' or 'close' or 'restore'(minimize)
        @author : Kiruthika 13Jun2016
        """
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, (InfoassistLocators.move_to_title.format(chart_title)))))
        move = self.driver.find_element_by_xpath((InfoassistLocators.move_to_title.format(chart_title)))
        action = ActionChains(self.driver)
        action.move_to_element(move).perform()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, (InfoassistLocators.preview_menu.format(option)))))
        menu = self.driver.find_element_by_xpath((InfoassistLocators.preview_menu.format(option)))
        menu.click()
        
class AS_Ribbon(BasePage):
    def __init__(self, driver):
        super(AS_Ribbon, self).__init__(driver)

    def _validate_page(self, locator):
        self.longwait.until(EC.visibility_of_element_located(locator))
       
    def switch_as_tab(self, tab_name): 
        """
        param tab_name: 'Home' OR 'Components....
        Syntax: switch_ia_tab('Components')
        @author = Jesmin        """    
        self.driver.find_element_by_name(tab_name).click() 
        time.sleep(2)
        
    def click_ribbon_item(self,tab_name, ribbon_button_name): 
        """
        param tab_name: 'Home' OR 'Components....
        Syntax: click_ribbon_item('Components','Report')
        Param: param name must be entered as it displayed in AS (upper, lower or mixed cases
        @author = Jesmin"""       
        self.switch_as_tab(tab_name)   
        button_name = tab_name.lower() + "_" + ribbon_button_name.lower()
        self._validate_page(AsRibbonLocators.__dict__[button_name])
        self.driver.find_element(*AsRibbonLocators.__dict__[button_name]).click()
        time.sleep(3) 
        
    def click_application_menu_item(self,ribbon_button_name):  
        # NEED to test it
        button_name = ribbon_button_name.lower()
        self._validate_page(AsRibbonLocators.__dict__[button_name])
        self.driver.find_element(*AsRibbonLocators.__dict__[button_name]).click()
        time.sleep(3)
    
    def click_quick_access_toolbar_item(self,ribbon_button_name):
        # NEED to test it
        button_name = ribbon_button_name.lower()
        self._validate_page(AsRibbonLocators.__dict__[button_name])
        self.driver.find_element(*AsRibbonLocators.__dict__[button_name]).click()
        time.sleep(3)       
        
          
        
    def save_document(self,button_name,File_Name):
        self._validate_page(AsRibbonLocators.__dict__[button_name])
        self.driver.find_element(*AsRibbonLocators.__dict__[button_name]).click()
        time.sleep(3)
        
    def Verify_Tooltip(self,tab_name,component,msg,**kwargs):
        
        '''@author: Adithyaa AK : Description : To verify document canvas panel tooltips 
           ================================================================================
           Usage : as_panels_obj.Verifypanel_Tooltip('5','5','Auto Hide',"Verified - Tooltip is Auto Hide",move_x=-43,move_y=-49)'''
        
        self.switch_as_tab(tab_name) 
        time.sleep(1)
        utilobj= utillity.UtillityMethods(self.driver)
        as1 = self.driver.find_element_by_name(component)
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(as1,10,5).perform()
        time.sleep(2)
        del action
            
        if 'move_x' in kwargs:
            action = ActionChains(self.driver)
            action.move_by_offset(kwargs['move_x'], kwargs['move_y']).perform()
            time.sleep(1)
            
        tooltip=self.driver.find_element_by_class_name('tooltips_class32').get_attribute('Name')
        utilobj.asequal(tooltip,component,msg)
        del action 
        
    def Verify_Diff_Tooltip(self,tab_name,component,tooltipname,msg,**kwargs):
        
        '''@author: Adithyaa AK : Description : To verify document canvas ribbon tooltips when ribbon object name and tooltip name differs. 
           ================================================================================================================================
           Usage : as_ribbon_obj.Verify_Difftooltip('Controls','Slider','Horizontal Slider',"Step 14: Verify Generic Elements Tooltip is Grid - Insert Grid",move_x=5,move_y=5)'''
        

        self.switch_as_tab(tab_name) 
        time.sleep(1)
        utilobj= utillity.UtillityMethods(self.driver)
        as1 = self.driver.find_element_by_name(component)
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(as1,10,5).perform()
        time.sleep(2)
        del action
        
        if 'move_x' in kwargs:
            action = ActionChains(self.driver)
            action.move_by_offset(kwargs['move_x'], kwargs['move_y']).perform()
            time.sleep(1)
              
        tooltip=self.driver.find_element_by_class_name('tooltips_class32').get_attribute('Name')
        utilobj.asequal(tooltip,tooltipname,msg)
        del action  
        
        
    def Verify_Single_Tooltip(self,tab_name,component,msg,**kwargs):
        
        ''':@author: Adithyaa AK : Description : To verify AS Ribbon tooltips for Ribbon Object
        ======================================================================================
        Usage : as_ribbon_obj.Verify_Difftooltip('Slider',"Step 14: Verify Generic Elements Tooltip is Grid - Insert Grid",move_x=5,move_y=5)'''
    
#         self.driver.find_element_by_name('Home').click()
        self.switch_as_tab(tab_name) 
        utilobj= utillity.UtillityMethods(self.driver)
        as1 = self.driver.find_element_by_name(component)
        action = ActionChains(self.driver)
        action.move_to_element(as1).perform()
        time.sleep(1)
        del action
        
        if 'move_x' in kwargs:
            action = ActionChains(self.driver)
            action.move_by_offset(kwargs['move_x'], kwargs['move_y']).perform()
            time.sleep(1)
            
        tooltip=self.driver.find_element_by_class_name('tooltips_class32').get_attribute('Name')
        utilobj.asequal(tooltip,component,msg)
        del action
            
    def Verify_Singlediff_Tooltip(self,tab_name,component,tooltipname,msg,**kwargs):
        
            ''':author: Adithyaa AK : Description : To verify AS Ribbon tooltips when ribbon object name and tooltip name differs.
            =====================================================================================================================
            Usage : as_ribbon_obj.Verify_Difftooltip('Slider','Horizontal Slider',"Step 14: Verify Generic Elements Tooltip is Grid - Insert Grid",move_x=5,move_y=5)'''
            
#             self.driver.find_element_by_name('App Studio').click()
            
            self.switch_as_tab(tab_name) 
            utilobj= utillity.UtillityMethods(self.driver)
            as1 = self.driver.find_element_by_name(component)
            action = ActionChains(self.driver)
            action.move_to_element(as1).perform()
            time.sleep(1)
            del action
            
            if 'move_x' in kwargs:
                action = ActionChains(self.driver)
                action.move_by_offset(kwargs['move_x'], kwargs['move_y']).perform()
                time.sleep(1)
                
            tooltip=self.driver.find_element_by_class_name('tooltips_class32').get_attribute('Name')
            utilobj.asequal(tooltip,tooltipname,msg)
            del action
            
    def Verify_Ribbon_Checkbox(self,tab_name,component):
        
            ''':author: Adithyaa AK : Description : To verify AS Ribbon checkboxes.
            =====================================================================================================================
            Usage : as_ribbon_obj.Verify_Ribbon_Checkbox('File/Folder Properties')'''
        
            self.switch_as_tab(tab_name) 
            time.sleep(1)
            x=self.driver.find_element_by_name(component).is_selected()
            if x==True:
                print(component+'-Checked by default')
            else:
                print(component+'-Unchecked by default')
                
    def Verify_Dropdown_Tooltip(self,component,tooltip,msg,xoffset,yoffset):
        
            '''@author: Adithyaa AK : Description : To verify AS dropdown options tooltips providing direct offset x,y
            =========================================================================================================
            Usage : as_ribbon_obj.Verify_Dropdown_Tooltip('WebFOCUS Administration', 'WebFOCUS Administration Console',"Any Messages",5,20)'''
        
            utilobj= utillity.UtillityMethods(self.driver)
            self.driver.find_element_by_name(component).click()
            time.sleep(1)
            action = ActionChains(self.driver)
            action.move_by_offset(xoffset,yoffset).perform()
            time.sleep(1)
            dropdown=self.driver.find_element_by_class_name('tooltips_class32').get_attribute('Name')
            utilobj.asequal(dropdown,tooltip,msg)
            time.sleep(1)
            self.driver.find_element_by_name(component).click()
            del action
            
    def Verify_Dropdown_Tooltip_Splitbox(self,component,tooltip,msg,elem_xoffset,elem_yoffset,xoffset,yoffset):
        
            '''===========================================================================================================
            @author: Adithyaa AK : Description : To verify AS dropdown options tooltips by locating element and moving x,y
            Component : Ribbon Element Name
            Tooptip : Tooltip Name
            Msg : Print any message
            elem_xoffset : X value should to click dropdown area of element
            elem_yoffset : Y value should to click dropdown area of element
            xoffset : X value to move to dropdown option
            yoffset : y value to move to dropdown option
            Usage : as_ribbon_obj.Verify_Dropdown_Tooltip('WebFOCUS Administration', 'WebFOCUS Administration Console',"Any Messages",27,10,5,20)
            ================================================================================================================================='''
        
            utilobj= utillity.UtillityMethods(self.driver)
            action = ActionChains(self.driver)
            x=self.driver.find_element_by_name(component)
            action.move_to_element_with_offset(x,elem_xoffset,elem_yoffset).click().perform()   
            time.sleep(1)
            del action
            action = ActionChains(self.driver)
            action.move_by_offset(xoffset,yoffset).perform()
            time.sleep(1)
            dropdown=self.driver.find_element_by_class_name('tooltips_class32').get_attribute('Name')
            utilobj.asequal(dropdown,tooltip,msg)
            time.sleep(1)
            self.driver.find_element_by_name('Home').click()
            time.sleep(2)
            del action
            
    def Verify_Tab_Dropdown_Tooltip_Splitbox_Click(self,tab_name,component,tooltip,msg,elem_xoffset,elem_yoffset,xoffset,yoffset):
        
            '''===========================================================================================================
            @author: Adithyaa AK : Description : To verify AS dropdown options tooltips by locating element and moving x,y
            tab_name : Tab name to click and activate
            component : Ribbon Element Name
            Tooptip : Tooltip Name
            Msg : Print any message
            elem_xoffset : X value should to click dropdown area of element
            elem_yoffset : Y value should to click dropdown area of element
            xoffset : X value to move to dropdown option
            yoffset : y value to move to dropdown option
            Usage : as_ribbon_obj.Verify_Dropdown_Tooltip('WebFOCUS Administration', 'WebFOCUS Administration Console',"Any Messages",27,10,5,20)
            ================================================================================================================================='''
            
            self.switch_as_tab(tab_name) 
            utilobj= utillity.UtillityMethods(self.driver)
            action = ActionChains(self.driver)
            x=self.driver.find_element_by_name(component)
            action.move_to_element_with_offset(x,elem_xoffset,elem_yoffset).click().perform()   
            time.sleep(1)
            del action
            action = ActionChains(self.driver)
            action.move_by_offset(xoffset,yoffset).perform()
            time.sleep(1)
            dropdown=self.driver.find_element_by_class_name('tooltips_class32').get_attribute('Name')
            utilobj.asequal(dropdown,tooltip,msg)
            time.sleep(1)
            self.driver.find_element_by_name('Home').click()
            time.sleep(2)
            del action
            
    def Verify_Tab_Dropdown_Tooltip_Splitbox_Move(self,tab_name,component,tooltip,msg,elem_xoffset,elem_yoffset,xoffset,yoffset):
        
            '''===========================================================================================================
            @author: Adithyaa AK : Description : To verify AS dropdown options tooltips by locating element and moving x,y
            tab_name : Tab name to click and activate
            component : Ribbon Element Name to MOVE
            Tooptip : Tooltip Name
            Msg : Print any message
            elem_xoffset : X value should to click dropdown area of element
            elem_yoffset : Y value should to click dropdown area of element
            xoffset : X value to move to dropdown option
            yoffset : y value to move to dropdown option
            Usage : as_ribbon_obj.Verify_Dropdown_Tooltip('WebFOCUS Administration', 'WebFOCUS Administration Console',"Any Messages",27,10,5,20)
            ================================================================================================================================='''
            
            self.driver.find_element_by_name('Home').click()
            self.switch_as_tab(tab_name) 
            utilobj= utillity.UtillityMethods(self.driver)
            action = ActionChains(self.driver)
            x=self.driver.find_element_by_name(component)
            action.move_to_element_with_offset(x,elem_xoffset,elem_yoffset).perform()   
            time.sleep(1)
            del action
            action = ActionChains(self.driver)
            action.move_by_offset(xoffset,yoffset).perform()
            time.sleep(1)
            dropdown=self.driver.find_element_by_class_name('tooltips_class32').get_attribute('Name')
            utilobj.asequal(dropdown,tooltip,msg)
            time.sleep(2)
            del action
    
    def Click_Ribbon_Dropdown(self,tab,component,childid,dialogname,button,message,xoffset,yoffset):
        
            '''@author: Adithyaa AK : Description : To verify AS Ribbon dropdown Options.
            =================================================================================================================
            Usage : as_ribbon_obj.Click_Ribbon_Dropdown('Home','Data','1','Data Source Definition Wizard','Cancel','message',50,35):'''
        
            self.driver.find_element_by_name(tab).click()
            data=self.driver.find_element_by_name(component)
            data_button = ActionChains(self.driver)
            data_button.move_to_element_with_offset(data,20,50).click().perform()
            del data_button
            time.sleep(1)
            menu=self.driver.find_element_by_id(childid)
            toolbar = ActionChains(self.driver)
            toolbar.move_to_element_with_offset(menu,xoffset,yoffset).click().perform()
            time.sleep(5)
    
            '''Any Wizard opens'''
            booln=self.driver.find_element_by_name(dialogname).is_displayed()
            if booln==True:
                print(message)
                
            '''Click Cancel to close dialog'''
            self.driver.find_element_by_name(dialogname).find_element_by_name(button).click()
            time.sleep(5)
        
        #TODO: call Save As dialog function            
        #TODO: Check if the name already exists. If so, overwrite it. (Or am I supposed to throw an error instead?)
        #Otherwise, find name box within save screen, clear it, and enter the requested name
    '''
        if 'File_Name' in kwargs:
            pyautogui.typewrite(kwargs['File_Name'])
            time.sleep(1)
            self.driver.find_element_by_name("OK").click()
        time.sleep(1)

        try:
            self.driver.find_element_by_id("65535")
            self.driver.find_element_by_name("Yes").click()
            time.sleep(1)
        except: 
            print("Not prompted to overwrite existing HTML")   
            
        ''' 
        
    def as_menu(self,option): 
        """
        :param : option = 'open'
        :Usage: as_ribbon_obj.as_menu('save_as')
        :author: Jesmin
        :date: 04/11/17        """  
         
        opt={'open':'o', 'save':'s', 'save_as':'a','save_all':'l','run':'r','print':'close','close':'c','options':'t','exit':'x'}
        if sys.platform == 'linux':
            pykeyboard.tap_key(pykeyboard.alt_key)
            pykeyboard.tap_key(character=u'\u0066')
            pykeyboard.tap_key(pykeyboard.alt_key)
            pykeyboard.tap_key(pykeyboard.alt_key)
            pykeyboard.tap_key(character=u'\u0066')
            time.sleep(1)
            pykeyboard.type_string(str(opt[option]))
        else:
            keyboard = Controller()
            pyautogui.PAUSE = 1
            pyautogui.hotkey('alt')
            pyautogui.hotkey('f')
            pyautogui.hotkey('alt')
            #time.sleep(1)
            pyautogui.hotkey('alt')
            #time.sleep(1)
            keyboard.type("f")
            time.sleep(1)
            keyboard.type(opt[option])
        time.sleep(1)
    
    def click_by_offset(self,xoffset,yoffset):
        
        '''@author: Adithyaa AK : Description : To click on any element using offset.
        =================================================================================================================
        Usage : as_ribbon_obj.click_by_offset(self,244,40)'''
         
        action = ActionChains(self.driver)
        action.move_by_offset(xoffset,yoffset).click().perform()
        time.sleep(2)
        del action
                
        