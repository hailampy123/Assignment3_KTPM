# -*- coding: UTF-8 -*-
"""
Test create competition functionality
Version 1.1
Author Nguyen Hai Lam
"""

from testings.base_test import BaseTest
import unittest
from library import GetData
from ddt import ddt, data, unpack
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math

# Get actual DIR
CUR_DIR = os.path.dirname(os.path.abspath(__file__))

@ddt
class CreateCompetition(BaseTest):
    """Testing create competition."""
    file_path = os.path.join(CUR_DIR, '..', 'data/create_competition.xlsx')
    @data(*GetData.get_data(file_path))
    @unpack
    def test_create_competition(self, test_case, category, service, title, regulation, expect_output):
        """------------------Testing-------------------"""
        print('This is test case: ' + test_case)
        if math.isnan(category) == False:
            select1 = Select(self.driver.find_element(By.ID, "vlance_jobbundle_jobcontesttype_category"))
            select1.select_by_value(str(int(category)))
            
        if math.isnan(service) == False:
            select2 = Select(self.driver.find_element(By.ID, "vlance_jobbundle_jobcontesttype_service"))        
            select2.select_by_value(str(int(service)))
            
        if title != 'nan':
            self.driver.find_element(By.ID, "vlance_jobbundle_jobcontesttype_title").send_keys(title)
            
        if regulation != 'nan':
            self.driver.find_element(By.ID, "vlance_jobbundle_jobcontesttype_description").send_keys(regulation)
             
        self.driver.find_element(By.ID, "btn-submit-contest").submit()
        
        if math.isnan(category) == False and math.isnan(service) == False and title != 'nan' and regulation != 'nan' :
            # No error case
            error_text = 'success'
        else:
            # Error case
            error_text = self.driver.find_element(By.CSS_SELECTOR, "label.error").text
            
        self.assertEqual(error_text,expect_output)
        

if __name__ == "__main__":
    unittest.main(verbosity=2)
